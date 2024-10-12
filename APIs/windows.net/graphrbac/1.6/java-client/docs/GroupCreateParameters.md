

# GroupCreateParameters

Request parameters for creating a new group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Group display name |  |
|**mailEnabled** | [**MailEnabledEnum**](#MailEnabledEnum) | Whether the group is mail-enabled. Must be false. This is because only pure security groups can be created using the Graph API. |  |
|**mailNickname** | **String** | Mail nickname |  |
|**securityEnabled** | [**SecurityEnabledEnum**](#SecurityEnabledEnum) | Whether the group is a security group. Must be true. This is because only pure security groups can be created using the Graph API. |  |



## Enum: MailEnabledEnum

| Name | Value |
|---- | -----|
| FALSE | &quot;false&quot; |



## Enum: SecurityEnabledEnum

| Name | Value |
|---- | -----|
| TRUE | &quot;true&quot; |



