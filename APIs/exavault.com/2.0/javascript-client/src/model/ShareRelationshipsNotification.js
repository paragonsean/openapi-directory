/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ShareRelationshipsNotificationData from './ShareRelationshipsNotificationData';

/**
 * The ShareRelationshipsNotification model module.
 * @module model/ShareRelationshipsNotification
 * @version 2.0
 */
class ShareRelationshipsNotification {
    /**
     * Constructs a new <code>ShareRelationshipsNotification</code>.
     * @alias module:model/ShareRelationshipsNotification
     */
    constructor() { 
        
        ShareRelationshipsNotification.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ShareRelationshipsNotification</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ShareRelationshipsNotification} obj Optional instance to populate.
     * @return {module:model/ShareRelationshipsNotification} The populated <code>ShareRelationshipsNotification</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ShareRelationshipsNotification();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ShareRelationshipsNotificationData.constructFromObject(data['data']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ShareRelationshipsNotification</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ShareRelationshipsNotification</code>.
     */
    static validateJSON(data) {
        // validate the optional field `data`
        if (data['data']) { // data not null
          ShareRelationshipsNotificationData.validateJSON(data['data']);
        }

        return true;
    }


}



/**
 * @member {module:model/ShareRelationshipsNotificationData} data
 */
ShareRelationshipsNotification.prototype['data'] = undefined;






export default ShareRelationshipsNotification;

