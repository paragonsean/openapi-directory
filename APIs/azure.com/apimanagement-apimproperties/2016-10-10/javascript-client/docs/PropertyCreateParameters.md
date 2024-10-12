# ApiManagementClient.PropertyCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Unique name of Property. It may contain only letters, digits, period, dash, and underscore characters. | 
**secret** | **Boolean** | Determines whether the value is a secret and should be encrypted or not. Default value is false. | [optional] 
**tags** | **[String]** | Optional tags that when provided can be used to filter the property list. | [optional] 
**value** | **String** | Value of the property. Can contain policy expressions. It may not be empty or consist only of whitespace. | 


