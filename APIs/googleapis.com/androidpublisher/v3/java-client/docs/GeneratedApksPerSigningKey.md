

# GeneratedApksPerSigningKey

Download metadata for split, standalone and universal APKs, as well as asset pack slices, signed with a given key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateSha256Hash** | **String** | SHA256 hash of the APK signing public key certificate. |  [optional] |
|**generatedAssetPackSlices** | [**List&lt;GeneratedAssetPackSlice&gt;**](GeneratedAssetPackSlice.md) | List of asset pack slices which will be served for this app bundle, signed with a key corresponding to certificate_sha256_hash. |  [optional] |
|**generatedRecoveryModules** | [**List&lt;GeneratedRecoveryApk&gt;**](GeneratedRecoveryApk.md) | Generated recovery apks for recovery actions signed with a key corresponding to certificate_sha256_hash. This includes all generated recovery APKs, also those in draft or cancelled state. This field is not set if no recovery actions were created for this signing key. |  [optional] |
|**generatedSplitApks** | [**List&lt;GeneratedSplitApk&gt;**](GeneratedSplitApk.md) | List of generated split APKs, signed with a key corresponding to certificate_sha256_hash. |  [optional] |
|**generatedStandaloneApks** | [**List&lt;GeneratedStandaloneApk&gt;**](GeneratedStandaloneApk.md) | List of generated standalone APKs, signed with a key corresponding to certificate_sha256_hash. |  [optional] |
|**generatedUniversalApk** | [**GeneratedUniversalApk**](GeneratedUniversalApk.md) |  |  [optional] |
|**targetingInfo** | [**TargetingInfo**](TargetingInfo.md) |  |  [optional] |



