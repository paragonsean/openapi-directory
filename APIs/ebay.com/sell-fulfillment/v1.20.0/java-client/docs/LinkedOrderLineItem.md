

# LinkedOrderLineItem

This type contains data on a line item that is related to, but not a part of the order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lineItemAspects** | [**List&lt;NameValuePair&gt;**](NameValuePair.md) | This array contains the complete set of items aspects for the linked line item. For example:&lt;br&gt;&lt;pre&gt;\&quot;lineItemAspects\&quot;: [&lt;br&gt;    {&lt;br&gt;        \&quot;name\&quot;: \&quot;Tire Type\&quot;,&lt;br&gt;        \&quot;value\&quot;: \&quot;All Season\&quot;&lt;br&gt;    },&lt;br&gt;&lt;br&gt;    ...&lt;br&gt; &lt;br&gt;    {&lt;br&gt;        \&quot;name\&quot;: \&quot;Car Type\&quot;,&lt;br&gt;        \&quot;value\&quot;: \&quot;Performance\&quot;&lt;br&gt;    }&lt;br&gt;]&lt;/pre&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;strong&gt;Note:&lt;/strong&gt; All item specifics for the listing are returned. The name/value pairs returned are in the language of the linked line item&#39;s listing site, which may vary from the seller&#39;s language.&lt;/span&gt; |  [optional] |
|**lineItemId** | **String** | The unique identifier of the linked order line item. |  [optional] |
|**maxEstimatedDeliveryDate** | **String** | The end of the date range in which the linked line item is expected to be delivered to the shipping address. |  [optional] |
|**minEstimatedDeliveryDate** | **String** | The beginning of the date range in which the linked line item is expected to be delivered to the shipping address. |  [optional] |
|**orderId** | **String** | The unique identifier of the order to which the linked line item belongs. |  [optional] |
|**sellerId** | **String** | The eBay user ID of the seller who sold the linked line item. For example, the user ID of the tire seller. |  [optional] |
|**shipments** | [**List&lt;TrackingInfo&gt;**](TrackingInfo.md) | An array containing any shipment tracking information available for the linked line item. |  [optional] |
|**title** | **String** | The listing title of the linked line item. |  [optional] |



