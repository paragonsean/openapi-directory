# ServiceBroker.GoogleCloudServicebrokerV1alpha1Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindable** | **Boolean** | Specifies whether instances of the service can be bound to applications. Required. | [optional] 
**bindingRetrievable** | **Boolean** | Whether the service provides an endpoint to get service bindings. | [optional] 
**dashboardClient** | [**GoogleCloudServicebrokerV1alpha1DashboardClient**](GoogleCloudServicebrokerV1alpha1DashboardClient.md) |  | [optional] 
**description** | **String** | Textual description of the service. Required. | [optional] 
**id** | **String** | ID is a globally unique identifier used to uniquely identify the service. ID is an opaque string. | [optional] 
**instanceRetrievable** | **Boolean** | Whether the service provides an endpoint to get service instances. | [optional] 
**metadata** | **{String: Object}** | A list of metadata for a service offering. Metadata is an arbitrary JSON object. | [optional] 
**name** | **String** | User friendly service name. Name must match [a-z0-9]+ regexp. The name must be globally unique within GCP project. Note, which is different from (\&quot;This must be globally unique within a platform marketplace\&quot;). Required. | [optional] 
**planUpdateable** | **Boolean** | Whether the service supports upgrade/downgrade for some plans. | [optional] 
**plans** | [**[GoogleCloudServicebrokerV1alpha1Plan]**](GoogleCloudServicebrokerV1alpha1Plan.md) | A list of plans for this service. At least one plan is required. | [optional] 
**tags** | **[String]** | Tags provide a flexible mechanism to expose a classification, attribute, or base technology of a service. | [optional] 


