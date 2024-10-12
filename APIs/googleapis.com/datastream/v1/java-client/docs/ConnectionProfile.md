

# ConnectionProfile

A set of reusable connection configurations to be used as a source or destination for a stream.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryProfile** | **Object** | BigQuery warehouse profile. |  [optional] |
|**createTime** | **String** | Output only. The create time of the resource. |  [optional] [readonly] |
|**displayName** | **String** | Required. Display name. |  [optional] |
|**forwardSshConnectivity** | [**ForwardSshTunnelConnectivity**](ForwardSshTunnelConnectivity.md) |  |  [optional] |
|**gcsProfile** | [**GcsProfile**](GcsProfile.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels. |  [optional] |
|**mysqlProfile** | [**MysqlProfile**](MysqlProfile.md) |  |  [optional] |
|**name** | **String** | Output only. The resource&#39;s name. |  [optional] [readonly] |
|**oracleProfile** | [**OracleProfile**](OracleProfile.md) |  |  [optional] |
|**postgresqlProfile** | [**PostgresqlProfile**](PostgresqlProfile.md) |  |  [optional] |
|**privateConnectivity** | [**PrivateConnectivity**](PrivateConnectivity.md) |  |  [optional] |
|**sqlServerProfile** | [**SqlServerProfile**](SqlServerProfile.md) |  |  [optional] |
|**staticServiceIpConnectivity** | **Object** | Static IP address connectivity. Used when the source database is configured to allow incoming connections from the Datastream public IP addresses for the region specified in the connection profile. |  [optional] |
|**updateTime** | **String** | Output only. The update time of the resource. |  [optional] [readonly] |



