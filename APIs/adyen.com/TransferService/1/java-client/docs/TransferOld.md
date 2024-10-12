

# TransferOld


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**Amount**](Amount.md) | The amount of the transfer. |  |
|**description** | **String** | A human-readable description for the transfer. You can use alphanumeric characters and hyphens. We recommend sending a maximum of 140 characters, otherwise the description will be truncated in the webhooks that you receive about the transfer. |  [optional] |
|**destination** | [**PartyIdentification**](PartyIdentification.md) | Contains information about the resource to which funds will be transferred. |  |
|**id** | **String** | Unique identifier of the transfer. |  |
|**reference** | **String** | Your unique reference for the transfer. You can use alphanumeric characters and hyphens. Maximum length: 80 characters. |  [optional] |
|**refusalReason** | **String** | Additional information about the result of the transfer request. |  [optional] |
|**resultCode** | **String** | The result of the transfer request.   Possible values: **Authorised**, **Refused**. |  |
|**source** | [**InternalPartyIdentification**](InternalPartyIdentification.md) | Contains information about the resource from which funds will be taken. |  |



