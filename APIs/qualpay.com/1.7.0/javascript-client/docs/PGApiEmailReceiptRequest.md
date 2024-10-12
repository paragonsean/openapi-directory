# QualpayPaymentGatewayApi.PGApiEmailReceiptRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**developerId** | **String** | &lt;strong&gt;Format: &lt;/strong&gt;Variable length, up to 32 AN&lt;br&gt;&lt;strong&gt;Description: &lt;/strong&gt;Use to indicate which company developed the integration to Qualpay or the name of the payment solution that is connected to Qualpay.  Suggested usage is softwareABCv1.0 or companyXYZv2.0.  | [optional] 
**emailAddress** | **[String]** |  AN&lt;br&gt;&lt;strong&gt;Description: &lt;/strong&gt;An array of email addresses to which the transaction receipt should be sent to.  | 
**logoUrl** | **String** |  AN&lt;br&gt;&lt;strong&gt;Description: &lt;/strong&gt;A link to the logo image that will be included in the transaction receipt.  | [optional] 
**merchantId** | **Number** | &lt;strong&gt;Format: &lt;/strong&gt;Variable length, up to 12 N&lt;br&gt;&lt;strong&gt;Description: &lt;/strong&gt;Unique identifier on the Qualpay system. | 
**vendorId** | **Number** | &lt;strong&gt;Format: &lt;/strong&gt;Variable length, up to 12 N&lt;br&gt;&lt;strong&gt;Description: &lt;/strong&gt;Identifies the vendor to which this email receipt request applies. | [optional] 


