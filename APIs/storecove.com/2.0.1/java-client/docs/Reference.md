

# Reference

A reference to a document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentId** | **String** | The id of the referenced document. |  [optional] |
|**documentType** | [**DocumentTypeEnum**](#DocumentTypeEnum) | The type of the referenced document. The following types are supported: ++++ &lt;ul&gt;    &lt;li&gt;        &lt;b&gt;purchase_order&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to an order for this document, assigned by the buyer. Note that this often is a key field, since many receivers of invoices will use this field to automatically match the invoice to an order they placed. Many receivers refuse invoices that cannot be automatically matched, in particular government agencies. So it is highly recommended to fill this field whenever possible.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;billing&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a billing document. For instance, credit notes may refer to an invoice they are a credit note for.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;sales_order&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to an order for this document, assigned by the seller.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;buyer_reference&lt;/b&gt; (document level, Invoice, Order)        &lt;p&gt;The buyer&#39;s reference. Used for internal routing by the receiver. For orders, this becomes the customer reference which the receiver of the order should put back in the buyer reference field in the invoice.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;contract&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to a contract or framework agreement that this document relates to.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;despatch_advice&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a despatch advice for this document. In the FatturaPA, this is what will become the DDT.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;originator&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to an originator document for this invoice.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;receipt&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a receipt document for this document.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;project&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a project document for this document.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;quotation&lt;/b&gt; (document level, Order)        &lt;p&gt;A reference to a quotation document for this document.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;payment_url&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A to a payment URL for the invoice.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;item_classification_code&lt;/b&gt; (line level)        &lt;p&gt;A reference to a commodity classification / item classification code for this line.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;item_commodity_code&lt;/b&gt; (line level)        &lt;p&gt;A reference to a commodity classification / commodity code for this line.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_document_reference&lt;/b&gt; (line level)        &lt;p&gt;A reference to another document for this line.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_standard_item_identification&lt;/b&gt; (line level)        &lt;p&gt;A standard item identification.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_sellers_item_identification&lt;/b&gt; (line level)        &lt;p&gt;The seller&#39;s item identification.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_buyers_item_identification&lt;/b&gt; (line level)        &lt;p&gt;The buyer&#39;s item identification.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;item_specification&lt;/b&gt; (line level)        &lt;p&gt;Referece to an item specification document&lt;/p&gt;    &lt;/li&gt;&lt;/ul&gt; ++++  |  |
|**issueDate** | **String** | The issue date of the referenced document. |  [optional] |
|**lineId** | **String** | The line in the referenced document. |  [optional] |



## Enum: DocumentTypeEnum

| Name | Value |
|---- | -----|
| PURCHASE_ORDER | &quot;purchase_order&quot; |
| BUYER_REFERENCE | &quot;buyer_reference&quot; |
| BILLING | &quot;billing&quot; |
| SALES_ORDER | &quot;sales_order&quot; |
| CONTRACT | &quot;contract&quot; |
| DESPATCH_ADVICE | &quot;despatch_advice&quot; |
| ORIGINATOR | &quot;originator&quot; |
| RECEIPT | &quot;receipt&quot; |
| PROJECT | &quot;project&quot; |
| QUOTATION | &quot;quotation&quot; |
| PAYMENT_URL | &quot;payment_url&quot; |
| ITEM_CLASSIFICATION_CODE | &quot;item_classification_code&quot; |
| ITEM_COMMODITY_CODE | &quot;item_commodity_code&quot; |
| LINE_DOCUMENT_REFERENCE | &quot;line_document_reference&quot; |
| LINE_STANDARD_ITEM_IDENTIFICATION | &quot;line_standard_item_identification&quot; |
| LINE_SELLERS_ITEM_IDENTIFICATION | &quot;line_sellers_item_identification&quot; |
| LINE_BUYERS_ITEM_IDENTIFICATION | &quot;line_buyers_item_identification&quot; |
| ITEM_SPECIFICATION | &quot;item_specification&quot; |



