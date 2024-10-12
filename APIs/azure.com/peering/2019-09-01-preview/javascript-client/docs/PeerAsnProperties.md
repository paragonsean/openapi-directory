# PeeringManagementClient.PeerAsnProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | The error message for the validation state | [optional] [readonly] 
**peerAsn** | **Number** | The Autonomous System Number (ASN) of the peer. | [optional] 
**peerContactInfo** | [**ContactInfo**](ContactInfo.md) |  | [optional] 
**peerName** | **String** | The name of the peer. | [optional] 
**validationState** | **String** | The validation state of the ASN associated with the peer. | [optional] 



## Enum: ValidationStateEnum


* `None` (value: `"None"`)

* `Pending` (value: `"Pending"`)

* `Approved` (value: `"Approved"`)

* `Failed` (value: `"Failed"`)




