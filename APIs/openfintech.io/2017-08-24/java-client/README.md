# openapi-java-client

OpenFinTech.io
- API version: 2017-08-24
  - Build date: 2024-10-12T11:28:06.060998-04:00[America/New_York]
  - Generator version: 7.9.0

# Introduction
[OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br>
It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br>
It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>

### UML
UML Domain Model diagram you can find [here](https://api.openfintech.io/public_domain_model.png).<br>

### Persistence
Entities are updated not more than 1 time per day.<br>

### Terms and Conditions
This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br>
Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>

### Contacts
For any questions, please email - info@openfintech.io<br>
Or you can contact us at <a href=\"https://gitter.im/paymaxicom/openfintech.io\">Gitter</a><br>

Powered by [Paymaxi](https://www.paymaxi.com)

# Get Started

If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).

## Overview

The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br>
API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br>
JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br>
### Additional Request Headers
#### ACCEPT HEADER
Your requests should always include the header:
```curl
Accept: application/vnd.api+json
```

## Authentication

To use OpenFinTech API no needed authorization.

## Versioning

When we make changes to the API, we release new, dated versions. The current version is **2017-08-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.

## Pagination

OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br>
By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br>
The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br>
The `page[number]` parameter can be used to set needed page number.<br>
Example of response:
```json
{
  \"meta\": {
    \"total\": 419,
    \"pages\": 42
  },
  \"links\": {
    \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",
    \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",
    \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",
    \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"
  }
```

### Sorting

OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=code`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=code`] points to ascending sorting, negative  [e.g. `?sort=-code`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=code, -name, id`, etc.]
```curl
https://api.openfintech.io/v1/countries?sort=name,-area
```

### Filtering

Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description.
```curl
https://api.openfintech.io/v1/countries?filter[region]=europe
```

## Images

OpenFinTech provides two types of images: icons and logos. To get one of those types you should to use next url pattern:
``` curl
https://api.openfintech.io/v1/{path}/{id}/{icon/logo}
```
Also, images can be resized by adding next parameters: `h={height}&w={width}`. For example, you want to get organization icon with width equals to 20 pixels:
``` curl
https://api.openfintech.io/v1/organizations/{id}/icon?w=20&h=20
```
If argument height or width is missing API returns original image with real sizes.

## Errors

API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).

| Code | Description |
|------|-------------|
| 200 - OK | Everything worked as expected. |
| 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. |
| 401 - Unauthorized | No valid API key provided. |
| 402 - Request Failed | The parameters were valid but the request failed. |
| 404 - Not Found | The requested resource doesn't exist. |
| 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). |
| 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. |
| 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) |



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
  <version>2017-08-24</version>
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
     implementation "org.openapitools:openapi-java-client:2017-08-24"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-2017-08-24.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.BanksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    BanksApi apiInstance = new BanksApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterSortCode = "filterSortCode_example"; // String | Filtering by banks code.
    String filterCode = "filterCode_example"; // String | Filtering by code.
    Set<String> filterStatus = Arrays.asList(); // Set<String> | Filtration by status.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | sort_code | -sort_code | 
    try {
      BanksResponse result = apiInstance.banksGet(pageNumber, pageSize, filterSortCode, filterCode, filterStatus, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BanksApi#banksGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://api.openfintech.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BanksApi* | [**banksGet**](docs/BanksApi.md#banksGet) | **GET** /banks | List of banks
*BanksApi* | [**banksIdGet**](docs/BanksApi.md#banksIdGet) | **GET** /banks/{id} | Bank by ID
*CountriesApi* | [**countriesGet**](docs/CountriesApi.md#countriesGet) | **GET** /countries | List of countries
*CountriesApi* | [**countriesIdGet**](docs/CountriesApi.md#countriesIdGet) | **GET** /countries/{id} | Country by ID
*CurrenciesApi* | [**currenciesGet**](docs/CurrenciesApi.md#currenciesGet) | **GET** /currencies | List of currencies
*CurrenciesApi* | [**currenciesIdGet**](docs/CurrenciesApi.md#currenciesIdGet) | **GET** /currencies/{id} | Currency by ID
*DepositMethodsApi* | [**depositMethodsGet**](docs/DepositMethodsApi.md#depositMethodsGet) | **GET** /deposit-methods | List of deposit methods
*DepositMethodsApi* | [**depositMethodsIdGet**](docs/DepositMethodsApi.md#depositMethodsIdGet) | **GET** /deposit-methods/{id} | Deposit method by ID
*ExchangersApi* | [**exchangersGet**](docs/ExchangersApi.md#exchangersGet) | **GET** /exchangers | List of exchangers
*ExchangersApi* | [**exchangersIdGet**](docs/ExchangersApi.md#exchangersIdGet) | **GET** /exchangers/{id} | Exchanger by ID
*MerchantIndustriesApi* | [**merchantIndustriesGet**](docs/MerchantIndustriesApi.md#merchantIndustriesGet) | **GET** /merchant-industries | List of merchant industries
*MerchantIndustriesApi* | [**merchantIndustriesIdGet**](docs/MerchantIndustriesApi.md#merchantIndustriesIdGet) | **GET** /merchant-industries/{id} | Merchant industry by ID
*OrganizationsApi* | [**organizationsGet**](docs/OrganizationsApi.md#organizationsGet) | **GET** /organizations | List of organizations
*OrganizationsApi* | [**organizationsIdGet**](docs/OrganizationsApi.md#organizationsIdGet) | **GET** /organizations/{id} | Organization by ID
*PaymentMethodsApi* | [**paymentMethodsGet**](docs/PaymentMethodsApi.md#paymentMethodsGet) | **GET** /payment-methods | List of payment methods
*PaymentMethodsApi* | [**paymentMethodsIdGet**](docs/PaymentMethodsApi.md#paymentMethodsIdGet) | **GET** /payment-methods/{id} | Payment method by ID
*PaymentProvidersApi* | [**paymentProvidersGet**](docs/PaymentProvidersApi.md#paymentProvidersGet) | **GET** /payment-providers | List of payment providers
*PaymentProvidersApi* | [**paymentProvidersIdGet**](docs/PaymentProvidersApi.md#paymentProvidersIdGet) | **GET** /payment-providers/{id} | Payment provider by ID


## Documentation for Models

 - [ActiveInCountriesRelationship](docs/ActiveInCountriesRelationship.md)
 - [ActiveInCountriesRelationshipDataInner](docs/ActiveInCountriesRelationshipDataInner.md)
 - [ActiveInCountriesRelationshipLinks](docs/ActiveInCountriesRelationshipLinks.md)
 - [Bank](docs/Bank.md)
 - [BankAttributes](docs/BankAttributes.md)
 - [BankOrganization](docs/BankOrganization.md)
 - [BankOrganizationData](docs/BankOrganizationData.md)
 - [BankOrganizationLinks](docs/BankOrganizationLinks.md)
 - [BankRelationships](docs/BankRelationships.md)
 - [BankResponse](docs/BankResponse.md)
 - [BanksResponse](docs/BanksResponse.md)
 - [CountriesResponse](docs/CountriesResponse.md)
 - [Country](docs/Country.md)
 - [CountryAttributes](docs/CountryAttributes.md)
 - [CountryRelationships](docs/CountryRelationships.md)
 - [CountryResponse](docs/CountryResponse.md)
 - [CountryTranslations](docs/CountryTranslations.md)
 - [CountryTranslationsLinks](docs/CountryTranslationsLinks.md)
 - [CurrenciesResponse](docs/CurrenciesResponse.md)
 - [Currency](docs/Currency.md)
 - [CurrencyAttributes](docs/CurrencyAttributes.md)
 - [CurrencyAttributesIcon](docs/CurrencyAttributesIcon.md)
 - [CurrencyCountries](docs/CurrencyCountries.md)
 - [CurrencyCountryLinks](docs/CurrencyCountryLinks.md)
 - [CurrencyIssuer](docs/CurrencyIssuer.md)
 - [CurrencyIssuerLinks](docs/CurrencyIssuerLinks.md)
 - [CurrencyIssuerOrganization](docs/CurrencyIssuerOrganization.md)
 - [CurrencyIssuerOrganizationData](docs/CurrencyIssuerOrganizationData.md)
 - [CurrencyIssuerOrganizationLinks](docs/CurrencyIssuerOrganizationLinks.md)
 - [CurrencyIssuertData](docs/CurrencyIssuertData.md)
 - [CurrencyParent](docs/CurrencyParent.md)
 - [CurrencyParentData](docs/CurrencyParentData.md)
 - [CurrencyParentLinks](docs/CurrencyParentLinks.md)
 - [CurrencyRelationships](docs/CurrencyRelationships.md)
 - [CurrencyResponse](docs/CurrencyResponse.md)
 - [DepositMethod](docs/DepositMethod.md)
 - [DepositMethodAttributes](docs/DepositMethodAttributes.md)
 - [DepositMethodProcessorData](docs/DepositMethodProcessorData.md)
 - [DepositMethodProcessorDataDataInner](docs/DepositMethodProcessorDataDataInner.md)
 - [DepositMethodProcessorDataLinks](docs/DepositMethodProcessorDataLinks.md)
 - [DepositMethodRelationships](docs/DepositMethodRelationships.md)
 - [DepositMethodResponse](docs/DepositMethodResponse.md)
 - [DepositMethodsResponse](docs/DepositMethodsResponse.md)
 - [Exchanger](docs/Exchanger.md)
 - [ExchangerAttributes](docs/ExchangerAttributes.md)
 - [ExchangerOrganization](docs/ExchangerOrganization.md)
 - [ExchangerOrganizationData](docs/ExchangerOrganizationData.md)
 - [ExchangerOrganizationLinks](docs/ExchangerOrganizationLinks.md)
 - [ExchangerRelationships](docs/ExchangerRelationships.md)
 - [ExchangerResponse](docs/ExchangerResponse.md)
 - [ExchangersResponse](docs/ExchangersResponse.md)
 - [MerchantIndustriesResponse](docs/MerchantIndustriesResponse.md)
 - [MerchantIndustry](docs/MerchantIndustry.md)
 - [MerchantIndustryAttributes](docs/MerchantIndustryAttributes.md)
 - [MerchantIndustryResponse](docs/MerchantIndustryResponse.md)
 - [Organization](docs/Organization.md)
 - [OrganizationActive](docs/OrganizationActive.md)
 - [OrganizationActiveLinks](docs/OrganizationActiveLinks.md)
 - [OrganizationAddress](docs/OrganizationAddress.md)
 - [OrganizationAttributes](docs/OrganizationAttributes.md)
 - [OrganizationAttributesIcon](docs/OrganizationAttributesIcon.md)
 - [OrganizationAttributesLogo](docs/OrganizationAttributesLogo.md)
 - [OrganizationContacts](docs/OrganizationContacts.md)
 - [OrganizationHq](docs/OrganizationHq.md)
 - [OrganizationHqData](docs/OrganizationHqData.md)
 - [OrganizationHqLinks](docs/OrganizationHqLinks.md)
 - [OrganizationRelationships](docs/OrganizationRelationships.md)
 - [OrganizationResponse](docs/OrganizationResponse.md)
 - [OrganizationSocial](docs/OrganizationSocial.md)
 - [OrganizationSource](docs/OrganizationSource.md)
 - [OrganizationSourceData](docs/OrganizationSourceData.md)
 - [OrganizationSourceLinks](docs/OrganizationSourceLinks.md)
 - [OrganizationsResponse](docs/OrganizationsResponse.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentMethodAttributes](docs/PaymentMethodAttributes.md)
 - [PaymentMethodCurrencies](docs/PaymentMethodCurrencies.md)
 - [PaymentMethodCurrenciesLinks](docs/PaymentMethodCurrenciesLinks.md)
 - [PaymentMethodProcessor](docs/PaymentMethodProcessor.md)
 - [PaymentMethodProcessorData](docs/PaymentMethodProcessorData.md)
 - [PaymentMethodProcessorLinks](docs/PaymentMethodProcessorLinks.md)
 - [PaymentMethodRelationships](docs/PaymentMethodRelationships.md)
 - [PaymentMethodResponse](docs/PaymentMethodResponse.md)
 - [PaymentMethodsResponse](docs/PaymentMethodsResponse.md)
 - [PaymentProvider](docs/PaymentProvider.md)
 - [PaymentProviderAttributes](docs/PaymentProviderAttributes.md)
 - [PaymentProviderOrganization](docs/PaymentProviderOrganization.md)
 - [PaymentProviderOrganizationData](docs/PaymentProviderOrganizationData.md)
 - [PaymentProviderOrganizationLinks](docs/PaymentProviderOrganizationLinks.md)
 - [PaymentProviderPaymentMethods](docs/PaymentProviderPaymentMethods.md)
 - [PaymentProviderPaymentMethodsLinks](docs/PaymentProviderPaymentMethodsLinks.md)
 - [PaymentProviderRelationships](docs/PaymentProviderRelationships.md)
 - [PaymentProviderResponse](docs/PaymentProviderResponse.md)
 - [PaymentProvidersResponse](docs/PaymentProvidersResponse.md)
 - [ResponseLinks](docs/ResponseLinks.md)
 - [ResponseMeta](docs/ResponseMeta.md)
 - [SelfLinks](docs/SelfLinks.md)
 - [SupportedPspsRelationship](docs/SupportedPspsRelationship.md)
 - [SupportedPspsRelationshipDataInner](docs/SupportedPspsRelationshipDataInner.md)
 - [SupportedPspsRelationshipLinks](docs/SupportedPspsRelationshipLinks.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization

Endpoints do not require authorization.


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



