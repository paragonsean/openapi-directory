# NumbersV2SupportingDocumentApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSupportingDocument**](NumbersV2SupportingDocumentApi.md#createSupportingDocument) | **POST** /v2/RegulatoryCompliance/SupportingDocuments |  |
| [**deleteSupportingDocument**](NumbersV2SupportingDocumentApi.md#deleteSupportingDocument) | **DELETE** /v2/RegulatoryCompliance/SupportingDocuments/{Sid} |  |
| [**fetchSupportingDocument**](NumbersV2SupportingDocumentApi.md#fetchSupportingDocument) | **GET** /v2/RegulatoryCompliance/SupportingDocuments/{Sid} |  |
| [**listSupportingDocument**](NumbersV2SupportingDocumentApi.md#listSupportingDocument) | **GET** /v2/RegulatoryCompliance/SupportingDocuments |  |
| [**updateSupportingDocument**](NumbersV2SupportingDocumentApi.md#updateSupportingDocument) | **POST** /v2/RegulatoryCompliance/SupportingDocuments/{Sid} |  |


<a id="createSupportingDocument"></a>
# **createSupportingDocument**
> NumbersV2RegulatoryComplianceSupportingDocument createSupportingDocument(friendlyName, type, attributes)



Create a new Supporting Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2SupportingDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2SupportingDocumentApi apiInstance = new NumbersV2SupportingDocumentApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String type = "type_example"; // String | The type of the Supporting Document.
    Object attributes = null; // Object | The set of parameters that are the attributes of the Supporting Documents resource which are derived Supporting Document Types.
    try {
      NumbersV2RegulatoryComplianceSupportingDocument result = apiInstance.createSupportingDocument(friendlyName, type, attributes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2SupportingDocumentApi#createSupportingDocument");
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
| **friendlyName** | **String**| The string that you assigned to describe the resource. | |
| **type** | **String**| The type of the Supporting Document. | |
| **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the Supporting Documents resource which are derived Supporting Document Types. | [optional] |

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocument**](NumbersV2RegulatoryComplianceSupportingDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSupportingDocument"></a>
# **deleteSupportingDocument**
> deleteSupportingDocument(sid)



Delete a specific Supporting Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2SupportingDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2SupportingDocumentApi apiInstance = new NumbersV2SupportingDocumentApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the Supporting Document resource.
    try {
      apiInstance.deleteSupportingDocument(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2SupportingDocumentApi#deleteSupportingDocument");
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
| **sid** | **String**| The unique string created by Twilio to identify the Supporting Document resource. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchSupportingDocument"></a>
# **fetchSupportingDocument**
> NumbersV2RegulatoryComplianceSupportingDocument fetchSupportingDocument(sid)



Fetch specific Supporting Document Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2SupportingDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2SupportingDocumentApi apiInstance = new NumbersV2SupportingDocumentApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the Supporting Document resource.
    try {
      NumbersV2RegulatoryComplianceSupportingDocument result = apiInstance.fetchSupportingDocument(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2SupportingDocumentApi#fetchSupportingDocument");
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
| **sid** | **String**| The unique string created by Twilio to identify the Supporting Document resource. | |

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocument**](NumbersV2RegulatoryComplianceSupportingDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSupportingDocument"></a>
# **listSupportingDocument**
> ListSupportingDocumentResponse listSupportingDocument(pageSize, page, pageToken)



Retrieve a list of all Supporting Document for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2SupportingDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2SupportingDocumentApi apiInstance = new NumbersV2SupportingDocumentApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSupportingDocumentResponse result = apiInstance.listSupportingDocument(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2SupportingDocumentApi#listSupportingDocument");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSupportingDocumentResponse**](ListSupportingDocumentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSupportingDocument"></a>
# **updateSupportingDocument**
> NumbersV2RegulatoryComplianceSupportingDocument updateSupportingDocument(sid, attributes, friendlyName)



Update an existing Supporting Document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2SupportingDocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2SupportingDocumentApi apiInstance = new NumbersV2SupportingDocumentApi(defaultClient);
    String sid = "sid_example"; // String | The unique string created by Twilio to identify the Supporting Document resource.
    Object attributes = null; // Object | The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    try {
      NumbersV2RegulatoryComplianceSupportingDocument result = apiInstance.updateSupportingDocument(sid, attributes, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2SupportingDocumentApi#updateSupportingDocument");
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
| **sid** | **String**| The unique string created by Twilio to identify the Supporting Document resource. | |
| **attributes** | [**Object**](Object.md)| The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocument**](NumbersV2RegulatoryComplianceSupportingDocument.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

