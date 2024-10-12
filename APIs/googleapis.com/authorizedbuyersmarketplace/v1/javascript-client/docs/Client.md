# AuthorizedBuyersMarketplaceApi.Client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Required. Display name shown to publishers. Must be unique for clients without partnerClientId specified. Maximum length of 255 characters is allowed. | [optional] 
**name** | **String** | Output only. The resource name of the client. Format: &#x60;buyers/{accountId}/clients/{clientAccountId}&#x60; | [optional] [readonly] 
**partnerClientId** | **String** | Arbitrary unique identifier provided by the buyer. This field can be used to associate a client with an identifier in the namespace of the buyer, lookup clients by that identifier and verify whether an Authorized Buyers account of the client already exists. If present, must be unique across all the clients. | [optional] 
**role** | **String** | Required. The role assigned to the client. Each role implies a set of permissions granted to the client. | [optional] 
**sellerVisible** | **Boolean** | Whether the client will be visible to sellers. | [optional] 
**state** | **String** | Output only. The state of the client. | [optional] [readonly] 



## Enum: RoleEnum


* `ROLE_UNSPECIFIED` (value: `"CLIENT_ROLE_UNSPECIFIED"`)

* `DEAL_VIEWER` (value: `"CLIENT_DEAL_VIEWER"`)

* `DEAL_NEGOTIATOR` (value: `"CLIENT_DEAL_NEGOTIATOR"`)

* `DEAL_APPROVER` (value: `"CLIENT_DEAL_APPROVER"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)




