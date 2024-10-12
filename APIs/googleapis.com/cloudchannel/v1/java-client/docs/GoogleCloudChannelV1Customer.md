

# GoogleCloudChannelV1Customer

Entity representing a customer of a reseller or distributor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateEmail** | **String** | Secondary contact email. You need to provide an alternate email to create different domains if a primary contact email already exists. Users will receive a notification with credentials when you create an admin.google.com account. Secondary emails are also recovery email addresses. Alternate emails are optional when you create Team customers. |  [optional] |
|**channelPartnerId** | **String** | Cloud Identity ID of the customer&#39;s channel partner. Populated only if a channel partner exists for this customer. |  [optional] |
|**cloudIdentityId** | **String** | Output only. The customer&#39;s Cloud Identity ID if the customer has a Cloud Identity resource. |  [optional] [readonly] |
|**cloudIdentityInfo** | [**GoogleCloudChannelV1CloudIdentityInfo**](GoogleCloudChannelV1CloudIdentityInfo.md) |  |  [optional] |
|**correlationId** | **String** | Optional. External CRM ID for the customer. Populated only if a CRM ID exists for this customer. |  [optional] |
|**createTime** | **String** | Output only. Time when the customer was created. |  [optional] [readonly] |
|**domain** | **String** | Required. The customer&#39;s primary domain. Must match the primary contact email&#39;s domain. |  [optional] |
|**languageCode** | **String** | Optional. The BCP-47 language code, such as \&quot;en-US\&quot; or \&quot;sr-Latn\&quot;. For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. |  [optional] |
|**name** | **String** | Output only. Resource name of the customer. Format: accounts/{account_id}/customers/{customer_id} |  [optional] [readonly] |
|**orgDisplayName** | **String** | Required. Name of the organization that the customer entity represents. |  [optional] |
|**orgPostalAddress** | [**GoogleTypePostalAddress**](GoogleTypePostalAddress.md) |  |  [optional] |
|**primaryContactInfo** | [**GoogleCloudChannelV1ContactInfo**](GoogleCloudChannelV1ContactInfo.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Time when the customer was updated. |  [optional] [readonly] |



