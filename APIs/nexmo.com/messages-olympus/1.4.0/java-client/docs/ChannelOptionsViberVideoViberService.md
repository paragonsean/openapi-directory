

# ChannelOptionsViberVideoViberService


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The use of different category tags enables the business to send messages for different use cases. For Viber Business Messages the first message sent from a business to a user must be personal, informative &amp; a targeted message - not promotional. By default Vonage sends the &#x60;transaction&#x60; category to Viber Business Messages. |  [optional] |
|**duration** | **String** | The duration of the video in seconds. |  [optional] |
|**fileSize** | **String** | The file size of the video in MB. |  [optional] |
|**ttl** | **Integer** | Set the time-to-live of message to be delivered in seconds. i.e. if the message is not delivered in 600 seconds then delete the message. |  [optional] |
|**type** | **String** | Viber-specific type definition. To use \&quot;template\&quot;, please contact your Vonage Account Manager to setup your templates. To find out more please visit the [product page](https://www.vonage.com/communications-apis/messages/) |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| TRANSACTION | &quot;transaction&quot; |
| PROMOTION | &quot;promotion&quot; |



