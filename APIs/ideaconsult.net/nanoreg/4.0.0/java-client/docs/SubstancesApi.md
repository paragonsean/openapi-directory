# SubstancesApi

All URIs are relative to *https://api.ideaconsult.net/nanoreg1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSubstanceByUUID**](SubstancesApi.md#getSubstanceByUUID) | **GET** /enm/{db}/substance/{uuid} | Get a substance |
| [**getSubstanceComposition_0**](SubstancesApi.md#getSubstanceComposition_0) | **GET** /enm/{db}/substance/{uuid}/composition | Substance composition |
| [**getSubstanceStructures_0**](SubstancesApi.md#getSubstanceStructures_0) | **GET** /enm/{db}/substance/{uuid}/structures | Get substance composition as a dataset |
| [**getSubstanceStudySummary_0**](SubstancesApi.md#getSubstanceStudySummary_0) | **GET** /enm/{db}/substance/{uuid}/studySummary | Get study summary for the substance |
| [**getSubstanceStudy_0**](SubstancesApi.md#getSubstanceStudy_0) | **GET** /enm/{db}/substance/{uuid}/study | get substance study |
| [**getSubstances**](SubstancesApi.md#getSubstances) | **GET** /enm/{db}/substance | List substances |


<a id="getSubstanceByUUID"></a>
# **getSubstanceByUUID**
> Substance getSubstanceByUUID(db, uuid, propertyUris, page, pagesize)

Get a substance

Returns substance representation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SubstancesApi apiInstance = new SubstancesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String uuid = "uuid_example"; // String | Substance UUID
    String propertyUris = "propertyUris_example"; // String | Property URIs
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Substance result = apiInstance.getSubstanceByUUID(db, uuid, propertyUris, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubstancesApi#getSubstanceByUUID");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **uuid** | **String**| Substance UUID | |
| **propertyUris** | **String**| Property URIs | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Substance**](Substance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Substances found |  -  |
| **404** | Substances not found |  -  |

<a id="getSubstanceComposition_0"></a>
# **getSubstanceComposition_0**
> SubstanceComposition getSubstanceComposition_0(db, uuid, all, page, pagesize)

Substance composition

Returns substance composition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SubstancesApi apiInstance = new SubstancesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String uuid = "uuid_example"; // String | Substance UUID
    Boolean all = true; // Boolean | true (Show all compositions) false (do not show hidden compositions)
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      SubstanceComposition result = apiInstance.getSubstanceComposition_0(db, uuid, all, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubstancesApi#getSubstanceComposition_0");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **uuid** | **String**| Substance UUID | |
| **all** | **Boolean**| true (Show all compositions) false (do not show hidden compositions) | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**SubstanceComposition**](SubstanceComposition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. compositions found |  -  |
| **404** | compositions not found |  -  |

<a id="getSubstanceStructures_0"></a>
# **getSubstanceStructures_0**
> Dataset getSubstanceStructures_0(db, uuid, page, pagesize)

Get substance composition as a dataset

Returns substance composition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SubstancesApi apiInstance = new SubstancesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String uuid = "uuid_example"; // String | Substance UUID
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Dataset result = apiInstance.getSubstanceStructures_0(db, uuid, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubstancesApi#getSubstanceStructures_0");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **uuid** | **String**| Substance UUID | |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. compositions found |  -  |
| **404** | compositions not found |  -  |

<a id="getSubstanceStudySummary_0"></a>
# **getSubstanceStudySummary_0**
> SubstanceStudySummary getSubstanceStudySummary_0(db, uuid, top, category, propertyUri, property, result, page, pagesize)

Get study summary for the substance

Study summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SubstancesApi apiInstance = new SubstancesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String uuid = "uuid_example"; // String | Substance UUID
    String top = "P-CHEM"; // String | Top endpoint category
    String category = "category_example"; // String | Endpoint category (The value in the protocol.category.code field)
    String propertyUri = "propertyUri_example"; // String | Property URI https://data.enanomapper.net/property/{UUID} , see Property service
    String property = "property_example"; // String | Property UUID, see Property service
    Boolean result = true; // Boolean | If true will group by topcategory,endpointcategory,interpretation result
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      SubstanceStudySummary result = apiInstance.getSubstanceStudySummary_0(db, uuid, top, category, propertyUri, property, result, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubstancesApi#getSubstanceStudySummary_0");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **uuid** | **String**| Substance UUID | |
| **top** | **String**| Top endpoint category | [optional] [enum: P-CHEM, ECOTOX, ENV FATE, TOX, EXPOSURE] |
| **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] |
| **propertyUri** | **String**| Property URI https://data.enanomapper.net/property/{UUID} , see Property service | [optional] |
| **property** | **String**| Property UUID, see Property service | [optional] |
| **result** | **Boolean**| If true will group by topcategory,endpointcategory,interpretation result | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**SubstanceStudySummary**](SubstanceStudySummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **404** | Entries not found |  -  |

<a id="getSubstanceStudy_0"></a>
# **getSubstanceStudy_0**
> SubstanceStudy getSubstanceStudy_0(db, uuid, top, category, propertyUri, property, investigationUuid, page, pagesize)

get substance study

Returns substance study representation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SubstancesApi apiInstance = new SubstancesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String uuid = "uuid_example"; // String | Substance UUID
    String top = "P-CHEM"; // String | Top endpoint category
    String category = "category_example"; // String | Endpoint category (The value in the protocol.category.code field)
    String propertyUri = "propertyUri_example"; // String | Property URI https://data.enanomapper.net/property/{UUID} , see Property service
    String property = "property_example"; // String | Property UUID
    String investigationUuid = "investigationUuid_example"; // String | Investigation UUID, a code to link different studies
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      SubstanceStudy result = apiInstance.getSubstanceStudy_0(db, uuid, top, category, propertyUri, property, investigationUuid, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubstancesApi#getSubstanceStudy_0");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **uuid** | **String**| Substance UUID | |
| **top** | **String**| Top endpoint category | [optional] [enum: P-CHEM, ECOTOX, ENV FATE, TOX, EXPOSURE] |
| **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] |
| **propertyUri** | **String**| Property URI https://data.enanomapper.net/property/{UUID} , see Property service | [optional] |
| **property** | **String**| Property UUID | [optional] |
| **investigationUuid** | **String**| Investigation UUID, a code to link different studies | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**SubstanceStudy**](SubstanceStudy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Substances found |  -  |
| **404** | Substances not found |  -  |

<a id="getSubstances"></a>
# **getSubstances**
> Substance getSubstances(db, search, type, compoundUri, bundleUri, addDummySubstance, studysummary, page, pagesize)

List substances

Returns a list of substances, according to the search criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SubstancesApi apiInstance = new SubstancesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String search = "search_example"; // String | Search parameter
    String type = "substancetype"; // String | 
    String compoundUri = "compoundUri_example"; // String | If type=related finds all substances containing this compound; if typ =reference - finds all substances with this compound as reference structure
    String bundleUri = "bundleUri_example"; // String | Retrieves if selected in this bundle
    Boolean addDummySubstance = true; // Boolean | Adds a compound record as substance in JSON; only if type=related
    Boolean studysummary = true; // Boolean | If true retrieves study summary for each substance
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Substance result = apiInstance.getSubstances(db, search, type, compoundUri, bundleUri, addDummySubstance, studysummary, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubstancesApi#getSubstances");
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
| **db** | **String**| Database ID | [default to nanoreg1] [enum: calibrate, enanomapper, enpra, marina, nanogenotox, nanoinformatix, nanoreg1, nanoreg2, nanotest] |
| **search** | **String**| Search parameter | [optional] |
| **type** | **String**|  | [optional] [enum: substancetype, name, like, regexp, uuif, CompTox, DOI, reliability, purposeFlag, studyResultType, isRobustStudy, citation, citationowner, topcategory, endpointcategory, params, owner_name, owner_uuid, related, reference, facet] |
| **compoundUri** | **String**| If type&#x3D;related finds all substances containing this compound; if typ &#x3D;reference - finds all substances with this compound as reference structure | [optional] |
| **bundleUri** | **String**| Retrieves if selected in this bundle | [optional] |
| **addDummySubstance** | **Boolean**| Adds a compound record as substance in JSON; only if type&#x3D;related | [optional] |
| **studysummary** | **Boolean**| If true retrieves study summary for each substance | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Substance**](Substance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Substances found |  -  |
| **404** | Substances not found |  -  |

