# HoldingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssetClassificationList**](HoldingsApi.md#getAssetClassificationList) | **GET** /holdings/assetClassificationList | Get Asset Classification List |
| [**getHoldingTypeList**](HoldingsApi.md#getHoldingTypeList) | **GET** /holdings/holdingTypeList | Get Holding Type List |
| [**getHoldings**](HoldingsApi.md#getHoldings) | **GET** /holdings | Get Holdings |
| [**getSecurities**](HoldingsApi.md#getSecurities) | **GET** /holdings/securities | Get Security Details |


<a id="getAssetClassificationList"></a>
# **getAssetClassificationList**
> HoldingAssetClassificationListResponse getAssetClassificationList()

Get Asset Classification List

The get asset classifications list service is used to get the supported asset classifications. &lt;br&gt;The response includes different classification types like assetClass, country, sector, style, etc. and the values corresponding to each type.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoldingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HoldingsApi apiInstance = new HoldingsApi(defaultClient);
    try {
      HoldingAssetClassificationListResponse result = apiInstance.getAssetClassificationList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoldingsApi#getAssetClassificationList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HoldingAssetClassificationListResponse**](HoldingAssetClassificationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getHoldingTypeList"></a>
# **getHoldingTypeList**
> HoldingTypeListResponse getHoldingTypeList()

Get Holding Type List

The get holding types list service is used to get the supported holding types.&lt;br&gt;The response includes different holding types such as future, moneyMarketFund, stock, etc. and it returns the supported holding types &lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoldingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HoldingsApi apiInstance = new HoldingsApi(defaultClient);
    try {
      HoldingTypeListResponse result = apiInstance.getHoldingTypeList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoldingsApi#getHoldingTypeList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HoldingTypeListResponse**](HoldingTypeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getHoldings"></a>
# **getHoldings**
> HoldingResponse getHoldings(accountId, assetClassificationClassificationType, classificationValue, include, providerAccountId)

Get Holdings

The get holdings service is used to get the list of holdings of a user.&lt;br&gt;Supported holding types can be employeeStockOption, moneyMarketFund, bond, etc. and is obtained using get holding type list service. &lt;br&gt;Asset classifications for the holdings need to be requested through the \&quot;include\&quot; parameter.&lt;br&gt;Asset classification information for holdings are not available by default, as it is a premium feature.&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoldingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HoldingsApi apiInstance = new HoldingsApi(defaultClient);
    String accountId = "accountId_example"; // String | Comma separated accountId
    String assetClassificationClassificationType = "assetClassificationClassificationType_example"; // String | e.g. Country, Sector, etc.
    String classificationValue = "classificationValue_example"; // String | e.g. US
    String include = "include_example"; // String | assetClassification
    String providerAccountId = "providerAccountId_example"; // String | providerAccountId
    try {
      HoldingResponse result = apiInstance.getHoldings(accountId, assetClassificationClassificationType, classificationValue, include, providerAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoldingsApi#getHoldings");
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
| **accountId** | **String**| Comma separated accountId | [optional] |
| **assetClassificationClassificationType** | **String**| e.g. Country, Sector, etc. | [optional] |
| **classificationValue** | **String**| e.g. US | [optional] |
| **include** | **String**| assetClassification | [optional] |
| **providerAccountId** | **String**| providerAccountId | [optional] |

### Return type

[**HoldingResponse**](HoldingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for providerAccountId&lt;br&gt;Y800 : Invalid value for include&lt;br&gt;Y800 : Invalid value for classificationType&lt;br&gt;Y800 : Invalid value for classificationValue&lt;br&gt;Y800 : Invalid value for include&lt;br&gt;Y400 : classificationType mismatch&lt;br&gt;Y400 : classificationValue mismatch&lt;br&gt;Y824 : The maximum number of accountIds permitted is 100 |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getSecurities"></a>
# **getSecurities**
> HoldingSecuritiesResponse getSecurities(holdingId)

Get Security Details

The get security details service is used to get all the security information for the holdings&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HoldingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    HoldingsApi apiInstance = new HoldingsApi(defaultClient);
    String holdingId = "holdingId_example"; // String | Comma separated holdingId
    try {
      HoldingSecuritiesResponse result = apiInstance.getSecurities(holdingId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HoldingsApi#getSecurities");
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
| **holdingId** | **String**| Comma separated holdingId | [optional] |

### Return type

[**HoldingSecuritiesResponse**](HoldingSecuritiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for holdingId&lt;br&gt;Y824 : The maximum number of holdingIds permitted is 100 |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

