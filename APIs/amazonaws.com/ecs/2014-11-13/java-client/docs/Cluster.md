

# Cluster

A regional grouping of one or more container instances where you can run task requests. Each account receives a default cluster the first time you use the Amazon ECS service, but you may also create other clusters. Clusters may contain more than one instance type simultaneously.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterArn** | [**String**](String.md) |  |  [optional] |
|**clusterName** | [**String**](String.md) |  |  [optional] |
|**_configuration** | [**UpdateClusterRequestConfiguration**](UpdateClusterRequestConfiguration.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**registeredContainerInstancesCount** | [**Integer**](Integer.md) |  |  [optional] |
|**runningTasksCount** | [**Integer**](Integer.md) |  |  [optional] |
|**pendingTasksCount** | [**Integer**](Integer.md) |  |  [optional] |
|**activeServicesCount** | [**Integer**](Integer.md) |  |  [optional] |
|**statistics** | [**List**](List.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**settings** | [**List**](List.md) |  |  [optional] |
|**capacityProviders** | [**List**](List.md) |  |  [optional] |
|**defaultCapacityProviderStrategy** | [**List**](List.md) |  |  [optional] |
|**attachments** | [**List**](List.md) |  |  [optional] |
|**attachmentsStatus** | [**String**](String.md) |  |  [optional] |
|**serviceConnectDefaults** | [**ClusterServiceConnectDefaults**](ClusterServiceConnectDefaults.md) |  |  [optional] |



