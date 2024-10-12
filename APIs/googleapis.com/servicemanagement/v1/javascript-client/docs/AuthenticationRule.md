# ServiceManagementApi.AuthenticationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowWithoutCredential** | **Boolean** | If true, the service accepts API keys without any other credential. This flag only applies to HTTP and gRPC requests. | [optional] 
**oauth** | [**OAuthRequirements**](OAuthRequirements.md) |  | [optional] 
**requirements** | [**[AuthRequirement]**](AuthRequirement.md) | Requirements for additional authentication providers. | [optional] 
**selector** | **String** | Selects the methods to which this rule applies. Refer to selector for syntax details. | [optional] 


