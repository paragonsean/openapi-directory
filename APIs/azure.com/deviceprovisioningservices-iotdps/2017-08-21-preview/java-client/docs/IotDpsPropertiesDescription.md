

# IotDpsPropertiesDescription


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocationPolicy** | [**AllocationPolicyEnum**](#AllocationPolicyEnum) | Allocation policy to be used by this provisioning service. |  [optional] |
|**authorizationPolicies** | [**List&lt;SharedAccessSignatureAuthorizationRuleAccessRightsDescription&gt;**](SharedAccessSignatureAuthorizationRuleAccessRightsDescription.md) |  |  [optional] |
|**deviceProvisioningHostName** | **String** | Device endpoint for this provisioning service. |  [optional] [readonly] |
|**idScope** | **String** | Unique identifier of this provisioning service. |  [optional] [readonly] |
|**iotHubs** | [**List&lt;IotHubDefinitionDescription&gt;**](IotHubDefinitionDescription.md) | List of IoT hubs associated with this provisioning service. |  [optional] |
|**provisioningState** | **String** | The ARM provisioning state of the provisioning service. |  [optional] |
|**serviceOperationsHostName** | **String** | Service endpoint for provisioning service. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Current state of the provisioning service. |  [optional] |



## Enum: AllocationPolicyEnum

| Name | Value |
|---- | -----|
| HASHED | &quot;Hashed&quot; |
| GEO_LATENCY | &quot;GeoLatency&quot; |
| STATIC | &quot;Static&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVATING | &quot;Activating&quot; |
| ACTIVE | &quot;Active&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |
| ACTIVATION_FAILED | &quot;ActivationFailed&quot; |
| DELETION_FAILED | &quot;DeletionFailed&quot; |
| TRANSITIONING | &quot;Transitioning&quot; |
| SUSPENDING | &quot;Suspending&quot; |
| SUSPENDED | &quot;Suspended&quot; |
| RESUMING | &quot;Resuming&quot; |
| FAILING_OVER | &quot;FailingOver&quot; |
| FAILOVER_FAILED | &quot;FailoverFailed&quot; |



