# ServiceFabricManagementClient.ApplicationDeltaHealthPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultServiceTypeDeltaHealthPolicy** | [**ServiceTypeDeltaHealthPolicy**](ServiceTypeDeltaHealthPolicy.md) |  | [optional] 
**serviceTypeDeltaHealthPolicies** | [**{String: ServiceTypeDeltaHealthPolicy}**](ServiceTypeDeltaHealthPolicy.md) | Defines a map that contains specific delta health policies for different service types. Each entry specifies as key the service type name and as value a ServiceTypeDeltaHealthPolicy used to evaluate the service health when upgrading the cluster. The map is empty by default.  | [optional] 


