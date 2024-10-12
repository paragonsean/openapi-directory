

# ReadyToPayAchMethodFeature

The specific feature (eg. digital wallet or a processor) of this method. If method doesn't have any features – will be null. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expirationTime** | **OffsetDateTime** | The expiration time of a &#x60;linkToken&#x60;. |  [optional] |
|**linkToken** | **String** | The Plaid &#x60;linkToken&#x60; for frontend integrations. |  [optional] |
|**name** | [**NameEnum**](#NameEnum) | The feature name. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| PLAID | &quot;Plaid&quot; |



