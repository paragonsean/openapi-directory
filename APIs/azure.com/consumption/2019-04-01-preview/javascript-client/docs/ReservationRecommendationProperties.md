# ConsumptionManagementClient.ReservationRecommendationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costWithNoReservedInstances** | **Number** | The total amount of cost without reserved instances. | [optional] [readonly] 
**firstUsageDate** | **Date** | The usage date for looking back. | [optional] [readonly] 
**lookBackPeriod** | **String** | The number of days of usage to look back for recommendation. | [optional] [readonly] 
**meterId** | **String** | The meter id (GUID) | [optional] [readonly] 
**netSavings** | **Number** | Total estimated savings with reserved instances. | [optional] [readonly] 
**recommendedQuantity** | **Number** | Recommended quality for reserved instances. | [optional] [readonly] 
**scope** | **String** | Shared or single recommendation. | [optional] [readonly] 
**term** | **String** | RI recommendations in one or three year terms. | [optional] [readonly] 
**totalCostWithReservedInstances** | **Number** | The total amount of cost with reserved instances. | [optional] [readonly] 


