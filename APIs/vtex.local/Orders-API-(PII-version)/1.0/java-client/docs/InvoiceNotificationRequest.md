

# InvoiceNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cfop** | **String** | Fiscal code used in Brazil. |  [optional] |
|**courier** | **String** | The name of the carrier responsible for delivering the order.  &gt; This field should only be used when sending **tracking** information. When the request is used for sending the invoice, this field should be left empty (&#x60;\&quot;\&quot;&#x60;). |  [optional] |
|**extraValue** | **Integer** | Extra value in the invoice in cents. Do not use any decimal separator. For instance, &#x60;$24.99&#x60; should be represented as &#x60;2499&#x60;. |  [optional] |
|**invoiceKey** | **String** | Invoice key. |  [optional] |
|**invoiceNumber** | **String** | Number that identifies the invoice. |  |
|**invoiceUrl** | **String** | URL of the invoice. Can be used to send the URL of an XML file, for example, which is useful for some integrations. |  [optional] |
|**invoiceValue** | **String** | Total amount being invoiced in cents. Do not use any decimal separator. For instance, &#x60;$24.99&#x60; should be represented as &#x60;2499&#x60;. |  |
|**issuedDate** | **String** | Issuance date of the invoice in ISO format. |  |
|**items** | [**List&lt;Item1&gt;**](Item1.md) | Array containing the SKUs that are being invoiced. |  |
|**trackingNumber** | **String** | Code that identifies the order tracking.  &gt; This field should only be used when sending the **tracking** information. When the request is used for sending the invoice, this field should be left empty (&#x60;\&quot;\&quot;&#x60;). |  [optional] |
|**trackingUrl** | **String** | URL used to track the order.  &gt; This field should only be used when sending the **tracking** information. When the request is used for sending the invoice, this field should be left empty (&#x60;\&quot;\&quot;&#x60;). |  [optional] |
|**type** | **String** | The type of invoice. There are two possible values: &#x60;\&quot;Output\&quot;&#x60; and &#x60;\&quot;Input\&quot;&#x60;. The &#x60;\&quot;Output\&quot;&#x60; type should be used when the invoice you are sending is a selling invoice. The &#x60;\&quot;Input\&quot;&#x60; type should be used when you send a return invoice. |  |
|**volumes** | **Integer** | Number of volumes in the invoice. |  [optional] |



