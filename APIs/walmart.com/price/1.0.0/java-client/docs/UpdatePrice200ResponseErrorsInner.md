

# UpdatePrice200ResponseErrorsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional] |
|**causes** | [**List&lt;UpdatePrice200ResponseErrorsInnerCausesInner&gt;**](UpdatePrice200ResponseErrorsInnerCausesInner.md) |  |  [optional] |
|**code** | **String** |  |  |
|**component** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**errorIdentifiers** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**field** | **String** |  |  [optional] |
|**gatewayErrorCategory** | [**GatewayErrorCategoryEnum**](#GatewayErrorCategoryEnum) |  |  [optional] |
|**info** | **String** |  |  [optional] |
|**serviceName** | **String** |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |
|**type** | **String** |  |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| APPLICATION | &quot;APPLICATION&quot; |
| SYSTEM | &quot;SYSTEM&quot; |
| REQUEST | &quot;REQUEST&quot; |
| DATA | &quot;DATA&quot; |



## Enum: GatewayErrorCategoryEnum

| Name | Value |
|---- | -----|
| INTERNAL_DATA_ERROR | &quot;INTERNAL_DATA_ERROR&quot; |
| EXTERNAL_DATA_ERROR | &quot;EXTERNAL_DATA_ERROR&quot; |
| SYSTEM_ERROR | &quot;SYSTEM_ERROR&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFO | &quot;INFO&quot; |
| WARN | &quot;WARN&quot; |
| ERROR | &quot;ERROR&quot; |



