# ContentApiForShopping.Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | A boolean exposing the active status of the shipping service. Required. | [optional] 
**currency** | **String** | The CLDR code of the currency to which this service applies. Must match that of the prices in rate groups. | [optional] 
**deliveryCountry** | **String** | The CLDR territory code of the country to which the service applies. Required. | [optional] 
**deliveryTime** | [**DeliveryTime**](DeliveryTime.md) |  | [optional] 
**eligibility** | **String** | Eligibility for this service. Acceptable values are: - \&quot;&#x60;All scenarios&#x60;\&quot; - \&quot;&#x60;All scenarios except Shopping Actions&#x60;\&quot; - \&quot;&#x60;Shopping Actions&#x60;\&quot;  | [optional] 
**minimumOrderValue** | [**Price**](Price.md) |  | [optional] 
**minimumOrderValueTable** | [**MinimumOrderValueTable**](MinimumOrderValueTable.md) |  | [optional] 
**name** | **String** | Free-form name of the service. Must be unique within target account. Required. | [optional] 
**pickupService** | [**PickupCarrierService**](PickupCarrierService.md) |  | [optional] 
**rateGroups** | [**[RateGroup]**](RateGroup.md) | Shipping rate group definitions. Only the last one is allowed to have an empty &#x60;applicableShippingLabels&#x60;, which means \&quot;everything else\&quot;. The other &#x60;applicableShippingLabels&#x60; must not overlap. | [optional] 
**shipmentType** | **String** | Type of locations this service ships orders to. Acceptable values are: - \&quot;&#x60;delivery&#x60;\&quot; - \&quot;&#x60;pickup&#x60; (deprecated)\&quot; - \&quot;&#x60;local_delivery&#x60;\&quot; - \&quot;&#x60;collection_point&#x60;\&quot;  | [optional] 
**storeConfig** | [**ServiceStoreConfig**](ServiceStoreConfig.md) |  | [optional] 


