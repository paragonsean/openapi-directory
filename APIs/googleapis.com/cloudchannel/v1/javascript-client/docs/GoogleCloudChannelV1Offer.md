# CloudChannelApi.GoogleCloudChannelV1Offer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**GoogleCloudChannelV1Constraints**](GoogleCloudChannelV1Constraints.md) |  | [optional] 
**dealCode** | **String** | The deal code of the offer to get a special promotion or discount. | [optional] 
**endTime** | **String** | Output only. End of the Offer validity time. | [optional] [readonly] 
**marketingInfo** | [**GoogleCloudChannelV1MarketingInfo**](GoogleCloudChannelV1MarketingInfo.md) |  | [optional] 
**name** | **String** | Resource Name of the Offer. Format: accounts/{account_id}/offers/{offer_id} | [optional] 
**parameterDefinitions** | [**[GoogleCloudChannelV1ParameterDefinition]**](GoogleCloudChannelV1ParameterDefinition.md) | Parameters required to use current Offer to purchase. | [optional] 
**plan** | [**GoogleCloudChannelV1Plan**](GoogleCloudChannelV1Plan.md) |  | [optional] 
**priceByResources** | [**[GoogleCloudChannelV1PriceByResource]**](GoogleCloudChannelV1PriceByResource.md) | Price for each monetizable resource type. | [optional] 
**sku** | [**GoogleCloudChannelV1Sku**](GoogleCloudChannelV1Sku.md) |  | [optional] 
**startTime** | **String** | Start of the Offer validity time. | [optional] 


