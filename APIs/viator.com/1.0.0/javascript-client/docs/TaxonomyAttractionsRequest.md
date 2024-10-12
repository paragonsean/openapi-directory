# ViatorApiDocumentationAmpSpecificationMerchantPartners.TaxonomyAttractionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destId** | **Number** | **unique numeric identifier** of the destination in which to search for attractions | [optional] 
**sortOrder** | **String** | **sort order** in which to return the results that is *one of*:   * &#x60;\&quot;SEO_PUBLISHED_DATE_D\&quot;&#x60;: publish date (descending)   * &#x60;\&quot;SEO_PUBLISHED_DATE_A\&quot;&#x60;: publish date (ascending)   * &#x60;\&quot;SEO_REVIEW_AVG_RATING_D\&quot;&#x60;: traveler rating (high→low)   * &#x60;\&quot;SEO_REVIEW_AVG_RATING_A\&quot;&#x60;: traveler rating (low→high)   * &#x60;\&quot;SEO_ALPHABETICAL\&quot;&#x60;: alphabetical (A→Z)  | [optional] 
**topX** | **String** | **start and end rows** to return in the format {start}-{end} - e.g. &#x60;&#39;1-10&#39;&#x60;, &#x60;&#39;11-20&#39;&#x60;  **Note**:  - the maximum number of rows per request is 100; therefore, &#x60;&#39;100-400&#39;&#x60; will return the same as &#x60;&#39;100-200&#39;&#x60; - if &#x60;topX&#x60; is not specified, the default is &#x60;&#39;1-100&#39;&#x60;  | [optional] 



## Enum: SortOrderEnum


* `PUBLISHED_DATE_D` (value: `"SEO_PUBLISHED_DATE_D"`)

* `PUBLISHED_DATE_A` (value: `"SEO_PUBLISHED_DATE_A"`)

* `REVIEW_AVG_RATING_D` (value: `"SEO_REVIEW_AVG_RATING_D"`)

* `REVIEW_AVG_RATING_A` (value: `"SEO_REVIEW_AVG_RATING_A"`)

* `ALPHABETICAL` (value: `"SEO_ALPHABETICAL"`)




