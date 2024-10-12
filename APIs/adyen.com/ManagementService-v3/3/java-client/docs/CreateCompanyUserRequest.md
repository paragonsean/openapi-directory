

# CreateCompanyUserRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountGroups** | **List&lt;String&gt;** | The list of [account groups](https://docs.adyen.com/account/account-structure#account-groups) associated with this user. |  [optional] |
|**associatedMerchantAccounts** | **List&lt;String&gt;** | The list of [merchant accounts](https://docs.adyen.com/account/account-structure#merchant-accounts) associated with this user. |  [optional] |
|**email** | **String** | The email address of the user. |  |
|**name** | [**Name**](Name.md) | The user&#39;s full name.  Allowed length: 1—80 characters. |  |
|**roles** | **List&lt;String&gt;** | The list of [roles](https://docs.adyen.com/account/user-roles) for this user. |  [optional] |
|**timeZoneCode** | **String** | The [tz database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) of the time zone of the user. For example, **Europe/Amsterdam**. |  [optional] |
|**username** | **String** | The user&#39;s email address that will be their username. Must be the same as the one in the &#x60;email&#x60; field. |  |



