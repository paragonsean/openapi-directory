# IxApi.P2MPNetworkServiceConfigUpdatePartial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. | [optional] 
**capacity** | **Number** | The capacity of the service in Mbps. If set to Null, the maximum capacity will be used, i.e. the virtual circuit is not rate-limited.  An exchange may choose to constrain the available capacity range of a &#x60;ProductOffering&#x60;.  That means, the service can consume up to the total bandwidth of the &#x60;Connection&#x60;.  Typically the service is charged based on the capacity. | [optional] 
**connection** | **String** | The id of the connection to use for this &#x60;NetworkServiceConfig&#x60;. | [optional] 
**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  | [optional] 
**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  | [optional] 
**externalRef** | **String** | Reference field, free to use for the API user. | [optional] 
**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  | [optional] 
**networkFeatureConfigs** | **[String]** | A list of ids of &#x60;NetworkFeatureConfig&#x60;s.  | [optional] [readonly] 
**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  | [optional] [default to &#39;&#39;]
**role** | **String** | A &#x60;leaf&#x60; can only reach roots and is isolated from other leafs. A &#x60;root&#x60; can reach any other point in the virtual circuit including other roots. | [optional] [default to &#39;leaf&#39;]
**roleAssignments** | **[String]** | A set of &#x60;RoleAssignment&#x60;s. See the documentation on the specific &#x60;required_contact_roles&#x60;, &#x60;nfc_required_contact_roles&#x60; or &#x60;nsc_required_contact_roles&#x60; on what &#x60;RoleAssignment&#x60;s to provide.  | [optional] 
**type** | **String** |  | 
**vlanConfig** | [**VlanConfig**](VlanConfig.md) |  | [optional] 



## Enum: RoleEnum


* `root` (value: `"root"`)

* `leaf` (value: `"leaf"`)




