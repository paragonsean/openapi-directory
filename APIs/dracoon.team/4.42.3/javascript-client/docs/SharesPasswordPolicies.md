# DracoonApi.SharesPasswordPolicies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**characterRules** | [**CharacterRules**](CharacterRules.md) |  | [optional] 
**minLength** | **Number** | Minimum number of characters a password must contain | [optional] 
**rejectDictionaryWords** | **Boolean** | Determines whether a password must NOT contain word(s) from a dictionary | [optional] 
**rejectKeyboardPatterns** | **Boolean** | Determines whether a password must NOT contain keyboard patterns (e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60;)  (min. 4 character pattern) | [optional] 
**rejectUserInfo** | **Boolean** | Determines whether a password must NOT contain user info (first name, last name, email, user name) | [optional] 
**updatedAt** | **Date** | Modification date | [optional] 
**updatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 


