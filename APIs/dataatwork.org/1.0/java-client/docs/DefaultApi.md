# DefaultApi

All URIs are relative to *http://api.dataatwork.org/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobsAutocompleteGet**](DefaultApi.md#jobsAutocompleteGet) | **GET** /jobs/autocomplete | Job Title Autocomplete |
| [**jobsGet**](DefaultApi.md#jobsGet) | **GET** /jobs | Job Titles and Descriptions |
| [**jobsIdGet**](DefaultApi.md#jobsIdGet) | **GET** /jobs/{id} | Job Title and Description |
| [**jobsIdRelatedJobsGet**](DefaultApi.md#jobsIdRelatedJobsGet) | **GET** /jobs/{id}/related_jobs | Jobs Associated with a Job |
| [**jobsIdRelatedSkillsGet**](DefaultApi.md#jobsIdRelatedSkillsGet) | **GET** /jobs/{id}/related_skills | Skills Associated with a Job |
| [**jobsNormalizeGet**](DefaultApi.md#jobsNormalizeGet) | **GET** /jobs/normalize | Job Title Normalization |
| [**jobsUnusualTitlesGet**](DefaultApi.md#jobsUnusualTitlesGet) | **GET** /jobs/unusual_titles | Unusual Job Titles |
| [**skillsAutocompleteGet**](DefaultApi.md#skillsAutocompleteGet) | **GET** /skills/autocomplete | Skill Name Autocomplete |
| [**skillsGet**](DefaultApi.md#skillsGet) | **GET** /skills | Skill Names and Descriptions |
| [**skillsIdGet**](DefaultApi.md#skillsIdGet) | **GET** /skills/{id} | Skill Name and Description |
| [**skillsIdRelatedJobsGet**](DefaultApi.md#skillsIdRelatedJobsGet) | **GET** /skills/{id}/related_jobs | Jobs Associated with a Skill |
| [**skillsIdRelatedSkillsGet**](DefaultApi.md#skillsIdRelatedSkillsGet) | **GET** /skills/{id}/related_skills | Skills Associated with a Skill |
| [**skillsNormalizeGet**](DefaultApi.md#skillsNormalizeGet) | **GET** /skills/normalize | Skill Name Normalization |


<a id="jobsAutocompleteGet"></a>
# **jobsAutocompleteGet**
> List&lt;Job&gt; jobsAutocompleteGet(beginsWith, contains, endsWith)

Job Title Autocomplete

Retrieves the names, descriptions, and UUIDs of all job titles matching a given search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String beginsWith = "beginsWith_example"; // String | Find job titles beginning with the given text fragment
    String contains = "contains_example"; // String | Find job titles containing the given text fragment
    String endsWith = "endsWith_example"; // String | Find job titles ending with the given text fragment
    try {
      List<Job> result = apiInstance.jobsAutocompleteGet(beginsWith, contains, endsWith);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsAutocompleteGet");
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
| **beginsWith** | **String**| Find job titles beginning with the given text fragment | [optional] |
| **contains** | **String**| Find job titles containing the given text fragment | [optional] |
| **endsWith** | **String**| Find job titles ending with the given text fragment | [optional] |

### Return type

[**List&lt;Job&gt;**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of jobs |  -  |
| **0** | Unexpected error |  -  |

<a id="jobsGet"></a>
# **jobsGet**
> List&lt;Job&gt; jobsGet(offset, limit)

Job Titles and Descriptions

Retrieves the names, descriptions, and UUIDs of all job titles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer offset = 56; // Integer | Pagination offset. Default is 0.
    Integer limit = 56; // Integer | Maximum number of items per page. Default is 20 and cannot exceed 500.
    try {
      List<Job> result = apiInstance.jobsGet(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsGet");
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
| **offset** | **Integer**| Pagination offset. Default is 0. | [optional] |
| **limit** | **Integer**| Maximum number of items per page. Default is 20 and cannot exceed 500. | [optional] |

### Return type

[**List&lt;Job&gt;**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of jobs |  -  |
| **0** | Unexpected error |  -  |

<a id="jobsIdGet"></a>
# **jobsIdGet**
> Job jobsIdGet(id, fips)

Job Title and Description

Retrieves the name, description, and UUID of a job by specifying its O*NET SOC Code or UUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The O*NET SOC Code or UUID of the job title to retrieve
    String fips = "fips_example"; // String | The FIPS Code of a Core-Based Statistical Area. Only return the job if present in this area
    try {
      Job result = apiInstance.jobsIdGet(id, fips);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsIdGet");
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
| **id** | **String**| The O*NET SOC Code or UUID of the job title to retrieve | |
| **fips** | **String**| The FIPS Code of a Core-Based Statistical Area. Only return the job if present in this area | [optional] |

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A job |  -  |
| **0** | Unexpected error |  -  |

<a id="jobsIdRelatedJobsGet"></a>
# **jobsIdRelatedJobsGet**
> JobRelatedJobs jobsIdRelatedJobsGet(id)

Jobs Associated with a Job

Retrieves a collection of jobs associated with a specified job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The UUID of the job to retrieve related jobs for
    try {
      JobRelatedJobs result = apiInstance.jobsIdRelatedJobsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsIdRelatedJobsGet");
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
| **id** | **String**| The UUID of the job to retrieve related jobs for | |

### Return type

[**JobRelatedJobs**](JobRelatedJobs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A job and its related jobs |  -  |
| **0** | Unexpected error |  -  |

<a id="jobsIdRelatedSkillsGet"></a>
# **jobsIdRelatedSkillsGet**
> JobSkills jobsIdRelatedSkillsGet(id)

Skills Associated with a Job

Retrieves a collection of skills associated with a specified job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The UUID of the job to retrieve skills for
    try {
      JobSkills result = apiInstance.jobsIdRelatedSkillsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsIdRelatedSkillsGet");
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
| **id** | **String**| The UUID of the job to retrieve skills for | |

### Return type

[**JobSkills**](JobSkills.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A job and its related skills |  -  |
| **0** | Unexpected error |  -  |

<a id="jobsNormalizeGet"></a>
# **jobsNormalizeGet**
> List&lt;NormalizedJob&gt; jobsNormalizeGet(jobTitle, limit)

Job Title Normalization

Retrieves the canonical job title for a synonymous job title

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobTitle = "jobTitle_example"; // String | Find the canonical job title(s) for jobs matching the given text fragment
    Integer limit = 56; // Integer | Maximumn number of job title synonyms to return. Default is 1 and cannot exceed 10.
    try {
      List<NormalizedJob> result = apiInstance.jobsNormalizeGet(jobTitle, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsNormalizeGet");
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
| **jobTitle** | **String**| Find the canonical job title(s) for jobs matching the given text fragment | |
| **limit** | **Integer**| Maximumn number of job title synonyms to return. Default is 1 and cannot exceed 10. | [optional] |

### Return type

[**List&lt;NormalizedJob&gt;**](NormalizedJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of normalized jobs |  -  |

<a id="jobsUnusualTitlesGet"></a>
# **jobsUnusualTitlesGet**
> List&lt;NormalizedJob&gt; jobsUnusualTitlesGet()

Unusual Job Titles

Retrieves a list of unusual job titles and the UUIDs of their canonical jobs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      List<NormalizedJob> result = apiInstance.jobsUnusualTitlesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsUnusualTitlesGet");
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

[**List&lt;NormalizedJob&gt;**](NormalizedJob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of normalized jobs |  -  |

<a id="skillsAutocompleteGet"></a>
# **skillsAutocompleteGet**
> SkillJobs skillsAutocompleteGet(beginsWith, contains, endsWith)

Skill Name Autocomplete

Retrieves the names, descriptions, and UUIDs of all skills matching a given search criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String beginsWith = "beginsWith_example"; // String | Find skill names beginning with the given text fragment
    String contains = "contains_example"; // String | Find skill names containing the given text fragment
    String endsWith = "endsWith_example"; // String | Find skill names ending with the given text fragment
    try {
      SkillJobs result = apiInstance.skillsAutocompleteGet(beginsWith, contains, endsWith);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#skillsAutocompleteGet");
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
| **beginsWith** | **String**| Find skill names beginning with the given text fragment | [optional] |
| **contains** | **String**| Find skill names containing the given text fragment | [optional] |
| **endsWith** | **String**| Find skill names ending with the given text fragment | [optional] |

### Return type

[**SkillJobs**](SkillJobs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of skills |  -  |
| **0** | Unexpected error |  -  |

<a id="skillsGet"></a>
# **skillsGet**
> List&lt;Skill&gt; skillsGet(offset, limit)

Skill Names and Descriptions

Retrieve the names, descriptions, and UUIDs of all skills.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer offset = 56; // Integer | Pagination offset. Default is 0.
    Integer limit = 56; // Integer | Maximum number of items per page. Default is 20 and cannot exceed 500.
    try {
      List<Skill> result = apiInstance.skillsGet(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#skillsGet");
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
| **offset** | **Integer**| Pagination offset. Default is 0. | [optional] |
| **limit** | **Integer**| Maximum number of items per page. Default is 20 and cannot exceed 500. | [optional] |

### Return type

[**List&lt;Skill&gt;**](Skill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of skills |  -  |
| **0** | Unexpected error |  -  |

<a id="skillsIdGet"></a>
# **skillsIdGet**
> Skill skillsIdGet(id)

Skill Name and Description

Retrieves the name, description, and UUID of a job by specifying its UUID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The UUID of the skill name to retrieve
    try {
      Skill result = apiInstance.skillsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#skillsIdGet");
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
| **id** | **String**| The UUID of the skill name to retrieve | |

### Return type

[**Skill**](Skill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A skill |  -  |
| **0** | Unexpected error |  -  |

<a id="skillsIdRelatedJobsGet"></a>
# **skillsIdRelatedJobsGet**
> SkillJobs skillsIdRelatedJobsGet(id)

Jobs Associated with a Skill

Retrieves a collection of jobs associated with a specified skill.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The UUID of the skill to retrieve jobs for
    try {
      SkillJobs result = apiInstance.skillsIdRelatedJobsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#skillsIdRelatedJobsGet");
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
| **id** | **String**| The UUID of the skill to retrieve jobs for | |

### Return type

[**SkillJobs**](SkillJobs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A skill and its related jobs |  -  |
| **0** | Unexpected error |  -  |

<a id="skillsIdRelatedSkillsGet"></a>
# **skillsIdRelatedSkillsGet**
> SkillRelatedSkills skillsIdRelatedSkillsGet(id)

Skills Associated with a Skill

Retrieves a collection of skills associated with a specified skill.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The UUID of the skill to retrieve related skills for
    try {
      SkillRelatedSkills result = apiInstance.skillsIdRelatedSkillsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#skillsIdRelatedSkillsGet");
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
| **id** | **String**| The UUID of the skill to retrieve related skills for | |

### Return type

[**SkillRelatedSkills**](SkillRelatedSkills.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A skill and its related skills |  -  |
| **0** | Unexpected error |  -  |

<a id="skillsNormalizeGet"></a>
# **skillsNormalizeGet**
> List&lt;NormalizedSkill&gt; skillsNormalizeGet(skillName)

Skill Name Normalization

Retrieves the canonical skill name for a synonymous skill name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.dataatwork.org/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String skillName = "skillName_example"; // String | Find the canonical skill name(s) for skills matching the given text fragment
    try {
      List<NormalizedSkill> result = apiInstance.skillsNormalizeGet(skillName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#skillsNormalizeGet");
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
| **skillName** | **String**| Find the canonical skill name(s) for skills matching the given text fragment | |

### Return type

[**List&lt;NormalizedSkill&gt;**](NormalizedSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of normalized skills |  -  |

