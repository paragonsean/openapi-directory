# openapi-java-client

RESTful4Up
- API version: 1.0.0
  - Build date: 2024-10-12T09:56:55.437812-04:00[America/New_York]
  - Generator version: 7.9.0

RESTful API 4 Unipacker


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://restful4up.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | file
    List<String> rules = Arrays.asList(); // List<String> | 
    String isUnpackingRequired = "true"; // String | 
    try {
      ApplyYaraRules200Response result = apiInstance.applyYaraRules(_file, rules, isUnpackingRequired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#applyYaraRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://restful4up.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**applyYaraRules**](docs/DefaultApi.md#applyYaraRules) | **POST** /apply-yara-rules | 
*DefaultApi* | [**clean**](docs/DefaultApi.md#clean) | **HEAD** /clean | 
*DefaultApi* | [**emulationOutput**](docs/DefaultApi.md#emulationOutput) | **POST** /emulation-output | 
*DefaultApi* | [**generatePartialYaraRule**](docs/DefaultApi.md#generatePartialYaraRule) | **POST** /generate-partial-yara-rules | 
*DefaultApi* | [**unpack**](docs/DefaultApi.md#unpack) | **POST** /unpack | 


## Documentation for Models

 - [ApplyYaraRule](docs/ApplyYaraRule.md)
 - [ApplyYaraRuleMatchedYaraRulesInnerInner](docs/ApplyYaraRuleMatchedYaraRulesInnerInner.md)
 - [ApplyYaraRules200Response](docs/ApplyYaraRules200Response.md)
 - [EmulationOutput200Response](docs/EmulationOutput200Response.md)
 - [Error](docs/Error.md)
 - [GeneratePartialYaraRule200Response](docs/GeneratePartialYaraRule200Response.md)
 - [Yara](docs/Yara.md)
 - [YaraMeta](docs/YaraMeta.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



