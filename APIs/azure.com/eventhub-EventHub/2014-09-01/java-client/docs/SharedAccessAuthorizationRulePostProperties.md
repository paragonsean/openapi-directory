

# SharedAccessAuthorizationRulePostProperties

AuthorizationRule properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**claimType** | **String** | A string that describes Claim Type for authorization rule. |  [optional] |
|**claimValue** | **String** | A string that describes Claim Value of authorization rule. |  [optional] |
|**createdTime** | **OffsetDateTime** | The time the namespace was created. |  [optional] [readonly] |
|**keyName** | **String** | A string that describes the Key Name of authorization rule. |  [optional] |
|**modifiedTime** | **OffsetDateTime** | The time the namespace was updated. |  [optional] [readonly] |
|**primaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. |  [optional] |
|**rights** | [**List&lt;RightsEnum&gt;**](#List&lt;RightsEnum&gt;) | The rights associated with the rule. |  |
|**secondaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. |  [optional] |



## Enum: List&lt;RightsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGE | &quot;Manage&quot; |
| SEND | &quot;Send&quot; |
| LISTEN | &quot;Listen&quot; |



