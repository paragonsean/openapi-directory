

# StatelessServiceUpdateDescription

Describes an update for a stateless service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceCloseDelayDurationSeconds** | **String** | Duration in seconds, to wait before a stateless instance is closed, to allow the active requests to drain gracefully. This would be effective when the instance is closing during the application/cluster upgrade and disabling node. The endpoint exposed on this instance is removed prior to starting the delay, which prevents new connections to this instance. In addition, clients that have subscribed to service endpoint change events(https://docs.microsoft.com/en-us/dotnet/api/system.fabric.fabricclient.servicemanagementclient.registerservicenotificationfilterasync), can do the following upon receiving the endpoint removal notification:     - Stop sending new requests to this instance.     - Close existing connections after in-flight requests have completed.     - Connect to a different instance of the service partition for future requests. |  [optional] |
|**instanceCount** | **Integer** | The instance count. |  [optional] |
|**minInstanceCount** | **Integer** | MinInstanceCount is the minimum number of instances that must be up to meet the EnsureAvailability safety check during operations like upgrade or deactivate node. The actual number that is used is max( MinInstanceCount, ceil( MinInstancePercentage/100.0 * InstanceCount) ). Note, if InstanceCount is set to -1, during MinInstanceCount computation -1 is first converted into the number of nodes on which the instances are allowed to be placed according to the placement constraints on the service. |  [optional] |
|**minInstancePercentage** | **Integer** | MinInstancePercentage is the minimum percentage of InstanceCount that must be up to meet the EnsureAvailability safety check during operations like upgrade or deactivate node. The actual number that is used is max( MinInstanceCount, ceil( MinInstancePercentage/100.0 * InstanceCount) ). Note, if InstanceCount is set to -1, during MinInstancePercentage computation, -1 is first converted into the number of nodes on which the instances are allowed to be placed according to the placement constraints on the service. |  [optional] |



