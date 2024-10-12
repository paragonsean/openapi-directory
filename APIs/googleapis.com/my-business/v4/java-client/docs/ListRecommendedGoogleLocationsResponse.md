

# ListRecommendedGoogleLocationsResponse

Response message for GoogleLocations.ListRecommendedGoogleLocations. It also contains some locations that have been claimed by other Business Profile users since the last time they were recommended to this Business Profile account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**googleLocations** | [**List&lt;GoogleLocation&gt;**](GoogleLocation.md) | The locations recommended to a Business Profile account. Each of these represents a GoogleLocation that is present on Maps. The locations are sorted in decreasing order of relevance to the Business Profile account. |  [optional] |
|**nextPageToken** | **String** | During pagination, if there are more locations available to be fetched in the next page, this field is populated with a token to fetch the next page of locations in a subsequent call. If there are no more locations to be fetched, this field is not present in the response. |  [optional] |
|**totalSize** | **Integer** | The total number of recommended locations for this Business Profile account, irrespective of pagination. |  [optional] |



