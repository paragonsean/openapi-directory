/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import DeploymentSummary from './DeploymentSummary';

/**
 * The ModelOperationalState model module.
 * @module model/ModelOperationalState
 * @version 2019-09-30
 */
class ModelOperationalState {
    /**
     * Constructs a new <code>ModelOperationalState</code>.
     * The operational state of the Model.
     * @alias module:model/ModelOperationalState
     */
    constructor() { 
        
        ModelOperationalState.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ModelOperationalState</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ModelOperationalState} obj Optional instance to populate.
     * @return {module:model/ModelOperationalState} The populated <code>ModelOperationalState</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ModelOperationalState();

            if (data.hasOwnProperty('deploymentSummary')) {
                obj['deploymentSummary'] = DeploymentSummary.constructFromObject(data['deploymentSummary']);
            }
            if (data.hasOwnProperty('endTime')) {
                obj['endTime'] = ApiClient.convertToType(data['endTime'], 'String');
            }
            if (data.hasOwnProperty('startTime')) {
                obj['startTime'] = ApiClient.convertToType(data['startTime'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ModelOperationalState</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ModelOperationalState</code>.
     */
    static validateJSON(data) {
        // validate the optional field `deploymentSummary`
        if (data['deploymentSummary']) { // data not null
          DeploymentSummary.validateJSON(data['deploymentSummary']);
        }
        // ensure the json data is a string
        if (data['endTime'] && !(typeof data['endTime'] === 'string' || data['endTime'] instanceof String)) {
            throw new Error("Expected the field `endTime` to be a primitive type in the JSON string but got " + data['endTime']);
        }
        // ensure the json data is a string
        if (data['startTime'] && !(typeof data['startTime'] === 'string' || data['startTime'] instanceof String)) {
            throw new Error("Expected the field `startTime` to be a primitive type in the JSON string but got " + data['startTime']);
        }

        return true;
    }


}



/**
 * @member {module:model/DeploymentSummary} deploymentSummary
 */
ModelOperationalState.prototype['deploymentSummary'] = undefined;

/**
 * The deployment end time.
 * @member {String} endTime
 */
ModelOperationalState.prototype['endTime'] = undefined;

/**
 * The deployment start time.
 * @member {String} startTime
 */
ModelOperationalState.prototype['startTime'] = undefined;






export default ModelOperationalState;

