# SymptomsApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllSymptoms**](SymptomsApi.md#getAllSymptoms) | **GET** /symptoms | List all symptoms |
| [**getSymptom**](SymptomsApi.md#getSymptom) | **GET** /symptoms/{id} | Get symptoms by id |


<a id="getAllSymptoms"></a>
# **getAllSymptoms**
> List&lt;SymptomPublic&gt; getAllSymptoms(ageValue, ageUnit, enableTriage5)

List all symptoms

Returns a list of all available symptoms.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SymptomsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    SymptomsApi apiInstance = new SymptomsApi(defaultClient);
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    Boolean enableTriage5 = true; // Boolean | enable 5-level triage values
    try {
      List<SymptomPublic> result = apiInstance.getAllSymptoms(ageValue, ageUnit, enableTriage5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SymptomsApi#getAllSymptoms");
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
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |
| **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] |

### Return type

[**List&lt;SymptomPublic&gt;**](SymptomPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getSymptom"></a>
# **getSymptom**
> SymptomDetails getSymptom(id, ageValue, ageUnit, enableTriage5)

Get symptoms by id

Returns details of a single symptom specified by id parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SymptomsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    SymptomsApi apiInstance = new SymptomsApi(defaultClient);
    String id = "id_example"; // String | symptoms id
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    Boolean enableTriage5 = true; // Boolean | enable 5-level triage values
    try {
      SymptomDetails result = apiInstance.getSymptom(id, ageValue, ageUnit, enableTriage5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SymptomsApi#getSymptom");
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
| **id** | **String**| symptoms id | |
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |
| **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] |

### Return type

[**SymptomDetails**](SymptomDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid id specified |  -  |
| **404** | symptom not found |  -  |

