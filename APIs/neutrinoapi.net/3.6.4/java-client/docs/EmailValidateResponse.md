

# EmailValidateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | **String** | The email domain |  |
|**domainError** | **Boolean** | True if this address has a domain error (e.g. no valid mail server records) |  |
|**email** | **String** | The email address. If you have used the fix-typos option then this will be the fixed address |  |
|**isDisposable** | **Boolean** | True if this address is a disposable, temporary or darknet related email address |  |
|**isFreemail** | **Boolean** | True if this address is a free-mail address |  |
|**isPersonal** | **Boolean** | True if this address belongs to a person. False if this is a role based address, e.g. admin@, help@, office@, etc. |  |
|**provider** | **String** | The email service provider domain |  |
|**syntaxError** | **Boolean** | True if this address has a syntax error |  |
|**typosFixed** | **Boolean** | True if typos have been fixed |  |
|**valid** | **Boolean** | Is this a valid email |  |



