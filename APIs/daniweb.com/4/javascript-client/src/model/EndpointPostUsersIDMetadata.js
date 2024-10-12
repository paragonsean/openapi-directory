/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The EndpointPostUsersIDMetadata model module.
 * @module model/EndpointPostUsersIDMetadata
 * @version 4
 */
class EndpointPostUsersIDMetadata {
    /**
     * Constructs a new <code>EndpointPostUsersIDMetadata</code>.
     * @alias module:model/EndpointPostUsersIDMetadata
     */
    constructor() { 
        
        EndpointPostUsersIDMetadata.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointPostUsersIDMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointPostUsersIDMetadata} obj Optional instance to populate.
     * @return {module:model/EndpointPostUsersIDMetadata} The populated <code>EndpointPostUsersIDMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointPostUsersIDMetadata();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], {'String': ['String']});
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointPostUsersIDMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointPostUsersIDMetadata</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Object.<String, Array.<String>>} data
 */
EndpointPostUsersIDMetadata.prototype['data'] = undefined;

/**
 * @member {Boolean} success
 */
EndpointPostUsersIDMetadata.prototype['success'] = undefined;






export default EndpointPostUsersIDMetadata;

