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

import ApiClient from '../ApiClient';

/**
 * The CountryAttributes model module.
 * @module model/CountryAttributes
 * @version 2017-08-24
 */
class CountryAttributes {
    /**
     * Constructs a new <code>CountryAttributes</code>.
     * @alias module:model/CountryAttributes
     */
    constructor() { 
        
        CountryAttributes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CountryAttributes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CountryAttributes} obj Optional instance to populate.
     * @return {module:model/CountryAttributes} The populated <code>CountryAttributes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CountryAttributes();

            if (data.hasOwnProperty('area')) {
                obj['area'] = ApiClient.convertToType(data['area'], 'String');
            }
            if (data.hasOwnProperty('calling_codes')) {
                obj['calling_codes'] = ApiClient.convertToType(data['calling_codes'], ['Number']);
            }
            if (data.hasOwnProperty('capital')) {
                obj['capital'] = ApiClient.convertToType(data['capital'], 'String');
            }
            if (data.hasOwnProperty('code_alpha3')) {
                obj['code_alpha3'] = ApiClient.convertToType(data['code_alpha3'], 'String');
            }
            if (data.hasOwnProperty('languages')) {
                obj['languages'] = ApiClient.convertToType(data['languages'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('native_name')) {
                obj['native_name'] = ApiClient.convertToType(data['native_name'], 'String');
            }
            if (data.hasOwnProperty('population')) {
                obj['population'] = ApiClient.convertToType(data['population'], 'String');
            }
            if (data.hasOwnProperty('region')) {
                obj['region'] = ApiClient.convertToType(data['region'], 'String');
            }
            if (data.hasOwnProperty('sub_region')) {
                obj['sub_region'] = ApiClient.convertToType(data['sub_region'], 'String');
            }
            if (data.hasOwnProperty('timezones')) {
                obj['timezones'] = ApiClient.convertToType(data['timezones'], ['String']);
            }
            if (data.hasOwnProperty('top_level_domains')) {
                obj['top_level_domains'] = ApiClient.convertToType(data['top_level_domains'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CountryAttributes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CountryAttributes</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['area'] && !(typeof data['area'] === 'string' || data['area'] instanceof String)) {
            throw new Error("Expected the field `area` to be a primitive type in the JSON string but got " + data['area']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['calling_codes'])) {
            throw new Error("Expected the field `calling_codes` to be an array in the JSON data but got " + data['calling_codes']);
        }
        // ensure the json data is a string
        if (data['capital'] && !(typeof data['capital'] === 'string' || data['capital'] instanceof String)) {
            throw new Error("Expected the field `capital` to be a primitive type in the JSON string but got " + data['capital']);
        }
        // ensure the json data is a string
        if (data['code_alpha3'] && !(typeof data['code_alpha3'] === 'string' || data['code_alpha3'] instanceof String)) {
            throw new Error("Expected the field `code_alpha3` to be a primitive type in the JSON string but got " + data['code_alpha3']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['languages'])) {
            throw new Error("Expected the field `languages` to be an array in the JSON data but got " + data['languages']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['native_name'] && !(typeof data['native_name'] === 'string' || data['native_name'] instanceof String)) {
            throw new Error("Expected the field `native_name` to be a primitive type in the JSON string but got " + data['native_name']);
        }
        // ensure the json data is a string
        if (data['population'] && !(typeof data['population'] === 'string' || data['population'] instanceof String)) {
            throw new Error("Expected the field `population` to be a primitive type in the JSON string but got " + data['population']);
        }
        // ensure the json data is a string
        if (data['region'] && !(typeof data['region'] === 'string' || data['region'] instanceof String)) {
            throw new Error("Expected the field `region` to be a primitive type in the JSON string but got " + data['region']);
        }
        // ensure the json data is a string
        if (data['sub_region'] && !(typeof data['sub_region'] === 'string' || data['sub_region'] instanceof String)) {
            throw new Error("Expected the field `sub_region` to be a primitive type in the JSON string but got " + data['sub_region']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['timezones'])) {
            throw new Error("Expected the field `timezones` to be an array in the JSON data but got " + data['timezones']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['top_level_domains'])) {
            throw new Error("Expected the field `top_level_domains` to be an array in the JSON data but got " + data['top_level_domains']);
        }

        return true;
    }


}



/**
 * Countryâ€™s area (sq km)
 * @member {String} area
 */
CountryAttributes.prototype['area'] = undefined;

/**
 * Array of country`s phone codes
 * @member {Array.<Number>} calling_codes
 */
CountryAttributes.prototype['calling_codes'] = undefined;

/**
 * Countryâ€™s capital
 * @member {String} capital
 */
CountryAttributes.prototype['capital'] = undefined;

/**
 * Country`s ISO alpha3 code
 * @member {String} code_alpha3
 */
CountryAttributes.prototype['code_alpha3'] = undefined;

/**
 * Array of country`s languages
 * @member {Array.<String>} languages
 */
CountryAttributes.prototype['languages'] = undefined;

/**
 * Country`s name
 * @member {String} name
 */
CountryAttributes.prototype['name'] = undefined;

/**
 * Country`s nativ name
 * @member {String} native_name
 */
CountryAttributes.prototype['native_name'] = undefined;

/**
 * Countryâ€™s population
 * @member {String} population
 */
CountryAttributes.prototype['population'] = undefined;

/**
 * Countryâ€™s region:<br>    * Africa   * Americas   * Asia   * Europe   * Oceania   * Polar 
 * @member {String} region
 */
CountryAttributes.prototype['region'] = undefined;

/**
 * Countryâ€™s sub region:<br>    * Northern Africa   * Southern Africa   * Western Africa   * Eastern Africa   * Middle Africa   * Northern America   * South America   * Central America   * Caribbean   * Southern Asia   * Western Asia   * Eastern Asia   * South-Eastern Asia   * Central Asia   * Northern Europe   * Southern Europe   * Western Europe   * Eastern Europe   * Polynesia   * Australia and New Zealand   * Micronesia   * Melanesia 
 * @member {String} sub_region
 */
CountryAttributes.prototype['sub_region'] = undefined;

/**
 * Array of country`s timezones (UTC)
 * @member {Array.<String>} timezones
 */
CountryAttributes.prototype['timezones'] = undefined;

/**
 * Array of country`s domains
 * @member {Array.<String>} top_level_domains
 */
CountryAttributes.prototype['top_level_domains'] = undefined;






export default CountryAttributes;

