

# GoogleCloudRunV2EnvVar

EnvVar represents an environment variable present in a Container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. Name of the environment variable. Must not exceed 32768 characters. |  [optional] |
|**value** | **String** | Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any route environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to \&quot;\&quot;, and the maximum length is 32768 bytes. |  [optional] |
|**valueSource** | [**GoogleCloudRunV2EnvVarSource**](GoogleCloudRunV2EnvVarSource.md) |  |  [optional] |



