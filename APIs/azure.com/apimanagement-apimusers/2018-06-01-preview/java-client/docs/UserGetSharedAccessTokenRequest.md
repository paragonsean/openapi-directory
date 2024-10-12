

# UserGetSharedAccessTokenRequest

Parameters supplied to the Get User Token operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiry** | **OffsetDateTime** | The Expiry time of the Token. Maximum token expiry time is set to 30 days. The date conforms to the following format: &#x60;yyyy-MM-ddTHH:mm:ssZ&#x60; as specified by the ISO 8601 standard.  |  |
|**keyType** | [**KeyTypeEnum**](#KeyTypeEnum) | The Key to be used to generate token for user. |  |



## Enum: KeyTypeEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;primary&quot; |
| SECONDARY | &quot;secondary&quot; |



