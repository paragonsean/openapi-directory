# DialogflowApi.GoogleCloudDialogflowV2ReloadDocumentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentUri** | **String** | Optional. The path of gcs source file for reloading document content. For now, only gcs uri is supported. For documents stored in Google Cloud Storage, these URIs must have the form &#x60;gs:///&#x60;. | [optional] 
**importGcsCustomMetadata** | **Boolean** | Optional. Whether to import custom metadata from Google Cloud Storage. Only valid when the document source is Google Cloud Storage URI. | [optional] 
**smartMessagingPartialUpdate** | **Boolean** | Optional. When enabled, the reload request is to apply partial update to the smart messaging allowlist. | [optional] 


