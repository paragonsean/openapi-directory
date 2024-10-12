# ApiManagementClient.UserGetSharedAccessTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **Date** | The Expiry time of the Token. Maximum token expiry time is set to 30 days. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  | 
**keyType** | **String** | The Key to be used to generate token for user. | [default to &#39;primary&#39;]



## Enum: KeyTypeEnum


* `primary` (value: `"primary"`)

* `secondary` (value: `"secondary"`)




