# SalesLoftPlatform.BulkJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | When this bulk job was created | [optional] 
**errors** | **Number** | Number of errored records at the time of request for this Bulk Job | [optional] 
**finishedAt** | **Date** | When this bulk job finished processing | [optional] 
**id** | **Number** | ID of this Bulk Job | [optional] 
**markedReadyAt** | **Date** | When this bulk job was marked as ready to execute | [optional] 
**name** | **String** | Name of this Bulk Job | [optional] 
**processed** | **Number** | Number of processed records at the time of request for this Bulk Job | [optional] 
**readyToExecute** | **Boolean** | Whether the Bulk Job is ready to be executed | [optional] 
**scopes** | **[Object]** | Scopes | [optional] 
**startedAt** | **Date** | When this bulk job started processing. null until bulk job is done | [optional] 
**state** | **String** | State of the Bulk Job.  Must be one of: open, executing, done. | [optional] 
**total** | **Number** | Number of total records for this Bulk Job | [optional] 
**type** | **String** | Type of the Bulk Job. | [optional] 
**updatedAt** | **Date** | When this bulk job was updated | [optional] 


