

# ModifyNetworkSmDevicesTagsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ids** | **List&lt;String&gt;** | The ids of the devices to be modified. |  [optional] |
|**scope** | **List&lt;String&gt;** | The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified. |  [optional] |
|**serials** | **List&lt;String&gt;** | The serials of the devices to be modified. |  [optional] |
|**tags** | **List&lt;String&gt;** | The tags to be added, deleted, or updated. |  |
|**updateAction** | **String** | One of add, delete, or update. Only devices that have been modified will be returned. |  |
|**wifiMacs** | **List&lt;String&gt;** | The wifiMacs of the devices to be modified. |  [optional] |



