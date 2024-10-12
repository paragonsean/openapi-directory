

# TransactionNodeProperties

Payload of transaction node properties payload in the transaction node payload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dns** | **String** | Gets or sets the transaction node dns endpoint. |  [optional] [readonly] |
|**firewallRules** | [**List&lt;FirewallRule&gt;**](FirewallRule.md) | Gets or sets the firewall rules. |  [optional] |
|**password** | **String** | Sets the transaction node dns endpoint basic auth password. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets or sets the blockchain member provision state. |  [optional] [readonly] |
|**publicKey** | **String** | Gets or sets the transaction node public key. |  [optional] [readonly] |
|**userName** | **String** | Gets or sets the transaction node dns endpoint basic auth user name. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |



