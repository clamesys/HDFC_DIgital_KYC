# Data Visualization Guide
## Digital KYC: Reduce Drop-Off, Lift Conversion

This document describes all the visualizations created for the case study analysis.

---

## Visualization Files Created

### 1. **Stage Distribution Analysis** ![alt text](visualizations_creation_code/1_stage_distribution.png)
**Purpose**: Shows the volume of transactions at each stage of the KYC process.

**Key Insights**:
- Document Scan has the highest volume (140 records, 35%)
- Upload Document is second (100 records, 25%)
- Together, these two stages account for 60% of all transactions
- Indicates these are the primary bottleneck stages

**Use Case**: Include in Section 2.2 (Stage Distribution Analysis) of the case study report.

---

### 2. **Failure Rate by Stage** ![alt text](visualizations_creation_code/1_stage_distribution.png)
**Purpose**: Compares average and maximum failure percentages across all stages.

**Key Insights**:
- KYC Check has the highest average failure rate (46.8%)
- Upload Document shows the highest maximum failure rate (64.3%)
- Document Scan has moderate failure rates but highest volume
- Helps prioritize which stages need immediate attention

**Use Case**: Include in Section 2.3 (Failure Rate Analysis by Stage) of the case study report.

---

### 3. **Attempt Pattern Analysis** ![alt text](visualizations_creation_code/3_attempt_pattern_analysis.png)
**Purpose**: Dual chart showing attempt count distribution and failure rate progression.

**Key Insights**:
- 38.75% of customers require 3 attempts (155 out of 400)
- Only 3.5% reach 4th attempt (automatic rejection)
- Failure rate triples from 1st to 3rd attempt (7.7% → 33.6%)
- Shows progressive difficulty as customers retry

**Use Case**: Include in Section 2.4 (Attempt Pattern Analysis) of the case study report.

---

### 4. **Time Performance Analysis** ![alt text](visualizations_creation_code/4_time_performance_analysis.png)
**Purpose**: Shows average processing time by stage and overall time distribution.

**Key Insights**:
- 82% of transactions exceed the 20-second target
- KYC Check has the longest average time (33.2 seconds)
- Most stages exceed target significantly
- Time distribution shows wide variance in processing times

**Use Case**: Include in Section 2.5 (Time Performance Analysis) of the case study report.

---

### 5. **Error Type Distribution** ![alt text](visualizations_creation_code/5_error_type_distribution.png)
**Purpose**: Displays the top 10 most common error types encountered.

**Key Insights**:
- "Please scan the correct document" is the most common error (26%)
- Upload-related errors are second most common (14.8%)
- Duplicate KYC errors account for 4.8% of all errors
- Helps identify specific user guidance needs

**Use Case**: Include in Section 2.6 (Error Type Distribution) of the case study report.

---

### 6. **Time vs Target by Stage** ![alt text](visualizations_creation_code/6_time_vs_target_by_stage.png)
**Purpose**: Compares percentage of transactions exceeding target vs. average time as percentage of target.

**Key Insights**:
- KYC Check: 96.7% exceed target, 166% of target time
- Document Scan: 85% exceed target, 158% of target time
- All stages significantly exceed the 20-second target
- Visual comparison makes performance gaps clear

**Use Case**: Include in Section 2.5 (Time Performance Analysis) or Section 3 (Root Cause Analysis).

---

### 7. **Comprehensive Dashboard** ![alt text](visualizations_creation_code/7_comprehensive_dashboard.png)
**Purpose**: Single-page overview of all key metrics and analyses.

**Components**:
- Stage distribution (pie chart)
- Failure rate by stage (horizontal bar)
- Attempt count distribution
- Time performance box plot
- Top 5 error types
- Key metrics summary panel

**Key Insights**:
- Provides executive-level overview
- All critical metrics in one view
- Easy to understand at a glance

**Use Case**: 
- Include as a summary slide in presentations
- Use in Executive Summary section
- Reference in conclusion

---

### 8. **Customer Journey Flow** ![alt text](visualizations_creation_code/8_customer_journey_flow.png)
**Purpose**: Visual representation of success vs. failure rates at each stage of the customer journey.

**Key Insights**:
- Shows progression through stages
- Highlights where customers drop off
- Success/failure rates at each checkpoint
- Visual flow makes journey clear

**Use Case**: 
- Include in Problem Statement section
- Use in presentations to explain process
- Reference when discussing customer experience