# CloudDatastoreApi.ReadOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newTransaction** | [**TransactionOptions**](TransactionOptions.md) |  | [optional] 
**readConsistency** | **String** | The non-transactional read consistency to use. | [optional] 
**readTime** | **String** | Reads entities as they were at the given time. This value is only supported for Cloud Firestore in Datastore mode. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. | [optional] 
**transaction** | **Blob** | The identifier of the transaction in which to read. A transaction identifier is returned by a call to Datastore.BeginTransaction. | [optional] 



## Enum: ReadConsistencyEnum


* `READ_CONSISTENCY_UNSPECIFIED` (value: `"READ_CONSISTENCY_UNSPECIFIED"`)

* `STRONG` (value: `"STRONG"`)

* `EVENTUAL` (value: `"EVENTUAL"`)




