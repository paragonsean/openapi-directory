

# SignJwtRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delegates** | **List&lt;String&gt;** | The sequence of service accounts in a delegation chain. Each service account must be granted the &#x60;roles/iam.serviceAccountTokenCreator&#x60; role on its next service account in the chain. The last service account in the chain must be granted the &#x60;roles/iam.serviceAccountTokenCreator&#x60; role on the service account that is specified in the &#x60;name&#x60; field of the request. The delegates must have the following format: &#x60;projects/-/serviceAccounts/{ACCOUNT_EMAIL_OR_UNIQUEID}&#x60;. The &#x60;-&#x60; wildcard character is required; replacing it with a project ID is invalid. |  [optional] |
|**payload** | **String** | Required. The JWT payload to sign. Must be a serialized JSON object that contains a JWT Claims Set. For example: &#x60;{\&quot;sub\&quot;: \&quot;user@example.com\&quot;, \&quot;iat\&quot;: 313435}&#x60; If the JWT Claims Set contains an expiration time (&#x60;exp&#x60;) claim, it must be an integer timestamp that is not in the past and no more than 12 hours in the future. |  [optional] |



