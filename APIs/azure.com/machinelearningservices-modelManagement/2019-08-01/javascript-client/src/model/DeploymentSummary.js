/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
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
 * The DeploymentSummary model module.
 * @module model/DeploymentSummary
 * @version 2019-08-01
 */
class DeploymentSummary {
    /**
     * Constructs a new <code>DeploymentSummary</code>.
     * The deployment summary.
     * @alias module:model/DeploymentSummary
     */
    constructor() { 
        
        DeploymentSummary.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeploymentSummary</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeploymentSummary} obj Optional instance to populate.
     * @return {module:model/DeploymentSummary} The populated <code>DeploymentSummary</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeploymentSummary();

            if (data.hasOwnProperty('successfulDeployments')) {
                obj['successfulDeployments'] = ApiClient.convertToType(data['successfulDeployments'], 'Number');
            }
            if (data.hasOwnProperty('unsuccessfulDeployments')) {
                obj['unsuccessfulDeployments'] = ApiClient.convertToType(data['unsuccessfulDeployments'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeploymentSummary</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeploymentSummary</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * The number of successful deployments.
 * @member {Number} successfulDeployments
 */
DeploymentSummary.prototype['successfulDeployments'] = undefined;

/**
 * The number of unsuccessful deployments.
 * @member {Number} unsuccessfulDeployments
 */
DeploymentSummary.prototype['unsuccessfulDeployments'] = undefined;






export default DeploymentSummary;

