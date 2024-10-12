

# GenerateUploadUrlRequest

Request of `GenerateSourceUploadUrl` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyName** | **String** | Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function source code objects in intermediate Cloud Storage buckets. When you generate an upload url and upload your source code, it gets copied to an intermediate Cloud Storage bucket. The source code is then copied to a versioned directory in the sources bucket in the consumer project during the function deployment. It must match the pattern &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}&#x60;. The Google Cloud Functions service account (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role &#39;Cloud KMS CryptoKey Encrypter/Decrypter (roles/cloudkms.cryptoKeyEncrypterDecrypter)&#39; on the Key/KeyRing/Project/Organization (least access preferred). GCF will delegate access to the Google Storage service account in the internal project. |  [optional] |



