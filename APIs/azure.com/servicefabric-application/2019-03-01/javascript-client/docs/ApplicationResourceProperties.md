# ServiceFabricManagementClient.ApplicationResourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response | [optional] [readonly] 
**typeName** | **String** | The application type name as defined in the application manifest. | [optional] 
**maximumNodes** | **Number** | The maximum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. By default, the value of this property is zero and it means that the services can be placed on any node. | [optional] [default to 0]
**metrics** | [**[ApplicationMetricDescription]**](ApplicationMetricDescription.md) | List of application capacity metric description. | [optional] 
**minimumNodes** | **Number** | The minimum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. If this property is set to zero, no capacity will be reserved. The value of this property cannot be more than the value of the MaximumNodes property. | [optional] 
**parameters** | **{String: String}** | List of application parameters with overridden values from their default values specified in the application manifest. | [optional] 
**removeApplicationCapacity** | **Boolean** | Remove the current application capacity settings. | [optional] 
**typeVersion** | **String** | The version of the application type as defined in the application manifest. | [optional] 
**upgradePolicy** | [**ApplicationUpgradePolicy**](ApplicationUpgradePolicy.md) |  | [optional] 


