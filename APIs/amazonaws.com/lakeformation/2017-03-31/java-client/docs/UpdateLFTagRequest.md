

# UpdateLFTagRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogId** | **String** | The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.  |  [optional] |
|**tagKey** | **String** | The key-name for the LF-tag for which to add or delete values. |  |
|**tagValuesToDelete** | **List&lt;String&gt;** | A list of LF-tag values to delete from the LF-tag. |  [optional] |
|**tagValuesToAdd** | **List&lt;String&gt;** | A list of LF-tag values to add from the LF-tag. |  [optional] |



