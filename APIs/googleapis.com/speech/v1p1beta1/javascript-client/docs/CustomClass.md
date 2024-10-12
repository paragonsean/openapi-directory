# CloudSpeechToTextApi.CustomClass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Output only. Allows users to store small amounts of arbitrary data. Both the key and the value must be 63 characters or less each. At most 100 annotations. This field is not used. | [optional] [readonly] 
**customClassId** | **String** | If this custom class is a resource, the custom_class_id is the resource id of the CustomClass. Case sensitive. | [optional] 
**deleteTime** | **String** | Output only. The time at which this resource was requested for deletion. This field is not used. | [optional] [readonly] 
**displayName** | **String** | Output only. User-settable, human-readable name for the CustomClass. Must be 63 characters or less. This field is not used. | [optional] [readonly] 
**etag** | **String** | Output only. This checksum is computed by the server based on the value of other fields. This may be sent on update, undelete, and delete requests to ensure the client has an up-to-date value before proceeding. This field is not used. | [optional] [readonly] 
**expireTime** | **String** | Output only. The time at which this resource will be purged. This field is not used. | [optional] [readonly] 
**items** | [**[ClassItem]**](ClassItem.md) | A collection of class items. | [optional] 
**kmsKeyName** | **String** | Output only. The [KMS key name](https://cloud.google.com/kms/docs/resource-hierarchy#keys) with which the content of the ClassItem is encrypted. The expected format is &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}&#x60;. | [optional] [readonly] 
**kmsKeyVersionName** | **String** | Output only. The [KMS key version name](https://cloud.google.com/kms/docs/resource-hierarchy#key_versions) with which content of the ClassItem is encrypted. The expected format is &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}&#x60;. | [optional] [readonly] 
**name** | **String** | The resource name of the custom class. | [optional] 
**reconciling** | **Boolean** | Output only. Whether or not this CustomClass is in the process of being updated. This field is not used. | [optional] [readonly] 
**state** | **String** | Output only. The CustomClass lifecycle state. This field is not used. | [optional] [readonly] 
**uid** | **String** | Output only. System-assigned unique identifier for the CustomClass. This field is not used. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETED` (value: `"DELETED"`)




