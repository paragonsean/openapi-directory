

# WebTest

An Application Insights web test definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) | The kind of web test that this web test watches. Choices are ping and multistep. |  [optional] |
|**properties** | [**WebTestProperties**](WebTestProperties.md) |  |  [optional] |
|**id** | **String** | Azure resource Id |  [optional] [readonly] |
|**location** | **String** | Resource location |  |
|**name** | **String** | Azure resource name |  [optional] [readonly] |
|**tags** | **Object** | Resource tags |  [optional] |
|**type** | **String** | Azure resource type |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| PING | &quot;ping&quot; |
| MULTISTEP | &quot;multistep&quot; |



