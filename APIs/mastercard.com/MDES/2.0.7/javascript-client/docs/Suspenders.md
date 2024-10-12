# MdesCustomerService.Suspenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suspender** | **[String]** | Suspender(s) of the token when the token current status is SUSPENDED. Conditional field, only present when token mapping is suspended. Valid values:&lt;br /&gt;    \&quot;I\&quot; - The issuer has requested token suspension.&lt;br /&gt;    \&quot;W\&quot; - Token Requestor (including Wallet Provider) has requested token suspension.&lt;br /&gt;    \&quot;C\&quot; - The cardholder has requested token suspension.&lt;br /&gt;    \&quot;P\&quot; - The Mobile PIN Validation service has requested token suspension. Occurs when the cardholder has entered their Mobile PIN incorrectly too many times whilst performing a transaction.&lt;br /&gt;    \&quot;M\&quot; - The Mobile PIN Change Validation service has requested token suspension. Occurs when the cardholder has entered their Mobile PIN incorrectly too many times whilst changing their mobile pin. | [optional] 


