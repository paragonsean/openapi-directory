# BlockchainManagementClient.TransactionNodeProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | **String** | Gets or sets the transaction node dns endpoint. | [optional] [readonly] 
**firewallRules** | [**[FirewallRule]**](FirewallRule.md) | Gets or sets the firewall rules. | [optional] 
**password** | **String** | Sets the transaction node dns endpoint basic auth password. | [optional] 
**provisioningState** | **String** | Gets or sets the blockchain member provision state. | [optional] [readonly] 
**publicKey** | **String** | Gets or sets the transaction node public key. | [optional] [readonly] 
**userName** | **String** | Gets or sets the transaction node dns endpoint basic auth user name. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




