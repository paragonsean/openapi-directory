# TestApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**testComposerJsonComposerLockFile**](TestApi.md#testComposerJsonComposerLockFile) | **POST** /test/composer | Test composer.json &amp; composer.lock file |
| [**testDepGraph**](TestApi.md#testDepGraph) | **POST** /test/dep-graph | Test Dep Graph |
| [**testForIssuesInAPublicGemByNameAndVersion**](TestApi.md#testForIssuesInAPublicGemByNameAndVersion) | **GET** /test/rubygems/{gemName}/{version} | Test for issues in a public gem by name and version |
| [**testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion**](TestApi.md#testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion) | **GET** /test/maven/{groupId}/{artifactId}/{version} | Test for issues in a public package by group id, artifact id and version |
| [**testForIssuesInAPublicPackageByGroupNameAndVersion**](TestApi.md#testForIssuesInAPublicPackageByGroupNameAndVersion) | **GET** /test/gradle/{group}/{name}/{version} | Test for issues in a public package by group, name and version |
| [**testForIssuesInAPublicPackageByNameAndVersion**](TestApi.md#testForIssuesInAPublicPackageByNameAndVersion) | **GET** /test/npm/{packageName}/{version} | Test for issues in a public package by name and version |
| [**testGemfileLockFile**](TestApi.md#testGemfileLockFile) | **POST** /test/rubygems | Test gemfile.lock file |
| [**testGopkgTomlGopkgLockFile**](TestApi.md#testGopkgTomlGopkgLockFile) | **POST** /test/golangdep | Test Gopkg.toml &amp; Gopkg.lock File |
| [**testGradleFile**](TestApi.md#testGradleFile) | **POST** /test/gradle | Test gradle file |
| [**testMavenFile**](TestApi.md#testMavenFile) | **POST** /test/maven | Test maven file |
| [**testPackageJsonPackageLockJsonFile**](TestApi.md#testPackageJsonPackageLockJsonFile) | **POST** /test/npm | Test package.json &amp; package-lock.json File |
| [**testPackageJsonYarnLockFile**](TestApi.md#testPackageJsonYarnLockFile) | **POST** /test/yarn | Test package.json &amp; yarn.lock File |
| [**testPipPackageNameVersionGet**](TestApi.md#testPipPackageNameVersionGet) | **GET** /test/pip/{packageName}/{version} | Test for issues in a public package by name and version |
| [**testRequirementsTxtFile**](TestApi.md#testRequirementsTxtFile) | **POST** /test/pip | Test requirements.txt file |
| [**testSbtFile**](TestApi.md#testSbtFile) | **POST** /test/sbt | Test sbt file |
| [**testSbtGroupIdArtifactIdVersionGet**](TestApi.md#testSbtGroupIdArtifactIdVersionGet) | **GET** /test/sbt/{groupId}/{artifactId}/{version} | Test for issues in a public package by group id, artifact id and version |
| [**testVendorJsonFile**](TestApi.md#testVendorJsonFile) | **POST** /test/govendor | Test vendor.json File |


<a id="testComposerJsonComposerLockFile"></a>
# **testComposerJsonComposerLockFile**
> testComposerJsonComposerLockFile(testComposerJsonComposerLockFileRequest)

Test composer.json &amp; composer.lock file

You can test your Composer packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;composer.json&#x60; and a &#x60;composer.lock&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestComposerJsonComposerLockFileRequest testComposerJsonComposerLockFileRequest = new TestComposerJsonComposerLockFileRequest(); // TestComposerJsonComposerLockFileRequest | 
    try {
      apiInstance.testComposerJsonComposerLockFile(testComposerJsonComposerLockFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testComposerJsonComposerLockFile");
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
| **testComposerJsonComposerLockFileRequest** | [**TestComposerJsonComposerLockFileRequest**](TestComposerJsonComposerLockFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testDepGraph"></a>
# **testDepGraph**
> testDepGraph(org, testDepGraphRequest)

Test Dep Graph

Use this endpoint to find issues in a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    TestDepGraphRequest testDepGraphRequest = new TestDepGraphRequest(); // TestDepGraphRequest | 
    try {
      apiInstance.testDepGraph(org, testDepGraphRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testDepGraph");
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
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |
| **testDepGraphRequest** | [**TestDepGraphRequest**](TestDepGraphRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testForIssuesInAPublicGemByNameAndVersion"></a>
# **testForIssuesInAPublicGemByNameAndVersion**
> testForIssuesInAPublicGemByNameAndVersion(gemName, version, org)

Test for issues in a public gem by name and version

You can test &#x60;rubygems&#x60; packages for issues according to their name and version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String gemName = "rails-html-sanitizer"; // String | The gem name.
    String version = "1.0.3"; // String | The gem version to test.
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    try {
      apiInstance.testForIssuesInAPublicGemByNameAndVersion(gemName, version, org);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testForIssuesInAPublicGemByNameAndVersion");
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
| **gemName** | **String**| The gem name. | |
| **version** | **String**| The gem version to test. | |
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion"></a>
# **testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion**
> testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(groupId, artifactId, version, org, repository)

Test for issues in a public package by group id, artifact id and version

You can test &#x60;maven&#x60; packages for issues according to their [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates): group ID, artifact ID and version. The repository hosting the package may also be customized (see the &#x60;repository&#x60; query parameter).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String groupId = "org.apache.flex.blazeds"; // String | The package's group ID.
    String artifactId = "blazeds"; // String | The package's artifact ID.
    String version = "4.7.2"; // String | The package version to test.
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    String repository = "https://repo1.maven.org/maven2"; // String | The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    try {
      apiInstance.testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(groupId, artifactId, version, org, repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion");
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
| **groupId** | **String**| The package&#39;s group ID. | |
| **artifactId** | **String**| The package&#39;s artifact ID. | |
| **version** | **String**| The package version to test. | |
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |
| **repository** | **String**| The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testForIssuesInAPublicPackageByGroupNameAndVersion"></a>
# **testForIssuesInAPublicPackageByGroupNameAndVersion**
> testForIssuesInAPublicPackageByGroupNameAndVersion(group, name, version, org, repository)

Test for issues in a public package by group, name and version

You can test &#x60;gradle&#x60; packages for issues according to their group, name and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String group = "org.apache.flex.blazeds"; // String | The package's group ID.
    String name = "blazeds"; // String | The package's artifact ID.
    String version = "4.7.2"; // String | The package version to test.
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    String repository = "https://repo1.maven.org/maven2"; // String | The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    try {
      apiInstance.testForIssuesInAPublicPackageByGroupNameAndVersion(group, name, version, org, repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testForIssuesInAPublicPackageByGroupNameAndVersion");
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
| **group** | **String**| The package&#39;s group ID. | |
| **name** | **String**| The package&#39;s artifact ID. | |
| **version** | **String**| The package version to test. | |
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |
| **repository** | **String**| The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testForIssuesInAPublicPackageByNameAndVersion"></a>
# **testForIssuesInAPublicPackageByNameAndVersion**
> testForIssuesInAPublicPackageByNameAndVersion(packageName, version, org)

Test for issues in a public package by name and version

You can test &#x60;npm&#x60; packages for issues according to their name and version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String packageName = "ms"; // String | The package name. For scoped packages, **must** be url-encoded, so to test \"@angular/core\" version 4.3.2, one should `GET /test/npm/%40angular%2Fcore/4.3.2`.
    String version = "0.7.0"; // String | The Package version to test.
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    try {
      apiInstance.testForIssuesInAPublicPackageByNameAndVersion(packageName, version, org);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testForIssuesInAPublicPackageByNameAndVersion");
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
| **packageName** | **String**| The package name. For scoped packages, **must** be url-encoded, so to test \&quot;@angular/core\&quot; version 4.3.2, one should &#x60;GET /test/npm/%40angular%2Fcore/4.3.2&#x60;. | |
| **version** | **String**| The Package version to test. | |
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGemfileLockFile"></a>
# **testGemfileLockFile**
> testGemfileLockFile(testGemfileLockFileRequest)

Test gemfile.lock file

You can test your rubygems applications for issues according to their lockfile using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;Gemfile.lock&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestGemfileLockFileRequest testGemfileLockFileRequest = new TestGemfileLockFileRequest(); // TestGemfileLockFileRequest | 
    try {
      apiInstance.testGemfileLockFile(testGemfileLockFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGemfileLockFile");
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
| **testGemfileLockFileRequest** | [**TestGemfileLockFileRequest**](TestGemfileLockFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGopkgTomlGopkgLockFile"></a>
# **testGopkgTomlGopkgLockFile**
> testGopkgTomlGopkgLockFile(org, testGopkgTomlGopkgLockFileRequest)

Test Gopkg.toml &amp; Gopkg.lock File

You can test your Go dep packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;Gopkg.toml&#x60; and a &#x60;Gopkg.lock&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    TestGopkgTomlGopkgLockFileRequest testGopkgTomlGopkgLockFileRequest = new TestGopkgTomlGopkgLockFileRequest(); // TestGopkgTomlGopkgLockFileRequest | 
    try {
      apiInstance.testGopkgTomlGopkgLockFile(org, testGopkgTomlGopkgLockFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGopkgTomlGopkgLockFile");
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
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |
| **testGopkgTomlGopkgLockFileRequest** | [**TestGopkgTomlGopkgLockFileRequest**](TestGopkgTomlGopkgLockFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testGradleFile"></a>
# **testGradleFile**
> testGradleFile(testGradleFileRequest)

Test gradle file

You can test your Gradle packages for issues according to their manifest file using this action. It takes a JSON object containing the \&quot;target\&quot; &#x60;build.gradle&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestGradleFileRequest testGradleFileRequest = new TestGradleFileRequest(); // TestGradleFileRequest | 
    try {
      apiInstance.testGradleFile(testGradleFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testGradleFile");
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
| **testGradleFileRequest** | [**TestGradleFileRequest**](TestGradleFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testMavenFile"></a>
# **testMavenFile**
> testMavenFile(org, repository, testMavenFileRequest)

Test maven file

You can test your Maven packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;pom.xml&#x60;.  Additional manifest files, if they are needed, like parent &#x60;pom.xml&#x60; files, child poms, etc., according the the definitions in the target &#x60;pom.xml&#x60; file, should be supplied in the &#x60;additional&#x60; body parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    String repository = "https://repo1.maven.org/maven2"; // String | The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    TestMavenFileRequest testMavenFileRequest = new TestMavenFileRequest(); // TestMavenFileRequest | 
    try {
      apiInstance.testMavenFile(org, repository, testMavenFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testMavenFile");
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
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |
| **repository** | **String**| The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] |
| **testMavenFileRequest** | [**TestMavenFileRequest**](TestMavenFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testPackageJsonPackageLockJsonFile"></a>
# **testPackageJsonPackageLockJsonFile**
> testPackageJsonPackageLockJsonFile(testPackageJsonPackageLockJsonFileRequest)

Test package.json &amp; package-lock.json File

You can test your npm packages for issues according to their manifest file &amp; optional lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and optionally a &#x60;package-lock.json&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestPackageJsonPackageLockJsonFileRequest testPackageJsonPackageLockJsonFileRequest = new TestPackageJsonPackageLockJsonFileRequest(); // TestPackageJsonPackageLockJsonFileRequest | 
    try {
      apiInstance.testPackageJsonPackageLockJsonFile(testPackageJsonPackageLockJsonFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testPackageJsonPackageLockJsonFile");
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
| **testPackageJsonPackageLockJsonFileRequest** | [**TestPackageJsonPackageLockJsonFileRequest**](TestPackageJsonPackageLockJsonFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testPackageJsonYarnLockFile"></a>
# **testPackageJsonYarnLockFile**
> testPackageJsonYarnLockFile(testPackageJsonYarnLockFileRequest)

Test package.json &amp; yarn.lock File

You can test your yarn packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and a &#x60;yarn.lock&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestPackageJsonYarnLockFileRequest testPackageJsonYarnLockFileRequest = new TestPackageJsonYarnLockFileRequest(); // TestPackageJsonYarnLockFileRequest | 
    try {
      apiInstance.testPackageJsonYarnLockFile(testPackageJsonYarnLockFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testPackageJsonYarnLockFile");
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
| **testPackageJsonYarnLockFileRequest** | [**TestPackageJsonYarnLockFileRequest**](TestPackageJsonYarnLockFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testPipPackageNameVersionGet"></a>
# **testPipPackageNameVersionGet**
> testPipPackageNameVersionGet(packageName, version, org)

Test for issues in a public package by name and version

You can test &#x60;pip&#x60; packages for issues according to their name and version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String packageName = "rsa"; // String | The package name.
    String version = "3.3"; // String | The Package version to test.
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    try {
      apiInstance.testPipPackageNameVersionGet(packageName, version, org);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testPipPackageNameVersionGet");
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
| **packageName** | **String**| The package name. | |
| **version** | **String**| The Package version to test. | |
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testRequirementsTxtFile"></a>
# **testRequirementsTxtFile**
> testRequirementsTxtFile(testRequirementsTxtFileRequest)

Test requirements.txt file

You can test your pip packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;requirements.txt&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestRequirementsTxtFileRequest testRequirementsTxtFileRequest = new TestRequirementsTxtFileRequest(); // TestRequirementsTxtFileRequest | 
    try {
      apiInstance.testRequirementsTxtFile(testRequirementsTxtFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testRequirementsTxtFile");
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
| **testRequirementsTxtFileRequest** | [**TestRequirementsTxtFileRequest**](TestRequirementsTxtFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testSbtFile"></a>
# **testSbtFile**
> testSbtFile(testSbtFileRequest)

Test sbt file

You can test your &#x60;sbt&#x60; packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;build.sbt&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestSbtFileRequest testSbtFileRequest = new TestSbtFileRequest(); // TestSbtFileRequest | 
    try {
      apiInstance.testSbtFile(testSbtFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testSbtFile");
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
| **testSbtFileRequest** | [**TestSbtFileRequest**](TestSbtFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testSbtGroupIdArtifactIdVersionGet"></a>
# **testSbtGroupIdArtifactIdVersionGet**
> testSbtGroupIdArtifactIdVersionGet(groupId, artifactId, version, org, repository)

Test for issues in a public package by group id, artifact id and version

You can test &#x60;sbt&#x60; packages for issues according to their group ID, artifact ID and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    String groupId = "org.apache.flex.blazeds"; // String | The package's group ID.
    String artifactId = "blazeds"; // String | The package's artifact ID.
    String version = "4.7.2"; // String | The package version to test.
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    String repository = "https://repo1.maven.org/maven2"; // String | The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
    try {
      apiInstance.testSbtGroupIdArtifactIdVersionGet(groupId, artifactId, version, org, repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testSbtGroupIdArtifactIdVersionGet");
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
| **groupId** | **String**| The package&#39;s group ID. | |
| **artifactId** | **String**| The package&#39;s artifact ID. | |
| **version** | **String**| The package version to test. | |
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |
| **repository** | **String**| The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="testVendorJsonFile"></a>
# **testVendorJsonFile**
> testVendorJsonFile(testVendorJsonFileRequest)

Test vendor.json File

You can test your Go vendor packages for issues according to their manifest file using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;vendor.json&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    TestApi apiInstance = new TestApi(defaultClient);
    TestVendorJsonFileRequest testVendorJsonFileRequest = new TestVendorJsonFileRequest(); // TestVendorJsonFileRequest | 
    try {
      apiInstance.testVendorJsonFile(testVendorJsonFileRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestApi#testVendorJsonFile");
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
| **testVendorJsonFileRequest** | [**TestVendorJsonFileRequest**](TestVendorJsonFileRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

