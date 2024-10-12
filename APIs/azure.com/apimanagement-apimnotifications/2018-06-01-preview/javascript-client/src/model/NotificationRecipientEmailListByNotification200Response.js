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
import NotificationRecipientEmailListByNotification200ResponseValueInner from './NotificationRecipientEmailListByNotification200ResponseValueInner';

/**
 * The NotificationRecipientEmailListByNotification200Response model module.
 * @module model/NotificationRecipientEmailListByNotification200Response
 * @version 2018-06-01-preview
 */
class NotificationRecipientEmailListByNotification200Response {
    /**
     * Constructs a new <code>NotificationRecipientEmailListByNotification200Response</code>.
     * Paged Recipient User list representation.
     * @alias module:model/NotificationRecipientEmailListByNotification200Response
     */
    constructor() { 
        
        NotificationRecipientEmailListByNotification200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NotificationRecipientEmailListByNotification200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NotificationRecipientEmailListByNotification200Response} obj Optional instance to populate.
     * @return {module:model/NotificationRecipientEmailListByNotification200Response} The populated <code>NotificationRecipientEmailListByNotification200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NotificationRecipientEmailListByNotification200Response();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [NotificationRecipientEmailListByNotification200ResponseValueInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NotificationRecipientEmailListByNotification200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NotificationRecipientEmailListByNotification200Response</code>.
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
                NotificationRecipientEmailListByNotification200ResponseValueInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Next page link if any.
 * @member {String} nextLink
 */
NotificationRecipientEmailListByNotification200Response.prototype['nextLink'] = undefined;

/**
 * Page values.
 * @member {Array.<module:model/NotificationRecipientEmailListByNotification200ResponseValueInner>} value
 */
NotificationRecipientEmailListByNotification200Response.prototype['value'] = undefined;






export default NotificationRecipientEmailListByNotification200Response;

