/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The WebhookDeliveryLogResourceAttributesRequest model module.
 * @module model/WebhookDeliveryLogResourceAttributesRequest
 * @version v1
 */
class WebhookDeliveryLogResourceAttributesRequest {
    /**
     * Constructs a new <code>WebhookDeliveryLogResourceAttributesRequest</code>.
     * Information about the request that was sent to the webhook URL. 
     * @alias module:model/WebhookDeliveryLogResourceAttributesRequest
     * @param body {String} The payload that was sent in the request body. 
     */
    constructor(body) { 
        
        WebhookDeliveryLogResourceAttributesRequest.initialize(this, body);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, body) { 
        obj['body'] = body;
    }

    /**
     * Constructs a <code>WebhookDeliveryLogResourceAttributesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebhookDeliveryLogResourceAttributesRequest} obj Optional instance to populate.
     * @return {module:model/WebhookDeliveryLogResourceAttributesRequest} The populated <code>WebhookDeliveryLogResourceAttributesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebhookDeliveryLogResourceAttributesRequest();

            if (data.hasOwnProperty('body')) {
                obj['body'] = ApiClient.convertToType(data['body'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebhookDeliveryLogResourceAttributesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebhookDeliveryLogResourceAttributesRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of WebhookDeliveryLogResourceAttributesRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['body'] && !(typeof data['body'] === 'string' || data['body'] instanceof String)) {
            throw new Error("Expected the field `body` to be a primitive type in the JSON string but got " + data['body']);
        }

        return true;
    }


}

WebhookDeliveryLogResourceAttributesRequest.RequiredProperties = ["body"];

/**
 * The payload that was sent in the request body. 
 * @member {String} body
 */
WebhookDeliveryLogResourceAttributesRequest.prototype['body'] = undefined;






export default WebhookDeliveryLogResourceAttributesRequest;

