# ManagementApi.CreateCompanyApiCredentialRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedOrigins** | **[String]** | List of [allowed origins](https://docs.adyen.com/development-resources/client-side-authentication#allowed-origins) for the new API credential. | [optional] 
**associatedMerchantAccounts** | **[String]** | List of merchant accounts that the API credential has access to. | [optional] 
**description** | **String** | Description of the API credential. | [optional] 
**roles** | **[String]** | List of [roles](https://docs.adyen.com/development-resources/api-credentials#roles-1) for the API credential. Only roles assigned to &#39;ws@Company.&lt;CompanyName&gt;&#39; can be assigned to other API credentials. | [optional] 


