

# AccountCredentials

Credentials allowing Google to call a partner's API on behalf of a merchant.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | An OAuth access token. |  [optional] |
|**expiresIn** | **String** | The amount of time, in seconds, after which the access token is no longer valid. |  [optional] |
|**purpose** | [**PurposeEnum**](#PurposeEnum) | Indicates to Google how Google should use these OAuth tokens. |  [optional] |



## Enum: PurposeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_CREDENTIALS_PURPOSE_UNSPECIFIED | &quot;ACCOUNT_CREDENTIALS_PURPOSE_UNSPECIFIED&quot; |
| SHOPIFY_ORDER_MANAGEMENT | &quot;SHOPIFY_ORDER_MANAGEMENT&quot; |
| SHOPIFY_INTEGRATION | &quot;SHOPIFY_INTEGRATION&quot; |



