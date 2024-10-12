# NotificationHubsManagementClient.SharedAccessAuthorizationRuleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimType** | **String** | A string that describes the claim type | [optional] [readonly] 
**claimValue** | **String** | A string that describes the claim value | [optional] [readonly] 
**createdTime** | **String** | The created time for this rule | [optional] [readonly] 
**keyName** | **String** | A string that describes the authorization rule. | [optional] [readonly] 
**modifiedTime** | **String** | The last modified time for this rule | [optional] [readonly] 
**primaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. | [optional] [readonly] 
**revision** | **Number** | The revision number for the rule | [optional] [readonly] 
**rights** | **[String]** | The rights associated with the rule. | [optional] 
**secondaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. | [optional] [readonly] 



## Enum: [RightsEnum]


* `Manage` (value: `"Manage"`)

* `Send` (value: `"Send"`)

* `Listen` (value: `"Listen"`)




