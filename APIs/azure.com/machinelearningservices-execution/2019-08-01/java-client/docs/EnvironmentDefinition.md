

# EnvironmentDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**docker** | [**DockerSection**](DockerSection.md) |  |  [optional] |
|**environmentVariables** | **Map&lt;String, String&gt;** | Definition of environment variables to be defined in the environment. |  [optional] |
|**inferencingStackVersion** | **String** | The inferencing stack version added to the image. To avoid adding an inferencing stack, do not set this value. Valid values: \&quot;latest\&quot;. |  [optional] |
|**name** | **String** | The name of the environment. |  [optional] |
|**python** | [**PythonSection**](PythonSection.md) |  |  [optional] |
|**spark** | [**SparkSection**](SparkSection.md) |  |  [optional] |
|**version** | **String** | The environment version. |  [optional] |



