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
import LiabilityWithIdModel from './LiabilityWithIdModel';

/**
 * The LiabilitiesModel model module.
 * @module model/LiabilitiesModel
 * @version v1
 */
class LiabilitiesModel {
    /**
     * Constructs a new <code>LiabilitiesModel</code>.
     * @alias module:model/LiabilitiesModel
     */
    constructor() { 
        
        LiabilitiesModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LiabilitiesModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LiabilitiesModel} obj Optional instance to populate.
     * @return {module:model/LiabilitiesModel} The populated <code>LiabilitiesModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LiabilitiesModel();

            if (data.hasOwnProperty('liabilities')) {
                obj['liabilities'] = ApiClient.convertToType(data['liabilities'], [LiabilityWithIdModel]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LiabilitiesModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LiabilitiesModel</code>.
     */
    static validateJSON(data) {
        if (data['liabilities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['liabilities'])) {
                throw new Error("Expected the field `liabilities` to be an array in the JSON data but got " + data['liabilities']);
            }
            // validate the optional field `liabilities` (array)
            for (const item of data['liabilities']) {
                LiabilityWithIdModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/LiabilityWithIdModel>} liabilities
 */
LiabilitiesModel.prototype['liabilities'] = undefined;






export default LiabilitiesModel;

