# RubrikRestApi.LocalUserAccountLockoutStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountLockoutDurationInMinutes** | **Number** | Specifies the duration in minutes after which a locked user account is automatically unlocked. When set to 0, the user account is not unlocked automatically.  | 
**enabled** | **Boolean** | Specifies whether local user accounts are locked. When &#39;true&#39; the local user account is locked after &#39;x&#39; failed consecutive login attempts where &#39;x&#39; is specified by &#39;maxFailedLoginsForLocalUser&#39;. When &#39;false&#39; failed login attempts are not recorded and will not lock the local user account.  | 
**maxFailedLoginsForLocalUser** | **Number** | Specifies the number of consecutive failed logins after which the local user account is locked.  | 


