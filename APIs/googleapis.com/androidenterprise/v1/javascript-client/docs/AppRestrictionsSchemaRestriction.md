# GooglePlayEmmApi.AppRestrictionsSchemaRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultValue** | [**AppRestrictionsSchemaRestrictionRestrictionValue**](AppRestrictionsSchemaRestrictionRestrictionValue.md) |  | [optional] 
**description** | **String** | A longer description of the restriction, giving more detail of what it affects. | [optional] 
**entry** | **[String]** | For choice or multiselect restrictions, the list of possible entries&#39; human-readable names. | [optional] 
**entryValue** | **[String]** | For choice or multiselect restrictions, the list of possible entries&#39; machine-readable values. These values should be used in the configuration, either as a single string value for a choice restriction or in a stringArray for a multiselect restriction. | [optional] 
**key** | **String** | The unique key that the product uses to identify the restriction, e.g. \&quot;com.google.android.gm.fieldname\&quot;. | [optional] 
**nestedRestriction** | [**[AppRestrictionsSchemaRestriction]**](AppRestrictionsSchemaRestriction.md) | For bundle or bundleArray restrictions, the list of nested restrictions. A bundle restriction is always nested within a bundleArray restriction, and a bundleArray restriction is at most two levels deep. | [optional] 
**restrictionType** | **String** | The type of the restriction. | [optional] 
**title** | **String** | The name of the restriction. | [optional] 



## Enum: RestrictionTypeEnum


* `bool` (value: `"bool"`)

* `string` (value: `"string"`)

* `integer` (value: `"integer"`)

* `choice` (value: `"choice"`)

* `multiselect` (value: `"multiselect"`)

* `hidden` (value: `"hidden"`)

* `bundle` (value: `"bundle"`)

* `bundleArray` (value: `"bundleArray"`)




