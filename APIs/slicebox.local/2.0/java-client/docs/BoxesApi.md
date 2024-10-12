# BoxesApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**boxesConnectPost**](BoxesApi.md#boxesConnectPost) | **POST** /boxes/connect |  |
| [**boxesCreateconnectionPost**](BoxesApi.md#boxesCreateconnectionPost) | **POST** /boxes/createconnection |  |
| [**boxesGet**](BoxesApi.md#boxesGet) | **GET** /boxes |  |
| [**boxesIdDelete**](BoxesApi.md#boxesIdDelete) | **DELETE** /boxes/{id} |  |
| [**boxesIdSendPost**](BoxesApi.md#boxesIdSendPost) | **POST** /boxes/{id}/send |  |
| [**boxesIncomingGet**](BoxesApi.md#boxesIncomingGet) | **GET** /boxes/incoming |  |
| [**boxesIncomingIdDelete**](BoxesApi.md#boxesIncomingIdDelete) | **DELETE** /boxes/incoming/{id} |  |
| [**boxesIncomingIdImagesGet**](BoxesApi.md#boxesIncomingIdImagesGet) | **GET** /boxes/incoming/{id}/images |  |
| [**boxesOutgoingGet**](BoxesApi.md#boxesOutgoingGet) | **GET** /boxes/outgoing |  |
| [**boxesOutgoingIdDelete**](BoxesApi.md#boxesOutgoingIdDelete) | **DELETE** /boxes/outgoing/{id} |  |
| [**boxesOutgoingIdImagesGet**](BoxesApi.md#boxesOutgoingIdImagesGet) | **GET** /boxes/outgoing/{id}/images |  |


<a id="boxesConnectPost"></a>
# **boxesConnectPost**
> Box boxesConnectPost(remoteBox)



connect to another box using a received URL. Used to connect to a public box.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    RemoteBox remoteBox = new RemoteBox(); // RemoteBox | remote box to connect with
    try {
      Box result = apiInstance.boxesConnectPost(remoteBox);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesConnectPost");
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
| **remoteBox** | [**RemoteBox**](RemoteBox.md)| remote box to connect with | |

### Return type

[**Box**](Box.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | connected box |  -  |

<a id="boxesCreateconnectionPost"></a>
# **boxesCreateconnectionPost**
> Box boxesCreateconnectionPost(remoteBoxConnectionData)



create a new box connection where the supplied entity holds the remote box name. Used by publicly available boxes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    RemoteBoxConnectionData remoteBoxConnectionData = new RemoteBoxConnectionData(); // RemoteBoxConnectionData | name of box to connect (and send URL) to
    try {
      Box result = apiInstance.boxesCreateconnectionPost(remoteBoxConnectionData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesCreateconnectionPost");
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
| **remoteBoxConnectionData** | [**RemoteBoxConnectionData**](RemoteBoxConnectionData.md)| name of box to connect (and send URL) to | |

### Return type

[**Box**](Box.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | remote box of the connection |  -  |

<a id="boxesGet"></a>
# **boxesGet**
> List&lt;Box&gt; boxesGet(startindex, count)



get a list of box connections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of boxes
    Long count = 20L; // Long | size of returned slice of boxes
    try {
      List<Box> result = apiInstance.boxesGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesGet");
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
| **startindex** | **Long**| start index of returned slice of boxes | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of boxes | [optional] [default to 20] |

### Return type

[**List&lt;Box&gt;**](Box.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | box connections |  -  |

<a id="boxesIdDelete"></a>
# **boxesIdDelete**
> boxesIdDelete(id)



Delete the remote box with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long id = 56L; // Long | ID of box to remove
    try {
      apiInstance.boxesIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesIdDelete");
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
| **id** | **Long**| ID of box to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | box deleted |  -  |

<a id="boxesIdSendPost"></a>
# **boxesIdSendPost**
> boxesIdSendPost(id, sequenceOfImageTagValues)



send images corresponding to the supplied image ids to the remote box with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long id = 56L; // Long | ID of box to send images to
    BulkAnonymizationData sequenceOfImageTagValues = new BulkAnonymizationData(); // BulkAnonymizationData | specification of which images to send and list of DICOM attribute values to use in anonymized datasets
    try {
      apiInstance.boxesIdSendPost(id, sequenceOfImageTagValues);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesIdSendPost");
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
| **id** | **Long**| ID of box to send images to | |
| **sequenceOfImageTagValues** | [**BulkAnonymizationData**](BulkAnonymizationData.md)| specification of which images to send and list of DICOM attribute values to use in anonymized datasets | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | images sent |  -  |
| **404** | box not found (invalid ID) |  -  |

<a id="boxesIncomingGet"></a>
# **boxesIncomingGet**
> List&lt;IncomingTransaction&gt; boxesIncomingGet(startindex, count)



get incoming transactions (finished, currently receiving, waiting or failed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of transactions
    Long count = 20L; // Long | size of returned slice of transactions
    try {
      List<IncomingTransaction> result = apiInstance.boxesIncomingGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesIncomingGet");
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
| **startindex** | **Long**| start index of returned slice of transactions | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of transactions | [optional] [default to 20] |

### Return type

[**List&lt;IncomingTransaction&gt;**](IncomingTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | incoming transactions, sorted from most to least recently updated |  -  |

<a id="boxesIncomingIdDelete"></a>
# **boxesIncomingIdDelete**
> boxesIncomingIdDelete(id)



delete an incoming transaction. If a currently active transaction is deleted, a new transaction with the remainder of the images is created when receiving the next incoming image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long id = 56L; // Long | ID of incoming transaction
    try {
      apiInstance.boxesIncomingIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesIncomingIdDelete");
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
| **id** | **Long**| ID of incoming transaction | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | incoming transaction deleted |  -  |

<a id="boxesIncomingIdImagesGet"></a>
# **boxesIncomingIdImagesGet**
> List&lt;Image&gt; boxesIncomingIdImagesGet(id)



get the received images corresponding to the incoming transaction with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long id = 56L; // Long | ID of incoming transaction
    try {
      List<Image> result = apiInstance.boxesIncomingIdImagesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesIncomingIdImagesGet");
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
| **id** | **Long**| ID of incoming transaction | |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | images received corresponding to the specified incoming transaction |  -  |
| **404** | incoming transaction not found (invalid ID) |  -  |

<a id="boxesOutgoingGet"></a>
# **boxesOutgoingGet**
> List&lt;OutgoingTransaction&gt; boxesOutgoingGet(startindex, count)



get outgoing transactions (finished, currently sending, waiting or failed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of transactions
    Long count = 20L; // Long | size of returned slice of transactions
    try {
      List<OutgoingTransaction> result = apiInstance.boxesOutgoingGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesOutgoingGet");
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
| **startindex** | **Long**| start index of returned slice of transactions | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of transactions | [optional] [default to 20] |

### Return type

[**List&lt;OutgoingTransaction&gt;**](OutgoingTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | outgoing transactions, finished, sending, waiting or failed |  -  |

<a id="boxesOutgoingIdDelete"></a>
# **boxesOutgoingIdDelete**
> boxesOutgoingIdDelete(id)



delete an outgoing transaction. This will stop ongoing transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long id = 56L; // Long | ID of outgoing transaction
    try {
      apiInstance.boxesOutgoingIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesOutgoingIdDelete");
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
| **id** | **Long**| ID of outgoing transaction | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | outgoing transaction deleted |  -  |

<a id="boxesOutgoingIdImagesGet"></a>
# **boxesOutgoingIdImagesGet**
> List&lt;Image&gt; boxesOutgoingIdImagesGet(id)



get the sent images corresponding to the outgoing transaction with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BoxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    BoxesApi apiInstance = new BoxesApi(defaultClient);
    Long id = 56L; // Long | ID of outgoing transaction
    try {
      List<Image> result = apiInstance.boxesOutgoingIdImagesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BoxesApi#boxesOutgoingIdImagesGet");
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
| **id** | **Long**| ID of outgoing transaction | |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | images sent corresponding to the specified outgoing transaction |  -  |
| **404** | outgoing transaction not found (invalid ID) |  -  |

