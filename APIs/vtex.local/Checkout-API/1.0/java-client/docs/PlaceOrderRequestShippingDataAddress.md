

# PlaceOrderRequestShippingDataAddress

Shipping address.    For customers already in your data base, it is enough to send this object only with an `addressId`, which you may obtain from a [Cart simulation request](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#cartsimulation), for example.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressId** | **String** | Address ID. |  [optional] |
|**addressType** | **String** | Type of address. For example, &#x60;Residential&#x60; or &#x60;Pickup&#x60;, among others. |  [optional] |
|**city** | **String** | City of the shipping address. |  [optional] |
|**complement** | **String** | Complement to the shipping address in case it applies. |  [optional] |
|**country** | **String** | Three letter ISO code of the country of the shipping address. |  [optional] |
|**geoCoordinates** | **List&lt;BigDecimal&gt;** | Array containing two floats with geocoordinates, first longitude, then latitude. |  [optional] |
|**neighborhood** | **String** | Neighborhood of the shipping address. |  [optional] |
|**number** | **String** | Number of the building, house or apartment in the shipping address. |  [optional] |
|**postalCode** | **String** | Postal Code. |  [optional] |
|**receiverName** | **String** | Name of the person who is going to receive the order. |  [optional] |
|**reference** | **String** | Complement that might help locate the shipping address more precisely in case of delivery. |  [optional] |
|**state** | **String** | State of the shipping address. |  [optional] |
|**street** | **String** | Street of the shipping address. |  [optional] |



