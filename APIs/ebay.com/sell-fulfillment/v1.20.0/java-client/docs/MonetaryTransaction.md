

# MonetaryTransaction

This type is used to provide details about one or more monetary transactions that occur as part of a payment dispute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**DisputeAmount**](DisputeAmount.md) |  |  [optional] |
|**date** | **String** | This timestamp indicates when the monetary transaction occurred. A date is returned for all monetary transactions.&lt;br&gt;&lt;br&gt; The following format is used: &lt;code&gt;YYYY-MM-DDTHH:MM:SS.SSSZ&lt;/code&gt;. For example, &lt;code&gt;2015-08-04T19:09:02.768Z&lt;/code&gt;. |  [optional] |
|**reason** | **String** | This enumeration value indicates the reason for the monetary transaction. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/fulfillment/types/api:MonetaryTransactionReasonEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |
|**type** | **String** | This enumeration value indicates whether the monetary transaction is a charge or a credit to the seller. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/fulfillment/types/api:MonetaryTransactionTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |



