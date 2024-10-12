# StudiesApi

All URIs are relative to *https://api.ideaconsult.net/nanoreg1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEndpointSummary**](StudiesApi.md#getEndpointSummary) | **GET** /enm/{db}/query/study | Search endpoint summary |
| [**getInvestigationResults**](StudiesApi.md#getInvestigationResults) | **GET** /enm/{db}/investigation | Details of multiple studies |
| [**getSubstanceStudy**](StudiesApi.md#getSubstanceStudy) | **GET** /enm/{db}/substance/{uuid}/study | get substance study |
| [**getSubstanceStudySummary**](StudiesApi.md#getSubstanceStudySummary) | **GET** /enm/{db}/substance/{uuid}/studySummary | Get study summary for the substance |


<a id="getEndpointSummary"></a>
# **getEndpointSummary**
> Facet getEndpointSummary(db, top, category)

Search endpoint summary

Returns endpoint summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    StudiesApi apiInstance = new StudiesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String top = "P-CHEM"; // String | Top endpoint category
    String category = "category_example"; // String | Endpoint category (The value in the protocol.category.code field)
    try {
      Facet result = apiInstance.getEndpointSummary(db, top, category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudiesApi#getEndpointSummary");
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
| **top** | **String**| Top endpoint category | [optional] [enum: P-CHEM, ECOTOX, ENV FATE, TOX, EXPOSURE] |
| **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] |

### Return type

[**Facet**](Facet.md)

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

<a id="getInvestigationResults"></a>
# **getInvestigationResults**
> Investigation getInvestigationResults(db, type, search, inchikey, id, page, pagesize)

Details of multiple studies

Multiple studies in tabular form

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    StudiesApi apiInstance = new StudiesApi(defaultClient);
    String db = "calibrate"; // String | Database ID
    String type = "byinvestigation"; // String | query type
    String search = "PC_GRANULOMETRY_SECTION"; // String | Search parameter, UUID of the investigation or a substance
    String inchikey = "YUYCVXFAYWRXLS-UHFFFAOYSA-N"; // String | Search parameter, InChI key(s) of the substance component(s), comma delimited
    String id = "id_example"; // String | Search parameter, chemical structure or substance identifier(s), comma delimited
    Integer page = 0; // Integer | Starting page
    Integer pagesize = 10; // Integer | Page size
    try {
      Investigation result = apiInstance.getInvestigationResults(db, type, search, inchikey, id, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudiesApi#getInvestigationResults");
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
| **type** | **String**| query type | [enum: byinvestigation, byassay, bysubstance, byprovider, bycitation, bystudytype, bystructure_inchikey, bystructure_smiles, bystructure_name, bysubstance_name, bysubstance_type] |
| **search** | **String**| Search parameter, UUID of the investigation or a substance | |
| **inchikey** | **String**| Search parameter, InChI key(s) of the substance component(s), comma delimited | [optional] |
| **id** | **String**| Search parameter, chemical structure or substance identifier(s), comma delimited | [optional] |
| **page** | **Integer**| Starting page | [optional] |
| **pagesize** | **Integer**| Page size | [optional] |

### Return type

[**Investigation**](Investigation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/x-javascript, text/csv, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Entries found |  -  |
| **404** | Entries not found |  -  |

<a id="getSubstanceStudy"></a>
# **getSubstanceStudy**
> SubstanceStudy getSubstanceStudy(db, uuid, top, category, propertyUri, property, investigationUuid, page, pagesize)

get substance study

Returns substance study representation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    StudiesApi apiInstance = new StudiesApi(defaultClient);
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
      SubstanceStudy result = apiInstance.getSubstanceStudy(db, uuid, top, category, propertyUri, property, investigationUuid, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudiesApi#getSubstanceStudy");
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

<a id="getSubstanceStudySummary"></a>
# **getSubstanceStudySummary**
> SubstanceStudySummary getSubstanceStudySummary(db, uuid, top, category, propertyUri, property, result, page, pagesize)

Get study summary for the substance

Study summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StudiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    StudiesApi apiInstance = new StudiesApi(defaultClient);
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
      SubstanceStudySummary result = apiInstance.getSubstanceStudySummary(db, uuid, top, category, propertyUri, property, result, page, pagesize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StudiesApi#getSubstanceStudySummary");
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

