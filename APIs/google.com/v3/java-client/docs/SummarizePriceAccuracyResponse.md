

# SummarizePriceAccuracyResponse

Response message for PriceAccuracyViewService.SummarizePriceAccuracy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentBookOnGoogleScore** | [**CurrentBookOnGoogleScoreEnum**](#CurrentBookOnGoogleScoreEnum) | The current Book on Google price accuracy score. |  [optional] |
|**currentOverallScore** | [**CurrentOverallScoreEnum**](#CurrentOverallScoreEnum) | The current price accuracy score combining both website and Book on Google scores. |  [optional] |
|**currentScore** | [**CurrentScoreEnum**](#CurrentScoreEnum) | The current price accuracy score. Contains the same value as &#x60;current_website_score&#x60;. For clarity, use either &#x60;current_website_score&#x60; or &#39;current_overall_score&#x60; depending upon which is needed. |  [optional] |
|**currentWebsiteScore** | [**CurrentWebsiteScoreEnum**](#CurrentWebsiteScoreEnum) | The current website price accuracy score. |  [optional] |
|**predictedBookOnGoogleScore** | [**PredictedBookOnGoogleScoreEnum**](#PredictedBookOnGoogleScoreEnum) | The predicted Book on Google price accuracy score. |  [optional] |
|**predictedOverallScore** | [**PredictedOverallScoreEnum**](#PredictedOverallScoreEnum) | The predicted price accuracy score combining both website and Book on Google scores. |  [optional] |
|**predictedScore** | [**PredictedScoreEnum**](#PredictedScoreEnum) | The predicted price accuracy score. Contains the same value as &#x60;predicted_website_score&#x60;. For clarity, use either &#x60;predicted_website_score&#x60; or &#39;predicted_overall_score&#x60; depending upon which is needed. |  [optional] |
|**predictedWebsiteScore** | [**PredictedWebsiteScoreEnum**](#PredictedWebsiteScoreEnum) | The predicted website price accuracy score. |  [optional] |
|**updateTime** | **String** | The update timestamp for the current score. |  [optional] |



## Enum: CurrentBookOnGoogleScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: CurrentOverallScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: CurrentScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: CurrentWebsiteScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: PredictedBookOnGoogleScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: PredictedOverallScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: PredictedScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: PredictedWebsiteScoreEnum

| Name | Value |
|---- | -----|
| PRICE_ACCURACY_STATE_UNSPECIFIED | &quot;PRICE_ACCURACY_STATE_UNSPECIFIED&quot; |
| PRICE_ACCURACY_STATE_UNKNOWN | &quot;PRICE_ACCURACY_STATE_UNKNOWN&quot; |
| EXCELLENT | &quot;EXCELLENT&quot; |
| GOOD | &quot;GOOD&quot; |
| POOR | &quot;POOR&quot; |
| AT_RISK | &quot;AT_RISK&quot; |
| FAILED | &quot;FAILED&quot; |



