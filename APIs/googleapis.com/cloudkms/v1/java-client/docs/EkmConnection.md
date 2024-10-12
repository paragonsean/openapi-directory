

# EkmConnection

An EkmConnection represents an individual EKM connection. It can be used for creating CryptoKeys and CryptoKeyVersions with a ProtectionLevel of EXTERNAL_VPC, as well as performing cryptographic operations using keys created within the EkmConnection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time at which the EkmConnection was created. |  [optional] [readonly] |
|**cryptoSpacePath** | **String** | Optional. Identifies the EKM Crypto Space that this EkmConnection maps to. Note: This field is required if KeyManagementMode is CLOUD_KMS. |  [optional] |
|**etag** | **String** | Optional. Etag of the currently stored EkmConnection. |  [optional] |
|**keyManagementMode** | [**KeyManagementModeEnum**](#KeyManagementModeEnum) | Optional. Describes who can perform control plane operations on the EKM. If unset, this defaults to MANUAL. |  [optional] |
|**name** | **String** | Output only. The resource name for the EkmConnection in the format &#x60;projects/_*_/locations/_*_/ekmConnections/_*&#x60;. |  [optional] [readonly] |
|**serviceResolvers** | [**List&lt;ServiceResolver&gt;**](ServiceResolver.md) | A list of ServiceResolvers where the EKM can be reached. There should be one ServiceResolver per EKM replica. Currently, only a single ServiceResolver is supported. |  [optional] |



## Enum: KeyManagementModeEnum

| Name | Value |
|---- | -----|
| KEY_MANAGEMENT_MODE_UNSPECIFIED | &quot;KEY_MANAGEMENT_MODE_UNSPECIFIED&quot; |
| MANUAL | &quot;MANUAL&quot; |
| CLOUD_KMS | &quot;CLOUD_KMS&quot; |



