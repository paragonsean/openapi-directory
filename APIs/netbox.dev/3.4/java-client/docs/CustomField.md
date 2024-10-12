

# CustomField


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**choices** | **List&lt;String&gt;** | Comma-separated list of available choices (for selection fields) |  [optional] |
|**contentTypes** | **Set&lt;String&gt;** |  |  |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**dataType** | **String** |  |  [optional] [readonly] |
|**_default** | **Object** | Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. \&quot;Foo\&quot;). |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**filterLogic** | [**FilterLogic**](FilterLogic.md) |  |  [optional] |
|**groupName** | **String** | Custom fields within the same group will be displayed together |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**label** | **String** | Name of the field as displayed to users (if not provided, the field&#39;s name will be used) |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** | Internal field name |  |
|**objectType** | **String** |  |  [optional] |
|**required** | **Boolean** | If true, this field is required when creating new objects or editing an existing object. |  [optional] |
|**searchWeight** | **Integer** | Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored. |  [optional] |
|**type** | [**Type1**](Type1.md) |  |  |
|**uiVisibility** | [**UiVisibility**](UiVisibility.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**validationMaximum** | **Integer** | Maximum allowed value (for numeric fields) |  [optional] |
|**validationMinimum** | **Integer** | Minimum allowed value (for numeric fields) |  [optional] |
|**validationRegex** | **String** | Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, &lt;code&gt;^[A-Z]{3}$&lt;/code&gt; will limit values to exactly three uppercase letters. |  [optional] |
|**weight** | **Integer** | Fields with higher weights appear lower in a form. |  [optional] |



