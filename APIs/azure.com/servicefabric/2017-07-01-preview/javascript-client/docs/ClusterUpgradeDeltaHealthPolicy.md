# ServiceFabricManagementClient.ClusterUpgradeDeltaHealthPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPercentDeltaUnhealthyApplications** | **Number** | The maximum allowed percentage of applications health degradation allowed during cluster upgrades. The delta is measured between the state of the applications at the beginning of upgrade and the state of the applications at the time of the health evaluation. The check is performed after every upgrade domain upgrade completion to make sure the global state of the cluster is within tolerated limits. System services are not included in this. | 
**maxPercentDeltaUnhealthyNodes** | **Number** | The maximum allowed percentage of nodes health degradation allowed during cluster upgrades. The delta is measured between the state of the nodes at the beginning of upgrade and the state of the nodes at the time of the health evaluation. The check is performed after every upgrade domain upgrade completion to make sure the global state of the cluster is within tolerated limits. | 
**maxPercentUpgradeDomainDeltaUnhealthyNodes** | **Number** | The maximum allowed percentage of upgrade domain nodes health degradation allowed during cluster upgrades. The delta is measured between the state of the upgrade domain nodes at the beginning of upgrade and the state of the upgrade domain nodes at the time of the health evaluation. The check is performed after every upgrade domain upgrade completion for all completed upgrade domains to make sure the state of the upgrade domains is within tolerated limits.  | 


