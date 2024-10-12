

# Services

All services offered by a VA health or benefits facility grouped by service type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**benefits** | [**List&lt;BenefitsEnum&gt;**](#List&lt;BenefitsEnum&gt;) | List of benefits services for given facility. |  [optional] |
|**health** | [**List&lt;HealthEnum&gt;**](#List&lt;HealthEnum&gt;) | List of health services for given facility. |  [optional] |
|**lastUpdated** | **LocalDate** | Date of the most recent change in offered services. |  [optional] |
|**other** | [**List&lt;OtherEnum&gt;**](#List&lt;OtherEnum&gt;) | List of other services not included in one of the other service categories. |  [optional] |



## Enum: List&lt;BenefitsEnum&gt;

| Name | Value |
|---- | -----|
| APPLYING_FOR_BENEFITS | &quot;ApplyingForBenefits&quot; |
| BURIAL_CLAIM_ASSISTANCE | &quot;BurialClaimAssistance&quot; |
| DISABILITY_CLAIM_ASSISTANCE | &quot;DisabilityClaimAssistance&quot; |
| E_BENEFITS_REGISTRATION_ASSISTANCE | &quot;eBenefitsRegistrationAssistance&quot; |
| EDUCATION_AND_CAREER_COUNSELING | &quot;EducationAndCareerCounseling&quot; |
| EDUCATION_CLAIM_ASSISTANCE | &quot;EducationClaimAssistance&quot; |
| FAMILY_MEMBER_CLAIM_ASSISTANCE | &quot;FamilyMemberClaimAssistance&quot; |
| HOMELESS_ASSISTANCE | &quot;HomelessAssistance&quot; |
| INSURANCE_CLAIM_ASSISTANCE_AND_FINANCIAL_COUNSELING | &quot;InsuranceClaimAssistanceAndFinancialCounseling&quot; |
| INTEGRATED_DISABILITY_EVALUATION_SYSTEM_ASSISTANCE | &quot;IntegratedDisabilityEvaluationSystemAssistance&quot; |
| PENSIONS | &quot;Pensions&quot; |
| PRE_DISCHARGE_CLAIM_ASSISTANCE | &quot;PreDischargeClaimAssistance&quot; |
| TRANSITION_ASSISTANCE | &quot;TransitionAssistance&quot; |
| UPDATING_DIRECT_DEPOSIT_INFORMATION | &quot;UpdatingDirectDepositInformation&quot; |
| VA_HOME_LOAN_ASSISTANCE | &quot;VAHomeLoanAssistance&quot; |
| VOCATIONAL_REHABILITATION_AND_EMPLOYMENT_ASSISTANCE | &quot;VocationalRehabilitationAndEmploymentAssistance&quot; |



## Enum: List&lt;HealthEnum&gt;

| Name | Value |
|---- | -----|
| AUDIOLOGY | &quot;Audiology&quot; |
| CARDIOLOGY | &quot;Cardiology&quot; |
| CAREGIVER_SUPPORT | &quot;CaregiverSupport&quot; |
| COVID19_VACCINE | &quot;Covid19Vaccine&quot; |
| DENTAL_SERVICES | &quot;DentalServices&quot; |
| DERMATOLOGY | &quot;Dermatology&quot; |
| EMERGENCY_CARE | &quot;EmergencyCare&quot; |
| GASTROENTEROLOGY | &quot;Gastroenterology&quot; |
| GYNECOLOGY | &quot;Gynecology&quot; |
| MENTAL_HEALTH_CARE | &quot;MentalHealthCare&quot; |
| OPHTHALMOLOGY | &quot;Ophthalmology&quot; |
| OPTOMETRY | &quot;Optometry&quot; |
| ORTHOPEDICS | &quot;Orthopedics&quot; |
| NUTRITION | &quot;Nutrition&quot; |
| PODIATRY | &quot;Podiatry&quot; |
| PRIMARY_CARE | &quot;PrimaryCare&quot; |
| SPECIALTY_CARE | &quot;SpecialtyCare&quot; |
| URGENT_CARE | &quot;UrgentCare&quot; |
| UROLOGY | &quot;Urology&quot; |
| WOMENS_HEALTH | &quot;WomensHealth&quot; |



## Enum: List&lt;OtherEnum&gt;

| Name | Value |
|---- | -----|
| ONLINE_SCHEDULING | &quot;OnlineScheduling&quot; |



