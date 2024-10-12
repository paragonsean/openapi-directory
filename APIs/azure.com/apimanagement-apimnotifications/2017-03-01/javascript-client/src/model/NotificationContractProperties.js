/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2017-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RecipientsContractProperties from './RecipientsContractProperties';

/**
 * The NotificationContractProperties model module.
 * @module model/NotificationContractProperties
 * @version 2017-03-01
 */
class NotificationContractProperties {
    /**
     * Constructs a new <code>NotificationContractProperties</code>.
     * Notification Contract properties.
     * @alias module:model/NotificationContractProperties
     * @param title {String} Title of the Notification.
     */
    constructor(title) { 
        
        NotificationContractProperties.initialize(this, title);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, title) { 
        obj['title'] = title;
    }

    /**
     * Constructs a <code>NotificationContractProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NotificationContractProperties} obj Optional instance to populate.
     * @return {module:model/NotificationContractProperties} The populated <code>NotificationContractProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NotificationContractProperties();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('recipients')) {
                obj['recipients'] = RecipientsContractProperties.constructFromObject(data['recipients']);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NotificationContractProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NotificationContractProperties</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NotificationContractProperties.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // validate the optional field `recipients`
        if (data['recipients']) { // data not null
          RecipientsContractProperties.validateJSON(data['recipients']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}

NotificationContractProperties.RequiredProperties = ["title"];

/**
 * Description of the Notification.
 * @member {String} description
 */
NotificationContractProperties.prototype['description'] = undefined;

/**
 * @member {module:model/RecipientsContractProperties} recipients
 */
NotificationContractProperties.prototype['recipients'] = undefined;

/**
 * Title of the Notification.
 * @member {String} title
 */
NotificationContractProperties.prototype['title'] = undefined;






export default NotificationContractProperties;

