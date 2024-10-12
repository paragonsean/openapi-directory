

# ReserveIdsRequest

The request for Datastore.ReserveIds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseId** | **String** | The ID of the database against which to make the request. &#39;(default)&#39; is not allowed; please use empty string &#39;&#39; to refer the default database. |  [optional] |
|**keys** | [**List&lt;Key&gt;**](Key.md) | Required. A list of keys with complete key paths whose numeric IDs should not be auto-allocated. |  [optional] |



