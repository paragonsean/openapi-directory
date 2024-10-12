# WorkflowExecutionsApi.NavigationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | **[String]** | Step entries that can be reached by \&quot;stepping into\&quot; e.g. a subworkflow call. | [optional] 
**next** | **String** | The index of the next step in the current workflow, if any. | [optional] 
**parent** | **String** | The step entry, if any, that can be reached by \&quot;stepping out\&quot; of the current workflow being executed. | [optional] 
**previous** | **String** | The index of the previous step in the current workflow, if any. | [optional] 


