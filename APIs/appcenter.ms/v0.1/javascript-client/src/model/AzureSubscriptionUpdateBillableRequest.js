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
 * The AzureSubscriptionUpdateBillableRequest model module.
 * @module model/AzureSubscriptionUpdateBillableRequest
 * @version v0.1
 */
class AzureSubscriptionUpdateBillableRequest {
    /**
     * Constructs a new <code>AzureSubscriptionUpdateBillableRequest</code>.
     * @alias module:model/AzureSubscriptionUpdateBillableRequest
     * @param isBillable {Boolean} Billable status of the subscription
     */
    constructor(isBillable) { 
        
        AzureSubscriptionUpdateBillableRequest.initialize(this, isBillable);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, isBillable) { 
        obj['is_billable'] = isBillable;
    }

    /**
     * Constructs a <code>AzureSubscriptionUpdateBillableRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AzureSubscriptionUpdateBillableRequest} obj Optional instance to populate.
     * @return {module:model/AzureSubscriptionUpdateBillableRequest} The populated <code>AzureSubscriptionUpdateBillableRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AzureSubscriptionUpdateBillableRequest();

            if (data.hasOwnProperty('is_billable')) {
                obj['is_billable'] = ApiClient.convertToType(data['is_billable'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AzureSubscriptionUpdateBillableRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AzureSubscriptionUpdateBillableRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AzureSubscriptionUpdateBillableRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

AzureSubscriptionUpdateBillableRequest.RequiredProperties = ["is_billable"];

/**
 * Billable status of the subscription
 * @member {Boolean} is_billable
 */
AzureSubscriptionUpdateBillableRequest.prototype['is_billable'] = undefined;






export default AzureSubscriptionUpdateBillableRequest;

