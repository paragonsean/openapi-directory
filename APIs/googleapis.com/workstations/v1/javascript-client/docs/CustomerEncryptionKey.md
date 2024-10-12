# CloudWorkstationsApi.CustomerEncryptionKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kmsKey** | **String** | Immutable. The name of the Google Cloud KMS encryption key. For example, &#x60;\&quot;projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY_NAME\&quot;&#x60;. The key must be in the same region as the workstation configuration. | [optional] 
**kmsKeyServiceAccount** | **String** | Immutable. The service account to use with the specified KMS key. We recommend that you use a separate service account and follow KMS best practices. For more information, see [Separation of duties](https://cloud.google.com/kms/docs/separation-of-duties) and &#x60;gcloud kms keys add-iam-policy-binding&#x60; [&#x60;--member&#x60;](https://cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding#--member). | [optional] 


