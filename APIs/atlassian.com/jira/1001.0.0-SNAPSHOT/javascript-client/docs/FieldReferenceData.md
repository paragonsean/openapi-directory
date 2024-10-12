# TheJiraCloudPlatformRestApi.FieldReferenceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | **String** | Whether the field provide auto-complete suggestions. | [optional] 
**cfid** | **String** | If the item is a custom field, the ID of the custom field. | [optional] 
**deprecated** | **String** | Whether this field has been deprecated. | [optional] 
**deprecatedSearcherKey** | **String** | The searcher key of the field, only passed when the field is deprecated. | [optional] 
**displayName** | **String** | The display name contains the following:   *  for system fields, the field name. For example, &#x60;Summary&#x60;.  *  for collapsed custom fields, the field name followed by a hyphen and then the field name and field type. For example, &#x60;Component - Component[Dropdown]&#x60;.  *  for other custom fields, the field name followed by a hyphen and then the custom field ID. For example, &#x60;Component - cf[10061]&#x60;. | [optional] 
**operators** | **[String]** | The valid search operators for the field. | [optional] 
**orderable** | **String** | Whether the field can be used in a query&#39;s &#x60;ORDER BY&#x60; clause. | [optional] 
**searchable** | **String** | Whether the content of this field can be searched. | [optional] 
**types** | **[String]** | The data types of items in the field. | [optional] 
**value** | **String** | The field identifier. | [optional] 



## Enum: AutoEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)





## Enum: DeprecatedEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)





## Enum: OrderableEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)





## Enum: SearchableEnum


* `true` (value: `"true"`)

* `false` (value: `"false"`)




