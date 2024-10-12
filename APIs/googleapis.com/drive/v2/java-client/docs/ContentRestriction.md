

# ContentRestriction

A restriction for accessing the content of the file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ownerRestricted** | **Boolean** | Whether the content restriction can only be modified or removed by a user who owns the file. For files in shared drives, any user with &#x60;organizer&#x60; capabilities can modify or remove this content restriction. |  [optional] |
|**readOnly** | **Boolean** | Whether the content of the file is read-only. If a file is read-only, a new revision of the file may not be added, comments may not be added or modified, and the title of the file may not be modified. |  [optional] |
|**reason** | **String** | Reason for why the content of the file is restricted. This is only mutable on requests that also set &#x60;readOnly&#x3D;true&#x60;. |  [optional] |
|**restrictingUser** | [**User**](User.md) |  |  [optional] |
|**restrictionDate** | **OffsetDateTime** | The time at which the content restriction was set (formatted RFC 3339 timestamp). Only populated if readOnly is true. |  [optional] |
|**systemRestricted** | **Boolean** | Output only. Whether the content restriction was applied by the system, for example due to an esignature. Users cannot modify or remove system restricted content restrictions. |  [optional] |
|**type** | **String** | Output only. The type of the content restriction. Currently the only possible value is &#x60;globalContentRestriction&#x60;. |  [optional] |



