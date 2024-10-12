

# LaunchFlexTemplateParameter

Launch FlexTemplate Parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerSpec** | [**ContainerSpec**](ContainerSpec.md) |  |  [optional] |
|**containerSpecGcsPath** | **String** | Cloud Storage path to a file with json serialized ContainerSpec as content. |  [optional] |
|**environment** | [**FlexTemplateRuntimeEnvironment**](FlexTemplateRuntimeEnvironment.md) |  |  [optional] |
|**jobName** | **String** | Required. The job name to use for the created job. For update job request, job name should be same as the existing running job. |  [optional] |
|**launchOptions** | **Map&lt;String, String&gt;** | Launch options for this flex template job. This is a common set of options across languages and templates. This should not be used to pass job parameters. |  [optional] |
|**parameters** | **Map&lt;String, String&gt;** | The parameters for FlexTemplate. Ex. {\&quot;num_workers\&quot;:\&quot;5\&quot;} |  [optional] |
|**transformNameMappings** | **Map&lt;String, String&gt;** | Use this to pass transform_name_mappings for streaming update jobs. Ex:{\&quot;oldTransformName\&quot;:\&quot;newTransformName\&quot;,...}&#39; |  [optional] |
|**update** | **Boolean** | Set this to true if you are sending a request to update a running streaming job. When set, the job name should be the same as the running job. |  [optional] |



