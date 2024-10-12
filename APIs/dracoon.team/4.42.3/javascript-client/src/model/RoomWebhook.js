/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Webhook from './Webhook';

/**
 * The RoomWebhook model module.
 * @module model/RoomWebhook
 * @version 4.42.3
 */
class RoomWebhook {
    /**
     * Constructs a new <code>RoomWebhook</code>.
     * Webhook information
     * @alias module:model/RoomWebhook
     * @param isAssigned {Boolean} Determines whether webhook is assigned to the room.
     * @param webhook {module:model/Webhook} 
     */
    constructor(isAssigned, webhook) { 
        
        RoomWebhook.initialize(this, isAssigned, webhook);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, isAssigned, webhook) { 
        obj['isAssigned'] = isAssigned;
        obj['webhook'] = webhook;
    }

    /**
     * Constructs a <code>RoomWebhook</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RoomWebhook} obj Optional instance to populate.
     * @return {module:model/RoomWebhook} The populated <code>RoomWebhook</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RoomWebhook();

            if (data.hasOwnProperty('isAssigned')) {
                obj['isAssigned'] = ApiClient.convertToType(data['isAssigned'], 'Boolean');
            }
            if (data.hasOwnProperty('webhook')) {
                obj['webhook'] = Webhook.constructFromObject(data['webhook']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RoomWebhook</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RoomWebhook</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RoomWebhook.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `webhook`
        if (data['webhook']) { // data not null
          Webhook.validateJSON(data['webhook']);
        }

        return true;
    }


}

RoomWebhook.RequiredProperties = ["isAssigned", "webhook"];

/**
 * Determines whether webhook is assigned to the room.
 * @member {Boolean} isAssigned
 */
RoomWebhook.prototype['isAssigned'] = undefined;

/**
 * @member {module:model/Webhook} webhook
 */
RoomWebhook.prototype['webhook'] = undefined;






export default RoomWebhook;

