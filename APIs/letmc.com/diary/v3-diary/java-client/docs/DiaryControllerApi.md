# DiaryControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**diaryControllerAddFeedback**](DiaryControllerApi.md#diaryControllerAddFeedback) | **POST** /v3/diary/{shortName}/appointment/feedback | Submit appointment feedback |
| [**diaryControllerCancelAppointment**](DiaryControllerApi.md#diaryControllerCancelAppointment) | **PATCH** /v3/diary/{shortName}/appointment/{appointmentID}/cancel | Cancel an existing appointment using its unique identifier |
| [**diaryControllerDeleteAppointment**](DiaryControllerApi.md#diaryControllerDeleteAppointment) | **DELETE** /v3/diary/{shortName}/appointment | Delete an existing appointment using its unique identifier |
| [**diaryControllerGetAllocations**](DiaryControllerApi.md#diaryControllerGetAllocations) | **GET** /v3/diary/{shortName}/allocations | Get a list of all available allocations for a date + 7 days for a specified appointment type |
| [**diaryControllerGetAppointment**](DiaryControllerApi.md#diaryControllerGetAppointment) | **GET** /v3/diary/{shortName}/appointment | Get an appointment by ID |
| [**diaryControllerGetAppointmentTypes**](DiaryControllerApi.md#diaryControllerGetAppointmentTypes) | **GET** /v3/diary/{shortName}/appointmenttypes | A collection of all diary appointment types |
| [**diaryControllerGetAppointmentsBetweenDates**](DiaryControllerApi.md#diaryControllerGetAppointmentsBetweenDates) | **GET** /v3/diary/{shortName}/appointmentsbetweendates | A collection of diary appointments linked to a company filtered between specific dates and by appointment type |
| [**diaryControllerGetRecurringAppointments**](DiaryControllerApi.md#diaryControllerGetRecurringAppointments) | **GET** /v3/diary/{shortName}/recurringappointment | Retrieves all recurring appointments:- |
| [**diaryControllerPostAppointment**](DiaryControllerApi.md#diaryControllerPostAppointment) | **POST** /v3/diary/{shortName}/appointment | Post an appointment into a valid diary allocation |
| [**diaryControllerPutAppointment**](DiaryControllerApi.md#diaryControllerPutAppointment) | **PUT** /v3/diary/{shortName}/appointment | Update an existing appointment using its unique identifier |
| [**diaryControllerSearchGuest**](DiaryControllerApi.md#diaryControllerSearchGuest) | **GET** /v3/diary/{shortname}/{branchID}/guest/search | Match Guest Parameters with existing applicants |


<a id="diaryControllerAddFeedback"></a>
# **diaryControllerAddFeedback**
> String diaryControllerAddFeedback(shortName, feedbackSubmissionModel)

Submit appointment feedback

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
    FeedbackSubmissionModel feedbackSubmissionModel = new FeedbackSubmissionModel(); // FeedbackSubmissionModel | Feedback submission model
    try {
      String result = apiInstance.diaryControllerAddFeedback(shortName, feedbackSubmissionModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerAddFeedback");
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
| **feedbackSubmissionModel** | [**FeedbackSubmissionModel**](FeedbackSubmissionModel.md)| Feedback submission model | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerCancelAppointment"></a>
# **diaryControllerCancelAppointment**
> String diaryControllerCancelAppointment(shortName, appointmentID)

Cancel an existing appointment using its unique identifier

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
    String appointmentID = "appointmentID_example"; // String | The unique appointment id
    try {
      String result = apiInstance.diaryControllerCancelAppointment(shortName, appointmentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerCancelAppointment");
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
| **appointmentID** | **String**| The unique appointment id | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerDeleteAppointment"></a>
# **diaryControllerDeleteAppointment**
> String diaryControllerDeleteAppointment(shortName, appointmentID)

Delete an existing appointment using its unique identifier

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
    String appointmentID = "appointmentID_example"; // String | The unique appointment id
    try {
      String result = apiInstance.diaryControllerDeleteAppointment(shortName, appointmentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerDeleteAppointment");
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
| **appointmentID** | **String**| The unique appointment id | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerGetAllocations"></a>
# **diaryControllerGetAllocations**
> List&lt;DiaryBookingModel&gt; diaryControllerGetAllocations(shortName, preferredDate, appointmentType, lettings, propertyIdentifier, branchID)

Get a list of all available allocations for a date + 7 days for a specified appointment type

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
    OffsetDateTime preferredDate = OffsetDateTime.now(); // OffsetDateTime | The date to search from
    String appointmentType = "appointmentType_example"; // String | The unique appointment type identifier
    Boolean lettings = true; // Boolean | Sales or Lettings property?
    String propertyIdentifier = "propertyIdentifier_example"; // String | The unique property identifier (Sales or Lettings) determines branch and property type
    String branchID = "branchID_example"; // String | Branch ID to check appointments (required if no property submitted)
    try {
      List<DiaryBookingModel> result = apiInstance.diaryControllerGetAllocations(shortName, preferredDate, appointmentType, lettings, propertyIdentifier, branchID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerGetAllocations");
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
| **preferredDate** | **OffsetDateTime**| The date to search from | |
| **appointmentType** | **String**| The unique appointment type identifier | |
| **lettings** | **Boolean**| Sales or Lettings property? | [optional] |
| **propertyIdentifier** | **String**| The unique property identifier (Sales or Lettings) determines branch and property type | [optional] |
| **branchID** | **String**| Branch ID to check appointments (required if no property submitted) | [optional] |

### Return type

[**List&lt;DiaryBookingModel&gt;**](DiaryBookingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerGetAppointment"></a>
# **diaryControllerGetAppointment**
> DiaryAppointmentModel diaryControllerGetAppointment(shortName, appointmentID)

Get an appointment by ID

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
    String shortName = "shortName_example"; // String | Company short name
    String appointmentID = "appointmentID_example"; // String | Appointment ID
    try {
      DiaryAppointmentModel result = apiInstance.diaryControllerGetAppointment(shortName, appointmentID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerGetAppointment");
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
| **shortName** | **String**| Company short name | |
| **appointmentID** | **String**| Appointment ID | |

### Return type

[**DiaryAppointmentModel**](DiaryAppointmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerGetAppointmentTypes"></a>
# **diaryControllerGetAppointmentTypes**
> DiaryAppointmentTypeModelResults diaryControllerGetAppointmentTypes(shortName, offset, count)

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
      DiaryAppointmentTypeModelResults result = apiInstance.diaryControllerGetAppointmentTypes(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerGetAppointmentTypes");
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
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerGetAppointmentsBetweenDates"></a>
# **diaryControllerGetAppointmentsBetweenDates**
> DiaryAppointmentModelResults diaryControllerGetAppointmentsBetweenDates(shortName, branchID, startDate, endDate, appointmentTypesToSearch, offset, count)

A collection of diary appointments linked to a company filtered between specific dates and by appointment type

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
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | The search from date
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | The search to date
    List<String> appointmentTypesToSearch = Arrays.asList(); // List<String> | The appointment IDs to search for
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      DiaryAppointmentModelResults result = apiInstance.diaryControllerGetAppointmentsBetweenDates(shortName, branchID, startDate, endDate, appointmentTypesToSearch, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerGetAppointmentsBetweenDates");
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
| **branchID** | **String**| The unique ID of the Branch | |
| **startDate** | **OffsetDateTime**| The search from date | |
| **endDate** | **OffsetDateTime**| The search to date | |
| **appointmentTypesToSearch** | [**List&lt;String&gt;**](String.md)| The appointment IDs to search for | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**DiaryAppointmentModelResults**](DiaryAppointmentModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerGetRecurringAppointments"></a>
# **diaryControllerGetRecurringAppointments**
> DiaryAppointmentModelResults diaryControllerGetRecurringAppointments(shortName, branchID, appointmentTypesToSearch, offset, count)

Retrieves all recurring appointments:-

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
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    List<String> appointmentTypesToSearch = Arrays.asList(); // List<String> | The appointment IDs to search for
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      DiaryAppointmentModelResults result = apiInstance.diaryControllerGetRecurringAppointments(shortName, branchID, appointmentTypesToSearch, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerGetRecurringAppointments");
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
| **branchID** | **String**| The unique ID of the Branch | |
| **appointmentTypesToSearch** | [**List&lt;String&gt;**](String.md)| The appointment IDs to search for | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**DiaryAppointmentModelResults**](DiaryAppointmentModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerPostAppointment"></a>
# **diaryControllerPostAppointment**
> String diaryControllerPostAppointment(shortName, propertyIdentifier, diaryAppointmentDetails, lettings)

Post an appointment into a valid diary allocation

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
    List<String> propertyIdentifier = Arrays.asList(); // List<String> | The unique property identifier (Sales or Lettings)
    DiaryAppointmentDetails diaryAppointmentDetails = new DiaryAppointmentDetails(); // DiaryAppointmentDetails | The appointment details model
    Boolean lettings = true; // Boolean | Sales or Lettings property?
    try {
      String result = apiInstance.diaryControllerPostAppointment(shortName, propertyIdentifier, diaryAppointmentDetails, lettings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerPostAppointment");
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
| **propertyIdentifier** | [**List&lt;String&gt;**](String.md)| The unique property identifier (Sales or Lettings) | |
| **diaryAppointmentDetails** | [**DiaryAppointmentDetails**](DiaryAppointmentDetails.md)| The appointment details model | |
| **lettings** | **Boolean**| Sales or Lettings property? | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerPutAppointment"></a>
# **diaryControllerPutAppointment**
> String diaryControllerPutAppointment(shortName, appointmentID, diaryAppointmentDetails, lettings, allowMarketingCorrespondence)

Update an existing appointment using its unique identifier

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
    String appointmentID = "appointmentID_example"; // String | The unique appointment id
    DiaryAppointmentDetails diaryAppointmentDetails = new DiaryAppointmentDetails(); // DiaryAppointmentDetails | The appointment details model
    Boolean lettings = true; // Boolean | Sales or Lettings property?
    Boolean allowMarketingCorrespondence = true; // Boolean | Sales or Lettings property?
    try {
      String result = apiInstance.diaryControllerPutAppointment(shortName, appointmentID, diaryAppointmentDetails, lettings, allowMarketingCorrespondence);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerPutAppointment");
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
| **appointmentID** | **String**| The unique appointment id | |
| **diaryAppointmentDetails** | [**DiaryAppointmentDetails**](DiaryAppointmentDetails.md)| The appointment details model | |
| **lettings** | **Boolean**| Sales or Lettings property? | [optional] |
| **allowMarketingCorrespondence** | **Boolean**| Sales or Lettings property? | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="diaryControllerSearchGuest"></a>
# **diaryControllerSearchGuest**
> GuestDiaryParametersResultsModel diaryControllerSearchGuest(shortname, branchID, forename, emailaddress, surname, offset, count)

Match Guest Parameters with existing applicants

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
    String shortname = "shortname_example"; // String | 
    String branchID = "branchID_example"; // String | 
    String forename = "forename_example"; // String | 
    String emailaddress = "emailaddress_example"; // String | 
    String surname = "surname_example"; // String | 
    Integer offset = 56; // Integer | 
    Integer count = 56; // Integer | 
    try {
      GuestDiaryParametersResultsModel result = apiInstance.diaryControllerSearchGuest(shortname, branchID, forename, emailaddress, surname, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiaryControllerApi#diaryControllerSearchGuest");
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
| **shortname** | **String**|  | |
| **branchID** | **String**|  | |
| **forename** | **String**|  | |
| **emailaddress** | **String**|  | |
| **surname** | **String**|  | |
| **offset** | **Integer**|  | |
| **count** | **Integer**|  | |

### Return type

[**GuestDiaryParametersResultsModel**](GuestDiaryParametersResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

