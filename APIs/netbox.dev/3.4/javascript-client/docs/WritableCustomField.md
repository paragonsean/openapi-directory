# NetBoxApi.WritableCustomField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | **[String]** | Comma-separated list of available choices (for selection fields) | [optional] 
**contentTypes** | **[String]** |  | 
**created** | **Date** |  | [optional] [readonly] 
**dataType** | **String** |  | [optional] [readonly] 
**_default** | **Object** | Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. \&quot;Foo\&quot;). | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**filterLogic** | **String** | Loose matches any instance of a given string; exact matches the entire field. | [optional] 
**groupName** | **String** | Custom fields within the same group will be displayed together | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** | Name of the field as displayed to users (if not provided, the field&#39;s name will be used) | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**name** | **String** | Internal field name | 
**objectType** | **String** |  | [optional] 
**required** | **Boolean** | If true, this field is required when creating new objects or editing an existing object. | [optional] 
**searchWeight** | **Number** | Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored. | [optional] 
**type** | **String** | The type of data this custom field holds | [optional] 
**uiVisibility** | **String** | Specifies the visibility of custom field in the UI | [optional] 
**url** | **String** |  | [optional] [readonly] 
**validationMaximum** | **Number** | Maximum allowed value (for numeric fields) | [optional] 
**validationMinimum** | **Number** | Minimum allowed value (for numeric fields) | [optional] 
**validationRegex** | **String** | Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, &lt;code&gt;^[A-Z]{3}$&lt;/code&gt; will limit values to exactly three uppercase letters. | [optional] 
**weight** | **Number** | Fields with higher weights appear lower in a form. | [optional] 



## Enum: FilterLogicEnum


* `disabled` (value: `"disabled"`)

* `loose` (value: `"loose"`)

* `exact` (value: `"exact"`)





## Enum: TypeEnum


* `text` (value: `"text"`)

* `longtext` (value: `"longtext"`)

* `integer` (value: `"integer"`)

* `decimal` (value: `"decimal"`)

* `boolean` (value: `"boolean"`)

* `date` (value: `"date"`)

* `url` (value: `"url"`)

* `json` (value: `"json"`)

* `select` (value: `"select"`)

* `multiselect` (value: `"multiselect"`)

* `object` (value: `"object"`)

* `multiobject` (value: `"multiobject"`)





## Enum: UiVisibilityEnum


* `read-write` (value: `"read-write"`)

* `read-only` (value: `"read-only"`)

* `hidden` (value: `"hidden"`)




