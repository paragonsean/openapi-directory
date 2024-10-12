# SensitiveDataProtectionDlp.GooglePrivacyDlpV2TableDataProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configSnapshot** | [**GooglePrivacyDlpV2DataProfileConfigSnapshot**](GooglePrivacyDlpV2DataProfileConfigSnapshot.md) |  | [optional] 
**createTime** | **String** | The time at which the table was created. | [optional] 
**dataRiskLevel** | [**GooglePrivacyDlpV2DataRiskLevel**](GooglePrivacyDlpV2DataRiskLevel.md) |  | [optional] 
**dataSourceType** | [**GooglePrivacyDlpV2DataSourceType**](GooglePrivacyDlpV2DataSourceType.md) |  | [optional] 
**datasetId** | **String** | If the resource is BigQuery, the dataset ID. | [optional] 
**datasetLocation** | **String** | If supported, the location where the dataset&#39;s data is stored. See https://cloud.google.com/bigquery/docs/locations for supported locations. | [optional] 
**datasetProjectId** | **String** | The Google Cloud project ID that owns the resource. | [optional] 
**encryptionStatus** | **String** | How the table is encrypted. | [optional] 
**expirationTime** | **String** | Optional. The time when this table expires. | [optional] 
**failedColumnCount** | **String** | The number of columns skipped in the table because of an error. | [optional] 
**fullResource** | **String** | The resource name of the resource profiled. https://cloud.google.com/apis/design/resource_names#full_resource_name | [optional] 
**lastModifiedTime** | **String** | The time when this table was last modified | [optional] 
**name** | **String** | The name of the profile. | [optional] 
**otherInfoTypes** | [**[GooglePrivacyDlpV2OtherInfoTypeSummary]**](GooglePrivacyDlpV2OtherInfoTypeSummary.md) | Other infoTypes found in this table&#39;s data. | [optional] 
**predictedInfoTypes** | [**[GooglePrivacyDlpV2InfoTypeSummary]**](GooglePrivacyDlpV2InfoTypeSummary.md) | The infoTypes predicted from this table&#39;s data. | [optional] 
**profileLastGenerated** | **String** | The last time the profile was generated. | [optional] 
**profileStatus** | [**GooglePrivacyDlpV2ProfileStatus**](GooglePrivacyDlpV2ProfileStatus.md) |  | [optional] 
**projectDataProfile** | **String** | The resource name to the project data profile for this table. | [optional] 
**resourceLabels** | **{String: String}** | The labels applied to the resource at the time the profile was generated. | [optional] 
**resourceVisibility** | **String** | How broadly a resource has been shared. | [optional] 
**rowCount** | **String** | Number of rows in the table when the profile was generated. This will not be populated for BigLake tables. | [optional] 
**scannedColumnCount** | **String** | The number of columns profiled in the table. | [optional] 
**sensitivityScore** | [**GooglePrivacyDlpV2SensitivityScore**](GooglePrivacyDlpV2SensitivityScore.md) |  | [optional] 
**state** | **String** | State of a profile. | [optional] 
**tableId** | **String** | If the resource is BigQuery, the BigQuery table ID. | [optional] 
**tableSizeBytes** | **String** | The size of the table when the profile was generated. | [optional] 



## Enum: EncryptionStatusEnum


* `STATUS_UNSPECIFIED` (value: `"ENCRYPTION_STATUS_UNSPECIFIED"`)

* `GOOGLE_MANAGED` (value: `"ENCRYPTION_GOOGLE_MANAGED"`)

* `CUSTOMER_MANAGED` (value: `"ENCRYPTION_CUSTOMER_MANAGED"`)





## Enum: ResourceVisibilityEnum


* `UNSPECIFIED` (value: `"RESOURCE_VISIBILITY_UNSPECIFIED"`)

* `PUBLIC` (value: `"RESOURCE_VISIBILITY_PUBLIC"`)

* `RESTRICTED` (value: `"RESOURCE_VISIBILITY_RESTRICTED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)




