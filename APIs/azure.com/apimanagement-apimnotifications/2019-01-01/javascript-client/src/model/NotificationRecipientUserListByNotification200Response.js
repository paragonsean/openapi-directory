/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import NotificationRecipientUserListByNotification200ResponseValueInner from './NotificationRecipientUserListByNotification200ResponseValueInner';

/**
 * The NotificationRecipientUserListByNotification200Response model module.
 * @module model/NotificationRecipientUserListByNotification200Response
 * @version 2019-01-01
 */
class NotificationRecipientUserListByNotification200Response {
    /**
     * Constructs a new <code>NotificationRecipientUserListByNotification200Response</code>.
     * Paged Recipient User list representation.
     * @alias module:model/NotificationRecipientUserListByNotification200Response
     */
    constructor() { 
        
        NotificationRecipientUserListByNotification200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NotificationRecipientUserListByNotification200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NotificationRecipientUserListByNotification200Response} obj Optional instance to populate.
     * @return {module:model/NotificationRecipientUserListByNotification200Response} The populated <code>NotificationRecipientUserListByNotification200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NotificationRecipientUserListByNotification200Response();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [NotificationRecipientUserListByNotification200ResponseValueInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NotificationRecipientUserListByNotification200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NotificationRecipientUserListByNotification200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                NotificationRecipientUserListByNotification200ResponseValueInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Next page link if any.
 * @member {String} nextLink
 */
NotificationRecipientUserListByNotification200Response.prototype['nextLink'] = undefined;

/**
 * Page values.
 * @member {Array.<module:model/NotificationRecipientUserListByNotification200ResponseValueInner>} value
 */
NotificationRecipientUserListByNotification200Response.prototype['value'] = undefined;






export default NotificationRecipientUserListByNotification200Response;

