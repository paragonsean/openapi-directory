# RegulatoryComplianceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**regulatoryComplianceAssessmentsGet**](RegulatoryComplianceApi.md#regulatoryComplianceAssessmentsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls/{regulatoryComplianceControlName}/regulatoryComplianceAssessments/{regulatoryComplianceAssessmentName} |  |
| [**regulatoryComplianceAssessmentsList**](RegulatoryComplianceApi.md#regulatoryComplianceAssessmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls/{regulatoryComplianceControlName}/regulatoryComplianceAssessments |  |
| [**regulatoryComplianceControlsGet**](RegulatoryComplianceApi.md#regulatoryComplianceControlsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls/{regulatoryComplianceControlName} |  |
| [**regulatoryComplianceControlsList**](RegulatoryComplianceApi.md#regulatoryComplianceControlsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName}/regulatoryComplianceControls |  |
| [**regulatoryComplianceStandardsGet**](RegulatoryComplianceApi.md#regulatoryComplianceStandardsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards/{regulatoryComplianceStandardName} |  |
| [**regulatoryComplianceStandardsList**](RegulatoryComplianceApi.md#regulatoryComplianceStandardsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/regulatoryComplianceStandards |  |


<a id="regulatoryComplianceAssessmentsGet"></a>
# **regulatoryComplianceAssessmentsGet**
> RegulatoryComplianceAssessment regulatoryComplianceAssessmentsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, regulatoryComplianceAssessmentName)



Supported regulatory compliance details and state for selected assessment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegulatoryComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegulatoryComplianceApi apiInstance = new RegulatoryComplianceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
    String regulatoryComplianceControlName = "regulatoryComplianceControlName_example"; // String | Name of the regulatory compliance control object
    String regulatoryComplianceAssessmentName = "regulatoryComplianceAssessmentName_example"; // String | Name of the regulatory compliance assessment object
    try {
      RegulatoryComplianceAssessment result = apiInstance.regulatoryComplianceAssessmentsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, regulatoryComplianceAssessmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegulatoryComplianceApi#regulatoryComplianceAssessmentsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | |
| **regulatoryComplianceControlName** | **String**| Name of the regulatory compliance control object | |
| **regulatoryComplianceAssessmentName** | **String**| Name of the regulatory compliance assessment object | |

### Return type

[**RegulatoryComplianceAssessment**](RegulatoryComplianceAssessment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="regulatoryComplianceAssessmentsList"></a>
# **regulatoryComplianceAssessmentsList**
> RegulatoryComplianceAssessmentList regulatoryComplianceAssessmentsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, $filter)



Details and state of assessments mapped to selected regulatory compliance control

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegulatoryComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegulatoryComplianceApi apiInstance = new RegulatoryComplianceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
    String regulatoryComplianceControlName = "regulatoryComplianceControlName_example"; // String | Name of the regulatory compliance control object
    String $filter = "$filter_example"; // String | OData filter. Optional.
    try {
      RegulatoryComplianceAssessmentList result = apiInstance.regulatoryComplianceAssessmentsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegulatoryComplianceApi#regulatoryComplianceAssessmentsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | |
| **regulatoryComplianceControlName** | **String**| Name of the regulatory compliance control object | |
| **$filter** | **String**| OData filter. Optional. | [optional] |

### Return type

[**RegulatoryComplianceAssessmentList**](RegulatoryComplianceAssessmentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="regulatoryComplianceControlsGet"></a>
# **regulatoryComplianceControlsGet**
> RegulatoryComplianceControl regulatoryComplianceControlsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName)



Selected regulatory compliance control details and state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegulatoryComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegulatoryComplianceApi apiInstance = new RegulatoryComplianceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
    String regulatoryComplianceControlName = "regulatoryComplianceControlName_example"; // String | Name of the regulatory compliance control object
    try {
      RegulatoryComplianceControl result = apiInstance.regulatoryComplianceControlsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName, regulatoryComplianceControlName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegulatoryComplianceApi#regulatoryComplianceControlsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | |
| **regulatoryComplianceControlName** | **String**| Name of the regulatory compliance control object | |

### Return type

[**RegulatoryComplianceControl**](RegulatoryComplianceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="regulatoryComplianceControlsList"></a>
# **regulatoryComplianceControlsList**
> RegulatoryComplianceControlList regulatoryComplianceControlsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, $filter)



All supported regulatory compliance controls details and state for selected standard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegulatoryComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegulatoryComplianceApi apiInstance = new RegulatoryComplianceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
    String $filter = "$filter_example"; // String | OData filter. Optional.
    try {
      RegulatoryComplianceControlList result = apiInstance.regulatoryComplianceControlsList(apiVersion, subscriptionId, regulatoryComplianceStandardName, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegulatoryComplianceApi#regulatoryComplianceControlsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | |
| **$filter** | **String**| OData filter. Optional. | [optional] |

### Return type

[**RegulatoryComplianceControlList**](RegulatoryComplianceControlList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="regulatoryComplianceStandardsGet"></a>
# **regulatoryComplianceStandardsGet**
> RegulatoryComplianceStandard regulatoryComplianceStandardsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName)



Supported regulatory compliance details state for selected standard

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegulatoryComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegulatoryComplianceApi apiInstance = new RegulatoryComplianceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String regulatoryComplianceStandardName = "regulatoryComplianceStandardName_example"; // String | Name of the regulatory compliance standard object
    try {
      RegulatoryComplianceStandard result = apiInstance.regulatoryComplianceStandardsGet(apiVersion, subscriptionId, regulatoryComplianceStandardName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegulatoryComplianceApi#regulatoryComplianceStandardsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **regulatoryComplianceStandardName** | **String**| Name of the regulatory compliance standard object | |

### Return type

[**RegulatoryComplianceStandard**](RegulatoryComplianceStandard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="regulatoryComplianceStandardsList"></a>
# **regulatoryComplianceStandardsList**
> RegulatoryComplianceStandardList regulatoryComplianceStandardsList(apiVersion, subscriptionId, $filter)



Supported regulatory compliance standards details and state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegulatoryComplianceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegulatoryComplianceApi apiInstance = new RegulatoryComplianceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String $filter = "$filter_example"; // String | OData filter. Optional.
    try {
      RegulatoryComplianceStandardList result = apiInstance.regulatoryComplianceStandardsList(apiVersion, subscriptionId, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegulatoryComplianceApi#regulatoryComplianceStandardsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **$filter** | **String**| OData filter. Optional. | [optional] |

### Return type

[**RegulatoryComplianceStandardList**](RegulatoryComplianceStandardList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

