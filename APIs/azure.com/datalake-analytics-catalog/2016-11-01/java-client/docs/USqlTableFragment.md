

# USqlTableFragment

A Data Lake Analytics catalog U-SQL table fragment item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createDate** | **OffsetDateTime** | the creation time of the table fragment. |  [optional] |
|**fragmentId** | **UUID** | the version of the catalog item. |  [optional] |
|**indexId** | **Integer** | the ordinal of the index which contains the table fragment. |  [optional] |
|**parentId** | **UUID** | the parent object Id of the table fragment. The parent could be a table or table partition. |  [optional] |
|**rowCount** | **Long** | the number of rows in the table fragment. |  [optional] |
|**size** | **Long** | the data size of the table fragment in bytes. |  [optional] |
|**streamPath** | **String** | the relative path for the table fragment location. |  [optional] |



