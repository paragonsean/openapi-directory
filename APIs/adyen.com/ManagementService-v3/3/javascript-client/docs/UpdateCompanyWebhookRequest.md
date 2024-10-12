# ManagementApi.UpdateCompanyWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptsExpiredCertificate** | **Boolean** | Indicates if expired SSL certificates are accepted. Default value: **false**. | [optional] 
**acceptsSelfSignedCertificate** | **Boolean** | Indicates if self-signed SSL certificates are accepted. Default value: **false**. | [optional] 
**acceptsUntrustedRootCertificate** | **Boolean** | Indicates if untrusted SSL certificates are accepted. Default value: **false**. | [optional] 
**active** | **Boolean** | Indicates if the webhook configuration is active. The field must be **true** for us to send webhooks about events related an account. | [optional] 
**additionalSettings** | [**AdditionalSettings**](AdditionalSettings.md) | Additional shopper and transaction information to be included in your [standard notifications](https://docs.adyen.com/development-resources/webhooks/understand-notifications#event-codes). Find out more about the available [additional settings](https://docs.adyen.com/development-resources/webhooks/additional-settings). | [optional] 
**communicationFormat** | **String** | Format or protocol for receiving webhooks. Possible values: * **soap** * **http** * **json**  | [optional] 
**description** | **String** | Your description for this webhook configuration. | [optional] 
**encryptionProtocol** | **String** | SSL version to access the public webhook URL specified in the &#x60;url&#x60; field. Possible values: * **TLSv1.3** * **TLSv1.2** * **HTTP** - Only allowed on Test environment.  If not specified, the webhook will use &#x60;sslVersion&#x60;: **TLSv1.2**. | [optional] 
**filterMerchantAccountType** | **String** | Shows how merchant accounts are filtered when configuring the webhook. Possible values: * **includeAccounts**: The webhook is configured for the merchant accounts listed in &#x60;filterMerchantAccounts&#x60;. * **excludeAccounts**: The webhook is not configured for the merchant accounts listed in &#x60;filterMerchantAccounts&#x60;. * **allAccounts**: Includes all merchant accounts, and does not require specifying &#x60;filterMerchantAccounts&#x60;. | [optional] 
**filterMerchantAccounts** | **[String]** | A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined for &#x60;filterMerchantAccountType&#x60;.  Required if &#x60;filterMerchantAccountType&#x60; is either: * **includeAccounts** * **excludeAccounts**  Not needed for &#x60;filterMerchantAccountType&#x60;: **allAccounts**. | [optional] 
**networkType** | **String** | Network type for Terminal API notification webhooks. Possible values: * **public** * **local**  Default Value: **public**. | [optional] 
**password** | **String** | Password to access the webhook URL. | [optional] 
**populateSoapActionHeader** | **Boolean** | Indicates if the SOAP action header needs to be populated. Default value: **false**.  Only applies if &#x60;communicationFormat&#x60;: **soap**. | [optional] 
**url** | **String** | Public URL where webhooks will be sent, for example **https://www.domain.com/webhook-endpoint**. | [optional] 
**username** | **String** | Username to access the webhook URL. | [optional] 



## Enum: CommunicationFormatEnum


* `http` (value: `"http"`)

* `json` (value: `"json"`)

* `soap` (value: `"soap"`)





## Enum: EncryptionProtocolEnum


* `HTTP` (value: `"HTTP"`)

* `TLSv1.2` (value: `"TLSv1.2"`)

* `TLSv1.3` (value: `"TLSv1.3"`)





## Enum: FilterMerchantAccountTypeEnum


* `allAccounts` (value: `"allAccounts"`)

* `excludeAccounts` (value: `"excludeAccounts"`)

* `includeAccounts` (value: `"includeAccounts"`)





## Enum: NetworkTypeEnum


* `local` (value: `"local"`)

* `public` (value: `"public"`)




