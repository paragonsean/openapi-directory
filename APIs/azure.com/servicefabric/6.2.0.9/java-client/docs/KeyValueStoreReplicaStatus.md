

# KeyValueStoreReplicaStatus

Key value store related information for the replica.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyNotificationCurrentKeyFilter** | **String** | Value indicating the latest key-prefix filter applied to enumeration during the callback. Null if there is no pending callback. |  [optional] |
|**copyNotificationCurrentProgress** | **String** | Value indicating the latest number of keys enumerated during the callback. 0 if there is no pending callback. |  [optional] |
|**databaseLogicalSizeEstimate** | **String** | Value indicating the estimated size of the underlying database. |  [optional] |
|**databaseRowCountEstimate** | **String** | Value indicating the estimated number of rows in the underlying database. |  [optional] |
|**statusDetails** | **String** | Value indicating the current status details of the replica. |  [optional] |



