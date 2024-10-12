# CloudFunctionsApi.GenerateUploadUrlRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **String** | The function environment the generated upload url will be used for. The upload url for 2nd Gen functions can also be used for 1st gen functions, but not vice versa. If not specified, 2nd generation-style upload URLs are generated. | [optional] 
**kmsKeyName** | **String** | [Preview] Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function source code objects in intermediate Cloud Storage buckets. When you generate an upload url and upload your source code, it gets copied to an intermediate Cloud Storage bucket. The source code is then copied to a versioned directory in the sources bucket in the consumer project during the function deployment. It must match the pattern &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}&#x60;. The Google Cloud Functions service account (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role &#39;Cloud KMS CryptoKey Encrypter/Decrypter (roles/cloudkms.cryptoKeyEncrypterDecrypter)&#39; on the Key/KeyRing/Project/Organization (least access preferred). | [optional] 



## Enum: EnvironmentEnum


* `ENVIRONMENT_UNSPECIFIED` (value: `"ENVIRONMENT_UNSPECIFIED"`)

* `GEN_1` (value: `"GEN_1"`)

* `GEN_2` (value: `"GEN_2"`)




