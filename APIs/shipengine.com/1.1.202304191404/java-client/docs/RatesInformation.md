

# RatesInformation

A rates information resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | When the rate was created |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) |  |  [optional] |
|**invalidRates** | [**List&lt;Rate&gt;**](Rate.md) | An array of invalid shipment rates |  [optional] [readonly] |
|**rateRequestId** | **String** | A string that uniquely identifies the rate request |  [optional] [readonly] |
|**rates** | [**List&lt;Rate&gt;**](Rate.md) | An array of shipment rates |  [optional] [readonly] |
|**shipmentId** | **String** | A string that uniquely identifies the shipment |  [optional] [readonly] |
|**status** | **RateResponseStatus** |  |  [optional] [readonly] |



