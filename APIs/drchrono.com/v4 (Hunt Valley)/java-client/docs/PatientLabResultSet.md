

# PatientLabResultSet


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** |  |  [optional] [readonly] |
|**dateTestPerformed** | **String** | Date of lab test. |  [optional] |
|**doctorComments** | **String** | Comment from the doctor on lab result. |  [optional] |
|**doctorSignoff** | **Boolean** | Check this box when the doctor has reviewed the lab result and taken appropriate action. |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**labAbnormalFlag** | [**LabAbnormalFlagEnum**](#LabAbnormalFlagEnum) | HL7 codified abnormal flag for the result. |  [optional] |
|**labImportedFromCcr** | **String** | Imported CCR document that contains lab results. |  [optional] [readonly] |
|**labNormalRange** | **String** |  |  [optional] |
|**labNormalRangeUnits** | **String** |  |  [optional] |
|**labOrderStatus** | [**LabOrderStatusEnum**](#LabOrderStatusEnum) | Status of the lab order. |  [optional] |
|**labResultValue** | **String** |  |  [optional] |
|**labResultValueAsFloat** | **BigDecimal** |  |  [optional] |
|**labResultValueUnits** | **String** |  |  [optional] |
|**loincCode** | **String** |  |  [optional] |
|**orderingDoctor** | **Integer** |  |  |
|**patient** | **Integer** |  |  |
|**scannedInResult** | **String** | Scanned in PDF for this lab result (optional). |  [optional] [readonly] |
|**title** | **String** |  |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: LabAbnormalFlagEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| L | &quot;L&quot; |
| H | &quot;H&quot; |
| LL | &quot;LL&quot; |
| HH | &quot;HH&quot; |
| LESS_THAN | &quot;&lt;&quot; |
| GREATER_THAN | &quot;&gt;&quot; |
| N | &quot;N&quot; |
| A | &quot;A&quot; |
| AA | &quot;AA&quot; |
| NULL | &quot;null&quot; |
| U | &quot;U&quot; |
| D | &quot;D&quot; |
| B | &quot;B&quot; |
| W | &quot;W&quot; |
| S | &quot;S&quot; |
| R | &quot;R&quot; |
| I | &quot;I&quot; |
| MS | &quot;MS&quot; |
| VS | &quot;VS&quot; |



## Enum: LabOrderStatusEnum

| Name | Value |
|---- | -----|
| EMPTY | &quot;&quot; |
| ORDER_ENTERED | &quot;Order Entered&quot; |
| DISCONTINUED | &quot;Discontinued&quot; |
| IN_PROGRESS | &quot;In Progress&quot; |
| RESULTS_RECEIVED | &quot;Results Received&quot; |
| RESULTS_REVIEWED_WITH_PATIENT | &quot;Results Reviewed with Patient&quot; |
| PAPER_ORDER | &quot;Paper Order&quot; |



