/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner model module.
 * @module model/DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner
 * @version 2019-08-01
 */
class DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner {
    /**
     * Constructs a new <code>DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner</code>.
     * Worker pool of an App Service Environment.
     * @alias module:model/DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner
     */
    constructor() { 
        
        DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner} obj Optional instance to populate.
     * @return {module:model/DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner} The populated <code>DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner();

            if (data.hasOwnProperty('computeMode')) {
                obj['computeMode'] = ApiClient.convertToType(data['computeMode'], 'String');
            }
            if (data.hasOwnProperty('instanceNames')) {
                obj['instanceNames'] = ApiClient.convertToType(data['instanceNames'], ['String']);
            }
            if (data.hasOwnProperty('workerCount')) {
                obj['workerCount'] = ApiClient.convertToType(data['workerCount'], 'Number');
            }
            if (data.hasOwnProperty('workerSize')) {
                obj['workerSize'] = ApiClient.convertToType(data['workerSize'], 'String');
            }
            if (data.hasOwnProperty('workerSizeId')) {
                obj['workerSizeId'] = ApiClient.convertToType(data['workerSizeId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['computeMode'] && !(typeof data['computeMode'] === 'string' || data['computeMode'] instanceof String)) {
            throw new Error("Expected the field `computeMode` to be a primitive type in the JSON string but got " + data['computeMode']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['instanceNames'])) {
            throw new Error("Expected the field `instanceNames` to be an array in the JSON data but got " + data['instanceNames']);
        }
        // ensure the json data is a string
        if (data['workerSize'] && !(typeof data['workerSize'] === 'string' || data['workerSize'] instanceof String)) {
            throw new Error("Expected the field `workerSize` to be a primitive type in the JSON string but got " + data['workerSize']);
        }

        return true;
    }


}



/**
 * Shared or dedicated app hosting.
 * @member {module:model/DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.ComputeModeEnum} computeMode
 */
DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.prototype['computeMode'] = undefined;

/**
 * Names of all instances in the worker pool (read only).
 * @member {Array.<String>} instanceNames
 */
DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.prototype['instanceNames'] = undefined;

/**
 * Number of instances in the worker pool.
 * @member {Number} workerCount
 */
DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.prototype['workerCount'] = undefined;

/**
 * VM size of the worker pool instances.
 * @member {String} workerSize
 */
DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.prototype['workerSize'] = undefined;

/**
 * Worker size ID for referencing this worker pool.
 * @member {Number} workerSizeId
 */
DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.prototype['workerSizeId'] = undefined;





/**
 * Allowed values for the <code>computeMode</code> property.
 * @enum {String}
 * @readonly
 */
DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner['ComputeModeEnum'] = {

    /**
     * value: "Shared"
     * @const
     */
    "Shared": "Shared",

    /**
     * value: "Dedicated"
     * @const
     */
    "Dedicated": "Dedicated",

    /**
     * value: "Dynamic"
     * @const
     */
    "Dynamic": "Dynamic"
};



export default DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner;

