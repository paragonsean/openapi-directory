

# NavigationInfo

NavigationInfo describes what steps if any come before or after this step, or what steps are parents or children of this step.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**children** | **List&lt;String&gt;** | Step entries that can be reached by \&quot;stepping into\&quot; e.g. a subworkflow call. |  [optional] |
|**next** | **String** | The index of the next step in the current workflow, if any. |  [optional] |
|**parent** | **String** | The step entry, if any, that can be reached by \&quot;stepping out\&quot; of the current workflow being executed. |  [optional] |
|**previous** | **String** | The index of the previous step in the current workflow, if any. |  [optional] |



