

# GoogleCloudApigeeV1DeploymentGroupConfig

DeploymentGroupConfig represents a deployment group that should be present in a particular environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentGroupType** | [**DeploymentGroupTypeEnum**](#DeploymentGroupTypeEnum) | Type of the deployment group, which will be either Standard or Extensible. |  [optional] |
|**name** | **String** | Name of the deployment group in the following format: &#x60;organizations/{org}/environments/{env}/deploymentGroups/{group}&#x60;. |  [optional] |
|**revisionId** | **String** | Revision number which can be used by the runtime to detect if the deployment group has changed between two versions. |  [optional] |
|**uid** | **String** | Unique ID. The ID will only change if the deployment group is deleted and recreated. |  [optional] |



## Enum: DeploymentGroupTypeEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_GROUP_TYPE_UNSPECIFIED | &quot;DEPLOYMENT_GROUP_TYPE_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| EXTENSIBLE | &quot;EXTENSIBLE&quot; |



