# ManagementApi.CreateCompanyUserResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) | References to resources connected with this user. | [optional] 
**accountGroups** | **[String]** | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. | [optional] 
**active** | **Boolean** | Indicates whether this user is active. | [optional] 
**apps** | **[String]** | Set of apps available to this user | [optional] 
**associatedMerchantAccounts** | **[String]** | The list of [merchant accounts](https://docs.adyen.com/account/account-structure#merchant-accounts) associated with this user. | [optional] 
**email** | **String** | The email address of the user. | 
**id** | **String** | The unique identifier of the user. | 
**name** | [**Name**](Name.md) | The user&#39;s full name. | [optional] 
**roles** | **[String]** | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. | 
**timeZoneCode** | **String** | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. | 
**username** | **String** | The username for this user. | 


