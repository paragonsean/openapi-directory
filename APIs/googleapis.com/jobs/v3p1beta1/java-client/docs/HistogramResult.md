

# HistogramResult

Output only. Result of a histogram call. The response contains the histogram map for the search type specified by HistogramResult.field. The response is a map of each filter value to the corresponding count of jobs for that filter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**searchType** | [**SearchTypeEnum**](#SearchTypeEnum) | The Histogram search filters. |  [optional] |
|**values** | **Map&lt;String, Integer&gt;** | A map from the values of field to the number of jobs with that value in this search result. Key: search type (filter names, such as the companyName). Values: the count of jobs that match the filter for this search. |  [optional] |



## Enum: SearchTypeEnum

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



