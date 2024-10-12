# ServiceFabricManagementClient.ServiceTypeDeltaHealthPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxPercentDeltaUnhealthyServices** | **Number** | The maximum allowed percentage of services health degradation allowed during cluster upgrades. The delta is measured between the state of the services at the beginning of upgrade and the state of the services at the time of the health evaluation. The check is performed after every upgrade domain upgrade completion to make sure the global state of the cluster is within tolerated limits.  | [optional] 


