

# GoogleCloudApigeeV1ExportRequest

Request body for [CreateExportRequest]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**csvDelimiter** | **String** | Optional. Delimiter used in the CSV file, if &#x60;outputFormat&#x60; is set to &#x60;csv&#x60;. Defaults to the &#x60;,&#x60; (comma) character. Supported delimiter characters include comma (&#x60;,&#x60;), pipe (&#x60;|&#x60;), and tab (&#x60;\\t&#x60;). |  [optional] |
|**datastoreName** | **String** | Required. Name of the preconfigured datastore. |  [optional] |
|**dateRange** | [**GoogleCloudApigeeV1DateRange**](GoogleCloudApigeeV1DateRange.md) |  |  [optional] |
|**description** | **String** | Optional. Description of the export job. |  [optional] |
|**name** | **String** | Required. Display name of the export job. |  [optional] |
|**outputFormat** | **String** | Optional. Output format of the export. Valid values include: &#x60;csv&#x60; or &#x60;json&#x60;. Defaults to &#x60;json&#x60;. Note: Configure the delimiter for CSV output using the &#x60;csvDelimiter&#x60; property. |  [optional] |



