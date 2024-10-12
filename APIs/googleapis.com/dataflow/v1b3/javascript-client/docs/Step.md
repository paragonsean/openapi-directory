# DataflowApi.Step

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | The kind of step in the Cloud Dataflow job. | [optional] 
**name** | **String** | The name that identifies the step. This must be unique for each step with respect to all other steps in the Cloud Dataflow job. | [optional] 
**properties** | **{String: Object}** | Named properties associated with the step. Each kind of predefined step has its own required set of properties. Must be provided on Create. Only retrieved with JOB_VIEW_ALL. | [optional] 


