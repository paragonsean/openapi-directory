/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PrivateLinkServiceConnectionStateProperty model module.
 * @module model/PrivateLinkServiceConnectionStateProperty
 * @version 2018-06-01
 */
class PrivateLinkServiceConnectionStateProperty {
    /**
     * Constructs a new <code>PrivateLinkServiceConnectionStateProperty</code>.
     * @alias module:model/PrivateLinkServiceConnectionStateProperty
     * @param description {String} The private link service connection description.
     * @param status {String} The private link service connection status.
     */
    constructor(description, status) { 
        
        PrivateLinkServiceConnectionStateProperty.initialize(this, description, status);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, description, status) { 
        obj['description'] = description;
        obj['status'] = status;
    }

    /**
     * Constructs a <code>PrivateLinkServiceConnectionStateProperty</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PrivateLinkServiceConnectionStateProperty} obj Optional instance to populate.
     * @return {module:model/PrivateLinkServiceConnectionStateProperty} The populated <code>PrivateLinkServiceConnectionStateProperty</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PrivateLinkServiceConnectionStateProperty();

            if (data.hasOwnProperty('actionsRequired')) {
                obj['actionsRequired'] = ApiClient.convertToType(data['actionsRequired'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PrivateLinkServiceConnectionStateProperty</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PrivateLinkServiceConnectionStateProperty</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PrivateLinkServiceConnectionStateProperty.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['actionsRequired'] && !(typeof data['actionsRequired'] === 'string' || data['actionsRequired'] instanceof String)) {
            throw new Error("Expected the field `actionsRequired` to be a primitive type in the JSON string but got " + data['actionsRequired']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}

PrivateLinkServiceConnectionStateProperty.RequiredProperties = ["description", "status"];

/**
 * The actions required for private link service connection.
 * @member {String} actionsRequired
 */
PrivateLinkServiceConnectionStateProperty.prototype['actionsRequired'] = undefined;

/**
 * The private link service connection description.
 * @member {String} description
 */
PrivateLinkServiceConnectionStateProperty.prototype['description'] = undefined;

/**
 * The private link service connection status.
 * @member {String} status
 */
PrivateLinkServiceConnectionStateProperty.prototype['status'] = undefined;






export default PrivateLinkServiceConnectionStateProperty;

