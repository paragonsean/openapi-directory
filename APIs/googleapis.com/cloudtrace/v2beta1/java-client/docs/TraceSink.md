

# TraceSink

Describes a sink used to export traces to a BigQuery dataset. The sink must be created within a project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. The canonical sink resource name, unique within the project. Must be of the form: projects/[PROJECT_NUMBER]/traceSinks/[SINK_ID]. E.g.: &#x60;\&quot;projects/12345/traceSinks/my-project-trace-sink\&quot;&#x60;. Sink identifiers are limited to 256 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods. |  [optional] |
|**outputConfig** | [**OutputConfig**](OutputConfig.md) |  |  [optional] |
|**writerIdentity** | **String** | Output only. A service account name for exporting the data. This field is set by sinks.create and sinks.update. The service account will need to be granted write access to the destination specified in the output configuration, see [Granting access for a resource](/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource). To create tables and to write data, this account needs the &#x60;dataEditor&#x60; role. Read more about roles in the [BigQuery documentation](https://cloud.google.com/bigquery/docs/access-control). E.g.: \&quot;service-00000001@00000002.iam.gserviceaccount.com\&quot; |  [optional] [readonly] |



