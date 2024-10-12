

# ManagedProperty

A managed property of a managed configuration. The property must match one of the properties in the app restrictions schema of the product. Exactly one of the value fields must be populated, and it must match the property's type in the app restrictions schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The unique key that identifies the property. |  [optional] |
|**valueBool** | **Boolean** | The boolean value - this will only be present if type of the property is bool. |  [optional] |
|**valueBundle** | [**ManagedPropertyBundle**](ManagedPropertyBundle.md) |  |  [optional] |
|**valueBundleArray** | [**List&lt;ManagedPropertyBundle&gt;**](ManagedPropertyBundle.md) | The list of bundles of properties - this will only be present if type of the property is bundle_array. |  [optional] |
|**valueInteger** | **Integer** | The integer value - this will only be present if type of the property is integer. |  [optional] |
|**valueString** | **String** | The string value - this will only be present if type of the property is string, choice or hidden. |  [optional] |
|**valueStringArray** | **List&lt;String&gt;** | The list of string values - this will only be present if type of the property is multiselect. |  [optional] |



