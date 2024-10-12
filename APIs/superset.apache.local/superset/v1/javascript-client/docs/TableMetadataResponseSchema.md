# Superset.TableMetadataResponseSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**[TableMetadataColumnsResponse]**](TableMetadataColumnsResponse.md) | A list of columns and their metadata | [optional] 
**foreignKeys** | [**[TableMetadataForeignKeysIndexesResponse]**](TableMetadataForeignKeysIndexesResponse.md) | A list of foreign keys and their metadata | [optional] 
**indexes** | [**[TableMetadataForeignKeysIndexesResponse]**](TableMetadataForeignKeysIndexesResponse.md) | A list of indexes and their metadata | [optional] 
**name** | **String** | The name of the table | [optional] 
**primaryKey** | [**TableMetadataPrimaryKeyResponse**](TableMetadataPrimaryKeyResponse.md) | Primary keys metadata | [optional] 
**selectStar** | **String** | SQL select star | [optional] 


