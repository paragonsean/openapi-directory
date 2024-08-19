# ActiveDocumentationForV1.Topups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount, in cents, of the product you are purchasing. &#39;500&#39; &#x3D; $5.00 | [optional] 
**carrierCode** | **String** | Name of the mobile carrier. &#39;Claro&#39; | [optional] [default to &#39;Claro&#39;]
**clientTransactionId** | **String** | UNIQUE 15 char ID you use to track topups. &#39;trans0123456789&#39; | [optional] [default to &#39;&#39;]
**countryCode** | **String** | 2-digit code of the country in ISO 3166 format. &#39;GT&#39; | [optional] [default to &#39;GT&#39;]
**mobileNumber** | **String** | Mobile number to topup. VALIDATE prior to submission. &#39;50231234567&#39; | [optional] [default to &#39;50231234567&#39;]
**plan** | **String** | The Application plan being used. Case-sensitive. &#39;Sandbox&#39; or &#39;Production&#39; | [optional] [default to &#39;Sandbox&#39;]
**productCode** | **String** | Optional code to distinguish one particular product from another. &#39;76560&#39; | [optional] [default to &#39;&#39;]
**terminalId** | **String** | ID for the Terminal used to perform the topup. &#39;Kiosk 5&#39; | [optional] [default to &#39;Kiosk 5&#39;]


