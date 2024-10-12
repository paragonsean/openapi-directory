

# LabOrderDocument


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**document** | **String** |  |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**labOrder** | **Integer** | ID of the order this document is associated with |  |
|**timestamp** | **String** | Time at which the document was uploaded |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) |  Value | Notes ----- | ----- &#x60;\&quot;REQ\&quot;&#x60; | requisition form                                              | &#x60;\&quot;ABN\&quot;&#x60; | &#x60;ABN (Advance Beneficiary Notice)&#x60;                            | &#x60;\&quot;R-A\&quot;&#x60; | requisition form and :abbr:&#x60;ABN (Advance Beneficiary Notice)&#x60; | &#x60;\&quot;RES\&quot;&#x60; | lab results                                                   |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| REQ | &quot;REQ&quot; |
| ABN | &quot;ABN&quot; |
| R_A | &quot;R-A&quot; |
| RES | &quot;RES&quot; |



