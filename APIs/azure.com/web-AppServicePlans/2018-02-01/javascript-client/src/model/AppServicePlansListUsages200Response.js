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
import AppServicePlansListUsages200ResponseValueInner from './AppServicePlansListUsages200ResponseValueInner';

/**
 * The AppServicePlansListUsages200Response model module.
 * @module model/AppServicePlansListUsages200Response
 * @version 2018-02-01
 */
class AppServicePlansListUsages200Response {
    /**
     * Constructs a new <code>AppServicePlansListUsages200Response</code>.
     * Collection of CSM usage quotas.
     * @alias module:model/AppServicePlansListUsages200Response
     * @param value {Array.<module:model/AppServicePlansListUsages200ResponseValueInner>} Collection of resources.
     */
    constructor(value) { 
        
        AppServicePlansListUsages200Response.initialize(this, value);
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
     * Constructs a <code>AppServicePlansListUsages200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppServicePlansListUsages200Response} obj Optional instance to populate.
     * @return {module:model/AppServicePlansListUsages200Response} The populated <code>AppServicePlansListUsages200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppServicePlansListUsages200Response();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [AppServicePlansListUsages200ResponseValueInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppServicePlansListUsages200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppServicePlansListUsages200Response</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AppServicePlansListUsages200Response.RequiredProperties) {
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
                AppServicePlansListUsages200ResponseValueInner.validateJSON(item);
            };
        }

        return true;
    }


}

AppServicePlansListUsages200Response.RequiredProperties = ["value"];

/**
 * Link to next page of resources.
 * @member {String} nextLink
 */
AppServicePlansListUsages200Response.prototype['nextLink'] = undefined;

/**
 * Collection of resources.
 * @member {Array.<module:model/AppServicePlansListUsages200ResponseValueInner>} value
 */
AppServicePlansListUsages200Response.prototype['value'] = undefined;






export default AppServicePlansListUsages200Response;

