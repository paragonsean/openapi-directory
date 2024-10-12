# FeesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**flatRatesPatchFlatRate**](FeesWriteApi.md#flatRatesPatchFlatRate) | **PATCH** /v1/flatrates/{guid} | Update (Patch) a flat rate or a part of it. |
| [**flatRatesPostFlatRate**](FeesWriteApi.md#flatRatesPostFlatRate) | **POST** /v1/flatrates | Insert a flat rate. |
| [**projectFeesPatchProjectFee**](FeesWriteApi.md#projectFeesPatchProjectFee) | **PATCH** /v1/projectfees/{guid} | Update (Patch) a projectFee or a part of it. |
| [**projectFeesPostProjectFee**](FeesWriteApi.md#projectFeesPostProjectFee) | **POST** /v1/projectfees | Insert a project fee. |
| [**projectRecurringFeeRulesPatchProjectRecurringFeeRule**](FeesWriteApi.md#projectRecurringFeeRulesPatchProjectRecurringFeeRule) | **PATCH** /v1/projectrecurringfeerules/{guid} | Update (Patch) a projectRecurringFeeRule or a part of it. |
| [**projectRecurringFeeRulesPostProjectRecurringFeeRule**](FeesWriteApi.md#projectRecurringFeeRulesPostProjectRecurringFeeRule) | **POST** /v1/projectrecurringfeerules | Insert a projectRecurringFeeRule. |


<a id="flatRatesPatchFlatRate"></a>
# **flatRatesPatchFlatRate**
> List&lt;FlatRateOutputModel&gt; flatRatesPatchFlatRate(guid, patchOperation)

Update (Patch) a flat rate or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesWriteApi apiInstance = new FeesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the flat rate.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of FlatRateModel.
    try {
      List<FlatRateOutputModel> result = apiInstance.flatRatesPatchFlatRate(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesWriteApi#flatRatesPatchFlatRate");
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
| **guid** | **String**| ID of the flat rate. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of FlatRateModel. | [optional] |

### Return type

[**List&lt;FlatRateOutputModel&gt;**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of updated flat rates. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="flatRatesPostFlatRate"></a>
# **flatRatesPostFlatRate**
> FlatRateOutputModel flatRatesPostFlatRate(flatRateInputModel)

Insert a flat rate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesWriteApi apiInstance = new FeesWriteApi(defaultClient);
    FlatRateInputModel flatRateInputModel = new FlatRateInputModel(); // FlatRateInputModel | FlatRateModel.
    try {
      FlatRateOutputModel result = apiInstance.flatRatesPostFlatRate(flatRateInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesWriteApi#flatRatesPostFlatRate");
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
| **flatRateInputModel** | [**FlatRateInputModel**](FlatRateInputModel.md)| FlatRateModel. | [optional] |

### Return type

[**FlatRateOutputModel**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created flat rate. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesPatchProjectFee"></a>
# **projectFeesPatchProjectFee**
> List&lt;ProjectFeeOutputModel&gt; projectFeesPatchProjectFee(guid, patchOperation)

Update (Patch) a projectFee or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesWriteApi apiInstance = new FeesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project fee Can also be comma separate list of IDs to patch multiple project fees with one call. When multiple IDs are given, returns model which has list of succeeded project fees and list of errors.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectFeeInputModel.
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesPatchProjectFee(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesWriteApi#projectFeesPatchProjectFee");
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
| **guid** | **String**| ID of the project fee Can also be comma separate list of IDs to patch multiple project fees with one call. When multiple IDs are given, returns model which has list of succeeded project fees and list of errors. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectFeeInputModel. | [optional] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated project fees. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesPostProjectFee"></a>
# **projectFeesPostProjectFee**
> List&lt;ProjectFeeOutputModel&gt; projectFeesPostProjectFee(projectFeeInputModel)

Insert a project fee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesWriteApi apiInstance = new FeesWriteApi(defaultClient);
    ProjectFeeInputModel projectFeeInputModel = new ProjectFeeInputModel(); // ProjectFeeInputModel | ProjectFeeInputModel.
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesPostProjectFee(projectFeeInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesWriteApi#projectFeesPostProjectFee");
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
| **projectFeeInputModel** | [**ProjectFeeInputModel**](ProjectFeeInputModel.md)| ProjectFeeInputModel. | [optional] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project fees. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectRecurringFeeRulesPatchProjectRecurringFeeRule"></a>
# **projectRecurringFeeRulesPatchProjectRecurringFeeRule**
> List&lt;ProjectRecurringFeeRuleOutputModel&gt; projectRecurringFeeRulesPatchProjectRecurringFeeRule(guid, patchOperation)

Update (Patch) a projectRecurringFeeRule or a part of it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesWriteApi apiInstance = new FeesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the projectRecurringFeeRule.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of ProjectRecurringFeeRuleModel.
    try {
      List<ProjectRecurringFeeRuleOutputModel> result = apiInstance.projectRecurringFeeRulesPatchProjectRecurringFeeRule(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesWriteApi#projectRecurringFeeRulesPatchProjectRecurringFeeRule");
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
| **guid** | **String**| ID of the projectRecurringFeeRule. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of ProjectRecurringFeeRuleModel. | [optional] |

### Return type

[**List&lt;ProjectRecurringFeeRuleOutputModel&gt;**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated projectRecurringFeeRules. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectRecurringFeeRulesPostProjectRecurringFeeRule"></a>
# **projectRecurringFeeRulesPostProjectRecurringFeeRule**
> List&lt;ProjectRecurringFeeRuleOutputModel&gt; projectRecurringFeeRulesPostProjectRecurringFeeRule(projectRecurringFeeRuleInputModel)

Insert a projectRecurringFeeRule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeesWriteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    FeesWriteApi apiInstance = new FeesWriteApi(defaultClient);
    ProjectRecurringFeeRuleInputModel projectRecurringFeeRuleInputModel = new ProjectRecurringFeeRuleInputModel(); // ProjectRecurringFeeRuleInputModel | ProjectRecurringFeeRuleModel.
    try {
      List<ProjectRecurringFeeRuleOutputModel> result = apiInstance.projectRecurringFeeRulesPostProjectRecurringFeeRule(projectRecurringFeeRuleInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeesWriteApi#projectRecurringFeeRulesPostProjectRecurringFeeRule");
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
| **projectRecurringFeeRuleInputModel** | [**ProjectRecurringFeeRuleInputModel**](ProjectRecurringFeeRuleInputModel.md)| ProjectRecurringFeeRuleModel. | [optional] |

### Return type

[**List&lt;ProjectRecurringFeeRuleOutputModel&gt;**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created ProjectRecurringFeeRules. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

