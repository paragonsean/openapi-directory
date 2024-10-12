

# SendChannelMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The content of the message. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of message, &lt;code&gt;STANDARD&lt;/code&gt; or &lt;code&gt;CONTROL&lt;/code&gt;. |  |
|**persistence** | [**PersistenceEnum**](#PersistenceEnum) | Boolean that controls whether the message is persisted on the back end. Required. |  |
|**metadata** | **String** | The optional metadata for each message. |  [optional] |
|**clientRequestToken** | **String** | The &lt;code&gt;Idempotency&lt;/code&gt; token for each client request. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;STANDARD&quot; |
| CONTROL | &quot;CONTROL&quot; |



## Enum: PersistenceEnum

| Name | Value |
|---- | -----|
| PERSISTENT | &quot;PERSISTENT&quot; |
| NON_PERSISTENT | &quot;NON_PERSISTENT&quot; |



