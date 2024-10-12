# DracoonApi.LoginPasswordPolicies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characterRules** | [**CharacterRules**](CharacterRules.md) |  | 
**minLength** | **Number** | Minimum number of characters a password must contain | 
**numberOfArchivedPasswords** | **Number** | Number of passwords to archive  (must be between &#x60;0&#x60; and &#x60;10&#x60;; &#x60;0&#x60; means that password history is disabled) | 
**passwordExpiration** | [**PasswordExpiration**](PasswordExpiration.md) |  | 
**rejectDictionaryWords** | **Boolean** | Determines whether a password must NOT contain word(s) from a dictionary | 
**rejectKeyboardPatterns** | **Boolean** | Determines whether a password must NOT contain keyboard patterns (e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60;)  (min. 4 character pattern) | 
**rejectUserInfo** | **Boolean** | Determines whether a password must NOT contain user info (first name, last name, email, user name) | 
**updatedAt** | **Date** | Modification date | 
**updatedBy** | [**UserInfo**](UserInfo.md) |  | 
**userLockout** | [**UserLockout**](UserLockout.md) |  | 


