

# ContainerServiceOrchestratorProfile

Profile for the container service orchestrator.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**orchestratorType** | [**OrchestratorTypeEnum**](#OrchestratorTypeEnum) | The orchestrator to use to manage container service cluster resources. Valid values are Kubernetes, Swarm, DCOS, DockerCE and Custom. |  |
|**orchestratorVersion** | **String** | The version of the orchestrator to use. You can specify the major.minor.patch part of the actual version.For example, you can specify version as \&quot;1.6.11\&quot;. |  [optional] |



## Enum: OrchestratorTypeEnum

| Name | Value |
|---- | -----|
| KUBERNETES | &quot;Kubernetes&quot; |
| SWARM | &quot;Swarm&quot; |
| DCOS | &quot;DCOS&quot; |
| DOCKER_CE | &quot;DockerCE&quot; |
| CUSTOM | &quot;Custom&quot; |



