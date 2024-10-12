# CloudSqlAdminApi.ImportContextBakImportOptionsEncryptionOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certPath** | **String** | Path to the Certificate (.cer) in Cloud Storage, in the form &#x60;gs://bucketName/fileName&#x60;. The instance must have write permissions to the bucket and read access to the file. | [optional] 
**pvkPassword** | **String** | Password that encrypts the private key | [optional] 
**pvkPath** | **String** | Path to the Certificate Private Key (.pvk) in Cloud Storage, in the form &#x60;gs://bucketName/fileName&#x60;. The instance must have write permissions to the bucket and read access to the file. | [optional] 


