# ApigeeApi.GoogleCloudApigeeV1DeploymentChangeReportRoutingChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Human-readable description of this routing change. | [optional] 
**environmentGroup** | **String** | Name of the environment group affected by this routing change. | [optional] 
**fromDeployment** | [**GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment**](GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment.md) |  | [optional] 
**shouldSequenceRollout** | **Boolean** | Set to &#x60;true&#x60; if using sequenced rollout would make this routing change safer. **Note**: This does not necessarily imply that automated sequenced rollout mode is supported for the operation. | [optional] 
**toDeployment** | [**GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment**](GoogleCloudApigeeV1DeploymentChangeReportRoutingDeployment.md) |  | [optional] 


