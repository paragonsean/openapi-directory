

# ManagedInstanceProperties

The properties of a managed instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administratorLogin** | **String** | Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation). |  [optional] |
|**administratorLoginPassword** | **String** | The administrator login password (required for managed instance creation). |  [optional] |
|**collation** | **String** | Collation of the managed instance. |  [optional] |
|**dnsZone** | **String** | The Dns Zone that the managed instance is in. |  [optional] [readonly] |
|**dnsZonePartner** | **String** | The resource id of another managed instance whose DNS zone this managed instance will share after creation. |  [optional] |
|**fullyQualifiedDomainName** | **String** | The fully qualified domain name of the managed instance. |  [optional] [readonly] |
|**instancePoolId** | **String** | The Id of the instance pool this managed server belongs to. |  [optional] |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type. Possible values are &#39;LicenseIncluded&#39; (regular price inclusive of a new SQL license) and &#39;BasePrice&#39; (discounted AHB price for bringing your own SQL licenses). |  [optional] |
|**managedInstanceCreateMode** | [**ManagedInstanceCreateModeEnum**](#ManagedInstanceCreateModeEnum) | Specifies the mode of database creation.    Default: Regular instance creation.    Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified. |  [optional] |
|**proxyOverride** | [**ProxyOverrideEnum**](#ProxyOverrideEnum) | Connection type used for connecting to the instance. |  [optional] |
|**publicDataEndpointEnabled** | **Boolean** | Whether or not the public data endpoint is enabled. |  [optional] |
|**restorePointInTime** | **OffsetDateTime** | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. |  [optional] |
|**sourceManagedInstanceId** | **String** | The resource identifier of the source managed instance associated with create operation of this instance. |  [optional] |
|**state** | **String** | The state of the managed instance. |  [optional] [readonly] |
|**storageSizeInGB** | **Integer** | Storage size in GB. Minimum value: 32. Maximum value: 8192. Increments of 32 GB allowed only. |  [optional] |
|**subnetId** | **String** | Subnet resource ID for the managed instance. |  [optional] |
|**timezoneId** | **String** | Id of the timezone. Allowed values are timezones supported by Windows.  Windows keeps details on supported timezones, including the id, in registry under  KEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Time Zones.  You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info.  List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell.  An example of valid timezone id is \&quot;Pacific Standard Time\&quot; or \&quot;W. Europe Standard Time\&quot;. |  [optional] |
|**vCores** | **Integer** | The number of vCores. Allowed values: 8, 16, 24, 32, 40, 64, 80. |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| LICENSE_INCLUDED | &quot;LicenseIncluded&quot; |
| BASE_PRICE | &quot;BasePrice&quot; |



## Enum: ManagedInstanceCreateModeEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| POINT_IN_TIME_RESTORE | &quot;PointInTimeRestore&quot; |



## Enum: ProxyOverrideEnum

| Name | Value |
|---- | -----|
| PROXY | &quot;Proxy&quot; |
| REDIRECT | &quot;Redirect&quot; |
| DEFAULT | &quot;Default&quot; |



