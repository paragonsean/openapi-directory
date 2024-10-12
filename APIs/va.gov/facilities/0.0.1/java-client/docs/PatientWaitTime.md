

# PatientWaitTime

Expected wait times for new and established patients for a given health care service at VA health facilities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**established** | **BigDecimal** | Average number of days a patient who has already been to this location has to wait for a non-urgent appointment. |  [optional] |
|**_new** | **BigDecimal** | Average number of days a Veteran who hasn&#39;t been to this location has to wait for a non-urgent appointment. |  [optional] |
|**service** | [**ServiceEnum**](#ServiceEnum) | Service being offered by facility. |  |



## Enum: ServiceEnum

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



