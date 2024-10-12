# DatabaseMigrationApi.ValueListFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignoreCase** | **Boolean** | Required. Whether to ignore case when filtering by values. Defaults to false | [optional] 
**valuePresentList** | **String** | Required. Indicates whether the filter matches rows with values that are present in the list or those with values not present in it. | [optional] 
**values** | **[String]** | Required. The list to be used to filter by | [optional] 



## Enum: ValuePresentListEnum


* `UNSPECIFIED` (value: `"VALUE_PRESENT_IN_LIST_UNSPECIFIED"`)

* `IF_VALUE_LIST` (value: `"VALUE_PRESENT_IN_LIST_IF_VALUE_LIST"`)

* `IF_VALUE_NOT_LIST` (value: `"VALUE_PRESENT_IN_LIST_IF_VALUE_NOT_LIST"`)




