

# EncryptionPasswordPolicies

Encryption password policies

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**characterRules** | [**CharacterRules**](CharacterRules.md) |  |  [optional] |
|**minLength** | **Integer** | Minimum number of characters a password must contain |  [optional] |
|**rejectKeyboardPatterns** | **Boolean** | Determines whether a password must NOT contain keyboard patterns (e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60;)  (min. 4 character pattern) |  [optional] |
|**rejectUserInfo** | **Boolean** | Determines whether a password must NOT contain user info (first name, last name, email, user name) |  [optional] |
|**updatedAt** | **OffsetDateTime** | Modification date |  [optional] |
|**updatedBy** | [**UserInfo**](UserInfo.md) |  |  [optional] |



