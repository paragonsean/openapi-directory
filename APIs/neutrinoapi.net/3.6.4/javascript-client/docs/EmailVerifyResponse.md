# NeutrinoApi.EmailVerifyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **String** | The email domain | 
**domainError** | **Boolean** | True if this address has a domain error (e.g. no valid mail server records) | 
**email** | **String** | The email address. If you have used the fix-typos option then this will be the fixed address | 
**isCatchAll** | **Boolean** | True if this email domain has a catch-all policy (it will accept mail for any username) | 
**isDeferred** | **Boolean** | True if the mail server responded with a temporary failure (either a 4xx response code or unresponsive server). You can retry this address later, we recommend waiting at least 15 minutes before retrying | 
**isDisposable** | **Boolean** | True if this address is a disposable, temporary or darknet related email address | 
**isFreemail** | **Boolean** | True if this address is a free-mail address | 
**isPersonal** | **Boolean** | True if this address is for a person. False if this is a role based address, e.g. admin@, help@, office@, etc. | 
**provider** | **String** | The email service provider domain | 
**smtpResponse** | **String** | The raw SMTP response message received during verification | 
**smtpStatus** | **String** | The SMTP verification status for the address: &lt;br&gt; &lt;ul&gt; &lt;li&gt;ok - SMTP verification was successful, this is a real address that can receive mail&lt;/li&gt; &lt;li&gt;invalid - this is not a valid email address (has either a domain or syntax error)&lt;/li&gt; &lt;li&gt;absent - this address is not registered with the email service provider&lt;/li&gt; &lt;li&gt;unresponsive - the mail server(s) for this address timed-out or refused to open an SMTP connection&lt;/li&gt; &lt;li&gt;unknown - sorry, we could not reliably determine the real status of this address (this address may or may not exist)&lt;/li&gt; &lt;/ul&gt; | 
**syntaxError** | **Boolean** | True if this address has a syntax error | 
**typosFixed** | **Boolean** | True if typos have been fixed | 
**valid** | **Boolean** | Is this a valid email address (syntax and domain is valid) | 
**verified** | **Boolean** | True if this address has passed SMTP verification. Check the smtp-status and smtp-response fields for specific verification details | 


