

# GoogleCloudApigeeV1CustomReport


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chartType** | **String** | This field contains the chart type for the report |  [optional] |
|**comments** | **List&lt;String&gt;** | Legacy field: not used. This field contains a list of comments associated with custom report |  [optional] |
|**createdAt** | **String** | Output only. Unix time when the app was created json key: createdAt |  [optional] [readonly] |
|**dimensions** | **List&lt;String&gt;** | This contains the list of dimensions for the report |  [optional] |
|**displayName** | **String** | This is the display name for the report |  [optional] |
|**environment** | **String** | Output only. Environment name |  [optional] [readonly] |
|**filter** | **String** | This field contains the filter expression |  [optional] |
|**fromTime** | **String** | Legacy field: not used. Contains the from time for the report |  [optional] |
|**lastModifiedAt** | **String** | Output only. Modified time of this entity as milliseconds since epoch. json key: lastModifiedAt |  [optional] [readonly] |
|**lastViewedAt** | **String** | Output only. Last viewed time of this entity as milliseconds since epoch |  [optional] [readonly] |
|**limit** | **String** | Legacy field: not used This field contains the limit for the result retrieved |  [optional] |
|**metrics** | [**List&lt;GoogleCloudApigeeV1CustomReportMetric&gt;**](GoogleCloudApigeeV1CustomReportMetric.md) | Required. This contains the list of metrics |  [optional] |
|**name** | **String** | Required. Unique identifier for the report T his is a legacy field used to encode custom report unique id |  [optional] |
|**offset** | **String** | Legacy field: not used. This field contains the offset for the data |  [optional] |
|**organization** | **String** | Output only. Organization name |  [optional] [readonly] |
|**properties** | [**List&lt;GoogleCloudApigeeV1ReportProperty&gt;**](GoogleCloudApigeeV1ReportProperty.md) | This field contains report properties such as ui metadata etc. |  [optional] |
|**sortByCols** | **List&lt;String&gt;** | Legacy field: not used much. Contains the list of sort by columns |  [optional] |
|**sortOrder** | **String** | Legacy field: not used much. Contains the sort order for the sort columns |  [optional] |
|**tags** | **List&lt;String&gt;** | Legacy field: not used. This field contains a list of tags associated with custom report |  [optional] |
|**timeUnit** | **String** | This field contains the time unit of aggregation for the report |  [optional] |
|**toTime** | **String** | Legacy field: not used. Contains the end time for the report |  [optional] |
|**topk** | **String** | Legacy field: not used. This field contains the top k parameter value for restricting the result |  [optional] |



