# ServiceFabricClientApis.UpdateClusterUpgradeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationHealthPolicyMap** | [**ApplicationHealthPolicies**](ApplicationHealthPolicies.md) |  | [optional] 
**clusterHealthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  | [optional] 
**clusterUpgradeHealthPolicy** | [**ClusterUpgradeHealthPolicyObject**](ClusterUpgradeHealthPolicyObject.md) |  | [optional] 
**enableDeltaHealthEvaluation** | **Boolean** | When true, enables delta health evaluation rather than absolute health evaluation after completion of each upgrade domain. | [optional] 
**updateDescription** | [**RollingUpgradeUpdateDescription**](RollingUpgradeUpdateDescription.md) |  | [optional] 
**upgradeKind** | [**UpgradeType**](UpgradeType.md) |  | [optional] 


