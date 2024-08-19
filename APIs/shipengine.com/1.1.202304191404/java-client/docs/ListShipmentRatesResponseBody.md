

# ListShipmentRatesResponseBody

A list shipment rates response body

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | When the rate was created |  |
|**errors** | [**List&lt;Error&gt;**](Error.md) |  |  |
|**invalidRates** | [**List&lt;Rate&gt;**](Rate.md) | An array of invalid shipment rates |  [readonly] |
|**rateRequestId** | **String** | A string that uniquely identifies the rate request |  [readonly] |
|**rates** | [**List&lt;Rate&gt;**](Rate.md) | An array of shipment rates |  [readonly] |
|**shipmentId** | **String** | A string that uniquely identifies the shipment |  [readonly] |
|**status** | **RateResponseStatus** |  |  [readonly] |



