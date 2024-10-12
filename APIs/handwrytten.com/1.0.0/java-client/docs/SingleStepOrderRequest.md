

# SingleStepOrderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardId** | **Integer** | the id of the card you want to send |  |
|**creditCardId** | **Integer** | the credit card id to charge for the order.  Currently this is required, even for invoiced accounts, it just won&#39;t be charged. |  [optional] |
|**denominationId** | **Integer** | Optional.  Use if sending a gift card |  [optional] |
|**fontLabel** | **String** | the colloquial name of the font, such as &#39;Fancy Jenna&#39; or &#39;Casual David&#39; |  [optional] |
|**message** | **String** | the full message body.  Use &#39;\\n&#39; for new lines |  |
|**recipientAddress1** | **String** | the first address line of the return address |  [optional] |
|**recipientAddress2** | **String** | the second line of the address, such as suite, apartment, building, etc. Optional |  [optional] |
|**recipientBusinessName** | **String** | the second line of the recipient address.  Optional. |  [optional] |
|**recipientCity** | **String** | the city of the recipient, to appear in the address |  [optional] |
|**recipientCountry** | **String** | the country of the recipient.  Optional and defaults to usa |  [optional] |
|**recipientCountryId** | **Integer** | alternate way to specify country.  Optional and defaults to 1 |  [optional] |
|**recipientName** | **String** | the name on the recipient address |  [optional] |
|**recipientState** | **String** | the ABBREVIATED state or province of the recipient.  This is required for US and Canada addresses and optional for all other countries |  [optional] |
|**recipientZip** | **String** | the zip code or postal code of the recipient |  [optional] |
|**senderAddress1** | **String** | the first address line of the return address |  [optional] |
|**senderAddress2** | **String** | the second line of the address, such as suite, apartment, building, etc. Optional |  [optional] |
|**senderBusinessName** | **String** | the second line of the return address.  Optional. |  [optional] |
|**senderCity** | **String** | the city of the sender, to appear in the return address |  [optional] |
|**senderCountry** | **String** | the country of the recipient.  Optional and defaults to usa |  [optional] |
|**senderCountryId** | **Integer** | alternate way to specify country.  Optional and defaults to 1 |  [optional] |
|**senderName** | **String** | the name on the return address |  [optional] |
|**senderState** | **String** | the ABBREVIATED state or province of the sender.  This is required for US and Canada addresses and optional for all other countries |  [optional] |
|**senderZip** | **String** | The postal code or zip code of the sender. |  [optional] |
|**uid** | **String** | The UID of the logged-in user |  |



