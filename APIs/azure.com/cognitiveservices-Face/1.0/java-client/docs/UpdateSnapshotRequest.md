

# UpdateSnapshotRequest

Request body for updating a snapshot, with a combination of user defined apply scope and user specified data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applyScope** | **List&lt;UUID&gt;** | Array of the target Face subscription ids for the snapshot, specified by the user who created the snapshot when calling Snapshot - Take. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it. |  [optional] |
|**userData** | **String** | User specified data about the snapshot for any purpose. Length should not exceed 16KB. |  [optional] |



