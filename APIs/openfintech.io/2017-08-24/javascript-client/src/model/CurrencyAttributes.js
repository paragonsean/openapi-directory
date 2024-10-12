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
import CurrencyAttributesIcon from './CurrencyAttributesIcon';

/**
 * The CurrencyAttributes model module.
 * @module model/CurrencyAttributes
 * @version 2017-08-24
 */
class CurrencyAttributes {
    /**
     * Constructs a new <code>CurrencyAttributes</code>.
     * Array of currencies attributes
     * @alias module:model/CurrencyAttributes
     */
    constructor() { 
        
        CurrencyAttributes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CurrencyAttributes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CurrencyAttributes} obj Optional instance to populate.
     * @return {module:model/CurrencyAttributes} The populated <code>CurrencyAttributes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CurrencyAttributes();

            if (data.hasOwnProperty('category')) {
                obj['category'] = ApiClient.convertToType(data['category'], 'String');
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('code_estandards_alpha')) {
                obj['code_estandards_alpha'] = ApiClient.convertToType(data['code_estandards_alpha'], 'String');
            }
            if (data.hasOwnProperty('code_iso_alpha3')) {
                obj['code_iso_alpha3'] = ApiClient.convertToType(data['code_iso_alpha3'], 'String');
            }
            if (data.hasOwnProperty('code_iso_numeric3')) {
                obj['code_iso_numeric3'] = ApiClient.convertToType(data['code_iso_numeric3'], 'Number');
            }
            if (data.hasOwnProperty('code_json_alpha')) {
                obj['code_json_alpha'] = ApiClient.convertToType(data['code_json_alpha'], 'String');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'String');
            }
            if (data.hasOwnProperty('currency_type')) {
                obj['currency_type'] = ApiClient.convertToType(data['currency_type'], 'String');
            }
            if (data.hasOwnProperty('decimal_e')) {
                obj['decimal_e'] = ApiClient.convertToType(data['decimal_e'], 'String');
            }
            if (data.hasOwnProperty('icon')) {
                obj['icon'] = CurrencyAttributesIcon.constructFromObject(data['icon']);
            }
            if (data.hasOwnProperty('issuer')) {
                obj['issuer'] = ApiClient.convertToType(data['issuer'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('native_symbol')) {
                obj['native_symbol'] = ApiClient.convertToType(data['native_symbol'], 'String');
            }
            if (data.hasOwnProperty('symbol')) {
                obj['symbol'] = ApiClient.convertToType(data['symbol'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CurrencyAttributes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CurrencyAttributes</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['category'] && !(typeof data['category'] === 'string' || data['category'] instanceof String)) {
            throw new Error("Expected the field `category` to be a primitive type in the JSON string but got " + data['category']);
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['code_estandards_alpha'] && !(typeof data['code_estandards_alpha'] === 'string' || data['code_estandards_alpha'] instanceof String)) {
            throw new Error("Expected the field `code_estandards_alpha` to be a primitive type in the JSON string but got " + data['code_estandards_alpha']);
        }
        // ensure the json data is a string
        if (data['code_iso_alpha3'] && !(typeof data['code_iso_alpha3'] === 'string' || data['code_iso_alpha3'] instanceof String)) {
            throw new Error("Expected the field `code_iso_alpha3` to be a primitive type in the JSON string but got " + data['code_iso_alpha3']);
        }
        // ensure the json data is a string
        if (data['code_json_alpha'] && !(typeof data['code_json_alpha'] === 'string' || data['code_json_alpha'] instanceof String)) {
            throw new Error("Expected the field `code_json_alpha` to be a primitive type in the JSON string but got " + data['code_json_alpha']);
        }
        // ensure the json data is a string
        if (data['created'] && !(typeof data['created'] === 'string' || data['created'] instanceof String)) {
            throw new Error("Expected the field `created` to be a primitive type in the JSON string but got " + data['created']);
        }
        // ensure the json data is a string
        if (data['currency_type'] && !(typeof data['currency_type'] === 'string' || data['currency_type'] instanceof String)) {
            throw new Error("Expected the field `currency_type` to be a primitive type in the JSON string but got " + data['currency_type']);
        }
        // ensure the json data is a string
        if (data['decimal_e'] && !(typeof data['decimal_e'] === 'string' || data['decimal_e'] instanceof String)) {
            throw new Error("Expected the field `decimal_e` to be a primitive type in the JSON string but got " + data['decimal_e']);
        }
        // validate the optional field `icon`
        if (data['icon']) { // data not null
          CurrencyAttributesIcon.validateJSON(data['icon']);
        }
        // ensure the json data is a string
        if (data['issuer'] && !(typeof data['issuer'] === 'string' || data['issuer'] instanceof String)) {
            throw new Error("Expected the field `issuer` to be a primitive type in the JSON string but got " + data['issuer']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['native_symbol'] && !(typeof data['native_symbol'] === 'string' || data['native_symbol'] instanceof String)) {
            throw new Error("Expected the field `native_symbol` to be a primitive type in the JSON string but got " + data['native_symbol']);
        }
        // ensure the json data is a string
        if (data['symbol'] && !(typeof data['symbol'] === 'string' || data['symbol'] instanceof String)) {
            throw new Error("Expected the field `symbol` to be a primitive type in the JSON string but got " + data['symbol']);
        }

        return true;
    }


}



/**
 * Currency category
 * @member {String} category
 */
CurrencyAttributes.prototype['category'] = undefined;

/**
 * Currency system code
 * @member {String} code
 */
CurrencyAttributes.prototype['code'] = undefined;

/**
 * @member {String} code_estandards_alpha
 */
CurrencyAttributes.prototype['code_estandards_alpha'] = undefined;

/**
 * Currency ISO code
 * @member {String} code_iso_alpha3
 */
CurrencyAttributes.prototype['code_iso_alpha3'] = undefined;

/**
 * Currency ISO numeric code
 * @member {Number} code_iso_numeric3
 */
CurrencyAttributes.prototype['code_iso_numeric3'] = undefined;

/**
 * @member {String} code_json_alpha
 */
CurrencyAttributes.prototype['code_json_alpha'] = undefined;

/**
 * Created date in system (in Unixtime)
 * @member {String} created
 */
CurrencyAttributes.prototype['created'] = undefined;

/**
 * Type of currencies [national, digital, virtual, metal, energy]
 * @member {String} currency_type
 */
CurrencyAttributes.prototype['currency_type'] = undefined;

/**
 * Number of digits after the decimal separator
 * @member {String} decimal_e
 */
CurrencyAttributes.prototype['decimal_e'] = undefined;

/**
 * @member {module:model/CurrencyAttributesIcon} icon
 */
CurrencyAttributes.prototype['icon'] = undefined;

/**
 * Currency`s issuer
 * @member {String} issuer
 */
CurrencyAttributes.prototype['issuer'] = undefined;

/**
 * Currency description
 * @member {String} name
 */
CurrencyAttributes.prototype['name'] = undefined;

/**
 * Currencyâ€™s symbol. In general, only for nationals currencies
 * @member {String} native_symbol
 */
CurrencyAttributes.prototype['native_symbol'] = undefined;

/**
 * Currencyâ€™s symbol. In general, only for nationals currencies
 * @member {String} symbol
 */
CurrencyAttributes.prototype['symbol'] = undefined;






export default CurrencyAttributes;

