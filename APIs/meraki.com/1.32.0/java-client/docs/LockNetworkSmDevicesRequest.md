

# LockNetworkSmDevicesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ids** | **List&lt;String&gt;** | The ids of the devices to be locked. |  [optional] |
|**pin** | **Integer** | The pin number for locking macOS devices (a six digit number). Required only for macOS devices. |  [optional] |
|**scope** | **List&lt;String&gt;** | The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be wiped. |  [optional] |
|**serials** | **List&lt;String&gt;** | The serials of the devices to be locked. |  [optional] |
|**wifiMacs** | **List&lt;String&gt;** | The wifiMacs of the devices to be locked. |  [optional] |



