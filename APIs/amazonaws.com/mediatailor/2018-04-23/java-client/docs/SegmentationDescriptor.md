

# SegmentationDescriptor

<p>The <code>segmentation_descriptor</code> message can contain advanced metadata fields, like content identifiers, to convey a wide range of information about the ad break. MediaTailor writes the ad metadata in the egress manifest as part of the <code>EXT-X-DATERANGE</code> or <code>EventStream</code> ad marker's SCTE-35 data.</p> <p> <code>segmentation_descriptor</code> messages must be sent with the <code>time_signal</code> message type.</p> <p>See the <code>segmentation_descriptor()</code> table of the 2022 SCTE-35 specification for more information.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**segmentNum** | [**Integer**](Integer.md) |  |  [optional] |
|**segmentationEventId** | [**Integer**](Integer.md) |  |  [optional] |
|**segmentationTypeId** | [**Integer**](Integer.md) |  |  [optional] |
|**segmentationUpid** | [**String**](String.md) |  |  [optional] |
|**segmentationUpidType** | [**Integer**](Integer.md) |  |  [optional] |
|**segmentsExpected** | [**Integer**](Integer.md) |  |  [optional] |
|**subSegmentNum** | [**Integer**](Integer.md) |  |  [optional] |
|**subSegmentsExpected** | [**Integer**](Integer.md) |  |  [optional] |



