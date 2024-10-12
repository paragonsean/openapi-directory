# OpenapiJsClient.DoctorMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **Boolean** | If true, indicates that the message has been soft-deleted | [optional] [readonly] 
**attachment** | **String** | Files are passed using &#x60;multipart/form-data&#x60; encoding, but returned as URLs. | [optional] 
**doctor** | **Number** |  | 
**id** | **Number** |  | [optional] [readonly] 
**messageNotes** | [**[MessageNote]**](MessageNote.md) | Array of notes attached to the message | [optional] 
**owner** | **String** | ID of &#x60;/api/users&#x60; who owns the message, who may be the doctor themselves or one of their staff members | [optional] 
**patient** | **Number** | ID of patient that the message concerns, if applicable | [optional] 
**read** | **Boolean** |  | [optional] [readonly] 
**receivedAt** | **String** |  | [optional] [readonly] 
**responsibleUser** | **String** | ID of &#x60;/api/users&#x60; who has been assigned to process the message, who may be the doctor themselves or one of their staff members | [optional] 
**starred** | **Boolean** |  | [optional] [readonly] 
**title** | **String** |  | 
**type** | **String** |  Value | Description ----- | ----------- &#x60;\&quot;GP\&quot;&#x60; | Generated PDF &#x60;\&quot;GC\&quot;&#x60; | Generated CSV &#x60;\&quot;GZ\&quot;&#x60; | Generated ZIP &#x60;\&quot;IF\&quot;&#x60; | Incoming Fax &#x60;\&quot;OF\&quot;&#x60; | Outgoing Fax &#x60;\&quot;IL\&quot;&#x60; | Incoming Labs &#x60;\&quot;IR\&quot;&#x60; | Inbound Referrals &#x60;\&quot;OR\&quot;&#x60; | Outbound Referrals &#x60;\&quot;IE\&quot;&#x60; | Incoming eRx &#x60;\&quot;OA\&quot;&#x60; | Online Appointments &#x60;\&quot;PO\&quot;&#x60; | Patient Onboarding &#x60;\&quot;PI\&quot;&#x60; | Patient Incoming Message &#x60;\&quot;PM\&quot;&#x60; | Patient Outgoing Message &#x60;\&quot;OO\&quot;&#x60; | Demo Meeting Message &#x60;\&quot;OD\&quot;&#x60; | Outbound Direct Message &#x60;\&quot;ID\&quot;&#x60; | Inbound Direct Message  | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 
**workflowStep** | **String** | Used by doctors and their staff to keep track of what step of processing the message is in | [optional] [readonly] 



## Enum: TypeEnum


* `GP` (value: `"GP"`)

* `GC` (value: `"GC"`)

* `GT` (value: `"GT"`)

* `GZ` (value: `"GZ"`)

* `IF` (value: `"IF"`)

* `OF` (value: `"OF"`)

* `IL` (value: `"IL"`)

* `IR` (value: `"IR"`)

* `OR` (value: `"OR"`)

* `IE` (value: `"IE"`)

* `OA` (value: `"OA"`)

* `PO` (value: `"PO"`)

* `PI` (value: `"PI"`)

* `PM` (value: `"PM"`)

* `OO` (value: `"OO"`)

* `OD` (value: `"OD"`)

* `ID` (value: `"ID"`)

* `DL` (value: `"DL"`)

* `CN` (value: `"CN"`)




