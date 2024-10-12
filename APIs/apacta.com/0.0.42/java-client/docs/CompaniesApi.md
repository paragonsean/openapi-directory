# CompaniesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | View a company integration feature setting |
| [**companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut) | **PUT** /companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id} | Edit a company integration feature setting |
| [**companiesCompanyIdCompaniesIntegrationFeatureSettingsGet**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/companies_integration_feature_settings | List a company integration feature settings |
| [**companiesCompanyIdCompaniesIntegrationFeatureSettingsPost**](CompaniesApi.md#companiesCompanyIdCompaniesIntegrationFeatureSettingsPost) | **POST** /companies/{company_id}/companies_integration_feature_settings | Add a company integration feature setting |
| [**companiesCompanyIdFormTemplatesFormTemplateIdDelete**](CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdDelete) | **DELETE** /companies/{company_id}/form_templates/{form_template_id} | Delete a form template company |
| [**companiesCompanyIdFormTemplatesFormTemplateIdGet**](CompaniesApi.md#companiesCompanyIdFormTemplatesFormTemplateIdGet) | **GET** /companies/{company_id}/form_templates/{form_template_id} | Get a company form template |
| [**companiesCompanyIdFormTemplatesGet**](CompaniesApi.md#companiesCompanyIdFormTemplatesGet) | **GET** /companies/{company_id}/form_templates/ | Get a list of company form templates |
| [**companiesCompanyIdGet**](CompaniesApi.md#companiesCompanyIdGet) | **GET** /companies/{company_id} | Details of 1 company |
| [**companiesCompanyIdIntegrationFeatureSettingsGet**](CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsGet) | **GET** /companies/{company_id}/integration_feature_settings | Get a list of integration feature settings |
| [**companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet**](CompaniesApi.md#companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet) | **GET** /companies/{company_id}/integration_feature_settings/{integration_feature_setting_id} | Show details of 1 integration feature setting |
| [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete) | **DELETE** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Delete a company integration setting |
| [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet) | **GET** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Get a company integration setting |
| [**companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut) | **PUT** /companies/{company_id}/integration_settings/{companies_integration_setting_id} | Edit a company integration setting |
| [**companiesCompanyIdIntegrationSettingsGet**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsGet) | **GET** /companies/{company_id}/integration_settings | Get a list of company integration settings |
| [**companiesCompanyIdIntegrationSettingsPost**](CompaniesApi.md#companiesCompanyIdIntegrationSettingsPost) | **POST** /companies/{company_id}/integration_settings | Add a company integration setting |
| [**companiesCompanyIdPriceMarginsPriceMarginsIdDelete**](CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdDelete) | **DELETE** /companies/{company_id}/price_margins/{price_margins_id} | Delete a company price margin |
| [**companiesCompanyIdPriceMarginsPriceMarginsIdGet**](CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdGet) | **GET** /companies/{company_id}/price_margins/{price_margins_id} | Get a list of company price margins |
| [**companiesCompanyIdPriceMarginsPriceMarginsIdPost**](CompaniesApi.md#companiesCompanyIdPriceMarginsPriceMarginsIdPost) | **POST** /companies/{company_id}/price_margins/{price_margins_id} | Add a company price margin |
| [**companiesGet**](CompaniesApi.md#companiesGet) | **GET** /companies | Get a list of companies |
| [**companiesSubscriptionSelfServiceGet**](CompaniesApi.md#companiesSubscriptionSelfServiceGet) | **GET** /companies/subscription_self_service | URL for subscription selfservice |


<a id="companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet"></a>
# **companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet**
> CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(companyId, cIntegrationFeatureSettingId)

View a company integration feature setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String cIntegrationFeatureSettingId = "cIntegrationFeatureSettingId_example"; // String | 
    try {
      CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response result = apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet(companyId, cIntegrationFeatureSettingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdGet");
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
| **companyId** | **String**|  | |
| **cIntegrationFeatureSettingId** | **String**|  | |

### Return type

[**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | IntegrationFeatureSetting not found |  -  |

<a id="companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut"></a>
# **companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut**
> CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(companyId, cIntegrationFeatureSettingId)

Edit a company integration feature setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String cIntegrationFeatureSettingId = "cIntegrationFeatureSettingId_example"; // String | 
    try {
      CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response result = apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut(companyId, cIntegrationFeatureSettingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdCompaniesIntegrationFeatureSettingsCIntegrationFeatureSettingIdPut");
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
| **companyId** | **String**|  | |
| **cIntegrationFeatureSettingId** | **String**|  | |

### Return type

[**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | IntegrationFeatureSetting not found |  -  |

<a id="companiesCompanyIdCompaniesIntegrationFeatureSettingsGet"></a>
# **companiesCompanyIdCompaniesIntegrationFeatureSettingsGet**
> CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(companyId)

List a company integration feature settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    try {
      CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response result = apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsGet(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdCompaniesIntegrationFeatureSettingsGet");
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
| **companyId** | **String**|  | |

### Return type

[**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Company not found |  -  |

<a id="companiesCompanyIdCompaniesIntegrationFeatureSettingsPost"></a>
# **companiesCompanyIdCompaniesIntegrationFeatureSettingsPost**
> CreateSuccessResponse companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(companyId, companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest)

Add a company integration feature setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest = new CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest(); // CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest | 
    try {
      CreateSuccessResponse result = apiInstance.companiesCompanyIdCompaniesIntegrationFeatureSettingsPost(companyId, companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdCompaniesIntegrationFeatureSettingsPost");
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
| **companyId** | **String**|  | |
| **companiesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest** | [**CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest**](CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest.md)|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Company not found |  -  |
| **422** | Validation error |  -  |

<a id="companiesCompanyIdFormTemplatesFormTemplateIdDelete"></a>
# **companiesCompanyIdFormTemplatesFormTemplateIdDelete**
> EmptySuccessResponse companiesCompanyIdFormTemplatesFormTemplateIdDelete(companyId, formTemplateId)

Delete a form template company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String formTemplateId = "formTemplateId_example"; // String | Automatically added
    try {
      EmptySuccessResponse result = apiInstance.companiesCompanyIdFormTemplatesFormTemplateIdDelete(companyId, formTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdFormTemplatesFormTemplateIdDelete");
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
| **companyId** | **String**|  | |
| **formTemplateId** | **String**| Automatically added | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Companies form template not found |  -  |

<a id="companiesCompanyIdFormTemplatesFormTemplateIdGet"></a>
# **companiesCompanyIdFormTemplatesFormTemplateIdGet**
> CompaniesCompanyIdFormTemplatesGet200Response companiesCompanyIdFormTemplatesFormTemplateIdGet(companyId, id, formTemplateId)

Get a company form template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String id = "id_example"; // String | 
    String formTemplateId = "formTemplateId_example"; // String | Automatically added
    try {
      CompaniesCompanyIdFormTemplatesGet200Response result = apiInstance.companiesCompanyIdFormTemplatesFormTemplateIdGet(companyId, id, formTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdFormTemplatesFormTemplateIdGet");
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
| **companyId** | **String**|  | |
| **id** | **String**|  | |
| **formTemplateId** | **String**| Automatically added | |

### Return type

[**CompaniesCompanyIdFormTemplatesGet200Response**](CompaniesCompanyIdFormTemplatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Form template company not found |  -  |

<a id="companiesCompanyIdFormTemplatesGet"></a>
# **companiesCompanyIdFormTemplatesGet**
> CompaniesCompanyIdFormTemplatesGet200Response companiesCompanyIdFormTemplatesGet(companyId, formTemplateId)

Get a list of company form templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String formTemplateId = "formTemplateId_example"; // String | 
    try {
      CompaniesCompanyIdFormTemplatesGet200Response result = apiInstance.companiesCompanyIdFormTemplatesGet(companyId, formTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdFormTemplatesGet");
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
| **companyId** | **String**|  | |
| **formTemplateId** | **String**|  | |

### Return type

[**CompaniesCompanyIdFormTemplatesGet200Response**](CompaniesCompanyIdFormTemplatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Company not found |  -  |

<a id="companiesCompanyIdGet"></a>
# **companiesCompanyIdGet**
> CompaniesCompanyIdGet200Response companiesCompanyIdGet(companyId)

Details of 1 company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    try {
      CompaniesCompanyIdGet200Response result = apiInstance.companiesCompanyIdGet(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdGet");
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
| **companyId** | **String**|  | |

### Return type

[**CompaniesCompanyIdGet200Response**](CompaniesCompanyIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Company object |  -  |
| **404** | Company not found |  -  |

<a id="companiesCompanyIdIntegrationFeatureSettingsGet"></a>
# **companiesCompanyIdIntegrationFeatureSettingsGet**
> CompaniesCompanyIdIntegrationFeatureSettingsGet200Response companiesCompanyIdIntegrationFeatureSettingsGet(companyId)

Get a list of integration feature settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    try {
      CompaniesCompanyIdIntegrationFeatureSettingsGet200Response result = apiInstance.companiesCompanyIdIntegrationFeatureSettingsGet(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdIntegrationFeatureSettingsGet");
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
| **companyId** | **String**|  | |

### Return type

[**CompaniesCompanyIdIntegrationFeatureSettingsGet200Response**](CompaniesCompanyIdIntegrationFeatureSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet"></a>
# **companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet**
> CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(companyId, integrationFeatureSettingId)

Show details of 1 integration feature setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String integrationFeatureSettingId = "integrationFeatureSettingId_example"; // String | 
    try {
      CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response result = apiInstance.companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet(companyId, integrationFeatureSettingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet");
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
| **companyId** | **String**|  | |
| **integrationFeatureSettingId** | **String**|  | |

### Return type

[**CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response**](CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | IntegrationFeatureSetting not found |  -  |

<a id="companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete"></a>
# **companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete**
> EmptySuccessResponse companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(companyId, companiesIntegrationSettingId)

Delete a company integration setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String companiesIntegrationSettingId = "companiesIntegrationSettingId_example"; // String | 
    try {
      EmptySuccessResponse result = apiInstance.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete(companyId, companiesIntegrationSettingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdDelete");
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
| **companyId** | **String**|  | |
| **companiesIntegrationSettingId** | **String**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Companies integration setting not found |  -  |

<a id="companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet"></a>
# **companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet**
> CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(companyId, companiesIntegrationSettingId)

Get a company integration setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String companiesIntegrationSettingId = "companiesIntegrationSettingId_example"; // String | 
    try {
      CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response result = apiInstance.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet(companyId, companiesIntegrationSettingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet");
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
| **companyId** | **String**|  | |
| **companiesIntegrationSettingId** | **String**|  | |

### Return type

[**CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response**](CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Companies integration setting not found |  -  |

<a id="companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut"></a>
# **companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut**
> EmptySuccessResponse companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(companyId, companiesIntegrationSettingId)

Edit a company integration setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String companiesIntegrationSettingId = "companiesIntegrationSettingId_example"; // String | 
    try {
      EmptySuccessResponse result = apiInstance.companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut(companyId, companiesIntegrationSettingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdPut");
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
| **companyId** | **String**|  | |
| **companiesIntegrationSettingId** | **String**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Companies integration setting not found |  -  |
| **422** | Validation error |  -  |

<a id="companiesCompanyIdIntegrationSettingsGet"></a>
# **companiesCompanyIdIntegrationSettingsGet**
> CompaniesCompanyIdIntegrationSettingsGet200Response companiesCompanyIdIntegrationSettingsGet(companyId, identifier)

Get a list of company integration settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String identifier = "identifier_example"; // String | The identifier of an ERP integration
    try {
      CompaniesCompanyIdIntegrationSettingsGet200Response result = apiInstance.companiesCompanyIdIntegrationSettingsGet(companyId, identifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdIntegrationSettingsGet");
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
| **companyId** | **String**|  | |
| **identifier** | **String**| The identifier of an ERP integration | [optional] |

### Return type

[**CompaniesCompanyIdIntegrationSettingsGet200Response**](CompaniesCompanyIdIntegrationSettingsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Company not found |  -  |

<a id="companiesCompanyIdIntegrationSettingsPost"></a>
# **companiesCompanyIdIntegrationSettingsPost**
> CreateSuccessResponse companiesCompanyIdIntegrationSettingsPost(companyId, companiesCompanyIdIntegrationSettingsPostRequest)

Add a company integration setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    CompaniesCompanyIdIntegrationSettingsPostRequest companiesCompanyIdIntegrationSettingsPostRequest = new CompaniesCompanyIdIntegrationSettingsPostRequest(); // CompaniesCompanyIdIntegrationSettingsPostRequest | 
    try {
      CreateSuccessResponse result = apiInstance.companiesCompanyIdIntegrationSettingsPost(companyId, companiesCompanyIdIntegrationSettingsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdIntegrationSettingsPost");
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
| **companyId** | **String**|  | |
| **companiesCompanyIdIntegrationSettingsPostRequest** | [**CompaniesCompanyIdIntegrationSettingsPostRequest**](CompaniesCompanyIdIntegrationSettingsPostRequest.md)|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Company not found |  -  |
| **422** | Validation error |  -  |

<a id="companiesCompanyIdPriceMarginsPriceMarginsIdDelete"></a>
# **companiesCompanyIdPriceMarginsPriceMarginsIdDelete**
> EmptySuccessResponse companiesCompanyIdPriceMarginsPriceMarginsIdDelete(companyId, priceMarginId, priceMarginsId)

Delete a company price margin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String priceMarginId = "priceMarginId_example"; // String | 
    String priceMarginsId = "priceMarginsId_example"; // String | Automatically added
    try {
      EmptySuccessResponse result = apiInstance.companiesCompanyIdPriceMarginsPriceMarginsIdDelete(companyId, priceMarginId, priceMarginsId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdPriceMarginsPriceMarginsIdDelete");
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
| **companyId** | **String**|  | |
| **priceMarginId** | **String**|  | |
| **priceMarginsId** | **String**| Automatically added | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Companies integration setting not found |  -  |

<a id="companiesCompanyIdPriceMarginsPriceMarginsIdGet"></a>
# **companiesCompanyIdPriceMarginsPriceMarginsIdGet**
> CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response companiesCompanyIdPriceMarginsPriceMarginsIdGet(companyId, priceMarginsId)

Get a list of company price margins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String priceMarginsId = "priceMarginsId_example"; // String | Automatically added
    try {
      CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response result = apiInstance.companiesCompanyIdPriceMarginsPriceMarginsIdGet(companyId, priceMarginsId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdPriceMarginsPriceMarginsIdGet");
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
| **companyId** | **String**|  | |
| **priceMarginsId** | **String**| Automatically added | |

### Return type

[**CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response**](CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Company not found |  -  |

<a id="companiesCompanyIdPriceMarginsPriceMarginsIdPost"></a>
# **companiesCompanyIdPriceMarginsPriceMarginsIdPost**
> CreateSuccessResponse companiesCompanyIdPriceMarginsPriceMarginsIdPost(companyId, priceMarginsId, companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest)

Add a company price margin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    String companyId = "companyId_example"; // String | 
    String priceMarginsId = "priceMarginsId_example"; // String | Automatically added
    CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest = new CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest(); // CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest | 
    try {
      CreateSuccessResponse result = apiInstance.companiesCompanyIdPriceMarginsPriceMarginsIdPost(companyId, priceMarginsId, companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesCompanyIdPriceMarginsPriceMarginsIdPost");
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
| **companyId** | **String**|  | |
| **priceMarginsId** | **String**| Automatically added | |
| **companiesCompanyIdPriceMarginsPriceMarginsIdPostRequest** | [**CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest**](CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest.md)|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Company not found |  -  |
| **422** | Validation error |  -  |

<a id="companiesGet"></a>
# **companiesGet**
> CompaniesGet200Response companiesGet()

Get a list of companies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    try {
      CompaniesGet200Response result = apiInstance.companiesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompaniesGet200Response**](CompaniesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="companiesSubscriptionSelfServiceGet"></a>
# **companiesSubscriptionSelfServiceGet**
> CompaniesSubscriptionSelfServiceGet200Response companiesSubscriptionSelfServiceGet()

URL for subscription selfservice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompaniesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    CompaniesApi apiInstance = new CompaniesApi(defaultClient);
    try {
      CompaniesSubscriptionSelfServiceGet200Response result = apiInstance.companiesSubscriptionSelfServiceGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompaniesApi#companiesSubscriptionSelfServiceGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompaniesSubscriptionSelfServiceGet200Response**](CompaniesSubscriptionSelfServiceGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Self service url |  -  |
| **404** | Company not found |  -  |

