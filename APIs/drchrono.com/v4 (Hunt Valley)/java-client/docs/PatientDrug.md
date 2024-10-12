

# PatientDrug


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appointment** | **Integer** | Appointment ID corresponding to the initial prescription |  [optional] |
|**datePrescribed** | **String** |  |  [optional] |
|**dateStartedTaking** | **String** |  |  [optional] |
|**dateStoppedTaking** | **String** |  |  [optional] |
|**daw** | **Boolean** | If true, the prescription should be dispensed as written and not substituted |  [optional] |
|**dispenseQuantity** | **BigDecimal** |  |  [optional] |
|**doctor** | **Integer** | Prescribing doctor ID |  |
|**dosageQuantity** | **String** | Please note, this used to be an decimal field, you can still pass decimal value to it. Or you can pass in some formatted string if needed. |  [optional] |
|**dosageUnits** | **String** |  |  [optional] |
|**frequency** | **String** | Frequency pf administration |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**indication** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**ndc** | **String** |  |  [optional] |
|**notes** | **String** | Any additional notes from the provider |  [optional] |
|**numberRefills** | **Integer** |  |  [optional] |
|**orderStatus** | [**OrderStatusEnum**](#OrderStatusEnum) | One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Ordered\&quot;&#x60;, &#x60;\&quot;Administered during visit\&quot;&#x60;, &#x60;\&quot;Electronic eRx Sent\&quot;&#x60;, &#x60;\&quot;Phoned into Pharmacy\&quot;&#x60;, &#x60;\&quot;Faxed to Pharmacy\&quot;&#x60;, &#x60;\&quot;Paper Rx\&quot;&#x60;, &#x60;\&quot;Prescription Printed\&quot;&#x60;, &#x60;\&quot;Discontinued\&quot;&#x60;, &#x60;\&quot;Prescribed by other Dr\&quot;&#x60; or &#x60;\&quot;Over the Counter\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;\&quot;&#x60; |  [optional] |
|**patient** | **Integer** |  |  |
|**pharmacyNote** | **String** |  |  [optional] |
|**prn** | **Boolean** | If &#x60;True&#x60;, the medication should be taken when necessary |  [optional] |
|**route** | **String** | Route of administration |  [optional] |
|**rxnorm** | **String** | RxNorm code for the medication |  [optional] |
|**signatureNote** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | If present, one of &#x60;\&quot;active\&quot;&#x60; or &#x60;\&quot;inactive\&quot;&#x60;. If omitted in writing, default to &#x60;\&quot;active\&quot;&#x60; |  [optional] |



## Enum: OrderStatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| ORDERED | &quot;Ordered&quot; |
| ADMINISTERED_DURING_VISIT | &quot;Administered during visit&quot; |
| ELECTRONIC_E_RX_SENT | &quot;Electronic eRx Sent&quot; |
| PHONED_INTO_PHARMACY | &quot;Phoned into Pharmacy&quot; |
| FAXED_TO_PHARMACY | &quot;Faxed to Pharmacy&quot; |
| PAPER_RX | &quot;Paper Rx&quot; |
| PRESCRIPTION_PRINTED | &quot;Prescription Printed&quot; |
| DISCONTINUED | &quot;Discontinued&quot; |
| PRESCRIBED_BY_OTHER_DR | &quot;Prescribed by other Dr&quot; |
| OVER_THE_COUNTER | &quot;Over the Counter&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



