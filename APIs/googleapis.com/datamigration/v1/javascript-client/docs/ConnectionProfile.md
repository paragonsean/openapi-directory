# DatabaseMigrationApi.ConnectionProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloydb** | [**AlloyDbConnectionProfile**](AlloyDbConnectionProfile.md) |  | [optional] 
**cloudsql** | [**CloudSqlConnectionProfile**](CloudSqlConnectionProfile.md) |  | [optional] 
**createTime** | **String** | Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. | [optional] [readonly] 
**displayName** | **String** | The connection profile display name. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**labels** | **{String: String}** | The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. | [optional] 
**mysql** | [**MySqlConnectionProfile**](MySqlConnectionProfile.md) |  | [optional] 
**name** | **String** | The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}. | [optional] 
**oracle** | [**OracleConnectionProfile**](OracleConnectionProfile.md) |  | [optional] 
**postgresql** | [**PostgreSqlConnectionProfile**](PostgreSqlConnectionProfile.md) |  | [optional] 
**provider** | **String** | The database provider. | [optional] 
**state** | **String** | The current connection profile state (e.g. DRAFT, READY, or FAILED). | [optional] 
**updateTime** | **String** | Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. | [optional] [readonly] 



## Enum: ProviderEnum


* `DATABASE_PROVIDER_UNSPECIFIED` (value: `"DATABASE_PROVIDER_UNSPECIFIED"`)

* `CLOUDSQL` (value: `"CLOUDSQL"`)

* `RDS` (value: `"RDS"`)

* `AURORA` (value: `"AURORA"`)

* `ALLOYDB` (value: `"ALLOYDB"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `DRAFT` (value: `"DRAFT"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `DELETED` (value: `"DELETED"`)

* `FAILED` (value: `"FAILED"`)




