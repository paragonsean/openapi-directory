

# BusinessReportResponseDetails

Results of the entity create or update along with the results of the requested reports. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkId** | **UUID** | Unique identifier for the report operation.  |  [optional] |
|**entity** | [**EntityObject**](EntityObject.md) |  |  [optional] |
|**reports** | [**List&lt;BusinessReportResponseObject&gt;**](BusinessReportResponseObject.md) | The collection of requested business reports.  |  [optional] |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  [optional] |



