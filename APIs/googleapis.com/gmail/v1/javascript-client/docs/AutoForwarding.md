# GmailApi.AutoForwarding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disposition** | **String** | The state that a message should be left in after it has been forwarded. | [optional] 
**emailAddress** | **String** | Email address to which all incoming messages are forwarded. This email address must be a verified member of the forwarding addresses. | [optional] 
**enabled** | **Boolean** | Whether all incoming mail is automatically forwarded to another address. | [optional] 



## Enum: DispositionEnum


* `dispositionUnspecified` (value: `"dispositionUnspecified"`)

* `leaveInInbox` (value: `"leaveInInbox"`)

* `archive` (value: `"archive"`)

* `trash` (value: `"trash"`)

* `markRead` (value: `"markRead"`)




