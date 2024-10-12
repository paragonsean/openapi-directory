# ServiceBroker.GoogleCloudServicebrokerV1alpha1ServiceInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **{String: Object}** | Platform specific contextual information under which the service instance is to be provisioned. This replaces organization_guid and space_guid. But can also contain anything. Currently only used for logging context information. | [optional] 
**createTime** | **String** | Output only. Timestamp for when the instance was created. | [optional] 
**deploymentName** | **String** | Output only. Name of the Deployment Manager deployment used for provisioning of this service instance. | [optional] 
**instanceId** | **String** | The id of the service instance. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. | [optional] 
**organizationGuid** | **String** | The platform GUID for the organization under which the service is to be provisioned. Required. | [optional] 
**parameters** | **{String: Object}** | Configuration options for the service instance. Parameters is JSON object serialized to string. | [optional] 
**planId** | **String** | The ID of the plan. See &#x60;Service&#x60; and &#x60;Plan&#x60; resources for details. Maximum length is 64, GUID recommended. Required. | [optional] 
**previousValues** | **{String: Object}** | Used only in UpdateServiceInstance request to optionally specify previous fields. | [optional] 
**resourceName** | **String** | Output only. The resource name of the instance, e.g. projects/project_id/brokers/broker_id/service_instances/instance_id | [optional] 
**serviceId** | **String** | The id of the service. Must be a valid identifier of a service contained in the list from a &#x60;ListServices()&#x60; call. Maximum length is 64, GUID recommended. Required. | [optional] 
**spaceGuid** | **String** | The identifier for the project space within the platform organization. Required. | [optional] 


