# CloudKeyManagementServiceKmsApi.EkmConnection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time at which the EkmConnection was created. | [optional] [readonly] 
**cryptoSpacePath** | **String** | Optional. Identifies the EKM Crypto Space that this EkmConnection maps to. Note: This field is required if KeyManagementMode is CLOUD_KMS. | [optional] 
**etag** | **String** | Optional. Etag of the currently stored EkmConnection. | [optional] 
**keyManagementMode** | **String** | Optional. Describes who can perform control plane operations on the EKM. If unset, this defaults to MANUAL. | [optional] 
**name** | **String** | Output only. The resource name for the EkmConnection in the format &#x60;projects/_*_/locations/_*_/ekmConnections/_*&#x60;. | [optional] [readonly] 
**serviceResolvers** | [**[ServiceResolver]**](ServiceResolver.md) | A list of ServiceResolvers where the EKM can be reached. There should be one ServiceResolver per EKM replica. Currently, only a single ServiceResolver is supported. | [optional] 



## Enum: KeyManagementModeEnum


* `KEY_MANAGEMENT_MODE_UNSPECIFIED` (value: `"KEY_MANAGEMENT_MODE_UNSPECIFIED"`)

* `MANUAL` (value: `"MANUAL"`)

* `CLOUD_KMS` (value: `"CLOUD_KMS"`)




