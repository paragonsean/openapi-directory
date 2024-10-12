

# Authentication

`Authentication` defines the authentication configuration for API methods provided by an API service. Example: name: calendar.googleapis.com authentication: providers: - id: google_calendar_auth jwks_uri: https://www.googleapis.com/oauth2/v1/certs issuer: https://securetoken.google.com rules: - selector: \"*\" requirements: provider_id: google_calendar_auth - selector: google.calendar.Delegate oauth: canonical_scopes: https://www.googleapis.com/auth/calendar.read

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**providers** | [**List&lt;AuthProvider&gt;**](AuthProvider.md) | Defines a set of authentication providers that a service supports. |  [optional] |
|**rules** | [**List&lt;AuthenticationRule&gt;**](AuthenticationRule.md) | A list of authentication rules that apply to individual API methods. **NOTE:** All service configuration rules follow \&quot;last one wins\&quot; order. |  [optional] |



