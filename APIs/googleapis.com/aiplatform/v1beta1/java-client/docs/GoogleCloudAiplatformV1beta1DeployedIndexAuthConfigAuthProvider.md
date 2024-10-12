

# GoogleCloudAiplatformV1beta1DeployedIndexAuthConfigAuthProvider

Configuration for an authentication provider, including support for [JSON Web Token (JWT)](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedIssuers** | **List&lt;String&gt;** | A list of allowed JWT issuers. Each entry must be a valid Google service account, in the following format: &#x60;service-account-name@project-id.iam.gserviceaccount.com&#x60; |  [optional] |
|**audiences** | **List&lt;String&gt;** | The list of JWT [audiences](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.3). that are allowed to access. A JWT containing any of these audiences will be accepted. |  [optional] |



