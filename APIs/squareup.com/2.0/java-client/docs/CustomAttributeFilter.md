

# CustomAttributeFilter

Supported custom attribute query expressions for calling the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint to search for items or item variations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolFilter** | **Boolean** | A query expression to filter items or item variations by matching their custom attributes&#39; &#x60;boolean_value&#x60; property values against the specified Boolean expression. |  [optional] |
|**customAttributeDefinitionId** | **String** | A query expression to filter items or item variations by matching their custom attributes&#39; &#x60;custom_attribute_definition_id&#x60; property value against the the specified id. |  [optional] |
|**key** | **String** | A query expression to filter items or item variations by matching their custom attributes&#39; &#x60;key&#x60; property value against the specified key. |  [optional] |
|**numberFilter** | [**Range**](Range.md) |  |  [optional] |
|**selectionUidsFilter** | **List&lt;String&gt;** | A query expression to filter items or item variations by matching  their custom attributes&#39; &#x60;selection_uid_values&#x60; values against the specified selection uids. |  [optional] |
|**stringFilter** | **String** | A query expression to filter items or item variations by matching their custom attributes&#39; &#x60;string_value&#x60;  property value against the specified text. |  [optional] |



