

# USqlIndex

A Data Lake Analytics catalog U-SQL table index item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **List&lt;String&gt;** | the list of columns in the index |  [optional] |
|**distributionInfo** | [**USqlDistributionInfo**](USqlDistributionInfo.md) |  |  [optional] |
|**indexId** | **Integer** | the ID of this index within the table. |  [optional] |
|**indexKeys** | [**List&lt;USqlDirectedColumn&gt;**](USqlDirectedColumn.md) | the list of directed columns in the index |  [optional] |
|**isColumnstore** | **Boolean** | the switch indicating if this index is a columnstore index. |  [optional] |
|**isUnique** | **Boolean** | the switch indicating if this index is a unique index. |  [optional] |
|**name** | **String** | the name of the index in the table. |  [optional] |
|**partitionFunction** | **UUID** | partition function ID for the index. |  [optional] |
|**partitionKeyList** | **List&lt;String&gt;** | the list of partition keys in the index |  [optional] |
|**streamNames** | **List&lt;String&gt;** | the list of full paths to the streams that contain this index in the DataLake account. |  [optional] |



