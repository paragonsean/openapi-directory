/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Permission from './Permission';

/**
 * The AccessTokenAuthorization model module.
 * @module model/AccessTokenAuthorization
 * @version 1
 */
class AccessTokenAuthorization {
    /**
     * Constructs a new <code>AccessTokenAuthorization</code>.
     * @alias module:model/AccessTokenAuthorization
     */
    constructor() { 
        
        AccessTokenAuthorization.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AccessTokenAuthorization</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccessTokenAuthorization} obj Optional instance to populate.
     * @return {module:model/AccessTokenAuthorization} The populated <code>AccessTokenAuthorization</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccessTokenAuthorization();

            if (data.hasOwnProperty('permissions')) {
                obj['permissions'] = ApiClient.convertToType(data['permissions'], [Permission]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccessTokenAuthorization</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccessTokenAuthorization</code>.
     */
    static validateJSON(data) {
        if (data['permissions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['permissions'])) {
                throw new Error("Expected the field `permissions` to be an array in the JSON data but got " + data['permissions']);
            }
            // validate the optional field `permissions` (array)
            for (const item of data['permissions']) {
                Permission.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Permission>} permissions
 */
AccessTokenAuthorization.prototype['permissions'] = undefined;






export default AccessTokenAuthorization;

