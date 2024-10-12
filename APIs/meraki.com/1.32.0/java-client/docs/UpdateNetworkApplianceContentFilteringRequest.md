

# UpdateNetworkApplianceContentFilteringRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedUrlPatterns** | **List&lt;String&gt;** | A list of URL patterns that are allowed |  [optional] |
|**blockedUrlCategories** | **List&lt;String&gt;** | A list of URL categories to block |  [optional] |
|**blockedUrlPatterns** | **List&lt;String&gt;** | A list of URL patterns that are blocked |  [optional] |
|**urlCategoryListSize** | [**UrlCategoryListSizeEnum**](#UrlCategoryListSizeEnum) | URL category list size which is either &#39;topSites&#39; or &#39;fullList&#39; |  [optional] |



## Enum: UrlCategoryListSizeEnum

| Name | Value |
|---- | -----|
| FULL_LIST | &quot;fullList&quot; |
| TOP_SITES | &quot;topSites&quot; |



