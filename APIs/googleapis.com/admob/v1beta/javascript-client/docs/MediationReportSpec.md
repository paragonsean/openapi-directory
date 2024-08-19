# AdMobApi.MediationReportSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateRange** | [**DateRange**](DateRange.md) |  | [optional] 
**dimensionFilters** | [**[MediationReportSpecDimensionFilter]**](MediationReportSpecDimensionFilter.md) | Describes which report rows to match based on their dimension values. | [optional] 
**dimensions** | **[String]** | List of dimensions of the report. The value combination of these dimensions determines the row of the report. If no dimensions are specified, the report returns a single row of requested metrics for the entire account. | [optional] 
**localizationSettings** | [**LocalizationSettings**](LocalizationSettings.md) |  | [optional] 
**maxReportRows** | **Number** | Maximum number of report data rows to return. If the value is not set, the API returns as many rows as possible, up to 100000. Acceptable values are 1-100000, inclusive. Values larger than 100000 return an error. | [optional] 
**metrics** | **[String]** | List of metrics of the report. A report must specify at least one metric. | [optional] 
**sortConditions** | [**[MediationReportSpecSortCondition]**](MediationReportSpecSortCondition.md) | Describes the sorting of report rows. The order of the condition in the list defines its precedence; the earlier the condition, the higher its precedence. If no sort conditions are specified, the row ordering is undefined. | [optional] 
**timeZone** | **String** | A report time zone. Accepts an IANA TZ name values, such as \&quot;America/Los_Angeles.\&quot; If no time zone is defined, the account default takes effect. Check default value by the get account action. **Warning:** The \&quot;America/Los_Angeles\&quot; is the only supported value at the moment. | [optional] 



## Enum: [DimensionsEnum]


* `DIMENSION_UNSPECIFIED` (value: `"DIMENSION_UNSPECIFIED"`)

* `DATE` (value: `"DATE"`)

* `MONTH` (value: `"MONTH"`)

* `WEEK` (value: `"WEEK"`)

* `AD_SOURCE` (value: `"AD_SOURCE"`)

* `AD_SOURCE_INSTANCE` (value: `"AD_SOURCE_INSTANCE"`)

* `AD_UNIT` (value: `"AD_UNIT"`)

* `APP` (value: `"APP"`)

* `MEDIATION_GROUP` (value: `"MEDIATION_GROUP"`)

* `COUNTRY` (value: `"COUNTRY"`)

* `FORMAT` (value: `"FORMAT"`)

* `PLATFORM` (value: `"PLATFORM"`)

* `MOBILE_OS_VERSION` (value: `"MOBILE_OS_VERSION"`)

* `GMA_SDK_VERSION` (value: `"GMA_SDK_VERSION"`)

* `APP_VERSION_NAME` (value: `"APP_VERSION_NAME"`)

* `SERVING_RESTRICTION` (value: `"SERVING_RESTRICTION"`)





## Enum: [MetricsEnum]


* `METRIC_UNSPECIFIED` (value: `"METRIC_UNSPECIFIED"`)

* `AD_REQUESTS` (value: `"AD_REQUESTS"`)

* `CLICKS` (value: `"CLICKS"`)

* `ESTIMATED_EARNINGS` (value: `"ESTIMATED_EARNINGS"`)

* `IMPRESSIONS` (value: `"IMPRESSIONS"`)

* `IMPRESSION_CTR` (value: `"IMPRESSION_CTR"`)

* `MATCHED_REQUESTS` (value: `"MATCHED_REQUESTS"`)

* `MATCH_RATE` (value: `"MATCH_RATE"`)

* `OBSERVED_ECPM` (value: `"OBSERVED_ECPM"`)




