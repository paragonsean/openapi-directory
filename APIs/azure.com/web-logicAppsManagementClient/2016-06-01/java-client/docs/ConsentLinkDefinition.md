

# ConsentLinkDefinition

A consent link

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Display name of the parameter in the connection provider&#39;s OAuth settings |  [optional] |
|**firstPartyLoginUri** | **String** | URI for first party login |  [optional] |
|**link** | **String** | URI for the consent link |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the link |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNAUTHENTICATED | &quot;Unauthenticated&quot; |
| AUTHENTICATED | &quot;Authenticated&quot; |
| ERROR | &quot;Error&quot; |



