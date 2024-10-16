# openapi-java-client

Scrape Website Email API
- API version: 0.1
  - Build date: 2024-10-12T09:59:37.396837-04:00[America/New_York]
  - Generator version: 7.9.0

ScrapeWebsiteEmail is a service that exposes an api to fetch e-mails from a website.


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
  <version>0.1</version>
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
     implementation "org.openapitools:openapi-java-client:0.1"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-0.1.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.PingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://scrapewebsite.email");

    PingApi apiInstance = new PingApi(defaultClient);
    try {
      apiInstance.gETV1PingFormat();
    } catch (ApiException e) {
      System.err.println("Exception when calling PingApi#gETV1PingFormat");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://scrapewebsite.email*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PingApi* | [**gETV1PingFormat**](docs/PingApi.md#gETV1PingFormat) | **GET** /v1/ping.json | Returns whether the system is up.
*ScrapeEmailsApi* | [**gETV1ScrapeEmailsFormat**](docs/ScrapeEmailsApi.md#gETV1ScrapeEmailsFormat) | **GET** /v1/scrape_emails.json | Returns a list of emails scraped by priority (ie. e-mails appear on top level pages are first). Please note that subsequent calls to the same url will be fetched from the &lt;b&gt;cache&lt;/b&gt; (14 day flush). &lt;br/&gt;&lt;br/&gt;Will also parse patterns such as hello[at]site.com, hello[at]site[dot]com, hello(at)site.com, hello(at)site(dot)com, hello @ site.com, hello @ site . com. &lt;br/&gt;&lt;br/&gt;Please do note we cannot parse sites that require a login (for now), so for some Facebook pages it is not possible at the moment to fetch the e-mail.&lt;br/&gt;&lt;br/&gt;Finally, please note that the api will fetch links for up to 2 minutes. After that time it will start analysing the pages which have been scraped. &lt;b&gt;Therefore&lt;/b&gt; please ensure that your client has a timeout of at least &lt;b&gt;150 seconds&lt;/b&gt; (2 mins to fetch and the rest to parse). &lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that due to the fact that the api goes out to fetch the pages, the server allows only 1 concurrent request/ip. Requests which are made while the 1 request is still processing will result in a 429 code.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Please note&lt;/b&gt; that as of May 25, 2014, the main mechanism of tracking usage will be done via Mashape. You can get the free calls by signing up with the FREE plan.&lt;br/&gt;&lt;br/&gt;Please visit &lt;a href&#x3D;&#39;https://www.mashape.com/tommytcchan/scrape-website-email&#39;&gt;https://www.mashape.com/tommytcchan/scrape-website-email&lt;/a&gt;.&lt;br/&gt;&lt;br/&gt;&lt;b&gt;There is now a limit of 5 requests per day using this sample interface.&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;
*ScrapeStoreLinksApi* | [**gETV1ScrapeStoreLinksFormat**](docs/ScrapeStoreLinksApi.md#gETV1ScrapeStoreLinksFormat) | **GET** /v1/scrape_store_links.json | Attempts to grab the google store url or the ios store url for a site, after searching through the site.


## Documentation for Models



<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



