# GraphRbacManagementClient.GroupCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Group display name | 
**mailEnabled** | **Boolean** | Whether the group is mail-enabled. Must be false. This is because only pure security groups can be created using the Graph API. | 
**mailNickname** | **String** | Mail nickname | 
**securityEnabled** | **Boolean** | Whether the group is a security group. Must be true. This is because only pure security groups can be created using the Graph API. | 



## Enum: MailEnabledEnum


* `false` (value: `"false"`)





## Enum: SecurityEnabledEnum


* `true` (value: `"true"`)




