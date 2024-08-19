

# ApplicationResourceProperties

The application resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response |  [optional] [readonly] |
|**typeName** | **String** | The application type name as defined in the application manifest. |  [optional] |
|**managedIdentities** | [**List&lt;ApplicationUserAssignedIdentity&gt;**](ApplicationUserAssignedIdentity.md) | List of user assigned identities for the application, each mapped to a friendly name. |  [optional] |
|**maximumNodes** | **Long** | The maximum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. By default, the value of this property is zero and it means that the services can be placed on any node. |  [optional] |
|**metrics** | [**List&lt;ApplicationMetricDescription&gt;**](ApplicationMetricDescription.md) | List of application capacity metric description. |  [optional] |
|**minimumNodes** | **Long** | The minimum number of nodes where Service Fabric will reserve capacity for this application. Note that this does not mean that the services of this application will be placed on all of those nodes. If this property is set to zero, no capacity will be reserved. The value of this property cannot be more than the value of the MaximumNodes property. |  [optional] |
|**parameters** | **Map&lt;String, String&gt;** | List of application parameters with overridden values from their default values specified in the application manifest. |  [optional] |
|**removeApplicationCapacity** | **Boolean** | Remove the current application capacity settings. |  [optional] |
|**typeVersion** | **String** | The version of the application type as defined in the application manifest. |  [optional] |
|**upgradePolicy** | [**ApplicationUpgradePolicy**](ApplicationUpgradePolicy.md) |  |  [optional] |



