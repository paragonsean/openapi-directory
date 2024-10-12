

# Environment

An Environment describes a collection of environment variables to set when executing Tasks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptedVariables** | [**KMSEnvMap**](KMSEnvMap.md) |  |  [optional] |
|**secretVariables** | **Map&lt;String, String&gt;** | A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable. |  [optional] |
|**variables** | **Map&lt;String, String&gt;** | A map of environment variable names to values. |  [optional] |



