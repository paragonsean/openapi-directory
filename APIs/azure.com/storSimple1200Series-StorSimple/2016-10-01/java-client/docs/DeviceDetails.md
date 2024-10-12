

# DeviceDetails

Class containing more granular details about the device

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableLocalStorageInBytes** | **Long** | Local pending storage available on the device in bytes |  [optional] |
|**availableStorageInBytes** | **Long** | Total pending available storage on the device in bytes |  [optional] |
|**endpointCount** | **Integer** | Total number of endpoints that are currently on the device ( i.e. number of shares on FileServer or number of volumes on IscsiServer) |  [optional] |
|**provisionedLocalStorageInBytes** | **Long** | Storage in bytes that has been provisioned locally on the device |  [optional] |
|**provisionedStorageInBytes** | **Long** | Storage in bytes that has been provisioned on the device including both local and cloud |  [optional] |
|**totalBackupSizeInBytes** | **Long** | Total size taken up by backups in bytes |  [optional] |
|**totalLocalStorageInBytes** | **Long** | Total local storage capacity in device in bytes. |  [optional] |
|**totalStorageInBytes** | **Long** | Total storage available on the device in bytes. |  [optional] |
|**usingLocalStorageInBytes** | **Long** | Local Storage that is being currently used in bytes |  [optional] |
|**usingStorageInBytes** | **Long** | Storage that is being currently used in bytes including both local and cloud |  [optional] |



