

# FetchDatabasePropertiesResponse

Response for FetchDatabasePropertiesRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isFailoverReplicaAvailable** | **Boolean** | The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The primary instance can only fail over to the failover replica when the status is true. |  [optional] |
|**primaryGceZone** | **String** | The Compute Engine zone that the instance is currently serving from. |  [optional] |
|**secondaryGceZone** | **String** | The Compute Engine zone that the failover instance is currently serving from for a regional Cloud SQL instance. |  [optional] |



