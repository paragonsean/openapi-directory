# SubscriptionClient.ModernSubscriptionCreationParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costCenter** | **String** | If set, the cost center will show up on the Azure usage and charges file. | [optional] 
**displayName** | **String** | The friendly name of the subscription. | 
**managementGroupId** | **String** | The identifier of the management group to which this subscription will be associated. | [optional] 
**owner** | [**AdPrincipal**](AdPrincipal.md) |  | [optional] 
**skuId** | **String** | The SKU ID of the Azure plan. Azure plan determines the pricing and service-level agreement of the subscription.  Use 001 for Microsoft Azure Plan and 002 for Microsoft Azure Plan for DevTest. | 


