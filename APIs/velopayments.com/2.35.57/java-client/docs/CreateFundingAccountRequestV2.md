

# CreateFundingAccountRequestV2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** | Required if type is either FBO or PRIVATE |  [optional] |
|**accountNumber** | **String** | Required if type is either FBO or PRIVATE |  [optional] |
|**currency** | **String** | ISO 4217 currency code, Required if type is either WUBS_DECOUPLED or PRIVATE |  [optional] |
|**name** | **String** |  |  |
|**payorId** | **UUID** |  |  |
|**routingNumber** | **String** | Required if type is either FBO or PRIVATE |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FBO | &quot;FBO&quot; |
| WUBS_DECOUPLED | &quot;WUBS_DECOUPLED&quot; |
| PRIVATE | &quot;PRIVATE&quot; |



