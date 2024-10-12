

# GoogleCloudDataplexV1RunTaskRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **Map&lt;String, String&gt;** | Optional. Execution spec arguments. If the map is left empty, the task will run with existing execution spec args from task definition. If the map contains an entry with a new key, the same will be added to existing set of args. If the map contains an entry with an existing arg key in task definition, the task will run with new arg value for that entry. Clearing an existing arg will require arg value to be explicitly set to a hyphen \&quot;-\&quot;. The arg value cannot be empty. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-defined labels for the task. If the map is left empty, the task will run with existing labels from task definition. If the map contains an entry with a new key, the same will be added to existing set of labels. If the map contains an entry with an existing label key in task definition, the task will run with new label value for that entry. Clearing an existing label will require label value to be explicitly set to a hyphen \&quot;-\&quot;. The label value cannot be empty. |  [optional] |



