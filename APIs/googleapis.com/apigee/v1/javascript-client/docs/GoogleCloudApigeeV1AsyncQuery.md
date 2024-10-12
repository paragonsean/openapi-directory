# ApigeeApi.GoogleCloudApigeeV1AsyncQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **String** | Creation time of the query. | [optional] 
**envgroupHostname** | **String** | Hostname is available only when query is executed at host level. | [optional] 
**error** | **String** | Error is set when query fails. | [optional] 
**executionTime** | **String** | ExecutionTime is available only after the query is completed. | [optional] 
**name** | **String** | Asynchronous Query Name. | [optional] 
**queryParams** | [**GoogleCloudApigeeV1QueryMetadata**](GoogleCloudApigeeV1QueryMetadata.md) |  | [optional] 
**reportDefinitionId** | **String** | Asynchronous Report ID. | [optional] 
**result** | [**GoogleCloudApigeeV1AsyncQueryResult**](GoogleCloudApigeeV1AsyncQueryResult.md) |  | [optional] 
**resultFileSize** | **String** | ResultFileSize is available only after the query is completed. | [optional] 
**resultRows** | **String** | ResultRows is available only after the query is completed. | [optional] 
**self** | **String** | Self link of the query. Example: &#x60;/organizations/myorg/environments/myenv/queries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd&#x60; or following format if query is running at host level: &#x60;/organizations/myorg/hostQueries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd&#x60; | [optional] 
**state** | **String** | Query state could be \&quot;enqueued\&quot;, \&quot;running\&quot;, \&quot;completed\&quot;, \&quot;failed\&quot;. | [optional] 
**updated** | **String** | Last updated timestamp for the query. | [optional] 


