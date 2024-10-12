# ContinuousProjectApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addDocument**](ContinuousProjectApi.md#addDocument) | **POST** /continuous_projects/{projectId}/documents | Add a new document to your continuous project |
| [**collectAnalytics**](ContinuousProjectApi.md#collectAnalytics) | **POST** /continuous_projects/{id}/collect-analytics | Save/collect analytics data from Active widget |
| [**complete**](ContinuousProjectApi.md#complete) | **POST** /continuous_projects/{id}/complete | Complete continuous project |
| [**completeContinuousDocument**](ContinuousProjectApi.md#completeContinuousDocument) | **POST** /continuous_projects/{id}/documents/{documentId}/complete | Complete a continuous project document |
| [**completeLanguage**](ContinuousProjectApi.md#completeLanguage) | **POST** /continuous_projects/{id}/languages/{targetLanguage}/complete | Complete continuous project language |
| [**createActiveWidget**](ContinuousProjectApi.md#createActiveWidget) | **POST** /continuous_projects/{projectId}/widgets | Create a new Active widget |
| [**createContinuousProject**](ContinuousProjectApi.md#createContinuousProject) | **POST** /continuous_projects | Create a continuous project |
| [**createSubscription**](ContinuousProjectApi.md#createSubscription) | **POST** /continuous_projects/{id}/subscription | Create subscription for continuous project |
| [**deleteActiveWidget**](ContinuousProjectApi.md#deleteActiveWidget) | **DELETE** /continuous_projects/{projectId}/widgets/{widgetId} | Delete a single widget for this Active project |
| [**deleteContinuousProject**](ContinuousProjectApi.md#deleteContinuousProject) | **DELETE** /continuous_projects/{id} | Delete a continuous project |
| [**deleteSubscription**](ContinuousProjectApi.md#deleteSubscription) | **DELETE** /continuous_projects/{id}/subscription | Delete subscription for continuous project |
| [**getActiveWidget**](ContinuousProjectApi.md#getActiveWidget) | **GET** /continuous_projects/{projectId}/widgets/{widgetId} | View an Active widget |
| [**getActiveWidgets**](ContinuousProjectApi.md#getActiveWidgets) | **GET** /continuous_projects/{projectId}/widgets | View Active widgets |
| [**getAnalyticsToken**](ContinuousProjectApi.md#getAnalyticsToken) | **GET** /continuous_projects/{id}/analytics-token | Get JWT token to be used in analytics dashboards |
| [**getContinuousProject**](ContinuousProjectApi.md#getContinuousProject) | **GET** /continuous_projects/{id} | View a continuous project |
| [**getContinuousProjectDocument**](ContinuousProjectApi.md#getContinuousProjectDocument) | **GET** /continuous_projects/{projectId}/documents/{documentId} | View a continuous document |
| [**getContinuousProjectDocumentProgress**](ContinuousProjectApi.md#getContinuousProjectDocumentProgress) | **GET** /continuous_projects/{projectId}/documents/{documentId}/progress | Monitor progress of a continuous document |
| [**getContinuousProjectDocuments**](ContinuousProjectApi.md#getContinuousProjectDocuments) | **GET** /continuous_projects/{projectId}/documents | View continuous documents |
| [**getContinuousProjectInvoices**](ContinuousProjectApi.md#getContinuousProjectInvoices) | **GET** /continuous_projects/{projectId}/invoices | Invoices of a continuous project |
| [**getContinuousProjectProgress**](ContinuousProjectApi.md#getContinuousProjectProgress) | **GET** /continuous_projects/{projectId}/progress | Monitor progress and status of a continous project |
| [**getContinuousProjects**](ContinuousProjectApi.md#getContinuousProjects) | **GET** /continuous_projects | View continuous projects |
| [**getQuoteForDocument**](ContinuousProjectApi.md#getQuoteForDocument) | **POST** /continuous_projects/{id}/documents/{documentId}/quote | Get a quote for a continuous project document |
| [**getQuoteForDocuments**](ContinuousProjectApi.md#getQuoteForDocuments) | **POST** /continuous_projects/{id}/documents/quote | Get quote for documents |
| [**getQuoteForLanguage**](ContinuousProjectApi.md#getQuoteForLanguage) | **POST** /continuous_projects/{id}/languages/{targetLanguage}/quote | Get quote for language |
| [**getQuoteForLanguages**](ContinuousProjectApi.md#getQuoteForLanguages) | **POST** /continuous_projects/{id}/languages/quote | Get quote for languages |
| [**getSubscription**](ContinuousProjectApi.md#getSubscription) | **GET** /continuous_projects/{id}/subscription | Get subscription for continuous project |
| [**postContinuousProjectDocumentProgress**](ContinuousProjectApi.md#postContinuousProjectDocumentProgress) | **POST** /continuous_projects/{projectId}/documents/progress | Get continuous project document progress for multiple IDs |
| [**resetActiveWidgetToken**](ContinuousProjectApi.md#resetActiveWidgetToken) | **POST** /continuous_projects/{projectId}/widgets/{widgetId}/reset-token | Reset Active widget token |
| [**translate**](ContinuousProjectApi.md#translate) | **POST** /continuous_projects/{id}/translate/{targetLanguage} | Instantly translate your content |
| [**updateActiveWidget**](ContinuousProjectApi.md#updateActiveWidget) | **POST** /continuous_projects/{projectId}/widgets/{widgetId} | Update Active widget settings. |
| [**updateContinuousProject**](ContinuousProjectApi.md#updateContinuousProject) | **POST** /continuous_projects/{id} | Update a continuous project |
| [**updateDocument**](ContinuousProjectApi.md#updateDocument) | **POST** /continuous_projects/{projectId}/documents/{documentId} | Update the document |
| [**updateSubscription**](ContinuousProjectApi.md#updateSubscription) | **PUT** /continuous_projects/{id}/subscription | Update subscription for continuous project |
| [**updateSubscriptionPaymentMethod**](ContinuousProjectApi.md#updateSubscriptionPaymentMethod) | **PUT** /continuous_projects/{id}/subscription/payment | Update subscription payment method for continuous project |


<a id="addDocument"></a>
# **addDocument**
> ContinuousProjectDocument addDocument(projectId, addOrUpdateDocumentRequest)

Add a new document to your continuous project

Add a new document to your continuous project. If the name already exists, it will update the existing document. In most scenarios, this operation will also trigger auto-translation of your document, via MT and/or TM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous project ID
    AddOrUpdateDocumentRequest addOrUpdateDocumentRequest = new AddOrUpdateDocumentRequest(); // AddOrUpdateDocumentRequest | 
    try {
      ContinuousProjectDocument result = apiInstance.addDocument(projectId, addOrUpdateDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#addDocument");
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
| **projectId** | **Long**| Continuous project ID | |
| **addOrUpdateDocumentRequest** | [**AddOrUpdateDocumentRequest**](AddOrUpdateDocumentRequest.md)|  | [optional] |

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly added continuous project document object. |  -  |

<a id="collectAnalytics"></a>
# **collectAnalytics**
> OperationStatus collectAnalytics(id, analyticsCollection)

Save/collect analytics data from Active widget

Save/collect analytics data from Active widget

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    AnalyticsCollection analyticsCollection = new AnalyticsCollection(); // AnalyticsCollection | 
    try {
      OperationStatus result = apiInstance.collectAnalytics(id, analyticsCollection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#collectAnalytics");
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
| **id** | **Long**| Continuous project ID | |
| **analyticsCollection** | [**AnalyticsCollection**](AnalyticsCollection.md)|  | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Analytics data collection result |  -  |

<a id="complete"></a>
# **complete**
> OperationStatus complete(id)

Complete continuous project

Complete continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    try {
      OperationStatus result = apiInstance.complete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#complete");
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
| **id** | **Long**| Continuous project ID | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation status |  -  |

<a id="completeContinuousDocument"></a>
# **completeContinuousDocument**
> OperationStatus completeContinuousDocument(id, documentId)

Complete a continuous project document

Complete a continuous project document. Per your project settings, a continuous project document can be target language-specific or project-wide for all target languages of the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    Long documentId = 179469L; // Long | Document ID
    try {
      OperationStatus result = apiInstance.completeContinuousDocument(id, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#completeContinuousDocument");
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
| **id** | **Long**| Continuous project ID | |
| **documentId** | **Long**| Document ID | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation status |  -  |
| **404** | ProjectNotFound FileNotFound DocumentNotFound |  -  |

<a id="completeLanguage"></a>
# **completeLanguage**
> OperationStatus completeLanguage(id, targetLanguage)

Complete continuous project language

Complete continuous project language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    String targetLanguage = "en-US"; // String | Target language that you want to complete
    try {
      OperationStatus result = apiInstance.completeLanguage(id, targetLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#completeLanguage");
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
| **id** | **Long**| Continuous project ID | |
| **targetLanguage** | **String**| Target language that you want to complete | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation status |  -  |

<a id="createActiveWidget"></a>
# **createActiveWidget**
> ActiveWidget createActiveWidget(projectId, activeWidget)

Create a new Active widget

Create a new widget for your Active project to be used in your website. Most website-specific configuration is provided via widgets. This does not create a new Active project, just a separate widget.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous project ID
    ActiveWidget activeWidget = new ActiveWidget(); // ActiveWidget | 
    try {
      ActiveWidget result = apiInstance.createActiveWidget(projectId, activeWidget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#createActiveWidget");
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
| **projectId** | **Long**| Continuous project ID | |
| **activeWidget** | [**ActiveWidget**](ActiveWidget.md)|  | [optional] |

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated widget details |  -  |
| **404** | ProjectNotFound | ActiveWidgetNotFound | UnauthorizedUser |  -  |

<a id="createContinuousProject"></a>
# **createContinuousProject**
> ContinuousProject createContinuousProject(continuousProject)

Create a continuous project

Create a new continuous project for your software, website, CI/CD translation needs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    ContinuousProject continuousProject = new ContinuousProject(); // ContinuousProject | 
    try {
      ContinuousProject result = apiInstance.createContinuousProject(continuousProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#createContinuousProject");
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
| **continuousProject** | [**ContinuousProject**](ContinuousProject.md)|  | [optional] |

### Return type

[**ContinuousProject**](ContinuousProject.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created continuous project |  -  |

<a id="createSubscription"></a>
# **createSubscription**
> Subscription createSubscription(id, subscription)

Create subscription for continuous project

Create subscription for continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    Subscription subscription = new Subscription(); // Subscription | 
    try {
      Subscription result = apiInstance.createSubscription(id, subscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#createSubscription");
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
| **id** | **Long**| Continuous project ID | |
| **subscription** | [**Subscription**](Subscription.md)|  | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created continuous project subscription |  -  |
| **400** | MissingParameter |  -  |
| **404** | ProjectNotFound |  -  |

<a id="deleteActiveWidget"></a>
# **deleteActiveWidget**
> OperationStatus deleteActiveWidget(projectId, widgetId)

Delete a single widget for this Active project

Delete a single widget for this Active project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous Project ID
    Long widgetId = 236L; // Long | Active widget ID belonging to this Continuous Project
    try {
      OperationStatus result = apiInstance.deleteActiveWidget(projectId, widgetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#deleteActiveWidget");
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
| **projectId** | **Long**| Continuous Project ID | |
| **widgetId** | **Long**| Active widget ID belonging to this Continuous Project | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete operation result |  -  |
| **404** | ProjectNotFound | ActiveWidgetNotFound | UnauthorizedUser |  -  |

<a id="deleteContinuousProject"></a>
# **deleteContinuousProject**
> OperationStatus deleteContinuousProject(id)

Delete a continuous project

Delete an existing continuous project. Your project will be cancelled, and you will still be charged for the amount of translations we have done for you so far.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    try {
      OperationStatus result = apiInstance.deleteContinuousProject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#deleteContinuousProject");
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
| **id** | **Long**| Continuous project ID | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Continuous project deleted successfully |  -  |
| **404** | ProjectNotFound |  -  |

<a id="deleteSubscription"></a>
# **deleteSubscription**
> Subscription deleteSubscription(id)

Delete subscription for continuous project

Delete subscription for continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    try {
      Subscription result = apiInstance.deleteSubscription(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#deleteSubscription");
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
| **id** | **Long**| Continuous project ID | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete continuous project subscription |  -  |
| **400** | MissingParameter |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getActiveWidget"></a>
# **getActiveWidget**
> ActiveWidget getActiveWidget(projectId, widgetId)

View an Active widget

View the details of an Active widget to be used in your website. Most website-specific configuration is provided via widgets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous Project ID
    Long widgetId = 236L; // Long | Active widget ID belonging to this Continuous Project
    try {
      ActiveWidget result = apiInstance.getActiveWidget(projectId, widgetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getActiveWidget");
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
| **projectId** | **Long**| Continuous Project ID | |
| **widgetId** | **Long**| Active widget ID belonging to this Continuous Project | |

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Active widget details |  -  |
| **404** | ProjectNotFound | ActiveWidgetNotFound |  -  |

<a id="getActiveWidgets"></a>
# **getActiveWidgets**
> ActiveWidgetList getActiveWidgets(projectId)

View Active widgets

View a list of widgets in your Active project to be used in your website. Most website-specific configuration is provided via widgets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous Project ID
    try {
      ActiveWidgetList result = apiInstance.getActiveWidgets(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getActiveWidgets");
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
| **projectId** | **Long**| Continuous Project ID | |

### Return type

[**ActiveWidgetList**](ActiveWidgetList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of widgets |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getAnalyticsToken"></a>
# **getAnalyticsToken**
> AnalyticsToken getAnalyticsToken(id)

Get JWT token to be used in analytics dashboards

Get JWT token to be used in analytics dashboards

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    try {
      AnalyticsToken result = apiInstance.getAnalyticsToken(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getAnalyticsToken");
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
| **id** | **Long**| Continuous project ID | |

### Return type

[**AnalyticsToken**](AnalyticsToken.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JWT token result |  -  |

<a id="getContinuousProject"></a>
# **getContinuousProject**
> ContinuousProject getContinuousProject(id)

View a continuous project

View the details of a continuous project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous Project ID
    try {
      ContinuousProject result = apiInstance.getContinuousProject(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getContinuousProject");
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
| **id** | **Long**| Continuous Project ID | |

### Return type

[**ContinuousProject**](ContinuousProject.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ContinuousProject model |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getContinuousProjectDocument"></a>
# **getContinuousProjectDocument**
> ContinuousProjectDocument getContinuousProjectDocument(projectId, documentId)

View a continuous document

View the details of a source document in continuous translation project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous project ID
    Long documentId = 179469L; // Long | Document ID/Name
    try {
      ContinuousProjectDocument result = apiInstance.getContinuousProjectDocument(projectId, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getContinuousProjectDocument");
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
| **projectId** | **Long**| Continuous project ID | |
| **documentId** | **Long**| Document ID/Name | |

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Progress information |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getContinuousProjectDocumentProgress"></a>
# **getContinuousProjectDocumentProgress**
> Progress getContinuousProjectDocumentProgress(projectId, documentId, filterByLanguage)

Monitor progress of a continuous document

Monitor the translation progress of a document in a continuous project in real-time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous project ID
    Long documentId = 179469L; // Long | Document ID/Name
    String filterByLanguage = "filterByLanguage_example"; // String | 
    try {
      Progress result = apiInstance.getContinuousProjectDocumentProgress(projectId, documentId, filterByLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getContinuousProjectDocumentProgress");
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
| **projectId** | **Long**| Continuous project ID | |
| **documentId** | **Long**| Document ID/Name | |
| **filterByLanguage** | **String**|  | [optional] |

### Return type

[**Progress**](Progress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Progress information |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getContinuousProjectDocuments"></a>
# **getContinuousProjectDocuments**
> ContinuousProjectDocumentList getContinuousProjectDocuments(projectId, filterByLanguage)

View continuous documents

View the documents under this continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous Project ID
    String filterByLanguage = "filterByLanguage_example"; // String | 
    try {
      ContinuousProjectDocumentList result = apiInstance.getContinuousProjectDocuments(projectId, filterByLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getContinuousProjectDocuments");
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
| **projectId** | **Long**| Continuous Project ID | |
| **filterByLanguage** | **String**|  | [optional] |

### Return type

[**ContinuousProjectDocumentList**](ContinuousProjectDocumentList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of continuous project document models |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getContinuousProjectInvoices"></a>
# **getContinuousProjectInvoices**
> ContinuousProjectInvoices getContinuousProjectInvoices(projectId)

Invoices of a continuous project

Get real-time access to a continuous project&#39;s invoices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    try {
      ContinuousProjectInvoices result = apiInstance.getContinuousProjectInvoices(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getContinuousProjectInvoices");
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
| **projectId** | **Long**| Project ID | |

### Return type

[**ContinuousProjectInvoices**](ContinuousProjectInvoices.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoices List |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getContinuousProjectProgress"></a>
# **getContinuousProjectProgress**
> ContinuousProjectProgress getContinuousProjectProgress(projectId, filterByLanguage)

Monitor progress and status of a continous project

Monitor the translation progress of an ongoing continuous project in real-time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Project ID
    String filterByLanguage = "filterByLanguage_example"; // String | 
    try {
      ContinuousProjectProgress result = apiInstance.getContinuousProjectProgress(projectId, filterByLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getContinuousProjectProgress");
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
| **projectId** | **Long**| Project ID | |
| **filterByLanguage** | **String**|  | [optional] |

### Return type

[**ContinuousProjectProgress**](ContinuousProjectProgress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Progress information |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getContinuousProjects"></a>
# **getContinuousProjects**
> ContinuousProjectsList getContinuousProjects(type)

View continuous projects

View a list of continuous projects under your account. Continuous projects are those that are constantly updated, such as a CI/CD project, software project, website translation and such.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    String type = "active"; // String | Type of continuous project.
    try {
      ContinuousProjectsList result = apiInstance.getContinuousProjects(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getContinuousProjects");
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
| **type** | **String**| Type of continuous project. | [optional] [default to active] [enum: active] |

### Return type

[**ContinuousProjectsList**](ContinuousProjectsList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created continuous project |  -  |

<a id="getQuoteForDocument"></a>
# **getQuoteForDocument**
> ProjectList getQuoteForDocument(id, documentId)

Get a quote for a continuous project document

Get a new quote for provided document in continuous project. Per your project settings, a continuous project document can be target language-specific or project-wide for all target languages of the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    Long documentId = 179469L; // Long | Document ID
    try {
      ProjectList result = apiInstance.getQuoteForDocument(id, documentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getQuoteForDocument");
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
| **id** | **Long**| Continuous project ID | |
| **documentId** | **Long**| Document ID | |

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created project |  -  |
| **400** | FileTooLarge FileTooSmall FileWasAlreadyUploaded |  -  |
| **405** | UnsupportedDocumentFormat UnsupportedStyleGuideFormat UnsupportedGlossaryFormat |  -  |
| **406** | UnsupportedLanguage TooManyGlossaries ProjectAlreadyHasGlossary |  -  |
| **500** | ProjectInsertFailed |  -  |

<a id="getQuoteForDocuments"></a>
# **getQuoteForDocuments**
> ProjectList getQuoteForDocuments(id, getQuotesForDocumentsBody)

Get quote for documents

Get a new quote for provided documents in continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    GetQuotesForDocumentsBody getQuotesForDocumentsBody = new GetQuotesForDocumentsBody(); // GetQuotesForDocumentsBody | 
    try {
      ProjectList result = apiInstance.getQuoteForDocuments(id, getQuotesForDocumentsBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getQuoteForDocuments");
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
| **id** | **Long**| Continuous project ID | |
| **getQuotesForDocumentsBody** | [**GetQuotesForDocumentsBody**](GetQuotesForDocumentsBody.md)|  | [optional] |

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created project |  -  |
| **400** | FileTooLarge FileTooSmall FileWasAlreadyUploaded |  -  |
| **405** | UnsupportedDocumentFormat UnsupportedStyleGuideFormat UnsupportedGlossaryFormat |  -  |
| **406** | UnsupportedLanguage TooManyGlossaries ProjectAlreadyHasGlossary |  -  |
| **500** | ProjectInsertFailed |  -  |

<a id="getQuoteForLanguage"></a>
# **getQuoteForLanguage**
> ProjectList getQuoteForLanguage(id, targetLanguage)

Get quote for language

Get a new quote for provided target language in continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    String targetLanguage = "en-US"; // String | Target language that you want to complete
    try {
      ProjectList result = apiInstance.getQuoteForLanguage(id, targetLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getQuoteForLanguage");
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
| **id** | **Long**| Continuous project ID | |
| **targetLanguage** | **String**| Target language that you want to complete | |

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created project(s) |  -  |
| **400** | FileTooLarge FileTooSmall FileWasAlreadyUploaded |  -  |
| **405** | UnsupportedDocumentFormat UnsupportedStyleGuideFormat UnsupportedGlossaryFormat |  -  |
| **406** | UnsupportedLanguage TooManyGlossaries ProjectAlreadyHasGlossary |  -  |
| **500** | ProjectInsertFailed |  -  |

<a id="getQuoteForLanguages"></a>
# **getQuoteForLanguages**
> ProjectList getQuoteForLanguages(id, getQuotesForLanguagesBody)

Get quote for languages

Get a new quote for provided target languages in continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    GetQuotesForLanguagesBody getQuotesForLanguagesBody = new GetQuotesForLanguagesBody(); // GetQuotesForLanguagesBody | 
    try {
      ProjectList result = apiInstance.getQuoteForLanguages(id, getQuotesForLanguagesBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getQuoteForLanguages");
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
| **id** | **Long**| Continuous project ID | |
| **getQuotesForLanguagesBody** | [**GetQuotesForLanguagesBody**](GetQuotesForLanguagesBody.md)|  | [optional] |

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newly created project |  -  |
| **400** | FileTooLarge FileTooSmall FileWasAlreadyUploaded |  -  |
| **405** | UnsupportedDocumentFormat UnsupportedStyleGuideFormat UnsupportedGlossaryFormat |  -  |
| **406** | UnsupportedLanguage TooManyGlossaries ProjectAlreadyHasGlossary |  -  |
| **500** | ProjectInsertFailed |  -  |

<a id="getSubscription"></a>
# **getSubscription**
> Subscription getSubscription(id)

Get subscription for continuous project

Get subscription for continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    try {
      Subscription result = apiInstance.getSubscription(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#getSubscription");
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
| **id** | **Long**| Continuous project ID | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get continuous project subscription |  -  |
| **400** | MissingParameter |  -  |
| **404** | ProjectNotFound |  -  |

<a id="postContinuousProjectDocumentProgress"></a>
# **postContinuousProjectDocumentProgress**
> Progress postContinuousProjectDocumentProgress(projectId, continuousProjectDocumentProgressBody)

Get continuous project document progress for multiple IDs

Get continuous project document progress for multiple IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous project ID
    ContinuousProjectDocumentProgressBody continuousProjectDocumentProgressBody = new ContinuousProjectDocumentProgressBody(); // ContinuousProjectDocumentProgressBody | 
    try {
      Progress result = apiInstance.postContinuousProjectDocumentProgress(projectId, continuousProjectDocumentProgressBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#postContinuousProjectDocumentProgress");
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
| **projectId** | **Long**| Continuous project ID | |
| **continuousProjectDocumentProgressBody** | [**ContinuousProjectDocumentProgressBody**](ContinuousProjectDocumentProgressBody.md)|  | [optional] |

### Return type

[**Progress**](Progress.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Progress information |  -  |
| **404** | ProjectNotFound |  -  |

<a id="resetActiveWidgetToken"></a>
# **resetActiveWidgetToken**
> ActiveWidget resetActiveWidgetToken(projectId, widgetId)

Reset Active widget token

Reset the public token used with your Active widget. This token is used when communicating from your environment to MotaWord systems for translation, analytics and meta.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous Project ID
    Long widgetId = 236L; // Long | Active widget ID belonging to this Continuous Project
    try {
      ActiveWidget result = apiInstance.resetActiveWidgetToken(projectId, widgetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#resetActiveWidgetToken");
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
| **projectId** | **Long**| Continuous Project ID | |
| **widgetId** | **Long**| Active widget ID belonging to this Continuous Project | |

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated widget details |  -  |
| **404** | ProjectNotFound | ActiveWidgetNotFound | UnauthorizedUser |  -  |

<a id="translate"></a>
# **translate**
> InstantTranslationResult translate(id, targetLanguage, instantTranslationRequest)

Instantly translate your content

Instantly translate your content with your existing TM and MT resources. This is the primary endpoint to translate your files and content on the fly, especially in CI/CD environments. This is a complex endpoint that is configured in your Active or Continuous Project dashboards. For instance, you can configure whether to use your TM, or translate missing strings via MT and then post-edit those new translations. There are various scenarios you can establish via a set of configurations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    String targetLanguage = "en-US"; // String | Target language that you want to instantly translate your file into.
    InstantTranslationRequest instantTranslationRequest = new InstantTranslationRequest(); // InstantTranslationRequest | 
    try {
      InstantTranslationResult result = apiInstance.translate(id, targetLanguage, instantTranslationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#translate");
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
| **id** | **Long**| Continuous project ID | |
| **targetLanguage** | **String**| Target language that you want to instantly translate your file into. | |
| **instantTranslationRequest** | [**InstantTranslationRequest**](InstantTranslationRequest.md)|  | [optional] |

### Return type

[**InstantTranslationResult**](InstantTranslationResult.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instant translation result. It may return a list of translated strings, or a list of translated files. |  -  |

<a id="updateActiveWidget"></a>
# **updateActiveWidget**
> ActiveWidget updateActiveWidget(projectId, widgetId, activeWidget)

Update Active widget settings.

Update Active widget settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous Project ID
    Long widgetId = 236L; // Long | Active widget ID belonging to this Continuous Project
    ActiveWidget activeWidget = new ActiveWidget(); // ActiveWidget | 
    try {
      ActiveWidget result = apiInstance.updateActiveWidget(projectId, widgetId, activeWidget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#updateActiveWidget");
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
| **projectId** | **Long**| Continuous Project ID | |
| **widgetId** | **Long**| Active widget ID belonging to this Continuous Project | |
| **activeWidget** | [**ActiveWidget**](ActiveWidget.md)|  | [optional] |

### Return type

[**ActiveWidget**](ActiveWidget.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated widget details |  -  |
| **404** | ProjectNotFound | ActiveWidgetNotFound | UnauthorizedUser |  -  |

<a id="updateContinuousProject"></a>
# **updateContinuousProject**
> ContinuousProject updateContinuousProject(id, continuousProjectUpdateContent)

Update a continuous project

Update the details and settings of continuous project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    ContinuousProjectUpdateContent continuousProjectUpdateContent = new ContinuousProjectUpdateContent(); // ContinuousProjectUpdateContent | 
    try {
      ContinuousProject result = apiInstance.updateContinuousProject(id, continuousProjectUpdateContent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#updateContinuousProject");
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
| **id** | **Long**| Continuous project ID | |
| **continuousProjectUpdateContent** | [**ContinuousProjectUpdateContent**](ContinuousProjectUpdateContent.md)|  | [optional] |

### Return type

[**ContinuousProject**](ContinuousProject.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update continuous project operation status |  -  |
| **404** | ProjectNotFound |  -  |

<a id="updateDocument"></a>
# **updateDocument**
> ContinuousProjectDocument updateDocument(projectId, documentId, addOrUpdateDocumentRequest)

Update the document

Update source document in your continuous project. In most scenarios, this operation will also trigger auto-translation of your document, via MT and/or TM.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long projectId = 74L; // Long | Continuous project ID
    Long documentId = 179469L; // Long | Continuous project document ID
    AddOrUpdateDocumentRequest addOrUpdateDocumentRequest = new AddOrUpdateDocumentRequest(); // AddOrUpdateDocumentRequest | 
    try {
      ContinuousProjectDocument result = apiInstance.updateDocument(projectId, documentId, addOrUpdateDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#updateDocument");
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
| **projectId** | **Long**| Continuous project ID | |
| **documentId** | **Long**| Continuous project document ID | |
| **addOrUpdateDocumentRequest** | [**AddOrUpdateDocumentRequest**](AddOrUpdateDocumentRequest.md)|  | [optional] |

### Return type

[**ContinuousProjectDocument**](ContinuousProjectDocument.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated continuous project document object. |  -  |

<a id="updateSubscription"></a>
# **updateSubscription**
> Subscription updateSubscription(id, subscription)

Update subscription for continuous project

Update subscription for continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    Subscription subscription = new Subscription(); // Subscription | 
    try {
      Subscription result = apiInstance.updateSubscription(id, subscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#updateSubscription");
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
| **id** | **Long**| Continuous project ID | |
| **subscription** | [**Subscription**](Subscription.md)|  | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated continuous project subscription |  -  |
| **400** | MissingParameter |  -  |
| **404** | ProjectNotFound |  -  |

<a id="updateSubscriptionPaymentMethod"></a>
# **updateSubscriptionPaymentMethod**
> Subscription updateSubscriptionPaymentMethod(id, subscription)

Update subscription payment method for continuous project

Update subscription payment method for continuous project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContinuousProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ContinuousProjectApi apiInstance = new ContinuousProjectApi(defaultClient);
    Long id = 74L; // Long | Continuous project ID
    Subscription subscription = new Subscription(); // Subscription | 
    try {
      Subscription result = apiInstance.updateSubscriptionPaymentMethod(id, subscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContinuousProjectApi#updateSubscriptionPaymentMethod");
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
| **id** | **Long**| Continuous project ID | |
| **subscription** | [**Subscription**](Subscription.md)|  | |

### Return type

[**Subscription**](Subscription.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated continuous project subscription |  -  |
| **400** | MissingParameter |  -  |
| **404** | ProjectNotFound |  -  |

