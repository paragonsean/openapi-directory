

# ContainerOverride

Per container override specification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | Arguments to the entrypoint. The specified arguments replace and override any existing entrypoint arguments. Must be empty if &#x60;clear_args&#x60; is set to true. |  [optional] |
|**clearArgs** | **Boolean** | Optional. Set to True to clear all existing arguments. |  [optional] |
|**env** | [**List&lt;EnvVar&gt;**](EnvVar.md) | List of environment variables to set in the container. All specified environment variables are merged with existing environment variables. When the specified environment variables exist, these values override any existing values. |  [optional] |
|**name** | **String** | The name of the container specified as a DNS_LABEL. |  [optional] |



