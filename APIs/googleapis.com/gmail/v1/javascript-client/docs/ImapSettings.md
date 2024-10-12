# GmailApi.ImapSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoExpunge** | **Boolean** | If this value is true, Gmail will immediately expunge a message when it is marked as deleted in IMAP. Otherwise, Gmail will wait for an update from the client before expunging messages marked as deleted. | [optional] 
**enabled** | **Boolean** | Whether IMAP is enabled for the account. | [optional] 
**expungeBehavior** | **String** | The action that will be executed on a message when it is marked as deleted and expunged from the last visible IMAP folder. | [optional] 
**maxFolderSize** | **Number** | An optional limit on the number of messages that an IMAP folder may contain. Legal values are 0, 1000, 2000, 5000 or 10000. A value of zero is interpreted to mean that there is no limit. | [optional] 



## Enum: ExpungeBehaviorEnum


* `expungeBehaviorUnspecified` (value: `"expungeBehaviorUnspecified"`)

* `archive` (value: `"archive"`)

* `trash` (value: `"trash"`)

* `deleteForever` (value: `"deleteForever"`)




