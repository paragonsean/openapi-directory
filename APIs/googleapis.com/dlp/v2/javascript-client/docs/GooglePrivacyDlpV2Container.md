# SensitiveDataProtectionDlp.GooglePrivacyDlpV2Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fullPath** | **String** | A string representation of the full container name. Examples: - BigQuery: &#39;Project:DataSetId.TableId&#39; - Cloud Storage: &#39;gs://Bucket/folders/filename.txt&#39; | [optional] 
**projectId** | **String** | Project where the finding was found. Can be different from the project that owns the finding. | [optional] 
**relativePath** | **String** | The rest of the path after the root. Examples: - For BigQuery table &#x60;project_id:dataset_id.table_id&#x60;, the relative path is &#x60;table_id&#x60; - For Cloud Storage file &#x60;gs://bucket/folder/filename.txt&#x60;, the relative path is &#x60;folder/filename.txt&#x60; | [optional] 
**rootPath** | **String** | The root of the container. Examples: - For BigQuery table &#x60;project_id:dataset_id.table_id&#x60;, the root is &#x60;dataset_id&#x60; - For Cloud Storage file &#x60;gs://bucket/folder/filename.txt&#x60;, the root is &#x60;gs://bucket&#x60; | [optional] 
**type** | **String** | Container type, for example BigQuery or Cloud Storage. | [optional] 
**updateTime** | **String** | Findings container modification timestamp, if applicable. For Cloud Storage, this field contains the last file modification timestamp. For a BigQuery table, this field contains the last_modified_time property. For Datastore, this field isn&#39;t populated. | [optional] 
**version** | **String** | Findings container version, if available (\&quot;generation\&quot; for Cloud Storage). | [optional] 


