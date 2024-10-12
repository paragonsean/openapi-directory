

# ReadOptions

The options shared by read requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**readConsistency** | [**ReadConsistencyEnum**](#ReadConsistencyEnum) | The non-transactional read consistency to use. |  [optional] |
|**readTime** | **String** | Reads entities as they were at the given time. This value is only supported for Cloud Firestore in Datastore mode. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. |  [optional] |
|**transaction** | **byte[]** | The identifier of the transaction in which to read. A transaction identifier is returned by a call to Datastore.BeginTransaction. |  [optional] |



## Enum: ReadConsistencyEnum

| Name | Value |
|---- | -----|
| READ_CONSISTENCY_UNSPECIFIED | &quot;READ_CONSISTENCY_UNSPECIFIED&quot; |
| STRONG | &quot;STRONG&quot; |
| EVENTUAL | &quot;EVENTUAL&quot; |



