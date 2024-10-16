/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AzureSubscriptionResponse model module.
 * @module model/AzureSubscriptionResponse
 * @version v0.1
 */
class AzureSubscriptionResponse {
    /**
     * Constructs a new <code>AzureSubscriptionResponse</code>.
     * @alias module:model/AzureSubscriptionResponse
     * @param subscriptionId {String} The azure subscription id
     * @param subscriptionName {String} The name of the azure subscription
     * @param tenantId {String} The tenant id of the azure subscription belongs to
     */
    constructor(subscriptionId, subscriptionName, tenantId) { 
        
        AzureSubscriptionResponse.initialize(this, subscriptionId, subscriptionName, tenantId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, subscriptionId, subscriptionName, tenantId) { 
        obj['subscription_id'] = subscriptionId;
        obj['subscription_name'] = subscriptionName;
        obj['tenant_id'] = tenantId;
    }

    /**
     * Constructs a <code>AzureSubscriptionResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AzureSubscriptionResponse} obj Optional instance to populate.
     * @return {module:model/AzureSubscriptionResponse} The populated <code>AzureSubscriptionResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AzureSubscriptionResponse();

            if (data.hasOwnProperty('is_billable')) {
                obj['is_billable'] = ApiClient.convertToType(data['is_billable'], 'Boolean');
            }
            if (data.hasOwnProperty('is_billing')) {
                obj['is_billing'] = ApiClient.convertToType(data['is_billing'], 'Boolean');
            }
            if (data.hasOwnProperty('is_microsoft_internal')) {
                obj['is_microsoft_internal'] = ApiClient.convertToType(data['is_microsoft_internal'], 'Boolean');
            }
            if (data.hasOwnProperty('subscription_id')) {
                obj['subscription_id'] = ApiClient.convertToType(data['subscription_id'], 'String');
            }
            if (data.hasOwnProperty('subscription_name')) {
                obj['subscription_name'] = ApiClient.convertToType(data['subscription_name'], 'String');
            }
            if (data.hasOwnProperty('tenant_id')) {
                obj['tenant_id'] = ApiClient.convertToType(data['tenant_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AzureSubscriptionResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AzureSubscriptionResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AzureSubscriptionResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['subscription_id'] && !(typeof data['subscription_id'] === 'string' || data['subscription_id'] instanceof String)) {
            throw new Error("Expected the field `subscription_id` to be a primitive type in the JSON string but got " + data['subscription_id']);
        }
        // ensure the json data is a string
        if (data['subscription_name'] && !(typeof data['subscription_name'] === 'string' || data['subscription_name'] instanceof String)) {
            throw new Error("Expected the field `subscription_name` to be a primitive type in the JSON string but got " + data['subscription_name']);
        }
        // ensure the json data is a string
        if (data['tenant_id'] && !(typeof data['tenant_id'] === 'string' || data['tenant_id'] instanceof String)) {
            throw new Error("Expected the field `tenant_id` to be a primitive type in the JSON string but got " + data['tenant_id']);
        }

        return true;
    }


}

AzureSubscriptionResponse.RequiredProperties = ["subscription_id", "subscription_name", "tenant_id"];

/**
 * If the subscription can be used for billing
 * @member {Boolean} is_billable
 */
AzureSubscriptionResponse.prototype['is_billable'] = undefined;

/**
 * If the subscription is used for billing
 * @member {Boolean} is_billing
 */
AzureSubscriptionResponse.prototype['is_billing'] = undefined;

/**
 * If the subscription is internal Microsoft subscription
 * @member {Boolean} is_microsoft_internal
 */
AzureSubscriptionResponse.prototype['is_microsoft_internal'] = undefined;

/**
 * The azure subscription id
 * @member {String} subscription_id
 */
AzureSubscriptionResponse.prototype['subscription_id'] = undefined;

/**
 * The name of the azure subscription
 * @member {String} subscription_name
 */
AzureSubscriptionResponse.prototype['subscription_name'] = undefined;

/**
 * The tenant id of the azure subscription belongs to
 * @member {String} tenant_id
 */
AzureSubscriptionResponse.prototype['tenant_id'] = undefined;






export default AzureSubscriptionResponse;

