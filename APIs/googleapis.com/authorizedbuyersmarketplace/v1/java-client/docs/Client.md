

# Client

A client represents an agency, a brand, or an advertiser customer of the buyer. Based on the client's role, its client users will have varying levels of restricted access to the Marketplace and certain other sections of the Authorized Buyers UI.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Required. Display name shown to publishers. Must be unique for clients without partnerClientId specified. Maximum length of 255 characters is allowed. |  [optional] |
|**name** | **String** | Output only. The resource name of the client. Format: &#x60;buyers/{accountId}/clients/{clientAccountId}&#x60; |  [optional] [readonly] |
|**partnerClientId** | **String** | Arbitrary unique identifier provided by the buyer. This field can be used to associate a client with an identifier in the namespace of the buyer, lookup clients by that identifier and verify whether an Authorized Buyers account of the client already exists. If present, must be unique across all the clients. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Required. The role assigned to the client. Each role implies a set of permissions granted to the client. |  [optional] |
|**sellerVisible** | **Boolean** | Whether the client will be visible to sellers. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the client. |  [optional] [readonly] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;CLIENT_ROLE_UNSPECIFIED&quot; |
| DEAL_VIEWER | &quot;CLIENT_DEAL_VIEWER&quot; |
| DEAL_NEGOTIATOR | &quot;CLIENT_DEAL_NEGOTIATOR&quot; |
| DEAL_APPROVER | &quot;CLIENT_DEAL_APPROVER&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



