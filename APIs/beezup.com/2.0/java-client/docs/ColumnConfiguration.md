

# ColumnConfiguration

Indicates the configuration applied on the column (catalog or custom) during the importation process.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beezUPColumnName** | **String** | The BeezUP column name |  [optional] |
|**canBeTruncated** | **Boolean** | If the size of the value is greater than the limit we can truncate the value instead of failing... |  [optional] |
|**columnCultureName** | **String** | If non null, culture used to parse the value to the storage type of this column\\r\\n will be used for parsing and for consolidation proces |  [optional] |
|**columnDataType** | **BeezUPCommonColumnDataType** |  |  |
|**columnFormat** | **String** | If non null, format used to parse the value to the storage type of this column\\r\\n will be used for parsing and for consolidation proces |  [optional] |
|**columnImportance** | **BeezUPCommonColumnImportance** |  |  |
|**displayGroupName** | **String** | Indicate the display group name where the column must be putted |  [optional] |



