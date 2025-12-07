# Digital KYC: Reduce Drop-Off, Lift Conversion
## Case Study & Analysis Report

---

## Executive Summary

This case study analyzes the digital KYC (Know Your Customer) onboarding process implemented by a leading bank. The analysis reveals significant drop-off rates across multiple stages of the KYC process, with 82% of transactions exceeding the target response time of 15-20 seconds. The study identifies key pain points, root causes, and provides actionable recommendations to reduce abandonment rates, improve turnaround time, enhance user experience, and minimize re-submissions.

![Comprehensive Dashboard](visualizations_creation_code/7_comprehensive_dashboard.png)
*Figure 0: Comprehensive Analysis Dashboard - Overview of all key metrics*

**Key Findings:**
- Overall rejection rate: 3.5% (14 customers reaching 4th attempt)
- 82% of transactions exceed 20-second target response time
- Document Scan stage has highest failure rate (35% as per problem statement)
- KYC Check stage shows highest average failure percentage (46.8%)
- 4.75% of transactions involve duplicate KYC documents
- Failure rates increase significantly with each attempt (7.7% → 23.6% → 33.6%)

---

## 1. Problem Statement

### 1.1 Background
The bank has introduced a new digital KYC process to onboard new customers through a mobile application. The process involves multiple stages where customers must:
1. Select document type (Aadhaar Card, PAN Card, Voter ID, Passport, etc.)
2. Scan the selected document
3. Upload the document for server validation
4. Scan and upload a photograph
5. Upload a real-time photograph for verification

![Customer Journey Flow](visualizations_creation_code/8_customer_journey_flow.png)
*Figure: Customer Journey Flow - Success vs. failure rates at each stage*

### 1.2 Current Challenges
Since go-live, the bank has been experiencing:
- **High rejection rates** in the KYC process
- **Poor response times** exceeding the ideal 15-20 seconds per step
- **Customer frustration** leading to abandonment
- **High client turnover** due to failed KYC attempts

### 1.3 Known Issues
1. **Duplicate KYC**: Documents already existing in the database
2. **High server response time**: Process taking longer than 15-20 seconds
3. **Improper document scanning**: Customers struggling with document capture
4. **Attempt limit**: Customers reaching 4th attempt get automatically rejected

---

## 2. Data Analysis & Findings

### 2.1 Dataset Overview
- **Total Records Analyzed**: 400 KYC transaction records
- **Data Period**: Transaction-level data across all KYC stages
- **Key Metrics Tracked**: Stage name, attempt count, failure percentage, time taken, error messages

### 2.2 Stage Distribution Analysis

| Stage Name | Number of Records | Percentage |
|------------|------------------|------------|
| Document Scan | 140 | 35.0% |
| Upload Document | 100 | 25.0% |
| KYC Check | 60 | 15.0% |
| Select Document Type | 60 | 15.0% |
| KYC Approved | 40 | 10.0% |

**Insight**: Document Scan and Upload Document stages account for 60% of all transaction records, indicating these are the primary bottleneck stages.

![Stage Distribution Analysis](visualizations_creation_code/1_stage_distribution.png)
*Figure 1: Stage Distribution Analysis - Volume of transactions at each KYC stage*

### 2.3 Failure Rate Analysis by Stage

| Stage Name | Average Failure % | Maximum Failure % | Criticality |
|------------|-------------------|-------------------|-------------|
| KYC Check | 46.8% | 60.0% | **CRITICAL** |
| Upload Document | 24.2% | 64.3% | **HIGH** |
| Document Scan | 22.1% | 30.0% | **HIGH** |
| Select Document Type | 11.4% | 20.0% | Medium |
| KYC Approved | 6.2% | 15.0% | Low |

**Key Finding**: While Document Scan has the highest volume of failures (35% as per problem statement), KYC Check stage has the highest average failure percentage (46.8%), indicating systemic issues in document validation.

![Failure Rate by Stage](visualizations_creation_code/2_failure_rate_by_stage.png)
*Figure 2: Failure Rate Analysis by Stage - Average and maximum failure percentages*

### 2.4 Attempt Pattern Analysis

| Attempt Number | Number of Records | Average Failure % | Trend |
|----------------|------------------|-------------------|-------|
| 1st Attempt | 112 | 7.7% | Low |
| 2nd Attempt | 119 | 23.6% | Moderate |
| 3rd Attempt | 155 | 33.6% | High |
| 4th Attempt | 14 | 26.7% | **REJECTED** |

**Critical Insight**: 
- 38.75% of customers require 3 attempts (155 out of 400)
- 3.5% of customers reach 4th attempt and are automatically rejected
- Failure rate triples from 1st to 3rd attempt (7.7% → 33.6%)

![Attempt Pattern Analysis](visualizations_creation_code/3_attempt_pattern_analysis.png)
*Figure 3: Attempt Pattern Analysis - Distribution and failure rate progression*

### 2.5 Time Performance Analysis

**Target Performance**: ≤ 20 seconds per step

| Metric | Value |
|--------|-------|
| Records exceeding target | 328 out of 400 |
| Percentage exceeding target | **82.0%** |
| Average time across all stages | 30.3 seconds |

**Time Performance by Stage:**

| Stage Name | Average Time | % Exceeding 20s | Status |
|------------|--------------|-----------------|--------|
| KYC Check | 33.2 seconds | 96.7% | **CRITICAL** |
| Document Scan | 31.6 seconds | 85.0% | **CRITICAL** |
| Select Document Type | 30.4 seconds | 78.3% | **HIGH** |
| KYC Approved | 27.6 seconds | 80.0% | **HIGH** |
| Upload Document | 27.6 seconds | 72.0% | **HIGH** |

**Critical Finding**: 96.7% of KYC Check operations exceed the 20-second target, with an average time of 33.2 seconds - 66% above target.

![Time Performance Analysis](visualizations_creation_code/4_time_performance_analysis.png)
*Figure 4: Time Performance Analysis - Average time by stage and overall distribution*

![Time vs Target by Stage](visualizations_creation_code/6_time_vs_target_by_stage.png)
*Figure 5: Time Performance vs Target - Percentage exceeding 20s target by stage*

### 2.6 Error Type Distribution

| Error Type | Count | Percentage |
|------------|-------|------------|
| Please scan the correct document | 104 | 26.0% |
| Please upload the correct selected document | 59 | 14.8% |
| KYC Successful | 40 | 10.0% |
| Please select correct document type | 39 | 9.8% |
| Proceed to Document Upload | 36 | 9.0% |
| KYC data not found; please upload correct KYC | 34 | 8.5% |
| Upload the Selected Document | 32 | 8.0% |
| **KYC document already exists** | 19 | 4.8% |
| Select Document Type - PAN/ Aadhar/ Voter | 16 | 4.0% |
| Maximum tries exceeded | 9 | 2.3% |
| KYC check in progress please wait | 7 | 1.8% |
| Maximum upload tries exceeded | 5 | 1.3% |

**Key Insights**:
- 26% of errors relate to improper document scanning
- 4.8% involve duplicate KYC documents (systematic issue)
- 2.3% result in automatic rejection (maximum tries exceeded)

![Error Type Distribution](visualizations_creation_code/5_error_type_distribution.png)
*Figure 6: Error Type Distribution - Top 10 most common error types*

### 2.7 Duplicate KYC Analysis

- **Total Duplicate Instances**: 19 out of 400 records
- **Duplicate Rate**: 4.75%
- **Impact**: These represent systematic failures where customers are attempting to use documents already registered in the system

### 2.8 Customer Rejection Analysis

- **Total Rejections**: 14 customers (3.5% rejection rate)
- **Rejection Breakdown**:
  - Upload Document stage: 9 rejections (64.3%)
  - Select Document Type stage: 5 rejections (35.7%)

**Critical Finding**: 64% of rejections occur at the Upload Document stage, indicating this is a critical failure point.

---

## 3. Root Cause Analysis

### 3.1 Primary Root Causes

#### 3.1.1 Server Performance Issues (CRITICAL)
- **Evidence**: 82% of transactions exceed 20-second target
- **Impact**: Customer frustration, abandonment, perception of system failure
- **Root Cause**: 
  - Inadequate server infrastructure
  - Inefficient document processing algorithms
  - Lack of load balancing during peak times
  - Database query optimization issues

#### 3.1.2 Document Scanning Challenges (HIGH)
- **Evidence**: 26% of errors are "Please scan the correct document"
- **Impact**: Highest failure volume (35% as per problem statement)
- **Root Cause**:
  - Poor user guidance on how to scan documents
  - Lack of real-time feedback during scanning
  - Insufficient image quality validation before upload
  - No preview/edit capability before submission

#### 3.1.3 KYC Validation System Issues (CRITICAL)
- **Evidence**: 46.8% average failure rate at KYC Check stage, 96.7% exceed time target
- **Impact**: Highest failure percentage, longest processing times
- **Root Cause**:
  - Inefficient OCR (Optical Character Recognition) processing
  - Complex validation rules causing false negatives
  - Lack of duplicate detection before submission
  - Sequential processing instead of parallel processing

#### 3.1.4 Duplicate Document Management (HIGH)
- **Evidence**: 4.75% duplicate KYC instances
- **Impact**: Automatic rejection, customer frustration
- **Root Cause**:
  - No upfront duplicate checking
  - Customers unaware their document is already registered
  - Lack of clear messaging about document eligibility

#### 3.1.5 User Experience & Guidance Issues (MEDIUM)
- **Evidence**: Progressive failure rates (7.7% → 33.6% across attempts)
- **Impact**: Customers making repeated mistakes
- **Root Cause**:
  - Unclear error messages
  - Lack of visual guidance
  - No step-by-step tutorials
  - Insufficient real-time validation feedback

#### 3.1.6 Upload Process Issues (HIGH)
- **Evidence**: 24.2% average failure rate, 64% of rejections occur here
- **Impact**: Highest rejection concentration
- **Root Cause**:
  - File size/format restrictions not clearly communicated
  - Network timeout issues
  - Lack of upload progress indicators
  - No retry mechanism for failed uploads

---

## 4. Recommendations

### 4.1 Immediate Actions (Quick Wins - 0-3 months)

#### 4.1.1 Enhance User Guidance & Real-Time Feedback
**Objective**: Reduce Document Scan failures from 35% to <20%

**Actions**:
- Implement real-time document quality validation during scanning
- Add visual overlays showing correct document positioning
- Provide instant feedback on image quality (blur, lighting, completeness)
- Include step-by-step video tutorials within the app
- Add "Try Again" option with specific guidance on what went wrong

**Expected Impact**: 
- Reduce Document Scan failures by 40-50%
- Improve first-attempt success rate from 92.3% to 95%+

#### 4.1.2 Improve Error Messages
**Objective**: Help customers understand and fix issues faster

**Actions**:
- Replace generic errors with specific, actionable messages
- Add visual examples of correct vs. incorrect submissions
- Include direct links to help/support at error points
- Provide estimated time for resolution

**Expected Impact**: Reduce re-submissions by 30-40%

#### 4.1.3 Implement Duplicate Detection Upfront
**Objective**: Prevent duplicate KYC submissions before processing

**Actions**:
- Add duplicate check before document upload
- Display clear message if document already exists
- Provide alternative options (use existing KYC, contact support)
- Implement document number pre-validation

**Expected Impact**: 
- Eliminate 4.75% duplicate KYC errors
- Reduce unnecessary processing load

### 4.2 Short-Term Improvements (3-6 months)

#### 4.2.1 Server Infrastructure Optimization
**Objective**: Reduce processing time to meet 15-20 second target

**Actions**:
- Implement load balancing and auto-scaling
- Optimize database queries and indexing
- Implement caching for frequently accessed data
- Upgrade server capacity for peak loads
- Implement parallel processing for document validation

**Expected Impact**:
- Reduce average processing time from 30.3s to <18s
- Reduce transactions exceeding target from 82% to <20%
- Improve KYC Check time from 33.2s to <18s

#### 4.2.2 Enhanced Document Processing
**Objective**: Improve OCR accuracy and validation speed

**Actions**:
- Upgrade OCR engine with better accuracy
- Implement machine learning for document validation
- Add pre-processing image enhancement
- Implement batch processing for multiple validations
- Add confidence scoring for validation results

**Expected Impact**:
- Reduce KYC Check failure rate from 46.8% to <25%
- Improve processing speed by 40-50%

#### 4.2.3 Upload Process Optimization
**Objective**: Reduce Upload Document failures and rejections

**Actions**:
- Implement chunked upload for large files
- Add upload progress indicators with time estimates
- Implement automatic retry mechanism for failed uploads
- Add file compression before upload
- Implement resume capability for interrupted uploads

**Expected Impact**:
- Reduce Upload Document failure rate from 24.2% to <15%
- Reduce rejection rate at this stage from 64% to <30%

### 4.3 Medium-Term Enhancements (6-12 months)

#### 4.3.1 Advanced User Experience Features
**Objective**: Reduce overall drop-off rate and improve conversion

**Actions**:
- Implement save & resume functionality
- Add multi-language support
- Implement offline mode for document capture
- Add biometric verification options
- Implement AI-powered document auto-cropping and enhancement

**Expected Impact**:
- Reduce overall drop-off rate by 50-60%
- Improve customer satisfaction scores

#### 4.3.2 Predictive Analytics & Proactive Support
**Objective**: Identify and assist at-risk customers early

**Actions**:
- Implement real-time analytics dashboard
- Add predictive models to identify likely failures
- Provide proactive chat support at critical stages
- Implement smart retry suggestions based on error patterns
- Add customer journey analytics

**Expected Impact**:
- Reduce 3rd attempt rate from 38.75% to <20%
- Reduce rejection rate from 3.5% to <1%

#### 4.3.3 Process Redesign
**Objective**: Streamline the KYC process flow

**Actions**:
- Combine document selection and scanning into single step
- Implement parallel processing for photo and document upload
- Add pre-validation before final submission
- Implement smart defaults based on customer profile
- Reduce total number of steps from 5 to 3-4

**Expected Impact**:
- Reduce total process time by 30-40%
- Improve completion rate by 25-35%

---

## 5. Expected Outcomes & Impact

### 5.1 Quantitative Improvements

| Metric | Current State | Target State | Improvement |
|--------|---------------|--------------|-------------|
| Overall Drop-Off Rate | 3.5% rejection | <1% rejection | **71% reduction** |
| Document Scan Failure | 35% | <20% | **43% reduction** |
| KYC Check Failure | 46.8% | <25% | **47% reduction** |
| Average Processing Time | 30.3 seconds | <18 seconds | **41% reduction** |
| Transactions Exceeding 20s | 82% | <20% | **76% reduction** |
| Duplicate KYC Rate | 4.75% | <1% | **79% reduction** |
| 3rd Attempt Rate | 38.75% | <20% | **48% reduction** |
| First Attempt Success | 92.3% | 95%+ | **3% improvement** |

### 5.2 Qualitative Improvements

1. **Customer Experience**:
   - Clearer guidance reduces frustration
   - Faster processing improves satisfaction
   - Better error messages enable self-service resolution

2. **Operational Efficiency**:
   - Reduced support ticket volume
   - Lower processing costs per KYC
   - Improved system reliability

3. **Business Impact**:
   - Higher customer acquisition rate
   - Reduced customer churn
   - Improved brand perception
   - Faster time-to-onboard

### 5.3 ROI Estimation

**Assumptions**:
- Average cost per KYC processing: ₹50
- Average customer lifetime value: ₹5,000
- Current monthly KYC applications: 10,000
- Support cost per failed KYC: ₹200

**Current Monthly Costs**:
- Processing costs: ₹500,000 (10,000 × ₹50)
- Failed KYC costs: ₹175,000 (3.5% × 10,000 × ₹200)
- Lost revenue: ₹1,750,000 (3.5% × 10,000 × ₹5,000)
- **Total Monthly Impact**: ₹2,425,000

**Projected Monthly Savings (after improvements)**:
- Reduced processing costs: ₹50,000 (faster processing)
- Reduced failed KYC costs: ₹50,000 (1% rejection rate)
- Recovered revenue: ₹1,250,000 (2.5% additional conversions)
- **Total Monthly Benefit**: ₹1,350,000

**Annual ROI**: ₹16,200,000 in benefits

---

## 6. Implementation Roadmap

### Phase 1: Quick Wins (Months 1-3)
- Week 1-2: Error message improvements
- Week 3-4: User guidance enhancements
- Week 5-8: Duplicate detection implementation
- Week 9-12: Real-time feedback features

**Budget**: ₹5,00,000
**Expected Impact**: 20-30% improvement in key metrics

### Phase 2: Infrastructure (Months 4-6)
- Month 4: Server capacity upgrade
- Month 5: Database optimization
- Month 6: Load balancing implementation

**Budget**: ₹15,00,000
**Expected Impact**: 40-50% reduction in processing time

### Phase 3: Advanced Features (Months 7-12)
- Months 7-9: OCR upgrade and ML implementation
- Months 10-12: Process redesign and UX enhancements

**Budget**: ₹25,00,000
**Expected Impact**: 50-60% overall improvement

**Total Investment**: ₹45,00,000
**Expected Payback Period**: 3-4 months

---

## 7. Success Metrics & KPIs

### 7.1 Primary KPIs
1. **Drop-Off Rate**: Target <1% (from 3.5%)
2. **Average Processing Time**: Target <18 seconds (from 30.3s)
3. **First Attempt Success Rate**: Target 95%+ (from 92.3%)
4. **Customer Satisfaction Score**: Target 4.5/5.0

### 7.2 Secondary KPIs
1. **Stage-wise Failure Rates**: All stages <20%
2. **Time Target Compliance**: >80% transactions <20 seconds
3. **Duplicate KYC Rate**: <1%
4. **Support Ticket Volume**: 50% reduction

### 7.3 Monitoring Dashboard
- Real-time transaction monitoring
- Stage-wise performance metrics
- Error type distribution
- Customer journey analytics
- Time performance tracking

---

## 8. Risk Mitigation

### 8.1 Implementation Risks
1. **Technical Complexity**: Mitigate with phased approach and proof-of-concept
2. **User Adoption**: Mitigate with comprehensive training and communication
3. **System Downtime**: Mitigate with gradual rollout and rollback plans
4. **Budget Overruns**: Mitigate with clear scope definition and regular reviews

### 8.2 Operational Risks
1. **Increased Load**: Mitigate with capacity planning and auto-scaling
2. **Data Security**: Mitigate with encryption and compliance checks
3. **Regulatory Changes**: Mitigate with flexible architecture

---

## 9. Conclusion

The digital KYC process, while innovative, faces significant challenges that impact customer experience and business outcomes. Through comprehensive data analysis, this study has identified critical pain points:

1. **Server performance** causing 82% of transactions to exceed time targets
2. **Document scanning issues** accounting for 35% of failures
3. **KYC validation problems** with 46.8% failure rate
4. **Duplicate document management** affecting 4.75% of customers
5. **Poor user guidance** leading to progressive failure rates

The recommended solutions, implemented in phases, can deliver:
- **71% reduction** in drop-off rate
- **41% reduction** in processing time
- **47% reduction** in KYC Check failures
- **₹16.2 million** annual benefit

With proper implementation and monitoring, the bank can transform its digital KYC process into a competitive advantage, improving customer acquisition, satisfaction, and operational efficiency.

---

## 10. Appendices

### Appendix A: Data Summary Statistics
- Total Records: 400
- Date Range: [To be filled based on actual data]
- Data Source: Digital KYC Transaction Database

### Appendix B: Methodology
- Data extraction from Excel database
- Statistical analysis using Python/pandas
- Root cause analysis using 5-Why technique
- Recommendations based on industry best practices

### Appendix C: References
- Digital KYC Guidelines - RBI Regulations
- Industry Benchmarks for KYC Processing
- Best Practices in Digital Onboarding

---

**Report Prepared By**: Debayangshu Sen
**Id Number**: DT.13