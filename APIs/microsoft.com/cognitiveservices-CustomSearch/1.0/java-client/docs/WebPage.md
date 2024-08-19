

# WebPage

Defines a webpage that is relevant to the query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateLastCrawled** | **String** | The last time that Bing crawled the webpage. The date is in the form, YYYY-MM-DDTHH:MM:SS. For example, 2015-04-13T05:23:39. |  [optional] [readonly] |
|**deepLinks** | [**List&lt;WebPage&gt;**](WebPage.md) | A list of links to related content that Bing found in the website that contains this webpage. The Webpage object in this context includes only the name, url, urlPingSuffix, and snippet fields. |  [optional] [readonly] |
|**displayUrl** | **String** | The display URL of the webpage. The URL is meant for display purposes only and is not well formed. |  [optional] [readonly] |
|**searchTags** | [**List&lt;WebMetaTag&gt;**](WebMetaTag.md) | A list of search tags that the webpage owner specified on the webpage. The API returns only indexed search tags. The name field of the MetaTag object contains the indexed search tag. Search tags begin with search.* (for example, search.assetId). The content field contains the tag&#39;s value. |  [optional] [readonly] |
|**snippet** | **String** | A snippet of text from the webpage that describes its contents. |  [optional] [readonly] |



