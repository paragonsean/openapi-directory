

# IdentitytoolkitRelyingpartyGetAccountInfoRequest

Request to get the account information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. |  [optional] |
|**email** | **List&lt;String&gt;** | The list of emails of the users to inquiry. |  [optional] |
|**idToken** | **String** | The GITKit token of the authenticated user. |  [optional] |
|**localId** | **List&lt;String&gt;** | The list of local ID&#39;s of the users to inquiry. |  [optional] |
|**phoneNumber** | **List&lt;String&gt;** | Privileged caller can query users by specified phone number. |  [optional] |



