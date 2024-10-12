

# QueryAccessibleDataRequest

Queries all data_ids that are consented for a given use in the given consent store and writes them to a specified destination. The returned Operation includes a progress counter for the number of User data mappings processed. Errors are logged to Cloud Logging (see [Viewing error logs in Cloud Logging] (https://cloud.google.com/healthcare/docs/how-tos/logging) and [QueryAccessibleData] for a sample log entry).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsDestination** | [**GoogleCloudHealthcareV1ConsentGcsDestination**](GoogleCloudHealthcareV1ConsentGcsDestination.md) |  |  [optional] |
|**requestAttributes** | **Map&lt;String, String&gt;** | The values of request attributes associated with this access request. |  [optional] |
|**resourceAttributes** | **Map&lt;String, String&gt;** | Optional. The values of resource attributes associated with the type of resources being requested. If no values are specified, then all resource types are included in the output. |  [optional] |



