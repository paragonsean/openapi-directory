# ChecksApi.ChecksApi

All URIs are relative to *https://api.truora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCheck**](ChecksApi.md#createCheck) | **POST** /v1/checks | Create a background check
[**getCheck**](ChecksApi.md#getCheck) | **GET** /v1/checks/{check_id} | Get Background Check
[**getHealthDashboard**](ChecksApi.md#getHealthDashboard) | **GET** /v1/checks/health | Get Health Dashboard
[**listCheckDetails**](ChecksApi.md#listCheckDetails) | **GET** /v1/checks/{check_id}/details | List Check Details
[**listChecks**](ChecksApi.md#listChecks) | **GET** /v1/checks | List Checks



## createCheck

> CheckOutput createCheck(country, type, opts)

Create a background check

Creates a background check and queues it to start collecting information. The full details of background checks can be retrieved with their respective Check IDs using getCheck endpoint. Keep in mind that, depending on the check type, input document, and country of a search, certain inputs are required. You should always provide as many inputs as possible in order to get the highest accuracy.  If your check type is not referenced in the following table, please reach out to find out the fields that apply for you.  | Country | Person-National | PersonForeigner | Company | Vehicle-National | Vehicle-Foreigner | |:-------:|:---------------:|:---------------:|:-------:|:----------------:|:-----------------:| | Chile&lt;br&gt;CL | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;date_of_birth*&lt;br&gt;phone_number&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;native_country* | N/A | national_id*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | foreign_id*&lt;br&gt;first_name*&lt;br&gt;last_name*&lt;br&gt;date_of_birth*&lt;br&gt;native_country*&lt;br&gt;license_plate*&lt;br&gt;payment_date (Santiago only)&lt;br&gt;driver_license (Santiago only) | | Colombia&lt;br&gt;CO | national_id*&lt;br&gt;date_of_birth&lt;br&gt;issue_date&lt;br&gt;phone_number | foreign_id* or PEP*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;issue_date* | tax_id*&lt;br&gt;national_id | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;owner_document_type&lt;br&gt;owner_document_id | foreign_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number&lt;br&gt;license_plate*&lt;br&gt;issue_date* | | Mexico&lt;br&gt;MX | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate*&lt;br&gt;national_id&lt;br&gt;vehicle_id&lt;br&gt;driver_license(Estado de Mexico only) | N/A | | Brazil&lt;br&gt;BR | national_id*&lt;br&gt;date_of_birth*&lt;br&gt;region*&lt;br&gt;phone_number | N/A | tax_id* | license_plate* | N/A | | Costa Rica&lt;br&gt;CR | national_id*&lt;br&gt;phone_number | foreign_id* | N/A | license_plate* | N/A | | Ecuador&lt;br&gt;EC | national_id*&lt;br&gt;phone_number | foreign_id* | tax_id* | license_plate* | N/A | | Peru&lt;br&gt;PE | national_id*&lt;br&gt;date_of_birth&lt;br&gt;phone_number | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;phone_number | N/A | national_id*&lt;br&gt;date_of_birth&lt;br&gt;license_plate* | foreign_id*&lt;br&gt;ptp&lt;br&gt;date_of_birth*&lt;br&gt;license_plate* | | Argentina&lt;br&gt;AR | national_id* | N/A | N/A | national_id* | N/A | | International&lt;br&gt;ALL | name* | name* | company_name* | N/A | N/A |  (*) Required field

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ChecksApi();
let country = "country_example"; // String | Document country
let type = "type_example"; // String | Background check type
let opts = {
  'truoraPriority': "truoraPriority_example", // String | Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default
  'birthCertificate': "birthCertificate_example", // String | Person birth certificate
  'companyName': "companyName_example", // String | Company name \\\"Don't forget this required field to complete background checks in Brazil\\\"
  'dateOfBirth': new Date("2013-10-20"), // Date | Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil
  'diplomaticId': "diplomaticId_example", // String | Diplomatic ID
  'driverLicense': "driverLicense_example", // String | Driver's license number
  'escrow': "escrow_example", // String | Colombian escrow
  'firstName': "firstName_example", // String | Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil
  'forceCreation': true, // Boolean | Forces a new background check creation when true. Reuses recently created background checks otherwise
  'foreignId': "foreignId_example", // String | Person foreign ID
  'issueDate': new Date("2013-10-20"), // Date | Person document issue date in \\\"YYYY-mm-dd\\\" format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases
  'lastName': "lastName_example", // String | Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil
  'licensePlate': "licensePlate_example", // String | Vehicle license plate
  'nationalId': "nationalId_example", // String | National ID
  'nativeCountry': "nativeCountry_example", // String | Country of birth
  'ownerDocumentId': "ownerDocumentId_example", // String | National ID of the vehicle owner
  'ownerDocumentType': "ownerDocumentType_example", // String | National ID, foreign ID, or tax ID
  'passport': "passport_example", // String | Person passport
  'paymentDate': new Date("2013-10-20"), // Date | Payment day of a vehicle circulation permit (Chile only)
  'pep': "pep_example", // String | ID for Venezuelans working in Colombia
  'phoneNumber': "phoneNumber_example", // String | Person phone number. Required by law to notify the person their background is being checked
  'professionalCard': "professionalCard_example", // String | Professional ID card
  'ptp': "ptp_example", // String | ID for Venezuelans working in Peru
  'region': "region_example", // String | Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins.
  'reportId': "reportId_example", // String | Report ID the background check will be inserted into
  'stateId': "stateId_example", // String |  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil
  'taxId': "taxId_example", // String | Company ID used for tax payments
  'userAuthorized': true, // Boolean | Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later]
  'vehicleId': "vehicleId_example", // String | Vehicle license plate
  'verificationCode': "verificationCode_example", // String | Verification code registered for criminal records in Peru only
  'watch': "watch_example" // String | Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once
};
apiInstance.createCheck(country, type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| Document country | 
 **type** | **String**| Background check type | 
 **truoraPriority** | **String**| Describes the background check priority. The amount of high priority checks is limited by country. Medium priority is used by default | [optional] 
 **birthCertificate** | **String**| Person birth certificate | [optional] 
 **companyName** | **String**| Company name \\\&quot;Don&#39;t forget this required field to complete background checks in Brazil\\\&quot; | [optional] 
 **dateOfBirth** | **Date**| Person birthdate. This date is used to get some additional information about a person and to filter homonyms in some cases. YYYY-MM-DD format, Required for complete background checks in Brazil | [optional] 
 **diplomaticId** | **String**| Diplomatic ID | [optional] 
 **driverLicense** | **String**| Driver&#39;s license number | [optional] 
 **escrow** | **String**| Colombian escrow | [optional] 
 **firstName** | **String**| Person or entity first name. If the document type and number are not provided, the report might include homonyms. Required when searching by first name, Required in order to get complete background checks in Brazil | [optional] 
 **forceCreation** | **Boolean**| Forces a new background check creation when true. Reuses recently created background checks otherwise | [optional] 
 **foreignId** | **String**| Person foreign ID | [optional] 
 **issueDate** | **Date**| Person document issue date in \\\&quot;YYYY-mm-dd\\\&quot; format (e.g. 2008-12-31) . This date is used to get some additional information about a person in some cases | [optional] 
 **lastName** | **String**| Person or entity last name. If the document type and number are not provided, the report might include homonyms. Required when searching by last name. Required in order to get complete background checks in Brazil | [optional] 
 **licensePlate** | **String**| Vehicle license plate | [optional] 
 **nationalId** | **String**| National ID | [optional] 
 **nativeCountry** | **String**| Country of birth | [optional] 
 **ownerDocumentId** | **String**| National ID of the vehicle owner | [optional] 
 **ownerDocumentType** | **String**| National ID, foreign ID, or tax ID | [optional] 
 **passport** | **String**| Person passport | [optional] 
 **paymentDate** | **Date**| Payment day of a vehicle circulation permit (Chile only) | [optional] 
 **pep** | **String**| ID for Venezuelans working in Colombia | [optional] 
 **phoneNumber** | **String**| Person phone number. Required by law to notify the person their background is being checked | [optional] 
 **professionalCard** | **String**| Professional ID card | [optional] 
 **ptp** | **String**| ID for Venezuelans working in Peru | [optional] 
 **region** | **String**| Region where the background is to be checked in addition to the region where the person is from. By default, background checks in Brazil are performed in the region where the person is from. Required for Brazil only. Allowed values are: DF: Distrito Federal, AC: Acre, AL: Alagoas, AP: Amapá, AM: Amazonas, BA: Bahía, CE: Ceará, ES: Espírito Santo, GO: Goiás, MA: Maranhão, MT: Mato Grosso, MS: Mato Grosso do Sul, MG: Minas Gerais, PA: Pará, PB: Paraíba, PR: Paraná, PE: Pernambuco, PI: Piauí, RJ: Río de Janeiro, RN: Río Grande do Norte, RS: Río Grande do Sul, RO: Rondônia, RR: Roraima, SC: Santa Catarina, SP: São Paulo, SE: Sergipe, TO : Tocantins. | [optional] 
 **reportId** | **String**| Report ID the background check will be inserted into | [optional] 
 **stateId** | **String**|  Used for the RG (Registro Geral) identification in Brazil. This identification has different formats according to the state that issues the document. It can have numbers and letters but other characters (- * , . ) are omitted, Required in order to get complete background checks in Brazil | [optional] 
 **taxId** | **String**| Company ID used for tax payments | [optional] 
 **userAuthorized** | **Boolean**| Indicates whether the person subject to the validation authorized the validation. Must be true in order to proceed [Required for API key V1 or later] | [optional] 
 **vehicleId** | **String**| Vehicle license plate | [optional] 
 **verificationCode** | **String**| Verification code registered for criminal records in Peru only | [optional] 
 **watch** | **String**| Indicates whether the check score is to be periodically revised and its frequency. It can be daily, weekly, monthly, yearly or have a custom frequency written as a number accompanied by d: day, w: week, m: month, y: year for instance: 3d: every three days, 2w: every two weeks. Ignore this field if the check is only to be performed once | [optional] 

### Return type

[**CheckOutput**](CheckOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getCheck

> CheckOutput getCheck(checkId)

Get Background Check

Returns the results of the check that matches the ID provided, complete with a set of scores explained below.  ### Scores:   - **Global Score**: Average risk associated with a person, company or vehicle, according to  the background check results. The global score considers results that are validated with the  ID number provided. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   - **ID Score**: Average risk associated with a person according to the background check  results. The ID score considers the results that are validated with a person identity  document. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.    - **Homonym Score**: Average risk associated with a person according to the background check  results. The homonym score considers results that are validated against the name of a person and could not be validated with their ID number. These results might have homonyms associated with them. The score ranges from 0 to 1, where 0 represents high risk and 1 low risk.   In order to calculate these scores, a weighted average is considered with different weights allocated to each dataset. Scores can be customized using the config endpoints by assigning a weight to each dataset according to its relevance.  Keep in mind that results from the API vary depending on the country, check type and the inputs entered on check creation.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ChecksApi();
let checkId = "checkId_example"; // String | Check ID
apiInstance.getCheck(checkId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkId** | **String**| Check ID | 

### Return type

[**CheckOutput**](CheckOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHealthDashboard

> [Database] getHealthDashboard(opts)

Get Health Dashboard

Get the status of a database

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ChecksApi();
let opts = {
  'country': "country_example", // String | Country in ISO 3166, uppercase
  'unixTimestampSeconds': "unixTimestampSeconds_example", // String | Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status
  'unixtimezoneOffsetSeconds': "unixtimezoneOffsetSeconds_example" // String | Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)  
};
apiInstance.getHealthDashboard(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| Country in ISO 3166, uppercase | [optional] 
 **unixTimestampSeconds** | **String**| Unix timestamp in seconds. Send a day timestamp to view the database hourly status for that day or send the current time to know the current database status | [optional] 
 **unixtimezoneOffsetSeconds** | **String**| Offset between the local time and the UTC time in seconds. (e.g., Colombia is at UTC -18000 seconds)   | [optional] 

### Return type

[**[Database]**](Database.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCheckDetails

> CheckDetailsOutput listCheckDetails(checkId, opts)

List Check Details

Lists all details associated with a Check. It can be paginated.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ChecksApi();
let checkId = "checkId_example"; // String | ID of the Check
let opts = {
  'startKey': "startKey_example", // String | Start key value for the pagination
  'lang': "lang_example" // String | This parameter is used to specify the language wanted for details, if not specified details will come in their original language.
};
apiInstance.listCheckDetails(checkId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkId** | **String**| ID of the Check | 
 **startKey** | **String**| Start key value for the pagination | [optional] 
 **lang** | **String**| This parameter is used to specify the language wanted for details, if not specified details will come in their original language. | [optional] 

### Return type

[**CheckDetailsOutput**](CheckDetailsOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChecks

> ChecksOutput listChecks(opts)

List Checks

Lists the existing checks in the account or in a specified report.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.ChecksApi();
let opts = {
  'startKey': "startKey_example", // String | Start key value for the pagination
  'reportId': "reportId_example" // String | Report id checks to be returned
};
apiInstance.listChecks(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startKey** | **String**| Start key value for the pagination | [optional] 
 **reportId** | **String**| Report id checks to be returned | [optional] 

### Return type

[**ChecksOutput**](ChecksOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

