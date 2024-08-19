

# SensorStatisticsSummary

 Summary of ingestion statistics like whether data exists, number of missing values, number of invalid values and so on related to the particular sensor. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**componentName** | [**String**](String.md) |  |  [optional] |
|**sensorName** | [**String**](String.md) |  |  [optional] |
|**dataExists** | [**Boolean**](Boolean.md) |  |  [optional] |
|**missingValues** | [**SensorStatisticsSummaryMissingValues**](SensorStatisticsSummaryMissingValues.md) |  |  [optional] |
|**invalidValues** | [**SensorStatisticsSummaryInvalidValues**](SensorStatisticsSummaryInvalidValues.md) |  |  [optional] |
|**invalidDateEntries** | [**SensorStatisticsSummaryInvalidDateEntries**](SensorStatisticsSummaryInvalidDateEntries.md) |  |  [optional] |
|**duplicateTimestamps** | [**SensorStatisticsSummaryDuplicateTimestamps**](SensorStatisticsSummaryDuplicateTimestamps.md) |  |  [optional] |
|**categoricalValues** | [**SensorStatisticsSummaryCategoricalValues**](SensorStatisticsSummaryCategoricalValues.md) |  |  [optional] |
|**multipleOperatingModes** | [**SensorStatisticsSummaryMultipleOperatingModes**](SensorStatisticsSummaryMultipleOperatingModes.md) |  |  [optional] |
|**largeTimestampGaps** | [**SensorStatisticsSummaryLargeTimestampGaps**](SensorStatisticsSummaryLargeTimestampGaps.md) |  |  [optional] |
|**monotonicValues** | [**SensorStatisticsSummaryMonotonicValues**](SensorStatisticsSummaryMonotonicValues.md) |  |  [optional] |
|**dataStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**dataEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



