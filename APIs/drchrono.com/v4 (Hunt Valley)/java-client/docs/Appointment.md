

# Appointment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowOverlapping** | **Boolean** | Bypass overlap check. |  [optional] |
|**apptIsBreak** | **Boolean** |  |  [optional] |
|**baseRecurringAppointment** | **String** | ID of base appointment of a recurrign series |  [optional] [readonly] |
|**billingNotes** | [**List&lt;ClaimBillingNotes1&gt;**](ClaimBillingNotes1.md) | Billing notes of the appointment. For writing, check &#x60;/api/claim_billing_notes&#x60; |  [optional] [readonly] |
|**billingProvider** | **String** |  |  [optional] [readonly] |
|**billingStatus** | **String** | Should be one of &#x60;Auto Accident Claim&#x60;, &#x60;Balance Due&#x60;, &#x60;Bill Insurance&#x60;, &#x60;Bill Secondary Insurance&#x60;, &#x60;Durable Medical Equipment Claim&#x60;, &#x60;Internal Review&#x60;, &#x60;Paid In Full&#x60;, &#x60;Settled&#x60;, &#x60;Worker&#39;s Comp Claim&#x60; or one of the custom billing status |  [optional] |
|**clinicalNote** | [**ClinicalNote1**](ClinicalNote1.md) |  |  [optional] |
|**clonedFrom** | **Integer** | ID of the original appointment which this appointment cloned from. Will be null if the appointment is not cloned. |  [optional] |
|**color** | **String** |  |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**customFields** | [**List&lt;CustomAppointmentFieldValue&gt;**](CustomAppointmentFieldValue.md) | Custom appointment fields |  [optional] |
|**customVitals** | [**List&lt;CustomVitalValue&gt;**](CustomVitalValue.md) | Custom vitals associated with this appointment. |  [optional] |
|**deletedFlag** | **Boolean** | Whether the appointmetn is deleted. |  [optional] [readonly] |
|**doctor** | **Integer** | Doctor ID |  |
|**duration** | **Integer** | Length of the appointment in minutes. Optional if &#x60;profile&#x60; is provided. |  [optional] |
|**examRoom** | **Integer** | Index of the exam room that this appointment occurs in. See &#x60;/api/offices&#x60; |  |
|**extendedUpdatedAt** | **String** | The most recent update time among appointment itself, its vitals and its custom vitals |  [optional] [readonly] |
|**firstBilledDate** | **String** |  |  [optional] [readonly] |
|**icd10Codes** | **List&lt;String&gt;** |  |  [optional] |
|**icd9Codes** | **List&lt;String&gt;** |  |  [optional] |
|**id** | **String** | Unique identifier. Usually numeric, but not always |  [optional] [readonly] |
|**ins1Status** | [**Ins1StatusEnum**](#Ins1StatusEnum) | Billing status of primary insurer |  [optional] [readonly] |
|**ins2Status** | [**Ins2StatusEnum**](#Ins2StatusEnum) | Billing status of secondary insurer |  [optional] [readonly] |
|**isVirtualBase** | **Boolean** |  |  [optional] [readonly] |
|**isWalkIn** | **Boolean** | Whether the appointment is a walk-in appointment |  [optional] |
|**lastBilledDate** | **String** |  |  [optional] [readonly] |
|**notes** | **String** |  |  [optional] |
|**office** | **Integer** | Office ID |  |
|**patient** | **Integer** | ID of this appointment&#39;s patient. Breaks have a null patient field. |  |
|**primaryInsuranceIdNumber** | **String** |  |  [optional] [readonly] |
|**primaryInsurerName** | **String** |  |  [optional] [readonly] |
|**primaryInsurerPayerId** | **String** |  |  [optional] [readonly] |
|**profile** | **Integer** | ID of an &#x60;/api/appointment_profiles&#x60; instance. The profile sets default values for &#x60;color&#x60;, &#x60;duration&#x60;, and &#x60;reason&#x60; on creation, which can be overriden by setting these values explicitly. |  [optional] |
|**reason** | **String** | Default to &#x60;\&quot;\&quot;&#x60; |  [optional] |
|**recurringAppointment** | **Boolean** | Whether the appointment is a recurring appointment or not |  [optional] [readonly] |
|**reminderProfile** | **String** | Write-only. ID of an &#x60;/api/reminder_profiles&#x60; instance. Set this to apply a reminder profile to the appointment. Cannot be applied to an appointment with reminders. |  [optional] |
|**reminders** | [**List&lt;SimpleReminder&gt;**](SimpleReminder.md) | Scheduled reminders of the appointment |  [optional] [readonly] |
|**scheduledTime** | **String** | The starting time of the appointment |  |
|**secondaryInsuranceIdNumber** | **String** |  |  [optional] [readonly] |
|**secondaryInsurerName** | **String** |  |  [optional] [readonly] |
|**secondaryInsurerPayerId** | **String** |  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | One of &#x60;&#x60;, &#x60;Arrived&#x60;, &#x60;Checked In&#x60;, &#x60;In Room&#x60;, &#x60;Cancelled&#x60;, &#x60;Complete&#x60;, &#x60;Confirmed&#x60;, &#x60;In Session&#x60;, &#x60;No Show&#x60;, &#x60;Not Confirmed&#x60;, or &#x60;Rescheduled&#x60;. Or one of the custom statuses. |  [optional] |
|**statusTransitions** | [**List&lt;AppointmentStatusTransition&gt;**](AppointmentStatusTransition.md) |  |  [optional] [readonly] |
|**supervisingProvider** | **String** | Supervising provider of appointment if set. |  [optional] [readonly] |
|**updatedAt** | **String** |  |  [optional] [readonly] |
|**vitals** | [**SystemVitals**](SystemVitals.md) |  |  [optional] |



## Enum: Ins1StatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| INCOMPLETE_INFORMATION | &quot;Incomplete Information&quot; |
| IN_PROCESS_EMDEON | &quot;In Process Emdeon&quot; |
| REJECTED_EMDEON | &quot;Rejected Emdeon&quot; |
| REJECTED_JOPARI | &quot;Rejected Jopari&quot; |
| IN_PROCESS_PAYOR | &quot;In Process Payor&quot; |
| REJECTED_WAYSTAR_PROFESSIONAL | &quot;Rejected Waystar Professional&quot; |
| REJECTED_WAYSTAR_INSTITUTIONAL | &quot;Rejected Waystar Institutional&quot; |
| IN_PROCESS_PAYER | &quot;In Process Payer&quot; |
| PAYER_ACKNOWLEDGED | &quot;Payer Acknowledged&quot; |
| REJECTED_PAYOR | &quot;Rejected Payor&quot; |
| REJECTED_PAYER | &quot;Rejected Payer&quot; |
| PAID_IN_FULL | &quot;Paid in Full&quot; |
| PARTIALLY_PAID | &quot;Partially Paid&quot; |
| COORDINATION_OF_BENEFITS | &quot;Coordination of Benefits&quot; |
| ERA_RECEIVED | &quot;ERA Received&quot; |
| ERA_DENIED | &quot;ERA Denied&quot; |
| HCFA_FORM_FAXED | &quot;HCFA Form Faxed&quot; |



## Enum: Ins2StatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| INCOMPLETE_INFORMATION | &quot;Incomplete Information&quot; |
| IN_PROCESS_EMDEON | &quot;In Process Emdeon&quot; |
| REJECTED_EMDEON | &quot;Rejected Emdeon&quot; |
| REJECTED_JOPARI | &quot;Rejected Jopari&quot; |
| IN_PROCESS_PAYOR | &quot;In Process Payor&quot; |
| REJECTED_WAYSTAR_PROFESSIONAL | &quot;Rejected Waystar Professional&quot; |
| REJECTED_WAYSTAR_INSTITUTIONAL | &quot;Rejected Waystar Institutional&quot; |
| IN_PROCESS_PAYER | &quot;In Process Payer&quot; |
| PAYER_ACKNOWLEDGED | &quot;Payer Acknowledged&quot; |
| REJECTED_PAYOR | &quot;Rejected Payor&quot; |
| REJECTED_PAYER | &quot;Rejected Payer&quot; |
| PAID_IN_FULL | &quot;Paid in Full&quot; |
| PARTIALLY_PAID | &quot;Partially Paid&quot; |
| COORDINATION_OF_BENEFITS | &quot;Coordination of Benefits&quot; |
| ERA_RECEIVED | &quot;ERA Received&quot; |
| ERA_DENIED | &quot;ERA Denied&quot; |
| HCFA_FORM_FAXED | &quot;HCFA Form Faxed&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| ARRIVED | &quot;Arrived&quot; |
| CHECKED_IN | &quot;Checked In&quot; |
| CHECKED_IN_ONLINE | &quot;Checked In Online&quot; |
| IN_ROOM | &quot;In Room&quot; |
| IN_SESSION | &quot;In Session&quot; |
| COMPLETE | &quot;Complete&quot; |
| CONFIRMED | &quot;Confirmed&quot; |
| NOT_CONFIRMED | &quot;Not Confirmed&quot; |
| RESCHEDULED | &quot;Rescheduled&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| NO_SHOW | &quot;No Show&quot; |



