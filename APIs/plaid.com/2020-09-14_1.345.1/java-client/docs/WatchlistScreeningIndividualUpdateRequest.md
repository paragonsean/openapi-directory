

# WatchlistScreeningIndividualUpdateRequest

Request input for editing an individual watchlist screening

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignee** | **String** | ID of the associated user. |  [optional] |
|**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. |  [optional] |
|**clientUserId** | **String** | An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object. |  [optional] |
|**resetFields** | **List&lt;WatchlistScreeningIndividualUpdateRequestResettableField&gt;** | A list of fields to reset back to null |  [optional] |
|**searchTerms** | [**UpdateIndividualScreeningRequestSearchTerms**](UpdateIndividualScreeningRequestSearchTerms.md) |  |  [optional] |
|**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. |  [optional] |
|**status** | **WatchlistScreeningStatus** |  |  [optional] |
|**watchlistScreeningId** | **String** | ID of the associated screening. |  |



