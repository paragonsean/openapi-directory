

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | ISO-4217 currency code (3-letter alphabetic currency code). |  [optional] |
|**merchantCategoryCode** | **String** | Merchant category of the merchant. Conditional field. When available, it must be included in the response. |  [optional] |
|**merchantCategoryDescription** | **String** | Description of the merchant category. |  [optional] |
|**merchantName** | **String** | Name of the merchant. Conditional field. When available, it must be included in the response. |  [optional] |
|**poSEntryMode** | **String** | Indicates the mode by which transaction data was collected at the merchant. Conditional field. When available, it must be included in the response.  Valid values:&lt;br /&gt;    \&quot;07\&quot; - Contactless M/Chip transaction&lt;br /&gt;    \&quot;09\&quot; - Digital Secure Remote Payment containing EMV data&lt;br /&gt;    \&quot;81\&quot; - Digital Secure Remote Payment containing UCAF data or CoF&lt;br /&gt;    \&quot;82\&quot; - CoF - PAN auto entry via server&lt;br /&gt;    \&quot;90\&quot; - Dynamic Magnetic Strip Data&lt;br /&gt;    \&quot;91\&quot; - Contactless magnetic stripe |  [optional] |
|**transactionAmount** | **String** | Amount of the transaction formatted with decimal places. |  [optional] |
|**transactionDateTime** | **String** | Date and time the comment was updated. String, YYYY-MM-DDThh:mm:ssTZD. |  [optional] |
|**transactionStatusCode** | **String** | Transaction status. Valid values:&lt;br /&gt;    \&quot;AUTH\&quot; &#x3D; Authorized&lt;br /&gt;    \&quot;COMP\&quot; &#x3D; Completed&lt;br /&gt;    \&quot;DCLN\&quot; &#x3D; Declined&lt;br /&gt;    \&quot;PAUTH\&quot; &#x3D; Pre-Authorized&lt;br /&gt;    \&quot;PAUTC\&quot; &#x3D; Pre-Authorization Completed&lt;br /&gt;    \&quot;PAUTD\&quot; &#x3D; Pre-Authorization Declined&lt;br /&gt;    \&quot;REFND\&quot; &#x3D; Refunded |  [optional] |
|**transactionTypeCode** | **String** | Type of transaction. Valid values:&lt;br /&gt;    \&quot;PURCH\&quot; &#x3D; Purchase&lt;br /&gt;    \&quot;PURCB\&quot; &#x3D; Purchase with Cashback&lt;br /&gt;    \&quot;REFND\&quot; &#x3D; Refund&lt;br /&gt;    \&quot;AFD\&quot; &#x3D; Purchase Pre-Auth AFD&lt;br /&gt;    \&quot;CLRRF\&quot; &#x3D; Clearing Refund&lt;br /&gt;    \&quot;NAFD\&quot; &#x3D; Purchase Pre-Auth Non-AFD&lt;br /&gt;    \&quot;PYMT\&quot; &#x3D; Push Payments. |  [optional] |
|**transactionTypeDescription** | **String** | Description of the transaction type. |  [optional] |



