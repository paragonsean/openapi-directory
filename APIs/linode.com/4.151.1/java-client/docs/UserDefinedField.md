

# UserDefinedField

A custom field defined by the User with a special syntax within a StackScript. Derived from the contents of the script. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_default** | **String** | The default value.  If not specified, this value will be used.  |  [optional] [readonly] |
|**example** | **String** | An example value for the field.  |  [readonly] |
|**label** | **String** | A human-readable label for the field that will serve as the input prompt for entering the value during deployment.  |  [readonly] |
|**manyOf** | **String** | A list of acceptable values for the field in any quantity, combination or order.  |  [optional] [readonly] |
|**name** | **String** | The name of the field.  |  [readonly] |
|**oneOf** | **String** | A list of acceptable single values for the field.  |  [optional] [readonly] |



