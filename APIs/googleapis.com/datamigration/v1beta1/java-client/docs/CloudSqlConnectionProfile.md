

# CloudSqlConnectionProfile

Specifies required connection parameters, and, optionally, the parameters required to create a Cloud SQL destination database instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudSqlId** | **String** | Output only. The Cloud SQL instance ID that this connection profile is associated with. |  [optional] [readonly] |
|**privateIp** | **String** | Output only. The Cloud SQL database instance&#39;s private IP. |  [optional] [readonly] |
|**publicIp** | **String** | Output only. The Cloud SQL database instance&#39;s public IP. |  [optional] [readonly] |
|**settings** | [**CloudSqlSettings**](CloudSqlSettings.md) |  |  [optional] |



