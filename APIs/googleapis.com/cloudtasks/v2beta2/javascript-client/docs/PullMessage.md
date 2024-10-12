# CloudTasksApi.PullMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **Blob** | A data payload consumed by the worker to execute the task. | [optional] 
**tag** | **String** | The task&#39;s tag. Tags allow similar tasks to be processed in a batch. If you label tasks with a tag, your worker can lease tasks with the same tag using filter. For example, if you want to aggregate the events associated with a specific user once a day, you could tag tasks with the user ID. The task&#39;s tag can only be set when the task is created. The tag must be less than 500 characters. SDK compatibility: Although the SDK allows tags to be either string or [bytes](https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/taskqueue/TaskOptions.html#tag-byte:A-), only UTF-8 encoded tags can be used in Cloud Tasks. If a tag isn&#39;t UTF-8 encoded, the tag will be empty when the task is returned by Cloud Tasks. | [optional] 


