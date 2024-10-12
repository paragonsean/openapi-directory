# ShipmentsApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelShipments**](ShipmentsApi.md#cancelShipments) | **PUT** /v1/shipments/{shipment_id}/cancel | Cancel a Shipment |
| [**createShipments**](ShipmentsApi.md#createShipments) | **POST** /v1/shipments | Create Shipments |
| [**getShipmentByExternalId**](ShipmentsApi.md#getShipmentByExternalId) | **GET** /v1/shipments/external_shipment_id/{external_shipment_id} | Get Shipment By External ID |
| [**getShipmentById**](ShipmentsApi.md#getShipmentById) | **GET** /v1/shipments/{shipment_id} | Get Shipment By ID |
| [**listShipmentRates**](ShipmentsApi.md#listShipmentRates) | **GET** /v1/shipments/{shipment_id}/rates | Get Shipment Rates |
| [**listShipments**](ShipmentsApi.md#listShipments) | **GET** /v1/shipments | List Shipments |
| [**parseShipment**](ShipmentsApi.md#parseShipment) | **PUT** /v1/shipments/recognize | Parse shipping info |
| [**tagShipment**](ShipmentsApi.md#tagShipment) | **POST** /v1/shipments/{shipment_id}/tags/{tag_name} | Add Tag to Shipment |
| [**untagShipment**](ShipmentsApi.md#untagShipment) | **DELETE** /v1/shipments/{shipment_id}/tags/{tag_name} | Remove Tag from Shipment |
| [**updateShipment**](ShipmentsApi.md#updateShipment) | **PUT** /v1/shipments/{shipment_id} | Update Shipment By ID |


<a id="cancelShipments"></a>
# **cancelShipments**
> String cancelShipments(shipmentId)

Cancel a Shipment

Mark a shipment cancelled, if it is no longer needed or being used by your organized. Any label associated with the shipment needs to be voided first An example use case would be if a batch label creation job is going to run at a set time and only queries &#x60;pending&#x60; shipments. Marking a shipment as cancelled would remove it from this process 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    try {
      String result = apiInstance.cancelShipments(shipmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#cancelShipments");
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
| **shipmentId** | **String**| Shipment ID | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="createShipments"></a>
# **createShipments**
> CreateShipmentsResponseBody createShipments(createShipmentsRequestBody)

Create Shipments

Create one or multiple shipments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    CreateShipmentsRequestBody createShipmentsRequestBody = new CreateShipmentsRequestBody(); // CreateShipmentsRequestBody | 
    try {
      CreateShipmentsResponseBody result = apiInstance.createShipments(createShipmentsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#createShipments");
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
| **createShipmentsRequestBody** | [**CreateShipmentsRequestBody**](CreateShipmentsRequestBody.md)|  | |

### Return type

[**CreateShipmentsResponseBody**](CreateShipmentsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested object creation was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getShipmentByExternalId"></a>
# **getShipmentByExternalId**
> GetShipmentByExternalIdResponseBody getShipmentByExternalId(externalShipmentId)

Get Shipment By External ID

Query Shipments created using your own custom ID convention using this endpint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    String externalShipmentId = "0bcb569d-1727-4ff9-ab49-b2fec0cee5ae"; // String | 
    try {
      GetShipmentByExternalIdResponseBody result = apiInstance.getShipmentByExternalId(externalShipmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#getShipmentByExternalId");
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
| **externalShipmentId** | **String**|  | |

### Return type

[**GetShipmentByExternalIdResponseBody**](GetShipmentByExternalIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="getShipmentById"></a>
# **getShipmentById**
> GetShipmentByIdResponseBody getShipmentById(shipmentId)

Get Shipment By ID

Get an individual shipment based on its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    try {
      GetShipmentByIdResponseBody result = apiInstance.getShipmentById(shipmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#getShipmentById");
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
| **shipmentId** | **String**| Shipment ID | |

### Return type

[**GetShipmentByIdResponseBody**](GetShipmentByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listShipmentRates"></a>
# **listShipmentRates**
> ListShipmentRatesResponseBody listShipmentRates(shipmentId, createdAtStart)

Get Shipment Rates

Get Rates for the shipment information associated with the shipment ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    OffsetDateTime createdAtStart = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
    try {
      ListShipmentRatesResponseBody result = apiInstance.listShipmentRates(shipmentId, createdAtStart);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#listShipmentRates");
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
| **shipmentId** | **String**| Shipment ID | |
| **createdAtStart** | **OffsetDateTime**| Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time) | [optional] |

### Return type

[**ListShipmentRatesResponseBody**](ListShipmentRatesResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="listShipments"></a>
# **listShipments**
> ListShipmentsResponseBody listShipments(shipmentStatus, batchId, tag, createdAtStart, createdAtEnd, modifiedAtStart, modifiedAtEnd, page, pageSize, salesOrderId, sortDir, sortBy)

List Shipments

Get list of Shipments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    ShipmentStatus shipmentStatus = ShipmentStatus.fromValue("pending"); // ShipmentStatus | 
    String batchId = "batchId_example"; // String | Batch ID
    String tag = "Letters_to_santa"; // String | Search for shipments based on the custom tag added to the shipment object
    OffsetDateTime createdAtStart = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
    OffsetDateTime createdAtEnd = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)
    OffsetDateTime modifiedAtStart = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Used to create a filter for when a resource was modified (ex. A shipment that was modified after a certain time)
    OffsetDateTime modifiedAtEnd = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Used to create a filter for when a resource was modified (ex. A shipment that was modified before a certain time)
    Integer page = 1; // Integer | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
    Integer pageSize = 25; // Integer | The number of results to return per response.
    String salesOrderId = "salesOrderId_example"; // String | Sales Order ID
    SortDir sortDir = SortDir.fromValue("asc"); // SortDir | Controls the sort order of the query.
    ShipmentsSortBy sortBy = ShipmentsSortBy.fromValue("modified_at"); // ShipmentsSortBy | 
    try {
      ListShipmentsResponseBody result = apiInstance.listShipments(shipmentStatus, batchId, tag, createdAtStart, createdAtEnd, modifiedAtStart, modifiedAtEnd, page, pageSize, salesOrderId, sortDir, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#listShipments");
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
| **shipmentStatus** | [**ShipmentStatus**](.md)|  | [optional] [enum: pending, processing, label_purchased, cancelled] |
| **batchId** | **String**| Batch ID | [optional] |
| **tag** | **String**| Search for shipments based on the custom tag added to the shipment object | [optional] |
| **createdAtStart** | **OffsetDateTime**| Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time) | [optional] |
| **createdAtEnd** | **OffsetDateTime**| Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time) | [optional] |
| **modifiedAtStart** | **OffsetDateTime**| Used to create a filter for when a resource was modified (ex. A shipment that was modified after a certain time) | [optional] |
| **modifiedAtEnd** | **OffsetDateTime**| Used to create a filter for when a resource was modified (ex. A shipment that was modified before a certain time) | [optional] |
| **page** | **Integer**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per response. | [optional] [default to 25] |
| **salesOrderId** | **String**| Sales Order ID | [optional] |
| **sortDir** | [**SortDir**](.md)| Controls the sort order of the query. | [optional] [default to desc] [enum: asc, desc] |
| **sortBy** | [**ShipmentsSortBy**](.md)|  | [optional] [enum: modified_at, created_at] |

### Return type

[**ListShipmentsResponseBody**](ListShipmentsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="parseShipment"></a>
# **parseShipment**
> ParseShipmentResponseBody parseShipment(parseShipmentRequestBody)

Parse shipping info

The shipment-recognition API makes it easy for you to extract shipping data from unstructured text, including people&#39;s names, addresses, package weights and dimensions, insurance and delivery requirements, and more.  Data often enters your system as unstructured text (for example: emails, SMS messages, support tickets, or other documents). ShipEngine&#39;s shipment-recognition API helps you extract meaningful, structured data from this unstructured text. The parsed shipment data is returned in the same structure that&#39;s used for other ShipEngine APIs, so you can easily use the parsed data to create a shipping label.  &gt; **Note:** Shipment recognition is currently supported for the United States, Canada, Australia, New Zealand, the United Kingdom, and Ireland. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    ParseShipmentRequestBody parseShipmentRequestBody = new ParseShipmentRequestBody(); // ParseShipmentRequestBody | The only required field is `text`, which is the text to be parsed. You can optionally also provide a `shipment` containing any already-known values. For example, you probably already know the `ship_from` address, and you may also already know what carrier and service you want to use. 
    try {
      ParseShipmentResponseBody result = apiInstance.parseShipment(parseShipmentRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#parseShipment");
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
| **parseShipmentRequestBody** | [**ParseShipmentRequestBody**](ParseShipmentRequestBody.md)| The only required field is &#x60;text&#x60;, which is the text to be parsed. You can optionally also provide a &#x60;shipment&#x60; containing any already-known values. For example, you probably already know the &#x60;ship_from&#x60; address, and you may also already know what carrier and service you want to use.  | |

### Return type

[**ParseShipmentResponseBody**](ParseShipmentResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the parsed shipment, as well as a confidence score and a list of all the shipping entities that were recognized in the text.  |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="tagShipment"></a>
# **tagShipment**
> TagShipmentResponseBody tagShipment(shipmentId, tagName)

Add Tag to Shipment

Add a tag to the shipment object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    String tagName = "tagName_example"; // String | 
    try {
      TagShipmentResponseBody result = apiInstance.tagShipment(shipmentId, tagName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#tagShipment");
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
| **shipmentId** | **String**| Shipment ID | |
| **tagName** | **String**|  | |

### Return type

[**TagShipmentResponseBody**](TagShipmentResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested object creation was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="untagShipment"></a>
# **untagShipment**
> String untagShipment(shipmentId, tagName)

Remove Tag from Shipment

Remove an existing tag from the Shipment object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    String tagName = "tagName_example"; // String | 
    try {
      String result = apiInstance.untagShipment(shipmentId, tagName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#untagShipment");
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
| **shipmentId** | **String**| Shipment ID | |
| **tagName** | **String**|  | |

### Return type

**String**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The request was successful. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="updateShipment"></a>
# **updateShipment**
> UpdateShipmentResponseBody updateShipment(shipmentId, updateShipmentRequestBody)

Update Shipment By ID

Update a shipment object based on its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ShipmentsApi apiInstance = new ShipmentsApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    UpdateShipmentRequestBody updateShipmentRequestBody = new UpdateShipmentRequestBody(); // UpdateShipmentRequestBody | 
    try {
      UpdateShipmentResponseBody result = apiInstance.updateShipment(shipmentId, updateShipmentRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentsApi#updateShipment");
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
| **shipmentId** | **String**| Shipment ID | |
| **updateShipmentRequestBody** | [**UpdateShipmentRequestBody**](UpdateShipmentRequestBody.md)|  | |

### Return type

[**UpdateShipmentResponseBody**](UpdateShipmentResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was a success. |  -  |
| **400** | The request contained errors. |  -  |
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

