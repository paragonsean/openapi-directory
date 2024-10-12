

# NoPriceCountDetails

The reasons that contributed to the no price count and the total count for each reason.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**livePricingConfigIssueCount** | **String** | The total number of missed participation due to live pricing not being triggered for any of the following reasons: * You didn&#39;t have live pricing configured for these searches. * You restricted Google from accessing the hotel itinerary in question. |  [optional] |
|**livePricingNotAvailableCount** | **String** | The total number of missed participation due to live pricing being unavailable. Live pricing will not be triggered for certain default itineraries or UIs. In this scenario, partners will need a cached price to participate. |  [optional] |
|**livePricingNotTriggeredCount** | **String** | The total number of missed participation due to live pricing not being triggered for any of the following reasons: * You didn&#39;t set a bid. * You didn&#39;t have a valid landing page. * There weren&#39;t enough prices in the cache. |  [optional] |
|**livePricingOtherReasonCount** | **String** | The number of missed participations due to other issues with live pricing. |  [optional] |
|**livePricingTechnicalIssueCount** | **String** | The total number of missed participation due to technical issues with live pricing for any of the following reasons: * You didn’t respond quickly enough and exceeded the response deadline (around 4000 milliseconds). * You returned an error. * Your response was malformed. |  [optional] |



