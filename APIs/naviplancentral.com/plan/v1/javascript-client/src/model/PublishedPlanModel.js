/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
 * The PublishedPlanModel model module.
 * @module model/PublishedPlanModel
 * @version v1
 */
class PublishedPlanModel {
    /**
     * Constructs a new <code>PublishedPlanModel</code>.
     * @alias module:model/PublishedPlanModel
     */
    constructor() { 
        
        PublishedPlanModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PublishedPlanModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PublishedPlanModel} obj Optional instance to populate.
     * @return {module:model/PublishedPlanModel} The populated <code>PublishedPlanModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PublishedPlanModel();

            if (data.hasOwnProperty('internalPlanId')) {
                obj['internalPlanId'] = ApiClient.convertToType(data['internalPlanId'], 'Number');
            }
            if (data.hasOwnProperty('planId')) {
                obj['planId'] = ApiClient.convertToType(data['planId'], 'String');
            }
            if (data.hasOwnProperty('planPublishDate')) {
                obj['planPublishDate'] = ApiClient.convertToType(data['planPublishDate'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PublishedPlanModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PublishedPlanModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['planId'] && !(typeof data['planId'] === 'string' || data['planId'] instanceof String)) {
            throw new Error("Expected the field `planId` to be a primitive type in the JSON string but got " + data['planId']);
        }

        return true;
    }


}



/**
 * @member {Number} internalPlanId
 */
PublishedPlanModel.prototype['internalPlanId'] = undefined;

/**
 * @member {String} planId
 */
PublishedPlanModel.prototype['planId'] = undefined;

/**
 * @member {Date} planPublishDate
 */
PublishedPlanModel.prototype['planPublishDate'] = undefined;






export default PublishedPlanModel;

