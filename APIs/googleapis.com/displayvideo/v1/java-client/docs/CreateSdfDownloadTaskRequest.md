

# CreateSdfDownloadTaskRequest

Request message for [SdfDownloadTaskService.CreateSdfDownloadTask].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | The ID of the advertiser to download SDF for. |  [optional] |
|**idFilter** | [**IdFilter**](IdFilter.md) |  |  [optional] |
|**inventorySourceFilter** | [**InventorySourceFilter**](InventorySourceFilter.md) |  |  [optional] |
|**parentEntityFilter** | [**ParentEntityFilter**](ParentEntityFilter.md) |  |  [optional] |
|**partnerId** | **String** | The ID of the partner to download SDF for. |  [optional] |
|**version** | [**VersionEnum**](#VersionEnum) | Required. The SDF version of the downloaded file. If set to &#x60;SDF_VERSION_UNSPECIFIED&#x60;, this will default to the version specified by the advertiser or partner identified by &#x60;root_id&#x60;. An advertiser inherits its SDF version from its partner unless configured otherwise. |  [optional] |



## Enum: VersionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SDF_VERSION_UNSPECIFIED&quot; |
| _3_1 | &quot;SDF_VERSION_3_1&quot; |
| _4 | &quot;SDF_VERSION_4&quot; |
| _4_1 | &quot;SDF_VERSION_4_1&quot; |
| _4_2 | &quot;SDF_VERSION_4_2&quot; |
| _5 | &quot;SDF_VERSION_5&quot; |
| _5_1 | &quot;SDF_VERSION_5_1&quot; |
| _5_2 | &quot;SDF_VERSION_5_2&quot; |
| _5_3 | &quot;SDF_VERSION_5_3&quot; |
| _5_4 | &quot;SDF_VERSION_5_4&quot; |
| _5_5 | &quot;SDF_VERSION_5_5&quot; |
| _6 | &quot;SDF_VERSION_6&quot; |
| _7 | &quot;SDF_VERSION_7&quot; |



