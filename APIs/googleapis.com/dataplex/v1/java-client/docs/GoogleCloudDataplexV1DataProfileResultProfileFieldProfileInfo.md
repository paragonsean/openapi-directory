

# GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfo

The profile information for each field type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**distinctRatio** | **Double** | Ratio of rows with distinct values against total scanned rows. Not available for complex non-groupable field type RECORD and fields with REPEATABLE mode. |  [optional] |
|**doubleProfile** | [**GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfo**](GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfo.md) |  |  [optional] |
|**integerProfile** | [**GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfo**](GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfo.md) |  |  [optional] |
|**nullRatio** | **Double** | Ratio of rows with null value against total scanned rows. |  [optional] |
|**stringProfile** | [**GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfo**](GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfo.md) |  |  [optional] |
|**topNValues** | [**List&lt;GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValue&gt;**](GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValue.md) | The list of top N non-null values, frequency and ratio with which they occur in the scanned data. N is 10 or equal to the number of distinct values in the field, whichever is smaller. Not available for complex non-groupable field type RECORD and fields with REPEATABLE mode. |  [optional] |



