# ThePlaidApi.PartnerCustomerCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**PartnerEndCustomerAddress**](PartnerEndCustomerAddress.md) |  | 
**applicationName** | **String** | The name of the end customer&#39;s application. This will be shown to end users when they go through the Plaid Link flow. | 
**assetsUnderManagement** | [**PartnerEndCustomerAssetsUnderManagement**](PartnerEndCustomerAssetsUnderManagement.md) |  | [optional] 
**billingContact** | [**PartnerEndCustomerBillingContact**](PartnerEndCustomerBillingContact.md) |  | [optional] 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**companyName** | **String** | The company name of the end customer being created. This will be used to display the end customer in the Plaid Dashboard. It will not be shown to end users. | 
**createLinkCustomization** | **Boolean** | If &#x60;true&#x60;, the end customer&#39;s default Link customization will be set to match the partner&#39;s. You can always change the end customer&#39;s Link customization in the Plaid Dashboard. See the [Link Customization docs](https://plaid.com/docs/link/customization/) for more information. | [optional] 
**customerSupportInfo** | [**PartnerEndCustomerCustomerSupportInfo**](PartnerEndCustomerCustomerSupportInfo.md) |  | [optional] 
**isBankAddendumCompleted** | **Boolean** | Denotes whether the partner has forwarded the Plaid bank addendum to the end customer. | 
**isDiligenceAttested** | **Boolean** | Denotes whether or not the partner has completed attestation of diligence for the end customer to be created. | 
**legalEntityName** | **String** | The end customer&#39;s legal name. This will be shared with financial institutions as part of the OAuth registration process. It will not be shown to end users. | 
**logo** | **String** | Base64-encoded representation of the end customer&#39;s logo. Must be a PNG of size 1024x1024 under 4MB. The logo will be shared with financial institutions and shown to the end user during Link flows. A logo is required if &#x60;create_link_customization&#x60; is &#x60;true&#x60;. If &#x60;create_link_customization&#x60; is &#x60;false&#x60; and the logo is omitted, a stock logo will be used. | [optional] 
**products** | [**[Products]**](Products.md) | The products to be enabled for the end customer. | 
**redirectUris** | **[String]** | A list of URIs indicating the destination(s) where a user can be forwarded after completing the Link flow; used to support OAuth authentication flows when launching Link in the browser or via a webview. URIs should not contain any query parameters. When used in Production or Development, URIs must use https. To specify any subdomain, use &#x60;*&#x60; as a wildcard character, e.g. &#x60;https://_*.example.com/oauth.html&#x60;. To modify redirect URIs for an end customer after creating them, go to the end customer&#39;s [API page](https://dashboard.plaid.com/team/api) in the Dashboard. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**technicalContact** | [**PartnerEndCustomerTechnicalContact**](PartnerEndCustomerTechnicalContact.md) |  | [optional] 
**website** | **String** | The end customer&#39;s website. | 


