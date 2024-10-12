

# User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionNotificationsLastReadOn** | **OffsetDateTime** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**externalConnections** | [**List&lt;ExternalConnection&gt;**](ExternalConnection.md) |  |  [optional] |
|**hasBeenOnboarded** | **Boolean** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**isLocked** | **Boolean** |  |  [optional] |
|**isVerified** | **Boolean** |  |  [optional] |
|**knowledgeNotificationsLastReadOn** | **OffsetDateTime** |  |  [optional] |
|**lastSeenOn** | **OffsetDateTime** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**password** | **String** |  |  [optional] |
|**passwordSalt** | **String** |  |  [optional] |
|**referralPath** | **String** |  |  [optional] |
|**referredUsers** | **Integer** |  |  [optional] |
|**referrerKey** | **String** |  |  [optional] |
|**settings** | [**UserSettings**](UserSettings.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**subscriptionPlan** | [**SubscriptionPlan**](SubscriptionPlan.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**username** | **String** |  |  [optional] |
|**verifiedOn** | **OffsetDateTime** |  |  [optional] |
|**yearsOfExperience** | [**YearsOfExperienceEnum**](#YearsOfExperienceEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;Normal&quot; |
| FRAUDLENT | &quot;Fraudlent&quot; |
| LOCKED | &quot;Locked&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ANONYMOUS | &quot;Anonymous&quot; |
| CUSTOMER | &quot;Customer&quot; |
| SYSTEM_ADMINISTRATOR | &quot;SystemAdministrator&quot; |
| COLLABORATOR | &quot;Collaborator&quot; |



## Enum: YearsOfExperienceEnum

| Name | Value |
|---- | -----|
| ONE | &quot;One&quot; |
| ONE_TO_THREE | &quot;OneToThree&quot; |
| THREE_TO_FIVE | &quot;ThreeToFive&quot; |
| SIX_PLUS | &quot;SixPlus&quot; |



