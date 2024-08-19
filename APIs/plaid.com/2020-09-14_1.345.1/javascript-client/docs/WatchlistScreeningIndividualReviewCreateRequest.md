# ThePlaidApi.WatchlistScreeningIndividualReviewCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**comment** | **String** | A comment submitted by a team member as part of reviewing a watchlist screening. | [optional] 
**confirmedHits** | **[String]** | Hits to mark as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected. | 
**dismissedHits** | **[String]** | Hits to mark as a false positive after thorough manual review. These hits will never recur or be updated once dismissed. | 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**watchlistScreeningId** | **String** | ID of the associated screening. | 


