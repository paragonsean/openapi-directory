

# GoogleFirestoreAdminV1DatabaseSnapshot

A consistent snapshot of a database at a specific point in time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**database** | **String** | Required. A name of the form &#x60;projects/{project_id}/databases/{database_id}&#x60; |  [optional] |
|**snapshotTime** | **String** | Required. The timestamp at which the database snapshot is taken. The requested timestamp must be a whole minute within the PITR window. |  [optional] |



