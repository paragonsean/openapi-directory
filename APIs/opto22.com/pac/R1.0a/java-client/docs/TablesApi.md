# TablesApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**readFloatTableElement_0**](TablesApi.md#readFloatTableElement_0) | **GET** /device/strategy/tables/floats/{tableName}/{index} |  |
| [**readFloatTable_0**](TablesApi.md#readFloatTable_0) | **GET** /device/strategy/tables/floats/{tableName} |  |
| [**readFloatTables_0**](TablesApi.md#readFloatTables_0) | **GET** /device/strategy/tables/floats |  |
| [**readInt32TableElement_0**](TablesApi.md#readInt32TableElement_0) | **GET** /device/strategy/tables/int32s/{tableName}/{index} |  |
| [**readInt32Table_0**](TablesApi.md#readInt32Table_0) | **GET** /device/strategy/tables/int32s/{tableName} |  |
| [**readInt32Tables_0**](TablesApi.md#readInt32Tables_0) | **GET** /device/strategy/tables/int32s |  |
| [**readInt64TableAsString_0**](TablesApi.md#readInt64TableAsString_0) | **GET** /device/strategy/tables/int64s/{tableName}/_string |  |
| [**readInt64TableElementAsString_0**](TablesApi.md#readInt64TableElementAsString_0) | **GET** /device/strategy/tables/int64s/{tableName}/{index}/_string |  |
| [**readInt64TableElement_0**](TablesApi.md#readInt64TableElement_0) | **GET** /device/strategy/tables/int64s/{tableName}/{index} |  |
| [**readInt64Table_0**](TablesApi.md#readInt64Table_0) | **GET** /device/strategy/tables/int64s/{tableName} |  |
| [**readInt64Tables_0**](TablesApi.md#readInt64Tables_0) | **GET** /device/strategy/tables/int64s |  |
| [**readStringTableElement_0**](TablesApi.md#readStringTableElement_0) | **GET** /device/strategy/tables/strings/{tableName}/{index} |  |
| [**readStringTable_0**](TablesApi.md#readStringTable_0) | **GET** /device/strategy/tables/strings/{tableName} |  |
| [**readStringTables_0**](TablesApi.md#readStringTables_0) | **GET** /device/strategy/tables/strings |  |
| [**writeFloatTableElement_0**](TablesApi.md#writeFloatTableElement_0) | **POST** /device/strategy/tables/floats/{tableName}/{index} |  |
| [**writeFloatTable_0**](TablesApi.md#writeFloatTable_0) | **POST** /device/strategy/tables/floats/{tableName} |  |
| [**writeInt32TableElement_0**](TablesApi.md#writeInt32TableElement_0) | **POST** /device/strategy/tables/int32s/{tableName}/{index} |  |
| [**writeInt32Table_0**](TablesApi.md#writeInt32Table_0) | **POST** /device/strategy/tables/int32s/{tableName} |  |
| [**writeInt64TableAsString_0**](TablesApi.md#writeInt64TableAsString_0) | **POST** /device/strategy/tables/int64s/{tableName}/_string |  |
| [**writeInt64TableElementAsString_0**](TablesApi.md#writeInt64TableElementAsString_0) | **POST** /device/strategy/tables/int64s/{tableName}/{index}/_string |  |
| [**writeInt64TableElement_0**](TablesApi.md#writeInt64TableElement_0) | **POST** /device/strategy/tables/int64s/{tableName}/{index} |  |
| [**writeInt64Table_0**](TablesApi.md#writeInt64Table_0) | **POST** /device/strategy/tables/int64s/{tableName} |  |
| [**writeStringTableElement_0**](TablesApi.md#writeStringTableElement_0) | **POST** /device/strategy/tables/strings/{tableName}/{index} |  |
| [**writeStringTable_0**](TablesApi.md#writeStringTable_0) | **POST** /device/strategy/tables/strings/{tableName} |  |


<a id="readFloatTableElement_0"></a>
# **readFloatTableElement_0**
> FloatValueObject readFloatTableElement_0(tableName, index)



Read specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      FloatValueObject result = apiInstance.readFloatTableElement_0(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readFloatTableElement_0");
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
| **tableName** | **String**| Name of float table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readFloatTable_0"></a>
# **readFloatTable_0**
> List&lt;Float&gt; readFloatTable_0(tableName, startIndex, numElements)



Read table elements #### Examples #### * Read all elements in a table named ftable: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable * Read elements 5 and up in a table named ftable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;5 * Read 3 consecutive elements in a table named ftable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<Float> result = apiInstance.readFloatTable_0(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readFloatTable_0");
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
| **tableName** | **String**| Name of float table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;Float&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readFloatTables_0"></a>
# **readFloatTables_0**
> List&lt;TableDef&gt; readFloatTables_0()



Returns an array of the name and length of all the float tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readFloatTables_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readFloatTables_0");
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

[**List&lt;TableDef&gt;**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="readInt32TableElement_0"></a>
# **readInt32TableElement_0**
> Int32ValueObject readInt32TableElement_0(tableName, index)



Read specified integer32 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer32 table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      Int32ValueObject result = apiInstance.readInt32TableElement_0(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt32TableElement_0");
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
| **tableName** | **String**| Name of the integer32 table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**Int32ValueObject**](Int32ValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readInt32Table_0"></a>
# **readInt32Table_0**
> List&lt;Integer&gt; readInt32Table_0(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified integer32 table\&quot;  #### Examples ####  * Read all elements in a table named itable: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable  * Read elements 5 and up in a table named itable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named itable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<Integer> result = apiInstance.readInt32Table_0(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt32Table_0");
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
| **tableName** | **String**| Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readInt32Tables_0"></a>
# **readInt32Tables_0**
> List&lt;TableDef&gt; readInt32Tables_0()



Returns an array of the name and length of all the integer32 tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readInt32Tables_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt32Tables_0");
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

[**List&lt;TableDef&gt;**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="readInt64TableAsString_0"></a>
# **readInt64TableAsString_0**
> List&lt;String&gt; readInt64TableAsString_0(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<String> result = apiInstance.readInt64TableAsString_0(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt64TableAsString_0");
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
| **tableName** | **String**| Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readInt64TableElementAsString_0"></a>
# **readInt64TableElementAsString_0**
> Int64StringValueObject readInt64TableElementAsString_0(tableName, index)



Read specified integer64 table element as string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      Int64StringValueObject result = apiInstance.readInt64TableElementAsString_0(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt64TableElementAsString_0");
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
| **tableName** | **String**| Name of integer64 table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**Int64StringValueObject**](Int64StringValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readInt64TableElement_0"></a>
# **readInt64TableElement_0**
> Int64ValueObject readInt64TableElement_0(tableName, index)



Read specified integer64 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      Int64ValueObject result = apiInstance.readInt64TableElement_0(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt64TableElement_0");
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
| **tableName** | **String**| Name of integer64 table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**Int64ValueObject**](Int64ValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readInt64Table_0"></a>
# **readInt64Table_0**
> List&lt;Long&gt; readInt64Table_0(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<Long> result = apiInstance.readInt64Table_0(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt64Table_0");
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
| **tableName** | **String**| Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;Long&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readInt64Tables_0"></a>
# **readInt64Tables_0**
> List&lt;TableDef&gt; readInt64Tables_0()



Returns an array of the name and length of all the integer64 tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readInt64Tables_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readInt64Tables_0");
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

[**List&lt;TableDef&gt;**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="readStringTableElement_0"></a>
# **readStringTableElement_0**
> StringValueObject readStringTableElement_0(tableName, index)



Read specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to read
    Integer index = 56; // Integer | Index of element to read
    try {
      StringValueObject result = apiInstance.readStringTableElement_0(tableName, index);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readStringTableElement_0");
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
| **tableName** | **String**| Name of string table to read | |
| **index** | **Integer**| Index of element to read | |

### Return type

[**StringValueObject**](StringValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readStringTable_0"></a>
# **readStringTable_0**
> List&lt;String&gt; readStringTable_0(tableName, startIndex, numElements)



\&quot;Read a range of table elements from the specified string table\&quot;  #### Examples ####  * Read all elements in a table named strTable: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to read; starting index and number of elements may be specified (defaults to all elements)
    Integer startIndex = 56; // Integer | Index of first element to read (default is 0)
    Integer numElements = 56; // Integer | Number of elements to read (default is number of elements in the table minus startIndex)
    try {
      List<String> result = apiInstance.readStringTable_0(tableName, startIndex, numElements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readStringTable_0");
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
| **tableName** | **String**| Name of string table to read; starting index and number of elements may be specified (defaults to all elements) | |
| **startIndex** | **Integer**| Index of first element to read (default is 0) | [optional] |
| **numElements** | **Integer**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="readStringTables_0"></a>
# **readStringTables_0**
> List&lt;TableDef&gt; readStringTables_0()



Returns an array of the name and length of all the string tables in the strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    try {
      List<TableDef> result = apiInstance.readStringTables_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#readStringTables_0");
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

[**List&lt;TableDef&gt;**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |

<a id="writeFloatTableElement_0"></a>
# **writeFloatTableElement_0**
> writeFloatTableElement_0(tableName, index, floatElementObject)



Write specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to write
    Integer index = 56; // Integer | Index of element to write
    FloatValueObject floatElementObject = new FloatValueObject(); // FloatValueObject | Element to write starting at index
    try {
      apiInstance.writeFloatTableElement_0(tableName, index, floatElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeFloatTableElement_0");
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
| **tableName** | **String**| Name of float table to write | |
| **index** | **Integer**| Index of element to write | |
| **floatElementObject** | [**FloatValueObject**](FloatValueObject.md)| Element to write starting at index | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeFloatTable_0"></a>
# **writeFloatTable_0**
> writeFloatTable_0(tableName, floatArray, startIndex)



Write table elements #### Examples #### * Write the values (1.5, 2.4, 3.5) to 3 consecutive elements in a table named ftable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10  with body of the POST request set to [ 1.5, 2.4, 3.5 ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of float table to write; starting index may be specified
    List<Float> floatArray = Arrays.asList(); // List<Float> | Array of element values to write starting at startIndex
    Integer startIndex = 56; // Integer | Index of first element to write (default is 0)
    try {
      apiInstance.writeFloatTable_0(tableName, floatArray, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeFloatTable_0");
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
| **tableName** | **String**| Name of float table to write; starting index may be specified | |
| **floatArray** | [**List&lt;Float&gt;**](Float.md)| Array of element values to write starting at startIndex | |
| **startIndex** | **Integer**| Index of first element to write (default is 0) | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeInt32TableElement_0"></a>
# **writeInt32TableElement_0**
> writeInt32TableElement_0(tableName, index, int32ElementObject)



Write specified integer32 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer32 table to write
    Integer index = 56; // Integer | Index of element to write
    Int32ValueObject int32ElementObject = new Int32ValueObject(); // Int32ValueObject | Element to write at index specified
    try {
      apiInstance.writeInt32TableElement_0(tableName, index, int32ElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeInt32TableElement_0");
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
| **tableName** | **String**| Name of the integer32 table to write | |
| **index** | **Integer**| Index of element to write | |
| **int32ElementObject** | [**Int32ValueObject**](Int32ValueObject.md)| Element to write at index specified | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeInt32Table_0"></a>
# **writeInt32Table_0**
> writeInt32Table_0(tableName, int32Array, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named itable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ]       

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer32 table to write; starting index may be specified
    List<Integer> int32Array = Arrays.asList(); // List<Integer> | Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored
    Integer startIndex = 56; // Integer | Index of first element to write (default is 0)
    try {
      apiInstance.writeInt32Table_0(tableName, int32Array, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeInt32Table_0");
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
| **tableName** | **String**| Name of integer32 table to write; starting index may be specified | |
| **int32Array** | [**List&lt;Integer&gt;**](Integer.md)| Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored | |
| **startIndex** | **Integer**| Index of first element to write (default is 0) | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeInt64TableAsString_0"></a>
# **writeInt64TableAsString_0**
> writeInt64TableAsString_0(tableName, int64AsStringArray, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10  with body of the POST request set to [ \&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot; ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
    List<String> int64AsStringArray = Arrays.asList(); // List<String> | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    Integer startIndex = 56; // Integer | Index of first element to write; default is 0.
    try {
      apiInstance.writeInt64TableAsString_0(tableName, int64AsStringArray, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeInt64TableAsString_0");
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
| **tableName** | **String**| Name of integer64 table to write; starting index may be specified | |
| **int64AsStringArray** | [**List&lt;String&gt;**](String.md)| Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored | |
| **startIndex** | **Integer**| Index of first element to write; default is 0. | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeInt64TableElementAsString_0"></a>
# **writeInt64TableElementAsString_0**
> writeInt64TableElementAsString_0(tableName, index, int64ElementObject)



Write specified integer64 table element as string

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to write
    Integer index = 56; // Integer | Index of element to write
    Int64StringValueObject int64ElementObject = new Int64StringValueObject(); // Int64StringValueObject | Element to write starting at index specified
    try {
      apiInstance.writeInt64TableElementAsString_0(tableName, index, int64ElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeInt64TableElementAsString_0");
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
| **tableName** | **String**| Name of the integer64 table to write | |
| **index** | **Integer**| Index of element to write | |
| **int64ElementObject** | [**Int64StringValueObject**](Int64StringValueObject.md)| Element to write starting at index specified | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeInt64TableElement_0"></a>
# **writeInt64TableElement_0**
> writeInt64TableElement_0(tableName, index, int64ElementObject)



Write specified integer64 table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of the integer64 table to write
    Integer index = 56; // Integer | Index of element to write
    Int64ValueObject int64ElementObject = new Int64ValueObject(); // Int64ValueObject | Element to write starting at index specified
    try {
      apiInstance.writeInt64TableElement_0(tableName, index, int64ElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeInt64TableElement_0");
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
| **tableName** | **String**| Name of the integer64 table to write | |
| **index** | **Integer**| Index of element to write | |
| **int64ElementObject** | [**Int64ValueObject**](Int64ValueObject.md)| Element to write starting at index specified | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeInt64Table_0"></a>
# **writeInt64Table_0**
> writeInt64Table_0(tableName, int64Array, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
    List<Long> int64Array = Arrays.asList(); // List<Long> | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
    Integer startIndex = 56; // Integer | Index of first element to write; default is 0
    try {
      apiInstance.writeInt64Table_0(tableName, int64Array, startIndex);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeInt64Table_0");
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
| **tableName** | **String**| Name of integer64 table to write; starting index may be specified | |
| **int64Array** | [**List&lt;Long&gt;**](Long.md)| Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored | |
| **startIndex** | **Integer**| Index of first element to write; default is 0 | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeStringTableElement_0"></a>
# **writeStringTableElement_0**
> writeStringTableElement_0(tableName, index, stringElementObject)



Write specified table element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to write
    Integer index = 56; // Integer | Index of element to write
    StringValueObject stringElementObject = new StringValueObject(); // StringValueObject | Element to write starting at index
    try {
      apiInstance.writeStringTableElement_0(tableName, index, stringElementObject);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeStringTableElement_0");
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
| **tableName** | **String**| Name of string table to write | |
| **index** | **Integer**| Index of element to write | |
| **stringElementObject** | [**StringValueObject**](StringValueObject.md)| Element to write starting at index | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="writeStringTable_0"></a>
# **writeStringTable_0**
> ErrorResponse200OKish writeStringTable_0(tableName, stringArray, startIndex)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (\&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot;) to 3 consecutive elements in a table named strTable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/strings/strtable?startIndex&#x3D;10  with body of the POST request set to [ \&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot; ] 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    TablesApi apiInstance = new TablesApi(defaultClient);
    String tableName = "tableName_example"; // String | Name of string table to write; starting index may be specified
    List<String> stringArray = Arrays.asList(); // List<String> | Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit
    Integer startIndex = 56; // Integer | Index of first element to write (default is 0)
    try {
      ErrorResponse200OKish result = apiInstance.writeStringTable_0(tableName, stringArray, startIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TablesApi#writeStringTable_0");
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
| **tableName** | **String**| Name of string table to write; starting index may be specified | |
| **stringArray** | [**List&lt;String&gt;**](String.md)| Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit | |
| **startIndex** | **Integer**| Index of first element to write (default is 0) | [optional] |

### Return type

[**ErrorResponse200OKish**](ErrorResponse200OKish.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - but check details for any error messages |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

