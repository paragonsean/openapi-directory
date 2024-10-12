# AmazonDynamoDb.ScanInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tableName** | **String** |  | 
**attributesToGet** | **[String]** | List of &lt;code&gt;Attribute&lt;/code&gt; names. If attribute names are not specified then all attributes will be returned. If some attributes are not found, they will not appear in the result. | [optional] 
**limit** | **Number** |  | [optional] 
**count** | **Boolean** |  | [optional] 
**scanFilter** | **Object** |  | [optional] 
**exclusiveStartKey** | [**ScanInputExclusiveStartKey**](ScanInputExclusiveStartKey.md) |  | [optional] 


