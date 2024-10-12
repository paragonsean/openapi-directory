# AmazonSimpleEmailService.PutAccountDetailsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailType** | **String** | The type of email your account will send. | 
**websiteURL** | **String** | The URL of your website. This information helps us better understand the type of content that you plan to send. | 
**contactLanguage** | **String** | The language you would prefer to be contacted with. | [optional] 
**useCaseDescription** | **String** | A description of the types of email that you plan to send. | 
**additionalContactEmailAddresses** | **[String]** | Additional email addresses that you would like to be notified regarding Amazon SES matters. | [optional] 
**productionAccessEnabled** | **Boolean** | &lt;p&gt;Indicates whether or not your account should have production access in the current Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;If the value is &lt;code&gt;false&lt;/code&gt;, then your account is in the &lt;i&gt;sandbox&lt;/i&gt;. When your account is in the sandbox, you can only send email to verified identities. Additionally, the maximum number of emails you can send in a 24-hour period (your sending quota) is 200, and the maximum number of emails you can send per second (your maximum sending rate) is 1.&lt;/p&gt; &lt;p&gt;If the value is &lt;code&gt;true&lt;/code&gt;, then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.&lt;/p&gt; | [optional] 



## Enum: MailTypeEnum


* `MARKETING` (value: `"MARKETING"`)

* `TRANSACTIONAL` (value: `"TRANSACTIONAL"`)





## Enum: ContactLanguageEnum


* `EN` (value: `"EN"`)

* `JA` (value: `"JA"`)




