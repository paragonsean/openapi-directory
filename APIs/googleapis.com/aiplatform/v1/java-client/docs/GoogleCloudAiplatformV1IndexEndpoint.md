

# GoogleCloudAiplatformV1IndexEndpoint

Indexes are deployed into it. An IndexEndpoint can have multiple DeployedIndexes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when this IndexEndpoint was created. |  [optional] [readonly] |
|**deployedIndexes** | [**List&lt;GoogleCloudAiplatformV1DeployedIndex&gt;**](GoogleCloudAiplatformV1DeployedIndex.md) | Output only. The indexes deployed in this endpoint. |  [optional] [readonly] |
|**description** | **String** | The description of the IndexEndpoint. |  [optional] |
|**displayName** | **String** | Required. The display name of the IndexEndpoint. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**enablePrivateServiceConnect** | **Boolean** | Optional. Deprecated: If true, expose the IndexEndpoint via private service connect. Only one of the fields, network or enable_private_service_connect, can be set. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1EncryptionSpec**](GoogleCloudAiplatformV1EncryptionSpec.md) |  |  [optional] |
|**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize your IndexEndpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |  [optional] |
|**name** | **String** | Output only. The resource name of the IndexEndpoint. |  [optional] [readonly] |
|**network** | **String** | Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the IndexEndpoint should be peered. Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network. network and private_service_connect_config are mutually exclusive. [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert): &#x60;projects/{project}/global/networks/{network}&#x60;. Where {project} is a project number, as in &#39;12345&#39;, and {network} is network name. |  [optional] |
|**privateServiceConnectConfig** | [**GoogleCloudAiplatformV1PrivateServiceConnectConfig**](GoogleCloudAiplatformV1PrivateServiceConnectConfig.md) |  |  [optional] |
|**publicEndpointDomainName** | **String** | Output only. If public_endpoint_enabled is true, this field will be populated with the domain name to use for this index endpoint. |  [optional] [readonly] |
|**publicEndpointEnabled** | **Boolean** | Optional. If true, the deployed index will be accessible through public endpoint. |  [optional] |
|**updateTime** | **String** | Output only. Timestamp when this IndexEndpoint was last updated. This timestamp is not updated when the endpoint&#39;s DeployedIndexes are updated, e.g. due to updates of the original Indexes they are the deployments of. |  [optional] [readonly] |



