

# CreateConfiguredTableRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the configured table. |  |
|**description** | **String** | A description for the configured table. |  [optional] |
|**tableReference** | [**CreateConfiguredTableRequestTableReference**](CreateConfiguredTableRequestTableReference.md) |  |  |
|**allowedColumns** | **List&lt;String&gt;** | The columns of the underlying table that can be used by collaborations or analysis rules. |  |
|**analysisMethod** | [**AnalysisMethodEnum**](#AnalysisMethodEnum) | The analysis method for the configured tables. The only valid value is currently &#x60;DIRECT_QUERY&#x60;. |  |
|**tags** | **Map&lt;String, String&gt;** | Map of tags assigned to a resource |  [optional] |



## Enum: AnalysisMethodEnum

| Name | Value |
|---- | -----|
| DIRECT_QUERY | &quot;DIRECT_QUERY&quot; |



