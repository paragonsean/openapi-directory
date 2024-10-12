# RiskFactorsApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllRiskFactors**](RiskFactorsApi.md#getAllRiskFactors) | **GET** /risk_factors | List all risk factors |
| [**getRiskFactor**](RiskFactorsApi.md#getRiskFactor) | **GET** /risk_factors/{id} | Get risk factor by id |


<a id="getAllRiskFactors"></a>
# **getAllRiskFactors**
> List&lt;RiskFactorPublic&gt; getAllRiskFactors(ageValue, ageUnit, enableTriage5)

List all risk factors

Returns a list of all available risk factors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RiskFactorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    RiskFactorsApi apiInstance = new RiskFactorsApi(defaultClient);
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    Boolean enableTriage5 = true; // Boolean | enable 5-level triage values
    try {
      List<RiskFactorPublic> result = apiInstance.getAllRiskFactors(ageValue, ageUnit, enableTriage5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RiskFactorsApi#getAllRiskFactors");
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

[**List&lt;RiskFactorPublic&gt;**](RiskFactorPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getRiskFactor"></a>
# **getRiskFactor**
> RiskFactorDetails getRiskFactor(id, ageValue, ageUnit, enableTriage5)

Get risk factor by id

Returns details of a single risk factor specified by id parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RiskFactorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    RiskFactorsApi apiInstance = new RiskFactorsApi(defaultClient);
    String id = "id_example"; // String | risk factor id
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    Boolean enableTriage5 = true; // Boolean | enable 5-level triage values
    try {
      RiskFactorDetails result = apiInstance.getRiskFactor(id, ageValue, ageUnit, enableTriage5);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RiskFactorsApi#getRiskFactor");
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
| **id** | **String**| risk factor id | |
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |
| **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] |

### Return type

[**RiskFactorDetails**](RiskFactorDetails.md)

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
| **404** | Risk factor not found |  -  |

