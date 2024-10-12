# ApiGatewayApi.ApigatewayBackendConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**googleServiceAccount** | **String** | Google Cloud IAM service account used to sign OIDC tokens for backends that have authentication configured (https://cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#backend). This may either be the Service Account&#39;s email (i.e. \&quot;{ACCOUNT_ID}@{PROJECT}.iam.gserviceaccount.com\&quot;) or its full resource name (i.e. \&quot;projects/{PROJECT}/accounts/{UNIQUE_ID}\&quot;). This is most often used when the backend is a GCP resource such as a Cloud Run Service or an IAP-secured service. Note that this token is always sent as an authorization header bearer token. The audience of the OIDC token is configured in the associated Service Config in the BackendRule option (https://github.com/googleapis/googleapis/blob/master/google/api/backend.proto#L125). | [optional] 


