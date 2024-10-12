

# ServicesCheckNameAvailability200Response

Indicates whether a proposed resource name is available

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The localized reason why the name is not available, if nameAvailable is false |  [optional] |
|**nameAvailable** | **Boolean** | If true, the name is valid and available. If false, &#39;reason&#39; describes why not. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason why the name is not available, if nameAvailable is false |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| ALREADY_EXISTS | &quot;AlreadyExists&quot; |
| INVALID | &quot;Invalid&quot; |



