

# FailoverGroupReadWriteEndpoint

Read-write endpoint of the failover group instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failoverPolicy** | [**FailoverPolicyEnum**](#FailoverPolicyEnum) | Failover policy of the read-write endpoint for the failover group. If failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is required. |  |
|**failoverWithDataLossGracePeriodMinutes** | **Integer** | Grace period before failover with data loss is attempted for the read-write endpoint. If failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is required. |  [optional] |



## Enum: FailoverPolicyEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;Manual&quot; |
| AUTOMATIC | &quot;Automatic&quot; |



