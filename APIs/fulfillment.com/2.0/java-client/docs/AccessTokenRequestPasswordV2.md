

# AccessTokenRequestPasswordV2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**password** | **String** |  |  |
|**username** | **String** |  |  |
|**clientId** | **String** | Id and secret provided by FDC |  |
|**clientSecret** | **String** |  |  |
|**grantType** | [**GrantTypeEnum**](#GrantTypeEnum) | Indicates how you&#39;re authenticating your request |  |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Currently limited to Order Management System |  |



## Enum: GrantTypeEnum

| Name | Value |
|---- | -----|
| PASSWORD | &quot;password&quot; |
| REFRESH_TOKEN | &quot;refresh_token&quot; |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| OMS | &quot;oms&quot; |



