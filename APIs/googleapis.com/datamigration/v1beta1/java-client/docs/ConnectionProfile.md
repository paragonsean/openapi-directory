

# ConnectionProfile

A connection profile definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudsql** | [**CloudSqlConnectionProfile**](CloudSqlConnectionProfile.md) |  |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. |  [optional] [readonly] |
|**displayName** | **String** | The connection profile display name. |  [optional] |
|**error** | [**Status**](Status.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. |  [optional] |
|**mysql** | [**MySqlConnectionProfile**](MySqlConnectionProfile.md) |  |  [optional] |
|**name** | **String** | The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}. |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | The database provider. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current connection profile state (e.g. DRAFT, READY, or FAILED). |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. |  [optional] [readonly] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| DATABASE_PROVIDER_UNSPECIFIED | &quot;DATABASE_PROVIDER_UNSPECIFIED&quot; |
| CLOUDSQL | &quot;CLOUDSQL&quot; |
| RDS | &quot;RDS&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| DELETED | &quot;DELETED&quot; |
| FAILED | &quot;FAILED&quot; |



