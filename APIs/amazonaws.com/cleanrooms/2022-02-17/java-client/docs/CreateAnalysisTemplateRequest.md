

# CreateAnalysisTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the analysis template. |  [optional] |
|**name** | **String** | The name of the analysis template. |  |
|**format** | [**FormatEnum**](#FormatEnum) | The format of the analysis template. |  |
|**source** | [**CreateAnalysisTemplateRequestSource**](CreateAnalysisTemplateRequestSource.md) |  |  |
|**tags** | **Map&lt;String, String&gt;** | Map of tags assigned to a resource |  [optional] |
|**analysisParameters** | [**List&lt;AnalysisParameter&gt;**](AnalysisParameter.md) | The parameters of the analysis template. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| SQL | &quot;SQL&quot; |



