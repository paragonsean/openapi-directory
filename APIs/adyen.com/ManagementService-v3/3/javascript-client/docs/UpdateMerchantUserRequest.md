# ManagementApi.UpdateMerchantUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountGroups** | **[String]** | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. | [optional] 
**active** | **Boolean** | Sets the status of the user to active (**true**) or inactive (**false**). | [optional] 
**email** | **String** | The email address of the user. | [optional] 
**name** | [**Name2**](Name2.md) | The user&#39;s full name. | [optional] 
**roles** | **[String]** | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. | [optional] 
**timeZoneCode** | **String** | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. | [optional] 


