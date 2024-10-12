

# MediaRequestInfo

Extra information added to operations that support Scotty media requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentBytes** | **String** | The number of current bytes uploaded or downloaded. |  [optional] |
|**customData** | **String** | Data to be copied to backend requests. Custom data is returned to Scotty in the agent_state field, which Scotty will then provide in subsequent upload notifications. |  [optional] |
|**diffObjectVersion** | **String** | Set if the http request info is diff encoded. The value of this field is the version number of the base revision. This is corresponding to Apiary&#39;s mediaDiffObjectVersion (//depot/google3/java/com/google/api/server/media/variable/DiffObjectVersionVariable.java). See go/esf-scotty-diff-upload for more information. |  [optional] |
|**finalStatus** | **Integer** | The existence of the final_status field indicates that this is the last call to the agent for this request_id. http://google3/uploader/agent/scotty_agent.proto?l&#x3D;737&amp;rcl&#x3D;347601929 |  [optional] |
|**notificationType** | [**NotificationTypeEnum**](#NotificationTypeEnum) | The type of notification received from Scotty. |  [optional] |
|**requestId** | **String** | The Scotty request ID. |  [optional] |
|**totalBytes** | **String** | The total size of the file. |  [optional] |
|**totalBytesIsEstimated** | **Boolean** | Whether the total bytes field contains an estimated data. |  [optional] |



## Enum: NotificationTypeEnum

| Name | Value |
|---- | -----|
| START | &quot;START&quot; |
| PROGRESS | &quot;PROGRESS&quot; |
| END | &quot;END&quot; |
| RESPONSE_SENT | &quot;RESPONSE_SENT&quot; |
| ERROR | &quot;ERROR&quot; |



