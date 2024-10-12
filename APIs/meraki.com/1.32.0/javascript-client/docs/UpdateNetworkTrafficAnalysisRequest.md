# MerakiDashboardApi.UpdateNetworkTrafficAnalysisRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customPieChartItems** | [**[UpdateNetworkTrafficAnalysisRequestCustomPieChartItemsInner]**](UpdateNetworkTrafficAnalysisRequestCustomPieChartItemsInner.md) | The list of items that make up the custom pie chart for traffic reporting. | [optional] 
**mode** | **String** |     The traffic analysis mode for the network. Can be one of &#39;disabled&#39; (do not collect traffic types),     &#39;basic&#39; (collect generic traffic categories), or &#39;detailed&#39; (collect destination hostnames).  | [optional] 



## Enum: ModeEnum


* `basic` (value: `"basic"`)

* `detailed` (value: `"detailed"`)

* `disabled` (value: `"disabled"`)




