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
import RoleRepresentation from './RoleRepresentation';

/**
 * The RolesRepresentation model module.
 * @module model/RolesRepresentation
 * @version 1
 */
class RolesRepresentation {
    /**
     * Constructs a new <code>RolesRepresentation</code>.
     * @alias module:model/RolesRepresentation
     */
    constructor() { 
        
        RolesRepresentation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RolesRepresentation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RolesRepresentation} obj Optional instance to populate.
     * @return {module:model/RolesRepresentation} The populated <code>RolesRepresentation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RolesRepresentation();

            if (data.hasOwnProperty('client')) {
                obj['client'] = ApiClient.convertToType(data['client'], {'String': Object});
            }
            if (data.hasOwnProperty('realm')) {
                obj['realm'] = ApiClient.convertToType(data['realm'], [RoleRepresentation]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RolesRepresentation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RolesRepresentation</code>.
     */
    static validateJSON(data) {
        if (data['realm']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['realm'])) {
                throw new Error("Expected the field `realm` to be an array in the JSON data but got " + data['realm']);
            }
            // validate the optional field `realm` (array)
            for (const item of data['realm']) {
                RoleRepresentation.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Object.<String, Object>} client
 */
RolesRepresentation.prototype['client'] = undefined;

/**
 * @member {Array.<module:model/RoleRepresentation>} realm
 */
RolesRepresentation.prototype['realm'] = undefined;






export default RolesRepresentation;

