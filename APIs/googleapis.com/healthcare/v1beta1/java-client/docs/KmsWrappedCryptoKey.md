

# KmsWrappedCryptoKey

Include to use an existing data crypto key wrapped by KMS. The wrapped key must be a 128-, 192-, or 256-bit key. The key must grant the Cloud IAM permission `cloudkms.cryptoKeyVersions.useToDecrypt` to the project's Cloud Healthcare Service Agent service account. For more information, see [Creating a wrapped key] (https://cloud.google.com/dlp/docs/create-wrapped-key).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cryptoKey** | **String** | Required. The resource name of the KMS CryptoKey to use for unwrapping. For example, &#x60;projects/{project_id}/locations/{location_id}/keyRings/{keyring}/cryptoKeys/{key}&#x60;. |  [optional] |
|**wrappedKey** | **byte[]** | Required. The wrapped data crypto key. |  [optional] |



