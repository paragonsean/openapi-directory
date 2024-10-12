# AzureMediaServices.VideoAnalyzerPreset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insightsToExtract** | **String** | Defines the type of insights that you want the service to generate. The allowed values are &#39;AudioInsightsOnly&#39;, &#39;VideoInsightsOnly&#39;, and &#39;AllInsights&#39;. The default is AllInsights. If you set this to AllInsights and the input is audio only, then only audio insights are generated. Similarly if the input is video only, then only video insights are generated. It is recommended that you not use AudioInsightsOnly if you expect some of your inputs to be video only; or use VideoInsightsOnly if you expect some of your inputs to be audio only. Your Jobs in such conditions would error out. | [optional] 



## Enum: InsightsToExtractEnum


* `AudioInsightsOnly` (value: `"AudioInsightsOnly"`)

* `VideoInsightsOnly` (value: `"VideoInsightsOnly"`)

* `AllInsights` (value: `"AllInsights"`)




