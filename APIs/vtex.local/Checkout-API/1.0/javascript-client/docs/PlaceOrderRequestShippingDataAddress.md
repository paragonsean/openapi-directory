# CheckoutApi.PlaceOrderRequestShippingDataAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressId** | **String** | Address ID. | [optional] [default to &#39;Home&#39;]
**addressType** | **String** | Type of address. For example, &#x60;Residential&#x60; or &#x60;Pickup&#x60;, among others. | [optional] 
**city** | **String** | City of the shipping address. | [optional] [default to &#39;Rio de Janeiro&#39;]
**complement** | **String** | Complement to the shipping address in case it applies. | [optional] [default to &#39;3rd floor&#39;]
**country** | **String** | Three letter ISO code of the country of the shipping address. | [optional] [default to &#39;BRA&#39;]
**geoCoordinates** | **[Number]** | Array containing two floats with geocoordinates, first longitude, then latitude. | [optional] 
**neighborhood** | **String** | Neighborhood of the shipping address. | [optional] [default to &#39;Botafogo&#39;]
**number** | **String** | Number of the building, house or apartment in the shipping address. | [optional] [default to &#39;300&#39;]
**postalCode** | **String** | Postal Code. | [optional] [default to &#39;12345-000&#39;]
**receiverName** | **String** | Name of the person who is going to receive the order. | [optional] [default to &#39;receiver-name&#39;]
**reference** | **String** | Complement that might help locate the shipping address more precisely in case of delivery. | [optional] [default to &#39;Grey building&#39;]
**state** | **String** | State of the shipping address. | [optional] [default to &#39;Rio de Janeiro&#39;]
**street** | **String** | Street of the shipping address. | [optional] [default to &#39;Praia de Botafogo&#39;]


