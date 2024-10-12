# ExecutionService.RunDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**RunConfiguration**](RunConfiguration.md) |  | [optional] 
**parentRunId** | **String** | Specifies that the run history entry for this execution should be scoped within  an existing run as a child. Defaults to null, meaning the run has no parent.  This is intended for first-party service integration, not third-party API users. | [optional] 
**runType** | **String** | Specifies the runsource property for this run. The default value is \&quot;experiment\&quot; if not specified. | [optional] 
**snapshotId** | **String** | Snapshots are user project folders that have been uploaded to the cloud for subsequent  execution. This field is required when executing against cloud-based compute targets  unless the run submission was against the API endpoint that takes a zipped project folder  inline with the request. | [optional] 


