

# ClientUser

A user of a client who has restricted access to the Marketplace and certain other sections of the Authorized Buyers UI based on the role granted to the associated client.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Required. The client user&#39;s email address that has to be unique across all users for the same client. |  [optional] |
|**name** | **String** | Output only. The resource name of the client user. Format: &#x60;buyers/{accountId}/clients/{clientAccountId}/users/{userId}&#x60; |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the client user. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INVITED | &quot;INVITED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



