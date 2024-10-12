# BareMetalSolutionApi.ProvisioningQuota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetType** | **String** | The asset type of this provisioning quota. | [optional] 
**availableCount** | **Number** | The available count of the provisioning quota. | [optional] 
**gcpService** | **String** | The gcp service of the provisioning quota. | [optional] 
**instanceQuota** | [**InstanceQuota**](InstanceQuota.md) |  | [optional] 
**location** | **String** | The specific location of the provisioining quota. | [optional] 
**name** | **String** | Output only. The name of the provisioning quota. | [optional] [readonly] 
**networkBandwidth** | **String** | Network bandwidth, Gbps | [optional] 
**serverCount** | **String** | Server count. | [optional] 
**storageGib** | **String** | Storage size (GB). | [optional] 



## Enum: AssetTypeEnum


* `UNSPECIFIED` (value: `"ASSET_TYPE_UNSPECIFIED"`)

* `SERVER` (value: `"ASSET_TYPE_SERVER"`)

* `STORAGE` (value: `"ASSET_TYPE_STORAGE"`)

* `NETWORK` (value: `"ASSET_TYPE_NETWORK"`)




