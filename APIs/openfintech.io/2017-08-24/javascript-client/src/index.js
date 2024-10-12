/**
 * OpenFinTech.io
 * # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://api.openfintech.io/public_domain_model.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io<br> Or you can contact us at <a href=\"https://gitter.im/paymaxicom/openfintech.io\">Gitter</a><br>  Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-08-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Example of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=code`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=code`] points to ascending sorting, negative  [e.g. `?sort=-code`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=code, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Images  OpenFinTech provides two types of images: icons and logos. To get one of those types you should to use next url pattern: ``` curl https://api.openfintech.io/v1/{path}/{id}/{icon/logo} ``` Also, images can be resized by adding next parameters: `h={height}&w={width}`. For example, you want to get organization icon with width equals to 20 pixels: ``` curl https://api.openfintech.io/v1/organizations/{id}/icon?w=20&h=20 ``` If argument height or width is missing API returns original image with real sizes.  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 
 *
 * The version of the OpenAPI document: 2017-08-24
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ActiveInCountriesRelationship from './model/ActiveInCountriesRelationship';
import ActiveInCountriesRelationshipDataInner from './model/ActiveInCountriesRelationshipDataInner';
import ActiveInCountriesRelationshipLinks from './model/ActiveInCountriesRelationshipLinks';
import Bank from './model/Bank';
import BankAttributes from './model/BankAttributes';
import BankOrganization from './model/BankOrganization';
import BankOrganizationData from './model/BankOrganizationData';
import BankOrganizationLinks from './model/BankOrganizationLinks';
import BankRelationships from './model/BankRelationships';
import BankResponse from './model/BankResponse';
import BanksResponse from './model/BanksResponse';
import CountriesResponse from './model/CountriesResponse';
import Country from './model/Country';
import CountryAttributes from './model/CountryAttributes';
import CountryRelationships from './model/CountryRelationships';
import CountryResponse from './model/CountryResponse';
import CountryTranslations from './model/CountryTranslations';
import CountryTranslationsLinks from './model/CountryTranslationsLinks';
import CurrenciesResponse from './model/CurrenciesResponse';
import Currency from './model/Currency';
import CurrencyAttributes from './model/CurrencyAttributes';
import CurrencyAttributesIcon from './model/CurrencyAttributesIcon';
import CurrencyCountries from './model/CurrencyCountries';
import CurrencyCountryLinks from './model/CurrencyCountryLinks';
import CurrencyIssuer from './model/CurrencyIssuer';
import CurrencyIssuerLinks from './model/CurrencyIssuerLinks';
import CurrencyIssuerOrganization from './model/CurrencyIssuerOrganization';
import CurrencyIssuerOrganizationData from './model/CurrencyIssuerOrganizationData';
import CurrencyIssuerOrganizationLinks from './model/CurrencyIssuerOrganizationLinks';
import CurrencyIssuertData from './model/CurrencyIssuertData';
import CurrencyParent from './model/CurrencyParent';
import CurrencyParentData from './model/CurrencyParentData';
import CurrencyParentLinks from './model/CurrencyParentLinks';
import CurrencyRelationships from './model/CurrencyRelationships';
import CurrencyResponse from './model/CurrencyResponse';
import DepositMethod from './model/DepositMethod';
import DepositMethodAttributes from './model/DepositMethodAttributes';
import DepositMethodProcessorData from './model/DepositMethodProcessorData';
import DepositMethodProcessorDataDataInner from './model/DepositMethodProcessorDataDataInner';
import DepositMethodProcessorDataLinks from './model/DepositMethodProcessorDataLinks';
import DepositMethodRelationships from './model/DepositMethodRelationships';
import DepositMethodResponse from './model/DepositMethodResponse';
import DepositMethodsResponse from './model/DepositMethodsResponse';
import Exchanger from './model/Exchanger';
import ExchangerAttributes from './model/ExchangerAttributes';
import ExchangerOrganization from './model/ExchangerOrganization';
import ExchangerOrganizationData from './model/ExchangerOrganizationData';
import ExchangerOrganizationLinks from './model/ExchangerOrganizationLinks';
import ExchangerRelationships from './model/ExchangerRelationships';
import ExchangerResponse from './model/ExchangerResponse';
import ExchangersResponse from './model/ExchangersResponse';
import MerchantIndustriesResponse from './model/MerchantIndustriesResponse';
import MerchantIndustry from './model/MerchantIndustry';
import MerchantIndustryAttributes from './model/MerchantIndustryAttributes';
import MerchantIndustryResponse from './model/MerchantIndustryResponse';
import Organization from './model/Organization';
import OrganizationActive from './model/OrganizationActive';
import OrganizationActiveLinks from './model/OrganizationActiveLinks';
import OrganizationAddress from './model/OrganizationAddress';
import OrganizationAttributes from './model/OrganizationAttributes';
import OrganizationAttributesIcon from './model/OrganizationAttributesIcon';
import OrganizationAttributesLogo from './model/OrganizationAttributesLogo';
import OrganizationContacts from './model/OrganizationContacts';
import OrganizationHq from './model/OrganizationHq';
import OrganizationHqData from './model/OrganizationHqData';
import OrganizationHqLinks from './model/OrganizationHqLinks';
import OrganizationRelationships from './model/OrganizationRelationships';
import OrganizationResponse from './model/OrganizationResponse';
import OrganizationSocial from './model/OrganizationSocial';
import OrganizationSource from './model/OrganizationSource';
import OrganizationSourceData from './model/OrganizationSourceData';
import OrganizationSourceLinks from './model/OrganizationSourceLinks';
import OrganizationsResponse from './model/OrganizationsResponse';
import PaymentMethod from './model/PaymentMethod';
import PaymentMethodAttributes from './model/PaymentMethodAttributes';
import PaymentMethodCurrencies from './model/PaymentMethodCurrencies';
import PaymentMethodCurrenciesLinks from './model/PaymentMethodCurrenciesLinks';
import PaymentMethodProcessor from './model/PaymentMethodProcessor';
import PaymentMethodProcessorData from './model/PaymentMethodProcessorData';
import PaymentMethodProcessorLinks from './model/PaymentMethodProcessorLinks';
import PaymentMethodRelationships from './model/PaymentMethodRelationships';
import PaymentMethodResponse from './model/PaymentMethodResponse';
import PaymentMethodsResponse from './model/PaymentMethodsResponse';
import PaymentProvider from './model/PaymentProvider';
import PaymentProviderAttributes from './model/PaymentProviderAttributes';
import PaymentProviderOrganization from './model/PaymentProviderOrganization';
import PaymentProviderOrganizationData from './model/PaymentProviderOrganizationData';
import PaymentProviderOrganizationLinks from './model/PaymentProviderOrganizationLinks';
import PaymentProviderPaymentMethods from './model/PaymentProviderPaymentMethods';
import PaymentProviderPaymentMethodsLinks from './model/PaymentProviderPaymentMethodsLinks';
import PaymentProviderRelationships from './model/PaymentProviderRelationships';
import PaymentProviderResponse from './model/PaymentProviderResponse';
import PaymentProvidersResponse from './model/PaymentProvidersResponse';
import ResponseLinks from './model/ResponseLinks';
import ResponseMeta from './model/ResponseMeta';
import SelfLinks from './model/SelfLinks';
import SupportedPspsRelationship from './model/SupportedPspsRelationship';
import SupportedPspsRelationshipDataInner from './model/SupportedPspsRelationshipDataInner';
import SupportedPspsRelationshipLinks from './model/SupportedPspsRelationshipLinks';
import BanksApi from './api/BanksApi';
import CountriesApi from './api/CountriesApi';
import CurrenciesApi from './api/CurrenciesApi';
import DepositMethodsApi from './api/DepositMethodsApi';
import ExchangersApi from './api/ExchangersApi';
import MerchantIndustriesApi from './api/MerchantIndustriesApi';
import OrganizationsApi from './api/OrganizationsApi';
import PaymentMethodsApi from './api/PaymentMethodsApi';
import PaymentProvidersApi from './api/PaymentProvidersApi';


/**
* # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.&lt;br&gt; It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.&lt;br&gt; It is created for communication of cross-integrated micro-services on \&quot;one language\&quot;. This is achieved through standardization of entity identifiers that are used to exchange information among different services.&lt;br&gt;  ### UML UML Domain Model diagram you can find [here](https://api.openfintech.io/public_domain_model.png).&lt;br&gt;  ### Persistence Entities are updated not more than 1 time per day.&lt;br&gt;  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).&lt;br&gt; Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).&lt;br&gt;  ### Contacts For any questions, please email - info@openfintech.io&lt;br&gt; Or you can contact us at &lt;a href&#x3D;\&quot;https://gitter.im/paymaxicom/openfintech.io\&quot;&gt;Gitter&lt;/a&gt;&lt;br&gt;  Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger&#x60;s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.&lt;br&gt; API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.&lt;br&gt; JSON API requires use of the JSON API media type (&#x60;application/vnd.api+json&#x60;) for exchanging data.&lt;br&gt; ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: &#x60;&#x60;&#x60;curl Accept: application/vnd.api+json &#x60;&#x60;&#x60;  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-08-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name &#x60;meta&#x60; - contains information about listed objects [&#x60;total&#x60; - contains information about total count of listed objects, &#x60;pages&#x60; - count of pages], &#x60;links&#x60; - contain links to navigate between pages [&#x60;first&#x60; - link to first page, &#x60;prev&#x60; - link to previous page, &#x60;next&#x60; - link to next page, &#x60;last&#x60; - link to last page].&lt;br&gt; By default first page will be listed. For navigating through pages, use the page parameter (e.g. &#x60;page[number]&#x60;, &#x60;page[size]&#x60;).&lt;br&gt; The &#x60;page[size]&#x60; parameter can be used to set the number of records that you want to receive in the response.&lt;br&gt; The &#x60;page[number]&#x60; parameter can be used to set needed page number.&lt;br&gt; Example of response: &#x60;&#x60;&#x60;json {   \&quot;meta\&quot;: {     \&quot;total\&quot;: 419,     \&quot;pages\&quot;: 42   },   \&quot;links\&quot;: {     \&quot;first\&quot;: \&quot;/v1/{path}?page[number]&#x3D;1&amp;page[size]&#x3D;10\&quot;,     \&quot;prev\&quot;: \&quot;/v1/{path}?page[number]&#x3D;39&amp;page[size]&#x3D;10\&quot;,     \&quot;next\&quot;: \&quot;/v1/{path}?page[number]&#x3D;41&amp;page[size]&#x3D;10\&quot;,     \&quot;last\&quot;: \&quot;/v1/{path}?page[number]&#x3D;42&amp;page[size]&#x3D;10\&quot;   } &#x60;&#x60;&#x60;  ### Sorting  OpenFinTech\\&#x60;s API supported query parameter to sort result collection [e.g. &#x60;?sort&#x3D;code&#x60;]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. &#x60;?sort&#x3D;code&#x60;] points to ascending sorting, negative  [e.g. &#x60;?sort&#x3D;-code&#x60;] - to descending sorting. Also, supported multiple sorting parameters [e.g. &#x60;?sort&#x3D;code, -name, id&#x60;, etc.] &#x60;&#x60;&#x60;curl https://api.openfintech.io/v1/countries?sort&#x3D;name,-area &#x60;&#x60;&#x60;  ### Filtering  Filtering provided by unique query key &#x60;filter[*filtering_condition*]&#x60;. Information about available parameters may be found in the endpoint description. &#x60;&#x60;&#x60;curl https://api.openfintech.io/v1/countries?filter[region]&#x3D;europe &#x60;&#x60;&#x60;  ## Images  OpenFinTech provides two types of images: icons and logos. To get one of those types you should to use next url pattern: &#x60;&#x60;&#x60; curl https://api.openfintech.io/v1/{path}/{id}/{icon/logo} &#x60;&#x60;&#x60; Also, images can be resized by adding next parameters: &#x60;h&#x3D;{height}&amp;w&#x3D;{width}&#x60;. For example, you want to get organization icon with width equals to 20 pixels: &#x60;&#x60;&#x60; curl https://api.openfintech.io/v1/organizations/{id}/icon?w&#x3D;20&amp;h&#x3D;20 &#x60;&#x60;&#x60; If argument height or width is missing API returns original image with real sizes.  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the &#x60;2xx&#x60; range indicate success, codes in the &#x60;4xx&#x60; range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the &#x60;5xx&#x60; range indicate an error with OpenFinTech&#39;s servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn&#39;t exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech&#39;s end. (These are rare.) | .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var OpenFinTechIo = require('index'); // See note below*.
* var xxxSvc = new OpenFinTechIo.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new OpenFinTechIo.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new OpenFinTechIo.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new OpenFinTechIo.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2017-08-24
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ActiveInCountriesRelationship model constructor.
     * @property {module:model/ActiveInCountriesRelationship}
     */
    ActiveInCountriesRelationship,

    /**
     * The ActiveInCountriesRelationshipDataInner model constructor.
     * @property {module:model/ActiveInCountriesRelationshipDataInner}
     */
    ActiveInCountriesRelationshipDataInner,

    /**
     * The ActiveInCountriesRelationshipLinks model constructor.
     * @property {module:model/ActiveInCountriesRelationshipLinks}
     */
    ActiveInCountriesRelationshipLinks,

    /**
     * The Bank model constructor.
     * @property {module:model/Bank}
     */
    Bank,

    /**
     * The BankAttributes model constructor.
     * @property {module:model/BankAttributes}
     */
    BankAttributes,

    /**
     * The BankOrganization model constructor.
     * @property {module:model/BankOrganization}
     */
    BankOrganization,

    /**
     * The BankOrganizationData model constructor.
     * @property {module:model/BankOrganizationData}
     */
    BankOrganizationData,

    /**
     * The BankOrganizationLinks model constructor.
     * @property {module:model/BankOrganizationLinks}
     */
    BankOrganizationLinks,

    /**
     * The BankRelationships model constructor.
     * @property {module:model/BankRelationships}
     */
    BankRelationships,

    /**
     * The BankResponse model constructor.
     * @property {module:model/BankResponse}
     */
    BankResponse,

    /**
     * The BanksResponse model constructor.
     * @property {module:model/BanksResponse}
     */
    BanksResponse,

    /**
     * The CountriesResponse model constructor.
     * @property {module:model/CountriesResponse}
     */
    CountriesResponse,

    /**
     * The Country model constructor.
     * @property {module:model/Country}
     */
    Country,

    /**
     * The CountryAttributes model constructor.
     * @property {module:model/CountryAttributes}
     */
    CountryAttributes,

    /**
     * The CountryRelationships model constructor.
     * @property {module:model/CountryRelationships}
     */
    CountryRelationships,

    /**
     * The CountryResponse model constructor.
     * @property {module:model/CountryResponse}
     */
    CountryResponse,

    /**
     * The CountryTranslations model constructor.
     * @property {module:model/CountryTranslations}
     */
    CountryTranslations,

    /**
     * The CountryTranslationsLinks model constructor.
     * @property {module:model/CountryTranslationsLinks}
     */
    CountryTranslationsLinks,

    /**
     * The CurrenciesResponse model constructor.
     * @property {module:model/CurrenciesResponse}
     */
    CurrenciesResponse,

    /**
     * The Currency model constructor.
     * @property {module:model/Currency}
     */
    Currency,

    /**
     * The CurrencyAttributes model constructor.
     * @property {module:model/CurrencyAttributes}
     */
    CurrencyAttributes,

    /**
     * The CurrencyAttributesIcon model constructor.
     * @property {module:model/CurrencyAttributesIcon}
     */
    CurrencyAttributesIcon,

    /**
     * The CurrencyCountries model constructor.
     * @property {module:model/CurrencyCountries}
     */
    CurrencyCountries,

    /**
     * The CurrencyCountryLinks model constructor.
     * @property {module:model/CurrencyCountryLinks}
     */
    CurrencyCountryLinks,

    /**
     * The CurrencyIssuer model constructor.
     * @property {module:model/CurrencyIssuer}
     */
    CurrencyIssuer,

    /**
     * The CurrencyIssuerLinks model constructor.
     * @property {module:model/CurrencyIssuerLinks}
     */
    CurrencyIssuerLinks,

    /**
     * The CurrencyIssuerOrganization model constructor.
     * @property {module:model/CurrencyIssuerOrganization}
     */
    CurrencyIssuerOrganization,

    /**
     * The CurrencyIssuerOrganizationData model constructor.
     * @property {module:model/CurrencyIssuerOrganizationData}
     */
    CurrencyIssuerOrganizationData,

    /**
     * The CurrencyIssuerOrganizationLinks model constructor.
     * @property {module:model/CurrencyIssuerOrganizationLinks}
     */
    CurrencyIssuerOrganizationLinks,

    /**
     * The CurrencyIssuertData model constructor.
     * @property {module:model/CurrencyIssuertData}
     */
    CurrencyIssuertData,

    /**
     * The CurrencyParent model constructor.
     * @property {module:model/CurrencyParent}
     */
    CurrencyParent,

    /**
     * The CurrencyParentData model constructor.
     * @property {module:model/CurrencyParentData}
     */
    CurrencyParentData,

    /**
     * The CurrencyParentLinks model constructor.
     * @property {module:model/CurrencyParentLinks}
     */
    CurrencyParentLinks,

    /**
     * The CurrencyRelationships model constructor.
     * @property {module:model/CurrencyRelationships}
     */
    CurrencyRelationships,

    /**
     * The CurrencyResponse model constructor.
     * @property {module:model/CurrencyResponse}
     */
    CurrencyResponse,

    /**
     * The DepositMethod model constructor.
     * @property {module:model/DepositMethod}
     */
    DepositMethod,

    /**
     * The DepositMethodAttributes model constructor.
     * @property {module:model/DepositMethodAttributes}
     */
    DepositMethodAttributes,

    /**
     * The DepositMethodProcessorData model constructor.
     * @property {module:model/DepositMethodProcessorData}
     */
    DepositMethodProcessorData,

    /**
     * The DepositMethodProcessorDataDataInner model constructor.
     * @property {module:model/DepositMethodProcessorDataDataInner}
     */
    DepositMethodProcessorDataDataInner,

    /**
     * The DepositMethodProcessorDataLinks model constructor.
     * @property {module:model/DepositMethodProcessorDataLinks}
     */
    DepositMethodProcessorDataLinks,

    /**
     * The DepositMethodRelationships model constructor.
     * @property {module:model/DepositMethodRelationships}
     */
    DepositMethodRelationships,

    /**
     * The DepositMethodResponse model constructor.
     * @property {module:model/DepositMethodResponse}
     */
    DepositMethodResponse,

    /**
     * The DepositMethodsResponse model constructor.
     * @property {module:model/DepositMethodsResponse}
     */
    DepositMethodsResponse,

    /**
     * The Exchanger model constructor.
     * @property {module:model/Exchanger}
     */
    Exchanger,

    /**
     * The ExchangerAttributes model constructor.
     * @property {module:model/ExchangerAttributes}
     */
    ExchangerAttributes,

    /**
     * The ExchangerOrganization model constructor.
     * @property {module:model/ExchangerOrganization}
     */
    ExchangerOrganization,

    /**
     * The ExchangerOrganizationData model constructor.
     * @property {module:model/ExchangerOrganizationData}
     */
    ExchangerOrganizationData,

    /**
     * The ExchangerOrganizationLinks model constructor.
     * @property {module:model/ExchangerOrganizationLinks}
     */
    ExchangerOrganizationLinks,

    /**
     * The ExchangerRelationships model constructor.
     * @property {module:model/ExchangerRelationships}
     */
    ExchangerRelationships,

    /**
     * The ExchangerResponse model constructor.
     * @property {module:model/ExchangerResponse}
     */
    ExchangerResponse,

    /**
     * The ExchangersResponse model constructor.
     * @property {module:model/ExchangersResponse}
     */
    ExchangersResponse,

    /**
     * The MerchantIndustriesResponse model constructor.
     * @property {module:model/MerchantIndustriesResponse}
     */
    MerchantIndustriesResponse,

    /**
     * The MerchantIndustry model constructor.
     * @property {module:model/MerchantIndustry}
     */
    MerchantIndustry,

    /**
     * The MerchantIndustryAttributes model constructor.
     * @property {module:model/MerchantIndustryAttributes}
     */
    MerchantIndustryAttributes,

    /**
     * The MerchantIndustryResponse model constructor.
     * @property {module:model/MerchantIndustryResponse}
     */
    MerchantIndustryResponse,

    /**
     * The Organization model constructor.
     * @property {module:model/Organization}
     */
    Organization,

    /**
     * The OrganizationActive model constructor.
     * @property {module:model/OrganizationActive}
     */
    OrganizationActive,

    /**
     * The OrganizationActiveLinks model constructor.
     * @property {module:model/OrganizationActiveLinks}
     */
    OrganizationActiveLinks,

    /**
     * The OrganizationAddress model constructor.
     * @property {module:model/OrganizationAddress}
     */
    OrganizationAddress,

    /**
     * The OrganizationAttributes model constructor.
     * @property {module:model/OrganizationAttributes}
     */
    OrganizationAttributes,

    /**
     * The OrganizationAttributesIcon model constructor.
     * @property {module:model/OrganizationAttributesIcon}
     */
    OrganizationAttributesIcon,

    /**
     * The OrganizationAttributesLogo model constructor.
     * @property {module:model/OrganizationAttributesLogo}
     */
    OrganizationAttributesLogo,

    /**
     * The OrganizationContacts model constructor.
     * @property {module:model/OrganizationContacts}
     */
    OrganizationContacts,

    /**
     * The OrganizationHq model constructor.
     * @property {module:model/OrganizationHq}
     */
    OrganizationHq,

    /**
     * The OrganizationHqData model constructor.
     * @property {module:model/OrganizationHqData}
     */
    OrganizationHqData,

    /**
     * The OrganizationHqLinks model constructor.
     * @property {module:model/OrganizationHqLinks}
     */
    OrganizationHqLinks,

    /**
     * The OrganizationRelationships model constructor.
     * @property {module:model/OrganizationRelationships}
     */
    OrganizationRelationships,

    /**
     * The OrganizationResponse model constructor.
     * @property {module:model/OrganizationResponse}
     */
    OrganizationResponse,

    /**
     * The OrganizationSocial model constructor.
     * @property {module:model/OrganizationSocial}
     */
    OrganizationSocial,

    /**
     * The OrganizationSource model constructor.
     * @property {module:model/OrganizationSource}
     */
    OrganizationSource,

    /**
     * The OrganizationSourceData model constructor.
     * @property {module:model/OrganizationSourceData}
     */
    OrganizationSourceData,

    /**
     * The OrganizationSourceLinks model constructor.
     * @property {module:model/OrganizationSourceLinks}
     */
    OrganizationSourceLinks,

    /**
     * The OrganizationsResponse model constructor.
     * @property {module:model/OrganizationsResponse}
     */
    OrganizationsResponse,

    /**
     * The PaymentMethod model constructor.
     * @property {module:model/PaymentMethod}
     */
    PaymentMethod,

    /**
     * The PaymentMethodAttributes model constructor.
     * @property {module:model/PaymentMethodAttributes}
     */
    PaymentMethodAttributes,

    /**
     * The PaymentMethodCurrencies model constructor.
     * @property {module:model/PaymentMethodCurrencies}
     */
    PaymentMethodCurrencies,

    /**
     * The PaymentMethodCurrenciesLinks model constructor.
     * @property {module:model/PaymentMethodCurrenciesLinks}
     */
    PaymentMethodCurrenciesLinks,

    /**
     * The PaymentMethodProcessor model constructor.
     * @property {module:model/PaymentMethodProcessor}
     */
    PaymentMethodProcessor,

    /**
     * The PaymentMethodProcessorData model constructor.
     * @property {module:model/PaymentMethodProcessorData}
     */
    PaymentMethodProcessorData,

    /**
     * The PaymentMethodProcessorLinks model constructor.
     * @property {module:model/PaymentMethodProcessorLinks}
     */
    PaymentMethodProcessorLinks,

    /**
     * The PaymentMethodRelationships model constructor.
     * @property {module:model/PaymentMethodRelationships}
     */
    PaymentMethodRelationships,

    /**
     * The PaymentMethodResponse model constructor.
     * @property {module:model/PaymentMethodResponse}
     */
    PaymentMethodResponse,

    /**
     * The PaymentMethodsResponse model constructor.
     * @property {module:model/PaymentMethodsResponse}
     */
    PaymentMethodsResponse,

    /**
     * The PaymentProvider model constructor.
     * @property {module:model/PaymentProvider}
     */
    PaymentProvider,

    /**
     * The PaymentProviderAttributes model constructor.
     * @property {module:model/PaymentProviderAttributes}
     */
    PaymentProviderAttributes,

    /**
     * The PaymentProviderOrganization model constructor.
     * @property {module:model/PaymentProviderOrganization}
     */
    PaymentProviderOrganization,

    /**
     * The PaymentProviderOrganizationData model constructor.
     * @property {module:model/PaymentProviderOrganizationData}
     */
    PaymentProviderOrganizationData,

    /**
     * The PaymentProviderOrganizationLinks model constructor.
     * @property {module:model/PaymentProviderOrganizationLinks}
     */
    PaymentProviderOrganizationLinks,

    /**
     * The PaymentProviderPaymentMethods model constructor.
     * @property {module:model/PaymentProviderPaymentMethods}
     */
    PaymentProviderPaymentMethods,

    /**
     * The PaymentProviderPaymentMethodsLinks model constructor.
     * @property {module:model/PaymentProviderPaymentMethodsLinks}
     */
    PaymentProviderPaymentMethodsLinks,

    /**
     * The PaymentProviderRelationships model constructor.
     * @property {module:model/PaymentProviderRelationships}
     */
    PaymentProviderRelationships,

    /**
     * The PaymentProviderResponse model constructor.
     * @property {module:model/PaymentProviderResponse}
     */
    PaymentProviderResponse,

    /**
     * The PaymentProvidersResponse model constructor.
     * @property {module:model/PaymentProvidersResponse}
     */
    PaymentProvidersResponse,

    /**
     * The ResponseLinks model constructor.
     * @property {module:model/ResponseLinks}
     */
    ResponseLinks,

    /**
     * The ResponseMeta model constructor.
     * @property {module:model/ResponseMeta}
     */
    ResponseMeta,

    /**
     * The SelfLinks model constructor.
     * @property {module:model/SelfLinks}
     */
    SelfLinks,

    /**
     * The SupportedPspsRelationship model constructor.
     * @property {module:model/SupportedPspsRelationship}
     */
    SupportedPspsRelationship,

    /**
     * The SupportedPspsRelationshipDataInner model constructor.
     * @property {module:model/SupportedPspsRelationshipDataInner}
     */
    SupportedPspsRelationshipDataInner,

    /**
     * The SupportedPspsRelationshipLinks model constructor.
     * @property {module:model/SupportedPspsRelationshipLinks}
     */
    SupportedPspsRelationshipLinks,

    /**
    * The BanksApi service constructor.
    * @property {module:api/BanksApi}
    */
    BanksApi,

    /**
    * The CountriesApi service constructor.
    * @property {module:api/CountriesApi}
    */
    CountriesApi,

    /**
    * The CurrenciesApi service constructor.
    * @property {module:api/CurrenciesApi}
    */
    CurrenciesApi,

    /**
    * The DepositMethodsApi service constructor.
    * @property {module:api/DepositMethodsApi}
    */
    DepositMethodsApi,

    /**
    * The ExchangersApi service constructor.
    * @property {module:api/ExchangersApi}
    */
    ExchangersApi,

    /**
    * The MerchantIndustriesApi service constructor.
    * @property {module:api/MerchantIndustriesApi}
    */
    MerchantIndustriesApi,

    /**
    * The OrganizationsApi service constructor.
    * @property {module:api/OrganizationsApi}
    */
    OrganizationsApi,

    /**
    * The PaymentMethodsApi service constructor.
    * @property {module:api/PaymentMethodsApi}
    */
    PaymentMethodsApi,

    /**
    * The PaymentProvidersApi service constructor.
    * @property {module:api/PaymentProvidersApi}
    */
    PaymentProvidersApi
};
