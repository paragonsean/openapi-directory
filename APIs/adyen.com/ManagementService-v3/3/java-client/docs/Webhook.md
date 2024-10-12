

# Webhook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**WebhookLinks**](WebhookLinks.md) | References to resources connected with this webhook. |  [optional] |
|**acceptsExpiredCertificate** | **Boolean** | Indicates if expired SSL certificates are accepted. Default value: **false**. |  [optional] |
|**acceptsSelfSignedCertificate** | **Boolean** | Indicates if self-signed SSL certificates are accepted. Default value: **false**. |  [optional] |
|**acceptsUntrustedRootCertificate** | **Boolean** | Indicates if untrusted SSL certificates are accepted. Default value: **false**. |  [optional] |
|**accountReference** | **String** | Reference to the account the webook is set on. |  [optional] |
|**active** | **Boolean** | Indicates if the webhook configuration is active. The field must be **true** for you to receive webhooks about events related an account. |  |
|**additionalSettings** | [**AdditionalSettingsResponse**](AdditionalSettingsResponse.md) | Additional shopper and transaction information to be included in your [standard notifications](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes). Find out more about the available [additional settings](https://docs.adyen.com/development-resources/webhooks/additional-settings). |  [optional] |
|**certificateAlias** | **String** | The alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will match this alias. |  [optional] |
|**communicationFormat** | [**CommunicationFormatEnum**](#CommunicationFormatEnum) | Format or protocol for receiving webhooks. Possible values: * **soap** * **http** * **json**  |  |
|**description** | **String** | Your description for this webhook configuration. |  [optional] |
|**encryptionProtocol** | [**EncryptionProtocolEnum**](#EncryptionProtocolEnum) | SSL version to access the public webhook URL specified in the &#x60;url&#x60; field. Possible values: * **TLSv1.3** * **TLSv1.2** * **HTTP** - Only allowed on Test environment.  If not specified, the webhook will use &#x60;sslVersion&#x60;: **TLSv1.2**. |  [optional] |
|**filterMerchantAccountType** | [**FilterMerchantAccountTypeEnum**](#FilterMerchantAccountTypeEnum) | Shows how merchant accounts are included in company-level webhooks. Possible values: * **includeAccounts** * **excludeAccounts** * **allAccounts**: Includes all merchant accounts, and does not require specifying &#x60;filterMerchantAccounts&#x60;. |  [optional] |
|**filterMerchantAccounts** | **List&lt;String&gt;** | A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for &#x60;filterMerchantAccountType&#x60;.  Required if &#x60;filterMerchantAccountType&#x60; is either: * **includeAccounts** * **excludeAccounts**  Not needed for &#x60;filterMerchantAccountType&#x60;: **allAccounts**. |  [optional] |
|**hasError** | **Boolean** | Indicates if the webhook configuration has errors that need troubleshooting. If the value is **true**, troubleshoot the configuration using the [testing endpoint](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookid}/test). |  [optional] |
|**hasPassword** | **Boolean** | Indicates if the webhook is password protected. |  [optional] |
|**hmacKeyCheckValue** | **String** | The [checksum](https://en.wikipedia.org/wiki/Key_checksum_value) of the HMAC key generated for this webhook. You can use this value to uniquely identify the HMAC key configured for this webhook. |  [optional] |
|**id** | **String** | Unique identifier for this webhook. |  [optional] |
|**networkType** | [**NetworkTypeEnum**](#NetworkTypeEnum) | Network type for Terminal API details webhooks. |  [optional] |
|**populateSoapActionHeader** | **Boolean** | Indicates if the SOAP action header needs to be populated. Default value: **false**.  Only applies if &#x60;communicationFormat&#x60;: **soap**. |  [optional] |
|**type** | **String** | The type of webhook. Possible values are:  - **standard** - **account-settings-notification** - **banktransfer-notification** - **boletobancario-notification** - **directdebit-notification** - **ach-notification-of-change-notification** - **pending-notification** - **ideal-notification** - **ideal-pending-notification** - **report-notification** - **terminal-api-notification**  Find out more about [standard notification webhooks](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes) and [other types of notifications](https://docs.adyen.com/development-resources/webhooks/understand-notifications#other-notifications). |  |
|**url** | **String** | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. |  |
|**username** | **String** | Username to access the webhook URL. |  [optional] |



## Enum: CommunicationFormatEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| JSON | &quot;json&quot; |
| SOAP | &quot;soap&quot; |



## Enum: EncryptionProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;HTTP&quot; |
| TLSV1_2 | &quot;TLSv1.2&quot; |
| TLSV1_3 | &quot;TLSv1.3&quot; |



## Enum: FilterMerchantAccountTypeEnum

| Name | Value |
|---- | -----|
| ALL_ACCOUNTS | &quot;allAccounts&quot; |
| EXCLUDE_ACCOUNTS | &quot;excludeAccounts&quot; |
| INCLUDE_ACCOUNTS | &quot;includeAccounts&quot; |



## Enum: NetworkTypeEnum

| Name | Value |
|---- | -----|
| LOCAL | &quot;local&quot; |
| PUBLIC | &quot;public&quot; |



