# BeezUpMerchantApi.BeezUPColumnConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beezUPColumnName** | **String** | The BeezUP column name | 
**canBeTruncated** | **Boolean** | If the size of the value is greater than the limit we can truncate the value instead of failing... | [optional] [default to false]
**columnDataType** | [**BeezUPCommonColumnDataType**](BeezUPCommonColumnDataType.md) |  | [optional] 
**columnImportance** | [**BeezUPCommonColumnImportance**](BeezUPCommonColumnImportance.md) |  | 
**description** | **String** | Describe the BeezUP column | [optional] 
**displayGroupName** | **String** | Indicate the display group name where the column must be putted | 
**unique** | **Boolean** | /!\\ ONLY AVAILABLE ON CATALOG COLUMN NOT ON CUSTOM COLUMNS!!  If true, an error happen at the second occurence of the same value for this column  This information will be used during the importation process and later for mapping proposal | [optional] [default to false]


