

# ApplicationDeltaHealthPolicy

Defines a delta health policy used to evaluate the health of an application or one of its child entities when upgrading the cluster. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultServiceTypeDeltaHealthPolicy** | [**ServiceTypeDeltaHealthPolicy**](ServiceTypeDeltaHealthPolicy.md) |  |  [optional] |
|**serviceTypeDeltaHealthPolicies** | [**Map&lt;String, ServiceTypeDeltaHealthPolicy&gt;**](ServiceTypeDeltaHealthPolicy.md) | Defines a map that contains specific delta health policies for different service types. Each entry specifies as key the service type name and as value a ServiceTypeDeltaHealthPolicy used to evaluate the service health when upgrading the cluster. The map is empty by default.  |  [optional] |



