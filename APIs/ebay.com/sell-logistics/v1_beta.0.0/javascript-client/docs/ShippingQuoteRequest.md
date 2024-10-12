# LogisticsApi.ShippingQuoteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**[Order]**](Order.md) | A seller-defined list that contains information about the orders in the package. This allows sellers to include information about the line items in the package with the shipment information.  &lt;br&gt;&lt;br&gt;A package can contain any number of line items from one or more orders, providing they all ship in the same package.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Maximum list size:&lt;/b&gt; 10 | [optional] 
**packageSpecification** | [**PackageSpecification**](PackageSpecification.md) |  | [optional] 
**shipFrom** | [**Contact**](Contact.md) |  | [optional] 
**shipTo** | [**Contact**](Contact.md) |  | [optional] 


