# PeoplegeneratorapiApplicationApi

All URIs are relative to *http://peoplegeneratorapi.live*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**age**](PeoplegeneratorapiApplicationApi.md#age) | **GET** /api/person/age/ |  |
| [**age1**](PeoplegeneratorapiApplicationApi.md#age1) | **GET** /api/person/age |  |
| [**bloodtype**](PeoplegeneratorapiApplicationApi.md#bloodtype) | **GET** /api/person/bloodtype/ |  |
| [**bloodtype1**](PeoplegeneratorapiApplicationApi.md#bloodtype1) | **GET** /api/person/bloodtype |  |
| [**creditcardnumber**](PeoplegeneratorapiApplicationApi.md#creditcardnumber) | **GET** /api/person/creditcardnumber |  |
| [**creditcardnumber1**](PeoplegeneratorapiApplicationApi.md#creditcardnumber1) | **GET** /api/person/creditcardnumber/ |  |
| [**creditscore**](PeoplegeneratorapiApplicationApi.md#creditscore) | **GET** /api/person/creditscore/ |  |
| [**creditscore1**](PeoplegeneratorapiApplicationApi.md#creditscore1) | **GET** /api/person/creditscore |  |
| [**email**](PeoplegeneratorapiApplicationApi.md#email) | **GET** /api/person/email |  |
| [**email1**](PeoplegeneratorapiApplicationApi.md#email1) | **GET** /api/person/email/ |  |
| [**eyecolor**](PeoplegeneratorapiApplicationApi.md#eyecolor) | **GET** /api/person/eyecolor/ |  |
| [**eyecolor1**](PeoplegeneratorapiApplicationApi.md#eyecolor1) | **GET** /api/person/eyecolor |  |
| [**gender**](PeoplegeneratorapiApplicationApi.md#gender) | **GET** /api/person/gender |  |
| [**gender1**](PeoplegeneratorapiApplicationApi.md#gender1) | **GET** /api/person/gender/ |  |
| [**generateAddress**](PeoplegeneratorapiApplicationApi.md#generateAddress) | **GET** /api/address |  |
| [**generateAddress1**](PeoplegeneratorapiApplicationApi.md#generateAddress1) | **GET** /api/address/ |  |
| [**generateLifeStory**](PeoplegeneratorapiApplicationApi.md#generateLifeStory) | **GET** /api/lifestory/ |  |
| [**generateLifeStory1**](PeoplegeneratorapiApplicationApi.md#generateLifeStory1) | **GET** /api/lifestory |  |
| [**getCompressedPerson**](PeoplegeneratorapiApplicationApi.md#getCompressedPerson) | **GET** /api/person/{number}/ |  |
| [**getCompressedPerson1**](PeoplegeneratorapiApplicationApi.md#getCompressedPerson1) | **GET** /api/person/{number} |  |
| [**getPerson**](PeoplegeneratorapiApplicationApi.md#getPerson) | **GET** /api/person/ |  |
| [**getPerson1**](PeoplegeneratorapiApplicationApi.md#getPerson1) | **GET** /api/person |  |
| [**gpa**](PeoplegeneratorapiApplicationApi.md#gpa) | **GET** /api/person/gpa |  |
| [**gpa1**](PeoplegeneratorapiApplicationApi.md#gpa1) | **GET** /api/person/gpa/ |  |
| [**haschildren**](PeoplegeneratorapiApplicationApi.md#haschildren) | **GET** /api/person/haschildren/ |  |
| [**haschildren1**](PeoplegeneratorapiApplicationApi.md#haschildren1) | **GET** /api/person/haschildren |  |
| [**hasdegree**](PeoplegeneratorapiApplicationApi.md#hasdegree) | **GET** /api/person/hasdegree |  |
| [**hasdegree1**](PeoplegeneratorapiApplicationApi.md#hasdegree1) | **GET** /api/person/hasdegree/ |  |
| [**height**](PeoplegeneratorapiApplicationApi.md#height) | **GET** /api/person/height |  |
| [**height1**](PeoplegeneratorapiApplicationApi.md#height1) | **GET** /api/person/height/ |  |
| [**income**](PeoplegeneratorapiApplicationApi.md#income) | **GET** /api/person/income |  |
| [**income1**](PeoplegeneratorapiApplicationApi.md#income1) | **GET** /api/person/income/ |  |
| [**job**](PeoplegeneratorapiApplicationApi.md#job) | **GET** /api/person/job |  |
| [**job1**](PeoplegeneratorapiApplicationApi.md#job1) | **GET** /api/person/job/ |  |
| [**maritalstatus**](PeoplegeneratorapiApplicationApi.md#maritalstatus) | **GET** /api/person/maritalstatus/ |  |
| [**maritalstatus1**](PeoplegeneratorapiApplicationApi.md#maritalstatus1) | **GET** /api/person/maritalstatus |  |
| [**name**](PeoplegeneratorapiApplicationApi.md#name) | **GET** /api/person/name/ |  |
| [**name1**](PeoplegeneratorapiApplicationApi.md#name1) | **GET** /api/person/name |  |
| [**politicalLeaning**](PeoplegeneratorapiApplicationApi.md#politicalLeaning) | **GET** /api/person/politicalleaning |  |
| [**politicalLeaning1**](PeoplegeneratorapiApplicationApi.md#politicalLeaning1) | **GET** /api/person/politicalleaning/ |  |
| [**religion**](PeoplegeneratorapiApplicationApi.md#religion) | **GET** /api/person/religion/ |  |
| [**religion1**](PeoplegeneratorapiApplicationApi.md#religion1) | **GET** /api/person/religion |  |
| [**username**](PeoplegeneratorapiApplicationApi.md#username) | **GET** /api/person/username/ |  |
| [**username1**](PeoplegeneratorapiApplicationApi.md#username1) | **GET** /api/person/username |  |
| [**weight**](PeoplegeneratorapiApplicationApi.md#weight) | **GET** /api/person/weight |  |
| [**weight1**](PeoplegeneratorapiApplicationApi.md#weight1) | **GET** /api/person/weight/ |  |


<a id="age"></a>
# **age**
> Integer age()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Integer result = apiInstance.age();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#age");
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

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="age1"></a>
# **age1**
> Integer age1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Integer result = apiInstance.age1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#age1");
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

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bloodtype"></a>
# **bloodtype**
> String bloodtype()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.bloodtype();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#bloodtype");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="bloodtype1"></a>
# **bloodtype1**
> String bloodtype1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.bloodtype1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#bloodtype1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="creditcardnumber"></a>
# **creditcardnumber**
> String creditcardnumber()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.creditcardnumber();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#creditcardnumber");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="creditcardnumber1"></a>
# **creditcardnumber1**
> String creditcardnumber1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.creditcardnumber1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#creditcardnumber1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="creditscore"></a>
# **creditscore**
> Integer creditscore()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Integer result = apiInstance.creditscore();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#creditscore");
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

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="creditscore1"></a>
# **creditscore1**
> Integer creditscore1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Integer result = apiInstance.creditscore1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#creditscore1");
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

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="email"></a>
# **email**
> String email()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.email();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#email");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="email1"></a>
# **email1**
> String email1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.email1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#email1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="eyecolor"></a>
# **eyecolor**
> String eyecolor()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.eyecolor();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#eyecolor");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="eyecolor1"></a>
# **eyecolor1**
> String eyecolor1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.eyecolor1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#eyecolor1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gender"></a>
# **gender**
> String gender()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.gender();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#gender");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gender1"></a>
# **gender1**
> String gender1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.gender1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#gender1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="generateAddress"></a>
# **generateAddress**
> Address generateAddress()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Address result = apiInstance.generateAddress();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#generateAddress");
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

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="generateAddress1"></a>
# **generateAddress1**
> Address generateAddress1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Address result = apiInstance.generateAddress1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#generateAddress1");
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

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="generateLifeStory"></a>
# **generateLifeStory**
> Lifestory generateLifeStory()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Lifestory result = apiInstance.generateLifeStory();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#generateLifeStory");
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

[**Lifestory**](Lifestory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="generateLifeStory1"></a>
# **generateLifeStory1**
> Lifestory generateLifeStory1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Lifestory result = apiInstance.generateLifeStory1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#generateLifeStory1");
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

[**Lifestory**](Lifestory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCompressedPerson"></a>
# **getCompressedPerson**
> List&lt;byte[]&gt; getCompressedPerson(number)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      List<byte[]> result = apiInstance.getCompressedPerson(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#getCompressedPerson");
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
| **number** | **Integer**|  | |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCompressedPerson1"></a>
# **getCompressedPerson1**
> List&lt;byte[]&gt; getCompressedPerson1(number)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      List<byte[]> result = apiInstance.getCompressedPerson1(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#getCompressedPerson1");
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
| **number** | **Integer**|  | |

### Return type

**List&lt;byte[]&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPerson"></a>
# **getPerson**
> Person getPerson()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Person result = apiInstance.getPerson();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#getPerson");
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

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getPerson1"></a>
# **getPerson1**
> Person getPerson1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Person result = apiInstance.getPerson1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#getPerson1");
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

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gpa"></a>
# **gpa**
> Double gpa()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.gpa();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#gpa");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gpa1"></a>
# **gpa1**
> Double gpa1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.gpa1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#gpa1");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="haschildren"></a>
# **haschildren**
> Boolean haschildren()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Boolean result = apiInstance.haschildren();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#haschildren");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="haschildren1"></a>
# **haschildren1**
> Boolean haschildren1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Boolean result = apiInstance.haschildren1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#haschildren1");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hasdegree"></a>
# **hasdegree**
> Boolean hasdegree()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Boolean result = apiInstance.hasdegree();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#hasdegree");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="hasdegree1"></a>
# **hasdegree1**
> Boolean hasdegree1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Boolean result = apiInstance.hasdegree1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#hasdegree1");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="height"></a>
# **height**
> Double height()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.height();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#height");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="height1"></a>
# **height1**
> Double height1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.height1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#height1");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="income"></a>
# **income**
> Integer income()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Integer result = apiInstance.income();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#income");
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

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="income1"></a>
# **income1**
> Integer income1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Integer result = apiInstance.income1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#income1");
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

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="job"></a>
# **job**
> String job()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.job();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#job");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="job1"></a>
# **job1**
> String job1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.job1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#job1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="maritalstatus"></a>
# **maritalstatus**
> Boolean maritalstatus()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Boolean result = apiInstance.maritalstatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#maritalstatus");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="maritalstatus1"></a>
# **maritalstatus1**
> Boolean maritalstatus1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Boolean result = apiInstance.maritalstatus1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#maritalstatus1");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="name"></a>
# **name**
> String name()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.name();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#name");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="name1"></a>
# **name1**
> String name1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.name1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#name1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="politicalLeaning"></a>
# **politicalLeaning**
> Double politicalLeaning()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.politicalLeaning();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#politicalLeaning");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="politicalLeaning1"></a>
# **politicalLeaning1**
> Double politicalLeaning1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.politicalLeaning1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#politicalLeaning1");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="religion"></a>
# **religion**
> String religion()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.religion();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#religion");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="religion1"></a>
# **religion1**
> String religion1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.religion1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#religion1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="username"></a>
# **username**
> String username()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.username();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#username");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="username1"></a>
# **username1**
> String username1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      String result = apiInstance.username1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#username1");
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
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="weight"></a>
# **weight**
> Double weight()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.weight();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#weight");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="weight1"></a>
# **weight1**
> Double weight1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeoplegeneratorapiApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://peoplegeneratorapi.live");

    PeoplegeneratorapiApplicationApi apiInstance = new PeoplegeneratorapiApplicationApi(defaultClient);
    try {
      Double result = apiInstance.weight1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeoplegeneratorapiApplicationApi#weight1");
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

**Double**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

