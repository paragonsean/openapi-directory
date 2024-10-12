

# UpdateStorageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentVersion** | **String** |              &lt;p&gt;The version of cluster to update from. A successful operation will then generate a new version.&lt;/p&gt;           |  |
|**provisionedThroughput** | [**UpdateStorageRequestProvisionedThroughput**](UpdateStorageRequestProvisionedThroughput.md) |  |  [optional] |
|**storageMode** | [**StorageModeEnum**](#StorageModeEnum) | Controls storage mode for various supported storage tiers. |  [optional] |
|**volumeSizeGB** | **Integer** |              &lt;p&gt;size of the EBS volume to update.&lt;/p&gt;           |  [optional] |



## Enum: StorageModeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;LOCAL&quot; |
| TIERED | &quot;TIERED&quot; |



