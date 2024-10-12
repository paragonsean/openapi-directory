# ApiV100.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionNotificationsLastReadOn** | **Date** |  | [optional] 
**email** | **String** |  | [optional] 
**externalConnections** | [**[ExternalConnection]**](ExternalConnection.md) |  | [optional] 
**hasBeenOnboarded** | **Boolean** |  | [optional] 
**id** | **Number** |  | [optional] 
**isLocked** | **Boolean** |  | [optional] 
**isVerified** | **Boolean** |  | [optional] 
**knowledgeNotificationsLastReadOn** | **Date** |  | [optional] 
**lastSeenOn** | **Date** |  | [optional] 
**name** | **String** |  | [optional] 
**password** | **String** |  | [optional] 
**passwordSalt** | **String** |  | [optional] 
**referralPath** | **String** |  | [optional] 
**referredUsers** | **Number** |  | [optional] 
**referrerKey** | **String** |  | [optional] 
**settings** | [**UserSettings**](UserSettings.md) |  | [optional] 
**status** | **String** |  | [optional] 
**subscriptionPlan** | [**SubscriptionPlan**](SubscriptionPlan.md) |  | [optional] 
**type** | **String** |  | [optional] 
**username** | **String** |  | [optional] 
**verifiedOn** | **Date** |  | [optional] 
**yearsOfExperience** | **String** |  | [optional] 



## Enum: StatusEnum


* `Normal` (value: `"Normal"`)

* `Fraudlent` (value: `"Fraudlent"`)

* `Locked` (value: `"Locked"`)





## Enum: TypeEnum


* `Anonymous` (value: `"Anonymous"`)

* `Customer` (value: `"Customer"`)

* `SystemAdministrator` (value: `"SystemAdministrator"`)

* `Collaborator` (value: `"Collaborator"`)





## Enum: YearsOfExperienceEnum


* `One` (value: `"One"`)

* `OneToThree` (value: `"OneToThree"`)

* `ThreeToFive` (value: `"ThreeToFive"`)

* `SixPlus` (value: `"SixPlus"`)




