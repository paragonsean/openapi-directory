

# Deployment

The details of an Amazon ECS service deployment. This is used only when a service uses the <code>ECS</code> deployment controller type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**taskDefinition** | [**String**](String.md) |  |  [optional] |
|**desiredCount** | [**Integer**](Integer.md) |  |  [optional] |
|**pendingCount** | [**Integer**](Integer.md) |  |  [optional] |
|**runningCount** | [**Integer**](Integer.md) |  |  [optional] |
|**failedTasks** | [**Integer**](Integer.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**capacityProviderStrategy** | [**List**](List.md) |  |  [optional] |
|**launchType** | [**LaunchType**](LaunchType.md) |  |  [optional] |
|**platformVersion** | [**String**](String.md) |  |  [optional] |
|**platformFamily** | [**String**](String.md) |  |  [optional] |
|**networkConfiguration** | [**StartTaskRequestNetworkConfiguration**](StartTaskRequestNetworkConfiguration.md) |  |  [optional] |
|**rolloutState** | [**DeploymentRolloutState**](DeploymentRolloutState.md) |  |  [optional] |
|**rolloutStateReason** | [**String**](String.md) |  |  [optional] |
|**serviceConnectConfiguration** | [**DeploymentServiceConnectConfiguration**](DeploymentServiceConnectConfiguration.md) |  |  [optional] |
|**serviceConnectResources** | [**List**](List.md) |  |  [optional] |



