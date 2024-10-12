

# OAuthToken

Contains information needed for generating an [OAuth token](https://developers.google.com/identity/protocols/OAuth2). This type of authorization should generally only be used when calling Google APIs hosted on *.googleapis.com.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scope** | **String** | OAuth scope to be used for generating OAuth access token. If not specified, \&quot;https://www.googleapis.com/auth/cloud-platform\&quot; will be used. |  [optional] |
|**serviceAccountEmail** | **String** | [Service account email](https://cloud.google.com/iam/docs/service-accounts) to be used for generating OAuth token. The service account must be within the same project as the queue. The caller must have iam.serviceAccounts.actAs permission for the service account. |  [optional] |



