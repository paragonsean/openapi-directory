

# CreateUpdateFreightValuesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absoluteMoneyCost** | **String** | Fixed shipping cost to be charged in a decimal number. |  |
|**country** | **String** | Three letter ISO code for the country where the delivery will take place. |  |
|**maxVolume** | **Integer** | Maximum volume that can be transported by the carrier in cm³. |  |
|**operationType** | **Integer** | Indicates desired action for the object. Possible values are &#x60;1&#x60; (Insert), &#x60;2&#x60; (Update) or &#x60;3&#x60;(Delete). |  |
|**polygon** | **String** | Polygon ID, according to the [geolocation](https://help.vtex.com/en/tutorial/registering-geolocation/) feature. |  |
|**pricePercent** | **Integer** | [Price-based additional shipping charge](https://help.vtex.com/en/tutorial/additional-shipping-costs--2vqGwMn0LabkOHY6zSHYNV), calculated based on the total price of the order, in decimal number. You must fill in this field with a percentage value. For example, for an additional charge of 10%, fill in the table with 10. |  |
|**pricePercentByWeight** | **Integer** | [Weight-based additional shipping charge](https://help.vtex.com/en/tutorial/additional-shipping-costs--2vqGwMn0LabkOHY6zSHYNV), calculated based on the total weight of the order. |  |
|**timeCost** | **String** | Delivery time frame informed by the carrier, in the format DD.HH:MM:SS. |  |
|**weightEnd** | **Integer** | Maximum weight allowed. |  |
|**weightStart** | **Integer** | Minimum weight allowed |  |
|**zipCodeEnd** | **String** | End of postal code interval. |  |
|**zipCodeStart** | **String** | Start of postal code interval. |  |



