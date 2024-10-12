

# SalesDataOrderPaymentInterface

Order payment interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountStatus** | **String** | Account status. |  |
|**additionalData** | **String** | Additional data. |  [optional] |
|**additionalInformation** | **List&lt;String&gt;** | Array of additional information. |  |
|**addressStatus** | **String** | Address status. |  [optional] |
|**amountAuthorized** | **BigDecimal** | Amount authorized. |  [optional] |
|**amountCanceled** | **BigDecimal** | Amount canceled. |  [optional] |
|**amountOrdered** | **BigDecimal** | Amount ordered. |  [optional] |
|**amountPaid** | **BigDecimal** | Amount paid. |  [optional] |
|**amountRefunded** | **BigDecimal** | Amount refunded. |  [optional] |
|**anetTransMethod** | **String** | Anet transaction method. |  [optional] |
|**baseAmountAuthorized** | **BigDecimal** | Base amount authorized. |  [optional] |
|**baseAmountCanceled** | **BigDecimal** | Base amount canceled. |  [optional] |
|**baseAmountOrdered** | **BigDecimal** | Base amount ordered. |  [optional] |
|**baseAmountPaid** | **BigDecimal** | Base amount paid. |  [optional] |
|**baseAmountPaidOnline** | **BigDecimal** | Base amount paid online. |  [optional] |
|**baseAmountRefunded** | **BigDecimal** | Base amount refunded. |  [optional] |
|**baseAmountRefundedOnline** | **BigDecimal** | Base amount refunded online. |  [optional] |
|**baseShippingAmount** | **BigDecimal** | Base shipping amount. |  [optional] |
|**baseShippingCaptured** | **BigDecimal** | Base shipping captured amount. |  [optional] |
|**baseShippingRefunded** | **BigDecimal** | Base shipping refunded amount. |  [optional] |
|**ccApproval** | **String** | Credit card approval. |  [optional] |
|**ccAvsStatus** | **String** | Credit card avs status. |  [optional] |
|**ccCidStatus** | **String** | Credit card CID status. |  [optional] |
|**ccDebugRequestBody** | **String** | Credit card debug request body. |  [optional] |
|**ccDebugResponseBody** | **String** | Credit card debug response body. |  [optional] |
|**ccDebugResponseSerialized** | **String** | Credit card debug response serialized. |  [optional] |
|**ccExpMonth** | **String** | Credit card expiration month. |  [optional] |
|**ccExpYear** | **String** | Credit card expiration year. |  [optional] |
|**ccLast4** | **String** | Last four digits of the credit card. |  |
|**ccNumberEnc** | **String** | Encrypted credit card number. |  [optional] |
|**ccOwner** | **String** | Credit card number. |  [optional] |
|**ccSecureVerify** | **String** | Credit card secure verify. |  [optional] |
|**ccSsIssue** | **String** | Credit card SS issue. |  [optional] |
|**ccSsStartMonth** | **String** | Credit card SS start month. |  [optional] |
|**ccSsStartYear** | **String** | Credit card SS start year. |  [optional] |
|**ccStatus** | **String** | Credit card status. |  [optional] |
|**ccStatusDescription** | **String** | Credit card status description. |  [optional] |
|**ccTransId** | **String** | Credit card transaction ID. |  [optional] |
|**ccType** | **String** | Credit card type. |  [optional] |
|**echeckAccountName** | **String** | eCheck account name. |  [optional] |
|**echeckAccountType** | **String** | eCheck account type. |  [optional] |
|**echeckBankName** | **String** | eCheck bank name. |  [optional] |
|**echeckRoutingNumber** | **String** | eCheck routing number. |  [optional] |
|**echeckType** | **String** | eCheck type. |  [optional] |
|**entityId** | **Integer** | Entity ID. |  [optional] |
|**extensionAttributes** | [**SalesDataOrderPaymentExtensionInterface**](SalesDataOrderPaymentExtensionInterface.md) |  |  [optional] |
|**lastTransId** | **String** | Last transaction ID. |  [optional] |
|**method** | **String** | Method. |  |
|**parentId** | **Integer** | Parent ID. |  [optional] |
|**poNumber** | **String** | PO number. |  [optional] |
|**protectionEligibility** | **String** | Protection eligibility. |  [optional] |
|**quotePaymentId** | **Integer** | Quote payment ID. |  [optional] |
|**shippingAmount** | **BigDecimal** | Shipping amount. |  [optional] |
|**shippingCaptured** | **BigDecimal** | Shipping captured. |  [optional] |
|**shippingRefunded** | **BigDecimal** | Shipping refunded. |  [optional] |



