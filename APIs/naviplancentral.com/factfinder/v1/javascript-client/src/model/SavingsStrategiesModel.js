/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
import SavingsStrategyWithIdModel from './SavingsStrategyWithIdModel';

/**
 * The SavingsStrategiesModel model module.
 * @module model/SavingsStrategiesModel
 * @version v1
 */
class SavingsStrategiesModel {
    /**
     * Constructs a new <code>SavingsStrategiesModel</code>.
     * @alias module:model/SavingsStrategiesModel
     */
    constructor() { 
        
        SavingsStrategiesModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SavingsStrategiesModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SavingsStrategiesModel} obj Optional instance to populate.
     * @return {module:model/SavingsStrategiesModel} The populated <code>SavingsStrategiesModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SavingsStrategiesModel();

            if (data.hasOwnProperty('savingsStrategies')) {
                obj['savingsStrategies'] = ApiClient.convertToType(data['savingsStrategies'], [SavingsStrategyWithIdModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SavingsStrategiesModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SavingsStrategiesModel</code>.
     */
    static validateJSON(data) {
        if (data['savingsStrategies']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['savingsStrategies'])) {
                throw new Error("Expected the field `savingsStrategies` to be an array in the JSON data but got " + data['savingsStrategies']);
            }
            // validate the optional field `savingsStrategies` (array)
            for (const item of data['savingsStrategies']) {
                SavingsStrategyWithIdModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/SavingsStrategyWithIdModel>} savingsStrategies
 */
SavingsStrategiesModel.prototype['savingsStrategies'] = undefined;






export default SavingsStrategiesModel;

