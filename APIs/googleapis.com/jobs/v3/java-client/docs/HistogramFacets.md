

# HistogramFacets

Input only. Histogram facets to be specified in SearchJobsRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compensationHistogramFacets** | [**List&lt;CompensationHistogramRequest&gt;**](CompensationHistogramRequest.md) | Optional. Specifies compensation field-based histogram requests. Duplicate values of CompensationHistogramRequest.type are not allowed. |  [optional] |
|**customAttributeHistogramFacets** | [**List&lt;CustomAttributeHistogramRequest&gt;**](CustomAttributeHistogramRequest.md) | Optional. Specifies the custom attributes histogram requests. Duplicate values of CustomAttributeHistogramRequest.key are not allowed. |  [optional] |
|**simpleHistogramFacets** | [**List&lt;SimpleHistogramFacetsEnum&gt;**](#List&lt;SimpleHistogramFacetsEnum&gt;) | Optional. Specifies the simple type of histogram facets, for example, &#x60;COMPANY_SIZE&#x60;, &#x60;EMPLOYMENT_TYPE&#x60; etc. |  [optional] |



## Enum: List&lt;SimpleHistogramFacetsEnum&gt;

| Name | Value |
|---- | -----|
| SEARCH_TYPE_UNSPECIFIED | &quot;SEARCH_TYPE_UNSPECIFIED&quot; |
| COMPANY_ID | &quot;COMPANY_ID&quot; |
| EMPLOYMENT_TYPE | &quot;EMPLOYMENT_TYPE&quot; |
| COMPANY_SIZE | &quot;COMPANY_SIZE&quot; |
| DATE_PUBLISHED | &quot;DATE_PUBLISHED&quot; |
| EDUCATION_LEVEL | &quot;EDUCATION_LEVEL&quot; |
| EXPERIENCE_LEVEL | &quot;EXPERIENCE_LEVEL&quot; |
| ADMIN_1 | &quot;ADMIN_1&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| CITY | &quot;CITY&quot; |
| LOCALE | &quot;LOCALE&quot; |
| LANGUAGE | &quot;LANGUAGE&quot; |
| CATEGORY | &quot;CATEGORY&quot; |
| CITY_COORDINATE | &quot;CITY_COORDINATE&quot; |
| ADMIN_1_COUNTRY | &quot;ADMIN_1_COUNTRY&quot; |
| COMPANY_DISPLAY_NAME | &quot;COMPANY_DISPLAY_NAME&quot; |
| BASE_COMPENSATION_UNIT | &quot;BASE_COMPENSATION_UNIT&quot; |



