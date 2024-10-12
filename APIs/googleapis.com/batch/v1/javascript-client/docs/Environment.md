# BatchApi.Environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptedVariables** | [**KMSEnvMap**](KMSEnvMap.md) |  | [optional] 
**secretVariables** | **{String: String}** | A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable. | [optional] 
**variables** | **{String: String}** | A map of environment variable names to values. | [optional] 


