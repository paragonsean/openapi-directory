/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-12-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import NotificationRecipientUserListByNotification200ResponseValueInnerProperties from './NotificationRecipientUserListByNotification200ResponseValueInnerProperties';

/**
 * The NotificationRecipientUserListByNotification200ResponseValueInner model module.
 * @module model/NotificationRecipientUserListByNotification200ResponseValueInner
 * @version 2019-12-01-preview
 */
class NotificationRecipientUserListByNotification200ResponseValueInner {
    /**
     * Constructs a new <code>NotificationRecipientUserListByNotification200ResponseValueInner</code>.
     * Recipient User details.
     * @alias module:model/NotificationRecipientUserListByNotification200ResponseValueInner
     */
    constructor() { 
        
        NotificationRecipientUserListByNotification200ResponseValueInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NotificationRecipientUserListByNotification200ResponseValueInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NotificationRecipientUserListByNotification200ResponseValueInner} obj Optional instance to populate.
     * @return {module:model/NotificationRecipientUserListByNotification200ResponseValueInner} The populated <code>NotificationRecipientUserListByNotification200ResponseValueInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NotificationRecipientUserListByNotification200ResponseValueInner();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = NotificationRecipientUserListByNotification200ResponseValueInnerProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NotificationRecipientUserListByNotification200ResponseValueInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NotificationRecipientUserListByNotification200ResponseValueInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          NotificationRecipientUserListByNotification200ResponseValueInnerProperties.validateJSON(data['properties']);
        }

        return true;
    }


}



/**
 * @member {module:model/NotificationRecipientUserListByNotification200ResponseValueInnerProperties} properties
 */
NotificationRecipientUserListByNotification200ResponseValueInner.prototype['properties'] = undefined;






export default NotificationRecipientUserListByNotification200ResponseValueInner;

