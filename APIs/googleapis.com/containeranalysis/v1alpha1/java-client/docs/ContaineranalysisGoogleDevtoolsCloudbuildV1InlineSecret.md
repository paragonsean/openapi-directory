

# ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecret

Pairs a set of secret environment variables mapped to encrypted values with the Cloud KMS key to use to decrypt the value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**envMap** | **Map&lt;String, byte[]&gt;** | Map of environment variable name to its encrypted value. Secret environment variables must be unique across all of a build&#39;s secrets, and must be used by at least one build step. Values can be at most 64 KB in size. There can be at most 100 secret values across all of a build&#39;s secrets. |  [optional] |
|**kmsKeyName** | **String** | Resource name of Cloud KMS crypto key to decrypt the encrypted value. In format: projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_* |  [optional] |



