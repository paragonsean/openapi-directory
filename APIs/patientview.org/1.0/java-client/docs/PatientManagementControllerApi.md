# PatientManagementControllerApi

All URIs are relative to *https://www.patientview.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPatientManagement**](PatientManagementControllerApi.md#getPatientManagement) | **GET** /patientmanagement/{userId}/group/{groupId}/identifier/{identifierId} | getPatientManagement |
| [**getPatientManagementDiagnoses**](PatientManagementControllerApi.md#getPatientManagementDiagnoses) | **GET** /patientmanagement/diagnoses | getPatientManagementDiagnoses |
| [**getPatientManagementLookupTypes**](PatientManagementControllerApi.md#getPatientManagementLookupTypes) | **GET** /patientmanagement/lookuptypes | getPatientManagementLookupTypes |
| [**savePatientManagement**](PatientManagementControllerApi.md#savePatientManagement) | **POST** /patientmanagement/{userId}/group/{groupId}/identifier/{identifierId} | savePatientManagement |
| [**savePatientManagementSurgeries**](PatientManagementControllerApi.md#savePatientManagementSurgeries) | **POST** /patientmanagement/{userId}/group/{groupId}/identifier/{identifierId}/surgeries | savePatientManagementSurgeries |
| [**validatePatientManagement**](PatientManagementControllerApi.md#validatePatientManagement) | **POST** /patientmanagement/validate | validatePatientManagement |


<a id="getPatientManagement"></a>
# **getPatientManagement**
> PatientManagement getPatientManagement(userId, groupId, identifierId)

getPatientManagement

getPatientManagement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientManagementControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    PatientManagementControllerApi apiInstance = new PatientManagementControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    Long groupId = 56L; // Long | groupId
    Long identifierId = 56L; // Long | identifierId
    try {
      PatientManagement result = apiInstance.getPatientManagement(userId, groupId, identifierId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientManagementControllerApi#getPatientManagement");
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
| **userId** | **Long**| userId | |
| **groupId** | **Long**| groupId | |
| **identifierId** | **Long**| identifierId | |

### Return type

[**PatientManagement**](PatientManagement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getPatientManagementDiagnoses"></a>
# **getPatientManagementDiagnoses**
> List&lt;Code&gt; getPatientManagementDiagnoses()

getPatientManagementDiagnoses

getPatientManagementDiagnoses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientManagementControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    PatientManagementControllerApi apiInstance = new PatientManagementControllerApi(defaultClient);
    try {
      List<Code> result = apiInstance.getPatientManagementDiagnoses();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientManagementControllerApi#getPatientManagementDiagnoses");
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

[**List&lt;Code&gt;**](Code.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getPatientManagementLookupTypes"></a>
# **getPatientManagementLookupTypes**
> List&lt;LookupType&gt; getPatientManagementLookupTypes()

getPatientManagementLookupTypes

getPatientManagementLookupTypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientManagementControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    PatientManagementControllerApi apiInstance = new PatientManagementControllerApi(defaultClient);
    try {
      List<LookupType> result = apiInstance.getPatientManagementLookupTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientManagementControllerApi#getPatientManagementLookupTypes");
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

[**List&lt;LookupType&gt;**](LookupType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="savePatientManagement"></a>
# **savePatientManagement**
> savePatientManagement(userId, groupId, identifierId, patientManagement)

savePatientManagement

savePatientManagement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientManagementControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    PatientManagementControllerApi apiInstance = new PatientManagementControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    Long groupId = 56L; // Long | groupId
    Long identifierId = 56L; // Long | identifierId
    PatientManagement patientManagement = new PatientManagement(); // PatientManagement | patientManagement
    try {
      apiInstance.savePatientManagement(userId, groupId, identifierId, patientManagement);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientManagementControllerApi#savePatientManagement");
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
| **userId** | **Long**| userId | |
| **groupId** | **Long**| groupId | |
| **identifierId** | **Long**| identifierId | |
| **patientManagement** | [**PatientManagement**](PatientManagement.md)| patientManagement | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="savePatientManagementSurgeries"></a>
# **savePatientManagementSurgeries**
> savePatientManagementSurgeries(userId, groupId, identifierId, patientManagement)

savePatientManagementSurgeries

savePatientManagementSurgeries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientManagementControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    PatientManagementControllerApi apiInstance = new PatientManagementControllerApi(defaultClient);
    Long userId = 56L; // Long | userId
    Long groupId = 56L; // Long | groupId
    Long identifierId = 56L; // Long | identifierId
    PatientManagement patientManagement = new PatientManagement(); // PatientManagement | patientManagement
    try {
      apiInstance.savePatientManagementSurgeries(userId, groupId, identifierId, patientManagement);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientManagementControllerApi#savePatientManagementSurgeries");
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
| **userId** | **Long**| userId | |
| **groupId** | **Long**| groupId | |
| **identifierId** | **Long**| identifierId | |
| **patientManagement** | [**PatientManagement**](PatientManagement.md)| patientManagement | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="validatePatientManagement"></a>
# **validatePatientManagement**
> validatePatientManagement(patientManagement)

validatePatientManagement

validatePatientManagement

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PatientManagementControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.patientview.org");

    PatientManagementControllerApi apiInstance = new PatientManagementControllerApi(defaultClient);
    PatientManagement patientManagement = new PatientManagement(); // PatientManagement | patientManagement
    try {
      apiInstance.validatePatientManagement(patientManagement);
    } catch (ApiException e) {
      System.err.println("Exception when calling PatientManagementControllerApi#validatePatientManagement");
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
| **patientManagement** | [**PatientManagement**](PatientManagement.md)| patientManagement | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Description was not specified |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

