

# OidcIdentityProviderConfigRequest

An object representing an OpenID Connect (OIDC) configuration. Before associating an OIDC identity provider to your cluster, review the considerations in <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/authenticate-oidc-identity-provider.html\">Authenticating users for your cluster from an OpenID Connect identity provider</a> in the <i>Amazon EKS User Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identityProviderConfigName** | [**String**](String.md) |  |  |
|**issuerUrl** | [**String**](String.md) |  |  |
|**clientId** | [**String**](String.md) |  |  |
|**usernameClaim** | [**String**](String.md) |  |  [optional] |
|**usernamePrefix** | [**String**](String.md) |  |  [optional] |
|**groupsClaim** | [**String**](String.md) |  |  [optional] |
|**groupsPrefix** | [**String**](String.md) |  |  [optional] |
|**requiredClaims** | [**Map**](Map.md) |  |  [optional] |



