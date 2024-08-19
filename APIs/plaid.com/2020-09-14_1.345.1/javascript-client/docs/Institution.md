# ThePlaidApi.Institution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authMetadata** | [**AuthMetadata**](AuthMetadata.md) |  | [optional] 
**countryCodes** | [**[CountryCode]**](CountryCode.md) | A list of the country codes supported by the institution. | 
**dtcNumbers** | **[String]** | A partial list of DTC numbers associated with the institution. | [optional] 
**institutionId** | **String** | Unique identifier for the institution | 
**logo** | **String** | Base64 encoded representation of the institution&#39;s logo, returned as a base64 encoded 152x152 PNG. Not all institutions&#39; logos are available. | [optional] 
**name** | **String** | The official name of the institution | 
**oauth** | **Boolean** | Indicates that the institution has a mandatory OAuth login flow. Note that &#x60;oauth&#x60; may be &#x60;false&#x60; even for institutions that support OAuth, if the institution is in the process of migrating to OAuth and some active Items still exist that do not use OAuth. | 
**paymentInitiationMetadata** | [**PaymentInitiationMetadata**](PaymentInitiationMetadata.md) |  | [optional] 
**primaryColor** | **String** | Hexadecimal representation of the primary color used by the institution | [optional] 
**products** | [**[Products]**](Products.md) | A list of the Plaid products supported by the institution. Note that only institutions that support Instant Auth will return &#x60;auth&#x60; in the product array; institutions that do not list &#x60;auth&#x60; may still support other Auth methods such as Instant Match or Automated Micro-deposit Verification. To identify institutions that support those methods, use the &#x60;auth_metadata&#x60; object. For more details, see [Full Auth coverage](https://plaid.com/docs/auth/coverage/). | 
**routingNumbers** | **[String]** | A partial list of routing numbers associated with the institution. This list is provided for the purpose of looking up institutions by routing number. It is not comprehensive and should never be used as a complete list of routing numbers for an institution. | 
**status** | [**InstitutionStatus**](InstitutionStatus.md) |  | [optional] 
**url** | **String** | The URL for the institution&#39;s website | [optional] 


