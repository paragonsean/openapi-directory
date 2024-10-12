# BillingApi

All URIs are relative to *https://app.drchrono.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingProfilesList**](BillingApi.md#billingProfilesList) | **GET** /api/billing_profiles |  |
| [**billingProfilesRead**](BillingApi.md#billingProfilesRead) | **GET** /api/billing_profiles/{id} |  |
| [**commLogsCreate**](BillingApi.md#commLogsCreate) | **POST** /api/comm_logs |  |
| [**commLogsList**](BillingApi.md#commLogsList) | **GET** /api/comm_logs |  |
| [**commLogsPartialUpdate**](BillingApi.md#commLogsPartialUpdate) | **PATCH** /api/comm_logs/{id} |  |
| [**commLogsRead**](BillingApi.md#commLogsRead) | **GET** /api/comm_logs/{id} |  |
| [**commLogsUpdate**](BillingApi.md#commLogsUpdate) | **PUT** /api/comm_logs/{id} |  |
| [**customInsurancePlanNamesList**](BillingApi.md#customInsurancePlanNamesList) | **GET** /api/custom_insurance_plan_names |  |
| [**customInsurancePlanNamesRead**](BillingApi.md#customInsurancePlanNamesRead) | **GET** /api/custom_insurance_plan_names/{id} |  |
| [**eligibilityChecksList**](BillingApi.md#eligibilityChecksList) | **GET** /api/eligibility_checks |  |
| [**eligibilityChecksRead**](BillingApi.md#eligibilityChecksRead) | **GET** /api/eligibility_checks/{id} |  |
| [**lineItemsCreate**](BillingApi.md#lineItemsCreate) | **POST** /api/line_items |  |
| [**lineItemsDelete**](BillingApi.md#lineItemsDelete) | **DELETE** /api/line_items/{id} |  |
| [**lineItemsList**](BillingApi.md#lineItemsList) | **GET** /api/line_items |  |
| [**lineItemsPartialUpdate**](BillingApi.md#lineItemsPartialUpdate) | **PATCH** /api/line_items/{id} |  |
| [**lineItemsRead**](BillingApi.md#lineItemsRead) | **GET** /api/line_items/{id} |  |
| [**lineItemsUpdate**](BillingApi.md#lineItemsUpdate) | **PUT** /api/line_items/{id} |  |
| [**patientPaymentLogList**](BillingApi.md#patientPaymentLogList) | **GET** /api/patient_payment_log |  |
| [**patientPaymentLogRead**](BillingApi.md#patientPaymentLogRead) | **GET** /api/patient_payment_log/{id} |  |
| [**patientPaymentsCreate**](BillingApi.md#patientPaymentsCreate) | **POST** /api/patient_payments |  |
| [**patientPaymentsList**](BillingApi.md#patientPaymentsList) | **GET** /api/patient_payments |  |
| [**patientPaymentsRead**](BillingApi.md#patientPaymentsRead) | **GET** /api/patient_payments/{id} |  |
| [**proceduresList**](BillingApi.md#proceduresList) | **GET** /api/procedures |  |
| [**proceduresRead**](BillingApi.md#proceduresRead) | **GET** /api/procedures/{id} |  |
| [**transactionsList**](BillingApi.md#transactionsList) | **GET** /api/transactions |  |
| [**transactionsRead**](BillingApi.md#transactionsRead) | **GET** /api/transactions/{id} |  |


<a id="billingProfilesList"></a>
# **billingProfilesList**
> BillingProfilesList200Response billingProfilesList(cursor, pageSize, doctor)



Retrieve or search billing profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      BillingProfilesList200Response result = apiInstance.billingProfilesList(cursor, pageSize, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingProfilesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**BillingProfilesList200Response**](BillingProfilesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="billingProfilesRead"></a>
# **billingProfilesRead**
> BillingProfile billingProfilesRead(id, doctor)



Retrieve an existing billing profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      BillingProfile result = apiInstance.billingProfilesRead(id, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#billingProfilesRead");
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
| **id** | **String**|  | |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**BillingProfile**](BillingProfile.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="commLogsCreate"></a>
# **commLogsCreate**
> PhoneCallLog commLogsCreate(since, patient, doctor)



Create communication (phone call) logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      PhoneCallLog result = apiInstance.commLogsCreate(since, patient, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#commLogsCreate");
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
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**PhoneCallLog**](PhoneCallLog.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="commLogsList"></a>
# **commLogsList**
> CommLogsList200Response commLogsList(cursor, pageSize, since, patient, doctor)



Retrieve or search communicatioin (phone call) logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      CommLogsList200Response result = apiInstance.commLogsList(cursor, pageSize, since, patient, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#commLogsList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**CommLogsList200Response**](CommLogsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="commLogsPartialUpdate"></a>
# **commLogsPartialUpdate**
> commLogsPartialUpdate(id, since, patient, doctor)



Update an existing communication (phone call) logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      apiInstance.commLogsPartialUpdate(id, since, patient, doctor);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#commLogsPartialUpdate");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="commLogsRead"></a>
# **commLogsRead**
> PhoneCallLog commLogsRead(id, since, patient, doctor)



Retrieve an existing communication (phone call) logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      PhoneCallLog result = apiInstance.commLogsRead(id, since, patient, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#commLogsRead");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**PhoneCallLog**](PhoneCallLog.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="commLogsUpdate"></a>
# **commLogsUpdate**
> commLogsUpdate(id, since, patient, doctor)



Update an existing communication (phone call) logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      apiInstance.commLogsUpdate(id, since, patient, doctor);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#commLogsUpdate");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="customInsurancePlanNamesList"></a>
# **customInsurancePlanNamesList**
> CustomInsurancePlanNamesList200Response customInsurancePlanNamesList(cursor, pageSize, since, user, name, doctor)



Retrieve or search custom insurance plan names

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer user = 56; // Integer | 
    String name = "name_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      CustomInsurancePlanNamesList200Response result = apiInstance.customInsurancePlanNamesList(cursor, pageSize, since, user, name, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#customInsurancePlanNamesList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **user** | **Integer**|  | [optional] |
| **name** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**CustomInsurancePlanNamesList200Response**](CustomInsurancePlanNamesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="customInsurancePlanNamesRead"></a>
# **customInsurancePlanNamesRead**
> CustomInsurancePlanName customInsurancePlanNamesRead(id, since, user, name, doctor)



Retrieve an existing custom insurance plan name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    Integer user = 56; // Integer | 
    String name = "name_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      CustomInsurancePlanName result = apiInstance.customInsurancePlanNamesRead(id, since, user, name, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#customInsurancePlanNamesRead");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |
| **user** | **Integer**|  | [optional] |
| **name** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**CustomInsurancePlanName**](CustomInsurancePlanName.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="eligibilityChecksList"></a>
# **eligibilityChecksList**
> EligibilityChecksList200Response eligibilityChecksList(cursor, pageSize, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient)



Retrieve or search past eligibility checks for patient

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer appointment = 56; // Integer | 
    String appointmentDate = "appointmentDate_example"; // String | 
    Integer doctor = 56; // Integer | 
    String queryDateRange = "queryDateRange_example"; // String | 
    String appointmentDateRange = "appointmentDateRange_example"; // String | 
    String queryDate = "queryDate_example"; // String | 
    Integer patient = 56; // Integer | 
    try {
      EligibilityChecksList200Response result = apiInstance.eligibilityChecksList(cursor, pageSize, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#eligibilityChecksList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **appointmentDate** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **queryDateRange** | **String**|  | [optional] |
| **appointmentDateRange** | **String**|  | [optional] |
| **queryDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |

### Return type

[**EligibilityChecksList200Response**](EligibilityChecksList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="eligibilityChecksRead"></a>
# **eligibilityChecksRead**
> Coverage eligibilityChecksRead(id, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient)



Retrieve an existing past eligibility check

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    Integer appointment = 56; // Integer | 
    String appointmentDate = "appointmentDate_example"; // String | 
    Integer doctor = 56; // Integer | 
    String queryDateRange = "queryDateRange_example"; // String | 
    String appointmentDateRange = "appointmentDateRange_example"; // String | 
    String queryDate = "queryDate_example"; // String | 
    Integer patient = 56; // Integer | 
    try {
      Coverage result = apiInstance.eligibilityChecksRead(id, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#eligibilityChecksRead");
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
| **id** | **String**|  | |
| **appointment** | **Integer**|  | [optional] |
| **appointmentDate** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **queryDateRange** | **String**|  | [optional] |
| **appointmentDateRange** | **String**|  | [optional] |
| **queryDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |

### Return type

[**Coverage**](Coverage.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="lineItemsCreate"></a>
# **lineItemsCreate**
> BillingLineItem lineItemsCreate(postedDate, patient, office, doctor, since, appointment, serviceDate)



Create billing line item for appointments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String postedDate = "postedDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      BillingLineItem result = apiInstance.lineItemsCreate(postedDate, patient, office, doctor, since, appointment, serviceDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#lineItemsCreate");
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
| **postedDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

[**BillingLineItem**](BillingLineItem.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="lineItemsDelete"></a>
# **lineItemsDelete**
> lineItemsDelete(id, postedDate, patient, office, doctor, since, appointment, serviceDate)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String postedDate = "postedDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      apiInstance.lineItemsDelete(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#lineItemsDelete");
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
| **id** | **String**|  | |
| **postedDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="lineItemsList"></a>
# **lineItemsList**
> LineItemsList200Response lineItemsList(cursor, pageSize, postedDate, patient, office, doctor, since, appointment, serviceDate)



Retrieve or search billing line items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String postedDate = "postedDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      LineItemsList200Response result = apiInstance.lineItemsList(cursor, pageSize, postedDate, patient, office, doctor, since, appointment, serviceDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#lineItemsList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **postedDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

[**LineItemsList200Response**](LineItemsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="lineItemsPartialUpdate"></a>
# **lineItemsPartialUpdate**
> lineItemsPartialUpdate(id, postedDate, patient, office, doctor, since, appointment, serviceDate)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String postedDate = "postedDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      apiInstance.lineItemsPartialUpdate(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#lineItemsPartialUpdate");
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
| **id** | **String**|  | |
| **postedDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="lineItemsRead"></a>
# **lineItemsRead**
> BillingLineItem lineItemsRead(id, postedDate, patient, office, doctor, since, appointment, serviceDate)



Retrieve an existing billing line item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String postedDate = "postedDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      BillingLineItem result = apiInstance.lineItemsRead(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#lineItemsRead");
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
| **id** | **String**|  | |
| **postedDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

[**BillingLineItem**](BillingLineItem.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="lineItemsUpdate"></a>
# **lineItemsUpdate**
> lineItemsUpdate(id, postedDate, patient, office, doctor, since, appointment, serviceDate)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String postedDate = "postedDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      apiInstance.lineItemsUpdate(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#lineItemsUpdate");
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
| **id** | **String**|  | |
| **postedDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="patientPaymentLogList"></a>
# **patientPaymentLogList**
> PatientPaymentLogList200Response patientPaymentLogList(cursor, pageSize, since, office, doctor)



Retrieve or search patient payment logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      PatientPaymentLogList200Response result = apiInstance.patientPaymentLogList(cursor, pageSize, since, office, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#patientPaymentLogList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**PatientPaymentLogList200Response**](PatientPaymentLogList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="patientPaymentLogRead"></a>
# **patientPaymentLogRead**
> CashPaymentLog patientPaymentLogRead(id, since, office, doctor)



Retrieve an existing patient payment log

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    Integer office = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      CashPaymentLog result = apiInstance.patientPaymentLogRead(id, since, office, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#patientPaymentLogRead");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |
| **office** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**CashPaymentLog**](CashPaymentLog.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="patientPaymentsCreate"></a>
# **patientPaymentsCreate**
> CashPayment patientPaymentsCreate(since, patient, doctor)



Create patient payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      CashPayment result = apiInstance.patientPaymentsCreate(since, patient, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#patientPaymentsCreate");
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
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**CashPayment**](CashPayment.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="patientPaymentsList"></a>
# **patientPaymentsList**
> PatientPaymentsList200Response patientPaymentsList(cursor, pageSize, since, patient, doctor)



Retrieve or search patient payments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      PatientPaymentsList200Response result = apiInstance.patientPaymentsList(cursor, pageSize, since, patient, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#patientPaymentsList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**PatientPaymentsList200Response**](PatientPaymentsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="patientPaymentsRead"></a>
# **patientPaymentsRead**
> CashPayment patientPaymentsRead(id, since, patient, doctor)



Retrieve an existing patient payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String since = "since_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      CashPayment result = apiInstance.patientPaymentsRead(id, since, patient, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#patientPaymentsRead");
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
| **id** | **String**|  | |
| **since** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**CashPayment**](CashPayment.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="proceduresList"></a>
# **proceduresList**
> LineItemsList200Response proceduresList(cursor, pageSize, muDate, patient, doctor, muDateRange, appointment, serviceDate)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    String muDate = "muDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String muDateRange = "muDateRange_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      LineItemsList200Response result = apiInstance.proceduresList(cursor, pageSize, muDate, patient, doctor, muDateRange, appointment, serviceDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#proceduresList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **muDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **muDateRange** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

[**LineItemsList200Response**](LineItemsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="proceduresRead"></a>
# **proceduresRead**
> BillingLineItem proceduresRead(id, muDate, patient, doctor, muDateRange, appointment, serviceDate)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    String muDate = "muDate_example"; // String | 
    Integer patient = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    String muDateRange = "muDateRange_example"; // String | 
    Integer appointment = 56; // Integer | 
    String serviceDate = "serviceDate_example"; // String | 
    try {
      BillingLineItem result = apiInstance.proceduresRead(id, muDate, patient, doctor, muDateRange, appointment, serviceDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#proceduresRead");
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
| **id** | **String**|  | |
| **muDate** | **String**|  | [optional] |
| **patient** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |
| **muDateRange** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **serviceDate** | **String**|  | [optional] |

### Return type

[**BillingLineItem**](BillingLineItem.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="transactionsList"></a>
# **transactionsList**
> TransactionsList200Response transactionsList(cursor, pageSize, lineItem, postedDate, appointment, since, doctor)



Retrieve or search insurance transactions associated with billing line items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer lineItem = 56; // Integer | 
    String postedDate = "postedDate_example"; // String | 
    Integer appointment = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      TransactionsList200Response result = apiInstance.transactionsList(cursor, pageSize, lineItem, postedDate, appointment, since, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#transactionsList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **lineItem** | **Integer**|  | [optional] |
| **postedDate** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**TransactionsList200Response**](TransactionsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="transactionsRead"></a>
# **transactionsRead**
> LineItemTransaction transactionsRead(id, lineItem, postedDate, appointment, since, doctor)



Retrieve an existing insurance transaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BillingApi apiInstance = new BillingApi(defaultClient);
    String id = "id_example"; // String | 
    Integer lineItem = 56; // Integer | 
    String postedDate = "postedDate_example"; // String | 
    Integer appointment = 56; // Integer | 
    String since = "since_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      LineItemTransaction result = apiInstance.transactionsRead(id, lineItem, postedDate, appointment, since, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingApi#transactionsRead");
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
| **id** | **String**|  | |
| **lineItem** | **Integer**|  | [optional] |
| **postedDate** | **String**|  | [optional] |
| **appointment** | **Integer**|  | [optional] |
| **since** | **String**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**LineItemTransaction**](LineItemTransaction.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

