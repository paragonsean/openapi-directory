

# AttributeDefinition

A client-defined consent attribute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedValues** | **List&lt;String&gt;** | Required. Possible values for the attribute. The number of allowed values must not exceed 500. An empty list is invalid. The list can only be expanded after creation. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Required. The category of the attribute. The value of this field cannot be changed after creation. |  [optional] |
|**consentDefaultValues** | **List&lt;String&gt;** | Optional. Default values of the attribute in Consents. If no default values are specified, it defaults to an empty value. |  [optional] |
|**dataMappingDefaultValue** | **String** | Optional. Default value of the attribute in User data mappings. If no default value is specified, it defaults to an empty value. This field is only applicable to attributes of the category &#x60;RESOURCE&#x60;. |  [optional] |
|**description** | **String** | Optional. A description of the attribute. |  [optional] |
|**name** | **String** | Identifier. Resource name of the Attribute definition, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/consentStores/{consent_store_id}/attributeDefinitions/{attribute_definition_id}&#x60;. Cannot be changed after creation. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| CATEGORY_UNSPECIFIED | &quot;CATEGORY_UNSPECIFIED&quot; |
| RESOURCE | &quot;RESOURCE&quot; |
| REQUEST | &quot;REQUEST&quot; |



