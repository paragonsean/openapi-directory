# DebianCodeSearch.SearchResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **String** | The full line containing the search result. | 
**contextAfter** | **[String]** | Up to 2 full lines after the search result (see &#x60;context&#x60;). | [optional] 
**contextBefore** | **[String]** | Up to 2 full lines before the search result (see &#x60;context&#x60;). | [optional] 
**line** | **Number** | Line number containing the search result. | 
**_package** | **String** | The Debian source package containing this search result, including the full Debian version number. | 
**path** | **String** | Path to the file containing the this search result, starting with &#x60;package&#x60;. | 


