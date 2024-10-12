

# PaymentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | A decimal value in dollars, or relevant currency. digits(9) |  |
|**billing** | [**Address**](Address.md) |  |  [optional] |
|**card** | [**Card**](Card.md) |  |  [optional] |
|**comments** | **String** | alphanumeric (256) |  [optional] |
|**custom** | [**Custom**](Custom.md) |  |  [optional] |
|**customerIp** | **String** | alphanumeric (30) |  [optional] |
|**language** | **String** | characters (3) |  [optional] |
|**orderNumber** | **String** | A unique order number. alphanumeric(30) |  [optional] |
|**paymentMethod** | **String** | One of (card, token, payment_profile, cash, cheque). characters(20) |  |
|**paymentProfile** | [**ProfilePurchase**](ProfilePurchase.md) |  |  [optional] |
|**shipping** | [**Address**](Address.md) |  |  [optional] |
|**termUrl** | **String** | alphanumeric (256) |  [optional] |
|**token** | [**TokenPurchase**](TokenPurchase.md) |  |  [optional] |



