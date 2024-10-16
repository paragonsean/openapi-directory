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
 * The AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel model module.
 * @module model/AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel
 * @version v1
 */
class AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel {
    /**
     * Constructs a new <code>AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel</code>.
     * @alias module:model/AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel
     */
    constructor() { 
        
        AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel} obj Optional instance to populate.
     * @return {module:model/AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel} The populated <code>AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel();

            if (data.hasOwnProperty('additionalMonthlySavings')) {
                obj['additionalMonthlySavings'] = ApiClient.convertToType(data['additionalMonthlySavings'], 'Number');
            }
            if (data.hasOwnProperty('clientRetirementAge')) {
                obj['clientRetirementAge'] = ApiClient.convertToType(data['clientRetirementAge'], 'Number');
            }
            if (data.hasOwnProperty('clientRetirementAgeDate')) {
                obj['clientRetirementAgeDate'] = ApiClient.convertToType(data['clientRetirementAgeDate'], 'Date');
            }
            if (data.hasOwnProperty('coClientRetirementAge')) {
                obj['coClientRetirementAge'] = ApiClient.convertToType(data['coClientRetirementAge'], 'Number');
            }
            if (data.hasOwnProperty('coClientRetirementAgeDate')) {
                obj['coClientRetirementAgeDate'] = ApiClient.convertToType(data['coClientRetirementAgeDate'], 'Date');
            }
            if (data.hasOwnProperty('expenseCoverageDollars')) {
                obj['expenseCoverageDollars'] = ApiClient.convertToType(data['expenseCoverageDollars'], 'Number');
            }
            if (data.hasOwnProperty('expenseCoveragePercentage')) {
                obj['expenseCoveragePercentage'] = ApiClient.convertToType(data['expenseCoveragePercentage'], 'Number');
            }
            if (data.hasOwnProperty('lumpSumSavings')) {
                obj['lumpSumSavings'] = ApiClient.convertToType(data['lumpSumSavings'], 'Number');
            }
            if (data.hasOwnProperty('purchaseDate')) {
                obj['purchaseDate'] = ApiClient.convertToType(data['purchaseDate'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Number} additionalMonthlySavings
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['additionalMonthlySavings'] = undefined;

/**
 * @member {Number} clientRetirementAge
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['clientRetirementAge'] = undefined;

/**
 * @member {Date} clientRetirementAgeDate
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['clientRetirementAgeDate'] = undefined;

/**
 * @member {Number} coClientRetirementAge
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['coClientRetirementAge'] = undefined;

/**
 * @member {Date} coClientRetirementAgeDate
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['coClientRetirementAgeDate'] = undefined;

/**
 * @member {Number} expenseCoverageDollars
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['expenseCoverageDollars'] = undefined;

/**
 * @member {Number} expenseCoveragePercentage
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['expenseCoveragePercentage'] = undefined;

/**
 * @member {Number} lumpSumSavings
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['lumpSumSavings'] = undefined;

/**
 * @member {Date} purchaseDate
 */
AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel.prototype['purchaseDate'] = undefined;






export default AdvicentNaviPlanRestApiGoalAdjustmentsModelsWhatAreMyOptionsModel;

