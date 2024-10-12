

# GoogleAdsSearchads360V0ServicesSearchSearchAds360FieldsResponse

Response message for SearchAds360FieldService.SearchSearchAds360Fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Pagination token used to retrieve the next page of results. Pass the content of this string as the &#x60;page_token&#x60; attribute of the next request. &#x60;next_page_token&#x60; is not returned for the last page. |  [optional] |
|**results** | [**List&lt;GoogleAdsSearchads360V0ResourcesSearchAds360Field&gt;**](GoogleAdsSearchads360V0ResourcesSearchAds360Field.md) | The list of fields that matched the query. |  [optional] |
|**totalResultsCount** | **String** | Total number of results that match the query ignoring the LIMIT clause. |  [optional] |



