/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner model module.
 * @module model/AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner
 * @version 2018-02-01
 */
class AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner {
    /**
     * Constructs a new <code>AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner</code>.
     * Metrics availability and retention.
     * @alias module:model/AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner
     */
    constructor() { 
        
        AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner} The populated <code>AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner();

            if (data.hasOwnProperty('retention')) {
                obj['retention'] = ApiClient.convertToType(data['retention'], 'String');
            }
            if (data.hasOwnProperty('timeGrain')) {
                obj['timeGrain'] = ApiClient.convertToType(data['timeGrain'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['retention'] && !(typeof data['retention'] === 'string' || data['retention'] instanceof String)) {
            throw new Error("Expected the field `retention` to be a primitive type in the JSON string but got " + data['retention']);
        }
        // ensure the json data is a string
        if (data['timeGrain'] && !(typeof data['timeGrain'] === 'string' || data['timeGrain'] instanceof String)) {
            throw new Error("Expected the field `timeGrain` to be a primitive type in the JSON string but got " + data['timeGrain']);
        }

        return true;
    }


}



/**
 * Retention period for the current time grain.
 * @member {String} retention
 */
AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner.prototype['retention'] = undefined;

/**
 * Time grain .
 * @member {String} timeGrain
 */
AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner.prototype['timeGrain'] = undefined;






export default AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner;

