

# CodeConfigurationValues

Describes the basic configuration needed for building and running an App Runner service. This type doesn't support the full set of possible configuration options. Fur full configuration capabilities, use a <code>apprunner.yaml</code> file in the source code repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**runtime** | [**Runtime**](Runtime.md) |  |  |
|**buildCommand** | [**String**](String.md) |  |  [optional] |
|**startCommand** | [**String**](String.md) |  |  [optional] |
|**port** | [**String**](String.md) |  |  [optional] |
|**runtimeEnvironmentVariables** | [**Map**](Map.md) |  |  [optional] |
|**runtimeEnvironmentSecrets** | [**Map**](Map.md) |  |  [optional] |



