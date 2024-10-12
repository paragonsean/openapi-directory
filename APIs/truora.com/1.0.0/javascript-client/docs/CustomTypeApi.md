# ChecksApi.CustomTypeApi

All URIs are relative to *https://api.truora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createScoreConfig**](CustomTypeApi.md#createScoreConfig) | **POST** /v1/config | Create Score Configurations
[**deleteCustomType**](CustomTypeApi.md#deleteCustomType) | **DELETE** /v1/config | Delete Custom Type
[**listScoreConfigs**](CustomTypeApi.md#listScoreConfigs) | **GET** /v1/config | List Score Configurations
[**updateCustomType**](CustomTypeApi.md#updateCustomType) | **PUT** /v1/config | Update Custom Type



## createScoreConfig

> ScoreConfigOutput createScoreConfig(country, type, opts)

Create Score Configurations

Create a custom score configuration selecting the weight for each background check dataset and the country where it applies. Weights are numbers between 0 and 1 that represent how impactful the dataset is for the score. Keep in mind that the sum of all weights must equal 1.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.CustomTypeApi();
let country = "country_example"; // String | Country where this set of rules applies. Use \\\"all\\\" if the check type searches by name by relying on international databases
let type = "type_example"; // String | Score configuration name. It cannot be person, vehicle, or company
let opts = {
  'datasetAffiliationsAndInsurances': 3.4, // Number | Affiliation and insurance weight for score calculation. From 0 to 1
  'datasetAlertInMedia': 3.4, // Number | Alert in media weight for score calculation. From 0 to 1
  'datasetBusinessBackground': 3.4, // Number | Business background weight for score calculation. From 0 to 1
  'datasetCriminalRecord': 3.4, // Number | Criminal record weight for score calculation. From 0 to 1
  'datasetDrivingLicenses': 3.4, // Number | Driving license weight for score calculation. From 0 to 1
  'datasetInternationalBackground': 3.4, // Number | International background weight for score calculation. From 0 to 1
  'datasetLegalBackground': 3.4, // Number | Legal background weight for score calculation. From 0 to 1
  'datasetPersonalIdentity': 3.4, // Number | Personal identity weight for score calculation. From 0 to 1
  'datasetProfessionalBackground': 3.4, // Number | Professional background weight for score calculation. From 0 to 1
  'datasetTaxesAndFinances': 3.4, // Number | Taxes and financial background weight for score calculation. From 0 to 1
  'datasetTrafficFines': 3.4, // Number | Traffic fines weight for score calculation. From 0 to 1
  'datasetVehicleInformation': 3.4, // Number | Vehicle information weight for score calculation. From 0 to 1
  'datasetVehiclePermits': 3.4 // Number | Vehicle certificate background weight for score calculation. From 0 to 1
};
apiInstance.createScoreConfig(country, type, opts, (error, data, response) => {
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
 **country** | **String**| Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases | 
 **type** | **String**| Score configuration name. It cannot be person, vehicle, or company | 
 **datasetAffiliationsAndInsurances** | **Number**| Affiliation and insurance weight for score calculation. From 0 to 1 | [optional] 
 **datasetAlertInMedia** | **Number**| Alert in media weight for score calculation. From 0 to 1 | [optional] 
 **datasetBusinessBackground** | **Number**| Business background weight for score calculation. From 0 to 1 | [optional] 
 **datasetCriminalRecord** | **Number**| Criminal record weight for score calculation. From 0 to 1 | [optional] 
 **datasetDrivingLicenses** | **Number**| Driving license weight for score calculation. From 0 to 1 | [optional] 
 **datasetInternationalBackground** | **Number**| International background weight for score calculation. From 0 to 1 | [optional] 
 **datasetLegalBackground** | **Number**| Legal background weight for score calculation. From 0 to 1 | [optional] 
 **datasetPersonalIdentity** | **Number**| Personal identity weight for score calculation. From 0 to 1 | [optional] 
 **datasetProfessionalBackground** | **Number**| Professional background weight for score calculation. From 0 to 1 | [optional] 
 **datasetTaxesAndFinances** | **Number**| Taxes and financial background weight for score calculation. From 0 to 1 | [optional] 
 **datasetTrafficFines** | **Number**| Traffic fines weight for score calculation. From 0 to 1 | [optional] 
 **datasetVehicleInformation** | **Number**| Vehicle information weight for score calculation. From 0 to 1 | [optional] 
 **datasetVehiclePermits** | **Number**| Vehicle certificate background weight for score calculation. From 0 to 1 | [optional] 

### Return type

[**ScoreConfigOutput**](ScoreConfigOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteCustomType

> deleteCustomType(type, opts)

Delete Custom Type

Allows deleting a custom type. Person, vehicle, and company types cannot be deleted

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.CustomTypeApi();
let type = "type_example"; // String | Name of the custom type to be deleted
let opts = {
  'country': "country_example" // String | Country where the custom type is valid
};
apiInstance.deleteCustomType(type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| Name of the custom type to be deleted | 
 **country** | **String**| Country where the custom type is valid | [optional] 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listScoreConfigs

> ScoreConfigsOutput listScoreConfigs(opts)

List Score Configurations

Lists the custom score configurations of the associated account.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.CustomTypeApi();
let opts = {
  'startKey': "startKey_example" // String | The key to start the pagination
};
apiInstance.listScoreConfigs(opts, (error, data, response) => {
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
 **startKey** | **String**| The key to start the pagination | [optional] 

### Return type

[**ScoreConfigsOutput**](ScoreConfigsOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCustomType

> updateCustomType(country, type, opts)

Update Custom Type

Allows updating a custom type. Person, vehicle, and company types are not modifiable

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.CustomTypeApi();
let country = "country_example"; // String | Country where this set of rules applies. Use \\\"all\\\" if the check type searches by name by relying on international databases
let type = "type_example"; // String | Score configuration name. It cannot be person, vehicle, or company
let opts = {
  'datasetAffiliationsAndInsurances': 3.4, // Number | Affiliation and insurance weight for score calculation. From 0 to 1
  'datasetAlertInMedia': 3.4, // Number | Alert in media weight for score calculation. From 0 to 1
  'datasetBusinessBackground': 3.4, // Number | Business background weight for score calculation. From 0 to 1
  'datasetCriminalRecord': 3.4, // Number | Criminal record weight for score calculation. From 0 to 1
  'datasetDrivingLicenses': 3.4, // Number | Driving license weight for score calculation. From 0 to 1
  'datasetInternationalBackground': 3.4, // Number | International background weight for score calculation. From 0 to 1
  'datasetLegalBackground': 3.4, // Number | Legal background weight for score calculation. From 0 to 1
  'datasetPersonalIdentity': 3.4, // Number | Personal identity weight for score calculation. From 0 to 1
  'datasetProfessionalBackground': 3.4, // Number | Professional background weight for score calculation. From 0 to 1
  'datasetTaxesAndFinances': 3.4, // Number | Taxes and financial background weight for score calculation. From 0 to 1
  'datasetTrafficFines': 3.4, // Number | Traffic fines weight for score calculation. From 0 to 1
  'datasetVehicleInformation': 3.4, // Number | Vehicle information weight for score calculation. From 0 to 1
  'datasetVehiclePermits': 3.4 // Number | Vehicle certificate background weight for score calculation. From 0 to 1
};
apiInstance.updateCustomType(country, type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **String**| Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases | 
 **type** | **String**| Score configuration name. It cannot be person, vehicle, or company | 
 **datasetAffiliationsAndInsurances** | **Number**| Affiliation and insurance weight for score calculation. From 0 to 1 | [optional] 
 **datasetAlertInMedia** | **Number**| Alert in media weight for score calculation. From 0 to 1 | [optional] 
 **datasetBusinessBackground** | **Number**| Business background weight for score calculation. From 0 to 1 | [optional] 
 **datasetCriminalRecord** | **Number**| Criminal record weight for score calculation. From 0 to 1 | [optional] 
 **datasetDrivingLicenses** | **Number**| Driving license weight for score calculation. From 0 to 1 | [optional] 
 **datasetInternationalBackground** | **Number**| International background weight for score calculation. From 0 to 1 | [optional] 
 **datasetLegalBackground** | **Number**| Legal background weight for score calculation. From 0 to 1 | [optional] 
 **datasetPersonalIdentity** | **Number**| Personal identity weight for score calculation. From 0 to 1 | [optional] 
 **datasetProfessionalBackground** | **Number**| Professional background weight for score calculation. From 0 to 1 | [optional] 
 **datasetTaxesAndFinances** | **Number**| Taxes and financial background weight for score calculation. From 0 to 1 | [optional] 
 **datasetTrafficFines** | **Number**| Traffic fines weight for score calculation. From 0 to 1 | [optional] 
 **datasetVehicleInformation** | **Number**| Vehicle information weight for score calculation. From 0 to 1 | [optional] 
 **datasetVehiclePermits** | **Number**| Vehicle certificate background weight for score calculation. From 0 to 1 | [optional] 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

