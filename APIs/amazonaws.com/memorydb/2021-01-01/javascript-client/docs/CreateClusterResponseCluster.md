# AmazonMemoryDb.CreateClusterResponseCluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**status** | **String** |  | [optional] 
**pendingUpdates** | [**ClusterPendingUpdates**](ClusterPendingUpdates.md) |  | [optional] 
**numberOfShards** | **Number** |  | [optional] 
**shards** | **Array** |  | [optional] 
**availabilityMode** | [**AZStatus**](AZStatus.md) |  | [optional] 
**clusterEndpoint** | [**ClusterClusterEndpoint**](ClusterClusterEndpoint.md) |  | [optional] 
**nodeType** | **String** |  | [optional] 
**engineVersion** | **String** |  | [optional] 
**enginePatchVersion** | **String** |  | [optional] 
**parameterGroupName** | **String** |  | [optional] 
**parameterGroupStatus** | **String** |  | [optional] 
**securityGroups** | **Array** |  | [optional] 
**subnetGroupName** | **String** |  | [optional] 
**tLSEnabled** | **Boolean** |  | [optional] 
**kmsKeyId** | **String** |  | [optional] 
**ARN** | **String** |  | [optional] 
**snsTopicArn** | **String** |  | [optional] 
**snsTopicStatus** | **String** |  | [optional] 
**snapshotRetentionLimit** | **Number** |  | [optional] 
**maintenanceWindow** | **String** |  | [optional] 
**snapshotWindow** | **String** |  | [optional] 
**aCLName** | **String** |  | [optional] 
**autoMinorVersionUpgrade** | **Boolean** |  | [optional] 
**dataTiering** | [**DataTieringStatus**](DataTieringStatus.md) |  | [optional] 


