# DracoonApi.UpdateLoginPasswordPolicies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characterRules** | [**CharacterRules**](CharacterRules.md) |  | [optional] 
**enforceLoginPasswordChange** | **Boolean** | &amp;#128679; Deprecated since v4.24.0  Determines whether a login password change should be enforced for all users  Only takes effect, if login password policies get stricter | [optional] [default to false]
**minLength** | **Number** | Minimum number of characters a password must contain | [optional] 
**numberOfArchivedPasswords** | **Number** | Number of passwords to archive  (must be between &#x60;0&#x60; and &#x60;10&#x60;; &#x60;0&#x60; means that password history is disabled) | [optional] 
**passwordExpiration** | [**PasswordExpiration**](PasswordExpiration.md) |  | [optional] 
**rejectDictionaryWords** | **Boolean** | Determines whether a password must NOT contain word(s) from a dictionary | [optional] 
**rejectKeyboardPatterns** | **Boolean** | Determines whether a password must NOT contain keyboard patterns (e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60;)  (min. 4 character pattern) | [optional] 
**rejectUserInfo** | **Boolean** | Determines whether a password must NOT contain user info (first name, last name, email, user name) | [optional] 
**userLockout** | [**UserLockout**](UserLockout.md) |  | [optional] 


