

# VolumesGet200ResponseVolumesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**format** | **String** | Filesystem of the Volume if formatted on creation, null if not formatted on creation |  |
|**id** | **Integer** | ID of the Resource |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**linuxDevice** | **String** | Device path on the file system for the Volume |  |
|**location** | [**VolumesGet200ResponseVolumesInnerLocation**](VolumesGet200ResponseVolumesInnerLocation.md) |  |  |
|**name** | **String** | Name of the Resource. Must be unique per Project. |  |
|**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  |  |
|**server** | **Integer** | ID of the Server the Volume is attached to, null if it is not attached at all |  |
|**size** | **BigDecimal** | Size in GB of the Volume |  |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the Volume |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;creating&quot; |
| AVAILABLE | &quot;available&quot; |



