# ThePlaidApi.EntityWatchlistScreeningHit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | [**EntityScreeningHitAnalysis**](EntityScreeningHitAnalysis.md) |  | [optional] 
**data** | [**EntityScreeningHitData**](EntityScreeningHitData.md) |  | [optional] 
**firstActive** | **Date** | An ISO8601 formatted timestamp. | 
**historicalSince** | **Date** | An ISO8601 formatted timestamp. | 
**id** | **String** | ID of the associated entity screening hit. | 
**inactiveSince** | **Date** | An ISO8601 formatted timestamp. | 
**listCode** | [**EntityWatchlistCode**](EntityWatchlistCode.md) |  | 
**plaidUid** | **String** | A universal identifier for a watchlist individual that is stable across searches and updates. | 
**reviewStatus** | [**WatchlistScreeningHitStatus**](WatchlistScreeningHitStatus.md) |  | 
**sourceUid** | **String** | The identifier provided by the source sanction or watchlist. When one is not provided by the source, this is &#x60;null&#x60;. | 


