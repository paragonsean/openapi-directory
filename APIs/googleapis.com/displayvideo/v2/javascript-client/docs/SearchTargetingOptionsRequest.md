# DisplayVideo360Api.SearchTargetingOptionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserId** | **String** | Required. The Advertiser this request is being made in the context of. | [optional] 
**businessChainSearchTerms** | [**BusinessChainSearchTerms**](BusinessChainSearchTerms.md) |  | [optional] 
**geoRegionSearchTerms** | [**GeoRegionSearchTerms**](GeoRegionSearchTerms.md) |  | [optional] 
**pageSize** | **Number** | Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] 
**pageToken** | **String** | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;SearchTargetingOptions&#x60; method. If not specified, the first page of results will be returned. | [optional] 
**poiSearchTerms** | [**PoiSearchTerms**](PoiSearchTerms.md) |  | [optional] 


