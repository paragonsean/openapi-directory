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

/**
 * The WebhookRelationshipsOwnerAccountData model module.
 * @module model/WebhookRelationshipsOwnerAccountData
 * @version 2.0
 */
class WebhookRelationshipsOwnerAccountData {
    /**
     * Constructs a new <code>WebhookRelationshipsOwnerAccountData</code>.
     * @alias module:model/WebhookRelationshipsOwnerAccountData
     */
    constructor() { 
        
        WebhookRelationshipsOwnerAccountData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WebhookRelationshipsOwnerAccountData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebhookRelationshipsOwnerAccountData} obj Optional instance to populate.
     * @return {module:model/WebhookRelationshipsOwnerAccountData} The populated <code>WebhookRelationshipsOwnerAccountData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebhookRelationshipsOwnerAccountData();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebhookRelationshipsOwnerAccountData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebhookRelationshipsOwnerAccountData</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * Account ID
 * @member {Number} id
 */
WebhookRelationshipsOwnerAccountData.prototype['id'] = undefined;

/**
 * Type of thing it is \"account\"
 * @member {String} type
 */
WebhookRelationshipsOwnerAccountData.prototype['type'] = undefined;






export default WebhookRelationshipsOwnerAccountData;

