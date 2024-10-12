

# LabOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessionNumber** | **String** | For external use only |  [optional] |
|**doctor** | **Integer** |  |  |
|**documents** | **List&lt;String&gt;** | Associated &#x60;/lab_documents&#x60; objects |  [optional] [readonly] |
|**icd10Codes** | [**List&lt;ICD10Code&gt;**](ICD10Code.md) | ICD-10 codes of the conditions which the tests concerns. |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**notes** | **String** |  |  [optional] |
|**patient** | **Integer** |  |  |
|**priority** | [**PriorityEnum**](#PriorityEnum) | &#x60;\&quot;Normal\&quot;&#x60; or &#x60;\&quot;STAT\&quot;&#x60;. Default &#x60;\&quot;Normal\&quot;&#x60; |  [optional] |
|**requisitionId** | **String** | The ID printed on the requisition PDF. Generally the same as id. |  [optional] [readonly] |
|**status** | **String** | Equivalent to HL7&#39;s ORC.5. Defaults to &#x60;\&quot;N\&quot;&#x60;. Value | Notes ----- | ----- &#x60;\&quot;N\&quot;&#x60; | not sent                                          | &#x60;\&quot;Q\&quot;&#x60; | queued for processing                             | &#x60;\&quot;A\&quot;&#x60; | &#x60;ABN (Advance Beneficiary Notice)&#x60; required       | &#x60;\&quot;S\&quot;&#x60; | send                                              | &#x60;\&quot;R\&quot;&#x60; | results received                                  | &#x60;\&quot;E\&quot;&#x60; | error                                             |  |  [optional] |
|**sublab** | **Integer** |  |  |
|**timestamp** | **String** | Time at which the order was submitted. Defaults to now |  [optional] [readonly] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| N | &quot;N&quot; |
| S | &quot;S&quot; |



