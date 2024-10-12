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
import AppServicePlansListMetrics200ResponseValueInner from './AppServicePlansListMetrics200ResponseValueInner';

/**
 * The AppServicePlansListMetrics200Response model module.
 * @module model/AppServicePlansListMetrics200Response
 * @version 2018-02-01
 */
class AppServicePlansListMetrics200Response {
    /**
     * Constructs a new <code>AppServicePlansListMetrics200Response</code>.
     * Collection of metric responses.
     * @alias module:model/AppServicePlansListMetrics200Response
     * @param value {Array.<module:model/AppServicePlansListMetrics200ResponseValueInner>} Collection of resources.
     */
    constructor(value) { 
        
        AppServicePlansListMetrics200Response.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>AppServicePlansListMetrics200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListMetrics200Response} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListMetrics200Response} The populated <code>AppServicePlansListMetrics200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListMetrics200Response();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [AppServicePlansListMetrics200ResponseValueInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListMetrics200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListMetrics200Response</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AppServicePlansListMetrics200Response.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                AppServicePlansListMetrics200ResponseValueInner.validateJSON(item);
            };
        }

        return true;
    }


}

AppServicePlansListMetrics200Response.RequiredProperties = ["value"];

/**
 * Link to next page of resources.
 * @member {String} nextLink
 */
AppServicePlansListMetrics200Response.prototype['nextLink'] = undefined;

/**
 * Collection of resources.
 * @member {Array.<module:model/AppServicePlansListMetrics200ResponseValueInner>} value
 */
AppServicePlansListMetrics200Response.prototype['value'] = undefined;






export default AppServicePlansListMetrics200Response;

