

# AMetadataTemplateUpdateOperation

A [JSON-Patch](https://tools.ietf.org/html/rfc6902) operation for a change to make to the metadata instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Map&lt;String, String&gt;** | The data for the operation. This will vary depending on the operation being performed. |  [optional] |
|**enumOptionKey** | **String** | For operations that affect a single &#x60;enum&#x60; option this defines the key of the option that is affected. |  [optional] |
|**enumOptionKeys** | **List&lt;String&gt;** | For operations that affect multiple &#x60;enum&#x60; options this defines the keys of the options that are affected. |  [optional] |
|**fieldKey** | **String** | For operations that affect a single field this defines the key of the field that is affected. |  [optional] |
|**fieldKeys** | **List&lt;String&gt;** | For operations that affect multiple fields this defines the keys of the fields that are affected. |  [optional] |
|**multiSelectOptionKey** | **String** | For operations that affect a single multi select option this defines the key of the option that is affected. |  [optional] |
|**multiSelectOptionKeys** | **List&lt;String&gt;** | For operations that affect multiple multi select options this defines the keys of the options that are affected. |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | The type of change to perform on the template. Some of these are hazardous as they will change existing templates. |  |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| EDIT_TEMPLATE | &quot;editTemplate&quot; |
| ADD_FIELD | &quot;addField&quot; |
| REORDER_FIELDS | &quot;reorderFields&quot; |
| ADD_ENUM_OPTION | &quot;addEnumOption&quot; |
| REORDER_ENUM_OPTIONS | &quot;reorderEnumOptions&quot; |
| REORDER_MULTI_SELECT_OPTIONS | &quot;reorderMultiSelectOptions&quot; |
| ADD_MULTI_SELECT_OPTION | &quot;addMultiSelectOption&quot; |
| EDIT_FIELD | &quot;editField&quot; |
| REMOVE_FIELD | &quot;removeField&quot; |
| EDIT_ENUM_OPTION | &quot;editEnumOption&quot; |
| REMOVE_ENUM_OPTION | &quot;removeEnumOption&quot; |
| EDIT_MULTI_SELECT_OPTION | &quot;editMultiSelectOption&quot; |
| REMOVE_MULTI_SELECT_OPTION | &quot;removeMultiSelectOption&quot; |



