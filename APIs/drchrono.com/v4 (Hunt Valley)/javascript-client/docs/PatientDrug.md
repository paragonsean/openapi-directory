# OpenapiJsClient.PatientDrug

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment** | **Number** | Appointment ID corresponding to the initial prescription | [optional] 
**datePrescribed** | **String** |  | [optional] 
**dateStartedTaking** | **String** |  | [optional] 
**dateStoppedTaking** | **String** |  | [optional] 
**daw** | **Boolean** | If true, the prescription should be dispensed as written and not substituted | [optional] 
**dispenseQuantity** | **Number** |  | [optional] 
**doctor** | **Number** | Prescribing doctor ID | 
**dosageQuantity** | **String** | Please note, this used to be an decimal field, you can still pass decimal value to it. Or you can pass in some formatted string if needed. | [optional] 
**dosageUnits** | **String** |  | [optional] 
**frequency** | **String** | Frequency pf administration | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**indication** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**ndc** | **String** |  | [optional] 
**notes** | **String** | Any additional notes from the provider | [optional] 
**numberRefills** | **Number** |  | [optional] 
**orderStatus** | **String** | One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Ordered\&quot;&#x60;, &#x60;\&quot;Administered during visit\&quot;&#x60;, &#x60;\&quot;Electronic eRx Sent\&quot;&#x60;, &#x60;\&quot;Phoned into Pharmacy\&quot;&#x60;, &#x60;\&quot;Faxed to Pharmacy\&quot;&#x60;, &#x60;\&quot;Paper Rx\&quot;&#x60;, &#x60;\&quot;Prescription Printed\&quot;&#x60;, &#x60;\&quot;Discontinued\&quot;&#x60;, &#x60;\&quot;Prescribed by other Dr\&quot;&#x60; or &#x60;\&quot;Over the Counter\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;\&quot;&#x60; | [optional] 
**patient** | **Number** |  | 
**pharmacyNote** | **String** |  | [optional] 
**prn** | **Boolean** | If &#x60;True&#x60;, the medication should be taken when necessary | [optional] 
**route** | **String** | Route of administration | [optional] 
**rxnorm** | **String** | RxNorm code for the medication | [optional] 
**signatureNote** | **String** |  | [optional] 
**status** | **String** | If present, one of &#x60;\&quot;active\&quot;&#x60; or &#x60;\&quot;inactive\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;active\&quot;&#x60; | [optional] 



## Enum: OrderStatusEnum


* `empty` (value: `""`)

* `Ordered` (value: `"Ordered"`)

* `Administered during visit` (value: `"Administered during visit"`)

* `Electronic eRx Sent` (value: `"Electronic eRx Sent"`)

* `Phoned into Pharmacy` (value: `"Phoned into Pharmacy"`)

* `Faxed to Pharmacy` (value: `"Faxed to Pharmacy"`)

* `Paper Rx` (value: `"Paper Rx"`)

* `Prescription Printed` (value: `"Prescription Printed"`)

* `Discontinued` (value: `"Discontinued"`)

* `Prescribed by other Dr` (value: `"Prescribed by other Dr"`)

* `Over the Counter` (value: `"Over the Counter"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)




