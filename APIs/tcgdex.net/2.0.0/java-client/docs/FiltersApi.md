# FiltersApi

All URIs are relative to *https://api.tcgdex.net/v2/en*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesCategoryGet**](FiltersApi.md#categoriesCategoryGet) | **GET** /categories/{category} |  |
| [**categoriesGet**](FiltersApi.md#categoriesGet) | **GET** /categories |  |
| [**dexIdsDexIdGet**](FiltersApi.md#dexIdsDexIdGet) | **GET** /dex-ids/{dexId} |  |
| [**dexIdsGet**](FiltersApi.md#dexIdsGet) | **GET** /dex-ids |  |
| [**energyTypesEnergyTypeGet**](FiltersApi.md#energyTypesEnergyTypeGet) | **GET** /energy-types/{energy-type} |  |
| [**energyTypesGet**](FiltersApi.md#energyTypesGet) | **GET** /energy-types |  |
| [**hpGet**](FiltersApi.md#hpGet) | **GET** /hp |  |
| [**hpHpGet**](FiltersApi.md#hpHpGet) | **GET** /hp/{hp} |  |
| [**illustratorsGet**](FiltersApi.md#illustratorsGet) | **GET** /illustrators |  |
| [**illustratorsIllustratorGet**](FiltersApi.md#illustratorsIllustratorGet) | **GET** /illustrators/{illustrator} |  |
| [**raritiesGet**](FiltersApi.md#raritiesGet) | **GET** /rarities |  |
| [**raritiesRarityGet**](FiltersApi.md#raritiesRarityGet) | **GET** /rarities/{rarity} |  |
| [**regulationMarksGet**](FiltersApi.md#regulationMarksGet) | **GET** /regulation-marks |  |
| [**regulationMarksRegulationMarkGet**](FiltersApi.md#regulationMarksRegulationMarkGet) | **GET** /regulation-marks/{regulation-mark} |  |
| [**retreatsGet**](FiltersApi.md#retreatsGet) | **GET** /retreats |  |
| [**retreatsRetreatGet**](FiltersApi.md#retreatsRetreatGet) | **GET** /retreats/{retreat} |  |
| [**seriesGet**](FiltersApi.md#seriesGet) | **GET** /series |  |
| [**seriesSerieGet**](FiltersApi.md#seriesSerieGet) | **GET** /series/{serie} |  |
| [**setsGet**](FiltersApi.md#setsGet) | **GET** /sets |  |
| [**setsSetGet**](FiltersApi.md#setsSetGet) | **GET** /sets/{set} |  |
| [**stagesGet**](FiltersApi.md#stagesGet) | **GET** /stages |  |
| [**stagesStageGet**](FiltersApi.md#stagesStageGet) | **GET** /stages/{stage} |  |
| [**suffixesGet**](FiltersApi.md#suffixesGet) | **GET** /suffixes |  |
| [**suffixesSuffixGet**](FiltersApi.md#suffixesSuffixGet) | **GET** /suffixes/{suffix} |  |
| [**trainerTypesGet**](FiltersApi.md#trainerTypesGet) | **GET** /trainer-types |  |
| [**trainerTypesTrainerTypeGet**](FiltersApi.md#trainerTypesTrainerTypeGet) | **GET** /trainer-types/{trainer-type} |  |
| [**typesGet**](FiltersApi.md#typesGet) | **GET** /types |  |
| [**typesTypeGet**](FiltersApi.md#typesTypeGet) | **GET** /types/{type} |  |
| [**variantsGet**](FiltersApi.md#variantsGet) | **GET** /variants |  |
| [**variantsVariantGet**](FiltersApi.md#variantsVariantGet) | **GET** /variants/{variant} |  |


<a id="categoriesCategoryGet"></a>
# **categoriesCategoryGet**
> StringEndpoint categoriesCategoryGet(category)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String category = "category_example"; // String | 
    try {
      StringEndpoint result = apiInstance.categoriesCategoryGet(category);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#categoriesCategoryGet");
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
| **category** | **String**|  | |

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List cards with the category |  -  |
| **404** | The Category doesn&#39;t exist |  -  |

<a id="categoriesGet"></a>
# **categoriesGet**
> List&lt;String&gt; categoriesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.categoriesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#categoriesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List cards categories |  -  |

<a id="dexIdsDexIdGet"></a>
# **dexIdsDexIdGet**
> List&lt;CardResume&gt; dexIdsDexIdGet(dexId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String dexId = "dexId_example"; // String | 
    try {
      List<CardResume> result = apiInstance.dexIdsDexIdGet(dexId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#dexIdsDexIdGet");
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
| **dexId** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the cards containing the specified dexId |  -  |
| **404** | no cards contain the specified dexID |  -  |

<a id="dexIdsGet"></a>
# **dexIdsGet**
> List&lt;String&gt; dexIdsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.dexIdsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#dexIdsGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List all possible Pokemon(s) Pokédex Ids that appeared in the TCG |  -  |

<a id="energyTypesEnergyTypeGet"></a>
# **energyTypesEnergyTypeGet**
> List&lt;CardResume&gt; energyTypesEnergyTypeGet(energyType)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String energyType = "energyType_example"; // String | 
    try {
      List<CardResume> result = apiInstance.energyTypesEnergyTypeGet(energyType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#energyTypesEnergyTypeGet");
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
| **energyType** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the Energy cards containing the specified energy-type |  -  |
| **404** | The specified energy-type doesn&#39;t exist |  -  |

<a id="energyTypesGet"></a>
# **energyTypesGet**
> List&lt;String&gt; energyTypesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.energyTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#energyTypesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list the different Energy types an Energy card can have |  -  |

<a id="hpGet"></a>
# **hpGet**
> List&lt;String&gt; hpGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.hpGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#hpGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List all different possibilities number of HP a card can have |  -  |

<a id="hpHpGet"></a>
# **hpHpGet**
> StringEndpoint hpHpGet(hp)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String hp = "hp_example"; // String | 
    try {
      StringEndpoint result = apiInstance.hpHpGet(hp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#hpHpGet");
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
| **hp** | **String**|  | |

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the Pokémon cards containing specified number of HP |  -  |
| **404** | The HP count doesn&#39;t exist |  -  |

<a id="illustratorsGet"></a>
# **illustratorsGet**
> List&lt;String&gt; illustratorsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.illustratorsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#illustratorsGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all the Pokémon cards illustrators |  -  |

<a id="illustratorsIllustratorGet"></a>
# **illustratorsIllustratorGet**
> StringEndpoint illustratorsIllustratorGet(illustrator)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String illustrator = "illustrator_example"; // String | 
    try {
      StringEndpoint result = apiInstance.illustratorsIllustratorGet(illustrator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#illustratorsIllustratorGet");
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
| **illustrator** | **String**|  | |

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the cards containing the specified illustrator |  -  |
| **404** | The Illustrator doesn&#39;t exist |  -  |

<a id="raritiesGet"></a>
# **raritiesGet**
> List&lt;String&gt; raritiesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.raritiesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#raritiesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List cards rarities |  -  |

<a id="raritiesRarityGet"></a>
# **raritiesRarityGet**
> StringEndpoint raritiesRarityGet(rarity)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String rarity = "rarity_example"; // String | 
    try {
      StringEndpoint result = apiInstance.raritiesRarityGet(rarity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#raritiesRarityGet");
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
| **rarity** | **String**|  | |

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the cards containing the specified rarity |  -  |
| **404** | The Rarity doesn&#39;t exist |  -  |

<a id="regulationMarksGet"></a>
# **regulationMarksGet**
> List&lt;String&gt; regulationMarksGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.regulationMarksGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#regulationMarksGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List the current regulation marks |  -  |

<a id="regulationMarksRegulationMarkGet"></a>
# **regulationMarksRegulationMarkGet**
> List&lt;CardResume&gt; regulationMarksRegulationMarkGet(regulationMark)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String regulationMark = "regulationMark_example"; // String | 
    try {
      List<CardResume> result = apiInstance.regulationMarksRegulationMarkGet(regulationMark);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#regulationMarksRegulationMarkGet");
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
| **regulationMark** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get every cards respecting the specified regulation-mark |  -  |
| **404** | The regulation-mark doesn&#39;t exist |  -  |

<a id="retreatsGet"></a>
# **retreatsGet**
> List&lt;String&gt; retreatsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.retreatsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#retreatsGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | return the different number of retreats count |  -  |

<a id="retreatsRetreatGet"></a>
# **retreatsRetreatGet**
> StringEndpoint retreatsRetreatGet(retreat)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String retreat = "retreat_example"; // String | 
    try {
      StringEndpoint result = apiInstance.retreatsRetreatGet(retreat);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#retreatsRetreatGet");
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
| **retreat** | **String**|  | |

### Return type

[**StringEndpoint**](StringEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the cards containing the specified retreat count |  -  |
| **404** | The Retreat count doesn&#39;t exist |  -  |

<a id="seriesGet"></a>
# **seriesGet**
> List&lt;SerieResume&gt; seriesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<SerieResume> result = apiInstance.seriesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#seriesGet");
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

[**List&lt;SerieResume&gt;**](SerieResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |

<a id="seriesSerieGet"></a>
# **seriesSerieGet**
> Serie seriesSerieGet(serie)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String serie = "serie_example"; // String | the serie ID or name
    try {
      Serie result = apiInstance.seriesSerieGet(serie);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#seriesSerieGet");
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
| **serie** | **String**| the serie ID or name | |

### Return type

[**Serie**](Serie.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | The Serie doesn&#39;t exist |  -  |

<a id="setsGet"></a>
# **setsGet**
> List&lt;SetResume&gt; setsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<SetResume> result = apiInstance.setsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#setsGet");
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

[**List&lt;SetResume&gt;**](SetResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |

<a id="setsSetGet"></a>
# **setsSetGet**
> Set setsSetGet(set)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String set = "set_example"; // String | the set ID or the set name
    try {
      Set result = apiInstance.setsSetGet(set);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#setsSetGet");
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
| **set** | **String**| the set ID or the set name | |

### Return type

[**Set**](Set.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | The Set doesn&#39;t exist |  -  |

<a id="stagesGet"></a>
# **stagesGet**
> List&lt;String&gt; stagesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.stagesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#stagesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all the possible stages a Pokémon card can have |  -  |

<a id="stagesStageGet"></a>
# **stagesStageGet**
> List&lt;CardResume&gt; stagesStageGet(stage)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String stage = "stage_example"; // String | 
    try {
      List<CardResume> result = apiInstance.stagesStageGet(stage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#stagesStageGet");
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
| **stage** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all the cards having the specified stage |  -  |
| **404** | The stage doesn&#39;t exist |  -  |

<a id="suffixesGet"></a>
# **suffixesGet**
> List&lt;String&gt; suffixesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.suffixesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#suffixesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all the cards having the specified suffix |  -  |

<a id="suffixesSuffixGet"></a>
# **suffixesSuffixGet**
> List&lt;CardResume&gt; suffixesSuffixGet(suffix)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String suffix = "suffix_example"; // String | 
    try {
      List<CardResume> result = apiInstance.suffixesSuffixGet(suffix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#suffixesSuffixGet");
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
| **suffix** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all the cards having the specified stage suffix |  -  |
| **404** | The suffix doesn&#39;t exist |  -  |

<a id="trainerTypesGet"></a>
# **trainerTypesGet**
> List&lt;String&gt; trainerTypesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.trainerTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#trainerTypesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the different trainer-types |  -  |

<a id="trainerTypesTrainerTypeGet"></a>
# **trainerTypesTrainerTypeGet**
> List&lt;CardResume&gt; trainerTypesTrainerTypeGet(trainerType)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String trainerType = "trainerType_example"; // String | 
    try {
      List<CardResume> result = apiInstance.trainerTypesTrainerTypeGet(trainerType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#trainerTypesTrainerTypeGet");
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
| **trainerType** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the cards containing with the specified trainer-type |  -  |
| **404** | The trainer-type doesn&#39;t exist |  -  |

<a id="typesGet"></a>
# **typesGet**
> List&lt;String&gt; typesGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.typesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#typesGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List all possible cards types |  -  |

<a id="typesTypeGet"></a>
# **typesTypeGet**
> List&lt;CardResume&gt; typesTypeGet(type)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String type = "type_example"; // String | 
    try {
      List<CardResume> result = apiInstance.typesTypeGet(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#typesTypeGet");
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
| **type** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the cards containing the specified type |  -  |
| **404** | The Type doesn&#39;t exist |  -  |

<a id="variantsGet"></a>
# **variantsGet**
> List&lt;String&gt; variantsGet()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    try {
      List<String> result = apiInstance.variantsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#variantsGet");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the different variants available |  -  |

<a id="variantsVariantGet"></a>
# **variantsVariantGet**
> List&lt;CardResume&gt; variantsVariantGet(variant)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tcgdex.net/v2/en");

    FiltersApi apiInstance = new FiltersApi(defaultClient);
    String variant = "variant_example"; // String | 
    try {
      List<CardResume> result = apiInstance.variantsVariantGet(variant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FiltersApi#variantsVariantGet");
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
| **variant** | **String**|  | |

### Return type

[**List&lt;CardResume&gt;**](CardResume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the cards available in the specified variant |  -  |
| **404** | The variant doesn&#39;t exist |  -  |

