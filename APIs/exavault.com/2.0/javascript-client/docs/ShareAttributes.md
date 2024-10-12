# ExaVault.ShareAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessDescription** | **String** | Description of the share access rights. | [optional] 
**accessMode** | [**AccessMode**](AccessMode.md) |  | [optional] 
**created** | **Date** | Timestamp of share creation. | [optional] 
**embed** | **Boolean** | True if share can be embedded. | [optional] 
**expiration** | **String** | Expiration date of the share. | [optional] 
**expired** | **Boolean** | True if the share has expired. | [optional] 
**fileDropCreateFolders** | **Boolean** | Flag to show if separate folders should be created for each file upload to receive folder. | [optional] 
**formId** | **Number** | ID of the form. | [optional] 
**hasNotification** | **Boolean** | True if share has notification. | [optional] 
**hasPassword** | **Boolean** | True if the share has password. | [optional] 
**hash** | **String** | Share hash. | [optional] 
**inherited** | **Boolean** | True if share inherited from parent folder. | [optional] 
**messages** | [**[ShareMessage]**](ShareMessage.md) | Array of invitation messages. | [optional] 
**modified** | **Date** | Timestamp of share modification. Can be &#x60;null&#x60; if it wasn&#39;t modified. | [optional] 
**name** | **String** | Share name. | [optional] 
**ownerHash** | **String** | Share owner&#39;s hash. | [optional] 
**paths** | **[String]** | Path to the shared resource in your account. | [optional] 
**_public** | **Boolean** | True if the share has a public url. | [optional] 
**recipients** | [**[ShareRecipient]**](ShareRecipient.md) | Array of recipients. | [optional] 
**requireEmail** | **Boolean** | True if share requires email to access. | [optional] 
**resent** | **Date** | Invitations resent date. Can be &#x60;null&#x60; if resent never happened. | [optional] 
**status** | **Number** | Share activity status. Can be active (1) or deactivated (0). | [optional] 
**trackingStatus** | **String** | Checks recipient received status and returns whether it&#39;s been received (&#x60;complete&#x60;,) partial received (&#x60;incomplete&#x60;,) or not received yet (&#x60;pending&#x60;.) | [optional] 
**type** | **String** | Type of share. | [optional] 



## Enum: StatusEnum


* `0` (value: `0`)

* `1` (value: `1`)





## Enum: TrackingStatusEnum


* `complete` (value: `"complete"`)

* `incomplete` (value: `"incomplete"`)

* `pending` (value: `"pending"`)





## Enum: TypeEnum


* `shared_folder` (value: `"shared_folder"`)

* `send` (value: `"send"`)

* `receive` (value: `"receive"`)




