

# AcsClusterProperties

Information about the container service backing the cluster

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentCount** | **Integer** | The number of agent nodes in the Container Service. This can be changed to scale the cluster. |  [optional] |
|**agentVmSize** | [**AgentVmSizeEnum**](#AgentVmSizeEnum) | The Azure VM size of the agent VM nodes. This cannot be changed once the cluster is created. |  [optional] |
|**clusterFqdn** | **String** | The FQDN of the cluster.  |  [optional] [readonly] |
|**orchestratorProperties** | [**KubernetesClusterProperties**](KubernetesClusterProperties.md) |  |  |
|**orchestratorType** | [**OrchestratorTypeEnum**](#OrchestratorTypeEnum) | Type of orchestrator. It cannot be changed once the cluster is created. |  |
|**systemServices** | **List&lt;SystemServices&gt;** | The system services deployed to the cluster |  [optional] |



## Enum: AgentVmSizeEnum

| Name | Value |
|---- | -----|
| A0 | &quot;Standard_A0&quot; |
| A1 | &quot;Standard_A1&quot; |
| A2 | &quot;Standard_A2&quot; |
| A3 | &quot;Standard_A3&quot; |
| A4 | &quot;Standard_A4&quot; |
| A5 | &quot;Standard_A5&quot; |
| A6 | &quot;Standard_A6&quot; |
| A7 | &quot;Standard_A7&quot; |
| A8 | &quot;Standard_A8&quot; |
| A9 | &quot;Standard_A9&quot; |
| A10 | &quot;Standard_A10&quot; |
| A11 | &quot;Standard_A11&quot; |
| D1 | &quot;Standard_D1&quot; |
| D2 | &quot;Standard_D2&quot; |
| D3 | &quot;Standard_D3&quot; |
| D4 | &quot;Standard_D4&quot; |
| D11 | &quot;Standard_D11&quot; |
| D12 | &quot;Standard_D12&quot; |
| D13 | &quot;Standard_D13&quot; |
| D14 | &quot;Standard_D14&quot; |
| D1_V2 | &quot;Standard_D1_v2&quot; |
| D2_V2 | &quot;Standard_D2_v2&quot; |
| D3_V2 | &quot;Standard_D3_v2&quot; |
| D4_V2 | &quot;Standard_D4_v2&quot; |
| D5_V2 | &quot;Standard_D5_v2&quot; |
| D11_V2 | &quot;Standard_D11_v2&quot; |
| D12_V2 | &quot;Standard_D12_v2&quot; |
| D13_V2 | &quot;Standard_D13_v2&quot; |
| D14_V2 | &quot;Standard_D14_v2&quot; |
| G1 | &quot;Standard_G1&quot; |
| G2 | &quot;Standard_G2&quot; |
| G3 | &quot;Standard_G3&quot; |
| G4 | &quot;Standard_G4&quot; |
| G5 | &quot;Standard_G5&quot; |
| DS1 | &quot;Standard_DS1&quot; |
| DS2 | &quot;Standard_DS2&quot; |
| DS3 | &quot;Standard_DS3&quot; |
| DS4 | &quot;Standard_DS4&quot; |
| DS11 | &quot;Standard_DS11&quot; |
| DS12 | &quot;Standard_DS12&quot; |
| DS13 | &quot;Standard_DS13&quot; |
| DS14 | &quot;Standard_DS14&quot; |
| GS1 | &quot;Standard_GS1&quot; |
| GS2 | &quot;Standard_GS2&quot; |
| GS3 | &quot;Standard_GS3&quot; |
| GS4 | &quot;Standard_GS4&quot; |
| GS5 | &quot;Standard_GS5&quot; |



## Enum: OrchestratorTypeEnum

| Name | Value |
|---- | -----|
| KUBERNETES | &quot;Kubernetes&quot; |



