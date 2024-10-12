# AnonymizationApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**anonymizationAnonymizePost**](AnonymizationApi.md#anonymizationAnonymizePost) | **POST** /anonymization/anonymize |  |
| [**anonymizationKeysExportCsvGet**](AnonymizationApi.md#anonymizationKeysExportCsvGet) | **GET** /anonymization/keys/export/csv |  |
| [**anonymizationKeysGet**](AnonymizationApi.md#anonymizationKeysGet) | **GET** /anonymization/keys |  |
| [**anonymizationKeysIdDelete**](AnonymizationApi.md#anonymizationKeysIdDelete) | **DELETE** /anonymization/keys/{id} |  |
| [**anonymizationKeysIdGet**](AnonymizationApi.md#anonymizationKeysIdGet) | **GET** /anonymization/keys/{id} |  |
| [**anonymizationKeysIdKeyvaluesGet**](AnonymizationApi.md#anonymizationKeysIdKeyvaluesGet) | **GET** /anonymization/keys/{id}/keyvalues |  |
| [**anonymizationKeysQueryPost**](AnonymizationApi.md#anonymizationKeysQueryPost) | **POST** /anonymization/keys/query |  |
| [**anonymizationOptionsGet**](AnonymizationApi.md#anonymizationOptionsGet) | **GET** /anonymization/options |  |
| [**imagesIdAnonymizePut**](AnonymizationApi.md#imagesIdAnonymizePut) | **PUT** /images/{id}/anonymize |  |
| [**imagesIdAnonymizedPost**](AnonymizationApi.md#imagesIdAnonymizedPost) | **POST** /images/{id}/anonymized |  |


<a id="anonymizationAnonymizePost"></a>
# **anonymizationAnonymizePost**
> List&lt;Image&gt; anonymizationAnonymizePost(query)



anonymize the images corresponding to the supplied list of image IDs (each paired with a list of DICOM tag translation). This route corresponds to repeated use of the route /images/{id}/anonymize.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    List<ImageTagValues> query = Arrays.asList(); // List<ImageTagValues> | parameters of anonymization key query
    try {
      List<Image> result = apiInstance.anonymizationAnonymizePost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationAnonymizePost");
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
| **query** | [**List&lt;ImageTagValues&gt;**](ImageTagValues.md)| parameters of anonymization key query | |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of newly created anonymous images |  -  |

<a id="anonymizationKeysExportCsvGet"></a>
# **anonymizationKeysExportCsvGet**
> String anonymizationKeysExportCsvGet()



export all anonymization keys as a csv file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    try {
      String result = apiInstance.anonymizationKeysExportCsvGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationKeysExportCsvGet");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | all anonymization keys as a csv file |  -  |

<a id="anonymizationKeysGet"></a>
# **anonymizationKeysGet**
> List&lt;AnonymizationKey&gt; anonymizationKeysGet(startindex, count, orderby, orderascending, filter)



get a list of anonymization keys, each specifying how vital DICOM attributes have been anonymized for a particular image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of anonymization keys
    Long count = 20L; // Long | size of returned slice of anonymization keys
    String orderby = "orderby_example"; // String | property to order results by
    Boolean orderascending = true; // Boolean | order result ascendingly if true, descendingly otherwise
    String filter = "filter_example"; // String | filter the results by matching substrings of properties against this value
    try {
      List<AnonymizationKey> result = apiInstance.anonymizationKeysGet(startindex, count, orderby, orderascending, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationKeysGet");
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
| **startindex** | **Long**| start index of returned slice of anonymization keys | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of anonymization keys | [optional] [default to 20] |
| **orderby** | **String**| property to order results by | [optional] |
| **orderascending** | **Boolean**| order result ascendingly if true, descendingly otherwise | [optional] [default to true] |
| **filter** | **String**| filter the results by matching substrings of properties against this value | [optional] |

### Return type

[**List&lt;AnonymizationKey&gt;**](AnonymizationKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | anonymization keys, one per DICOM image |  -  |

<a id="anonymizationKeysIdDelete"></a>
# **anonymizationKeysIdDelete**
> anonymizationKeysIdDelete(id)



delete an anonymization key that is no longer of interest

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    Long id = 56L; // Long | ID of anonymization key
    try {
      apiInstance.anonymizationKeysIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationKeysIdDelete");
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
| **id** | **Long**| ID of anonymization key | |

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
| **204** | anonymization key deleted |  -  |

<a id="anonymizationKeysIdGet"></a>
# **anonymizationKeysIdGet**
> AnonymizationKey anonymizationKeysIdGet(id)



get the anonymization key with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    Long id = 56L; // Long | ID of anonymization key
    try {
      AnonymizationKey result = apiInstance.anonymizationKeysIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationKeysIdGet");
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
| **id** | **Long**| ID of anonymization key | |

### Return type

[**AnonymizationKey**](AnonymizationKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | anonymization key for the supplied ID |  -  |
| **404** | if no anonymization key could be found for the supplied ID |  -  |

<a id="anonymizationKeysIdKeyvaluesGet"></a>
# **anonymizationKeysIdKeyvaluesGet**
> List&lt;AnonymizationKeyValue&gt; anonymizationKeysIdKeyvaluesGet(id)



get pointers to the images corresponding to the anonymization key with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    Long id = 56L; // Long | ID of anonymization key
    try {
      List<AnonymizationKeyValue> result = apiInstance.anonymizationKeysIdKeyvaluesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationKeysIdKeyvaluesGet");
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
| **id** | **Long**| ID of anonymization key | |

### Return type

[**List&lt;AnonymizationKeyValue&gt;**](AnonymizationKeyValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an array of anonymization key-value pairs corresponding to the anonymization key for the supplied ID |  -  |
| **404** | if no anonymization key could be found for the supplied ID |  -  |

<a id="anonymizationKeysQueryPost"></a>
# **anonymizationKeysQueryPost**
> List&lt;AnonymizationKey&gt; anonymizationKeysQueryPost(query)



submit a query for anonymization keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    AnonymizationKeyQuery query = new AnonymizationKeyQuery(); // AnonymizationKeyQuery | parameters of anonymization key query
    try {
      List<AnonymizationKey> result = apiInstance.anonymizationKeysQueryPost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationKeysQueryPost");
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
| **query** | [**AnonymizationKeyQuery**](AnonymizationKeyQuery.md)| parameters of anonymization key query | |

### Return type

[**List&lt;AnonymizationKey&gt;**](AnonymizationKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | anonymization keys |  -  |

<a id="anonymizationOptionsGet"></a>
# **anonymizationOptionsGet**
> List&lt;ConfidentialityOption&gt; anonymizationOptionsGet()



list all supported anonymization options defining an anonymization profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    try {
      List<ConfidentialityOption> result = apiInstance.anonymizationOptionsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#anonymizationOptionsGet");
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

[**List&lt;ConfidentialityOption&gt;**](ConfidentialityOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | supported anonymization options |  -  |

<a id="imagesIdAnonymizePut"></a>
# **imagesIdAnonymizePut**
> Image imagesIdAnonymizePut(id, tagValues)



delete the selected image and replace it with an anonymized version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    Long id = 56L; // Long | ID of image to anonymize
    AnonymizationData tagValues = new AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
    try {
      Image result = apiInstance.imagesIdAnonymizePut(id, tagValues);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#imagesIdAnonymizePut");
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
| **id** | **Long**| ID of image to anonymize | |
| **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created anonymous image |  -  |
| **404** | image or corresponding dataset not found |  -  |

<a id="imagesIdAnonymizedPost"></a>
# **imagesIdAnonymizedPost**
> imagesIdAnonymizedPost(id, tagValues)



get an anonymized version of the image with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnonymizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    AnonymizationApi apiInstance = new AnonymizationApi(defaultClient);
    Long id = 56L; // Long | ID of image for which to get anonymized dataset
    AnonymizationData tagValues = new AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
    try {
      apiInstance.imagesIdAnonymizedPost(id, tagValues);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnonymizationApi#imagesIdAnonymizedPost");
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
| **id** | **Long**| ID of image for which to get anonymized dataset | |
| **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | |

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
| **200** | binary data of anonymized dataset |  -  |
| **404** | if no image was found for the supplied image ID |  -  |

