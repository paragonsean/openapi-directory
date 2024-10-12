# AuthorizedBuyersMarketplaceApi.ClientUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **String** | Required. The client user&#39;s email address that has to be unique across all users for the same client. | [optional] 
**name** | **String** | Output only. The resource name of the client user. Format: &#x60;buyers/{accountId}/clients/{clientAccountId}/users/{userId}&#x60; | [optional] [readonly] 
**state** | **String** | Output only. The state of the client user. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INVITED` (value: `"INVITED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)




