

# ProvisioningQuota

A provisioning quota for a given project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetType** | [**AssetTypeEnum**](#AssetTypeEnum) | The asset type of this provisioning quota. |  [optional] |
|**availableCount** | **Integer** | The available count of the provisioning quota. |  [optional] |
|**gcpService** | **String** | The gcp service of the provisioning quota. |  [optional] |
|**instanceQuota** | [**InstanceQuota**](InstanceQuota.md) |  |  [optional] |
|**location** | **String** | The specific location of the provisioining quota. |  [optional] |
|**name** | **String** | Output only. The name of the provisioning quota. |  [optional] [readonly] |
|**networkBandwidth** | **String** | Network bandwidth, Gbps |  [optional] |
|**serverCount** | **String** | Server count. |  [optional] |
|**storageGib** | **String** | Storage size (GB). |  [optional] |



## Enum: AssetTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ASSET_TYPE_UNSPECIFIED&quot; |
| SERVER | &quot;ASSET_TYPE_SERVER&quot; |
| STORAGE | &quot;ASSET_TYPE_STORAGE&quot; |
| NETWORK | &quot;ASSET_TYPE_NETWORK&quot; |



