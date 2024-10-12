/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ListSiteIdentifiersAssignedToHostNameRequest model module.
 * @module model/ListSiteIdentifiersAssignedToHostNameRequest
 * @version 2018-02-01
 */
class ListSiteIdentifiersAssignedToHostNameRequest {
    /**
     * Constructs a new <code>ListSiteIdentifiersAssignedToHostNameRequest</code>.
     * Identifies an object.
     * @alias module:model/ListSiteIdentifiersAssignedToHostNameRequest
     */
    constructor() { 
        
        ListSiteIdentifiersAssignedToHostNameRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListSiteIdentifiersAssignedToHostNameRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListSiteIdentifiersAssignedToHostNameRequest} obj Optional instance to populate.
     * @return {module:model/ListSiteIdentifiersAssignedToHostNameRequest} The populated <code>ListSiteIdentifiersAssignedToHostNameRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListSiteIdentifiersAssignedToHostNameRequest();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListSiteIdentifiersAssignedToHostNameRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListSiteIdentifiersAssignedToHostNameRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * Name of the object.
 * @member {String} name
 */
ListSiteIdentifiersAssignedToHostNameRequest.prototype['name'] = undefined;






export default ListSiteIdentifiersAssignedToHostNameRequest;

