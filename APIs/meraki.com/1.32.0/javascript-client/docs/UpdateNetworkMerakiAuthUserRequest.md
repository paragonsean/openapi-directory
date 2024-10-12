# MerakiDashboardApi.UpdateNetworkMerakiAuthUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizations** | [**[UpdateNetworkMerakiAuthUserRequestAuthorizationsInner]**](UpdateNetworkMerakiAuthUserRequestAuthorizationsInner.md) | Authorization zones and expiration dates for the user. | [optional] 
**emailPasswordToUser** | **Boolean** | Whether or not Meraki should email the password to user. Default is false. | [optional] 
**name** | **String** | Name of the user. Only allowed If the user is not Dashboard administrator. | [optional] 
**password** | **String** | The password for this user account. Only allowed If the user is not Dashboard administrator. | [optional] 


