

# PropertyContract

Property details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Uniquely identifies the property within the current API Management service instance. The value is a valid relative URL in the format of /properties/{propId} where {propId} is a property identifier. |  [optional] [readonly] |
|**name** | **String** | Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters. |  |
|**secret** | **Boolean** | Determines whether the value is a secret and should be encrypted or not. Default value is false. |  [optional] |
|**tags** | **List&lt;String&gt;** | Optional tags that when provided can be used to filter the property list. |  [optional] |
|**value** | **String** | Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace. |  |



