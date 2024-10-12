# SwaggerApi2Cart.OrderShipmentUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isShipped** | **Boolean** | Defines shipment&#39;s status | [optional] [default to true]
**orderId** | **String** | Defines the order that will be updated | [optional] 
**replace** | **Boolean** | Allows rewrite tracking numbers | [optional] [default to true]
**shipmentId** | **String** | Shipment id indicates the number of delivery | 
**storeId** | **String** | Store Id | [optional] 
**trackingLink** | **String** | Defines custom tracking link | [optional] 
**trackingNumbers** | [**[OrderShipmentAddTrackingNumbersInner]**](OrderShipmentAddTrackingNumbersInner.md) | Defines shipment&#39;s tracking numbers that have to be added&lt;/br&gt; How set tracking numbers to appropriate carrier:&lt;ul&gt;&lt;li&gt;tracking_numbers[]&#x3D;a2c.demo1,a2c.demo2 - set default carrier&lt;/li&gt;&lt;li&gt;tracking_numbers[&lt;b&gt;carrier_id&lt;/b&gt;]&#x3D;a2c.demo - set appropriate carrier&lt;/li&gt;&lt;/ul&gt;To get the list of carriers IDs that are available in your store, use the &lt;a href &#x3D; \&quot;https://api2cart.com/docs/#/cart/CartInfo\&quot;&gt;cart.info&lt;/a &gt; method | [optional] 


