

# LineItemReference

This type identifies the line item and quantity of that line item that comprises one fulfillment, such as a shipping package.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lineItemId** | **String** | This is the unique identifier of the eBay order line item that is part of the shipping fulfillment. The line item ID is created as soon as there is a commitment to buy from the seller. |  [optional] |
|**quantity** | **Integer** | This is the number of lineItems associated with the &lt;a href&#x3D;\&quot;#request.trackingNumber\&quot;&gt;trackingNumber&lt;/a&gt; specified by the seller. This must be a whole number greater than zero (0). |  [optional] |



