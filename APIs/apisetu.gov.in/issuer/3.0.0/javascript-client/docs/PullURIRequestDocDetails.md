# DigiLockerIssuerApis.PullURIRequestDocDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DOB** | **[Object]** | Date of birth of the DigiLocker user searching for the document/certificate as on Aadhaar in DD-MM-YYYY format. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. | 
**digiLockerId** | **[Object]** | A unique 36 character DigiLocker Id of the user account. | 
**docType** | **[Object]** | Digital Locker will pass the document type being searched in this parameter. | 
**fullName** | **[Object]** | Name of the DigiLocker user searching for the document/certificate as on Aadhaar. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. | 
**photo** | **[Object]** | The base 64 encoded contents of JPEG photograph as on Aadhaar. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. | 
**uDF1** | **[Object]** | User defined search parameters to search a unique document/certificate. The &lt;UDF&gt; may be &lt;RollNo&gt; for CBSE, &lt;RegistrationNo&gt; for Transportation Dept. and &lt;PAN&gt; for Income Tax Dept. The search parameters for the API will be configured in the issuer portal of Digital Locker while configuring this API. | 
**uDF2** | **[Object]** |  | 
**uDF3** | **[Object]** |  | 
**uDFn** | **[Object]** |  | 
**UID** | **[Object]** | Aadhaar number of the DigiLocker user searching for the document/certificate. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. | 


