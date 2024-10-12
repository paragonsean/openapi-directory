

# AddShareRequestBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessMode** | [**AccessMode**](AccessMode.md) |  |  [optional] |
|**embed** | **Boolean** | Whether this share can be embedded within a web page. |  [optional] |
|**expiration** | **OffsetDateTime** | Expiration date for the share. If someone attempts to use the share after this date, they will receive an error that the share is not available. |  [optional] |
|**fileDropCreateFolders** | **Boolean** | Only used for **receive** shares. If true, uploads will be automatically placed into sub-folders of the folder, named after the chosen field on your form.  |  [optional] |
|**hasNotification** | **Boolean** | Whether delivery receipts should be sent. |  [optional] |
|**isPublic** | **Boolean** | Whether someone can visit the share without following a personalized recipient link. |  [optional] |
|**messageBody** | **String** | The message to be included in email invitations for your recipients. Ignored if you have not also provided &#x60;recipients&#x60; and &#x60;messageSubject&#x60; |  [optional] |
|**messageSubject** | **String** | Subject to use on emails inviting recipients to the share. Ignored if you have not also provided &#x60;recipients&#x60; and a &#x60;messageBody&#x60; |  [optional] |
|**name** | **String** | A name for the share. This will be visible on the page that recipients visit.  |  |
|**notificationEmails** | **List&lt;String&gt;** | Emails that will receive delivery receipts for this share. &#x60;hasNotification&#x60; must be **true** for delivery receipts will be sent. |  [optional] |
|**password** | **String** | Set a password for recipients to access the share. All recipients will use the same password. |  [optional] |
|**recipients** | [**List&lt;AddShareRequestBodyRecipientsInner&gt;**](AddShareRequestBodyRecipientsInner.md) | People you want to invite to the share. **Note**: unless you also set the &#x60;messageSubject&#x60; and &#x60;messageBody&#x60; for the new share, invitation emails will not be sent to these recipients. |  [optional] |
|**requireEmail** | **Boolean** | True if recipients must provide their email to view the share. |  [optional] |
|**resources** | **List&lt;String&gt;** | Array of resources for this share. See details on [how to specify resources](#section/Identifying-Resources) above.  **shared_folder** and **receive** shares must have only one &#x60;resource&#x60;, which is a directory that does not have a current share attached.  **send** shares may have multiple &#x60;resource&#x60; parameters. You can also leave this parameter null if you are planning to upload files to the send. If you are planning to upload files to the send that are not yet in your account, you will also need to call the [POST /shares/complete-send/{id}](#operation/completeDirectSend) endpoint to finish the send operation.  |  [optional] |
|**sendingLocalFiles** | **Boolean** | Use this only for **send** shares. Flag to indicate that you are going to upload additional files from your computer to the share. If this is **true**, you will also need to use the [POST /shares/complete-send/{id}](#operation/completeDirectSend) call to finish setting up your share after the files are uploaded. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of share to create. See above for a description of each. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SHARED_FOLDER | &quot;shared_folder&quot; |
| RECEIVE | &quot;receive&quot; |
| SEND | &quot;send&quot; |



