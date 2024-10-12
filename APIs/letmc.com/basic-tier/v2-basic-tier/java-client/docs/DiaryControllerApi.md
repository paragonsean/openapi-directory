# DiaryControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet**](DiaryControllerApi.md#v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet) | **GET** /v2/tier2/{shortName}/diary/allocations/{diaryAllocationID} | Get a specific diary allocation given its unique Object ID (OID) |
| [**v2Tier2ShortNameDiaryAllocationsGet**](DiaryControllerApi.md#v2Tier2ShortNameDiaryAllocationsGet) | **GET** /v2/tier2/{shortName}/diary/allocations | A collection of all diary allocations |
| [**v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet**](DiaryControllerApi.md#v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet) | **GET** /v2/tier2/{shortName}/diary/appointments/{diaryAppointmentID} | Get a specific diary appointment given its unique Object ID (OID) |
| [**v2Tier2ShortNameDiaryAppointmentsGet**](DiaryControllerApi.md#v2Tier2ShortNameDiaryAppointmentsGet) | **GET** /v2/tier2/{shortName}/diary/appointments | A collection of all diary appointments |
| [**v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet**](DiaryControllerApi.md#v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet) | **GET** /v2/tier2/{shortName}/diary/appointmenttypes/{diaryAppointmentTypeID} | Get a specific diary appointment type given its unique Object ID (OID) |
| [**v2Tier2ShortNameDiaryAppointmenttypesGet**](DiaryControllerApi.md#v2Tier2ShortNameDiaryAppointmenttypesGet) | **GET** /v2/tier2/{shortName}/diary/appointmenttypes | A collection of all diary appointment types |


<a id="v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet"></a>
# **v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet**
> DiaryAllocationModel v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet(shortName, diaryAllocationID)

Get a specific diary allocation given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiaryControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    DiaryControllerApi apiInstance = new DiaryControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String diaryAllocationID = "diaryAllocationID_example"; // String | The unique ID of the DiaryAllocation
    try {
      DiaryAllocationModel result = apiInstance.v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet(shortName, diaryAllocationID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet");
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
| **shortName** | **String**| The unique client short-name | |
| **diaryAllocationID** | **String**| The unique ID of the DiaryAllocation | |

### Return type

[**DiaryAllocationModel**](DiaryAllocationModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameDiaryAllocationsGet"></a>
# **v2Tier2ShortNameDiaryAllocationsGet**
> DiaryAllocationModelResults v2Tier2ShortNameDiaryAllocationsGet(shortName, offset, count)

A collection of all diary allocations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiaryControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    DiaryControllerApi apiInstance = new DiaryControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      DiaryAllocationModelResults result = apiInstance.v2Tier2ShortNameDiaryAllocationsGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#v2Tier2ShortNameDiaryAllocationsGet");
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
| **shortName** | **String**| The unique client short-name | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**DiaryAllocationModelResults**](DiaryAllocationModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet"></a>
# **v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet**
> DiaryAppointmentModel v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet(shortName, diaryAppointmentID)

Get a specific diary appointment given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiaryControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    DiaryControllerApi apiInstance = new DiaryControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String diaryAppointmentID = "diaryAppointmentID_example"; // String | The unique ID of the DiaryAppointment
    try {
      DiaryAppointmentModel result = apiInstance.v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet(shortName, diaryAppointmentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet");
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
| **shortName** | **String**| The unique client short-name | |
| **diaryAppointmentID** | **String**| The unique ID of the DiaryAppointment | |

### Return type

[**DiaryAppointmentModel**](DiaryAppointmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameDiaryAppointmentsGet"></a>
# **v2Tier2ShortNameDiaryAppointmentsGet**
> DiaryAppointmentModelResults v2Tier2ShortNameDiaryAppointmentsGet(shortName, offset, count)

A collection of all diary appointments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiaryControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    DiaryControllerApi apiInstance = new DiaryControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      DiaryAppointmentModelResults result = apiInstance.v2Tier2ShortNameDiaryAppointmentsGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#v2Tier2ShortNameDiaryAppointmentsGet");
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
| **shortName** | **String**| The unique client short-name | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**DiaryAppointmentModelResults**](DiaryAppointmentModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet"></a>
# **v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet**
> DiaryAppointmentTypeModel v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet(shortName, diaryAppointmentTypeID)

Get a specific diary appointment type given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiaryControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    DiaryControllerApi apiInstance = new DiaryControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String diaryAppointmentTypeID = "diaryAppointmentTypeID_example"; // String | The unique ID of the DiaryAppointmentType
    try {
      DiaryAppointmentTypeModel result = apiInstance.v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet(shortName, diaryAppointmentTypeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet");
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
| **shortName** | **String**| The unique client short-name | |
| **diaryAppointmentTypeID** | **String**| The unique ID of the DiaryAppointmentType | |

### Return type

[**DiaryAppointmentTypeModel**](DiaryAppointmentTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameDiaryAppointmenttypesGet"></a>
# **v2Tier2ShortNameDiaryAppointmenttypesGet**
> DiaryAppointmentTypeModelResults v2Tier2ShortNameDiaryAppointmenttypesGet(shortName, offset, count)

A collection of all diary appointment types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiaryControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    DiaryControllerApi apiInstance = new DiaryControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      DiaryAppointmentTypeModelResults result = apiInstance.v2Tier2ShortNameDiaryAppointmenttypesGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#v2Tier2ShortNameDiaryAppointmenttypesGet");
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
| **shortName** | **String**| The unique client short-name | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**DiaryAppointmentTypeModelResults**](DiaryAppointmentTypeModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

