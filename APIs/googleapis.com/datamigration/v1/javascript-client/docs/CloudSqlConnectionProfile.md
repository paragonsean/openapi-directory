# DatabaseMigrationApi.CloudSqlConnectionProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalPublicIp** | **String** | Output only. The Cloud SQL database instance&#39;s additional (outgoing) public IP. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). | [optional] [readonly] 
**cloudSqlId** | **String** | Output only. The Cloud SQL instance ID that this connection profile is associated with. | [optional] [readonly] 
**privateIp** | **String** | Output only. The Cloud SQL database instance&#39;s private IP. | [optional] [readonly] 
**publicIp** | **String** | Output only. The Cloud SQL database instance&#39;s public IP. | [optional] [readonly] 
**settings** | [**CloudSqlSettings**](CloudSqlSettings.md) |  | [optional] 


