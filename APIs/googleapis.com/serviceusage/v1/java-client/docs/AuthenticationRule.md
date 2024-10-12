

# AuthenticationRule

Authentication rules for the service. By default, if a method has any authentication requirements, every request must include a valid credential matching one of the requirements. It's an error to include more than one kind of credential in a single request. If a method doesn't have any auth requirements, request credentials will be ignored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowWithoutCredential** | **Boolean** | If true, the service accepts API keys without any other credential. This flag only applies to HTTP and gRPC requests. |  [optional] |
|**oauth** | [**OAuthRequirements**](OAuthRequirements.md) |  |  [optional] |
|**requirements** | [**List&lt;AuthRequirement&gt;**](AuthRequirement.md) | Requirements for additional authentication providers. |  [optional] |
|**selector** | **String** | Selects the methods to which this rule applies. Refer to selector for syntax details. |  [optional] |



