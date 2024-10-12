# PropertyControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**propertyControllerGetPropertiesFacilities**](PropertyControllerApi.md#propertyControllerGetPropertiesFacilities) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/facilities | A collection of facilities linked to a block, property or room |
| [**propertyControllerGetPropertiesPhotos**](PropertyControllerApi.md#propertyControllerGetPropertiesPhotos) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/photos | A collection showing all the photos linked to a specific block, property or room |
| [**propertyControllerGetPropertiesRooms**](PropertyControllerApi.md#propertyControllerGetPropertiesRooms) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/rooms | A collection of the rooms that belong to this property or block |
| [**propertyControllerGetPropertiesTenancies**](PropertyControllerApi.md#propertyControllerGetPropertiesTenancies) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID}/tenancies | A collection of all tenancies associated with this block, property or room |
| [**propertyControllerGetPropertyEERDownload**](PropertyControllerApi.md#propertyControllerGetPropertyEERDownload) | **GET** /v2/tier2/{shortName}/property/structures/{propertyStructureID}/reports/eer | Downloads the energy efficiency report (EER) graph for a property |
| [**propertyControllerGetPropertyEIRDownload**](PropertyControllerApi.md#propertyControllerGetPropertyEIRDownload) | **GET** /v2/tier2/{shortName}/property/structures/{propertyStructureID}/reports/eir | Downloads the environmental impact report (EIR) graph for a property |
| [**v2Tier2ShortNamePropertyPropertiesGet**](PropertyControllerApi.md#v2Tier2ShortNamePropertyPropertiesGet) | **GET** /v2/tier2/{shortName}/property/properties | A collection of all properties within a company |
| [**v2Tier2ShortNamePropertyPropertiesPropertyIDGet**](PropertyControllerApi.md#v2Tier2ShortNamePropertyPropertiesPropertyIDGet) | **GET** /v2/tier2/{shortName}/property/properties/{propertyID} | Get a specific property given its unique Object ID (OID) |


<a id="propertyControllerGetPropertiesFacilities"></a>
# **propertyControllerGetPropertiesFacilities**
> PropertyFacilityModelResults propertyControllerGetPropertiesFacilities(shortName, propertyID, offset, count)

A collection of facilities linked to a block, property or room

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String propertyID = "propertyID_example"; // String | The unique ID of the Property
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PropertyFacilityModelResults result = apiInstance.propertyControllerGetPropertiesFacilities(shortName, propertyID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#propertyControllerGetPropertiesFacilities");
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
| **propertyID** | **String**| The unique ID of the Property | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**PropertyFacilityModelResults**](PropertyFacilityModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="propertyControllerGetPropertiesPhotos"></a>
# **propertyControllerGetPropertiesPhotos**
> PhotoModelResults propertyControllerGetPropertiesPhotos(shortName, propertyID, offset, count)

A collection showing all the photos linked to a specific block, property or room

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String propertyID = "propertyID_example"; // String | The unique ID of the Property
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PhotoModelResults result = apiInstance.propertyControllerGetPropertiesPhotos(shortName, propertyID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#propertyControllerGetPropertiesPhotos");
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
| **propertyID** | **String**| The unique ID of the Property | |
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

<a id="propertyControllerGetPropertiesRooms"></a>
# **propertyControllerGetPropertiesRooms**
> PropertyRoomModelResults propertyControllerGetPropertiesRooms(shortName, propertyID, offset, count)

A collection of the rooms that belong to this property or block

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String propertyID = "propertyID_example"; // String | The unique ID of the Property
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PropertyRoomModelResults result = apiInstance.propertyControllerGetPropertiesRooms(shortName, propertyID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#propertyControllerGetPropertiesRooms");
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
| **propertyID** | **String**| The unique ID of the Property | |
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

<a id="propertyControllerGetPropertiesTenancies"></a>
# **propertyControllerGetPropertiesTenancies**
> TenancyModelResults propertyControllerGetPropertiesTenancies(shortName, propertyID, offset, count)

A collection of all tenancies associated with this block, property or room

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String propertyID = "propertyID_example"; // String | The unique ID of the Property
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      TenancyModelResults result = apiInstance.propertyControllerGetPropertiesTenancies(shortName, propertyID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#propertyControllerGetPropertiesTenancies");
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
| **propertyID** | **String**| The unique ID of the Property | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="propertyControllerGetPropertyEERDownload"></a>
# **propertyControllerGetPropertyEERDownload**
> Object propertyControllerGetPropertyEERDownload(shortName, propertyStructureID)

Downloads the energy efficiency report (EER) graph for a property

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String propertyStructureID = "propertyStructureID_example"; // String | The unique ID of the property structure
    try {
      Object result = apiInstance.propertyControllerGetPropertyEERDownload(shortName, propertyStructureID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#propertyControllerGetPropertyEERDownload");
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
| **propertyStructureID** | **String**| The unique ID of the property structure | |

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

<a id="propertyControllerGetPropertyEIRDownload"></a>
# **propertyControllerGetPropertyEIRDownload**
> Object propertyControllerGetPropertyEIRDownload(shortName, propertyStructureID)

Downloads the environmental impact report (EIR) graph for a property

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String propertyStructureID = "propertyStructureID_example"; // String | The unique ID of the property structure
    try {
      Object result = apiInstance.propertyControllerGetPropertyEIRDownload(shortName, propertyStructureID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#propertyControllerGetPropertyEIRDownload");
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
| **propertyStructureID** | **String**| The unique ID of the property structure | |

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

<a id="v2Tier2ShortNamePropertyPropertiesGet"></a>
# **v2Tier2ShortNamePropertyPropertiesGet**
> PropertyModelResults v2Tier2ShortNamePropertyPropertiesGet(shortName, offset, count)

A collection of all properties within a company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      PropertyModelResults result = apiInstance.v2Tier2ShortNamePropertyPropertiesGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#v2Tier2ShortNamePropertyPropertiesGet");
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

[**PropertyModelResults**](PropertyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNamePropertyPropertiesPropertyIDGet"></a>
# **v2Tier2ShortNamePropertyPropertiesPropertyIDGet**
> PropertyModel v2Tier2ShortNamePropertyPropertiesPropertyIDGet(shortName, propertyID)

Get a specific property given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PropertyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    PropertyControllerApi apiInstance = new PropertyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String propertyID = "propertyID_example"; // String | The unique ID of the Property
    try {
      PropertyModel result = apiInstance.v2Tier2ShortNamePropertyPropertiesPropertyIDGet(shortName, propertyID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PropertyControllerApi#v2Tier2ShortNamePropertyPropertiesPropertyIDGet");
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
| **propertyID** | **String**| The unique ID of the Property | |

### Return type

[**PropertyModel**](PropertyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

