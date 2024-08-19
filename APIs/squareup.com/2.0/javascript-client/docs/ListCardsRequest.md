# SquareConnectApi.ListCardsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. | [optional] 
**customerId** | **String** | Limit results to cards associated with the customer supplied. By default, all cards owned by the merchant are returned. | [optional] 
**includeDisabled** | **Boolean** | Includes disabled cards. By default, all enabled cards owned by the merchant are returned. | [optional] 
**referenceId** | **String** | Limit results to cards associated with the reference_id supplied. | [optional] 
**sortOrder** | **String** | Sorts the returned list by when the card was created with the specified order. This field defaults to ASC. | [optional] 


