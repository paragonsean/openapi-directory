# openapi-java-client

Background Removal API
- API version: 1.0.0
  - Build date: 2024-10-12T09:59:19.553431-04:00[America/New_York]
  - Generator version: 7.9.0

Remove the background of any image


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
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.BackgroundRemovalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.remove.bg/v1.0");
    
    // Configure API key authorization: APIKeyHeader
    ApiKeyAuth APIKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("APIKeyHeader");
    APIKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIKeyHeader.setApiKeyPrefix("Token");

    BackgroundRemovalApi apiInstance = new BackgroundRemovalApi(defaultClient);
    RemoveBgJson removeBgJson = new RemoveBgJson(); // RemoveBgJson | 
    try {
      RemoveBgJsonResponse result = apiInstance.removebgPost(removeBgJson);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackgroundRemovalApi#removebgPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.remove.bg/v1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BackgroundRemovalApi* | [**removebgPost**](docs/BackgroundRemovalApi.md#removebgPost) | **POST** /removebg | Remove the background of an image
*FetchAccountInfoApi* | [**accountGet**](docs/FetchAccountInfoApi.md#accountGet) | **GET** /account | Fetch credit balance and free API calls.
*ImprovementProgramApi* | [**improvePost**](docs/ImprovementProgramApi.md#improvePost) | **POST** /improve | 


## Documentation for Models

 - [AccountGet200Response](docs/AccountGet200Response.md)
 - [AccountGet200ResponseData](docs/AccountGet200ResponseData.md)
 - [AccountGet200ResponseDataAttributes](docs/AccountGet200ResponseDataAttributes.md)
 - [AccountGet200ResponseDataAttributesApi](docs/AccountGet200ResponseDataAttributesApi.md)
 - [AccountGet200ResponseDataAttributesCredits](docs/AccountGet200ResponseDataAttributesCredits.md)
 - [AuthFailed](docs/AuthFailed.md)
 - [AuthFailedErrorsInner](docs/AuthFailedErrorsInner.md)
 - [ImprovePost400Response](docs/ImprovePost400Response.md)
 - [ImprovePost400ResponseErrorsInner](docs/ImprovePost400ResponseErrorsInner.md)
 - [ImprovementProgramJson](docs/ImprovementProgramJson.md)
 - [ImprovementProgramJsonResponse](docs/ImprovementProgramJsonResponse.md)
 - [RateLimit](docs/RateLimit.md)
 - [RateLimitErrorsInner](docs/RateLimitErrorsInner.md)
 - [RemoveBgJson](docs/RemoveBgJson.md)
 - [RemoveBgJsonResponse](docs/RemoveBgJsonResponse.md)
 - [RemoveBgJsonResponseData](docs/RemoveBgJsonResponseData.md)
 - [RemovebgPost400Response](docs/RemovebgPost400Response.md)
 - [RemovebgPost400ResponseErrorsInner](docs/RemovebgPost400ResponseErrorsInner.md)
 - [RemovebgPost402Response](docs/RemovebgPost402Response.md)
 - [RemovebgPost402ResponseErrorsInner](docs/RemovebgPost402ResponseErrorsInner.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="APIKeyHeader"></a>
### APIKeyHeader

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



