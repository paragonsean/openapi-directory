

# GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest

Request message for MetadataService.AddContextArtifactsAndExecutions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifacts** | **List&lt;String&gt;** | The resource names of the Artifacts to attribute to the Context. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/artifacts/{artifact}&#x60; |  [optional] |
|**executions** | **List&lt;String&gt;** | The resource names of the Executions to associate with the Context. Format: &#x60;projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}&#x60; |  [optional] |



