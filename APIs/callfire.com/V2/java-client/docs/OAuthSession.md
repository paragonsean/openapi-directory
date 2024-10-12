

# OAuthSession

~

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ~ |  [optional] |
|**actor** | [**OAuthSession**](OAuthSession.md) |  |  [optional] |
|**brand** | [**BrandEnum**](#BrandEnum) | ~ |  [optional] |
|**clientId** | **String** | ~ |  [optional] |
|**email** | **String** | ~ |  [optional] |
|**expires** | **OffsetDateTime** | ~ |  [optional] |
|**grantType** | [**GrantTypeEnum**](#GrantTypeEnum) | ~ |  [optional] |
|**id** | **String** | ~ |  [optional] |
|**ipAddress** | **String** | ~ |  [optional] |
|**issued** | **OffsetDateTime** | ~ |  [optional] |
|**scope** | **String** | ~ |  [optional] |
|**sid** | **Long** | ~ |  [optional] |
|**userId** | **String** | ~ |  [optional] |
|**username** | **String** | ~ |  [optional] |
|**verificationRequired** | **Boolean** | ~ |  [optional] |



## Enum: BrandEnum

| Name | Value |
|---- | -----|
| EZTEXTING | &quot;EZTEXTING&quot; |
| CLUBTEXTING | &quot;CLUBTEXTING&quot; |
| GROUPTEXTING | &quot;GROUPTEXTING&quot; |
| TELLMYCELL | &quot;TELLMYCELL&quot; |
| EZ | &quot;EZ&quot; |
| CALLFIRE | &quot;CALLFIRE&quot; |
| TESLA | &quot;TESLA&quot; |



## Enum: GrantTypeEnum

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;AUTHORIZATION_CODE&quot; |
| PASSWORD | &quot;PASSWORD&quot; |
| REFRESH_TOKEN | &quot;REFRESH_TOKEN&quot; |
| CLIENT_CREDENTIALS | &quot;CLIENT_CREDENTIALS&quot; |
| JWT_BEARER | &quot;JWT_BEARER&quot; |
| IMPERSONATE | &quot;IMPERSONATE&quot; |
| EXCHANGE | &quot;EXCHANGE&quot; |



