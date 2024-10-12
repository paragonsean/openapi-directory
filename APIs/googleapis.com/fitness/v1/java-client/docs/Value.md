

# Value

Holder object for the value of a single field in a data point. A field value has a particular format and is only ever set to one of an integer or a floating point value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fpVal** | **Double** | Floating point value. When this is set, other values must not be set. |  [optional] |
|**intVal** | **Integer** | Integer value. When this is set, other values must not be set. |  [optional] |
|**mapVal** | [**List&lt;ValueMapValEntry&gt;**](ValueMapValEntry.md) | Map value. The valid key space and units for the corresponding value of each entry should be documented as part of the data type definition. Keys should be kept small whenever possible. Data streams with large keys and high data frequency may be down sampled. |  [optional] |
|**stringVal** | **String** | String value. When this is set, other values must not be set. Strings should be kept small whenever possible. Data streams with large string values and high data frequency may be down sampled. |  [optional] |



