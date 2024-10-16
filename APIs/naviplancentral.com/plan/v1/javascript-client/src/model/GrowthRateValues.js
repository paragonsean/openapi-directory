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
import Percent from './Percent';

/**
 * The GrowthRateValues model module.
 * @module model/GrowthRateValues
 * @version v1
 */
class GrowthRateValues {
    /**
     * Constructs a new <code>GrowthRateValues</code>.
     * @alias module:model/GrowthRateValues
     */
    constructor() { 
        
        GrowthRateValues.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GrowthRateValues</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GrowthRateValues} obj Optional instance to populate.
     * @return {module:model/GrowthRateValues} The populated <code>GrowthRateValues</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GrowthRateValues();

            if (data.hasOwnProperty('additionalGrowthPercent')) {
                obj['additionalGrowthPercent'] = Percent.constructFromObject(data['additionalGrowthPercent']);
            }
            if (data.hasOwnProperty('isInflationAdjusted')) {
                obj['isInflationAdjusted'] = ApiClient.convertToType(data['isInflationAdjusted'], 'Boolean');
            }
            if (data.hasOwnProperty('totalGrowth')) {
                obj['totalGrowth'] = Percent.constructFromObject(data['totalGrowth']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GrowthRateValues</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GrowthRateValues</code>.
     */
    static validateJSON(data) {
        // validate the optional field `additionalGrowthPercent`
        if (data['additionalGrowthPercent']) { // data not null
          Percent.validateJSON(data['additionalGrowthPercent']);
        }
        // validate the optional field `totalGrowth`
        if (data['totalGrowth']) { // data not null
          Percent.validateJSON(data['totalGrowth']);
        }

        return true;
    }


}



/**
 * @member {module:model/Percent} additionalGrowthPercent
 */
GrowthRateValues.prototype['additionalGrowthPercent'] = undefined;

/**
 * @member {Boolean} isInflationAdjusted
 */
GrowthRateValues.prototype['isInflationAdjusted'] = undefined;

/**
 * @member {module:model/Percent} totalGrowth
 */
GrowthRateValues.prototype['totalGrowth'] = undefined;






export default GrowthRateValues;

