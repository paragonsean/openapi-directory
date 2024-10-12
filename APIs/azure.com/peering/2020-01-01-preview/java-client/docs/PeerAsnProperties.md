

# PeerAsnProperties

The properties that define a peer's ASN.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | The error message for the validation state |  [optional] [readonly] |
|**peerAsn** | **Integer** | The Autonomous System Number (ASN) of the peer. |  [optional] |
|**peerContactDetail** | [**List&lt;ContactDetail&gt;**](ContactDetail.md) | The contact details of the peer. |  [optional] |
|**peerName** | **String** | The name of the peer. |  [optional] |
|**validationState** | [**ValidationStateEnum**](#ValidationStateEnum) | The validation state of the ASN associated with the peer. |  [optional] |



## Enum: ValidationStateEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PENDING | &quot;Pending&quot; |
| APPROVED | &quot;Approved&quot; |
| FAILED | &quot;Failed&quot; |



