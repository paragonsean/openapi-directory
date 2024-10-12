# SnykApi.TestApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testComposerJsonComposerLockFile**](TestApi.md#testComposerJsonComposerLockFile) | **POST** /test/composer | Test composer.json &amp; composer.lock file
[**testDepGraph**](TestApi.md#testDepGraph) | **POST** /test/dep-graph | Test Dep Graph
[**testForIssuesInAPublicGemByNameAndVersion**](TestApi.md#testForIssuesInAPublicGemByNameAndVersion) | **GET** /test/rubygems/{gemName}/{version} | Test for issues in a public gem by name and version
[**testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion**](TestApi.md#testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion) | **GET** /test/maven/{groupId}/{artifactId}/{version} | Test for issues in a public package by group id, artifact id and version
[**testForIssuesInAPublicPackageByGroupNameAndVersion**](TestApi.md#testForIssuesInAPublicPackageByGroupNameAndVersion) | **GET** /test/gradle/{group}/{name}/{version} | Test for issues in a public package by group, name and version
[**testForIssuesInAPublicPackageByNameAndVersion**](TestApi.md#testForIssuesInAPublicPackageByNameAndVersion) | **GET** /test/npm/{packageName}/{version} | Test for issues in a public package by name and version
[**testGemfileLockFile**](TestApi.md#testGemfileLockFile) | **POST** /test/rubygems | Test gemfile.lock file
[**testGopkgTomlGopkgLockFile**](TestApi.md#testGopkgTomlGopkgLockFile) | **POST** /test/golangdep | Test Gopkg.toml &amp; Gopkg.lock File
[**testGradleFile**](TestApi.md#testGradleFile) | **POST** /test/gradle | Test gradle file
[**testMavenFile**](TestApi.md#testMavenFile) | **POST** /test/maven | Test maven file
[**testPackageJsonPackageLockJsonFile**](TestApi.md#testPackageJsonPackageLockJsonFile) | **POST** /test/npm | Test package.json &amp; package-lock.json File
[**testPackageJsonYarnLockFile**](TestApi.md#testPackageJsonYarnLockFile) | **POST** /test/yarn | Test package.json &amp; yarn.lock File
[**testPipPackageNameVersionGet**](TestApi.md#testPipPackageNameVersionGet) | **GET** /test/pip/{packageName}/{version} | Test for issues in a public package by name and version
[**testRequirementsTxtFile**](TestApi.md#testRequirementsTxtFile) | **POST** /test/pip | Test requirements.txt file
[**testSbtFile**](TestApi.md#testSbtFile) | **POST** /test/sbt | Test sbt file
[**testSbtGroupIdArtifactIdVersionGet**](TestApi.md#testSbtGroupIdArtifactIdVersionGet) | **GET** /test/sbt/{groupId}/{artifactId}/{version} | Test for issues in a public package by group id, artifact id and version
[**testVendorJsonFile**](TestApi.md#testVendorJsonFile) | **POST** /test/govendor | Test vendor.json File



## testComposerJsonComposerLockFile

> testComposerJsonComposerLockFile(opts)

Test composer.json &amp; composer.lock file

You can test your Composer packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;composer.json&#x60; and a &#x60;composer.lock&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testComposerJsonComposerLockFileRequest': new SnykApi.TestComposerJsonComposerLockFileRequest() // TestComposerJsonComposerLockFileRequest | 
};
apiInstance.testComposerJsonComposerLockFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testComposerJsonComposerLockFileRequest** | [**TestComposerJsonComposerLockFileRequest**](TestComposerJsonComposerLockFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testDepGraph

> testDepGraph(opts)

Test Dep Graph

Use this endpoint to find issues in a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7", // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
  'testDepGraphRequest': new SnykApi.TestDepGraphRequest() // TestDepGraphRequest | 
};
apiInstance.testDepGraph(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 
 **testDepGraphRequest** | [**TestDepGraphRequest**](TestDepGraphRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testForIssuesInAPublicGemByNameAndVersion

> testForIssuesInAPublicGemByNameAndVersion(gemName, version, opts)

Test for issues in a public gem by name and version

You can test &#x60;rubygems&#x60; packages for issues according to their name and version.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let gemName = "rails-html-sanitizer"; // String | The gem name.
let version = "1.0.3"; // String | The gem version to test.
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7" // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
};
apiInstance.testForIssuesInAPublicGemByNameAndVersion(gemName, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gemName** | **String**| The gem name. | 
 **version** | **String**| The gem version to test. | 
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion

> testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(groupId, artifactId, version, opts)

Test for issues in a public package by group id, artifact id and version

You can test &#x60;maven&#x60; packages for issues according to their [coordinates](https://maven.apache.org/pom.html#Maven_Coordinates): group ID, artifact ID and version. The repository hosting the package may also be customized (see the &#x60;repository&#x60; query parameter).

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let groupId = "org.apache.flex.blazeds"; // String | The package's group ID.
let artifactId = "blazeds"; // String | The package's artifact ID.
let version = "4.7.2"; // String | The package version to test.
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7", // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
  'repository': "https://repo1.maven.org/maven2" // String | The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
};
apiInstance.testForIssuesInAPublicPackageByGroupIdArtifactIdAndVersion(groupId, artifactId, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupId** | **String**| The package&#39;s group ID. | 
 **artifactId** | **String**| The package&#39;s artifact ID. | 
 **version** | **String**| The package version to test. | 
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 
 **repository** | **String**| The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## testForIssuesInAPublicPackageByGroupNameAndVersion

> testForIssuesInAPublicPackageByGroupNameAndVersion(group, name, version, opts)

Test for issues in a public package by group, name and version

You can test &#x60;gradle&#x60; packages for issues according to their group, name and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let group = "org.apache.flex.blazeds"; // String | The package's group ID.
let name = "blazeds"; // String | The package's artifact ID.
let version = "4.7.2"; // String | The package version to test.
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7", // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
  'repository': "https://repo1.maven.org/maven2" // String | The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
};
apiInstance.testForIssuesInAPublicPackageByGroupNameAndVersion(group, name, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **String**| The package&#39;s group ID. | 
 **name** | **String**| The package&#39;s artifact ID. | 
 **version** | **String**| The package version to test. | 
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 
 **repository** | **String**| The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## testForIssuesInAPublicPackageByNameAndVersion

> testForIssuesInAPublicPackageByNameAndVersion(packageName, version, opts)

Test for issues in a public package by name and version

You can test &#x60;npm&#x60; packages for issues according to their name and version.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let packageName = "ms"; // String | The package name. For scoped packages, **must** be url-encoded, so to test \"@angular/core\" version 4.3.2, one should `GET /test/npm/%40angular%2Fcore/4.3.2`.
let version = "0.7.0"; // String | The Package version to test.
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7" // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
};
apiInstance.testForIssuesInAPublicPackageByNameAndVersion(packageName, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| The package name. For scoped packages, **must** be url-encoded, so to test \&quot;@angular/core\&quot; version 4.3.2, one should &#x60;GET /test/npm/%40angular%2Fcore/4.3.2&#x60;. | 
 **version** | **String**| The Package version to test. | 
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## testGemfileLockFile

> testGemfileLockFile(opts)

Test gemfile.lock file

You can test your rubygems applications for issues according to their lockfile using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;Gemfile.lock&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testGemfileLockFileRequest': new SnykApi.TestGemfileLockFileRequest() // TestGemfileLockFileRequest | 
};
apiInstance.testGemfileLockFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testGemfileLockFileRequest** | [**TestGemfileLockFileRequest**](TestGemfileLockFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testGopkgTomlGopkgLockFile

> testGopkgTomlGopkgLockFile(opts)

Test Gopkg.toml &amp; Gopkg.lock File

You can test your Go dep packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;Gopkg.toml&#x60; and a &#x60;Gopkg.lock&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7", // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
  'testGopkgTomlGopkgLockFileRequest': new SnykApi.TestGopkgTomlGopkgLockFileRequest() // TestGopkgTomlGopkgLockFileRequest | 
};
apiInstance.testGopkgTomlGopkgLockFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 
 **testGopkgTomlGopkgLockFileRequest** | [**TestGopkgTomlGopkgLockFileRequest**](TestGopkgTomlGopkgLockFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testGradleFile

> testGradleFile(opts)

Test gradle file

You can test your Gradle packages for issues according to their manifest file using this action. It takes a JSON object containing the \&quot;target\&quot; &#x60;build.gradle&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testGradleFileRequest': new SnykApi.TestGradleFileRequest() // TestGradleFileRequest | 
};
apiInstance.testGradleFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testGradleFileRequest** | [**TestGradleFileRequest**](TestGradleFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testMavenFile

> testMavenFile(opts)

Test maven file

You can test your Maven packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;pom.xml&#x60;.  Additional manifest files, if they are needed, like parent &#x60;pom.xml&#x60; files, child poms, etc., according the the definitions in the target &#x60;pom.xml&#x60; file, should be supplied in the &#x60;additional&#x60; body parameter.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7", // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
  'repository': "https://repo1.maven.org/maven2", // String | The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
  'testMavenFileRequest': new SnykApi.TestMavenFileRequest() // TestMavenFileRequest | 
};
apiInstance.testMavenFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 
 **repository** | **String**| The Maven repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] 
 **testMavenFileRequest** | [**TestMavenFileRequest**](TestMavenFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testPackageJsonPackageLockJsonFile

> testPackageJsonPackageLockJsonFile(opts)

Test package.json &amp; package-lock.json File

You can test your npm packages for issues according to their manifest file &amp; optional lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and optionally a &#x60;package-lock.json&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testPackageJsonPackageLockJsonFileRequest': new SnykApi.TestPackageJsonPackageLockJsonFileRequest() // TestPackageJsonPackageLockJsonFileRequest | 
};
apiInstance.testPackageJsonPackageLockJsonFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testPackageJsonPackageLockJsonFileRequest** | [**TestPackageJsonPackageLockJsonFileRequest**](TestPackageJsonPackageLockJsonFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testPackageJsonYarnLockFile

> testPackageJsonYarnLockFile(opts)

Test package.json &amp; yarn.lock File

You can test your yarn packages for issues according to their manifest file &amp; lockfile using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;package.json&#x60; and a &#x60;yarn.lock&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testPackageJsonYarnLockFileRequest': new SnykApi.TestPackageJsonYarnLockFileRequest() // TestPackageJsonYarnLockFileRequest | 
};
apiInstance.testPackageJsonYarnLockFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testPackageJsonYarnLockFileRequest** | [**TestPackageJsonYarnLockFileRequest**](TestPackageJsonYarnLockFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testPipPackageNameVersionGet

> testPipPackageNameVersionGet(packageName, version, opts)

Test for issues in a public package by name and version

You can test &#x60;pip&#x60; packages for issues according to their name and version.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let packageName = "rsa"; // String | The package name.
let version = "3.3"; // String | The Package version to test.
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7" // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
};
apiInstance.testPipPackageNameVersionGet(packageName, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **packageName** | **String**| The package name. | 
 **version** | **String**| The Package version to test. | 
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## testRequirementsTxtFile

> testRequirementsTxtFile(opts)

Test requirements.txt file

You can test your pip packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;requirements.txt&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testRequirementsTxtFileRequest': new SnykApi.TestRequirementsTxtFileRequest() // TestRequirementsTxtFileRequest | 
};
apiInstance.testRequirementsTxtFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testRequirementsTxtFileRequest** | [**TestRequirementsTxtFileRequest**](TestRequirementsTxtFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testSbtFile

> testSbtFile(opts)

Test sbt file

You can test your &#x60;sbt&#x60; packages for issues according to their manifest file using this action. It takes a JSON object containing a the \&quot;target\&quot; &#x60;build.sbt&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testSbtFileRequest': new SnykApi.TestSbtFileRequest() // TestSbtFileRequest | 
};
apiInstance.testSbtFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testSbtFileRequest** | [**TestSbtFileRequest**](TestSbtFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## testSbtGroupIdArtifactIdVersionGet

> testSbtGroupIdArtifactIdVersionGet(groupId, artifactId, version, opts)

Test for issues in a public package by group id, artifact id and version

You can test &#x60;sbt&#x60; packages for issues according to their group ID, artifact ID and version. This is done via the maven endpoint (for Java), since the packages are hosted on maven central or a compatible repository. See \&quot;Maven\&quot; above for details.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let groupId = "org.apache.flex.blazeds"; // String | The package's group ID.
let artifactId = "blazeds"; // String | The package's artifact ID.
let version = "4.7.2"; // String | The package version to test.
let opts = {
  'org': "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7", // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
  'repository': "https://repo1.maven.org/maven2" // String | The repository hosting this package. The default value is Maven Central. More than one value is supported, in order.
};
apiInstance.testSbtGroupIdArtifactIdVersionGet(groupId, artifactId, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupId** | **String**| The package&#39;s group ID. | 
 **artifactId** | **String**| The package&#39;s artifact ID. | 
 **version** | **String**| The package version to test. | 
 **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] 
 **repository** | **String**| The repository hosting this package. The default value is Maven Central. More than one value is supported, in order. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## testVendorJsonFile

> testVendorJsonFile(opts)

Test vendor.json File

You can test your Go vendor packages for issues according to their manifest file using this action. It takes a JSON object containing a \&quot;target\&quot; &#x60;vendor.json&#x60;.

### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.TestApi();
let opts = {
  'testVendorJsonFileRequest': new SnykApi.TestVendorJsonFileRequest() // TestVendorJsonFileRequest | 
};
apiInstance.testVendorJsonFile(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **testVendorJsonFileRequest** | [**TestVendorJsonFileRequest**](TestVendorJsonFileRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

