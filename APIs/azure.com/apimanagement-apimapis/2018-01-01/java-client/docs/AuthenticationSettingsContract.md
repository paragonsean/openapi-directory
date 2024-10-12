

# AuthenticationSettingsContract

API Authentication Settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**oAuth2** | [**ApiEntityBaseContractAuthenticationSettingsOAuth2**](ApiEntityBaseContractAuthenticationSettingsOAuth2.md) |  |  [optional] |
|**openid** | [**ApiEntityBaseContractAuthenticationSettingsOpenid**](ApiEntityBaseContractAuthenticationSettingsOpenid.md) |  |  [optional] |
|**subscriptionKeyRequired** | **Boolean** | Specifies whether subscription key is required during call to this API, true - API is included into closed products only, false - API is included into open products alone, null - there is a mix of products. |  [optional] |



