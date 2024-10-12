# CustomSearchApi.Result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cacheId** | **String** | Indicates the ID of Google&#39;s cached version of the search result. | [optional] 
**displayLink** | **String** | An abridged version of this search result’s URL, e.g. www.example.com. | [optional] 
**fileFormat** | **String** | The file format of the search result. | [optional] 
**formattedUrl** | **String** | The URL displayed after the snippet for each search result. | [optional] 
**htmlFormattedUrl** | **String** | The HTML-formatted URL displayed after the snippet for each search result. | [optional] 
**htmlSnippet** | **String** | The snippet of the search result, in HTML. | [optional] 
**htmlTitle** | **String** | The title of the search result, in HTML. | [optional] 
**image** | [**ResultImage**](ResultImage.md) |  | [optional] 
**kind** | **String** | A unique identifier for the type of current object. For this API, it is &#x60;customsearch#result.&#x60; | [optional] 
**labels** | [**[ResultLabelsInner]**](ResultLabelsInner.md) | Encapsulates all information about refinement labels. | [optional] 
**link** | **String** | The full URL to which the search result is pointing, e.g. http://www.example.com/foo/bar. | [optional] 
**mime** | **String** | The MIME type of the search result. | [optional] 
**pagemap** | **{String: Object}** | Contains [PageMap](https://developers.google.com/custom-search/docs/structured_data#pagemaps) information for this search result. | [optional] 
**snippet** | **String** | The snippet of the search result, in plain text. | [optional] 
**title** | **String** | The title of the search result, in plain text. | [optional] 


