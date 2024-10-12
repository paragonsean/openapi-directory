# FaceClient.UpdateSnapshotRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyScope** | **[String]** | Array of the target Face subscription ids for the snapshot, specified by the user who created the snapshot when calling Snapshot - Take. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it. | [optional] 
**userData** | **String** | User specified data about the snapshot for any purpose. Length should not exceed 16KB. | [optional] 


