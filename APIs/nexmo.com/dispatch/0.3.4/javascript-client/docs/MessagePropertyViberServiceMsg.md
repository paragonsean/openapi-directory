# DispatchApi.MessagePropertyViberServiceMsg

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The use of different category tags enables the business to send messages for different use cases. For Viber Business Messages the first message sent from a business to a user must be personal, informative and a targeted message - not promotional. By default Vonage sends the &#x60;transaction&#x60; category to Viber Business Messages. | [optional] 
**ttl** | **Number** | Only valid for Viber Business Messages. Set the time-to-live of message to be delivered in seconds. i.e. if the message is not delivered in 600 seconds then delete the message. | [optional] 



## Enum: CategoryEnum


* `transaction` (value: `"transaction"`)

* `promotion` (value: `"promotion"`)




