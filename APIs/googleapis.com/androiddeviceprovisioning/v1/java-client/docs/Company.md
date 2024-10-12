

# Company

A reseller, vendor, or customer in the zero-touch reseller and customer APIs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminEmails** | **List&lt;String&gt;** | Optional. Email address of customer&#39;s users in the admin role. Each email address must be associated with a Google Account. |  [optional] |
|**companyId** | **String** | Output only. The ID of the company. Assigned by the server. |  [optional] [readonly] |
|**companyName** | **String** | Required. The name of the company. For example _XYZ Corp_. Displayed to the company&#39;s employees in the zero-touch enrollment portal. |  [optional] |
|**googleWorkspaceAccount** | [**GoogleWorkspaceAccount**](GoogleWorkspaceAccount.md) |  |  [optional] |
|**languageCode** | **String** | Input only. The preferred locale of the customer represented as a BCP47 language code. This field is validated on input and requests containing unsupported language codes will be rejected. Supported language codes: Arabic (ar) Chinese (Hong Kong) (zh-HK) Chinese (Simplified) (zh-CN) Chinese (Traditional) (zh-TW) Czech (cs) Danish (da) Dutch (nl) English (UK) (en-GB) English (US) (en-US) Filipino (fil) Finnish (fi) French (fr) German (de) Hebrew (iw) Hindi (hi) Hungarian (hu) Indonesian (id) Italian (it) Japanese (ja) Korean (ko) Norwegian (Bokmal) (no) Polish (pl) Portuguese (Brazil) (pt-BR) Portuguese (Portugal) (pt-PT) Russian (ru) Spanish (es) Spanish (Latin America) (es-419) Swedish (sv) Thai (th) Turkish (tr) Ukrainian (uk) Vietnamese (vi) |  [optional] |
|**name** | **String** | Output only. The API resource name of the company. The resource name is one of the following formats: * &#x60;partners/[PARTNER_ID]/customers/[CUSTOMER_ID]&#x60; * &#x60;partners/[PARTNER_ID]/vendors/[VENDOR_ID]&#x60; * &#x60;partners/[PARTNER_ID]/vendors/[VENDOR_ID]/customers/[CUSTOMER_ID]&#x60; Assigned by the server. |  [optional] [readonly] |
|**ownerEmails** | **List&lt;String&gt;** | Required. Input only. Email address of customer&#39;s users in the owner role. At least one &#x60;owner_email&#x60; is required. Owners share the same access as admins but can also add, delete, and edit your organization&#39;s portal users. |  [optional] |
|**skipWelcomeEmail** | **Boolean** | Input only. If set to true, welcome email will not be sent to the customer. It is recommended to skip the welcome email if devices will be claimed with additional DEVICE_PROTECTION service, as the customer will receive separate emails at device claim time. This field is ignored if this is not a Zero-touch customer. |  [optional] |
|**termsStatus** | [**TermsStatusEnum**](#TermsStatusEnum) | Output only. Whether any user from the company has accepted the latest Terms of Service (ToS). See TermsStatus. |  [optional] [readonly] |



## Enum: TermsStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TERMS_STATUS_UNSPECIFIED&quot; |
| NOT_ACCEPTED | &quot;TERMS_STATUS_NOT_ACCEPTED&quot; |
| ACCEPTED | &quot;TERMS_STATUS_ACCEPTED&quot; |
| STALE | &quot;TERMS_STATUS_STALE&quot; |



