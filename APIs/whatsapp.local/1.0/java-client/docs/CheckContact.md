

# CheckContact



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**input** | **String** | The value you sent in the contacts field of the JSON request. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the user. |  [optional] |
|**waId** | **String** | WhatsApp user identifier that can be used in other API calls. Only returned if the status is valid. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROCESSING | &quot;processing&quot; |
| VALID | &quot;valid&quot; |
| INVALID | &quot;invalid&quot; |



