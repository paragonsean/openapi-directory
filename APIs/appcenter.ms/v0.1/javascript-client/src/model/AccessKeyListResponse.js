/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AccessKeyListResponseAccessKeysInner from './AccessKeyListResponseAccessKeysInner';

/**
 * The AccessKeyListResponse model module.
 * @module model/AccessKeyListResponse
 * @version v0.1
 */
class AccessKeyListResponse {
    /**
     * Constructs a new <code>AccessKeyListResponse</code>.
     * @alias module:model/AccessKeyListResponse
     */
    constructor() { 
        
        AccessKeyListResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AccessKeyListResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccessKeyListResponse} obj Optional instance to populate.
     * @return {module:model/AccessKeyListResponse} The populated <code>AccessKeyListResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccessKeyListResponse();

            if (data.hasOwnProperty('accessKeys')) {
                obj['accessKeys'] = ApiClient.convertToType(data['accessKeys'], [AccessKeyListResponseAccessKeysInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccessKeyListResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccessKeyListResponse</code>.
     */
    static validateJSON(data) {
        if (data['accessKeys']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['accessKeys'])) {
                throw new Error("Expected the field `accessKeys` to be an array in the JSON data but got " + data['accessKeys']);
            }
            // validate the optional field `accessKeys` (array)
            for (const item of data['accessKeys']) {
                AccessKeyListResponseAccessKeysInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Array containing the list of existing AccessKeys
 * @member {Array.<module:model/AccessKeyListResponseAccessKeysInner>} accessKeys
 */
AccessKeyListResponse.prototype['accessKeys'] = undefined;






export default AccessKeyListResponse;

