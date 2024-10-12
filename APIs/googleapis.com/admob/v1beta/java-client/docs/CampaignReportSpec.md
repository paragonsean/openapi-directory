

# CampaignReportSpec

The specification for generating a Campaign report. For example, the specification to get IMPRESSIONS and CLICKS sliced by CAMPAIGN_ID can look like the following example: { \"date_range\": { \"start_date\": {\"year\": 2021, \"month\": 12, \"day\": 1}, \"end_date\": {\"year\": 2021, \"month\": 12, \"day\": 30} }, \"dimensions\": [\"CAMPAIGN_ID\"], \"metrics\": [\"IMPRESSIONS\", \"CLICKS\"], }

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**dimensions** | [**List&lt;DimensionsEnum&gt;**](#List&lt;DimensionsEnum&gt;) | List of dimensions of the report. The value combination of these dimensions determines the row of the report. If no dimensions are specified, the report returns a single row of requested metrics for the entire account. |  [optional] |
|**languageCode** | **String** | Language used for any localized text, such as certain applicable dimension values. The language tag is defined in the IETF BCP47. Defaults to &#39;en-US&#39; if unspecified or invalid. |  [optional] |
|**metrics** | [**List&lt;MetricsEnum&gt;**](#List&lt;MetricsEnum&gt;) | List of metrics of the report. A report must specify at least one metric. |  [optional] |



## Enum: List&lt;DimensionsEnum&gt;

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| DATE | &quot;DATE&quot; |
| CAMPAIGN_ID | &quot;CAMPAIGN_ID&quot; |
| CAMPAIGN_NAME | &quot;CAMPAIGN_NAME&quot; |
| AD_ID | &quot;AD_ID&quot; |
| AD_NAME | &quot;AD_NAME&quot; |
| PLACEMENT_ID | &quot;PLACEMENT_ID&quot; |
| PLACEMENT_NAME | &quot;PLACEMENT_NAME&quot; |
| PLACEMENT_PLATFORM | &quot;PLACEMENT_PLATFORM&quot; |
| COUNTRY | &quot;COUNTRY&quot; |
| FORMAT | &quot;FORMAT&quot; |



## Enum: List&lt;MetricsEnum&gt;

| Name | Value |
|---- | -----|
| METRIC_UNSPECIFIED | &quot;METRIC_UNSPECIFIED&quot; |
| IMPRESSIONS | &quot;IMPRESSIONS&quot; |
| CLICKS | &quot;CLICKS&quot; |
| CLICK_THROUGH_RATE | &quot;CLICK_THROUGH_RATE&quot; |
| INSTALLS | &quot;INSTALLS&quot; |
| ESTIMATED_COST | &quot;ESTIMATED_COST&quot; |
| AVERAGE_CPI | &quot;AVERAGE_CPI&quot; |
| INTERACTIONS | &quot;INTERACTIONS&quot; |



