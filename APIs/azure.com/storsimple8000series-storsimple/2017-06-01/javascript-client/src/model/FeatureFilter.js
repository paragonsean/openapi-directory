/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FeatureFilter model module.
 * @module model/FeatureFilter
 * @version 2017-06-01
 */
class FeatureFilter {
    /**
     * Constructs a new <code>FeatureFilter</code>.
     * The OData filter to be used for features.
     * @alias module:model/FeatureFilter
     */
    constructor() { 
        
        FeatureFilter.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FeatureFilter</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FeatureFilter} obj Optional instance to populate.
     * @return {module:model/FeatureFilter} The populated <code>FeatureFilter</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FeatureFilter();

            if (data.hasOwnProperty('deviceId')) {
                obj['deviceId'] = ApiClient.convertToType(data['deviceId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FeatureFilter</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FeatureFilter</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['deviceId'] && !(typeof data['deviceId'] === 'string' || data['deviceId'] instanceof String)) {
            throw new Error("Expected the field `deviceId` to be a primitive type in the JSON string but got " + data['deviceId']);
        }

        return true;
    }


}



/**
 * Specifies the device ID for which the features are required. Only 'Equality' operator is supported for this property.
 * @member {String} deviceId
 */
FeatureFilter.prototype['deviceId'] = undefined;






export default FeatureFilter;

