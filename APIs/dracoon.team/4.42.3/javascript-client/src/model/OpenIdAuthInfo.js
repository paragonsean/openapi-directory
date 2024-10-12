/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OpenIdProvider from './OpenIdProvider';

/**
 * The OpenIdAuthInfo model module.
 * @module model/OpenIdAuthInfo
 * @version 4.42.3
 */
class OpenIdAuthInfo {
    /**
     * Constructs a new <code>OpenIdAuthInfo</code>.
     * List of OpenID Connect providers
     * @alias module:model/OpenIdAuthInfo
     * @param items {Array.<module:model/OpenIdProvider>} List of available OpenID Connect identity providers
     */
    constructor(items) { 
        
        OpenIdAuthInfo.initialize(this, items);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, items) { 
        obj['items'] = items;
    }

    /**
     * Constructs a <code>OpenIdAuthInfo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OpenIdAuthInfo} obj Optional instance to populate.
     * @return {module:model/OpenIdAuthInfo} The populated <code>OpenIdAuthInfo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OpenIdAuthInfo();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [OpenIdProvider]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OpenIdAuthInfo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OpenIdAuthInfo</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OpenIdAuthInfo.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                OpenIdProvider.validateJSON(item);
            };
        }

        return true;
    }


}

OpenIdAuthInfo.RequiredProperties = ["items"];

/**
 * List of available OpenID Connect identity providers
 * @member {Array.<module:model/OpenIdProvider>} items
 */
OpenIdAuthInfo.prototype['items'] = undefined;






export default OpenIdAuthInfo;

