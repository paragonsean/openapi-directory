# open_fin_tech_io

OpenFinTechIo - JavaScript client for open_fin_tech_io
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

This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2017-08-24
- Package version: 2017-08-24
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install open_fin_tech_io --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your open_fin_tech_io from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var OpenFinTechIo = require('open_fin_tech_io');


var api = new OpenFinTechIo.BanksApi()
var opts = {
  'pageNumber': 56, // {Number} Current page number.
  'pageSize': 56, // {Number} Page size.<br>*Default value: 100* 
  'filterSortCode': "filterSortCode_example", // {String} Filtering by banks code.
  'filterCode': "filterCode_example", // {String} Filtering by code.
  'filterStatus': ["null"], // {[String]} Filtration by status.
  'sort': ["null"] // {[String]} Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | sort_code | -sort_code | 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.banksGet(opts, callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.openfintech.io/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OpenFinTechIo.BanksApi* | [**banksGet**](docs/BanksApi.md#banksGet) | **GET** /banks | List of banks
*OpenFinTechIo.BanksApi* | [**banksIdGet**](docs/BanksApi.md#banksIdGet) | **GET** /banks/{id} | Bank by ID
*OpenFinTechIo.CountriesApi* | [**countriesGet**](docs/CountriesApi.md#countriesGet) | **GET** /countries | List of countries
*OpenFinTechIo.CountriesApi* | [**countriesIdGet**](docs/CountriesApi.md#countriesIdGet) | **GET** /countries/{id} | Country by ID
*OpenFinTechIo.CurrenciesApi* | [**currenciesGet**](docs/CurrenciesApi.md#currenciesGet) | **GET** /currencies | List of currencies
*OpenFinTechIo.CurrenciesApi* | [**currenciesIdGet**](docs/CurrenciesApi.md#currenciesIdGet) | **GET** /currencies/{id} | Currency by ID
*OpenFinTechIo.DepositMethodsApi* | [**depositMethodsGet**](docs/DepositMethodsApi.md#depositMethodsGet) | **GET** /deposit-methods | List of deposit methods
*OpenFinTechIo.DepositMethodsApi* | [**depositMethodsIdGet**](docs/DepositMethodsApi.md#depositMethodsIdGet) | **GET** /deposit-methods/{id} | Deposit method by ID
*OpenFinTechIo.ExchangersApi* | [**exchangersGet**](docs/ExchangersApi.md#exchangersGet) | **GET** /exchangers | List of exchangers
*OpenFinTechIo.ExchangersApi* | [**exchangersIdGet**](docs/ExchangersApi.md#exchangersIdGet) | **GET** /exchangers/{id} | Exchanger by ID
*OpenFinTechIo.MerchantIndustriesApi* | [**merchantIndustriesGet**](docs/MerchantIndustriesApi.md#merchantIndustriesGet) | **GET** /merchant-industries | List of merchant industries
*OpenFinTechIo.MerchantIndustriesApi* | [**merchantIndustriesIdGet**](docs/MerchantIndustriesApi.md#merchantIndustriesIdGet) | **GET** /merchant-industries/{id} | Merchant industry by ID
*OpenFinTechIo.OrganizationsApi* | [**organizationsGet**](docs/OrganizationsApi.md#organizationsGet) | **GET** /organizations | List of organizations
*OpenFinTechIo.OrganizationsApi* | [**organizationsIdGet**](docs/OrganizationsApi.md#organizationsIdGet) | **GET** /organizations/{id} | Organization by ID
*OpenFinTechIo.PaymentMethodsApi* | [**paymentMethodsGet**](docs/PaymentMethodsApi.md#paymentMethodsGet) | **GET** /payment-methods | List of payment methods
*OpenFinTechIo.PaymentMethodsApi* | [**paymentMethodsIdGet**](docs/PaymentMethodsApi.md#paymentMethodsIdGet) | **GET** /payment-methods/{id} | Payment method by ID
*OpenFinTechIo.PaymentProvidersApi* | [**paymentProvidersGet**](docs/PaymentProvidersApi.md#paymentProvidersGet) | **GET** /payment-providers | List of payment providers
*OpenFinTechIo.PaymentProvidersApi* | [**paymentProvidersIdGet**](docs/PaymentProvidersApi.md#paymentProvidersIdGet) | **GET** /payment-providers/{id} | Payment provider by ID


## Documentation for Models

 - [OpenFinTechIo.ActiveInCountriesRelationship](docs/ActiveInCountriesRelationship.md)
 - [OpenFinTechIo.ActiveInCountriesRelationshipDataInner](docs/ActiveInCountriesRelationshipDataInner.md)
 - [OpenFinTechIo.ActiveInCountriesRelationshipLinks](docs/ActiveInCountriesRelationshipLinks.md)
 - [OpenFinTechIo.Bank](docs/Bank.md)
 - [OpenFinTechIo.BankAttributes](docs/BankAttributes.md)
 - [OpenFinTechIo.BankOrganization](docs/BankOrganization.md)
 - [OpenFinTechIo.BankOrganizationData](docs/BankOrganizationData.md)
 - [OpenFinTechIo.BankOrganizationLinks](docs/BankOrganizationLinks.md)
 - [OpenFinTechIo.BankRelationships](docs/BankRelationships.md)
 - [OpenFinTechIo.BankResponse](docs/BankResponse.md)
 - [OpenFinTechIo.BanksResponse](docs/BanksResponse.md)
 - [OpenFinTechIo.CountriesResponse](docs/CountriesResponse.md)
 - [OpenFinTechIo.Country](docs/Country.md)
 - [OpenFinTechIo.CountryAttributes](docs/CountryAttributes.md)
 - [OpenFinTechIo.CountryRelationships](docs/CountryRelationships.md)
 - [OpenFinTechIo.CountryResponse](docs/CountryResponse.md)
 - [OpenFinTechIo.CountryTranslations](docs/CountryTranslations.md)
 - [OpenFinTechIo.CountryTranslationsLinks](docs/CountryTranslationsLinks.md)
 - [OpenFinTechIo.CurrenciesResponse](docs/CurrenciesResponse.md)
 - [OpenFinTechIo.Currency](docs/Currency.md)
 - [OpenFinTechIo.CurrencyAttributes](docs/CurrencyAttributes.md)
 - [OpenFinTechIo.CurrencyAttributesIcon](docs/CurrencyAttributesIcon.md)
 - [OpenFinTechIo.CurrencyCountries](docs/CurrencyCountries.md)
 - [OpenFinTechIo.CurrencyCountryLinks](docs/CurrencyCountryLinks.md)
 - [OpenFinTechIo.CurrencyIssuer](docs/CurrencyIssuer.md)
 - [OpenFinTechIo.CurrencyIssuerLinks](docs/CurrencyIssuerLinks.md)
 - [OpenFinTechIo.CurrencyIssuerOrganization](docs/CurrencyIssuerOrganization.md)
 - [OpenFinTechIo.CurrencyIssuerOrganizationData](docs/CurrencyIssuerOrganizationData.md)
 - [OpenFinTechIo.CurrencyIssuerOrganizationLinks](docs/CurrencyIssuerOrganizationLinks.md)
 - [OpenFinTechIo.CurrencyIssuertData](docs/CurrencyIssuertData.md)
 - [OpenFinTechIo.CurrencyParent](docs/CurrencyParent.md)
 - [OpenFinTechIo.CurrencyParentData](docs/CurrencyParentData.md)
 - [OpenFinTechIo.CurrencyParentLinks](docs/CurrencyParentLinks.md)
 - [OpenFinTechIo.CurrencyRelationships](docs/CurrencyRelationships.md)
 - [OpenFinTechIo.CurrencyResponse](docs/CurrencyResponse.md)
 - [OpenFinTechIo.DepositMethod](docs/DepositMethod.md)
 - [OpenFinTechIo.DepositMethodAttributes](docs/DepositMethodAttributes.md)
 - [OpenFinTechIo.DepositMethodProcessorData](docs/DepositMethodProcessorData.md)
 - [OpenFinTechIo.DepositMethodProcessorDataDataInner](docs/DepositMethodProcessorDataDataInner.md)
 - [OpenFinTechIo.DepositMethodProcessorDataLinks](docs/DepositMethodProcessorDataLinks.md)
 - [OpenFinTechIo.DepositMethodRelationships](docs/DepositMethodRelationships.md)
 - [OpenFinTechIo.DepositMethodResponse](docs/DepositMethodResponse.md)
 - [OpenFinTechIo.DepositMethodsResponse](docs/DepositMethodsResponse.md)
 - [OpenFinTechIo.Exchanger](docs/Exchanger.md)
 - [OpenFinTechIo.ExchangerAttributes](docs/ExchangerAttributes.md)
 - [OpenFinTechIo.ExchangerOrganization](docs/ExchangerOrganization.md)
 - [OpenFinTechIo.ExchangerOrganizationData](docs/ExchangerOrganizationData.md)
 - [OpenFinTechIo.ExchangerOrganizationLinks](docs/ExchangerOrganizationLinks.md)
 - [OpenFinTechIo.ExchangerRelationships](docs/ExchangerRelationships.md)
 - [OpenFinTechIo.ExchangerResponse](docs/ExchangerResponse.md)
 - [OpenFinTechIo.ExchangersResponse](docs/ExchangersResponse.md)
 - [OpenFinTechIo.MerchantIndustriesResponse](docs/MerchantIndustriesResponse.md)
 - [OpenFinTechIo.MerchantIndustry](docs/MerchantIndustry.md)
 - [OpenFinTechIo.MerchantIndustryAttributes](docs/MerchantIndustryAttributes.md)
 - [OpenFinTechIo.MerchantIndustryResponse](docs/MerchantIndustryResponse.md)
 - [OpenFinTechIo.Organization](docs/Organization.md)
 - [OpenFinTechIo.OrganizationActive](docs/OrganizationActive.md)
 - [OpenFinTechIo.OrganizationActiveLinks](docs/OrganizationActiveLinks.md)
 - [OpenFinTechIo.OrganizationAddress](docs/OrganizationAddress.md)
 - [OpenFinTechIo.OrganizationAttributes](docs/OrganizationAttributes.md)
 - [OpenFinTechIo.OrganizationAttributesIcon](docs/OrganizationAttributesIcon.md)
 - [OpenFinTechIo.OrganizationAttributesLogo](docs/OrganizationAttributesLogo.md)
 - [OpenFinTechIo.OrganizationContacts](docs/OrganizationContacts.md)
 - [OpenFinTechIo.OrganizationHq](docs/OrganizationHq.md)
 - [OpenFinTechIo.OrganizationHqData](docs/OrganizationHqData.md)
 - [OpenFinTechIo.OrganizationHqLinks](docs/OrganizationHqLinks.md)
 - [OpenFinTechIo.OrganizationRelationships](docs/OrganizationRelationships.md)
 - [OpenFinTechIo.OrganizationResponse](docs/OrganizationResponse.md)
 - [OpenFinTechIo.OrganizationSocial](docs/OrganizationSocial.md)
 - [OpenFinTechIo.OrganizationSource](docs/OrganizationSource.md)
 - [OpenFinTechIo.OrganizationSourceData](docs/OrganizationSourceData.md)
 - [OpenFinTechIo.OrganizationSourceLinks](docs/OrganizationSourceLinks.md)
 - [OpenFinTechIo.OrganizationsResponse](docs/OrganizationsResponse.md)
 - [OpenFinTechIo.PaymentMethod](docs/PaymentMethod.md)
 - [OpenFinTechIo.PaymentMethodAttributes](docs/PaymentMethodAttributes.md)
 - [OpenFinTechIo.PaymentMethodCurrencies](docs/PaymentMethodCurrencies.md)
 - [OpenFinTechIo.PaymentMethodCurrenciesLinks](docs/PaymentMethodCurrenciesLinks.md)
 - [OpenFinTechIo.PaymentMethodProcessor](docs/PaymentMethodProcessor.md)
 - [OpenFinTechIo.PaymentMethodProcessorData](docs/PaymentMethodProcessorData.md)
 - [OpenFinTechIo.PaymentMethodProcessorLinks](docs/PaymentMethodProcessorLinks.md)
 - [OpenFinTechIo.PaymentMethodRelationships](docs/PaymentMethodRelationships.md)
 - [OpenFinTechIo.PaymentMethodResponse](docs/PaymentMethodResponse.md)
 - [OpenFinTechIo.PaymentMethodsResponse](docs/PaymentMethodsResponse.md)
 - [OpenFinTechIo.PaymentProvider](docs/PaymentProvider.md)
 - [OpenFinTechIo.PaymentProviderAttributes](docs/PaymentProviderAttributes.md)
 - [OpenFinTechIo.PaymentProviderOrganization](docs/PaymentProviderOrganization.md)
 - [OpenFinTechIo.PaymentProviderOrganizationData](docs/PaymentProviderOrganizationData.md)
 - [OpenFinTechIo.PaymentProviderOrganizationLinks](docs/PaymentProviderOrganizationLinks.md)
 - [OpenFinTechIo.PaymentProviderPaymentMethods](docs/PaymentProviderPaymentMethods.md)
 - [OpenFinTechIo.PaymentProviderPaymentMethodsLinks](docs/PaymentProviderPaymentMethodsLinks.md)
 - [OpenFinTechIo.PaymentProviderRelationships](docs/PaymentProviderRelationships.md)
 - [OpenFinTechIo.PaymentProviderResponse](docs/PaymentProviderResponse.md)
 - [OpenFinTechIo.PaymentProvidersResponse](docs/PaymentProvidersResponse.md)
 - [OpenFinTechIo.ResponseLinks](docs/ResponseLinks.md)
 - [OpenFinTechIo.ResponseMeta](docs/ResponseMeta.md)
 - [OpenFinTechIo.SelfLinks](docs/SelfLinks.md)
 - [OpenFinTechIo.SupportedPspsRelationship](docs/SupportedPspsRelationship.md)
 - [OpenFinTechIo.SupportedPspsRelationshipDataInner](docs/SupportedPspsRelationshipDataInner.md)
 - [OpenFinTechIo.SupportedPspsRelationshipLinks](docs/SupportedPspsRelationshipLinks.md)


## Documentation for Authorization

Endpoints do not require authorization.

