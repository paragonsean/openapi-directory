# BatchApi.Runnable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alwaysRun** | **Boolean** | By default, after a Runnable fails, no further Runnable are executed. This flag indicates that this Runnable must be run even if the Task has already failed. This is useful for Runnables that copy output files off of the VM or for debugging. The always_run flag does not override the Task&#39;s overall max_run_duration. If the max_run_duration has expired then no further Runnables will execute, not even always_run Runnables. | [optional] 
**background** | **Boolean** | This flag allows a Runnable to continue running in the background while the Task executes subsequent Runnables. This is useful to provide services to other Runnables (or to provide debugging support tools like SSH servers). | [optional] 
**barrier** | [**Barrier**](Barrier.md) |  | [optional] 
**container** | [**Container**](Container.md) |  | [optional] 
**displayName** | **String** | Optional. DisplayName is an optional field that can be provided by the caller. If provided, it will be used in logs and other outputs to identify the script, making it easier for users to understand the logs. If not provided the index of the runnable will be used for outputs. | [optional] 
**environment** | [**Environment**](Environment.md) |  | [optional] 
**ignoreExitStatus** | **Boolean** | Normally, a non-zero exit status causes the Task to fail. This flag allows execution of other Runnables to continue instead. | [optional] 
**labels** | **{String: String}** | Labels for this Runnable. | [optional] 
**script** | [**Script**](Script.md) |  | [optional] 
**timeout** | **String** | Timeout for this Runnable. | [optional] 


