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
 * The AnalyticsCrashGroupModelCounts200ResponseModelsInner model module.
 * @module model/AnalyticsCrashGroupModelCounts200ResponseModelsInner
 * @version v0.1
 */
class AnalyticsCrashGroupModelCounts200ResponseModelsInner {
    /**
     * Constructs a new <code>AnalyticsCrashGroupModelCounts200ResponseModelsInner</code>.
     * @alias module:model/AnalyticsCrashGroupModelCounts200ResponseModelsInner
     */
    constructor() { 
        
        AnalyticsCrashGroupModelCounts200ResponseModelsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalyticsCrashGroupModelCounts200ResponseModelsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalyticsCrashGroupModelCounts200ResponseModelsInner} obj Optional instance to populate.
     * @return {module:model/AnalyticsCrashGroupModelCounts200ResponseModelsInner} The populated <code>AnalyticsCrashGroupModelCounts200ResponseModelsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalyticsCrashGroupModelCounts200ResponseModelsInner();

            if (data.hasOwnProperty('crash_count')) {
                obj['crash_count'] = ApiClient.convertToType(data['crash_count'], 'Number');
            }
            if (data.hasOwnProperty('model_name')) {
                obj['model_name'] = ApiClient.convertToType(data['model_name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnalyticsCrashGroupModelCounts200ResponseModelsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnalyticsCrashGroupModelCounts200ResponseModelsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['model_name'] && !(typeof data['model_name'] === 'string' || data['model_name'] instanceof String)) {
            throw new Error("Expected the field `model_name` to be a primitive type in the JSON string but got " + data['model_name']);
        }

        return true;
    }


}



/**
 * Count of model.
 * @member {Number} crash_count
 */
AnalyticsCrashGroupModelCounts200ResponseModelsInner.prototype['crash_count'] = undefined;

/**
 * Model's name.
 * @member {String} model_name
 */
AnalyticsCrashGroupModelCounts200ResponseModelsInner.prototype['model_name'] = undefined;






export default AnalyticsCrashGroupModelCounts200ResponseModelsInner;

