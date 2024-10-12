# ExaVault.WebhookV2EventDataShareInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessDescription** | **String** | Human readable description of what visitors are allowed to do with the receive folder | [optional] 
**accessMode** | [**AccessMode**](AccessMode.md) |  | [optional] 
**assets** | **[String]** | List of items included in the share | [optional] 
**created** | **Date** | Date and ti | [optional] 
**embed** | **Boolean** | Whether the receive folder can be embedded within a web page | [optional] 
**expiration** | **String** | Date and time when the receive folder will no longer be  | [optional] 
**expired** | **Boolean** | Whether access to the receive folder has expired | [optional] 
**fileDropCreateFolders** | **Boolean** | Whether files should be automatically placed in subfolders of the receive folder | [optional] 
**formId** | **Number** | ID of the associated form | [optional] 
**hasNotification** | **Boolean** | Whether delivery receipts are enabled for this share | [optional] 
**hasPassword** | **Boolean** | Whether the receive folder requires visitors to enter a password | [optional] 
**hash** | **String** | Hash value of the receive | [optional] 
**id** | **Number** | Unique ID of associated receive folder | [optional] 
**inherited** | **Boolean** | Whether this share is inherited from a parent fol | [optional] 
**isPublic** | **Boolean** | Whether visitors can acccess the receive folder without an invitation link | [optional] 
**messages** | [**[ShareMessage]**](ShareMessage.md) | Invitation messages sent for receive folder | [optional] 
**modified** | **Date** | Date and time when the share was last changed | [optional] 
**name** | **String** | Name of receiv | [optional] 
**ownerHash** | **String** | Hash value of the user who \&quot;owns\&quot; the receive fo | [optional] 
**paths** | **[String]** | List | [optional] 
**recipients** | [**[ShareRecipient]**](ShareRecipient.md) | List of recipients invited  to the receive folder | [optional] 
**requireEmail** | **Boolean** | Whether visitors must enter their email addresses to access the receive folder | [optional] 
**resent** | **Boolean** | Whether invitations to the receive folder have been re-sent to recipients | [optional] 
**status** | **Number** | 1 if share is active. 0 if not. | [optional] 
**trackingStatus** | **String** | Status of invitations sent for this receive folder | [optional] 
**type** | **String** | Type of share **\&quot;receive\&quot;** | [optional] 


