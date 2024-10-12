

# SearchFreetextRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | **currency code** for the currency in which to display product pricing information |  [optional] |
|**destId** | **Integer** | **unique numeric identifier** of the destination to search within  - &#x60;destinationId&#x60; can be retrieved from the [/taxonomy/destinations](#operation/taxonomyDestinations) service  |  [optional] |
|**searchTypes** | [**List&lt;SearchTypesEnum&gt;**](#List&lt;SearchTypesEnum&gt;) | **array** of search domain specifiers where each item is *one of*:   - &#x60;\&quot;PRODUCT\&quot;&#x60;: a tour / activity   - &#x60;\&quot;DESTINATION\&quot;&#x60;: continent, country, city, region   - &#x60;\&quot;ATTRACTION\&quot;&#x60;: an attraction within a destination (only available to partners with SEO access)   - &#x60;\&quot;RECOMMENDATION\&quot;&#x60;: an attraction within a destination (only available to partners with SEO access)  |  [optional] |
|**sortOrder** | **SortOrder** |  |  [optional] |
|**text** | **String** | **text** to search for |  [optional] |
|**topX** | **String** | **start and end rows** to return in the format {start}-{end} - e.g. &#x60;&#39;1-10&#39;&#x60;, &#x60;&#39;11-20&#39;&#x60;  **Note**:  - the maximum number of rows per request is 100; therefore, &#x60;&#39;100-400&#39;&#x60; will return the same as &#x60;&#39;100-200&#39;&#x60; - if &#x60;topX&#x60; is not specified, the default is &#x60;&#39;1-100&#39;&#x60;  |  [optional] |



## Enum: List&lt;SearchTypesEnum&gt;

| Name | Value |
|---- | -----|
| PRODUCT | &quot;PRODUCT&quot; |
| DESTINATION | &quot;DESTINATION&quot; |
| ATTRACTION | &quot;ATTRACTION&quot; |
| RECOMMENDATION | &quot;RECOMMENDATION&quot; |



