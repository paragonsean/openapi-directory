

# ApigatewayApiConfig

An API Configuration is a combination of settings for both the Managed Service and Gateways serving this API Config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**displayName** | **String** | Optional. Display name. |  [optional] |
|**gatewayConfig** | [**ApigatewayGatewayConfig**](ApigatewayGatewayConfig.md) |  |  [optional] |
|**gatewayServiceAccount** | **String** | Immutable. The Google Cloud IAM Service Account that Gateways serving this config should use to authenticate to other services. This may either be the Service Account&#39;s email (&#x60;{ACCOUNT_ID}@{PROJECT}.iam.gserviceaccount.com&#x60;) or its full resource name (&#x60;projects/{PROJECT}/accounts/{UNIQUE_ID}&#x60;). This is most often used when the service is a GCP resource such as a Cloud Run Service or an IAP-secured service. |  [optional] |
|**grpcServices** | [**List&lt;ApigatewayApiConfigGrpcServiceDefinition&gt;**](ApigatewayApiConfigGrpcServiceDefinition.md) | Optional. gRPC service definition files. If specified, openapi_documents must not be included. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] |
|**managedServiceConfigs** | [**List&lt;ApigatewayApiConfigFile&gt;**](ApigatewayApiConfigFile.md) | Optional. Service Configuration files. At least one must be included when using gRPC service definitions. See https://cloud.google.com/endpoints/docs/grpc/grpc-service-config#service_configuration_overview for the expected file contents. If multiple files are specified, the files are merged with the following rules: * All singular scalar fields are merged using \&quot;last one wins\&quot; semantics in the order of the files uploaded. * Repeated fields are concatenated. * Singular embedded messages are merged using these rules for nested fields. |  [optional] |
|**name** | **String** | Output only. Resource name of the API Config. Format: projects/{project}/locations/global/apis/{api}/configs/{api_config} |  [optional] [readonly] |
|**openapiDocuments** | [**List&lt;ApigatewayApiConfigOpenApiDocument&gt;**](ApigatewayApiConfigOpenApiDocument.md) | Optional. OpenAPI specification documents. If specified, grpc_services and managed_service_configs must not be included. |  [optional] |
|**serviceConfigId** | **String** | Output only. The ID of the associated Service Config ( https://cloud.google.com/service-infrastructure/docs/glossary#config). |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the API Config. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| ACTIVATING | &quot;ACTIVATING&quot; |



