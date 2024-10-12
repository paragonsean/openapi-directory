# SensitiveDataProtectionDlp.GooglePrivacyDlpV2ContentLocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerName** | **String** | Name of the container where the finding is located. The top level name is the source file name or table name. Names of some common storage containers are formatted as follows: * BigQuery tables: &#x60;{project_id}:{dataset_id}.{table_id}&#x60; * Cloud Storage files: &#x60;gs://{bucket}/{path}&#x60; * Datastore namespace: {namespace} Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document). | [optional] 
**containerTimestamp** | **String** | Finding container modification timestamp, if applicable. For Cloud Storage, this field contains the last file modification timestamp. For a BigQuery table, this field contains the last_modified_time property. For Datastore, this field isn&#39;t populated. | [optional] 
**containerVersion** | **String** | Finding container version, if available (\&quot;generation\&quot; for Cloud Storage). | [optional] 
**documentLocation** | [**GooglePrivacyDlpV2DocumentLocation**](GooglePrivacyDlpV2DocumentLocation.md) |  | [optional] 
**imageLocation** | [**GooglePrivacyDlpV2ImageLocation**](GooglePrivacyDlpV2ImageLocation.md) |  | [optional] 
**metadataLocation** | [**GooglePrivacyDlpV2MetadataLocation**](GooglePrivacyDlpV2MetadataLocation.md) |  | [optional] 
**recordLocation** | [**GooglePrivacyDlpV2RecordLocation**](GooglePrivacyDlpV2RecordLocation.md) |  | [optional] 


