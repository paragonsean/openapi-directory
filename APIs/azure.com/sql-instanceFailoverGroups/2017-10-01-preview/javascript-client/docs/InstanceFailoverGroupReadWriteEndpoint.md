# SqlManagementClient.InstanceFailoverGroupReadWriteEndpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failoverPolicy** | **String** | Failover policy of the read-write endpoint for the failover group. If failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is required. | 
**failoverWithDataLossGracePeriodMinutes** | **Number** | Grace period before failover with data loss is attempted for the read-write endpoint. If failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is required. | [optional] 



## Enum: FailoverPolicyEnum


* `Manual` (value: `"Manual"`)

* `Automatic` (value: `"Automatic"`)




