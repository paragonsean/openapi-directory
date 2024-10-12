/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpgradeNotification model module.
 * @module model/UpgradeNotification
 * @version 2019-07-01
 */
class UpgradeNotification {
    /**
     * Constructs a new <code>UpgradeNotification</code>.
     * Properties of upgrade notification.
     * @alias module:model/UpgradeNotification
     */
    constructor() { 
        
        UpgradeNotification.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpgradeNotification</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpgradeNotification} obj Optional instance to populate.
     * @return {module:model/UpgradeNotification} The populated <code>UpgradeNotification</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpgradeNotification();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
            if (data.hasOwnProperty('upsellNotification')) {
                obj['upsellNotification'] = ApiClient.convertToType(data['upsellNotification'], {'String': 'String'});
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpgradeNotification</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpgradeNotification</code>.
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
 * Name of upgrade notification.
 * @member {String} name
 */
UpgradeNotification.prototype['name'] = undefined;

/**
 * Timestamp when upgrade notification occurred.
 * @member {Date} timestamp
 */
UpgradeNotification.prototype['timestamp'] = undefined;

/**
 * Details about this upgrade notification
 * @member {Object.<String, String>} upsellNotification
 */
UpgradeNotification.prototype['upsellNotification'] = undefined;






export default UpgradeNotification;

