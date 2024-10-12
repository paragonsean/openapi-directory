# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1alphaSearchInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **Number** | An integer that specifies the current offset for pagination (the 0-indexed starting location, amongst the products deemed by the API as relevant). See SearchRequest.offset for definition. If this field is negative, an &#x60;INVALID_ARGUMENT&#x60; is returned. This can only be set for &#x60;search&#x60; events. Other event types should not set this field. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. | [optional] 
**orderBy** | **String** | The order in which products are returned, if applicable. See SearchRequest.order_by for definition and syntax. The value must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. This can only be set for &#x60;search&#x60; events. Other event types should not set this field. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. | [optional] 
**searchQuery** | **String** | The user&#39;s search query. See SearchRequest.query for definition. The value must be a UTF-8 encoded string with a length limit of 5,000 characters. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. At least one of search_query or PageInfo.page_category is required for &#x60;search&#x60; events. Other event types should not set this field. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. | [optional] 


