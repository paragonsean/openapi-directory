# paylocity_api

PaylocityApi - JavaScript client for paylocity_api
For general questions and support of the API, contact: webservices@paylocity.com
# Overview

Paylocity Web Services API is an externally facing RESTful Internet protocol. The Paylocity API uses HTTP verbs and a RESTful endpoint structure. OAuth 2.0 is used as the API Authorization framework. Request and response payloads are formatted as JSON.
Paylocity supports v1 and v2 versions of its API endpoints. v1, while supported, won't be enhanced with additional functionality. For direct link to v1 documentation, please click [here](https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm). For additional resources regarding v1/v2 differences and conversion path, please contact webservices@paylocity.com.

##### Setup

Paylocity will provide the secure client credentials and set up the scope (type of requests and allowed company numbers). You will receive the unique client id, secret, and Paylocity public key for the data encryption. The secret will expire in 365 days. 
* Paylocity will send you an e-mail 10 days prior to the expiration date for the current secret. If not renewed, the second e-mail notification will be sent 5 days prior to secret's expiration. Each email will contain the code necessary to renew the client secret. 
* You can obtain the new secret by calling API endpoint using your current not yet expired credentials and the code that was sent with the notification email. For details on API endpoint, please see Client Credentials section. 
* Both the current secret value and the new secret value will be recognized during the transition period. After the current secret expires, you must use the new secret. 
* If you were unable to renew the secret via API endpoint, you can still contact Service and they will email you new secret via secure email.


When validating the request, Paylocity API will honor the defaults and required fields set up for the company default New Hire Template as defined in Web Pay.


# Authorization

Paylocity Web Services API uses OAuth2.0 Authentication with JSON Message Format.


All requests of the Paylocity Web Services API require a bearer token which can be obtained by authenticating the client with the Paylocity Web Services API via OAuth 2.0.


The client must request a bearer token from the authorization endpoint:


auth-server for production: https://api.paylocity.com/IdentityServer/connect/token


auth-server for testing: https://apisandbox.paylocity.com/IdentityServer/connect/token

Paylocity reserves the right to impose rate limits on the number of calls made to our APIs. Changes to API features/functionality may be made at anytime with or without prior notice.

##### Authorization Header

The request is expected to be in the form of a basic authentication request, with the \"Authorization\" header containing the client-id and client-secret. This means the standard base-64 encoded user:password, prefixed with \"Basic\" as the value for the Authorization header, where user is the client-id and password is the client-secret.

##### Content-Type Header

The \"Content-Type\" header is required to be \"application/x-www-form-urlencoded\".

##### Additional Values

The request must post the following form encoded values within the request body:

    grant_type = client_credentials
    scope = WebLinkAPI

##### Responses

Success will return HTTP 200 OK with JSON content:

    {
      \"access_token\": \"xxx\",
      \"expires_in\": 3600,
      \"token_type\": \"Bearer\"
    }

# Encryption

Paylocity uses a combination of RSA and AES cryptography. As part of the setup, each client is issued a public RSA key.

Paylocity recommends the encryption of the incoming requests as additional protection of the sensitive data. Clients can opt-out of the encryption during the initial setup process. Opt-out will allow Paylocity to process unencrypted requests.

The Paylocity Public Key has the following properties:

* 2048 bit key size

* PKCS1 key format

* PEM encoding

##### Properties

* key (base 64 encoded): The AES symmetric key encrypted with the Paylocity Public Key. It is the key used to encrypt the content. Paylocity will decrypt the AES key using RSA decryption and use it to decrypt the content.

* iv (base 64 encoded): The AES IV (Initialization Vector) used when encrypting the content.

* content (base 64 encoded): The AES encrypted request. The key and iv provided in the secureContent request are used by Paylocity for decryption of the content.

We suggest using the following for the AES:

* CBC cipher mode

* PKCS7 padding

* 128 bit block size

* 256 bit key size

##### Encryption Flow

* Generate the unencrypted JSON payload to POST/PUT
* Encrypt this JSON payload using your _own key and IV_ (NOT with the Paylocity public key)
* RSA encrypt the _key_ you used in step 2 with the Paylocity Public Key, then, base64 encode the result
* Base64 encode the IV used to encrypt the JSON payload in step 2
* Put together a \"securecontent\" JSON object:
 
{
  'secureContent' : {
    'key' : -- RSA-encrypted & base64 encoded key from step 3,
    'iv' : -- base64 encoded iv from step 4
    'content' -- content encrypted with your own key from step 2, base64 encoded
  }
}

##### Sample Example

    {
      \"secureContent\": {
        \"key\": \"eS3aw6H/qzHMJ00gSi6gQ3xa08DPMazk8BFY96Pd99ODA==\",
        \"iv\": \"NLyXMGq9svw0XO5aI9BzWw==\",
        \"content\": \"gAEOiQltO1w+LzGUoIK8FiYbU42hug94EasSl7N+Q1w=\"
      }
    }

##### Sample C# Code

    using Newtonsoft.Json;
    using System;
    using System.IO;
    using System.Security.Cryptography;
    using System.Text;

    public class SecuredContent
    {
      [JsonProperty(\"key\")]
      public string Key { get; set; }

      [JsonProperty(\"iv\")]
      public string Iv { get; set; }

      [JsonProperty(\"content\")]
      public string Content { get; set; }

    }

    public class EndUserSecureRequestExample
    {
      public string CreateSecuredRequest(FileInfo paylocityPublicKey, string unsecuredJsonRequest)
      {
        string publicKeyXml = File.ReadAllText(paylocityPublicKey.FullName, Encoding.UTF8);

        SecuredContent secureContent = this.CreateSecuredContent(publicKeyXml, unsecuredJsonRequest);

        string secureRequest = JsonConvert.SerializeObject(new { secureContent });

        return secureRequest;
      }

      private SecuredContent CreateSecuredContent(string publicKeyXml, string request)
      {
        using (AesCryptoServiceProvider aesCsp = new AesCryptoServiceProvider())
        {
          aesCsp.Mode = CipherMode.CBC;
          aesCsp.Padding = PaddingMode.PKCS7;
          aesCsp.BlockSize = 128;
          aesCsp.KeySize = 256;

          using (ICryptoTransform crt = aesCsp.CreateEncryptor(aesCsp.Key, aesCsp.IV))
          {
            using (MemoryStream outputStream = new MemoryStream())
            {
              using (CryptoStream encryptStream = new CryptoStream(outputStream, crt, CryptoStreamMode.Write))
              {
                byte[] encodedRequest = Encoding.UTF8.GetBytes(request);
                encryptStream.Write(encodedRequest, 0, encodedRequest.Length);
                encryptStream.FlushFinalBlock();
                byte[] encryptedRequest = outputStream.ToArray();

                using (RSACryptoServiceProvider crp = new RSACryptoServiceProvider())
                {
                  crp.FromXmlstring(publicKeyXml);
                  byte[] encryptedKey = crp.Encrypt(aesCsp.Key, false);

                  return new SecuredContent()
                  {
                    Key = Convert.ToBase64string(encryptedKey),
                    Iv = Convert.ToBase64string(aesCsp.IV),
                    Content = Convert.ToBase64string(encryptedRequest)
                  };
                }
              }
            }
          }
        }
      }
    }

## Support

Questions about using the Paylocity API? Please contact webservices@paylocity.com.

# Deductions (v1)

Deductions API provides endpoints to retrieve, add, update and delete deductions for a company's employees. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.

# OnBoarding (v1)

Onboarding API sends employee data into Paylocity Onboarding to help ensure an easy and accurate hiring process for subsequent completion into Web Pay. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2
- Package version: 2
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install paylocity_api --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your paylocity_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var PaylocityApi = require('paylocity_api');

var defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
var paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = "YOUR ACCESS TOKEN"

var api = new PaylocityApi.AdditionalRatesApi()
var companyId = "companyId_example"; // {String} Company Id
var employeeId = "employeeId_example"; // {String} Employee Id
var additionalRate = new PaylocityApi.AdditionalRate(); // {AdditionalRate} Additional Rate Model
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.addOrUpdateAdditionalRates(companyId, employeeId, additionalRate, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.paylocity.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PaylocityApi.AdditionalRatesApi* | [**addOrUpdateAdditionalRates**](docs/AdditionalRatesApi.md#addOrUpdateAdditionalRates) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/additionalRates | Add/update additional rates
*PaylocityApi.ClientCredentialsApi* | [**addClientSecret**](docs/ClientCredentialsApi.md#addClientSecret) | **POST** /v2/credentials/secrets | Obtain new client secret.
*PaylocityApi.CompanyCodesApi* | [**getAllCompanyCodesAndDescriptionsByResource**](docs/CompanyCodesApi.md#getAllCompanyCodesAndDescriptionsByResource) | **GET** /v2/companies/{companyId}/codes/{codeResource} | Get All Company Codes
*PaylocityApi.CompanySpecificSchemaApi* | [**getCompanySpecificOpenAPIDocumentation**](docs/CompanySpecificSchemaApi.md#getCompanySpecificOpenAPIDocumentation) | **GET** /v2/companies/{companyId}/openapi | Get Company-Specific Open API Documentation
*PaylocityApi.CustomFieldsApi* | [**getAllCustomFieldsByCategory**](docs/CustomFieldsApi.md#getAllCustomFieldsByCategory) | **GET** /v2/companies/{companyId}/customfields/{category} | Get All Custom Fields
*PaylocityApi.DirectDepositApi* | [**getAllDirectDeposit**](docs/DirectDepositApi.md#getAllDirectDeposit) | **GET** /v2/companies/{companyId}/employees/{employeeId}/directDeposit | Get All Direct Deposit
*PaylocityApi.EarningsApi* | [**addOrUpdateAnEmployeeEarning**](docs/EarningsApi.md#addOrUpdateAnEmployeeEarning) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/earnings | Add/Update Earning
*PaylocityApi.EarningsApi* | [**deleteEarningByEarningCodeAndStartDate**](docs/EarningsApi.md#deleteEarningByEarningCodeAndStartDate) | **DELETE** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate} | Delete Earning by Earning Code and Start Date
*PaylocityApi.EarningsApi* | [**getAllEarnings**](docs/EarningsApi.md#getAllEarnings) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings | Get All Earnings
*PaylocityApi.EarningsApi* | [**getEarningByEarningCodeAndStartDate**](docs/EarningsApi.md#getEarningByEarningCodeAndStartDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode}/{startDate} | Get Earning by Earning Code and Start Date
*PaylocityApi.EarningsApi* | [**getEarningsByEarningCode**](docs/EarningsApi.md#getEarningsByEarningCode) | **GET** /v2/companies/{companyId}/employees/{employeeId}/earnings/{earningCode} | Get Earnings by Earning Code
*PaylocityApi.EmergencyContactsApi* | [**addOrUpdateEmergencyContacts**](docs/EmergencyContactsApi.md#addOrUpdateEmergencyContacts) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/emergencyContacts | Add/update emergency contacts
*PaylocityApi.EmployeeApi* | [**addEmployee**](docs/EmployeeApi.md#addEmployee) | **POST** /v2/companies/{companyId}/employees | Add new employee
*PaylocityApi.EmployeeApi* | [**getAllEmployees**](docs/EmployeeApi.md#getAllEmployees) | **GET** /v2/companies/{companyId}/employees/ | Get all employees
*PaylocityApi.EmployeeApi* | [**getEmployee**](docs/EmployeeApi.md#getEmployee) | **GET** /v2/companies/{companyId}/employees/{employeeId} | Get employee
*PaylocityApi.EmployeeApi* | [**updateEmployee**](docs/EmployeeApi.md#updateEmployee) | **PATCH** /v2/companies/{companyId}/employees/{employeeId} | Update employee
*PaylocityApi.EmployeeBenefitSetupApi* | [**updateOrAddEmployeeBenefitSetup**](docs/EmployeeBenefitSetupApi.md#updateOrAddEmployeeBenefitSetup) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/benefitSetup | Add/update employee&#39;s benefit setup
*PaylocityApi.EmployeeStagingApi* | [**addNewEmployeeToWebLink**](docs/EmployeeStagingApi.md#addNewEmployeeToWebLink) | **POST** /v2/weblinkstaging/companies/{companyId}/employees/newemployees | Add new employee to Web Link
*PaylocityApi.LocalTaxesApi* | [**addLocalTax**](docs/LocalTaxesApi.md#addLocalTax) | **POST** /v2/companies/{companyId}/employees/{employeeId}/localTaxes | Add new local tax
*PaylocityApi.LocalTaxesApi* | [**deleteLocalTaxByTaxCode**](docs/LocalTaxesApi.md#deleteLocalTaxByTaxCode) | **DELETE** /v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode} | Delete local tax by tax code
*PaylocityApi.LocalTaxesApi* | [**getAllLocalTaxes**](docs/LocalTaxesApi.md#getAllLocalTaxes) | **GET** /v2/companies/{companyId}/employees/{employeeId}/localTaxes | Get all local taxes
*PaylocityApi.LocalTaxesApi* | [**getLocalTaxByTaxCode**](docs/LocalTaxesApi.md#getLocalTaxByTaxCode) | **GET** /v2/companies/{companyId}/employees/{employeeId}/localTaxes/{taxCode} | Get local taxes by tax code
*PaylocityApi.NonPrimaryStateTaxApi* | [**addOrUpdateNonPrimaryStateTax**](docs/NonPrimaryStateTaxApi.md#addOrUpdateNonPrimaryStateTax) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/nonprimaryStateTax | Add/update non-primary state tax
*PaylocityApi.PayStatementsApi* | [**getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear**](docs/PayStatementsApi.md#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYear) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year} | Get employee pay statement details data for the specified year.
*PaylocityApi.PayStatementsApi* | [**getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate**](docs/PayStatementsApi.md#getsEmployeePayStatementDetailDataBasedOnTheSpecifiedYearAndCheckDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/details/{year}/{checkDate} | Get employee pay statement details data for the specified year and check date.
*PaylocityApi.PayStatementsApi* | [**getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear**](docs/PayStatementsApi.md#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYear) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year} | Get employee pay statement summary data for the specified year.
*PaylocityApi.PayStatementsApi* | [**getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate**](docs/PayStatementsApi.md#getsEmployeePayStatementSummaryDataBasedOnTheSpecifiedYearAndCheckDate) | **GET** /v2/companies/{companyId}/employees/{employeeId}/paystatement/summary/{year}/{checkDate} | Get employee pay statement summary data for the specified year and check date.
*PaylocityApi.PrimaryStateTaxApi* | [**addOrUpdatePrimaryStateTax**](docs/PrimaryStateTaxApi.md#addOrUpdatePrimaryStateTax) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/primaryStateTax | Add/update primary state tax
*PaylocityApi.SensitiveDataApi* | [**addOrUpdateSensitiveData**](docs/SensitiveDataApi.md#addOrUpdateSensitiveData) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/sensitivedata | Add/update sensitive data
*PaylocityApi.SensitiveDataApi* | [**getSensitiveData**](docs/SensitiveDataApi.md#getSensitiveData) | **GET** /v2/companies/{companyId}/employees/{employeeId}/sensitivedata | Get sensitive data


## Documentation for Models

 - [PaylocityApi.AddClientSecret](docs/AddClientSecret.md)
 - [PaylocityApi.AdditionalRate](docs/AdditionalRate.md)
 - [PaylocityApi.BenefitSetup](docs/BenefitSetup.md)
 - [PaylocityApi.ClientCredentialsResponse](docs/ClientCredentialsResponse.md)
 - [PaylocityApi.CompanyCodes](docs/CompanyCodes.md)
 - [PaylocityApi.CustomFieldDefinition](docs/CustomFieldDefinition.md)
 - [PaylocityApi.CustomFieldDefinitionValuesInner](docs/CustomFieldDefinitionValuesInner.md)
 - [PaylocityApi.DirectDeposit](docs/DirectDeposit.md)
 - [PaylocityApi.DirectDepositAdditionalDirectDepositInner](docs/DirectDepositAdditionalDirectDepositInner.md)
 - [PaylocityApi.DirectDepositMainDirectDeposit](docs/DirectDepositMainDirectDeposit.md)
 - [PaylocityApi.Earning](docs/Earning.md)
 - [PaylocityApi.EmergencyContact](docs/EmergencyContact.md)
 - [PaylocityApi.Employee](docs/Employee.md)
 - [PaylocityApi.EmployeeAdditionalRateInner](docs/EmployeeAdditionalRateInner.md)
 - [PaylocityApi.EmployeeBenefitSetup](docs/EmployeeBenefitSetup.md)
 - [PaylocityApi.EmployeeCustomBooleanFieldsInner](docs/EmployeeCustomBooleanFieldsInner.md)
 - [PaylocityApi.EmployeeCustomDateFieldsInner](docs/EmployeeCustomDateFieldsInner.md)
 - [PaylocityApi.EmployeeCustomDropDownFieldsInner](docs/EmployeeCustomDropDownFieldsInner.md)
 - [PaylocityApi.EmployeeCustomNumberFieldsInner](docs/EmployeeCustomNumberFieldsInner.md)
 - [PaylocityApi.EmployeeCustomTextFieldsInner](docs/EmployeeCustomTextFieldsInner.md)
 - [PaylocityApi.EmployeeDepartmentPosition](docs/EmployeeDepartmentPosition.md)
 - [PaylocityApi.EmployeeEmergencyContactsInner](docs/EmployeeEmergencyContactsInner.md)
 - [PaylocityApi.EmployeeFederalTax](docs/EmployeeFederalTax.md)
 - [PaylocityApi.EmployeeHomeAddress](docs/EmployeeHomeAddress.md)
 - [PaylocityApi.EmployeeIdResponse](docs/EmployeeIdResponse.md)
 - [PaylocityApi.EmployeeInfo](docs/EmployeeInfo.md)
 - [PaylocityApi.EmployeeLocalTaxInner](docs/EmployeeLocalTaxInner.md)
 - [PaylocityApi.EmployeeMainDirectDeposit](docs/EmployeeMainDirectDeposit.md)
 - [PaylocityApi.EmployeeNonPrimaryStateTax](docs/EmployeeNonPrimaryStateTax.md)
 - [PaylocityApi.EmployeePrimaryPayRate](docs/EmployeePrimaryPayRate.md)
 - [PaylocityApi.EmployeePrimaryStateTax](docs/EmployeePrimaryStateTax.md)
 - [PaylocityApi.EmployeeStatus](docs/EmployeeStatus.md)
 - [PaylocityApi.EmployeeTaxSetup](docs/EmployeeTaxSetup.md)
 - [PaylocityApi.EmployeeWebTime](docs/EmployeeWebTime.md)
 - [PaylocityApi.EmployeeWorkAddress](docs/EmployeeWorkAddress.md)
 - [PaylocityApi.EmployeeWorkEligibility](docs/EmployeeWorkEligibility.md)
 - [PaylocityApi.Error](docs/Error.md)
 - [PaylocityApi.ErrorOptionsInner](docs/ErrorOptionsInner.md)
 - [PaylocityApi.LocalTax](docs/LocalTax.md)
 - [PaylocityApi.NonPrimaryStateTax](docs/NonPrimaryStateTax.md)
 - [PaylocityApi.PayStatementDetails](docs/PayStatementDetails.md)
 - [PaylocityApi.PayStatementSummary](docs/PayStatementSummary.md)
 - [PaylocityApi.SensitiveData](docs/SensitiveData.md)
 - [PaylocityApi.SensitiveDataDisability](docs/SensitiveDataDisability.md)
 - [PaylocityApi.SensitiveDataDisabilityDisabilityClassificationsInner](docs/SensitiveDataDisabilityDisabilityClassificationsInner.md)
 - [PaylocityApi.SensitiveDataEthnicity](docs/SensitiveDataEthnicity.md)
 - [PaylocityApi.SensitiveDataEthnicityEthnicRacialIdentitiesInner](docs/SensitiveDataEthnicityEthnicRacialIdentitiesInner.md)
 - [PaylocityApi.SensitiveDataGender](docs/SensitiveDataGender.md)
 - [PaylocityApi.SensitiveDataVeteran](docs/SensitiveDataVeteran.md)
 - [PaylocityApi.StagedEmployee](docs/StagedEmployee.md)
 - [PaylocityApi.StagedEmployeeAdditionalDirectDepositInner](docs/StagedEmployeeAdditionalDirectDepositInner.md)
 - [PaylocityApi.StagedEmployeeBenefitSetupInner](docs/StagedEmployeeBenefitSetupInner.md)
 - [PaylocityApi.StagedEmployeeDepartmentPositionInner](docs/StagedEmployeeDepartmentPositionInner.md)
 - [PaylocityApi.StagedEmployeeFederalTaxInner](docs/StagedEmployeeFederalTaxInner.md)
 - [PaylocityApi.StagedEmployeeHomeAddressInner](docs/StagedEmployeeHomeAddressInner.md)
 - [PaylocityApi.StagedEmployeeMainDirectDepositInner](docs/StagedEmployeeMainDirectDepositInner.md)
 - [PaylocityApi.StagedEmployeeNonPrimaryStateTaxInner](docs/StagedEmployeeNonPrimaryStateTaxInner.md)
 - [PaylocityApi.StagedEmployeePrimaryPayRateInner](docs/StagedEmployeePrimaryPayRateInner.md)
 - [PaylocityApi.StagedEmployeePrimaryStateTaxInner](docs/StagedEmployeePrimaryStateTaxInner.md)
 - [PaylocityApi.StagedEmployeeStatusInner](docs/StagedEmployeeStatusInner.md)
 - [PaylocityApi.StagedEmployeeWebTime](docs/StagedEmployeeWebTime.md)
 - [PaylocityApi.StagedEmployeeWorkAddressInner](docs/StagedEmployeeWorkAddressInner.md)
 - [PaylocityApi.StagedEmployeeWorkEligibilityInner](docs/StagedEmployeeWorkEligibilityInner.md)
 - [PaylocityApi.StateTax](docs/StateTax.md)
 - [PaylocityApi.TrackingNumberResponse](docs/TrackingNumberResponse.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### paylocity_auth


- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
  - WebLinkAPI: Web Link Api

