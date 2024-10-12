# DataLakeAnalyticsCatalogManagementClient.USqlIndex

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **[String]** | the list of columns in the index | [optional] 
**distributionInfo** | [**USqlDistributionInfo**](USqlDistributionInfo.md) |  | [optional] 
**indexId** | **Number** | the ID of this index within the table. | [optional] 
**indexKeys** | [**[USqlDirectedColumn]**](USqlDirectedColumn.md) | the list of directed columns in the index | [optional] 
**isColumnstore** | **Boolean** | the switch indicating if this index is a columnstore index. | [optional] 
**isUnique** | **Boolean** | the switch indicating if this index is a unique index. | [optional] 
**name** | **String** | the name of the index in the table. | [optional] 
**partitionFunction** | **String** | partition function ID for the index. | [optional] 
**partitionKeyList** | **[String]** | the list of partition keys in the index | [optional] 
**streamNames** | **[String]** | the list of full paths to the streams that contain this index in the DataLake account. | [optional] 


