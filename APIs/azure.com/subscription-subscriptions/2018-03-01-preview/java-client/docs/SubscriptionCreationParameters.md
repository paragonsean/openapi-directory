

# SubscriptionCreationParameters

Subscription Creation Parameters required to create a new Azure subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalParameters** | **Map&lt;String, Object&gt;** | Additional, untyped parameters to support custom subscription creation scenarios. |  [optional] |
|**displayName** | **String** | The display name of the subscription. |  [optional] |
|**offerType** | [**OfferTypeEnum**](#OfferTypeEnum) | The offer type of the subscription. For example, MS-AZR-0017P (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement devTest) are available. Only valid when creating a subscription in a enrollment account scope. |  [optional] |
|**owners** | [**List&lt;AdPrincipal&gt;**](AdPrincipal.md) | The list of principals that should be granted Owner access on the subscription. Principals should be of type User, Service Principal or Security Group. |  [optional] |



## Enum: OfferTypeEnum

| Name | Value |
|---- | -----|
| _0017_P | &quot;MS-AZR-0017P&quot; |
| _0148_P | &quot;MS-AZR-0148P&quot; |



