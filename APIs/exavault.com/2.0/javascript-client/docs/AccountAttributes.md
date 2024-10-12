# ExaVault.AccountAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | Name of the account | [optional] 
**accountOnboarding** | **Boolean** | Whether the web application onboarding help is enabled for new users in the account. | [optional] 
**allowedIp** | [**[AccountAttributesAllowedIpInner]**](AccountAttributesAllowedIpInner.md) | Range of IP addresses allowed to access this account. | [optional] 
**branding** | **Boolean** | Branding flag. Set to &#x60;true&#x60; if the account has branding functionality enabled. | [optional] 
**brandingSettings** | [**BrandingSettings**](BrandingSettings.md) |  | [optional] 
**clientId** | **Number** | (ExaVault Use Only) Internal ID of the account in CMS. | [optional] 
**complexPasswords** | **Boolean** | Flag to indicate whether the account requires complex passwords. Set to &#x60;true&#x60; to require complex passwords on all users and shares. | [optional] 
**created** | **Date** | Timestamp of account creation. | [optional] 
**customDomain** | **Boolean** | Custom domain flag. Set to &#x60;true&#x60; if account type allows custom domain functionality. | [optional] 
**customSignature** | **String** | Custom signature for all account emails users or recipients will receive. | [optional] 
**externalDomains** | **[String]** | Custom domain used to brand this account. | [optional] 
**maxUsers** | **Number** | Maximum number of users the account can have. This can be increased by contacting ExaVault Support. | [optional] 
**modified** | **Date** | Timestamp of account modification. | [optional] 
**planDetails** | [**PlanDetails**](PlanDetails.md) |  | [optional] 
**quota** | [**Quota**](Quota.md) |  | [optional] 
**secureOnly** | **Boolean** | Flag to indicate whether the account disables connections via insecure protocols (e.g. FTP). Set to &#x60;true&#x60; to disable all traffic over port 21. | [optional] 
**showReferralLinks** | **Boolean** | Flag to indicate showing of referrals links in the account. Set to &#x60;true&#x60; to include marketing messages in share invitations. | [optional] 
**status** | **Number** | Account status flag. A one (1) means the account is active; zero (0) means it is suspended. | [optional] 
**userCount** | **Number** | Current number of users on the account. | [optional] 
**welcomeEmailContent** | **String** | Content of welcome email each new user will receive. | [optional] 
**welcomeEmailSubject** | **String** | Subject of welcome email each new user will receive. | [optional] 



## Enum: StatusEnum


* `1` (value: `1`)

* `0` (value: `0`)




