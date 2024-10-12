# LetMcApiV3Reporting.ReportingReceivershipCaseDetailsModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointmentDate** | **Date** | Appointment Date | [optional] 
**closedDate** | **Date** | Closed Date | [optional] 
**closedReason** | **String** | Closed Reason | [optional] 
**createdAt** | **Date** | Created At | [optional] 
**displayFirstReceiver** | **String** | Display First Receiver (ApplicationStaff) | [optional] 
**displayFreeholdBlockManager** | **String** | Display Freehold Block Manager | [optional] 
**displaySecondReceiver** | **String** | Display Second Receiver (ApplicationStaff) | [optional] 
**displayValidatingSolicitor** | **String** | Display Validating Solicitor | [optional] 
**extraNotes** | **String** | Extra Notes | [optional] 
**firstReceiverID** | **String** | First Receiver ID (ApplicationStaff) | [optional] 
**freeholdBlockManagerID** | **String** | Freehold Block Manager ID | [optional] 
**passedToLenderDate** | **Date** | Passed to Lender Date | [optional] 
**propertyOwnableID** | **String** | The unique Property Ownable identifier | [optional] 
**secondReceiverID** | **String** | Second Receiver ID (ApplicationStaff) | [optional] 
**status** | **String** | Status | [optional] 
**tenure** | **String** | Tenure | [optional] 
**validatingSolicitorID** | **String** | The unique Validating Solicitor identifier | [optional] 
**valuationDate** | **Date** | Valuation Date | [optional] 



## Enum: ClosedReasonEnum


* `PropertySold` (value: `"PropertySold"`)

* `HandedBackToBorrower` (value: `"HandedBackToBorrower"`)

* `AppointmentIssues` (value: `"AppointmentIssues"`)

* `LenderSeekingPossession` (value: `"LenderSeekingPossession"`)

* `Other` (value: `"Other"`)





## Enum: StatusEnum


* `Opened` (value: `"Opened"`)

* `Litigation` (value: `"Litigation"`)

* `Closed` (value: `"Closed"`)





## Enum: TenureEnum


* `Freehold` (value: `"Freehold"`)

* `Leasehold` (value: `"Leasehold"`)

* `Commonhold` (value: `"Commonhold"`)

* `ShareOfFreehold` (value: `"ShareOfFreehold"`)

* `FlyingFreehold` (value: `"FlyingFreehold"`)

* `ShareTransfer` (value: `"ShareTransfer"`)

* `Unknown` (value: `"Unknown"`)




