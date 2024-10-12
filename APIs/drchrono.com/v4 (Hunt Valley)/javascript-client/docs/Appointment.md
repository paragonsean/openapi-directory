# OpenapiJsClient.Appointment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowOverlapping** | **Boolean** | Bypass overlap check. | [optional] 
**apptIsBreak** | **Boolean** |  | [optional] 
**baseRecurringAppointment** | **String** | ID of base appointment of a recurrign series | [optional] [readonly] 
**billingNotes** | [**[ClaimBillingNotes1]**](ClaimBillingNotes1.md) | Billing notes of the appointment. For writing, check &#x60;/api/claim_billing_notes&#x60; | [optional] [readonly] 
**billingProvider** | **String** |  | [optional] [readonly] 
**billingStatus** | **String** | Should be one of &#x60;Auto Accident Claim&#x60;, &#x60;Balance Due&#x60;, &#x60;Bill Insurance&#x60;, &#x60;Bill Secondary Insurance&#x60;, &#x60;Durable Medical Equipment Claim&#x60;, &#x60;Internal Review&#x60;, &#x60;Paid In Full&#x60;, &#x60;Settled&#x60;, &#x60;Worker&#39;s Comp Claim&#x60; or one of the custom billing status | [optional] 
**clinicalNote** | [**ClinicalNote1**](ClinicalNote1.md) |  | [optional] 
**clonedFrom** | **Number** | ID of the original appointment which this appointment cloned from. Will be null if the appointment is not cloned. | [optional] 
**color** | **String** |  | [optional] 
**createdAt** | **String** |  | [optional] [readonly] 
**customFields** | [**[CustomAppointmentFieldValue]**](CustomAppointmentFieldValue.md) | Custom appointment fields | [optional] 
**customVitals** | [**[CustomVitalValue]**](CustomVitalValue.md) | Custom vitals associated with this appointment. | [optional] 
**deletedFlag** | **Boolean** | Whether the appointmetn is deleted. | [optional] [readonly] 
**doctor** | **Number** | Doctor ID | 
**duration** | **Number** | Length of the appointment in minutes. Optional if &#x60;profile&#x60; is provided. | [optional] 
**examRoom** | **Number** | Index of the exam room that this appointment occurs in. See &#x60;/api/offices&#x60; | 
**extendedUpdatedAt** | **String** | The most recent update time among appointment itself, its vitals and its custom vitals | [optional] [readonly] 
**firstBilledDate** | **String** |  | [optional] [readonly] 
**icd10Codes** | **[String]** |  | [optional] 
**icd9Codes** | **[String]** |  | [optional] 
**id** | **String** | Unique identifier. Usually numeric, but not always | [optional] [readonly] 
**ins1Status** | **String** | Billing status of primary insurer | [optional] [readonly] 
**ins2Status** | **String** | Billing status of secondary insurer | [optional] [readonly] 
**isVirtualBase** | **Boolean** |  | [optional] [readonly] 
**isWalkIn** | **Boolean** | Whether the appointment is a walk-in appointment | [optional] 
**lastBilledDate** | **String** |  | [optional] [readonly] 
**notes** | **String** |  | [optional] 
**office** | **Number** | Office ID | 
**patient** | **Number** | ID of this appointment&#39;s patient. Breaks have a null patient field. | 
**primaryInsuranceIdNumber** | **String** |  | [optional] [readonly] 
**primaryInsurerName** | **String** |  | [optional] [readonly] 
**primaryInsurerPayerId** | **String** |  | [optional] [readonly] 
**profile** | **Number** | ID of an &#x60;/api/appointment_profiles&#x60; instance. The profile sets default values for &#x60;color&#x60;, &#x60;duration&#x60;, and &#x60;reason&#x60; on creation, which can be overriden by setting these values explicitly. | [optional] 
**reason** | **String** | Default to &#x60;\&quot;\&quot;&#x60; | [optional] 
**recurringAppointment** | **Boolean** | Whether the appointment is a recurring appointment or not | [optional] [readonly] 
**reminderProfile** | **String** | Write-only. ID of an &#x60;/api/reminder_profiles&#x60; instance. Set this to apply a reminder profile to the appointment. Cannot be applied to an appointment with reminders. | [optional] 
**reminders** | [**[SimpleReminder]**](SimpleReminder.md) | Scheduled reminders of the appointment | [optional] [readonly] 
**scheduledTime** | **String** | The starting time of the appointment | 
**secondaryInsuranceIdNumber** | **String** |  | [optional] [readonly] 
**secondaryInsurerName** | **String** |  | [optional] [readonly] 
**secondaryInsurerPayerId** | **String** |  | [optional] [readonly] 
**status** | **String** | One of &#x60;&#x60;, &#x60;Arrived&#x60;, &#x60;Checked In&#x60;, &#x60;In Room&#x60;, &#x60;Cancelled&#x60;, &#x60;Complete&#x60;, &#x60;Confirmed&#x60;, &#x60;In Session&#x60;, &#x60;No Show&#x60;, &#x60;Not Confirmed&#x60;, or &#x60;Rescheduled&#x60;. Or one of the custom statuses. | [optional] 
**statusTransitions** | [**[AppointmentStatusTransition]**](AppointmentStatusTransition.md) |  | [optional] [readonly] 
**supervisingProvider** | **String** | Supervising provider of appointment if set. | [optional] [readonly] 
**updatedAt** | **String** |  | [optional] [readonly] 
**vitals** | [**SystemVitals**](SystemVitals.md) |  | [optional] 



## Enum: Ins1StatusEnum


* `empty` (value: `""`)

* `Incomplete Information` (value: `"Incomplete Information"`)

* `In Process Emdeon` (value: `"In Process Emdeon"`)

* `Rejected Emdeon` (value: `"Rejected Emdeon"`)

* `Rejected Jopari` (value: `"Rejected Jopari"`)

* `In Process Payor` (value: `"In Process Payor"`)

* `Rejected Waystar Professional` (value: `"Rejected Waystar Professional"`)

* `Rejected Waystar Institutional` (value: `"Rejected Waystar Institutional"`)

* `In Process Payer` (value: `"In Process Payer"`)

* `Payer Acknowledged` (value: `"Payer Acknowledged"`)

* `Rejected Payor` (value: `"Rejected Payor"`)

* `Rejected Payer` (value: `"Rejected Payer"`)

* `Paid in Full` (value: `"Paid in Full"`)

* `Partially Paid` (value: `"Partially Paid"`)

* `Coordination of Benefits` (value: `"Coordination of Benefits"`)

* `ERA Received` (value: `"ERA Received"`)

* `ERA Denied` (value: `"ERA Denied"`)

* `HCFA Form Faxed` (value: `"HCFA Form Faxed"`)





## Enum: Ins2StatusEnum


* `empty` (value: `""`)

* `Incomplete Information` (value: `"Incomplete Information"`)

* `In Process Emdeon` (value: `"In Process Emdeon"`)

* `Rejected Emdeon` (value: `"Rejected Emdeon"`)

* `Rejected Jopari` (value: `"Rejected Jopari"`)

* `In Process Payor` (value: `"In Process Payor"`)

* `Rejected Waystar Professional` (value: `"Rejected Waystar Professional"`)

* `Rejected Waystar Institutional` (value: `"Rejected Waystar Institutional"`)

* `In Process Payer` (value: `"In Process Payer"`)

* `Payer Acknowledged` (value: `"Payer Acknowledged"`)

* `Rejected Payor` (value: `"Rejected Payor"`)

* `Rejected Payer` (value: `"Rejected Payer"`)

* `Paid in Full` (value: `"Paid in Full"`)

* `Partially Paid` (value: `"Partially Paid"`)

* `Coordination of Benefits` (value: `"Coordination of Benefits"`)

* `ERA Received` (value: `"ERA Received"`)

* `ERA Denied` (value: `"ERA Denied"`)

* `HCFA Form Faxed` (value: `"HCFA Form Faxed"`)





## Enum: StatusEnum


* `empty` (value: `""`)

* `Arrived` (value: `"Arrived"`)

* `Checked In` (value: `"Checked In"`)

* `Checked In Online` (value: `"Checked In Online"`)

* `In Room` (value: `"In Room"`)

* `In Session` (value: `"In Session"`)

* `Complete` (value: `"Complete"`)

* `Confirmed` (value: `"Confirmed"`)

* `Not Confirmed` (value: `"Not Confirmed"`)

* `Rescheduled` (value: `"Rescheduled"`)

* `Cancelled` (value: `"Cancelled"`)

* `No Show` (value: `"No Show"`)




