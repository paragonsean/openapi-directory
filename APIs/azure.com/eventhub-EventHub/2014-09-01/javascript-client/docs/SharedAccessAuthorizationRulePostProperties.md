# EventHubManagementClient.SharedAccessAuthorizationRulePostProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claimType** | **String** | A string that describes Claim Type for authorization rule. | [optional] 
**claimValue** | **String** | A string that describes Claim Value of authorization rule. | [optional] 
**createdTime** | **Date** | The time the namespace was created. | [optional] [readonly] 
**keyName** | **String** | A string that describes the Key Name of authorization rule. | [optional] 
**modifiedTime** | **Date** | The time the namespace was updated. | [optional] [readonly] 
**primaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. | [optional] 
**rights** | **[String]** | The rights associated with the rule. | 
**secondaryKey** | **String** | A base64-encoded 256-bit primary key for signing and validating the SAS token. | [optional] 



## Enum: [RightsEnum]


* `Manage` (value: `"Manage"`)

* `Send` (value: `"Send"`)

* `Listen` (value: `"Listen"`)




