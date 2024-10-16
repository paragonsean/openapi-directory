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
import AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel from './AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel';

/**
 * The AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel model module.
 * @module model/AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel
 * @version v1
 */
class AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel {
    /**
     * Constructs a new <code>AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel</code>.
     * @alias module:model/AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel
     */
    constructor() { 
        
        AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel} obj Optional instance to populate.
     * @return {module:model/AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel} The populated <code>AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel();

            if (data.hasOwnProperty('liabilities')) {
                obj['liabilities'] = ApiClient.convertToType(data['liabilities'], [AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel</code>.
     */
    static validateJSON(data) {
        if (data['liabilities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['liabilities'])) {
                throw new Error("Expected the field `liabilities` to be an array in the JSON data but got " + data['liabilities']);
            }
            // validate the optional field `liabilities` (array)
            for (const item of data['liabilities']) {
                AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/AdvicentNaviPlanRestApiNetWorthModelsLiabilityModel>} liabilities
 */
AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel.prototype['liabilities'] = undefined;






export default AdvicentNaviPlanRestApiNetWorthModelsLiabilityBaseModel;

