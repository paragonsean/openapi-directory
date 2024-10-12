# StorecoveApi.Reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentId** | **String** | The id of the referenced document. | [optional] 
**documentType** | **String** | The type of the referenced document. The following types are supported: ++++ &lt;ul&gt;    &lt;li&gt;        &lt;b&gt;purchase_order&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to an order for this document, assigned by the buyer. Note that this often is a key field, since many receivers of invoices will use this field to automatically match the invoice to an order they placed. Many receivers refuse invoices that cannot be automatically matched, in particular government agencies. So it is highly recommended to fill this field whenever possible.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;billing&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a billing document. For instance, credit notes may refer to an invoice they are a credit note for.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;sales_order&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to an order for this document, assigned by the seller.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;buyer_reference&lt;/b&gt; (document level, Invoice, Order)        &lt;p&gt;The buyer&#39;s reference. Used for internal routing by the receiver. For orders, this becomes the customer reference which the receiver of the order should put back in the buyer reference field in the invoice.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;contract&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to a contract or framework agreement that this document relates to.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;despatch_advice&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a despatch advice for this document. In the FatturaPA, this is what will become the DDT.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;originator&lt;/b&gt; (document level, Invoice + Order)        &lt;p&gt;A reference to an originator document for this invoice.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;receipt&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a receipt document for this document.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;project&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A reference to a project document for this document.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;quotation&lt;/b&gt; (document level, Order)        &lt;p&gt;A reference to a quotation document for this document.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;payment_url&lt;/b&gt; (document level, Invoice)        &lt;p&gt;A to a payment URL for the invoice.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;item_classification_code&lt;/b&gt; (line level)        &lt;p&gt;A reference to a commodity classification / item classification code for this line.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;item_commodity_code&lt;/b&gt; (line level)        &lt;p&gt;A reference to a commodity classification / commodity code for this line.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_document_reference&lt;/b&gt; (line level)        &lt;p&gt;A reference to another document for this line.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_standard_item_identification&lt;/b&gt; (line level)        &lt;p&gt;A standard item identification.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_sellers_item_identification&lt;/b&gt; (line level)        &lt;p&gt;The seller&#39;s item identification.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;line_buyers_item_identification&lt;/b&gt; (line level)        &lt;p&gt;The buyer&#39;s item identification.&lt;/p&gt;    &lt;/li&gt;    &lt;li&gt;        &lt;b&gt;item_specification&lt;/b&gt; (line level)        &lt;p&gt;Referece to an item specification document&lt;/p&gt;    &lt;/li&gt;&lt;/ul&gt; ++++  | 
**issueDate** | **String** | The issue date of the referenced document. | [optional] 
**lineId** | **String** | The line in the referenced document. | [optional] 



## Enum: DocumentTypeEnum


* `purchase_order` (value: `"purchase_order"`)

* `buyer_reference` (value: `"buyer_reference"`)

* `billing` (value: `"billing"`)

* `sales_order` (value: `"sales_order"`)

* `contract` (value: `"contract"`)

* `despatch_advice` (value: `"despatch_advice"`)

* `originator` (value: `"originator"`)

* `receipt` (value: `"receipt"`)

* `project` (value: `"project"`)

* `quotation` (value: `"quotation"`)

* `payment_url` (value: `"payment_url"`)

* `item_classification_code` (value: `"item_classification_code"`)

* `item_commodity_code` (value: `"item_commodity_code"`)

* `line_document_reference` (value: `"line_document_reference"`)

* `line_standard_item_identification` (value: `"line_standard_item_identification"`)

* `line_sellers_item_identification` (value: `"line_sellers_item_identification"`)

* `line_buyers_item_identification` (value: `"line_buyers_item_identification"`)

* `item_specification` (value: `"item_specification"`)




