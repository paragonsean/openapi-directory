

# ReportingReceivershipCaseDetailsModel

Helper Model - Case Details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appointmentDate** | **OffsetDateTime** | Appointment Date |  [optional] |
|**closedDate** | **OffsetDateTime** | Closed Date |  [optional] |
|**closedReason** | [**ClosedReasonEnum**](#ClosedReasonEnum) | Closed Reason |  [optional] |
|**createdAt** | **OffsetDateTime** | Created At |  [optional] |
|**displayFirstReceiver** | **String** | Display First Receiver (ApplicationStaff) |  [optional] |
|**displayFreeholdBlockManager** | **String** | Display Freehold Block Manager |  [optional] |
|**displaySecondReceiver** | **String** | Display Second Receiver (ApplicationStaff) |  [optional] |
|**displayValidatingSolicitor** | **String** | Display Validating Solicitor |  [optional] |
|**extraNotes** | **String** | Extra Notes |  [optional] |
|**firstReceiverID** | **String** | First Receiver ID (ApplicationStaff) |  [optional] |
|**freeholdBlockManagerID** | **String** | Freehold Block Manager ID |  [optional] |
|**passedToLenderDate** | **OffsetDateTime** | Passed to Lender Date |  [optional] |
|**propertyOwnableID** | **String** | The unique Property Ownable identifier |  [optional] |
|**secondReceiverID** | **String** | Second Receiver ID (ApplicationStaff) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status |  [optional] |
|**tenure** | [**TenureEnum**](#TenureEnum) | Tenure |  [optional] |
|**validatingSolicitorID** | **String** | The unique Validating Solicitor identifier |  [optional] |
|**valuationDate** | **OffsetDateTime** | Valuation Date |  [optional] |



## Enum: ClosedReasonEnum

| Name | Value |
|---- | -----|
| PROPERTY_SOLD | &quot;PropertySold&quot; |
| HANDED_BACK_TO_BORROWER | &quot;HandedBackToBorrower&quot; |
| APPOINTMENT_ISSUES | &quot;AppointmentIssues&quot; |
| LENDER_SEEKING_POSSESSION | &quot;LenderSeekingPossession&quot; |
| OTHER | &quot;Other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OPENED | &quot;Opened&quot; |
| LITIGATION | &quot;Litigation&quot; |
| CLOSED | &quot;Closed&quot; |



## Enum: TenureEnum

| Name | Value |
|---- | -----|
| FREEHOLD | &quot;Freehold&quot; |
| LEASEHOLD | &quot;Leasehold&quot; |
| COMMONHOLD | &quot;Commonhold&quot; |
| SHARE_OF_FREEHOLD | &quot;ShareOfFreehold&quot; |
| FLYING_FREEHOLD | &quot;FlyingFreehold&quot; |
| SHARE_TRANSFER | &quot;ShareTransfer&quot; |
| UNKNOWN | &quot;Unknown&quot; |



