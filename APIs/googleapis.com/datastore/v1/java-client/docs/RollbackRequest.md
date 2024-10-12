

# RollbackRequest

The request for Datastore.Rollback.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseId** | **String** | The ID of the database against which to make the request. &#39;(default)&#39; is not allowed; please use empty string &#39;&#39; to refer the default database. |  [optional] |
|**transaction** | **byte[]** | Required. The transaction identifier, returned by a call to Datastore.BeginTransaction. |  [optional] |



