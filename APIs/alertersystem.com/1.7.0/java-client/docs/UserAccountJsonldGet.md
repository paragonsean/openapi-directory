

# UserAccountJsonldGet

The UserAccount resource contains basic information regarding the authenticated user account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atContext** | [**AlertLogJsonldGetContext**](AlertLogJsonldGetContext.md) |  |  [optional] |
|**atId** | **String** |  |  [optional] [readonly] |
|**atType** | **String** |  |  [optional] [readonly] |
|**accountLevelCode** | **String** | The account level of the user. |  [optional] |
|**creditsOveragePercentTripSwitch** | **Integer** | If the credits consumed in the billing period are this percentage above the account plan&#39;s included credits, cease further consumption of credits until the end of the billing period. Any integer between 1 and 1,000. Optional. Leave blank for no limit. |  [optional] |
|**email** | **String** | The email address of the user. |  [optional] |
|**firstName** | **String** | The first name of the user. |  [optional] |
|**id** | **UUID** | The unique identifier of the resource instance. |  [optional] |
|**isDelinquent** | **Boolean** | Whether the user account has overdue payments. |  [optional] |
|**lastName** | **String** | The last name of the user. |  [optional] |
|**timezoneCode** | **String** | The timezone of the user. |  [optional] |



