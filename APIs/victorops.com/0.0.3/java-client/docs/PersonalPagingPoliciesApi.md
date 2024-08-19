# PersonalPagingPoliciesApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1ProfileUsernamePoliciesGet**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesGet) | **GET** /api-public/v1/profile/{username}/policies | Get the user&#39;s paging policy |
| [**apiPublicV1ProfileUsernamePoliciesPost**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesPost) | **POST** /api-public/v1/profile/{username}/policies | Create a paging policy step |
| [**apiPublicV1ProfileUsernamePoliciesStepGet**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepGet) | **GET** /api-public/v1/profile/{username}/policies/{step} | Get a paging policy step |
| [**apiPublicV1ProfileUsernamePoliciesStepPost**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepPost) | **POST** /api-public/v1/profile/{username}/policies/{step} | Create a rule for a paging policy step |
| [**apiPublicV1ProfileUsernamePoliciesStepPut**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepPut) | **PUT** /api-public/v1/profile/{username}/policies/{step} | Update a paging policy step |
| [**apiPublicV1ProfileUsernamePoliciesStepRuleDelete**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepRuleDelete) | **DELETE** /api-public/v1/profile/{username}/policies/{step}/{rule} | Delete a rule from a paging policy step |
| [**apiPublicV1ProfileUsernamePoliciesStepRuleGet**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepRuleGet) | **GET** /api-public/v1/profile/{username}/policies/{step}/{rule} | Get a rule from a paging policy step |
| [**apiPublicV1ProfileUsernamePoliciesStepRulePut**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepRulePut) | **PUT** /api-public/v1/profile/{username}/policies/{step}/{rule} | Update a rule for a paging policy step |


<a id="apiPublicV1ProfileUsernamePoliciesGet"></a>
# **apiPublicV1ProfileUsernamePoliciesGet**
> ApiPublicV1ProfileUsernamePoliciesGet200Response apiPublicV1ProfileUsernamePoliciesGet(username, xVOApiId, xVOApiKey)

Get the user&#39;s paging policy

Get all the paging policy steps for the user on the org associated with the API key  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1ProfileUsernamePoliciesGet200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesGet(username, xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesGet");
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
| **username** | **String**| Your username | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesGet200Response**](ApiPublicV1ProfileUsernamePoliciesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All steps of the user&#39;s paging policy |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1ProfileUsernamePoliciesPost"></a>
# **apiPublicV1ProfileUsernamePoliciesPost**
> ApiPublicV1ProfileUsernamePoliciesPost200Response apiPublicV1ProfileUsernamePoliciesPost(username, xVOApiId, xVOApiKey, body)

Create a paging policy step

Create a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AddGroupPayload body = new AddGroupPayload(); // AddGroupPayload | 
    try {
      ApiPublicV1ProfileUsernamePoliciesPost200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesPost(username, xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesPost");
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
| **username** | **String**| Your username | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **body** | [**AddGroupPayload**](AddGroupPayload.md)|  | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesPost200Response**](ApiPublicV1ProfileUsernamePoliciesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created paging policy step |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1ProfileUsernamePoliciesStepGet"></a>
# **apiPublicV1ProfileUsernamePoliciesStepGet**
> ApiPublicV1ProfileUsernamePoliciesPost200Response apiPublicV1ProfileUsernamePoliciesStepGet(username, step, xVOApiId, xVOApiKey)

Get a paging policy step

Get a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    BigDecimal step = new BigDecimal(78); // BigDecimal | Paging policy step
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1ProfileUsernamePoliciesPost200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesStepGet(username, step, xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesStepGet");
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
| **username** | **String**| Your username | |
| **step** | **BigDecimal**| Paging policy step | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesPost200Response**](ApiPublicV1ProfileUsernamePoliciesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The paging policy step |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1ProfileUsernamePoliciesStepPost"></a>
# **apiPublicV1ProfileUsernamePoliciesStepPost**
> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepPost(username, step, xVOApiId, xVOApiKey, body)

Create a rule for a paging policy step

Create a rule for a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    BigDecimal step = new BigDecimal(78); // BigDecimal | Paging policy step
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AddStepPayload body = new AddStepPayload(); // AddStepPayload | 
    try {
      ApiPublicV1ProfileUsernamePoliciesStepPost200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesStepPost(username, step, xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesStepPost");
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
| **username** | **String**| Your username | |
| **step** | **BigDecimal**| Paging policy step | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **body** | [**AddStepPayload**](AddStepPayload.md)|  | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created rule for the paging policy step |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1ProfileUsernamePoliciesStepPut"></a>
# **apiPublicV1ProfileUsernamePoliciesStepPut**
> ApiPublicV1ProfileUsernamePoliciesPost200Response apiPublicV1ProfileUsernamePoliciesStepPut(username, step, xVOApiId, xVOApiKey, body)

Update a paging policy step

Update a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    BigDecimal step = new BigDecimal(78); // BigDecimal | Paging policy step
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AddGroupPayload body = new AddGroupPayload(); // AddGroupPayload | 
    try {
      ApiPublicV1ProfileUsernamePoliciesPost200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesStepPut(username, step, xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesStepPut");
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
| **username** | **String**| Your username | |
| **step** | **BigDecimal**| Paging policy step | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **body** | [**AddGroupPayload**](AddGroupPayload.md)|  | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesPost200Response**](ApiPublicV1ProfileUsernamePoliciesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated paging policy step |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1ProfileUsernamePoliciesStepRuleDelete"></a>
# **apiPublicV1ProfileUsernamePoliciesStepRuleDelete**
> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepRuleDelete(username, step, rule, xVOApiId, xVOApiKey)

Delete a rule from a paging policy step

Delete a rule from a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    BigDecimal step = new BigDecimal(78); // BigDecimal | Paging policy step
    BigDecimal rule = new BigDecimal(78); // BigDecimal | Rule for a paging policy step
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1ProfileUsernamePoliciesStepPost200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesStepRuleDelete(username, step, rule, xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesStepRuleDelete");
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
| **username** | **String**| Your username | |
| **step** | **BigDecimal**| Paging policy step | |
| **rule** | **BigDecimal**| Rule for a paging policy step | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deleted rule from the paging policy step |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1ProfileUsernamePoliciesStepRuleGet"></a>
# **apiPublicV1ProfileUsernamePoliciesStepRuleGet**
> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepRuleGet(username, step, rule, xVOApiId, xVOApiKey)

Get a rule from a paging policy step

Get a rule from a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    BigDecimal step = new BigDecimal(78); // BigDecimal | Paging policy step
    BigDecimal rule = new BigDecimal(78); // BigDecimal | Rule for a paging policy step
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ApiPublicV1ProfileUsernamePoliciesStepPost200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesStepRuleGet(username, step, rule, xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesStepRuleGet");
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
| **username** | **String**| Your username | |
| **step** | **BigDecimal**| Paging policy step | |
| **rule** | **BigDecimal**| Rule for a paging policy step | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The rule from the paging policy step |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1ProfileUsernamePoliciesStepRulePut"></a>
# **apiPublicV1ProfileUsernamePoliciesStepRulePut**
> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepRulePut(username, step, rule, xVOApiId, xVOApiKey, body)

Update a rule for a paging policy step

Update a rule for a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    PersonalPagingPoliciesApi apiInstance = new PersonalPagingPoliciesApi(defaultClient);
    String username = "username_example"; // String | Your username
    BigDecimal step = new BigDecimal(78); // BigDecimal | Paging policy step
    BigDecimal rule = new BigDecimal(78); // BigDecimal | Rule for a paging policy step
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AddStepPayload body = new AddStepPayload(); // AddStepPayload | 
    try {
      ApiPublicV1ProfileUsernamePoliciesStepPost200Response result = apiInstance.apiPublicV1ProfileUsernamePoliciesStepRulePut(username, step, rule, xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalPagingPoliciesApi#apiPublicV1ProfileUsernamePoliciesStepRulePut");
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
| **username** | **String**| Your username | |
| **step** | **BigDecimal**| Paging policy step | |
| **rule** | **BigDecimal**| Rule for a paging policy step | |
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **body** | [**AddStepPayload**](AddStepPayload.md)|  | |

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated rule for the paging policy step |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **500** | Internal Server Error |  -  |

