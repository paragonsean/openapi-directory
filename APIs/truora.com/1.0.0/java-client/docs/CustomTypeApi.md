# CustomTypeApi

All URIs are relative to *https://api.truora.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createScoreConfig**](CustomTypeApi.md#createScoreConfig) | **POST** /v1/config | Create Score Configurations |
| [**deleteCustomType**](CustomTypeApi.md#deleteCustomType) | **DELETE** /v1/config | Delete Custom Type |
| [**listScoreConfigs**](CustomTypeApi.md#listScoreConfigs) | **GET** /v1/config | List Score Configurations |
| [**updateCustomType**](CustomTypeApi.md#updateCustomType) | **PUT** /v1/config | Update Custom Type |


<a id="createScoreConfig"></a>
# **createScoreConfig**
> ScoreConfigOutput createScoreConfig(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits)

Create Score Configurations

Create a custom score configuration selecting the weight for each background check dataset and the country where it applies. Weights are numbers between 0 and 1 that represent how impactful the dataset is for the score. Keep in mind that the sum of all weights must equal 1.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    CustomTypeApi apiInstance = new CustomTypeApi(defaultClient);
    String country = "ALL"; // String | Country where this set of rules applies. Use \\\"all\\\" if the check type searches by name by relying on international databases
    String type = "type_example"; // String | Score configuration name. It cannot be person, vehicle, or company
    Float datasetAffiliationsAndInsurances = 3.4F; // Float | Affiliation and insurance weight for score calculation. From 0 to 1
    Float datasetAlertInMedia = 3.4F; // Float | Alert in media weight for score calculation. From 0 to 1
    Float datasetBusinessBackground = 3.4F; // Float | Business background weight for score calculation. From 0 to 1
    Float datasetCriminalRecord = 3.4F; // Float | Criminal record weight for score calculation. From 0 to 1
    Float datasetDrivingLicenses = 3.4F; // Float | Driving license weight for score calculation. From 0 to 1
    Float datasetInternationalBackground = 3.4F; // Float | International background weight for score calculation. From 0 to 1
    Float datasetLegalBackground = 3.4F; // Float | Legal background weight for score calculation. From 0 to 1
    Float datasetPersonalIdentity = 3.4F; // Float | Personal identity weight for score calculation. From 0 to 1
    Float datasetProfessionalBackground = 3.4F; // Float | Professional background weight for score calculation. From 0 to 1
    Float datasetTaxesAndFinances = 3.4F; // Float | Taxes and financial background weight for score calculation. From 0 to 1
    Float datasetTrafficFines = 3.4F; // Float | Traffic fines weight for score calculation. From 0 to 1
    Float datasetVehicleInformation = 3.4F; // Float | Vehicle information weight for score calculation. From 0 to 1
    Float datasetVehiclePermits = 3.4F; // Float | Vehicle certificate background weight for score calculation. From 0 to 1
    try {
      ScoreConfigOutput result = apiInstance.createScoreConfig(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomTypeApi#createScoreConfig");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **country** | **String**| Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases | [enum: ALL, BR, CL, CO, CR, EC, MX, PE, AR] |
| **type** | **String**| Score configuration name. It cannot be person, vehicle, or company | |
| **datasetAffiliationsAndInsurances** | **Float**| Affiliation and insurance weight for score calculation. From 0 to 1 | [optional] |
| **datasetAlertInMedia** | **Float**| Alert in media weight for score calculation. From 0 to 1 | [optional] |
| **datasetBusinessBackground** | **Float**| Business background weight for score calculation. From 0 to 1 | [optional] |
| **datasetCriminalRecord** | **Float**| Criminal record weight for score calculation. From 0 to 1 | [optional] |
| **datasetDrivingLicenses** | **Float**| Driving license weight for score calculation. From 0 to 1 | [optional] |
| **datasetInternationalBackground** | **Float**| International background weight for score calculation. From 0 to 1 | [optional] |
| **datasetLegalBackground** | **Float**| Legal background weight for score calculation. From 0 to 1 | [optional] |
| **datasetPersonalIdentity** | **Float**| Personal identity weight for score calculation. From 0 to 1 | [optional] |
| **datasetProfessionalBackground** | **Float**| Professional background weight for score calculation. From 0 to 1 | [optional] |
| **datasetTaxesAndFinances** | **Float**| Taxes and financial background weight for score calculation. From 0 to 1 | [optional] |
| **datasetTrafficFines** | **Float**| Traffic fines weight for score calculation. From 0 to 1 | [optional] |
| **datasetVehicleInformation** | **Float**| Vehicle information weight for score calculation. From 0 to 1 | [optional] |
| **datasetVehiclePermits** | **Float**| Vehicle certificate background weight for score calculation. From 0 to 1 | [optional] |

### Return type

[**ScoreConfigOutput**](ScoreConfigOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |
| **400** | Validation error when creating the ScoreConfig |  -  |

<a id="deleteCustomType"></a>
# **deleteCustomType**
> deleteCustomType(type, country)

Delete Custom Type

Allows deleting a custom type. Person, vehicle, and company types cannot be deleted

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    CustomTypeApi apiInstance = new CustomTypeApi(defaultClient);
    String type = "type_example"; // String | Name of the custom type to be deleted
    String country = "BR"; // String | Country where the custom type is valid
    try {
      apiInstance.deleteCustomType(type, country);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomTypeApi#deleteCustomType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| Name of the custom type to be deleted | |
| **country** | **String**| Country where the custom type is valid | [optional] [enum: BR, CL, CO, CR, EC, MX, PE, ALL] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listScoreConfigs"></a>
# **listScoreConfigs**
> ScoreConfigsOutput listScoreConfigs(startKey)

List Score Configurations

Lists the custom score configurations of the associated account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    CustomTypeApi apiInstance = new CustomTypeApi(defaultClient);
    String startKey = "startKey_example"; // String | The key to start the pagination
    try {
      ScoreConfigsOutput result = apiInstance.listScoreConfigs(startKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomTypeApi#listScoreConfigs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **startKey** | **String**| The key to start the pagination | [optional] |

### Return type

[**ScoreConfigsOutput**](ScoreConfigsOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateCustomType"></a>
# **updateCustomType**
> updateCustomType(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits)

Update Custom Type

Allows updating a custom type. Person, vehicle, and company types are not modifiable

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    CustomTypeApi apiInstance = new CustomTypeApi(defaultClient);
    String country = "ALL"; // String | Country where this set of rules applies. Use \\\"all\\\" if the check type searches by name by relying on international databases
    String type = "type_example"; // String | Score configuration name. It cannot be person, vehicle, or company
    Float datasetAffiliationsAndInsurances = 3.4F; // Float | Affiliation and insurance weight for score calculation. From 0 to 1
    Float datasetAlertInMedia = 3.4F; // Float | Alert in media weight for score calculation. From 0 to 1
    Float datasetBusinessBackground = 3.4F; // Float | Business background weight for score calculation. From 0 to 1
    Float datasetCriminalRecord = 3.4F; // Float | Criminal record weight for score calculation. From 0 to 1
    Float datasetDrivingLicenses = 3.4F; // Float | Driving license weight for score calculation. From 0 to 1
    Float datasetInternationalBackground = 3.4F; // Float | International background weight for score calculation. From 0 to 1
    Float datasetLegalBackground = 3.4F; // Float | Legal background weight for score calculation. From 0 to 1
    Float datasetPersonalIdentity = 3.4F; // Float | Personal identity weight for score calculation. From 0 to 1
    Float datasetProfessionalBackground = 3.4F; // Float | Professional background weight for score calculation. From 0 to 1
    Float datasetTaxesAndFinances = 3.4F; // Float | Taxes and financial background weight for score calculation. From 0 to 1
    Float datasetTrafficFines = 3.4F; // Float | Traffic fines weight for score calculation. From 0 to 1
    Float datasetVehicleInformation = 3.4F; // Float | Vehicle information weight for score calculation. From 0 to 1
    Float datasetVehiclePermits = 3.4F; // Float | Vehicle certificate background weight for score calculation. From 0 to 1
    try {
      apiInstance.updateCustomType(country, type, datasetAffiliationsAndInsurances, datasetAlertInMedia, datasetBusinessBackground, datasetCriminalRecord, datasetDrivingLicenses, datasetInternationalBackground, datasetLegalBackground, datasetPersonalIdentity, datasetProfessionalBackground, datasetTaxesAndFinances, datasetTrafficFines, datasetVehicleInformation, datasetVehiclePermits);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomTypeApi#updateCustomType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **country** | **String**| Country where this set of rules applies. Use \\\&quot;all\\\&quot; if the check type searches by name by relying on international databases | [enum: ALL, BR, CL, CO, CR, EC, MX, PE, AR] |
| **type** | **String**| Score configuration name. It cannot be person, vehicle, or company | |
| **datasetAffiliationsAndInsurances** | **Float**| Affiliation and insurance weight for score calculation. From 0 to 1 | [optional] |
| **datasetAlertInMedia** | **Float**| Alert in media weight for score calculation. From 0 to 1 | [optional] |
| **datasetBusinessBackground** | **Float**| Business background weight for score calculation. From 0 to 1 | [optional] |
| **datasetCriminalRecord** | **Float**| Criminal record weight for score calculation. From 0 to 1 | [optional] |
| **datasetDrivingLicenses** | **Float**| Driving license weight for score calculation. From 0 to 1 | [optional] |
| **datasetInternationalBackground** | **Float**| International background weight for score calculation. From 0 to 1 | [optional] |
| **datasetLegalBackground** | **Float**| Legal background weight for score calculation. From 0 to 1 | [optional] |
| **datasetPersonalIdentity** | **Float**| Personal identity weight for score calculation. From 0 to 1 | [optional] |
| **datasetProfessionalBackground** | **Float**| Professional background weight for score calculation. From 0 to 1 | [optional] |
| **datasetTaxesAndFinances** | **Float**| Taxes and financial background weight for score calculation. From 0 to 1 | [optional] |
| **datasetTrafficFines** | **Float**| Traffic fines weight for score calculation. From 0 to 1 | [optional] |
| **datasetVehicleInformation** | **Float**| Vehicle information weight for score calculation. From 0 to 1 | [optional] |
| **datasetVehiclePermits** | **Float**| Vehicle certificate background weight for score calculation. From 0 to 1 | [optional] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

