

# NfsExportOptions

NFS export options specifications.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessMode** | [**AccessModeEnum**](#AccessModeEnum) | Either READ_ONLY, for allowing only read requests on the exported directory, or READ_WRITE, for allowing both read and write requests. The default is READ_WRITE. |  [optional] |
|**anonGid** | **String** | An integer representing the anonymous group id with a default value of 65534. Anon_gid may only be set with squash_mode of ROOT_SQUASH. An error will be returned if this field is specified for other squash_mode settings. |  [optional] |
|**anonUid** | **String** | An integer representing the anonymous user id with a default value of 65534. Anon_uid may only be set with squash_mode of ROOT_SQUASH. An error will be returned if this field is specified for other squash_mode settings. |  [optional] |
|**ipRanges** | **List&lt;String&gt;** | List of either an IPv4 addresses in the format &#x60;{octet1}.{octet2}.{octet3}.{octet4}&#x60; or CIDR ranges in the format &#x60;{octet1}.{octet2}.{octet3}.{octet4}/{mask size}&#x60; which may mount the file share. Overlapping IP ranges are not allowed, both within and across NfsExportOptions. An error will be returned. The limit is 64 IP ranges/addresses for each FileShareConfig among all NfsExportOptions. |  [optional] |
|**securityFlavors** | [**List&lt;SecurityFlavorsEnum&gt;**](#List&lt;SecurityFlavorsEnum&gt;) | The security flavors allowed for mount operations. The default is AUTH_SYS. |  [optional] |
|**squashMode** | [**SquashModeEnum**](#SquashModeEnum) | Either NO_ROOT_SQUASH, for allowing root access on the exported directory, or ROOT_SQUASH, for not allowing root access. The default is NO_ROOT_SQUASH. |  [optional] |



## Enum: AccessModeEnum

| Name | Value |
|---- | -----|
| ACCESS_MODE_UNSPECIFIED | &quot;ACCESS_MODE_UNSPECIFIED&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| READ_WRITE | &quot;READ_WRITE&quot; |



## Enum: List&lt;SecurityFlavorsEnum&gt;

| Name | Value |
|---- | -----|
| SECURITY_FLAVOR_UNSPECIFIED | &quot;SECURITY_FLAVOR_UNSPECIFIED&quot; |
| AUTH_SYS | &quot;AUTH_SYS&quot; |
| KRB5 | &quot;KRB5&quot; |
| KRB5_I | &quot;KRB5I&quot; |
| KRB5_P | &quot;KRB5P&quot; |



## Enum: SquashModeEnum

| Name | Value |
|---- | -----|
| SQUASH_MODE_UNSPECIFIED | &quot;SQUASH_MODE_UNSPECIFIED&quot; |
| NO_ROOT_SQUASH | &quot;NO_ROOT_SQUASH&quot; |
| ROOT_SQUASH | &quot;ROOT_SQUASH&quot; |



