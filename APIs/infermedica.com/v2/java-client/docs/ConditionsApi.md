# ConditionsApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllConditions**](ConditionsApi.md#getAllConditions) | **GET** /conditions | List all conditions |
| [**getCondition**](ConditionsApi.md#getCondition) | **GET** /conditions/{id} | Get condition by id |


<a id="getAllConditions"></a>
# **getAllConditions**
> List&lt;ConditionPublic&gt; getAllConditions(ageValue, ageUnit, enableTriage5)

List all conditions

Returns a list of all available conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConditionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    ConditionsApi apiInstance = new ConditionsApi(defaultClient);
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    Boolean enableTriage5 = true; // Boolean | enable 5-level triage values
    try {
      List<ConditionPublic> result = apiInstance.getAllConditions(ageValue, ageUnit, enableTriage5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConditionsApi#getAllConditions");
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

[**List&lt;ConditionPublic&gt;**](ConditionPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getCondition"></a>
# **getCondition**
> ConditionDetails getCondition(id, ageValue, ageUnit, enableTriage5)

Get condition by id

Returns details of a single condition specified by id parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConditionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    ConditionsApi apiInstance = new ConditionsApi(defaultClient);
    String id = "id_example"; // String | condition id
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    Boolean enableTriage5 = true; // Boolean | enable 5-level triage values
    try {
      ConditionDetails result = apiInstance.getCondition(id, ageValue, ageUnit, enableTriage5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConditionsApi#getCondition");
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
| **id** | **String**| condition id | |
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |
| **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] |

### Return type

[**ConditionDetails**](ConditionDetails.md)

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
| **404** | Condition not found |  -  |

