

# User

A Users resource represents an account associated with an enterprise. The account may be specific to a device or to an individual user (who can then use the account across multiple devices). The account may provide access to managed Google Play only, or to other Google services, depending on the identity model: - The Google managed domain identity model requires synchronization to Google account sources (via primaryEmail). - The managed Google Play Accounts identity model provides a dynamic means for enterprises to create user or device accounts as needed. These accounts provide access to managed Google Play. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountIdentifier** | **String** | A unique identifier you create for this user, such as \&quot;user342\&quot; or \&quot;asset#44418\&quot;. Do not use personally identifiable information (PII) for this property. Must always be set for EMM-managed users. Not set for Google-managed users. |  [optional] |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The type of account that this user represents. A userAccount can be installed on multiple devices, but a deviceAccount is specific to a single device. An EMM-managed user (emmManaged) can be either type (userAccount, deviceAccount), but a Google-managed user (googleManaged) is always a userAccount. |  [optional] |
|**displayName** | **String** | The name that will appear in user interfaces. Setting this property is optional when creating EMM-managed users. If you do set this property, use something generic about the organization (such as \&quot;Example, Inc.\&quot;) or your name (as EMM). Not used for Google-managed user accounts. @mutable androidenterprise.users.update |  [optional] |
|**id** | **String** | The unique ID for the user. |  [optional] |
|**managementType** | [**ManagementTypeEnum**](#ManagementTypeEnum) | The entity that manages the user. With googleManaged users, the source of truth is Google so EMMs have to make sure a Google Account exists for the user. With emmManaged users, the EMM is in charge. |  [optional] |
|**primaryEmail** | **String** | The user&#39;s primary email address, for example, \&quot;jsmith@example.com\&quot;. Will always be set for Google managed users and not set for EMM managed users. |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| DEVICE_ACCOUNT | &quot;deviceAccount&quot; |
| USER_ACCOUNT | &quot;userAccount&quot; |



## Enum: ManagementTypeEnum

| Name | Value |
|---- | -----|
| GOOGLE_MANAGED | &quot;googleManaged&quot; |
| EMM_MANAGED | &quot;emmManaged&quot; |



