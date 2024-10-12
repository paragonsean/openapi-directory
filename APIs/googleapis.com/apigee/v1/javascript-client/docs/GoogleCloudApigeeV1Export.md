# ApigeeApi.GoogleCloudApigeeV1Export

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **String** | Output only. Time the export job was created. | [optional] [readonly] 
**datastoreName** | **String** | Name of the datastore that is the destination of the export job [datastore] | [optional] 
**description** | **String** | Description of the export job. | [optional] 
**error** | **String** | Output only. Error is set when export fails | [optional] [readonly] 
**executionTime** | **String** | Output only. Execution time for this export job. If the job is still in progress, it will be set to the amount of time that has elapsed since&#x60;created&#x60;, in seconds. Else, it will set to (&#x60;updated&#x60; - &#x60;created&#x60;), in seconds. | [optional] [readonly] 
**name** | **String** | Display name of the export job. | [optional] 
**self** | **String** | Output only. Self link of the export job. A URI that can be used to retrieve the status of an export job. Example: &#x60;/organizations/myorg/environments/myenv/analytics/exports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd&#x60; | [optional] [readonly] 
**state** | **String** | Output only. Status of the export job. Valid values include &#x60;enqueued&#x60;, &#x60;running&#x60;, &#x60;completed&#x60;, and &#x60;failed&#x60;. | [optional] [readonly] 
**updated** | **String** | Output only. Time the export job was last updated. | [optional] [readonly] 


