

# NetworkServiceRequestPartial

Polymorphic Network Service Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccount** | **String** | An account requires billing_information to be used as a &#x60;billing_account&#x60;. |  [optional] |
|**consumingAccount** | **String** | The &#x60;id&#x60; of the account consuming a service.  Used to be &#x60;owning_customer&#x60;.  |  [optional] |
|**contractRef** | **String** | A reference to a contract. If no specific contract is used, a default MAY be chosen by the implementer.  |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**joiningMemberAccount** | **String** | The account of the B-side member joining the virtual circuit.  |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of the account responsible for managing the service via the API. A manager can read and update the state of entities.  |  [optional] |
|**productOffering** | **String** |  |  [optional] |
|**purchaseOrder** | **String** | Purchase Order ID which will be displayed on the invoice.  |  [optional] |
|**type** | **String** |  |  |
|**name** | **String** | Name of the multi-point to multi-point virtual circuit. |  [optional] |
|**_public** | **Boolean** | A public mp2mp network service can be joined by everyone on the exchange unless denied by a member-joining-rule.  Public network services are visible to other members of the IXP, however only &#x60;name&#x60;, &#x60;type&#x60;, &#x60;product_offering&#x60;, &#x60;consuming_account&#x60; and &#x60;managing_account&#x60; are made available.  Other required fields are redacted. |  [optional] |
|**capacity** | **Integer** | The capacity of the service in Mbps. When null, the maximum capacity will be used. |  [optional] |
|**cloudKey** | **String** |  |  [optional] |



