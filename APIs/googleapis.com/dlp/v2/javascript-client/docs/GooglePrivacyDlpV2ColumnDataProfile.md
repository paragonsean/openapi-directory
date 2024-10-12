# SensitiveDataProtectionDlp.GooglePrivacyDlpV2ColumnDataProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **String** | The name of the column. | [optional] 
**columnInfoType** | [**GooglePrivacyDlpV2InfoTypeSummary**](GooglePrivacyDlpV2InfoTypeSummary.md) |  | [optional] 
**columnType** | **String** | The data type of a given column. | [optional] 
**dataRiskLevel** | [**GooglePrivacyDlpV2DataRiskLevel**](GooglePrivacyDlpV2DataRiskLevel.md) |  | [optional] 
**datasetId** | **String** | The BigQuery dataset ID. | [optional] 
**datasetLocation** | **String** | The BigQuery location where the dataset&#39;s data is stored. See https://cloud.google.com/bigquery/docs/locations for supported locations. | [optional] 
**datasetProjectId** | **String** | The Google Cloud project ID that owns the profiled resource. | [optional] 
**estimatedNullPercentage** | **String** | Approximate percentage of entries being null in the column. | [optional] 
**estimatedUniquenessScore** | **String** | Approximate uniqueness of the column. | [optional] 
**freeTextScore** | **Number** | The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1. | [optional] 
**name** | **String** | The name of the profile. | [optional] 
**otherMatches** | [**[GooglePrivacyDlpV2OtherInfoTypeSummary]**](GooglePrivacyDlpV2OtherInfoTypeSummary.md) | Other types found within this column. List will be unordered. | [optional] 
**policyState** | **String** | Indicates if a policy tag has been applied to the column. | [optional] 
**profileLastGenerated** | **String** | The last time the profile was generated. | [optional] 
**profileStatus** | [**GooglePrivacyDlpV2ProfileStatus**](GooglePrivacyDlpV2ProfileStatus.md) |  | [optional] 
**sensitivityScore** | [**GooglePrivacyDlpV2SensitivityScore**](GooglePrivacyDlpV2SensitivityScore.md) |  | [optional] 
**state** | **String** | State of a profile. | [optional] 
**tableDataProfile** | **String** | The resource name of the table data profile. | [optional] 
**tableFullResource** | **String** | The resource name of the resource this column is within. | [optional] 
**tableId** | **String** | The BigQuery table ID. | [optional] 



## Enum: ColumnTypeEnum


* `COLUMN_DATA_TYPE_UNSPECIFIED` (value: `"COLUMN_DATA_TYPE_UNSPECIFIED"`)

* `TYPE_INT64` (value: `"TYPE_INT64"`)

* `TYPE_BOOL` (value: `"TYPE_BOOL"`)

* `TYPE_FLOAT64` (value: `"TYPE_FLOAT64"`)

* `TYPE_STRING` (value: `"TYPE_STRING"`)

* `TYPE_BYTES` (value: `"TYPE_BYTES"`)

* `TYPE_TIMESTAMP` (value: `"TYPE_TIMESTAMP"`)

* `TYPE_DATE` (value: `"TYPE_DATE"`)

* `TYPE_TIME` (value: `"TYPE_TIME"`)

* `TYPE_DATETIME` (value: `"TYPE_DATETIME"`)

* `TYPE_GEOGRAPHY` (value: `"TYPE_GEOGRAPHY"`)

* `TYPE_NUMERIC` (value: `"TYPE_NUMERIC"`)

* `TYPE_RECORD` (value: `"TYPE_RECORD"`)

* `TYPE_BIGNUMERIC` (value: `"TYPE_BIGNUMERIC"`)

* `TYPE_JSON` (value: `"TYPE_JSON"`)





## Enum: EstimatedNullPercentageEnum


* `LEVEL_UNSPECIFIED` (value: `"NULL_PERCENTAGE_LEVEL_UNSPECIFIED"`)

* `VERY_LOW` (value: `"NULL_PERCENTAGE_VERY_LOW"`)

* `LOW` (value: `"NULL_PERCENTAGE_LOW"`)

* `MEDIUM` (value: `"NULL_PERCENTAGE_MEDIUM"`)

* `HIGH` (value: `"NULL_PERCENTAGE_HIGH"`)





## Enum: EstimatedUniquenessScoreEnum


* `LEVEL_UNSPECIFIED` (value: `"UNIQUENESS_SCORE_LEVEL_UNSPECIFIED"`)

* `LOW` (value: `"UNIQUENESS_SCORE_LOW"`)

* `MEDIUM` (value: `"UNIQUENESS_SCORE_MEDIUM"`)

* `HIGH` (value: `"UNIQUENESS_SCORE_HIGH"`)





## Enum: PolicyStateEnum


* `STATE_UNSPECIFIED` (value: `"COLUMN_POLICY_STATE_UNSPECIFIED"`)

* `TAGGED` (value: `"COLUMN_POLICY_TAGGED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)




