# openapi-java-client

FastAPI
- API version: 0.1.0
  - Build date: 2024-10-12T09:59:44.526823-04:00[America/New_York]
  - Generator version: 7.9.0

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)


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
  <version>0.1.0</version>
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
     implementation "org.openapitools:openapi-java-client:0.1.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-0.1.0.jar`
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
    defaultClient.setBasePath("http://botschaft.local");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String authorization = "authorization_example"; // String | 
    try {
      Config result = apiInstance.configConfigGet(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#configConfigGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://botschaft.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**configConfigGet**](docs/DefaultApi.md#configConfigGet) | **GET** /config | Config
*DefaultApi* | [**topicTopicTopicNameGet**](docs/DefaultApi.md#topicTopicTopicNameGet) | **GET** /topic/{topic_name} | Topic
*DiscordApi* | [**discordGetDiscordGet**](docs/DiscordApi.md#discordGetDiscordGet) | **GET** /discord | Discord Get
*DiscordApi* | [**discordPostDiscordPost**](docs/DiscordApi.md#discordPostDiscordPost) | **POST** /discord | Discord Post
*SlackApi* | [**slackGetSlackGet**](docs/SlackApi.md#slackGetSlackGet) | **GET** /slack | Slack Get
*SlackApi* | [**slackPostSlackPost**](docs/SlackApi.md#slackPostSlackPost) | **POST** /slack | Slack Post
*SnsApi* | [**snsGetSnsGet**](docs/SnsApi.md#snsGetSnsGet) | **GET** /sns | Sns Get
*SnsApi* | [**snsPostSnsPost**](docs/SnsApi.md#snsPostSnsPost) | **POST** /sns | Sns Post
*TwilioApi* | [**twilioMessageGetTwilioGet**](docs/TwilioApi.md#twilioMessageGetTwilioGet) | **GET** /twilio | Twilio Message Get
*TwilioApi* | [**twilioMessagePostTwilioPost**](docs/TwilioApi.md#twilioMessagePostTwilioPost) | **POST** /twilio | Twilio Message Post


## Documentation for Models

 - [Config](docs/Config.md)
 - [DiscordMessageRequest](docs/DiscordMessageRequest.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [SlackMessageRequest](docs/SlackMessageRequest.md)
 - [SnsMessageRequest](docs/SnsMessageRequest.md)
 - [TwilioMessageRequest](docs/TwilioMessageRequest.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



