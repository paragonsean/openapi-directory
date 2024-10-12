# SubscriptionClient.SubscriptionCreationParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalParameters** | **{String: Object}** | Additional, untyped parameters to support custom subscription creation scenarios. | [optional] 
**displayName** | **String** | The display name of the subscription. | [optional] 
**offerType** | **String** | The offer type of the subscription. For example, MS-AZR-0017P (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement devTest) are available. Only valid when creating a subscription in a enrollment account scope. | [optional] 
**owners** | [**[AdPrincipal]**](AdPrincipal.md) | The list of principals that should be granted Owner access on the subscription. Principals should be of type User, Service Principal or Security Group. | [optional] 



## Enum: OfferTypeEnum


* `0017P` (value: `"MS-AZR-0017P"`)

* `0148P` (value: `"MS-AZR-0148P"`)




