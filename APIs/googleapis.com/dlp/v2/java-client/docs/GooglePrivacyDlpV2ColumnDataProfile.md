

# GooglePrivacyDlpV2ColumnDataProfile

The profile for a scanned column within a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **String** | The name of the column. |  [optional] |
|**columnInfoType** | [**GooglePrivacyDlpV2InfoTypeSummary**](GooglePrivacyDlpV2InfoTypeSummary.md) |  |  [optional] |
|**columnType** | [**ColumnTypeEnum**](#ColumnTypeEnum) | The data type of a given column. |  [optional] |
|**dataRiskLevel** | [**GooglePrivacyDlpV2DataRiskLevel**](GooglePrivacyDlpV2DataRiskLevel.md) |  |  [optional] |
|**datasetId** | **String** | The BigQuery dataset ID. |  [optional] |
|**datasetLocation** | **String** | The BigQuery location where the dataset&#39;s data is stored. See https://cloud.google.com/bigquery/docs/locations for supported locations. |  [optional] |
|**datasetProjectId** | **String** | The Google Cloud project ID that owns the profiled resource. |  [optional] |
|**estimatedNullPercentage** | [**EstimatedNullPercentageEnum**](#EstimatedNullPercentageEnum) | Approximate percentage of entries being null in the column. |  [optional] |
|**estimatedUniquenessScore** | [**EstimatedUniquenessScoreEnum**](#EstimatedUniquenessScoreEnum) | Approximate uniqueness of the column. |  [optional] |
|**freeTextScore** | **Double** | The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1. |  [optional] |
|**name** | **String** | The name of the profile. |  [optional] |
|**otherMatches** | [**List&lt;GooglePrivacyDlpV2OtherInfoTypeSummary&gt;**](GooglePrivacyDlpV2OtherInfoTypeSummary.md) | Other types found within this column. List will be unordered. |  [optional] |
|**policyState** | [**PolicyStateEnum**](#PolicyStateEnum) | Indicates if a policy tag has been applied to the column. |  [optional] |
|**profileLastGenerated** | **String** | The last time the profile was generated. |  [optional] |
|**profileStatus** | [**GooglePrivacyDlpV2ProfileStatus**](GooglePrivacyDlpV2ProfileStatus.md) |  |  [optional] |
|**sensitivityScore** | [**GooglePrivacyDlpV2SensitivityScore**](GooglePrivacyDlpV2SensitivityScore.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of a profile. |  [optional] |
|**tableDataProfile** | **String** | The resource name of the table data profile. |  [optional] |
|**tableFullResource** | **String** | The resource name of the resource this column is within. |  [optional] |
|**tableId** | **String** | The BigQuery table ID. |  [optional] |



## Enum: ColumnTypeEnum

| Name | Value |
|---- | -----|
| COLUMN_DATA_TYPE_UNSPECIFIED | &quot;COLUMN_DATA_TYPE_UNSPECIFIED&quot; |
| TYPE_INT64 | &quot;TYPE_INT64&quot; |
| TYPE_BOOL | &quot;TYPE_BOOL&quot; |
| TYPE_FLOAT64 | &quot;TYPE_FLOAT64&quot; |
| TYPE_STRING | &quot;TYPE_STRING&quot; |
| TYPE_BYTES | &quot;TYPE_BYTES&quot; |
| TYPE_TIMESTAMP | &quot;TYPE_TIMESTAMP&quot; |
| TYPE_DATE | &quot;TYPE_DATE&quot; |
| TYPE_TIME | &quot;TYPE_TIME&quot; |
| TYPE_DATETIME | &quot;TYPE_DATETIME&quot; |
| TYPE_GEOGRAPHY | &quot;TYPE_GEOGRAPHY&quot; |
| TYPE_NUMERIC | &quot;TYPE_NUMERIC&quot; |
| TYPE_RECORD | &quot;TYPE_RECORD&quot; |
| TYPE_BIGNUMERIC | &quot;TYPE_BIGNUMERIC&quot; |
| TYPE_JSON | &quot;TYPE_JSON&quot; |



## Enum: EstimatedNullPercentageEnum

| Name | Value |
|---- | -----|
| LEVEL_UNSPECIFIED | &quot;NULL_PERCENTAGE_LEVEL_UNSPECIFIED&quot; |
| VERY_LOW | &quot;NULL_PERCENTAGE_VERY_LOW&quot; |
| LOW | &quot;NULL_PERCENTAGE_LOW&quot; |
| MEDIUM | &quot;NULL_PERCENTAGE_MEDIUM&quot; |
| HIGH | &quot;NULL_PERCENTAGE_HIGH&quot; |



## Enum: EstimatedUniquenessScoreEnum

| Name | Value |
|---- | -----|
| LEVEL_UNSPECIFIED | &quot;UNIQUENESS_SCORE_LEVEL_UNSPECIFIED&quot; |
| LOW | &quot;UNIQUENESS_SCORE_LOW&quot; |
| MEDIUM | &quot;UNIQUENESS_SCORE_MEDIUM&quot; |
| HIGH | &quot;UNIQUENESS_SCORE_HIGH&quot; |



## Enum: PolicyStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;COLUMN_POLICY_STATE_UNSPECIFIED&quot; |
| TAGGED | &quot;COLUMN_POLICY_TAGGED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |



