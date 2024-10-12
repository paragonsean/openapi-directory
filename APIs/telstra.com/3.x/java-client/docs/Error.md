

# Error


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Unique code of the error |  |
|**field** | **String** | The field that caused the error |  [optional] |
|**issue** | **String** | The reason for the error |  |
|**link** | **String** | URI for detailed information related to this error for the developer. |  [optional] |
|**location** | [**LocationEnum**](#LocationEnum) | The location of the field that caused the error. |  [optional] |
|**suggestedAction** | **String** | Suggest practical actions for this particular issue. |  |
|**value** | **String** | The value of the field that caused the error |  [optional] |



## Enum: LocationEnum

| Name | Value |
|---- | -----|
| BODY | &quot;body&quot; |
| PATH | &quot;path&quot; |
| QUERY | &quot;query&quot; |



