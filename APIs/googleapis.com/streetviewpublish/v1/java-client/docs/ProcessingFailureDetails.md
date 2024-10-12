

# ProcessingFailureDetails

Additional details to accompany the ProcessingFailureReason enum. This message is always expected to be used in conjunction with ProcessingFailureReason, and the oneof value set in this message should match the FailureReason.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gpsDataGapDetails** | [**GpsDataGapFailureDetails**](GpsDataGapFailureDetails.md) |  |  [optional] |
|**imuDataGapDetails** | [**ImuDataGapFailureDetails**](ImuDataGapFailureDetails.md) |  |  [optional] |
|**insufficientGpsDetails** | [**InsufficientGpsFailureDetails**](InsufficientGpsFailureDetails.md) |  |  [optional] |
|**noOverlapGpsDetails** | [**NoOverlapGpsFailureDetails**](NoOverlapGpsFailureDetails.md) |  |  [optional] |
|**notOutdoorsDetails** | [**NotOutdoorsFailureDetails**](NotOutdoorsFailureDetails.md) |  |  [optional] |



