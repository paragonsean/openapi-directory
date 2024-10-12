

# ConfigurationVariables

A configuration variables resource contains the managed configuration settings ID to be applied to a single user, as well as the variable set that is attributed to the user. The variable set will be used to replace placeholders in the managed configuration settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mcmId** | **String** | The ID of the managed configurations settings. |  [optional] |
|**variableSet** | [**List&lt;VariableSet&gt;**](VariableSet.md) | The variable set that is attributed to the user. |  [optional] |



