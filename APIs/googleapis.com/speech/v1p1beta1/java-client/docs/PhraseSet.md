

# PhraseSet

Provides \"hints\" to the speech recognizer to favor specific words and phrases in the results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Output only. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used. |  [optional] [readonly] |
|**boost** | **Float** | Hint Boost. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost values would correspond to anti-biasing. Anti-biasing is not enabled, so negative boost will simply be ignored. Though &#x60;boost&#x60; can accept a wide range of positive values, most use cases are best served with values between 0 (exclusive) and 20. We recommend using a binary search approach to finding the optimal value for your use case as well as adding phrases both with and without boost to your requests. |  [optional] |
|**deleteTime** | **String** | Output only. The time at which this resource was requested for deletion. This field is not used. |  [optional] [readonly] |
|**displayName** | **String** | Output only. User-settable, human-readable name for the PhraseSet. Must be 63 characters or less. This field is not used. |  [optional] [readonly] |
|**etag** | **String** | Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. The time at which this resource will be purged. This field is not used. |  [optional] [readonly] |
|**kmsKeyName** | **String** | Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the PhraseSet is encrypted. The expected format is &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}&#x60;. |  [optional] [readonly] |
|**kmsKeyVersionName** | **String** | Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the PhraseSet is encrypted. The expected format is &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}&#x60;. |  [optional] [readonly] |
|**name** | **String** | The resource name of the phrase set. |  [optional] |
|**phrases** | [**List&lt;Phrase&gt;**](Phrase.md) | A list of word and phrases. |  [optional] |
|**reconciling** | **Boolean** | Output only. Whether or not this PhraseSet is in the process of being updated. This field is not used. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The CustomClass lifecycle state. This field is not used. |  [optional] [readonly] |
|**uid** | **String** | Output only. System-assigned unique identifier for the PhraseSet. This field is not used. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETED | &quot;DELETED&quot; |



