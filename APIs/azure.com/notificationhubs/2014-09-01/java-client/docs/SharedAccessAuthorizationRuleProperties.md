

# SharedAccessAuthorizationRuleProperties

SharedAccessAuthorizationRule properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**claimType** | **String** | The type of the claim. |  [optional] |
|**claimValue** | **String** | The value of the claim. |  [optional] |
|**createdTime** | **OffsetDateTime** | The time at which the authorization rule was created. |  [optional] |
|**keyName** | **String** | The name of the key that was used. |  [optional] |
|**modifiedTime** | **OffsetDateTime** | The most recent time the rule was updated. |  [optional] |
|**primaryKey** | **String** | The primary key that was used. |  [optional] |
|**revision** | **Integer** | The revision number for the rule. |  [optional] |
|**rights** | [**List&lt;RightsEnum&gt;**](#List&lt;RightsEnum&gt;) | The rights associated with the rule. |  [optional] |
|**secondaryKey** | **String** | The secondary key that was used. |  [optional] |



## Enum: List&lt;RightsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGE | &quot;Manage&quot; |
| SEND | &quot;Send&quot; |
| LISTEN | &quot;Listen&quot; |



