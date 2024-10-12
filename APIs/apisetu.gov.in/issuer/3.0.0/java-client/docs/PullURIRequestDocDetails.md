

# PullURIRequestDocDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**DOB** | **List&lt;Object&gt;** | Date of birth of the DigiLocker user searching for the document/certificate as on Aadhaar in DD-MM-YYYY format. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. |  |
|**digiLockerId** | **List&lt;Object&gt;** | A unique 36 character DigiLocker Id of the user account. |  |
|**docType** | **List&lt;Object&gt;** | Digital Locker will pass the document type being searched in this parameter. |  |
|**fullName** | **List&lt;Object&gt;** | Name of the DigiLocker user searching for the document/certificate as on Aadhaar. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. |  |
|**photo** | **List&lt;Object&gt;** | The base 64 encoded contents of JPEG photograph as on Aadhaar. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. |  |
|**UDF1** | **List&lt;Object&gt;** | User defined search parameters to search a unique document/certificate. The &lt;UDF&gt; may be &lt;RollNo&gt; for CBSE, &lt;RegistrationNo&gt; for Transportation Dept. and &lt;PAN&gt; for Income Tax Dept. The search parameters for the API will be configured in the issuer portal of Digital Locker while configuring this API. |  |
|**UDF2** | **List&lt;Object&gt;** |  |  |
|**UDF3** | **List&lt;Object&gt;** |  |  |
|**udFn** | **List&lt;Object&gt;** |  |  |
|**UID** | **List&lt;Object&gt;** | Aadhaar number of the DigiLocker user searching for the document/certificate. This is an optional parameter and will be sent only if the issuer opts for it while configuring the API on Digital Locker Issuer Portal. |  |



