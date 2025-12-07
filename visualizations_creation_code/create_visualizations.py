import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Read data
df = pd.read_excel('Digital KYC_Reduce Drop-Off_Lift Conversion.xlsx', sheet_name='Digital KYC Data Dump')
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# Convert numeric columns
df['Failure Percentage'] = pd.to_numeric(df['Failure Percentage'], errors='coerce')
df['Time Taken (in seconds)'] = pd.to_numeric(df['Time Taken (in seconds)'], errors='coerce')
df['Attempt Count'] = pd.to_numeric(df['Attempt Count'], errors='coerce')

# Create output directory
import os
os.makedirs('visualizations', exist_ok=True)

# ============================================
# 1. Stage Distribution Analysis
# ============================================
fig, ax = plt.subplots(figsize=(10, 6))
stage_counts = df['Stage Name'].value_counts()
colors = ['#10b981', '#059669', '#047857', '#065f46', '#064e3b']  # Emerald green palette
bars = ax.bar(stage_counts.index, stage_counts.values, color=colors[:len(stage_counts)])
ax.set_xlabel('Stage Name', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Records', fontsize=12, fontweight='bold')
ax.set_title('Stage Distribution Analysis', fontsize=14, fontweight='bold', pad=20)
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}\n({height/len(df)*100:.1f}%)',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('visualizations/1_stage_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================
# 2. Failure Rate by Stage
# ============================================
fig, ax = plt.subplots(figsize=(10, 6))
failure_by_stage = df.groupby('Stage Name')['Failure Percentage'].agg(['mean', 'max']).sort_values('mean', ascending=False)
x_pos = np.arange(len(failure_by_stage))
width = 0.35

bars1 = ax.bar(x_pos - width/2, failure_by_stage['mean']*100, width, 
               label='Average Failure %', color='#10b981', alpha=0.8)
bars2 = ax.bar(x_pos + width/2, failure_by_stage['max']*100, width, 
               label='Maximum Failure %', color='#059669', alpha=0.8)

ax.set_xlabel('Stage Name', fontsize=12, fontweight='bold')
ax.set_ylabel('Failure Percentage (%)', fontsize=12, fontweight='bold')
ax.set_title('Failure Rate Analysis by Stage', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(failure_by_stage.index, rotation=45, ha='right')
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/2_failure_rate_by_stage.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================
# 3. Attempt Pattern Analysis
# ============================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Attempt count distribution
attempt_counts = df['Attempt Count'].value_counts().sort_index()
colors_attempt = ['#10b981', '#059669', '#047857', '#dc2626']
bars = ax1.bar(attempt_counts.index.astype(str), attempt_counts.values, 
               color=[colors_attempt[i-1] if i <= len(colors_attempt) else '#10b981' 
                      for i in attempt_counts.index])
ax1.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax1.set_ylabel('Number of Records', fontsize=12, fontweight='bold')
ax1.set_title('Attempt Count Distribution', fontsize=14, fontweight='bold', pad=20)
ax1.grid(axis='y', alpha=0.3)

for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}\n({height/len(df)*100:.1f}%)',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

# Failure rate by attempt
failure_by_attempt = df.groupby('Attempt Count')['Failure Percentage'].agg(['mean', 'std']).sort_index()
ax2.plot(failure_by_attempt.index, failure_by_attempt['mean']*100, 
         marker='o', linewidth=3, markersize=10, color='#10b981', label='Average Failure %')
ax2.fill_between(failure_by_attempt.index, 
                 (failure_by_attempt['mean'] - failure_by_attempt['std'])*100,
                 (failure_by_attempt['mean'] + failure_by_attempt['std'])*100,
                 alpha=0.3, color='#10b981')
ax2.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax2.set_ylabel('Failure Percentage (%)', fontsize=12, fontweight='bold')
ax2.set_title('Failure Rate Progression by Attempt', fontsize=14, fontweight='bold', pad=20)
ax2.grid(alpha=0.3)
ax2.set_xticks(failure_by_attempt.index)

# Add value labels
for idx, val in enumerate(failure_by_attempt['mean']*100):
    ax2.text(failure_by_attempt.index[idx], val,
            f'{val:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/3_attempt_pattern_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================
# 4. Time Performance Analysis
# ============================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Average time by stage
time_by_stage = df.groupby('Stage Name')['Time Taken (in seconds)'].mean().sort_values(ascending=False)
colors_time = ['#dc2626' if time > 20 else '#10b981' for time in time_by_stage.values]
bars = ax1.barh(time_by_stage.index, time_by_stage.values, color=colors_time, alpha=0.8)
ax1.axvline(x=20, color='red', linestyle='--', linewidth=2, label='Target (20 seconds)')
ax1.set_xlabel('Average Time (seconds)', fontsize=12, fontweight='bold')
ax1.set_ylabel('Stage Name', fontsize=12, fontweight='bold')
ax1.set_title('Average Processing Time by Stage', fontsize=14, fontweight='bold', pad=20)
ax1.legend(fontsize=11)
ax1.grid(axis='x', alpha=0.3)

for i, (idx, val) in enumerate(time_by_stage.items()):
    ax1.text(val, i, f' {val:.1f}s', va='center', fontsize=10, fontweight='bold')

# Time distribution histogram
ax2.hist(df['Time Taken (in seconds)'], bins=20, color='#10b981', alpha=0.7, edgecolor='black')
ax2.axvline(x=20, color='red', linestyle='--', linewidth=2, label='Target (20 seconds)')
ax2.axvline(x=df['Time Taken (in seconds)'].mean(), color='blue', 
           linestyle='--', linewidth=2, label=f'Mean ({df["Time Taken (in seconds)"].mean():.1f}s)')
ax2.set_xlabel('Time Taken (seconds)', fontsize=12, fontweight='bold')
ax2.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax2.set_title('Time Distribution Across All Stages', fontsize=14, fontweight='bold', pad=20)
ax2.legend(fontsize=11)
ax2.grid(alpha=0.3)

# Add statistics text
exceeds_target = (df['Time Taken (in seconds)'] > 20).sum()
ax2.text(0.65, 0.95, f'Exceeding Target: {exceeds_target}/{len(df)} ({exceeds_target/len(df)*100:.1f}%)',
        transform=ax2.transAxes, fontsize=11, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('visualizations/4_time_performance_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================
# 5. Error Type Distribution
# ============================================
fig, ax = plt.subplots(figsize=(12, 8))
error_counts = df['Error'].value_counts().head(10)
colors_error = plt.cm.Greens(np.linspace(0.4, 0.9, len(error_counts)))
bars = ax.barh(range(len(error_counts)), error_counts.values, color=colors_error)
ax.set_yticks(range(len(error_counts)))
ax.set_yticklabels([label[:50] + '...' if len(label) > 50 else label for label in error_counts.index], fontsize=10)
ax.set_xlabel('Number of Occurrences', fontsize=12, fontweight='bold')
ax.set_title('Top 10 Error Types Distribution', fontsize=14, fontweight='bold', pad=20)
ax.grid(axis='x', alpha=0.3)

# Add value labels
for i, (idx, val) in enumerate(error_counts.items()):
    ax.text(val, i, f' {int(val)} ({val/len(df)*100:.1f}%)', 
           va='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/5_error_type_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================
# 6. Time Performance vs Target by Stage
# ============================================
fig, ax = plt.subplots(figsize=(12, 7))
stages = df['Stage Name'].unique()
exceed_percentages = []
avg_times = []

for stage in stages:
    stage_df = df[df['Stage Name'] == stage]
    exceeds = (stage_df['Time Taken (in seconds)'] > 20).sum()
    exceed_percentages.append(exceeds / len(stage_df) * 100)
    avg_times.append(stage_df['Time Taken (in seconds)'].mean())

x = np.arange(len(stages))
width = 0.35

bars1 = ax.bar(x - width/2, exceed_percentages, width, 
               label='% Exceeding 20s Target', color='#dc2626', alpha=0.8)
bars2 = ax.bar(x + width/2, [t/20*100 for t in avg_times], width, 
               label='Avg Time as % of Target', color='#10b981', alpha=0.8)

ax.set_xlabel('Stage Name', fontsize=12, fontweight='bold')
ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
ax.set_title('Time Performance vs Target by Stage', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(stages, rotation=45, ha='right')
ax.axhline(y=100, color='red', linestyle='--', linewidth=2, alpha=0.5, label='100% (Target)')
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/6_time_vs_target_by_stage.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================
# 7. Comprehensive Dashboard View
# ============================================
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# 7.1 Stage Distribution (Pie Chart)
ax1 = fig.add_subplot(gs[0, 0])
stage_counts = df['Stage Name'].value_counts()
colors_pie = ['#10b981', '#059669', '#047857', '#065f46', '#064e3b']
wedges, texts, autotexts = ax1.pie(stage_counts.values, labels=stage_counts.index, 
                                   autopct='%1.1f%%', colors=colors_pie[:len(stage_counts)],
                                   startangle=90, textprops={'fontsize': 9, 'fontweight': 'bold'})
ax1.set_title('Stage Distribution', fontsize=12, fontweight='bold', pad=10)

# 7.2 Failure Rate by Stage
ax2 = fig.add_subplot(gs[0, 1])
failure_by_stage = df.groupby('Stage Name')['Failure Percentage'].mean().sort_values(ascending=True)
bars = ax2.barh(failure_by_stage.index, failure_by_stage.values*100, color='#10b981', alpha=0.8)
ax2.set_xlabel('Avg Failure %', fontsize=10, fontweight='bold')
ax2.set_title('Average Failure Rate by Stage', fontsize=12, fontweight='bold', pad=10)
ax2.grid(axis='x', alpha=0.3)
for i, (idx, val) in enumerate(failure_by_stage.items()):
    ax2.text(val*100, i, f' {val*100:.1f}%', va='center', fontsize=9, fontweight='bold')

# 7.3 Attempt Distribution
ax3 = fig.add_subplot(gs[0, 2])
attempt_counts = df['Attempt Count'].value_counts().sort_index()
colors_attempt = ['#10b981', '#059669', '#047857', '#dc2626']
bars = ax3.bar(attempt_counts.index.astype(str), attempt_counts.values, 
               color=[colors_attempt[i-1] if i <= len(colors_attempt) else '#10b981' 
                      for i in attempt_counts.index])
ax3.set_xlabel('Attempt #', fontsize=10, fontweight='bold')
ax3.set_ylabel('Count', fontsize=10, fontweight='bold')
ax3.set_title('Attempt Count Distribution', fontsize=12, fontweight='bold', pad=10)
ax3.grid(axis='y', alpha=0.3)

# 7.4 Time Performance Box Plot
ax4 = fig.add_subplot(gs[1, :2])
time_data = [df[df['Stage Name'] == stage]['Time Taken (in seconds)'].values for stage in df['Stage Name'].unique()]
bp = ax4.boxplot(time_data, tick_labels=df['Stage Name'].unique(), patch_artist=True)
for patch in bp['boxes']:
    patch.set_facecolor('#10b981')
    patch.set_alpha(0.7)
ax4.axhline(y=20, color='red', linestyle='--', linewidth=2, label='Target (20s)')
ax4.set_ylabel('Time (seconds)', fontsize=11, fontweight='bold')
ax4.set_title('Time Distribution by Stage (Box Plot)', fontsize=12, fontweight='bold', pad=10)
ax4.legend(fontsize=10)
ax4.grid(axis='y', alpha=0.3)
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')

# 7.5 Error Types (Top 5)
ax5 = fig.add_subplot(gs[1, 2])
error_top5 = df['Error'].value_counts().head(5)
colors_error = plt.cm.Greens(np.linspace(0.4, 0.9, len(error_top5)))
bars = ax5.barh(range(len(error_top5)), error_top5.values, color=colors_error)
ax5.set_yticks(range(len(error_top5)))
ax5.set_yticklabels([label[:30] + '...' if len(label) > 30 else label for label in error_top5.index], fontsize=8)
ax5.set_xlabel('Count', fontsize=10, fontweight='bold')
ax5.set_title('Top 5 Error Types', fontsize=12, fontweight='bold', pad=10)
ax5.grid(axis='x', alpha=0.3)

# 7.6 Key Metrics Summary
ax6 = fig.add_subplot(gs[2, :])
ax6.axis('off')

# Calculate key metrics
total_records = len(df)
rejection_rate = (df['Attempt Count'] == 4).sum() / total_records * 100
exceeds_target = (df['Time Taken (in seconds)'] > 20).sum() / total_records * 100
avg_time = df['Time Taken (in seconds)'].mean()
duplicate_rate = df['Error'].str.contains('already exists', na=False).sum() / total_records * 100
first_attempt_success = (df['Attempt Count'] == 1).sum() / total_records * 100

metrics_text = f"""
KEY PERFORMANCE METRICS SUMMARY

Total Records Analyzed: {total_records:,}
Overall Rejection Rate: {rejection_rate:.2f}% (Target: <1%)
Transactions Exceeding 20s Target: {exceeds_target:.1f}% (Target: <20%)
Average Processing Time: {avg_time:.1f} seconds (Target: <18s)
Duplicate KYC Rate: {duplicate_rate:.2f}% (Target: <1%)
First Attempt Success Rate: {first_attempt_success:.1f}% (Target: >95%)
"""

ax6.text(0.1, 0.5, metrics_text, fontsize=12, fontweight='bold',
        verticalalignment='center', family='monospace',
        bbox=dict(boxstyle='round', facecolor='#f0f9ff', alpha=0.8, edgecolor='#10b981', linewidth=2))

fig.suptitle('Digital KYC Process - Comprehensive Analysis Dashboard', 
            fontsize=16, fontweight='bold', y=0.98)

plt.savefig('visualizations/7_comprehensive_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

# ============================================
# 8. Customer Journey Flow
# ============================================
fig, ax = plt.subplots(figsize=(14, 8))

# Calculate success/failure rates for each stage
stages_ordered = ['Select Document Type', 'Document Scan', 'Upload Document', 'KYC Check', 'KYC Approved']
stage_stats = {}

for stage in stages_ordered:
    stage_df = df[df['Stage Name'] == stage]
    total = len(stage_df)
    if total > 0:
        success = (stage_df['Failure Percentage'] == 0).sum()
        failure = total - success
        stage_stats[stage] = {
            'total': total,
            'success': success,
            'failure': failure,
            'success_rate': success/total*100,
            'failure_rate': failure/total*100
        }

# Create flow diagram
y_positions = np.linspace(0.9, 0.1, len(stages_ordered))
box_width = 0.15
box_height = 0.08

for i, stage in enumerate(stages_ordered):
    if stage in stage_stats:
        stats = stage_stats[stage]
        # Success box (green)
        rect_success = Rectangle((0.3, y_positions[i] - box_height/2), box_width, box_height,
                                 facecolor='#10b981', edgecolor='black', linewidth=2)
        ax.add_patch(rect_success)
        ax.text(0.3 + box_width/2, y_positions[i], 
               f'Success\n{stats["success"]} ({stats["success_rate"]:.1f}%)',
               ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        
        # Failure box (red)
        rect_failure = Rectangle((0.5, y_positions[i] - box_height/2), box_width, box_height,
                                facecolor='#dc2626', edgecolor='black', linewidth=2)
        ax.add_patch(rect_failure)
        ax.text(0.5 + box_width/2, y_positions[i],
               f'Failure\n{stats["failure"]} ({stats["failure_rate"]:.1f}%)',
               ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        
        # Stage label
        ax.text(0.15, y_positions[i], stage, ha='right', va='center',
               fontsize=11, fontweight='bold')
        
        # Draw arrows between stages
        if i < len(stages_ordered) - 1:
            ax.arrow(0.3 + box_width/2, y_positions[i] - box_height/2 - 0.02,
                   0, -(y_positions[i] - y_positions[i+1] - box_height - 0.04),
                   head_width=0.02, head_length=0.01, fc='#10b981', ec='#10b981', linewidth=2)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Customer Journey Flow - Success vs Failure at Each Stage', 
            fontsize=14, fontweight='bold', pad=20)

plt.savefig('visualizations/8_customer_journey_flow.png', dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations created successfully!")
print("Files saved in 'visualizations' folder:")
print("1. 1_stage_distribution.png")
print("2. 2_failure_rate_by_stage.png")
print("3. 3_attempt_pattern_analysis.png")
print("4. 4_time_performance_analysis.png")
print("5. 5_error_type_distribution.png")
print("6. 6_time_vs_target_by_stage.png")
print("7. 7_comprehensive_dashboard.png")
print("8. 8_customer_journey_flow.png")

