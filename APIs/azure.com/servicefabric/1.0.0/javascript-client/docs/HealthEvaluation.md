# ServiceFabricClient.HealthEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregatedHealthState** | [**HealthState**](HealthState.md) |  | [optional] 
**description** | **String** |  | [optional] 
**kind** | **String** |  | 



## Enum: KindEnum


* `Invalid` (value: `"Invalid"`)

* `Event` (value: `"Event"`)

* `Replicas` (value: `"Replicas"`)

* `Partitions` (value: `"Partitions"`)

* `DeployedServicePackages` (value: `"DeployedServicePackages"`)

* `DeployedApplications` (value: `"DeployedApplications"`)

* `Services` (value: `"Services"`)

* `Nodes` (value: `"Nodes"`)

* `Applications` (value: `"Applications"`)

* `SystemApplication` (value: `"SystemApplication"`)

* `UpgradeDomainDeployedApplications` (value: `"UpgradeDomainDeployedApplications"`)

* `UpgradeDomainNodes` (value: `"UpgradeDomainNodes"`)

* `Node` (value: `"Node"`)

* `Replica` (value: `"Replica"`)

* `Partition` (value: `"Partition"`)

* `Service` (value: `"Service"`)

* `DeployedServicePackage` (value: `"DeployedServicePackage"`)

* `DeployedApplication` (value: `"DeployedApplication"`)

* `Application` (value: `"Application"`)

* `DeltaNodesCheck` (value: `"DeltaNodesCheck"`)

* `UpgradeDomainDeltaNodesCheck` (value: `"UpgradeDomainDeltaNodesCheck"`)

* `ApplicationTypeApplications` (value: `"ApplicationTypeApplications"`)




