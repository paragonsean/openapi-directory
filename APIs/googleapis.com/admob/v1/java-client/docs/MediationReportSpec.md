

# MediationReportSpec

The specification for generating an AdMob Mediation report. For example, the specification to get observed ECPM sliced by ad source and app for the 'US' and 'CN' countries can look like the following example: { \"date_range\": { \"start_date\": {\"year\": 2021, \"month\": 9, \"day\": 1}, \"end_date\": {\"year\": 2021, \"month\": 9, \"day\": 30} }, \"dimensions\": [\"AD_SOURCE\", \"APP\", \"COUNTRY\"], \"metrics\": [\"OBSERVED_ECPM\"], \"dimension_filters\": [ { \"dimension\": \"COUNTRY\", \"matches_any\": {\"values\": [{\"value\": \"US\", \"value\": \"CN\"}]} } ], \"sort_conditions\": [ {\"dimension\":\"APP\", order: \"ASCENDING\"} ], \"localization_settings\": { \"currency_code\": \"USD\", \"language_code\": \"en-US\" } } For a better understanding, you can treat the preceding specification like the following pseudo SQL: SELECT AD_SOURCE, APP, COUNTRY, OBSERVED_ECPM FROM MEDIATION_REPORT WHERE DATE >= '2021-09-01' AND DATE <= '2021-09-30' AND COUNTRY IN ('US', 'CN') GROUP BY AD_SOURCE, APP, COUNTRY ORDER BY APP ASC;

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**dimensionFilters** | [**List&lt;MediationReportSpecDimensionFilter&gt;**](MediationReportSpecDimensionFilter.md) | Describes which report rows to match based on their dimension values. |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions of the report. The value combination of these dimensions determines the row of the report. If no dimensions are specified, the report returns a single row of requested metrics for the entire account. |  [optional] |
|**localizationSettings** | [**LocalizationSettings**](LocalizationSettings.md) |  |  [optional] |
|**maxReportRows** | **Integer** | Maximum number of report data rows to return. If the value is not set, the API returns as many rows as possible, up to 100000. Acceptable values are 1-100000, inclusive. Values larger than 100000 return an error. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics of the report. A report must specify at least one metric. |  [optional] |
|**sortConditions** | [**List&lt;MediationReportSpecSortCondition&gt;**](MediationReportSpecSortCondition.md) | Describes the sorting of report rows. The order of the condition in the list defines its precedence; the earlier the condition, the higher its precedence. If no sort conditions are specified, the row ordering is undefined. |  [optional] |
|**timeZone** | **String** | A report time zone. Accepts an IANA TZ name values, such as \&quot;America/Los_Angeles.\&quot; If no time zone is defined, the account default takes effect. Check default value by the get account action. **Warning:** The \&quot;America/Los_Angeles\&quot; is the only supported value at the moment. |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| DATE | &quot;DATE&quot; |
| MONTH | &quot;MONTH&quot; |
| WEEK | &quot;WEEK&quot; |
| AD_SOURCE | &quot;AD_SOURCE&quot; |
| AD_SOURCE_INSTANCE | &quot;AD_SOURCE_INSTANCE&quot; |
| AD_UNIT | &quot;AD_UNIT&quot; |
| APP | &quot;APP&quot; |
| MEDIATION_GROUP | &quot;MEDIATION_GROUP&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| FORMAT | &quot;FORMAT&quot; |
| PLATFORM | &quot;PLATFORM&quot; |
| MOBILE_OS_VERSION | &quot;MOBILE_OS_VERSION&quot; |
| GMA_SDK_VERSION | &quot;GMA_SDK_VERSION&quot; |
| APP_VERSION_NAME | &quot;APP_VERSION_NAME&quot; |
| SERVING_RESTRICTION | &quot;SERVING_RESTRICTION&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| METRIC_UNSPECIFIED | &quot;METRIC_UNSPECIFIED&quot; |
| AD_REQUESTS | &quot;AD_REQUESTS&quot; |
| CLICKS | &quot;CLICKS&quot; |
| ESTIMATED_EARNINGS | &quot;ESTIMATED_EARNINGS&quot; |
| IMPRESSIONS | &quot;IMPRESSIONS&quot; |
| IMPRESSION_CTR | &quot;IMPRESSION_CTR&quot; |
| MATCHED_REQUESTS | &quot;MATCHED_REQUESTS&quot; |
| MATCH_RATE | &quot;MATCH_RATE&quot; |
| OBSERVED_ECPM | &quot;OBSERVED_ECPM&quot; |



