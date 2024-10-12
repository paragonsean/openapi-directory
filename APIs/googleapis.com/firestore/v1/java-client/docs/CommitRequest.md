

# CommitRequest

The request for Firestore.Commit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transaction** | **byte[]** | If set, applies all writes in this transaction, and commits it. |  [optional] |
|**writes** | [**List&lt;Write&gt;**](Write.md) | The writes to apply. Always executed atomically and in order. |  [optional] |



