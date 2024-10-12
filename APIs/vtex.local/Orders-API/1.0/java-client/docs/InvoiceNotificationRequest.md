

# InvoiceNotificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**courier** | **String** | The name of the carrier responsible for delivering the order. *This field should only be used when sending the **tracking** information. When the request is used for sending the invoice, this field should be left empty (&#x60;\&quot;\&quot;&#x60;).* |  [optional] |
|**dispatchedDate** | **String** | Order dispatch date. May be &#x60;null&#x60;. |  [optional] |
|**embeddedInvoice** | **String** | XML text of the invoice, not the URL. This field is very important for external marketplace integrations such as Mercado Libre. |  [optional] |
|**invoiceKey** | **String** |  |  [optional] |
|**invoiceNumber** | **String** | Number that identifies the invoice. |  |
|**invoiceUrl** | **String** | URL of the invoice. Can be used to send the URL of an XML file, for example, which is useful for some integrations. |  [optional] |
|**invoiceValue** | **String** | Total amount being invoiced in cents. Do not use any decimal separator. For instance, &#x60;$24.99&#x60; should be represented as &#x60;2499&#x60;. |  |
|**issuanceDate** | **String** | Issuance date of the invoice. You must add date and time in this field. |  |
|**items** | [**List&lt;Item1&gt;**](Item1.md) | Array containing the SKUs that are being invoiced. |  |
|**trackingNumber** | **String** | The number code that identifies the order tracking. *This field should only be used when sending the **tracking** information. When the request is used for sending the invoice, this field should be left empty (&#x60;\&quot;\&quot;&#x60;).* |  [optional] |
|**trackingUrl** | **String** | The URL used to track the order. *This field should only be used when sending the **tracking** information. When the request is used for sending the invoice, this field should be left empty (&#x60;\&quot;\&quot;&#x60;).* |  [optional] |
|**type** | **String** | The type of invoice. There are two possible values: **Output** and **Input**. The Output type should be used when the invoice you are sending is a selling invoice. The Input type should be used when you send a return invoice. |  |



