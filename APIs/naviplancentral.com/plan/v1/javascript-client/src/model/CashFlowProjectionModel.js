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
import ObjectLink from './ObjectLink';
import ProjectedCashFlowSummary from './ProjectedCashFlowSummary';

/**
 * The CashFlowProjectionModel model module.
 * @module model/CashFlowProjectionModel
 * @version v1
 */
class CashFlowProjectionModel {
    /**
     * Constructs a new <code>CashFlowProjectionModel</code>.
     * @alias module:model/CashFlowProjectionModel
     */
    constructor() { 
        
        CashFlowProjectionModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CashFlowProjectionModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CashFlowProjectionModel} obj Optional instance to populate.
     * @return {module:model/CashFlowProjectionModel} The populated <code>CashFlowProjectionModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CashFlowProjectionModel();

            if (data.hasOwnProperty('cashFlow')) {
                obj['cashFlow'] = ProjectedCashFlowSummary.constructFromObject(data['cashFlow']);
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = ApiClient.convertToType(data['links'], [ObjectLink]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CashFlowProjectionModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CashFlowProjectionModel</code>.
     */
    static validateJSON(data) {
        // validate the optional field `cashFlow`
        if (data['cashFlow']) { // data not null
          ProjectedCashFlowSummary.validateJSON(data['cashFlow']);
        }
        if (data['links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['links'])) {
                throw new Error("Expected the field `links` to be an array in the JSON data but got " + data['links']);
            }
            // validate the optional field `links` (array)
            for (const item of data['links']) {
                ObjectLink.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/ProjectedCashFlowSummary} cashFlow
 */
CashFlowProjectionModel.prototype['cashFlow'] = undefined;

/**
 * @member {Array.<module:model/ObjectLink>} links
 */
CashFlowProjectionModel.prototype['links'] = undefined;






export default CashFlowProjectionModel;

