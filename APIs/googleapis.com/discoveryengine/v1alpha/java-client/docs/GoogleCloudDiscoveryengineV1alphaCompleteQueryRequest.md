

# GoogleCloudDiscoveryengineV1alphaCompleteQueryRequest

Request message for CompletionService.CompleteQuery method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataStore** | **String** | Required. The parent data store resource name for which the completion is performed, such as &#x60;projects/_*_/locations/global/collections/default_collection/dataStores/default_data_store&#x60;. |  [optional] |
|**includeTailSuggestions** | **Boolean** | Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned. |  [optional] |
|**query** | **String** | Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters. |  [optional] |
|**queryModel** | **String** | Specifies the autocomplete data model. This overrides any model specified in the Configuration &gt; Autocomplete section of the Cloud console. Currently supported values: * &#x60;document&#x60; - Using suggestions generated from user-imported documents. * &#x60;search-history&#x60; - Using suggestions generated from the past history of SearchService.Search API calls. Do not use it when there is no traffic for Search API. * &#x60;user-event&#x60; - Using suggestions generated from user-imported search events. * &#x60;document-completable&#x60; - Using suggestions taken directly from user-imported document fields marked as completable. Default values: * &#x60;document&#x60; is the default model for regular dataStores. * &#x60;search-history&#x60; is the default model for site search dataStores. |  [optional] |
|**userPseudoId** | **String** | A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website. This field should NOT have a fixed value such as &#x60;unknown_visitor&#x60;. This should be the same identifier as UserEvent.user_pseudo_id and SearchRequest.user_pseudo_id. The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. |  [optional] |



