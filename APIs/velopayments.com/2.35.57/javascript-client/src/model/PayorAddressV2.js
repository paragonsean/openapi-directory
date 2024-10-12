/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PayorAddressV2 model module.
 * @module model/PayorAddressV2
 * @version 2.35.57
 */
class PayorAddressV2 {
    /**
     * Constructs a new <code>PayorAddressV2</code>.
     * @alias module:model/PayorAddressV2
     * @param city {String} 
     * @param country {String} 
     * @param line1 {String} 
     */
    constructor(city, country, line1) { 
        
        PayorAddressV2.initialize(this, city, country, line1);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, city, country, line1) { 
        obj['city'] = city;
        obj['country'] = country;
        obj['line1'] = line1;
    }

    /**
     * Constructs a <code>PayorAddressV2</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PayorAddressV2} obj Optional instance to populate.
     * @return {module:model/PayorAddressV2} The populated <code>PayorAddressV2</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PayorAddressV2();

            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('countyOrProvince')) {
                obj['countyOrProvince'] = ApiClient.convertToType(data['countyOrProvince'], 'String');
            }
            if (data.hasOwnProperty('line1')) {
                obj['line1'] = ApiClient.convertToType(data['line1'], 'String');
            }
            if (data.hasOwnProperty('line2')) {
                obj['line2'] = ApiClient.convertToType(data['line2'], 'String');
            }
            if (data.hasOwnProperty('line3')) {
                obj['line3'] = ApiClient.convertToType(data['line3'], 'String');
            }
            if (data.hasOwnProperty('line4')) {
                obj['line4'] = ApiClient.convertToType(data['line4'], 'String');
            }
            if (data.hasOwnProperty('zipOrPostcode')) {
                obj['zipOrPostcode'] = ApiClient.convertToType(data['zipOrPostcode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PayorAddressV2</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PayorAddressV2</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PayorAddressV2.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['countyOrProvince'] && !(typeof data['countyOrProvince'] === 'string' || data['countyOrProvince'] instanceof String)) {
            throw new Error("Expected the field `countyOrProvince` to be a primitive type in the JSON string but got " + data['countyOrProvince']);
        }
        // ensure the json data is a string
        if (data['line1'] && !(typeof data['line1'] === 'string' || data['line1'] instanceof String)) {
            throw new Error("Expected the field `line1` to be a primitive type in the JSON string but got " + data['line1']);
        }
        // ensure the json data is a string
        if (data['line2'] && !(typeof data['line2'] === 'string' || data['line2'] instanceof String)) {
            throw new Error("Expected the field `line2` to be a primitive type in the JSON string but got " + data['line2']);
        }
        // ensure the json data is a string
        if (data['line3'] && !(typeof data['line3'] === 'string' || data['line3'] instanceof String)) {
            throw new Error("Expected the field `line3` to be a primitive type in the JSON string but got " + data['line3']);
        }
        // ensure the json data is a string
        if (data['line4'] && !(typeof data['line4'] === 'string' || data['line4'] instanceof String)) {
            throw new Error("Expected the field `line4` to be a primitive type in the JSON string but got " + data['line4']);
        }
        // ensure the json data is a string
        if (data['zipOrPostcode'] && !(typeof data['zipOrPostcode'] === 'string' || data['zipOrPostcode'] instanceof String)) {
            throw new Error("Expected the field `zipOrPostcode` to be a primitive type in the JSON string but got " + data['zipOrPostcode']);
        }

        return true;
    }


}

PayorAddressV2.RequiredProperties = ["city", "country", "line1"];

/**
 * @member {String} city
 */
PayorAddressV2.prototype['city'] = undefined;

/**
 * @member {String} country
 */
PayorAddressV2.prototype['country'] = undefined;

/**
 * @member {String} countyOrProvince
 */
PayorAddressV2.prototype['countyOrProvince'] = undefined;

/**
 * @member {String} line1
 */
PayorAddressV2.prototype['line1'] = undefined;

/**
 * @member {String} line2
 */
PayorAddressV2.prototype['line2'] = undefined;

/**
 * @member {String} line3
 */
PayorAddressV2.prototype['line3'] = undefined;

/**
 * @member {String} line4
 */
PayorAddressV2.prototype['line4'] = undefined;

/**
 * @member {String} zipOrPostcode
 */
PayorAddressV2.prototype['zipOrPostcode'] = undefined;






export default PayorAddressV2;

