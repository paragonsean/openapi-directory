

# CartSimulationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | Three letter ISO code of the country of the shipping address. This value must be sent along with the &#x60;postalCode&#x60; or &#x60;geoCoordinates&#x60; values. |  [optional] |
|**geoCoordinates** | **List&lt;BigDecimal&gt;** | Array containing two floats with geocoordinates, first longitude, then latitude. |  [optional] |
|**items** | [**List&lt;CartSimulationRequestItemsInner&gt;**](CartSimulationRequestItemsInner.md) | Array containing information about the SKUs inside the cart to be simulated. |  [optional] |
|**postalCode** | **String** | Postal code. |  [optional] |



