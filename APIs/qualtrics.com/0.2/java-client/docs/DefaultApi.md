# DefaultApi

All URIs are relative to *https://fra1.qualtrics.com/API/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createContactInMailinglist**](DefaultApi.md#createContactInMailinglist) | **POST** /directories/{DirectoryId}/mailinglists/{MailingListId}/contacts | Create contact in mailing list |
| [**generateDistributionLinks**](DefaultApi.md#generateDistributionLinks) | **POST** /distributions | Generate distribution links |
| [**getDistributions**](DefaultApi.md#getDistributions) | **GET** /distributions | Get distributions for survey |
| [**getEventSubscriptions**](DefaultApi.md#getEventSubscriptions) | **GET** /eventsubscriptions/{SubscriptionId} | Get event subscriptions |
| [**getSurvey**](DefaultApi.md#getSurvey) | **GET** /survey-definitions/{SurveyId} | Get survey |
| [**retrievedistributionlinks**](DefaultApi.md#retrievedistributionlinks) | **GET** /distributions/{DistributionId}/links | Retrieve distribution links |
| [**webhookDelete**](DefaultApi.md#webhookDelete) | **DELETE** /eventsubscriptions/ | Remove subscription to response event |
| [**whenAResponseIsReceived**](DefaultApi.md#whenAResponseIsReceived) | **POST** /eventsubscriptions/ | Triggers when a response is submitted to a qualtrics survey |


<a id="createContactInMailinglist"></a>
# **createContactInMailinglist**
> createContactInMailinglist(directoryId, mailingListId, createContactInMailingList)

Create contact in mailing list

Creates a contact in a given mailing list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String directoryId = "directoryId_example"; // String | ID of the qualtrics directory to create the contact to
    String mailingListId = "mailingListId_example"; // String | ID of the mailing list
    CreateContactInMailingList createContactInMailingList = new CreateContactInMailingList(); // CreateContactInMailingList | Contact data
    try {
      apiInstance.createContactInMailinglist(directoryId, mailingListId, createContactInMailingList);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createContactInMailinglist");
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
| **directoryId** | **String**| ID of the qualtrics directory to create the contact to | |
| **mailingListId** | **String**| ID of the mailing list | |
| **createContactInMailingList** | [**CreateContactInMailingList**](CreateContactInMailingList.md)| Contact data | |

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
| **200** | OK - Contact created |  -  |

<a id="generateDistributionLinks"></a>
# **generateDistributionLinks**
> generateDistributionLinks(createDistributionLinks)

Generate distribution links

Geneates links for individual distribution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateDistributionLinks createDistributionLinks = new CreateDistributionLinks(); // CreateDistributionLinks | Parameters for the link generation
    try {
      apiInstance.generateDistributionLinks(createDistributionLinks);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#generateDistributionLinks");
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
| **createDistributionLinks** | [**CreateDistributionLinks**](CreateDistributionLinks.md)| Parameters for the link generation | |

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
| **200** | OK |  -  |

<a id="getDistributions"></a>
# **getDistributions**
> DistributionsResponse getDistributions(surveyId)

Get distributions for survey

Gets all distributions for a given survey

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String surveyId = "surveyId_example"; // String | The survey for which to load the distributions
    try {
      DistributionsResponse result = apiInstance.getDistributions(surveyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDistributions");
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
| **surveyId** | **String**| The survey for which to load the distributions | |

### Return type

[**DistributionsResponse**](DistributionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Distributions |  -  |

<a id="getEventSubscriptions"></a>
# **getEventSubscriptions**
> EventSubscriptionsResponse getEventSubscriptions(subscriptionId)

Get event subscriptions

Get event subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | ID of event subscription - can be obtained from web hook response
    try {
      EventSubscriptionsResponse result = apiInstance.getEventSubscriptions(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEventSubscriptions");
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
| **subscriptionId** | **String**| ID of event subscription - can be obtained from web hook response | |

### Return type

[**EventSubscriptionsResponse**](EventSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event subscriptions |  -  |

<a id="getSurvey"></a>
# **getSurvey**
> Object getSurvey(surveyId)

Get survey

Gets a single Qualtrics survey speficied by its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String surveyId = "surveyId_example"; // String | ID of survey (eg. SV_123)
    try {
      Object result = apiInstance.getSurvey(surveyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSurvey");
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
| **surveyId** | **String**| ID of survey (eg. SV_123) | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Survey data |  -  |
| **0** | Operation Failed. |  -  |

<a id="retrievedistributionlinks"></a>
# **retrievedistributionlinks**
> RetrieveDistributionLinksResponse retrievedistributionlinks(surveyId, distributionId)

Retrieve distribution links

Retrieves all the individual links for a given distribution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String surveyId = "surveyId_example"; // String | ID of the survey (eg: SV_123)
    String distributionId = "distributionId_example"; // String | ID of the distribution list
    try {
      RetrieveDistributionLinksResponse result = apiInstance.retrievedistributionlinks(surveyId, distributionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrievedistributionlinks");
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
| **surveyId** | **String**| ID of the survey (eg: SV_123) | |
| **distributionId** | **String**| ID of the distribution list | |

### Return type

[**RetrieveDistributionLinksResponse**](RetrieveDistributionLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated list of links |  -  |

<a id="webhookDelete"></a>
# **webhookDelete**
> EventSubscriptionsResponse webhookDelete(subscribeToEventBody)

Remove subscription to response event

Remove event subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SubscribeToEventBody subscribeToEventBody = new SubscribeToEventBody(); // SubscribeToEventBody | This is the request body of the webhook
    try {
      EventSubscriptionsResponse result = apiInstance.webhookDelete(subscribeToEventBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#webhookDelete");
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
| **subscribeToEventBody** | [**SubscribeToEventBody**](SubscribeToEventBody.md)| This is the request body of the webhook | |

### Return type

[**EventSubscriptionsResponse**](EventSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="whenAResponseIsReceived"></a>
# **whenAResponseIsReceived**
> EventSubscriptionsResponse whenAResponseIsReceived(subscribeToEventBody)

Triggers when a response is submitted to a qualtrics survey

Subscribe to response event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://fra1.qualtrics.com/API/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SubscribeToEventBody subscribeToEventBody = new SubscribeToEventBody(); // SubscribeToEventBody | This is the request body of the webhook
    try {
      EventSubscriptionsResponse result = apiInstance.whenAResponseIsReceived(subscribeToEventBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#whenAResponseIsReceived");
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
| **subscribeToEventBody** | [**SubscribeToEventBody**](SubscribeToEventBody.md)| This is the request body of the webhook | |

### Return type

[**EventSubscriptionsResponse**](EventSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - web hook registered |  -  |

