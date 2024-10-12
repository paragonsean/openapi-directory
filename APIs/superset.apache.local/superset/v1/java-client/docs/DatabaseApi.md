# DatabaseApi

All URIs are relative to *http://superset.apache.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseAvailableGet**](DatabaseApi.md#databaseAvailableGet) | **GET** /database/available/ |  |
| [**databaseExportGet**](DatabaseApi.md#databaseExportGet) | **GET** /database/export/ |  |
| [**databaseGet**](DatabaseApi.md#databaseGet) | **GET** /database/ |  |
| [**databaseImportPost**](DatabaseApi.md#databaseImportPost) | **POST** /database/import/ |  |
| [**databaseInfoGet**](DatabaseApi.md#databaseInfoGet) | **GET** /database/_info |  |
| [**databasePkDelete**](DatabaseApi.md#databasePkDelete) | **DELETE** /database/{pk} |  |
| [**databasePkFunctionNamesGet**](DatabaseApi.md#databasePkFunctionNamesGet) | **GET** /database/{pk}/function_names/ |  |
| [**databasePkGet**](DatabaseApi.md#databasePkGet) | **GET** /database/{pk} |  |
| [**databasePkPut**](DatabaseApi.md#databasePkPut) | **PUT** /database/{pk} |  |
| [**databasePkRelatedObjectsGet**](DatabaseApi.md#databasePkRelatedObjectsGet) | **GET** /database/{pk}/related_objects/ |  |
| [**databasePkSchemasGet**](DatabaseApi.md#databasePkSchemasGet) | **GET** /database/{pk}/schemas/ |  |
| [**databasePkSelectStarTableNameGet**](DatabaseApi.md#databasePkSelectStarTableNameGet) | **GET** /database/{pk}/select_star/{table_name}/ |  |
| [**databasePkSelectStarTableNameSchemaNameGet**](DatabaseApi.md#databasePkSelectStarTableNameSchemaNameGet) | **GET** /database/{pk}/select_star/{table_name}/{schema_name}/ |  |
| [**databasePkTableTableNameSchemaNameGet**](DatabaseApi.md#databasePkTableTableNameSchemaNameGet) | **GET** /database/{pk}/table/{table_name}/{schema_name}/ |  |
| [**databasePost**](DatabaseApi.md#databasePost) | **POST** /database/ |  |
| [**databaseTestConnectionPost**](DatabaseApi.md#databaseTestConnectionPost) | **POST** /database/test_connection |  |
| [**databaseValidateParametersPost**](DatabaseApi.md#databaseValidateParametersPost) | **POST** /database/validate_parameters |  |


<a id="databaseAvailableGet"></a>
# **databaseAvailableGet**
> List&lt;DatabaseAvailableGet200ResponseInner&gt; databaseAvailableGet()



Get names of databases currently available

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    try {
      List<DatabaseAvailableGet200ResponseInner> result = apiInstance.databaseAvailableGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseAvailableGet");
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

[**List&lt;DatabaseAvailableGet200ResponseInner&gt;**](DatabaseAvailableGet200ResponseInner.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database names |  -  |
| **400** | Bad request |  -  |
| **500** | Fatal error |  -  |

<a id="databaseExportGet"></a>
# **databaseExportGet**
> File databaseExportGet(q)



Download database(s) and associated dataset(s) as a zip file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    List<Integer> q = Arrays.asList(); // List<Integer> | 
    try {
      File result = apiInstance.databaseExportGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseExportGet");
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
| **q** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A zip file with database(s) and dataset(s) as YAML |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="databaseGet"></a>
# **databaseGet**
> DatabaseGet200Response databaseGet(q)



Get a list of models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    GetListSchema q = new GetListSchema(); // GetListSchema | 
    try {
      DatabaseGet200Response result = apiInstance.databaseGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseGet");
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
| **q** | [**GetListSchema**](.md)|  | [optional] |

### Return type

[**DatabaseGet200Response**](DatabaseGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Items from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databaseImportPost"></a>
# **databaseImportPost**
> AnnotationLayerGet400Response databaseImportPost(formData, overwrite, passwords)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    File formData = new File("/path/to/file"); // File | upload file (ZIP)
    Boolean overwrite = true; // Boolean | overwrite existing databases?
    String passwords = "passwords_example"; // String | JSON map of passwords for each file
    try {
      AnnotationLayerGet400Response result = apiInstance.databaseImportPost(formData, overwrite, passwords);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseImportPost");
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
| **formData** | **File**| upload file (ZIP) | [optional] |
| **overwrite** | **Boolean**| overwrite existing databases? | [optional] |
| **passwords** | **String**| JSON map of passwords for each file | [optional] |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database import result |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databaseInfoGet"></a>
# **databaseInfoGet**
> AnnotationLayerInfoGet200Response databaseInfoGet(q)



Get metadata information about this API resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    GetInfoSchema q = new GetInfoSchema(); // GetInfoSchema | 
    try {
      AnnotationLayerInfoGet200Response result = apiInstance.databaseInfoGet(q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseInfoGet");
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
| **q** | [**GetInfoSchema**](.md)|  | [optional] |

### Return type

[**AnnotationLayerInfoGet200Response**](AnnotationLayerInfoGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkDelete"></a>
# **databasePkDelete**
> AnnotationLayerGet400Response databasePkDelete(pk)



Deletes a Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | 
    try {
      AnnotationLayerGet400Response result = apiInstance.databasePkDelete(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkDelete");
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
| **pk** | **Integer**|  | |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database deleted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkFunctionNamesGet"></a>
# **databasePkFunctionNamesGet**
> DatabaseFunctionNamesResponse databasePkFunctionNamesGet(pk)



Get function names supported by a database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | 
    try {
      DatabaseFunctionNamesResponse result = apiInstance.databasePkFunctionNamesGet(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkFunctionNamesGet");
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
| **pk** | **Integer**|  | |

### Return type

[**DatabaseFunctionNamesResponse**](DatabaseFunctionNamesResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query result |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkGet"></a>
# **databasePkGet**
> DatabasePkGet200Response databasePkGet(pk, q)



Get an item model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | 
    GetItemSchema q = new GetItemSchema(); // GetItemSchema | 
    try {
      DatabasePkGet200Response result = apiInstance.databasePkGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkGet");
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
| **pk** | **Integer**|  | |
| **q** | [**GetItemSchema**](.md)|  | [optional] |

### Return type

[**DatabasePkGet200Response**](DatabasePkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Item from Model |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkPut"></a>
# **databasePkPut**
> DatabasePkPut200Response databasePkPut(pk, databaseRestApiPut)



Changes a Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | 
    DatabaseRestApiPut databaseRestApiPut = new DatabaseRestApiPut(); // DatabaseRestApiPut | Database schema
    try {
      DatabasePkPut200Response result = apiInstance.databasePkPut(pk, databaseRestApiPut);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkPut");
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
| **pk** | **Integer**|  | |
| **databaseRestApiPut** | [**DatabaseRestApiPut**](DatabaseRestApiPut.md)| Database schema | |

### Return type

[**DatabasePkPut200Response**](DatabasePkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database changed |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkRelatedObjectsGet"></a>
# **databasePkRelatedObjectsGet**
> DatabaseRelatedObjectsResponse databasePkRelatedObjectsGet(pk)



Get charts and dashboards count associated to a database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | 
    try {
      DatabaseRelatedObjectsResponse result = apiInstance.databasePkRelatedObjectsGet(pk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkRelatedObjectsGet");
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
| **pk** | **Integer**|  | |

### Return type

[**DatabaseRelatedObjectsResponse**](DatabaseRelatedObjectsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query result |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkSchemasGet"></a>
# **databasePkSchemasGet**
> SchemasResponseSchema databasePkSchemasGet(pk, q)



Get all schemas from a database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | The database id
    DatabaseSchemasQuerySchema q = new DatabaseSchemasQuerySchema(); // DatabaseSchemasQuerySchema | 
    try {
      SchemasResponseSchema result = apiInstance.databasePkSchemasGet(pk, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkSchemasGet");
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
| **pk** | **Integer**| The database id | |
| **q** | [**DatabaseSchemasQuerySchema**](.md)|  | [optional] |

### Return type

[**SchemasResponseSchema**](SchemasResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of all schemas from the database |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkSelectStarTableNameGet"></a>
# **databasePkSelectStarTableNameGet**
> SelectStarResponseSchema databasePkSelectStarTableNameGet(pk, tableName, schemaName)



Get database select star for table

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | The database id
    String tableName = "tableName_example"; // String | Table name
    String schemaName = "schemaName_example"; // String | Table schema
    try {
      SelectStarResponseSchema result = apiInstance.databasePkSelectStarTableNameGet(pk, tableName, schemaName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkSelectStarTableNameGet");
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
| **pk** | **Integer**| The database id | |
| **tableName** | **String**| Table name | |
| **schemaName** | **String**| Table schema | |

### Return type

[**SelectStarResponseSchema**](SelectStarResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SQL statement for a select star for table |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkSelectStarTableNameSchemaNameGet"></a>
# **databasePkSelectStarTableNameSchemaNameGet**
> SelectStarResponseSchema databasePkSelectStarTableNameSchemaNameGet(pk, tableName, schemaName)



Get database select star for table

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | The database id
    String tableName = "tableName_example"; // String | Table name
    String schemaName = "schemaName_example"; // String | Table schema
    try {
      SelectStarResponseSchema result = apiInstance.databasePkSelectStarTableNameSchemaNameGet(pk, tableName, schemaName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkSelectStarTableNameSchemaNameGet");
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
| **pk** | **Integer**| The database id | |
| **tableName** | **String**| Table name | |
| **schemaName** | **String**| Table schema | |

### Return type

[**SelectStarResponseSchema**](SelectStarResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SQL statement for a select star for table |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databasePkTableTableNameSchemaNameGet"></a>
# **databasePkTableTableNameSchemaNameGet**
> TableMetadataResponseSchema databasePkTableTableNameSchemaNameGet(pk, tableName, schemaName)



Get database table metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    Integer pk = 56; // Integer | The database id
    String tableName = "tableName_example"; // String | Table name
    String schemaName = "schemaName_example"; // String | Table schema
    try {
      TableMetadataResponseSchema result = apiInstance.databasePkTableTableNameSchemaNameGet(pk, tableName, schemaName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePkTableTableNameSchemaNameGet");
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
| **pk** | **Integer**| The database id | |
| **tableName** | **String**| Table name | |
| **schemaName** | **String**| Table schema | |

### Return type

[**TableMetadataResponseSchema**](TableMetadataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Table metadata information |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databasePost"></a>
# **databasePost**
> DatabasePost201Response databasePost(databaseRestApiPost)



Create a new Database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    DatabaseRestApiPost databaseRestApiPost = new DatabaseRestApiPost(); // DatabaseRestApiPost | Database schema
    try {
      DatabasePost201Response result = apiInstance.databasePost(databaseRestApiPost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databasePost");
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
| **databaseRestApiPost** | [**DatabaseRestApiPost**](DatabaseRestApiPost.md)| Database schema | |

### Return type

[**DatabasePost201Response**](DatabasePost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Database added |  -  |
| **302** | Redirects to the current digest |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Fatal error |  -  |

<a id="databaseTestConnectionPost"></a>
# **databaseTestConnectionPost**
> AnnotationLayerGet400Response databaseTestConnectionPost(databaseTestConnectionSchema)



Tests a database connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    DatabaseTestConnectionSchema databaseTestConnectionSchema = new DatabaseTestConnectionSchema(); // DatabaseTestConnectionSchema | Database schema
    try {
      AnnotationLayerGet400Response result = apiInstance.databaseTestConnectionPost(databaseTestConnectionSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseTestConnectionPost");
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
| **databaseTestConnectionSchema** | [**DatabaseTestConnectionSchema**](DatabaseTestConnectionSchema.md)| Database schema | |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database Test Connection |  -  |
| **400** | Bad request |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

<a id="databaseValidateParametersPost"></a>
# **databaseValidateParametersPost**
> AnnotationLayerGet400Response databaseValidateParametersPost(databaseValidateParametersSchema)



Validates parameters used to connect to a database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://superset.apache.local");
    
    // Configure HTTP bearer authorization: jwt
    HttpBearerAuth jwt = (HttpBearerAuth) defaultClient.getAuthentication("jwt");
    jwt.setBearerToken("BEARER TOKEN");

    DatabaseApi apiInstance = new DatabaseApi(defaultClient);
    DatabaseValidateParametersSchema databaseValidateParametersSchema = new DatabaseValidateParametersSchema(); // DatabaseValidateParametersSchema | DB-specific parameters
    try {
      AnnotationLayerGet400Response result = apiInstance.databaseValidateParametersPost(databaseValidateParametersSchema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseApi#databaseValidateParametersPost");
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
| **databaseValidateParametersSchema** | [**DatabaseValidateParametersSchema**](DatabaseValidateParametersSchema.md)| DB-specific parameters | |

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database Test Connection |  -  |
| **400** | Bad request |  -  |
| **422** | Could not process entity |  -  |
| **500** | Fatal error |  -  |

