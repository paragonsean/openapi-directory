# BlockchainManagementClient.BlockchainMemberProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consortium** | **String** | Gets or sets the consortium for the blockchain member. | [optional] 
**consortiumManagementAccountAddress** | **String** | Gets the managed consortium management account address. | [optional] [readonly] 
**consortiumManagementAccountPassword** | **String** | Sets the managed consortium management account password. | [optional] 
**consortiumMemberDisplayName** | **String** | Gets the display name of the member in the consortium. | [optional] 
**consortiumRole** | **String** | Gets the role of the member in the consortium. | [optional] 
**dns** | **String** | Gets the dns endpoint of the blockchain member. | [optional] [readonly] 
**firewallRules** | [**[FirewallRule]**](FirewallRule.md) | Gets or sets firewall rules | [optional] 
**password** | **String** | Sets the basic auth password of the blockchain member. | [optional] 
**protocol** | **String** | Gets or sets the blockchain protocol. | [optional] 
**provisioningState** | **String** | Gets or sets the blockchain member provision state. | [optional] [readonly] 
**publicKey** | **String** | Gets the public key of the blockchain member (default transaction node). | [optional] [readonly] 
**rootContractAddress** | **String** | Gets the Ethereum root contract address of the blockchain. | [optional] [readonly] 
**userName** | **String** | Gets the auth user name of the blockchain member. | [optional] [readonly] 
**validatorNodesSku** | [**BlockchainMemberNodesSku**](BlockchainMemberNodesSku.md) |  | [optional] 



## Enum: ProtocolEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `Parity` (value: `"Parity"`)

* `Quorum` (value: `"Quorum"`)

* `Corda` (value: `"Corda"`)





## Enum: ProvisioningStateEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Stale` (value: `"Stale"`)




