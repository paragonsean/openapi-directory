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
 * The CodePushDeploymentMetricsGet200ResponseInner model module.
 * @module model/CodePushDeploymentMetricsGet200ResponseInner
 * @version v0.1
 */
class CodePushDeploymentMetricsGet200ResponseInner {
    /**
     * Constructs a new <code>CodePushDeploymentMetricsGet200ResponseInner</code>.
     * @alias module:model/CodePushDeploymentMetricsGet200ResponseInner
     * @param active {Number} 
     * @param label {String} 
     */
    constructor(active, label) { 
        
        CodePushDeploymentMetricsGet200ResponseInner.initialize(this, active, label);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, active, label) { 
        obj['active'] = active;
        obj['label'] = label;
    }

    /**
     * Constructs a <code>CodePushDeploymentMetricsGet200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CodePushDeploymentMetricsGet200ResponseInner} obj Optional instance to populate.
     * @return {module:model/CodePushDeploymentMetricsGet200ResponseInner} The populated <code>CodePushDeploymentMetricsGet200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CodePushDeploymentMetricsGet200ResponseInner();

            if (data.hasOwnProperty('active')) {
                obj['active'] = ApiClient.convertToType(data['active'], 'Number');
            }
            if (data.hasOwnProperty('downloaded')) {
                obj['downloaded'] = ApiClient.convertToType(data['downloaded'], 'Number');
            }
            if (data.hasOwnProperty('failed')) {
                obj['failed'] = ApiClient.convertToType(data['failed'], 'Number');
            }
            if (data.hasOwnProperty('installed')) {
                obj['installed'] = ApiClient.convertToType(data['installed'], 'Number');
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CodePushDeploymentMetricsGet200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CodePushDeploymentMetricsGet200ResponseInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CodePushDeploymentMetricsGet200ResponseInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }

        return true;
    }


}

CodePushDeploymentMetricsGet200ResponseInner.RequiredProperties = ["active", "label"];

/**
 * @member {Number} active
 */
CodePushDeploymentMetricsGet200ResponseInner.prototype['active'] = undefined;

/**
 * @member {Number} downloaded
 */
CodePushDeploymentMetricsGet200ResponseInner.prototype['downloaded'] = undefined;

/**
 * @member {Number} failed
 */
CodePushDeploymentMetricsGet200ResponseInner.prototype['failed'] = undefined;

/**
 * @member {Number} installed
 */
CodePushDeploymentMetricsGet200ResponseInner.prototype['installed'] = undefined;

/**
 * @member {String} label
 */
CodePushDeploymentMetricsGet200ResponseInner.prototype['label'] = undefined;






export default CodePushDeploymentMetricsGet200ResponseInner;

