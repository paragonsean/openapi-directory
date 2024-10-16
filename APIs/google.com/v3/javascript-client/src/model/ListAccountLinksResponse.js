/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AccountLink from './AccountLink';

/**
 * The ListAccountLinksResponse model module.
 * @module model/ListAccountLinksResponse
 * @version v3
 */
class ListAccountLinksResponse {
    /**
     * Constructs a new <code>ListAccountLinksResponse</code>.
     * Response message for AccountLinkService.ListAccountLinks.
     * @alias module:model/ListAccountLinksResponse
     */
    constructor() { 
        
        ListAccountLinksResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListAccountLinksResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListAccountLinksResponse} obj Optional instance to populate.
     * @return {module:model/ListAccountLinksResponse} The populated <code>ListAccountLinksResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListAccountLinksResponse();

            if (data.hasOwnProperty('accountLinks')) {
                obj['accountLinks'] = ApiClient.convertToType(data['accountLinks'], [AccountLink]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListAccountLinksResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListAccountLinksResponse</code>.
     */
    static validateJSON(data) {
        if (data['accountLinks']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['accountLinks'])) {
                throw new Error("Expected the field `accountLinks` to be an array in the JSON data but got " + data['accountLinks']);
            }
            // validate the optional field `accountLinks` (array)
            for (const item of data['accountLinks']) {
                AccountLink.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * A list of all account links associated with the Hotel Center account being queried.
 * @member {Array.<module:model/AccountLink>} accountLinks
 */
ListAccountLinksResponse.prototype['accountLinks'] = undefined;






export default ListAccountLinksResponse;

