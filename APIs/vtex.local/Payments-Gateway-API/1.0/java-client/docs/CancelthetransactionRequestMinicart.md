

# CancelthetransactionRequestMinicart

This field is filled with the content of the cart of the transaction, which can be obtained using [Get Orders](https://developers.vtex.com/vtex-rest-api/reference/orders#getorder) or [Transaction Details](https://developers.vtex.com/vtex-rest-api/reference/transaction-process#transactiondetails) endpoints. It should only be included for transactions with split payment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**freight** | **Integer** |  |  [optional] |
|**items** | **List&lt;Object&gt;** |  |  [optional] |
|**tax** | **Integer** |  |  [optional] |



