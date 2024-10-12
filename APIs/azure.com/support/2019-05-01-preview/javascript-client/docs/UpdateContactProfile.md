# MicrosoftSupport.UpdateContactProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalEmailAddresses** | **[String]** | Email addresses listed will be copied on any correspondence about the support ticket | [optional] 
**country** | **String** | Country of the user. This is the ISO 3166-1 alpha-3 code. | [optional] 
**firstName** | **String** | First name | [optional] 
**lastName** | **String** | Last name | [optional] 
**phoneNumber** | **String** | Phone number. This is required if preferred contact method is phone. | [optional] 
**preferredContactMethod** | **String** | Preferred contact method | [optional] 
**preferredSupportLanguage** | **String** | Preferred language of support from Azure. Support languages vary based on the severity you choose for your support ticket. Learn more at &lt;a  target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://azure.microsoft.com/support/plans/response/&#39;&gt;Azure Severity and responsiveness&lt;/a&gt;. Use the standard language-country code. Valid values are &#39;en-us&#39; for English, &#39;zh-hans&#39; for Chinese, &#39;es-es&#39; for Spanish, &#39;fr-fr&#39; for French, &#39;ja-jp&#39; for Japanese, &#39;ko-kr&#39; for Korean, &#39;ru-ru&#39; for Russian, &#39;pt-br&#39; for Portuguese, &#39;it-it&#39; for Italian, &#39;zh-tw&#39; for Chinese and &#39;de-de&#39; for German. | [optional] 
**preferredTimeZone** | **String** | Time zone of the user. This is the name of the time zone from &lt;a  target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://support.microsoft.com/en-us/help/973627/microsoft-time-zone-index-values&#39;&gt;Microsoft Time Zone Index Values&lt;/a&gt;. | [optional] 
**primaryEmailAddress** | **String** | Primary email address | [optional] 



## Enum: PreferredContactMethodEnum


* `email` (value: `"email"`)

* `phone` (value: `"phone"`)




