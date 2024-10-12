/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ListEnvironmentsPayload model module.
 * @module model/ListEnvironmentsPayload
 * @version 2018-10-15
 */
class ListEnvironmentsPayload {
    /**
     * Constructs a new <code>ListEnvironmentsPayload</code>.
     * Represents the payload to list environments owned by a user
     * @alias module:model/ListEnvironmentsPayload
     */
    constructor() { 
        
        ListEnvironmentsPayload.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListEnvironmentsPayload</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListEnvironmentsPayload} obj Optional instance to populate.
     * @return {module:model/ListEnvironmentsPayload} The populated <code>ListEnvironmentsPayload</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListEnvironmentsPayload();

            if (data.hasOwnProperty('labId')) {
                obj['labId'] = ApiClient.convertToType(data['labId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListEnvironmentsPayload</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListEnvironmentsPayload</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['labId'] && !(typeof data['labId'] === 'string' || data['labId'] instanceof String)) {
            throw new Error("Expected the field `labId` to be a primitive type in the JSON string but got " + data['labId']);
        }

        return true;
    }


}



/**
 * The resource Id of the lab
 * @member {String} labId
 */
ListEnvironmentsPayload.prototype['labId'] = undefined;






export default ListEnvironmentsPayload;

