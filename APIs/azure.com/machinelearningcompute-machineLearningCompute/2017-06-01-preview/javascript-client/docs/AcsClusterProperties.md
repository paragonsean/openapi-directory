# AzureMachineLearningComputeManagementClient.AcsClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentCount** | **Number** | The number of agent nodes in the Container Service. This can be changed to scale the cluster. | [optional] 
**agentVmSize** | **String** | The Azure VM size of the agent VM nodes. This cannot be changed once the cluster is created. | [optional] [default to &#39;Standard_D2_v2&#39;]
**clusterFqdn** | **String** | The FQDN of the cluster.  | [optional] [readonly] 
**orchestratorProperties** | [**KubernetesClusterProperties**](KubernetesClusterProperties.md) |  | 
**orchestratorType** | **String** | Type of orchestrator. It cannot be changed once the cluster is created. | 
**systemServices** | [**[SystemServices]**](SystemServices.md) | The system services deployed to the cluster | [optional] 



## Enum: AgentVmSizeEnum


* `A0` (value: `"Standard_A0"`)

* `A1` (value: `"Standard_A1"`)

* `A2` (value: `"Standard_A2"`)

* `A3` (value: `"Standard_A3"`)

* `A4` (value: `"Standard_A4"`)

* `A5` (value: `"Standard_A5"`)

* `A6` (value: `"Standard_A6"`)

* `A7` (value: `"Standard_A7"`)

* `A8` (value: `"Standard_A8"`)

* `A9` (value: `"Standard_A9"`)

* `A10` (value: `"Standard_A10"`)

* `A11` (value: `"Standard_A11"`)

* `D1` (value: `"Standard_D1"`)

* `D2` (value: `"Standard_D2"`)

* `D3` (value: `"Standard_D3"`)

* `D4` (value: `"Standard_D4"`)

* `D11` (value: `"Standard_D11"`)

* `D12` (value: `"Standard_D12"`)

* `D13` (value: `"Standard_D13"`)

* `D14` (value: `"Standard_D14"`)

* `D1_v2` (value: `"Standard_D1_v2"`)

* `D2_v2` (value: `"Standard_D2_v2"`)

* `D3_v2` (value: `"Standard_D3_v2"`)

* `D4_v2` (value: `"Standard_D4_v2"`)

* `D5_v2` (value: `"Standard_D5_v2"`)

* `D11_v2` (value: `"Standard_D11_v2"`)

* `D12_v2` (value: `"Standard_D12_v2"`)

* `D13_v2` (value: `"Standard_D13_v2"`)

* `D14_v2` (value: `"Standard_D14_v2"`)

* `G1` (value: `"Standard_G1"`)

* `G2` (value: `"Standard_G2"`)

* `G3` (value: `"Standard_G3"`)

* `G4` (value: `"Standard_G4"`)

* `G5` (value: `"Standard_G5"`)

* `DS1` (value: `"Standard_DS1"`)

* `DS2` (value: `"Standard_DS2"`)

* `DS3` (value: `"Standard_DS3"`)

* `DS4` (value: `"Standard_DS4"`)

* `DS11` (value: `"Standard_DS11"`)

* `DS12` (value: `"Standard_DS12"`)

* `DS13` (value: `"Standard_DS13"`)

* `DS14` (value: `"Standard_DS14"`)

* `GS1` (value: `"Standard_GS1"`)

* `GS2` (value: `"Standard_GS2"`)

* `GS3` (value: `"Standard_GS3"`)

* `GS4` (value: `"Standard_GS4"`)

* `GS5` (value: `"Standard_GS5"`)





## Enum: OrchestratorTypeEnum


* `Kubernetes` (value: `"Kubernetes"`)




