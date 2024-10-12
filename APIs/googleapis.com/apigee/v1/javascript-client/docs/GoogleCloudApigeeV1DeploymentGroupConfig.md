# ApigeeApi.GoogleCloudApigeeV1DeploymentGroupConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploymentGroupType** | **String** | Type of the deployment group, which will be either Standard or Extensible. | [optional] 
**name** | **String** | Name of the deployment group in the following format: &#x60;organizations/{org}/environments/{env}/deploymentGroups/{group}&#x60;. | [optional] 
**revisionId** | **String** | Revision number which can be used by the runtime to detect if the deployment group has changed between two versions. | [optional] 
**uid** | **String** | Unique ID. The ID will only change if the deployment group is deleted and recreated. | [optional] 



## Enum: DeploymentGroupTypeEnum


* `DEPLOYMENT_GROUP_TYPE_UNSPECIFIED` (value: `"DEPLOYMENT_GROUP_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `EXTENSIBLE` (value: `"EXTENSIBLE"`)




