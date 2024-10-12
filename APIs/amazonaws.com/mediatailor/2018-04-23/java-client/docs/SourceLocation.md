

# SourceLocation

A source location is a container for sources. For more information about source locations, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\">Working with source locations</a> in the <i>MediaTailor User Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessConfiguration** | [**DescribeSourceLocationResponseAccessConfiguration**](DescribeSourceLocationResponseAccessConfiguration.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**defaultSegmentDeliveryConfiguration** | [**SourceLocationDefaultSegmentDeliveryConfiguration**](SourceLocationDefaultSegmentDeliveryConfiguration.md) |  |  [optional] |
|**httpConfiguration** | [**UpdateSourceLocationResponseHttpConfiguration**](UpdateSourceLocationResponseHttpConfiguration.md) |  |  |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**segmentDeliveryConfigurations** | [**List**](List.md) |  |  [optional] |
|**sourceLocationName** | [**String**](String.md) |  |  |
|**tags** | [**Map**](Map.md) |  |  [optional] |



