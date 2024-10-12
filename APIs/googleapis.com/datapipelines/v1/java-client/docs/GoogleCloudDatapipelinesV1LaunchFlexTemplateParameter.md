

# GoogleCloudDatapipelinesV1LaunchFlexTemplateParameter

Launch Flex Template parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerSpecGcsPath** | **String** | Cloud Storage path to a file with a JSON-serialized ContainerSpec as content. |  [optional] |
|**environment** | [**GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment**](GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment.md) |  |  [optional] |
|**jobName** | **String** | Required. The job name to use for the created job. For an update job request, the job name should be the same as the existing running job. |  [optional] |
|**launchOptions** | **Map&lt;String, String&gt;** | Launch options for this Flex Template job. This is a common set of options across languages and templates. This should not be used to pass job parameters. |  [optional] |
|**parameters** | **Map&lt;String, String&gt;** | The parameters for the Flex Template. Example: &#x60;{\&quot;num_workers\&quot;:\&quot;5\&quot;}&#x60; |  [optional] |
|**transformNameMappings** | **Map&lt;String, String&gt;** | Use this to pass transform name mappings for streaming update jobs. Example: &#x60;{\&quot;oldTransformName\&quot;:\&quot;newTransformName\&quot;,...}&#x60; |  [optional] |
|**update** | **Boolean** | Set this to true if you are sending a request to update a running streaming job. When set, the job name should be the same as the running job. |  [optional] |



