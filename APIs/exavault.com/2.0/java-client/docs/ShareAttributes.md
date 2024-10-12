

# ShareAttributes

Attributes of the share including the name, path and share recipients. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessDescription** | **String** | Description of the share access rights. |  [optional] |
|**accessMode** | [**AccessMode**](AccessMode.md) |  |  [optional] |
|**created** | **OffsetDateTime** | Timestamp of share creation. |  [optional] |
|**embed** | **Boolean** | True if share can be embedded. |  [optional] |
|**expiration** | **String** | Expiration date of the share. |  [optional] |
|**expired** | **Boolean** | True if the share has expired. |  [optional] |
|**fileDropCreateFolders** | **Boolean** | Flag to show if separate folders should be created for each file upload to receive folder. |  [optional] |
|**formId** | **Integer** | ID of the form. |  [optional] |
|**hasNotification** | **Boolean** | True if share has notification. |  [optional] |
|**hasPassword** | **Boolean** | True if the share has password. |  [optional] |
|**hash** | **String** | Share hash. |  [optional] |
|**inherited** | **Boolean** | True if share inherited from parent folder. |  [optional] |
|**messages** | [**List&lt;ShareMessage&gt;**](ShareMessage.md) | Array of invitation messages. |  [optional] |
|**modified** | **OffsetDateTime** | Timestamp of share modification. Can be &#x60;null&#x60; if it wasn&#39;t modified. |  [optional] |
|**name** | **String** | Share name. |  [optional] |
|**ownerHash** | **String** | Share owner&#39;s hash. |  [optional] |
|**paths** | **List&lt;String&gt;** | Path to the shared resource in your account. |  [optional] |
|**_public** | **Boolean** | True if the share has a public url. |  [optional] |
|**recipients** | [**List&lt;ShareRecipient&gt;**](ShareRecipient.md) | Array of recipients. |  [optional] |
|**requireEmail** | **Boolean** | True if share requires email to access. |  [optional] |
|**resent** | **OffsetDateTime** | Invitations resent date. Can be &#x60;null&#x60; if resent never happened. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Share activity status. Can be active (1) or deactivated (0). |  [optional] |
|**trackingStatus** | [**TrackingStatusEnum**](#TrackingStatusEnum) | Checks recipient received status and returns whether it&#39;s been received (&#x60;complete&#x60;,) partial received (&#x60;incomplete&#x60;,) or not received yet (&#x60;pending&#x60;.) |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of share. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



## Enum: TrackingStatusEnum

| Name | Value |
|---- | -----|
| COMPLETE | &quot;complete&quot; |
| INCOMPLETE | &quot;incomplete&quot; |
| PENDING | &quot;pending&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SHARED_FOLDER | &quot;shared_folder&quot; |
| SEND | &quot;send&quot; |
| RECEIVE | &quot;receive&quot; |



