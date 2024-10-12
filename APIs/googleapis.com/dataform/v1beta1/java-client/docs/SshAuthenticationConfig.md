

# SshAuthenticationConfig

Configures fields for performing SSH authentication.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostPublicKey** | **String** | Required. Content of a public SSH key to verify an identity of a remote Git host. |  [optional] |
|**userPrivateKeySecretVersion** | **String** | Required. The name of the Secret Manager secret version to use as a ssh private key for Git operations. Must be in the format &#x60;projects/_*_/secrets/_*_/versions/_*&#x60;. |  [optional] |



