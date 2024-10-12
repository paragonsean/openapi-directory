# VirtualMeterCalculateFormulaApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMeterCalculateFormulaGet**](VirtualMeterCalculateFormulaApi.md#virtualMeterCalculateFormulaGet) | **GET** /api/VirtualMeterCalculateFormula | Calculates a virtual meter from a formula.               A meter is coded as ID(\&quot;METERID\&quot;) |


<a id="virtualMeterCalculateFormulaGet"></a>
# **virtualMeterCalculateFormulaGet**
> Device virtualMeterCalculateFormulaGet(formula)

Calculates a virtual meter from a formula.               A meter is coded as ID(\&quot;METERID\&quot;)

Calculates a virtual meter from a formula.                            A meter is coded as ID(\&quot;METERID\&quot;)              Ariphmetical operators:               ()  parentheses;                 +   plus (a + b);                -  minus (a - b);                *  multiplycation symbol (a * b);                /  divide symbol (a / b);               Example: (ID(\&quot;63ac09cb-4e5f-4f3e-bd27-ad8c30bdfc0c\&quot;) + ID(\&quot;0209555e-9dc4-4e84-a166-a864488b4b12\&quot;)) * 2

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMeterCalculateFormulaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    VirtualMeterCalculateFormulaApi apiInstance = new VirtualMeterCalculateFormulaApi(defaultClient);
    String formula = "formula_example"; // String | 
    try {
      Device result = apiInstance.virtualMeterCalculateFormulaGet(formula);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMeterCalculateFormulaApi#virtualMeterCalculateFormulaGet");
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
| **formula** | **String**|  | |

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

