

# IdentitytoolkitRelyingpartyVerifyCustomTokenRequest

Request to verify a custom token

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. |  [optional] |
|**instanceId** | **String** | Instance id token of the app. |  [optional] |
|**returnSecureToken** | **Boolean** | Whether return sts id token and refresh token instead of gitkit token. |  [optional] |
|**token** | **String** | The custom token to verify |  [optional] |



