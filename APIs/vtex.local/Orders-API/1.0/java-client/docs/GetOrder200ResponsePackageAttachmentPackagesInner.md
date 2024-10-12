

# GetOrder200ResponsePackageAttachmentPackagesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cfop** | **String** | Fiscal operation code. |  [optional] |
|**courier** | **String** | The name of the carrier responsible for delivering the order. |  [optional] |
|**courierStatus** | **String** | Courier status. |  [optional] |
|**embeddedInvoice** | **String** | Embedded voice in XML. |  [optional] |
|**invoiceKey** | **String** | Invoice key. |  [optional] |
|**invoiceNumber** | **String** | Number that identifies the invoice. |  [optional] |
|**invoiceUrl** | **String** | Invoice URL. |  [optional] |
|**invoiceValue** | **Integer** | Invoice value in cents. |  [optional] |
|**issuanceDate** | **String** | Issuance date. |  [optional] |
|**items** | [**List&lt;GetOrder200ResponsePackageAttachmentPackagesInnerItemsInner&gt;**](GetOrder200ResponsePackageAttachmentPackagesInnerItemsInner.md) | Information on each item in the package. |  [optional] |
|**restitutions** | [**GetOrder200ResponsePackageAttachmentPackagesInnerRestitutions**](GetOrder200ResponsePackageAttachmentPackagesInnerRestitutions.md) |  |  [optional] |
|**trackingNumber** | **String** | The number code that identifies the order tracking. *This field should only be used when sending the **tracking** information. When the request is used for sending the invoice, this field should be left empty (&#x60;\&quot;\&quot;&#x60;).* |  [optional] |
|**trackingUrl** | **String** | Tracking URL. |  [optional] |
|**type** | **String** | Invoice type &#x60;Output&#x60; for sales and &#x60;Input&#x60; for returns. |  [optional] |
|**volumes** | **Integer** | Quantity of packages involved in the order. |  [optional] |



