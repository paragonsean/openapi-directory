

# IdpConfig

Template for a single idp configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | OAuth2 client ID. |  [optional] |
|**enabled** | **Boolean** | Whether this IDP is enabled. |  [optional] |
|**experimentPercent** | **Integer** | Percent of users who will be prompted/redirected federated login for this IDP. |  [optional] |
|**provider** | **String** | OAuth2 provider. |  [optional] |
|**secret** | **String** | OAuth2 client secret. |  [optional] |
|**whitelistedAudiences** | **List&lt;String&gt;** | Whitelisted client IDs for audience check. |  [optional] |



