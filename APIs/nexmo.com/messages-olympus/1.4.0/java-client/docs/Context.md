

# Context

This is only present for the Inbound Message where the user is quoting another message, or for a `product` message where the user has selected the 'Message Business'  option. It provides information about the quoted message and/or the product message being responded to.  

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageFrom** | **String** | The phone number of the **original sender** of the message being quoted in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Not present in a &#x60;context&#x60; object which is the result of a user selecting &#39;Message Business&#39; in a &#x60;product&#x60; message. |  |
|**messageUuid** | **String** | The UUID of the message being quoted. Not present in a &#x60;context&#x60; object which is the result of a user selecting &#39;Message Business&#39; in a &#x60;product&#x60; message. |  |
|**whatsappReferredProduct** | [**ContextWhatsappReferredProduct**](ContextWhatsappReferredProduct.md) |  |  [optional] |



