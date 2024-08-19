

# EkmConfig

An EkmConfig is a singleton resource that represents configuration parameters that apply to all CryptoKeys and CryptoKeyVersions with a ProtectionLevel of EXTERNAL_VPC in a given project and location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultEkmConnection** | **String** | Optional. Resource name of the default EkmConnection. Setting this field to the empty string removes the default. |  [optional] |
|**name** | **String** | Output only. The resource name for the EkmConfig in the format &#x60;projects/_*_/locations/_*_/ekmConfig&#x60;. |  [optional] [readonly] |



