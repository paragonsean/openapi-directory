

# NAWelcomeSubEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Identifier of the sub event |  [optional] |
|**message** | **String** | User facing sub event description |  [optional] |
|**offset** | **Integer** |  |  [optional] |
|**snapshot** | [**NAWelcomeSnapshot**](NAWelcomeSnapshot.md) |  |  [optional] |
|**time** | **Integer** | Time of occurence of the sub event |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the detected object. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HUMAN | &quot;human&quot; |
| ANIMAL | &quot;animal&quot; |
| VEHICLE | &quot;vehicle&quot; |



