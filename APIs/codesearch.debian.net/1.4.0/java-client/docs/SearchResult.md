

# SearchResult

A search result matching the specified query. You can use sources.debian.org to view the file contents. See https://github.com/Debian/dcs/blob/master/cmd/dcs-web/show/show.go for how to construct a sources.debian.org URL from a search result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | **String** | The full line containing the search result. |  |
|**contextAfter** | **List&lt;String&gt;** | Up to 2 full lines after the search result (see &#x60;context&#x60;). |  [optional] |
|**contextBefore** | **List&lt;String&gt;** | Up to 2 full lines before the search result (see &#x60;context&#x60;). |  [optional] |
|**line** | **Integer** | Line number containing the search result. |  |
|**_package** | **String** | The Debian source package containing this search result, including the full Debian version number. |  |
|**path** | **String** | Path to the file containing the this search result, starting with &#x60;package&#x60;. |  |



