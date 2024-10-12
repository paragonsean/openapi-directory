# ThePlaidApi.InstitutionsGetRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includeAuthMetadata** | **Boolean** | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional] [default to false]
**includeOptionalMetadata** | **Boolean** | When &#x60;true&#x60;, return the institution&#39;s homepage URL, logo and primary brand color.  Note that Plaid does not own any of the logos shared by the API, and that by accessing or using these logos, you agree that you are doing so at your own risk and will, if necessary, obtain all required permissions from the appropriate rights holders and adhere to any applicable usage guidelines. Plaid disclaims all express or implied warranties with respect to the logos. | [optional] 
**includePaymentInitiationMetadata** | **Boolean** | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional] [default to false]
**oauth** | **Boolean** | Limit results to institutions with or without mandatory OAuth login flows. Note that institutions will only have &#x60;oauth&#x60; set to &#x60;true&#x60; if *all* Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth may have the &#x60;oauth&#x60; attribute set to &#x60;false&#x60; even if they support OAuth. | [optional] 
**products** | [**[Products]**](Products.md) | Filter the Institutions based on which products they support.  | [optional] 
**routingNumbers** | **[String]** | Specify an array of routing numbers to filter institutions. The response will only return institutions that match all of the routing numbers in the array. Routing number records used for this matching are not comprehensive; failure to match a given routing number to an institution does not mean that the institution is unsupported by Plaid. | [optional] 


