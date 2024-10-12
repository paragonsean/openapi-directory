

# SigningBasketResponse200

Body of the JSON response for a successful get signing basket request.    * 'payments': payment initiations which shall be authorised through this signing basket.   * 'consents': consent objects which shall be authorised through this signing basket.   * 'transactionStatus': Only the codes RCVD, ACTC, RJCT are used.   * '_links': The ASPSP might integrate hyperlinks to indicate next (authorisation) steps to be taken. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**LinksSigningBasket**](LinksSigningBasket.md) |  |  [optional] |
|**consents** | **List&lt;String&gt;** | A list of consentIds. |  [optional] |
|**payments** | **List&lt;String&gt;** | A list of paymentIds. |  [optional] |
|**transactionStatus** | **TransactionStatusSBS** |  |  |



