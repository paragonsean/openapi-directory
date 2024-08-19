

# ContainerDefinition

Container definitions are used in task definitions to describe the different containers that are launched as part of a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**image** | [**String**](String.md) |  |  [optional] |
|**repositoryCredentials** | [**ContainerDefinitionRepositoryCredentials**](ContainerDefinitionRepositoryCredentials.md) |  |  [optional] |
|**cpu** | [**Integer**](Integer.md) |  |  [optional] |
|**memory** | [**Integer**](Integer.md) |  |  [optional] |
|**memoryReservation** | [**Integer**](Integer.md) |  |  [optional] |
|**links** | [**List**](List.md) |  |  [optional] |
|**portMappings** | [**List**](List.md) |  |  [optional] |
|**essential** | [**Boolean**](Boolean.md) |  |  [optional] |
|**entryPoint** | [**List**](List.md) |  |  [optional] |
|**command** | [**List**](List.md) |  |  [optional] |
|**environment** | [**List**](List.md) |  |  [optional] |
|**environmentFiles** | [**List**](List.md) |  |  [optional] |
|**mountPoints** | [**List**](List.md) |  |  [optional] |
|**volumesFrom** | [**List**](List.md) |  |  [optional] |
|**linuxParameters** | [**ContainerDefinitionLinuxParameters**](ContainerDefinitionLinuxParameters.md) |  |  [optional] |
|**secrets** | [**List**](List.md) |  |  [optional] |
|**dependsOn** | [**List**](List.md) |  |  [optional] |
|**startTimeout** | [**Integer**](Integer.md) |  |  [optional] |
|**stopTimeout** | [**Integer**](Integer.md) |  |  [optional] |
|**hostname** | [**String**](String.md) |  |  [optional] |
|**user** | [**String**](String.md) |  |  [optional] |
|**workingDirectory** | [**String**](String.md) |  |  [optional] |
|**disableNetworking** | [**Boolean**](Boolean.md) |  |  [optional] |
|**privileged** | [**Boolean**](Boolean.md) |  |  [optional] |
|**readonlyRootFilesystem** | [**Boolean**](Boolean.md) |  |  [optional] |
|**dnsServers** | [**List**](List.md) |  |  [optional] |
|**dnsSearchDomains** | [**List**](List.md) |  |  [optional] |
|**extraHosts** | [**List**](List.md) |  |  [optional] |
|**dockerSecurityOptions** | [**List**](List.md) |  |  [optional] |
|**interactive** | [**Boolean**](Boolean.md) |  |  [optional] |
|**pseudoTerminal** | [**Boolean**](Boolean.md) |  |  [optional] |
|**dockerLabels** | [**Map**](Map.md) |  |  [optional] |
|**ulimits** | [**List**](List.md) |  |  [optional] |
|**logConfiguration** | [**ContainerDefinitionLogConfiguration**](ContainerDefinitionLogConfiguration.md) |  |  [optional] |
|**healthCheck** | [**ContainerDefinitionHealthCheck**](ContainerDefinitionHealthCheck.md) |  |  [optional] |
|**systemControls** | [**List**](List.md) |  |  [optional] |
|**resourceRequirements** | [**List**](List.md) |  |  [optional] |
|**firelensConfiguration** | [**ContainerDefinitionFirelensConfiguration**](ContainerDefinitionFirelensConfiguration.md) |  |  [optional] |
|**credentialSpecs** | [**List**](List.md) |  |  [optional] |



