# MerakiDashboardApi.CreateNetworkMerakiAuthUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | Authorization type for user. Can be &#39;Guest&#39; or &#39;802.1X&#39; for wireless networks, or &#39;Client VPN&#39; for wired networks. Defaults to &#39;802.1X&#39;. | [optional] [default to &#39;802.1X&#39;]
**authorizations** | [**[CreateNetworkMerakiAuthUserRequestAuthorizationsInner]**](CreateNetworkMerakiAuthUserRequestAuthorizationsInner.md) | Authorization zones and expiration dates for the user. | 
**email** | **String** | Email address of the user | 
**emailPasswordToUser** | **Boolean** | Whether or not Meraki should email the password to user. Default is false. | [optional] 
**isAdmin** | **Boolean** | Whether or not the user is a Dashboard administrator. | [optional] 
**name** | **String** | Name of the user. Only required If the user is not a Dashboard administrator. | [optional] 
**password** | **String** | The password for this user account. Only required If the user is not a Dashboard administrator. | [optional] 



## Enum: AccountTypeEnum


* `802.1X` (value: `"802.1X"`)

* `Client VPN` (value: `"Client VPN"`)

* `Guest` (value: `"Guest"`)




