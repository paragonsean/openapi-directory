

# SharedAccessAuthorizationRuleProperties

SharedAccessAuthorizationRule properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**claimType** | **String** | A string that describes the claim type |  [optional] [readonly] |
|**claimValue** | **String** | A string that describes the claim value |  [optional] [readonly] |
|**createdTime** | **String** | The created time for this rule |  [optional] [readonly] |
|**keyName** | **String** | A string that describes the authorization rule. |  [optional] [readonly] |
|**modifiedTime** | **String** | The last modified time for this rule |  [optional] [readonly] |
|**primaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. |  [optional] [readonly] |
|**revision** | **Integer** | The revision number for the rule |  [optional] [readonly] |
|**rights** | [**List&lt;RightsEnum&gt;**](#List&lt;RightsEnum&gt;) | The rights associated with the rule. |  [optional] |
|**secondaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. |  [optional] [readonly] |



## Enum: List&lt;RightsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGE | &quot;Manage&quot; |
| SEND | &quot;Send&quot; |
| LISTEN | &quot;Listen&quot; |



