# SalesControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesControllerGetAdvertisedSales**](SalesControllerApi.md#salesControllerGetAdvertisedSales) | **GET** /v2/tier1/{shortName}/sales/advertisedsales | Search all sales properties available given a range of search criteria |
| [**salesControllerGetEER**](SalesControllerApi.md#salesControllerGetEER) | **GET** /v2/tier1/{shortName}/sales/reports/eer/{salesInstructionID} | Downloads the energy efficiency report (EER) graph for a sales instruction |
| [**salesControllerGetEIR**](SalesControllerApi.md#salesControllerGetEIR) | **GET** /v2/tier1/{shortName}/sales/reports/eir/{salesInstructionID} | Downloads the energy efficiency report (EIR) graph for a sales instruction |
| [**salesControllerGetSalesInstructionsFeatures**](SalesControllerApi.md#salesControllerGetSalesInstructionsFeatures) | **GET** /v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/features | A collection of all features linked to a sales instruction |
| [**salesControllerGetSalesInstructionsFloorPlans**](SalesControllerApi.md#salesControllerGetSalesInstructionsFloorPlans) | **GET** /v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/floorplans | A collection of floor plans linked to an instruction |
| [**salesControllerGetSalesInstructionsPhotos**](SalesControllerApi.md#salesControllerGetSalesInstructionsPhotos) | **GET** /v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/photos | A collection of photos linked to an instruction |
| [**salesControllerGetSalesInstructionsRooms**](SalesControllerApi.md#salesControllerGetSalesInstructionsRooms) | **GET** /v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID}/rooms | A collection of rooms linked to an instruction |
| [**v2Tier1ShortNameSalesSalesfeaturetypesGet**](SalesControllerApi.md#v2Tier1ShortNameSalesSalesfeaturetypesGet) | **GET** /v2/tier1/{shortName}/sales/salesfeaturetypes | A collection of all sales feature types linked to a company |
| [**v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet**](SalesControllerApi.md#v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet) | **GET** /v2/tier1/{shortName}/sales/salesfeaturetypes/{salesFeatureTypeID} | Get a specific sales feature type given its unique Object ID (OID) |
| [**v2Tier1ShortNameSalesSalesinstructionsGet**](SalesControllerApi.md#v2Tier1ShortNameSalesSalesinstructionsGet) | **GET** /v2/tier1/{shortName}/sales/salesinstructions | A collection of all sales instructions linked to a company |
| [**v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet**](SalesControllerApi.md#v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet) | **GET** /v2/tier1/{shortName}/sales/salesinstructions/{salesInstructionID} | Get a specific sales instruction given its unique Object ID (OID) |


<a id="salesControllerGetAdvertisedSales"></a>
# **salesControllerGetAdvertisedSales**
> SalesInstructionModelResults salesControllerGetAdvertisedSales(shortName, branchID, offset, count, onlyDevelopement, onlyInvestements, minimumPrice, maximumPrice, minimumBeds, minimumBathrooms, minimumEnsuites, minimumToilets, minimumReception)

Search all sales properties available given a range of search criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String branchID = "branchID_example"; // String | The unique ID of the Branch
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    Boolean onlyDevelopement = true; // Boolean | Show only development properties?
    Boolean onlyInvestements = true; // Boolean | Show only investment properties?
    Double minimumPrice = 3.4D; // Double | The minimum price to search for
    Double maximumPrice = 3.4D; // Double | The maximum price to search for
    Integer minimumBeds = 56; // Integer | The minimum beds to search for
    Integer minimumBathrooms = 56; // Integer | The minimum bathrooms to search for
    Integer minimumEnsuites = 56; // Integer | The minimum ensuite bathrooms to search for
    Integer minimumToilets = 56; // Integer | The minimum toilets to search for
    Integer minimumReception = 56; // Integer | The minimum reception rooms to search for
    try {
      SalesInstructionModelResults result = apiInstance.salesControllerGetAdvertisedSales(shortName, branchID, offset, count, onlyDevelopement, onlyInvestements, minimumPrice, maximumPrice, minimumBeds, minimumBathrooms, minimumEnsuites, minimumToilets, minimumReception);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#salesControllerGetAdvertisedSales");
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
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |
| **onlyDevelopement** | **Boolean**| Show only development properties? | |
| **onlyInvestements** | **Boolean**| Show only investment properties? | |
| **minimumPrice** | **Double**| The minimum price to search for | [optional] |
| **maximumPrice** | **Double**| The maximum price to search for | [optional] |
| **minimumBeds** | **Integer**| The minimum beds to search for | [optional] |
| **minimumBathrooms** | **Integer**| The minimum bathrooms to search for | [optional] |
| **minimumEnsuites** | **Integer**| The minimum ensuite bathrooms to search for | [optional] |
| **minimumToilets** | **Integer**| The minimum toilets to search for | [optional] |
| **minimumReception** | **Integer**| The minimum reception rooms to search for | [optional] |

### Return type

[**SalesInstructionModelResults**](SalesInstructionModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesControllerGetEER"></a>
# **salesControllerGetEER**
> Object salesControllerGetEER(shortName, salesInstructionID)

Downloads the energy efficiency report (EER) graph for a sales instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
    try {
      Object result = apiInstance.salesControllerGetEER(shortName, salesInstructionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#salesControllerGetEER");
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
| **salesInstructionID** | **String**| The unique ID of the SalesInstruction | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesControllerGetEIR"></a>
# **salesControllerGetEIR**
> Object salesControllerGetEIR(shortName, salesInstructionID)

Downloads the energy efficiency report (EIR) graph for a sales instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
    try {
      Object result = apiInstance.salesControllerGetEIR(shortName, salesInstructionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#salesControllerGetEIR");
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
| **salesInstructionID** | **String**| The unique ID of the SalesInstruction | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesControllerGetSalesInstructionsFeatures"></a>
# **salesControllerGetSalesInstructionsFeatures**
> SalesFeatureModelResults salesControllerGetSalesInstructionsFeatures(shortName, salesInstructionID, offset, count)

A collection of all features linked to a sales instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      SalesFeatureModelResults result = apiInstance.salesControllerGetSalesInstructionsFeatures(shortName, salesInstructionID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#salesControllerGetSalesInstructionsFeatures");
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
| **salesInstructionID** | **String**| The unique ID of the SalesInstruction | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**SalesFeatureModelResults**](SalesFeatureModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesControllerGetSalesInstructionsFloorPlans"></a>
# **salesControllerGetSalesInstructionsFloorPlans**
> PhotoModelResults salesControllerGetSalesInstructionsFloorPlans(shortName, salesInstructionID, offset, count)

A collection of floor plans linked to an instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PhotoModelResults result = apiInstance.salesControllerGetSalesInstructionsFloorPlans(shortName, salesInstructionID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#salesControllerGetSalesInstructionsFloorPlans");
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
| **salesInstructionID** | **String**| The unique ID of the SalesInstruction | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**PhotoModelResults**](PhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesControllerGetSalesInstructionsPhotos"></a>
# **salesControllerGetSalesInstructionsPhotos**
> PhotoModelResults salesControllerGetSalesInstructionsPhotos(shortName, salesInstructionID, offset, count)

A collection of photos linked to an instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PhotoModelResults result = apiInstance.salesControllerGetSalesInstructionsPhotos(shortName, salesInstructionID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#salesControllerGetSalesInstructionsPhotos");
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
| **salesInstructionID** | **String**| The unique ID of the SalesInstruction | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**PhotoModelResults**](PhotoModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesControllerGetSalesInstructionsRooms"></a>
# **salesControllerGetSalesInstructionsRooms**
> PropertyRoomModelResults salesControllerGetSalesInstructionsRooms(shortName, salesInstructionID, offset, count)

A collection of rooms linked to an instruction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PropertyRoomModelResults result = apiInstance.salesControllerGetSalesInstructionsRooms(shortName, salesInstructionID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#salesControllerGetSalesInstructionsRooms");
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
| **salesInstructionID** | **String**| The unique ID of the SalesInstruction | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**PropertyRoomModelResults**](PropertyRoomModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameSalesSalesfeaturetypesGet"></a>
# **v2Tier1ShortNameSalesSalesfeaturetypesGet**
> SalesFeatureTypeModelResults v2Tier1ShortNameSalesSalesfeaturetypesGet(shortName, offset, count)

A collection of all sales feature types linked to a company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      SalesFeatureTypeModelResults result = apiInstance.v2Tier1ShortNameSalesSalesfeaturetypesGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#v2Tier1ShortNameSalesSalesfeaturetypesGet");
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

[**SalesFeatureTypeModelResults**](SalesFeatureTypeModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet"></a>
# **v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet**
> SalesFeatureTypeModel v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet(shortName, salesFeatureTypeID)

Get a specific sales feature type given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesFeatureTypeID = "salesFeatureTypeID_example"; // String | The unique ID of the SalesFeatureType
    try {
      SalesFeatureTypeModel result = apiInstance.v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet(shortName, salesFeatureTypeID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#v2Tier1ShortNameSalesSalesfeaturetypesSalesFeatureTypeIDGet");
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
| **salesFeatureTypeID** | **String**| The unique ID of the SalesFeatureType | |

### Return type

[**SalesFeatureTypeModel**](SalesFeatureTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameSalesSalesinstructionsGet"></a>
# **v2Tier1ShortNameSalesSalesinstructionsGet**
> SalesInstructionModelResults v2Tier1ShortNameSalesSalesinstructionsGet(shortName, offset, count)

A collection of all sales instructions linked to a company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      SalesInstructionModelResults result = apiInstance.v2Tier1ShortNameSalesSalesinstructionsGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#v2Tier1ShortNameSalesSalesinstructionsGet");
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

[**SalesInstructionModelResults**](SalesInstructionModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet"></a>
# **v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet**
> SalesInstructionModel v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet(shortName, salesInstructionID)

Get a specific sales instruction given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    SalesControllerApi apiInstance = new SalesControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String salesInstructionID = "salesInstructionID_example"; // String | The unique ID of the SalesInstruction
    try {
      SalesInstructionModel result = apiInstance.v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet(shortName, salesInstructionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesControllerApi#v2Tier1ShortNameSalesSalesinstructionsSalesInstructionIDGet");
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
| **salesInstructionID** | **String**| The unique ID of the SalesInstruction | |

### Return type

[**SalesInstructionModel**](SalesInstructionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

