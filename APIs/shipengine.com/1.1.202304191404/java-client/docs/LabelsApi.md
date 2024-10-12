# LabelsApi

All URIs are relative to *https://api.shipengine.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLabel**](LabelsApi.md#createLabel) | **POST** /v1/labels | Purchase Label |
| [**createLabelFromRate**](LabelsApi.md#createLabelFromRate) | **POST** /v1/labels/rates/{rate_id} | Purchase Label with Rate ID |
| [**createLabelFromShipment**](LabelsApi.md#createLabelFromShipment) | **POST** /v1/labels/shipment/{shipment_id} | Purchase Label with Shipment ID |
| [**createReturnLabel**](LabelsApi.md#createReturnLabel) | **POST** /v1/labels/{label_id}/return | Create a return label |
| [**getLabelByExternalShipmentId**](LabelsApi.md#getLabelByExternalShipmentId) | **GET** /v1/labels/external_shipment_id/{external_shipment_id} | Get Label By External Shipment ID |
| [**getLabelById**](LabelsApi.md#getLabelById) | **GET** /v1/labels/{label_id} | Get Label By ID |
| [**getTrackingLogFromLabel**](LabelsApi.md#getTrackingLogFromLabel) | **GET** /v1/labels/{label_id}/track | Get Label Tracking Information |
| [**listLabels**](LabelsApi.md#listLabels) | **GET** /v1/labels | List labels |
| [**voidLabel**](LabelsApi.md#voidLabel) | **PUT** /v1/labels/{label_id}/void | Void a Label By ID |


<a id="createLabel"></a>
# **createLabel**
> CreateLabelResponseBody createLabel(createLabelRequestBody)

Purchase Label

Purchase and print a label for shipment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    CreateLabelRequestBody createLabelRequestBody = new CreateLabelRequestBody(); // CreateLabelRequestBody | 
    try {
      CreateLabelResponseBody result = apiInstance.createLabel(createLabelRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#createLabel");
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
| **createLabelRequestBody** | [**CreateLabelRequestBody**](CreateLabelRequestBody.md)|  | |

### Return type

[**CreateLabelResponseBody**](CreateLabelResponseBody.md)

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
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="createLabelFromRate"></a>
# **createLabelFromRate**
> CreateLabelFromRateResponseBody createLabelFromRate(rateId, createLabelFromRateRequestBody)

Purchase Label with Rate ID

When retrieving rates for shipments using the &#x60;/rates&#x60; endpoint, the returned information contains a &#x60;rate_id&#x60; property that can be used to generate a label without having to refill in the shipment information repeatedly. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String rateId = "rateId_example"; // String | Rate ID
    CreateLabelFromRateRequestBody createLabelFromRateRequestBody = new CreateLabelFromRateRequestBody(); // CreateLabelFromRateRequestBody | 
    try {
      CreateLabelFromRateResponseBody result = apiInstance.createLabelFromRate(rateId, createLabelFromRateRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#createLabelFromRate");
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
| **rateId** | **String**| Rate ID | |
| **createLabelFromRateRequestBody** | [**CreateLabelFromRateRequestBody**](CreateLabelFromRateRequestBody.md)|  | |

### Return type

[**CreateLabelFromRateResponseBody**](CreateLabelFromRateResponseBody.md)

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
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="createLabelFromShipment"></a>
# **createLabelFromShipment**
> CreateLabelFromShipmentResponseBody createLabelFromShipment(shipmentId, createLabelFromShipmentRequestBody)

Purchase Label with Shipment ID

Purchase a label using a shipment ID that has already been created with the desired address and package info. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    CreateLabelFromShipmentRequestBody createLabelFromShipmentRequestBody = new CreateLabelFromShipmentRequestBody(); // CreateLabelFromShipmentRequestBody | 
    try {
      CreateLabelFromShipmentResponseBody result = apiInstance.createLabelFromShipment(shipmentId, createLabelFromShipmentRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#createLabelFromShipment");
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
| **createLabelFromShipmentRequestBody** | [**CreateLabelFromShipmentRequestBody**](CreateLabelFromShipmentRequestBody.md)|  | |

### Return type

[**CreateLabelFromShipmentResponseBody**](CreateLabelFromShipmentResponseBody.md)

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
| **404** | The specified resource does not exist. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="createReturnLabel"></a>
# **createReturnLabel**
> CreateReturnLabelResponseBody createReturnLabel(labelId, createReturnLabelRequestBody)

Create a return label

Create a return label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String labelId = "labelId_example"; // String | Label ID
    CreateReturnLabelRequestBody createReturnLabelRequestBody = new CreateReturnLabelRequestBody(); // CreateReturnLabelRequestBody | 
    try {
      CreateReturnLabelResponseBody result = apiInstance.createReturnLabel(labelId, createReturnLabelRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#createReturnLabel");
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
| **labelId** | **String**| Label ID | |
| **createReturnLabelRequestBody** | [**CreateReturnLabelRequestBody**](CreateReturnLabelRequestBody.md)|  | |

### Return type

[**CreateReturnLabelResponseBody**](CreateReturnLabelResponseBody.md)

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

<a id="getLabelByExternalShipmentId"></a>
# **getLabelByExternalShipmentId**
> GetLabelByExternalShipmentIdResponseBody getLabelByExternalShipmentId(externalShipmentId, labelDownloadType)

Get Label By External Shipment ID

Find a label by using the external shipment id that was used during label creation 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String externalShipmentId = "0bcb569d-1727-4ff9-ab49-b2fec0cee5ae"; // String | 
    LabelDownloadType labelDownloadType = LabelDownloadType.fromValue("url"); // LabelDownloadType | 
    try {
      GetLabelByExternalShipmentIdResponseBody result = apiInstance.getLabelByExternalShipmentId(externalShipmentId, labelDownloadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#getLabelByExternalShipmentId");
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
| **labelDownloadType** | [**LabelDownloadType**](.md)|  | [optional] [enum: url, inline] |

### Return type

[**GetLabelByExternalShipmentIdResponseBody**](GetLabelByExternalShipmentIdResponseBody.md)

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

<a id="getLabelById"></a>
# **getLabelById**
> GetLabelByIdResponseBody getLabelById(labelId, labelDownloadType)

Get Label By ID

Retrieve information for individual labels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String labelId = "labelId_example"; // String | Label ID
    LabelDownloadType labelDownloadType = LabelDownloadType.fromValue("url"); // LabelDownloadType | 
    try {
      GetLabelByIdResponseBody result = apiInstance.getLabelById(labelId, labelDownloadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#getLabelById");
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
| **labelId** | **String**| Label ID | |
| **labelDownloadType** | [**LabelDownloadType**](.md)|  | [optional] [enum: url, inline] |

### Return type

[**GetLabelByIdResponseBody**](GetLabelByIdResponseBody.md)

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

<a id="getTrackingLogFromLabel"></a>
# **getTrackingLogFromLabel**
> GetTrackingLogFromLabelResponseBody getTrackingLogFromLabel(labelId)

Get Label Tracking Information

Retrieve the label&#39;s tracking information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String labelId = "labelId_example"; // String | Label ID
    try {
      GetTrackingLogFromLabelResponseBody result = apiInstance.getTrackingLogFromLabel(labelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#getTrackingLogFromLabel");
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
| **labelId** | **String**| Label ID | |

### Return type

[**GetTrackingLogFromLabelResponseBody**](GetTrackingLogFromLabelResponseBody.md)

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

<a id="listLabels"></a>
# **listLabels**
> ListLabelsResponseBody listLabels(labelStatus, serviceCode, carrierId, trackingNumber, batchId, rateId, shipmentId, warehouseId, createdAtStart, createdAtEnd, page, pageSize, sortDir, sortBy)

List labels

This endpoint returns a list of labels that you&#39;ve [created](https://www.shipengine.com/docs/labels/create-a-label/). You can optionally filter the results as well as control their sort order and the number of results returned at a time.  By default, all labels are returned, 25 at a time, starting with the most recently created ones.  You can combine multiple filter options to narrow-down the results.  For example, if you only want to get your UPS labels for your east coast warehouse you could query by both &#x60;warehouse_id&#x60; and &#x60;carrier_id&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    LabelStatus labelStatus = LabelStatus.fromValue("processing"); // LabelStatus | Only return labels that are currently in the specified status
    String serviceCode = "usps_first_class_mail"; // String | Only return labels for a specific [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/)
    String carrierId = "carrierId_example"; // String | Only return labels for a specific [carrier account](https://www.shipengine.com/docs/carriers/setup/)
    String trackingNumber = "9405511899223197428490"; // String | Only return labels with a specific tracking number
    String batchId = "batchId_example"; // String | Only return labels that were created in a specific [batch](https://www.shipengine.com/docs/labels/bulk/)
    String rateId = "rateId_example"; // String | Rate ID
    String shipmentId = "shipmentId_example"; // String | Shipment ID
    String warehouseId = "warehouseId_example"; // String | Only return labels that originate from a specific [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/)
    OffsetDateTime createdAtStart = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Only return labels that were created on or after a specific date/time
    OffsetDateTime createdAtEnd = OffsetDateTime.parse("2019-03-12T19:24:13.657Z"); // OffsetDateTime | Only return labels that were created on or before a specific date/time
    Integer page = 1; // Integer | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
    Integer pageSize = 25; // Integer | The number of results to return per response.
    SortDir sortDir = SortDir.fromValue("asc"); // SortDir | Controls the sort order of the query.
    String sortBy = "modified_at"; // String | Controls which field the query is sorted by.
    try {
      ListLabelsResponseBody result = apiInstance.listLabels(labelStatus, serviceCode, carrierId, trackingNumber, batchId, rateId, shipmentId, warehouseId, createdAtStart, createdAtEnd, page, pageSize, sortDir, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#listLabels");
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
| **labelStatus** | [**LabelStatus**](.md)| Only return labels that are currently in the specified status | [optional] [enum: processing, completed, error, voided] |
| **serviceCode** | **String**| Only return labels for a specific [carrier service](https://www.shipengine.com/docs/shipping/use-a-carrier-service/) | [optional] |
| **carrierId** | **String**| Only return labels for a specific [carrier account](https://www.shipengine.com/docs/carriers/setup/) | [optional] |
| **trackingNumber** | **String**| Only return labels with a specific tracking number | [optional] |
| **batchId** | **String**| Only return labels that were created in a specific [batch](https://www.shipengine.com/docs/labels/bulk/) | [optional] |
| **rateId** | **String**| Rate ID | [optional] |
| **shipmentId** | **String**| Shipment ID | [optional] |
| **warehouseId** | **String**| Only return labels that originate from a specific [warehouse](https://www.shipengine.com/docs/shipping/ship-from-a-warehouse/) | [optional] |
| **createdAtStart** | **OffsetDateTime**| Only return labels that were created on or after a specific date/time | [optional] |
| **createdAtEnd** | **OffsetDateTime**| Only return labels that were created on or before a specific date/time | [optional] |
| **page** | **Integer**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per response. | [optional] [default to 25] |
| **sortDir** | [**SortDir**](.md)| Controls the sort order of the query. | [optional] [default to desc] [enum: asc, desc] |
| **sortBy** | **String**| Controls which field the query is sorted by. | [optional] [default to created_at] [enum: modified_at, created_at] |

### Return type

[**ListLabelsResponseBody**](ListLabelsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response includes a &#x60;labels&#x60; array containing a page of results (as determined by the &#x60;page_size&#x60; query parameter).  It also includes other useful information, such as the total number of labels that match the query criteria, the number of pages of results, and the URLs of the first, last, next, and previous pages of results.  |  -  |
| **400** | The request contained errors. |  -  |
| **500** | An error occurred on ShipEngine&#39;s side.  &gt; This error will automatically be reported to our engineers.  |  -  |

<a id="voidLabel"></a>
# **voidLabel**
> VoidLabelResponseBody voidLabel(labelId)

Void a Label By ID

Void a label by ID to get a refund.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shipengine.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String labelId = "labelId_example"; // String | Label ID
    try {
      VoidLabelResponseBody result = apiInstance.voidLabel(labelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#voidLabel");
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
| **labelId** | **String**| Label ID | |

### Return type

[**VoidLabelResponseBody**](VoidLabelResponseBody.md)

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

