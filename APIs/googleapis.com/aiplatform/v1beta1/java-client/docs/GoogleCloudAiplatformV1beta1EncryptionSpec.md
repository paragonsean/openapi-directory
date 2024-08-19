

# GoogleCloudAiplatformV1beta1EncryptionSpec

Represents a customer-managed encryption key spec that can be applied to a top-level resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyName** | **String** | Required. The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: &#x60;projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key&#x60;. The key needs to be in the same region as where the compute resource is created. |  [optional] |



