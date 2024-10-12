

# Freight


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ETA** | **OffsetDateTime** | Estimated time of arrival |  [optional] |
|**additionalInfo** | **String** | Aditional information for the courier |  |
|**chargedAmount** | **Integer** | Shipment cost. Must be informed in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. Same as $1,2345.67 must be informed solely as 1234567 |  |
|**crossDockingTime** | **Integer** | Time it will take to manufacture, prepare or setup this product. Time must be provided in seconds. For example 1 day should be informed as 86400. This time will be included in the product ETA informed to the customer |  |
|**defaultAmount** | **Integer** | Default value of this shippment. |  |
|**scheduledPeriod** | **String** | Scheduled period |  [optional] |
|**transitTime** | **Integer** | Deliver time in seconds. Time must be provided in seconds. For example 1 day should be informed as 86400. This time will be included in the product ETA informed to the customer |  |
|**type** | **String** | Freight type |  [optional] |



