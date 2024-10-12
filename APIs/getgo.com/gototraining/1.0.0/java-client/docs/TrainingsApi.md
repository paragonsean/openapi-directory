# TrainingsApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelTraining**](TrainingsApi.md#cancelTraining) | **DELETE** /organizers/{organizerKey}/trainings/{trainingKey} | Delete Training |
| [**getAllTrainings**](TrainingsApi.md#getAllTrainings) | **GET** /organizers/{organizerKey}/trainings | Get Trainings |
| [**getManageTrainingURL**](TrainingsApi.md#getManageTrainingURL) | **GET** /organizers/{organizerKey}/trainings/{trainingKey}/manageUrl | Get Management URL for Training |
| [**getOrganisersForTraining**](TrainingsApi.md#getOrganisersForTraining) | **GET** /organizers/{organizerKey}/trainings/{trainingKey}/organizers | Get Training Organizers |
| [**getStartUrl**](TrainingsApi.md#getStartUrl) | **GET** /organizers/{organizerKey}/trainings/{trainingKey}/startUrl | Get Start Url |
| [**getTraining**](TrainingsApi.md#getTraining) | **GET** /organizers/{organizerKey}/trainings/{trainingKey} | Get Training |
| [**scheduleTraining**](TrainingsApi.md#scheduleTraining) | **POST** /organizers/{organizerKey}/trainings | Create Training |
| [**startTraining**](TrainingsApi.md#startTraining) | **GET** /trainings/{trainingKey}/start | Start Training |
| [**updateOrganisersForTraining**](TrainingsApi.md#updateOrganisersForTraining) | **PUT** /organizers/{organizerKey}/trainings/{trainingKey}/organizers | Update Training Organizers |
| [**updateRegistrationSettingsForTraining**](TrainingsApi.md#updateRegistrationSettingsForTraining) | **PUT** /organizers/{organizerKey}/trainings/{trainingKey}/registrationSettings | Update Training Registration Settings |
| [**updateTrainingNameDescription**](TrainingsApi.md#updateTrainingNameDescription) | **PUT** /organizers/{organizerKey}/trainings/{trainingKey}/nameDescription | Update Training Name and Description |
| [**updateTrainingTimes**](TrainingsApi.md#updateTrainingTimes) | **PUT** /organizers/{organizerKey}/trainings/{trainingKey}/times | Update Training Times |


<a id="cancelTraining"></a>
# **cancelTraining**
> cancelTraining(authorization, organizerKey, trainingKey)

Delete Training

Deletes a scheduled or completed training. For scheduled trainings, it deletes all scheduled sessions of the training. For completed trainings, the sessions remain in the database. No email is sent to organizers or registrants, but when participants attempt to start or join the training, they are directed to a page that states: Training Not Found: The training you are trying to join is no longer available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    try {
      apiInstance.cancelTraining(authorization, organizerKey, trainingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#cancelTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAllTrainings"></a>
# **getAllTrainings**
> List&lt;Training&gt; getAllTrainings(authorization, organizerKey)

Get Trainings

This call retrieves information on all scheduled trainings for a given organizer. The trainings are returned in the order in which they were created. Completed trainings are not included; ongoing trainings with past sessions are included along with the past sessions. If the organizer does not have any scheduled trainings, the response will be empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    try {
      List<Training> result = apiInstance.getAllTrainings(authorization, organizerKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#getAllTrainings");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |

### Return type

[**List&lt;Training&gt;**](Training.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="getManageTrainingURL"></a>
# **getManageTrainingURL**
> String getManageTrainingURL(authorization, organizerKey, trainingKey)

Get Management URL for Training

A request for a direct URL to the admin portal for a specific training. The request identifies the organizer and the training; the response provides a link the organizer can use to manage or launch the training in the admin portal. The training organizer will be required to log in. You can schedule and manage the training (e.g., add tests, polls and training materials) from the URL provided in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    try {
      String result = apiInstance.getManageTrainingURL(authorization, organizerKey, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#getManageTrainingURL");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getOrganisersForTraining"></a>
# **getOrganisersForTraining**
> List&lt;Organizer&gt; getOrganisersForTraining(authorization, organizerKey, trainingKey)

Get Training Organizers

Retrieves organizer details for a specific training. This is only applicable to multi-user accounts with sharing enabled (co-organizers).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    try {
      List<Organizer> result = apiInstance.getOrganisersForTraining(authorization, organizerKey, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#getOrganisersForTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

[**List&lt;Organizer&gt;**](Organizer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getStartUrl"></a>
# **getStartUrl**
> String getStartUrl(authorization, organizerKey, trainingKey)

Get Start Url

Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start after the organizer logs in with its credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    try {
      String result = apiInstance.getStartUrl(authorization, organizerKey, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#getStartUrl");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getTraining"></a>
# **getTraining**
> Training getTraining(authorization, organizerKey, trainingKey)

Get Training

Uses the organizer key and training key to retrieve information on a scheduled training.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    try {
      Training result = apiInstance.getTraining(authorization, organizerKey, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#getTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

[**Training**](Training.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="scheduleTraining"></a>
# **scheduleTraining**
> String scheduleTraining(authorization, organizerKey, body)

Create Training

Schedules a training of one or more sessions. The call requires a training&#39;s name, at least one start and end time, and optionally may include additional sessions, a description, additional organizers (presenters), and registration settings. You can only add organizers to a training if you have a multi-user account. Once a training has been created with this method, you can accept registrations to the training. Registration is for the entire training - all sessions. (The GoToTraining admin site enables you to create trainings that allow participants to register for individual sessions as well as automatically create weekly or monthly events.) Registration settings controls whether you allow web registration for this training, and whether a confirmation email is sent to the registrant following registration. Disabling the confirmation email is an API-only setting. If the user registers through the GoToTraining website, a confirmation email is sent. If the user is manually approved by the training administrator through the GoToTraining web site, the confirmation email is sent. It is recommended that you disable web registration if you disable confirmation emails. The response contains a trainingKey for the scheduled training.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    TrainingReqCreate body = new TrainingReqCreate(); // TrainingReqCreate | The details of the training to create
    try {
      String result = apiInstance.scheduleTraining(authorization, organizerKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#scheduleTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **body** | [**TrainingReqCreate**](TrainingReqCreate.md)| The details of the training to create | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="startTraining"></a>
# **startTraining**
> HostUrl startTraining(authorization, trainingKey)

Start Training

Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start. A login of the organizer is not required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long trainingKey = 56L; // Long | The key of the training
    try {
      HostUrl result = apiInstance.startTraining(authorization, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#startTraining");
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
| **authorization** | **String**| Access token | |
| **trainingKey** | **Long**| The key of the training | |

### Return type

[**HostUrl**](HostUrl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateOrganisersForTraining"></a>
# **updateOrganisersForTraining**
> updateOrganisersForTraining(authorization, organizerKey, trainingKey, body)

Update Training Organizers

Replaces the co-organizers for a specific training. The scheduling organizer cannot be unassigned. Organizers will be notified via email if the notifyOrganizers parameter is set to true. Replaced organizers are not notified. This method is only applicable to multi-user accounts with sharing enabled (co-organizers).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    TrainingOrganizers body = new TrainingOrganizers(); // TrainingOrganizers | The details of the training to create
    try {
      apiInstance.updateOrganisersForTraining(authorization, organizerKey, trainingKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#updateOrganisersForTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |
| **body** | [**TrainingOrganizers**](TrainingOrganizers.md)| The details of the training to create | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateRegistrationSettingsForTraining"></a>
# **updateRegistrationSettingsForTraining**
> updateRegistrationSettingsForTraining(authorization, organizerKey, trainingKey, body)

Update Training Registration Settings

An API request to automatically enable or disable web registrations and confirmation emails to registrants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    RegistrationSettings body = new RegistrationSettings(); // RegistrationSettings | The new registration settings for the training
    try {
      apiInstance.updateRegistrationSettingsForTraining(authorization, organizerKey, trainingKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#updateRegistrationSettingsForTraining");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |
| **body** | [**RegistrationSettings**](RegistrationSettings.md)| The new registration settings for the training | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateTrainingNameDescription"></a>
# **updateTrainingNameDescription**
> updateTrainingNameDescription(authorization, organizerKey, trainingKey, body)

Update Training Name and Description

Request to update a scheduled training name and description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    TrainingNameDescription body = new TrainingNameDescription(); // TrainingNameDescription | The new name and description for the training
    try {
      apiInstance.updateTrainingNameDescription(authorization, organizerKey, trainingKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#updateTrainingNameDescription");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |
| **body** | [**TrainingNameDescription**](TrainingNameDescription.md)| The new name and description for the training | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateTrainingTimes"></a>
# **updateTrainingTimes**
> NotifiedParties updateTrainingTimes(authorization, organizerKey, trainingKey, body)

Update Training Times

 A request to update a scheduled training&#39;s start and end times. If the request contains &#39;notifyTrainers &#x3D; true&#39; and &#39;notifyRegistrants &#x3D; true&#39;, both organizers and registrants are notified. The response provides the number of notified trainers and registrants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrainingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    TrainingsApi apiInstance = new TrainingsApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long organizerKey = 56L; // Long | The key of the training organizer
    Long trainingKey = 56L; // Long | The key of the training
    TrainingTimes body = new TrainingTimes(); // TrainingTimes | The new start and end times for the scheduled training
    try {
      NotifiedParties result = apiInstance.updateTrainingTimes(authorization, organizerKey, trainingKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrainingsApi#updateTrainingTimes");
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
| **authorization** | **String**| Access token | |
| **organizerKey** | **Long**| The key of the training organizer | |
| **trainingKey** | **Long**| The key of the training | |
| **body** | [**TrainingTimes**](TrainingTimes.md)| The new start and end times for the scheduled training | |

### Return type

[**NotifiedParties**](NotifiedParties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

