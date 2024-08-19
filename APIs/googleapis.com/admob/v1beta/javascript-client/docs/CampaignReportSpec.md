# AdMobApi.CampaignReportSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateRange** | [**DateRange**](DateRange.md) |  | [optional] 
**dimensions** | **[String]** | List of dimensions of the report. The value combination of these dimensions determines the row of the report. If no dimensions are specified, the report returns a single row of requested metrics for the entire account. | [optional] 
**languageCode** | **String** | Language used for any localized text, such as certain applicable dimension values. The language tag is defined in the IETF BCP47. Defaults to &#39;en-US&#39; if unspecified or invalid. | [optional] 
**metrics** | **[String]** | List of metrics of the report. A report must specify at least one metric. | [optional] 



## Enum: [DimensionsEnum]


* `DIMENSION_UNSPECIFIED` (value: `"DIMENSION_UNSPECIFIED"`)

* `DATE` (value: `"DATE"`)

* `CAMPAIGN_ID` (value: `"CAMPAIGN_ID"`)

* `CAMPAIGN_NAME` (value: `"CAMPAIGN_NAME"`)

* `AD_ID` (value: `"AD_ID"`)

* `AD_NAME` (value: `"AD_NAME"`)

* `PLACEMENT_ID` (value: `"PLACEMENT_ID"`)

* `PLACEMENT_NAME` (value: `"PLACEMENT_NAME"`)

* `PLACEMENT_PLATFORM` (value: `"PLACEMENT_PLATFORM"`)

* `COUNTRY` (value: `"COUNTRY"`)

* `FORMAT` (value: `"FORMAT"`)





## Enum: [MetricsEnum]


* `METRIC_UNSPECIFIED` (value: `"METRIC_UNSPECIFIED"`)

* `IMPRESSIONS` (value: `"IMPRESSIONS"`)

* `CLICKS` (value: `"CLICKS"`)

* `CLICK_THROUGH_RATE` (value: `"CLICK_THROUGH_RATE"`)

* `INSTALLS` (value: `"INSTALLS"`)

* `ESTIMATED_COST` (value: `"ESTIMATED_COST"`)

* `AVERAGE_CPI` (value: `"AVERAGE_CPI"`)

* `INTERACTIONS` (value: `"INTERACTIONS"`)




