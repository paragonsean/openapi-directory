/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import NotificationListByService200ResponseValueInnerProperties from './NotificationListByService200ResponseValueInnerProperties';

/**
 * The NotificationGet200Response model module.
 * @module model/NotificationGet200Response
 * @version 2018-06-01-preview
 */
class NotificationGet200Response {
    /**
     * Constructs a new <code>NotificationGet200Response</code>.
     * Notification details.
     * @alias module:model/NotificationGet200Response
     */
    constructor() { 
        
        NotificationGet200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NotificationGet200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NotificationGet200Response} obj Optional instance to populate.
     * @return {module:model/NotificationGet200Response} The populated <code>NotificationGet200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NotificationGet200Response();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = NotificationListByService200ResponseValueInnerProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NotificationGet200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NotificationGet200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          NotificationListByService200ResponseValueInnerProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/NotificationListByService200ResponseValueInnerProperties} properties
 */
NotificationGet200Response.prototype['properties'] = undefined;

/**
 * Resource ID.
 * @member {String} id
 */
NotificationGet200Response.prototype['id'] = undefined;

/**
 * Resource name.
 * @member {String} name
 */
NotificationGet200Response.prototype['name'] = undefined;

/**
 * Resource type for API Management resource.
 * @member {String} type
 */
NotificationGet200Response.prototype['type'] = undefined;






export default NotificationGet200Response;

