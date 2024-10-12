

# MetricRequest

A request to return values for one metric and the options for how those values should be returned.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metric** | [**MetricEnum**](#MetricEnum) | The requested metric. |  [optional] |
|**options** | [**List&lt;OptionsEnum&gt;**](#List&lt;OptionsEnum&gt;) | How the values should appear when returned. |  [optional] |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| METRIC_UNSPECIFIED | &quot;METRIC_UNSPECIFIED&quot; |
| ALL | &quot;ALL&quot; |
| QUERIES_DIRECT | &quot;QUERIES_DIRECT&quot; |
| QUERIES_INDIRECT | &quot;QUERIES_INDIRECT&quot; |
| QUERIES_CHAIN | &quot;QUERIES_CHAIN&quot; |
| VIEWS_MAPS | &quot;VIEWS_MAPS&quot; |
| VIEWS_SEARCH | &quot;VIEWS_SEARCH&quot; |
| ACTIONS_WEBSITE | &quot;ACTIONS_WEBSITE&quot; |
| ACTIONS_PHONE | &quot;ACTIONS_PHONE&quot; |
| ACTIONS_DRIVING_DIRECTIONS | &quot;ACTIONS_DRIVING_DIRECTIONS&quot; |
| PHOTOS_VIEWS_MERCHANT | &quot;PHOTOS_VIEWS_MERCHANT&quot; |
| PHOTOS_VIEWS_CUSTOMERS | &quot;PHOTOS_VIEWS_CUSTOMERS&quot; |
| PHOTOS_COUNT_MERCHANT | &quot;PHOTOS_COUNT_MERCHANT&quot; |
| PHOTOS_COUNT_CUSTOMERS | &quot;PHOTOS_COUNT_CUSTOMERS&quot; |
| LOCAL_POST_VIEWS_SEARCH | &quot;LOCAL_POST_VIEWS_SEARCH&quot; |
| LOCAL_POST_ACTIONS_CALL_TO_ACTION | &quot;LOCAL_POST_ACTIONS_CALL_TO_ACTION&quot; |



## Enum: List&lt;OptionsEnum&gt;

| Name | Value |
|---- | -----|
| METRIC_OPTION_UNSPECIFIED | &quot;METRIC_OPTION_UNSPECIFIED&quot; |
| AGGREGATED_TOTAL | &quot;AGGREGATED_TOTAL&quot; |
| AGGREGATED_DAILY | &quot;AGGREGATED_DAILY&quot; |
| BREAKDOWN_DAY_OF_WEEK | &quot;BREAKDOWN_DAY_OF_WEEK&quot; |
| BREAKDOWN_HOUR_OF_DAY | &quot;BREAKDOWN_HOUR_OF_DAY&quot; |



