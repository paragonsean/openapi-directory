

# CreateEnvironmentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  [optional] |
|**description** | **String** | The description of the environment. |  [optional] |
|**name** | **String** | The name of the environment. |  |
|**networkFabricType** | [**NetworkFabricTypeEnum**](#NetworkFabricTypeEnum) | The network fabric type of the environment. |  |
|**tags** | **Map&lt;String, String&gt;** | A collection of up to 50 unique tags |  [optional] |



## Enum: NetworkFabricTypeEnum

| Name | Value |
|---- | -----|
| TRANSIT_GATEWAY | &quot;TRANSIT_GATEWAY&quot; |
| NONE | &quot;NONE&quot; |



