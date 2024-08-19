# ThePlaidApi.DepositSwitchAltCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**countryCode** | **String** | ISO-3166-1 alpha-2 country code standard. | [optional] 
**options** | [**DepositSwitchCreateRequestOptions**](DepositSwitchCreateRequestOptions.md) |  | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**targetAccount** | [**DepositSwitchTargetAccount**](DepositSwitchTargetAccount.md) |  | 
**targetUser** | [**DepositSwitchTargetUser**](DepositSwitchTargetUser.md) |  | 



## Enum: CountryCodeEnum


* `US` (value: `"US"`)

* `CA` (value: `"CA"`)




