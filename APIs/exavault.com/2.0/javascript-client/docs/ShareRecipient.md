# ExaVault.ShareRecipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | Timestamp of adding recipient to the share. | [optional] 
**email** | **String** | Recipient email address. | [optional] 
**hash** | **String** | Share hash. | [optional] 
**id** | **Number** | ID of the recipient. | [optional] 
**received** | **Boolean** | Set to true if recipient has accessed the share. Note this is set to true when the recipient clicks the link to access the share; not when they download a file. | [optional] 
**sent** | **Boolean** | Set to true if invite email was sent; false otherwise. | [optional] 
**shareId** | **String** | ID of the share that the recipoient belongs to. | [optional] 
**type** | **String** | Type of the recipient. | [optional] 



## Enum: TypeEnum


* `owner` (value: `"owner"`)

* `direct` (value: `"direct"`)




