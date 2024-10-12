/**
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2019-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import OrchestratorProfile from './OrchestratorProfile';

/**
 * The OrchestratorVersionProfile model module.
 * @module model/OrchestratorVersionProfile
 * @version 2019-06-01
 */
class OrchestratorVersionProfile {
    /**
     * Constructs a new <code>OrchestratorVersionProfile</code>.
     * The profile of an orchestrator and its available versions.
     * @alias module:model/OrchestratorVersionProfile
     * @param orchestratorType {String} Orchestrator type.
     * @param orchestratorVersion {String} Orchestrator version (major, minor, patch).
     */
    constructor(orchestratorType, orchestratorVersion) { 
        
        OrchestratorVersionProfile.initialize(this, orchestratorType, orchestratorVersion);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, orchestratorType, orchestratorVersion) { 
        obj['orchestratorType'] = orchestratorType;
        obj['orchestratorVersion'] = orchestratorVersion;
    }

    /**
     * Constructs a <code>OrchestratorVersionProfile</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrchestratorVersionProfile} obj Optional instance to populate.
     * @return {module:model/OrchestratorVersionProfile} The populated <code>OrchestratorVersionProfile</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrchestratorVersionProfile();

            if (data.hasOwnProperty('default')) {
                obj['default'] = ApiClient.convertToType(data['default'], 'Boolean');
            }
            if (data.hasOwnProperty('isPreview')) {
                obj['isPreview'] = ApiClient.convertToType(data['isPreview'], 'Boolean');
            }
            if (data.hasOwnProperty('orchestratorType')) {
                obj['orchestratorType'] = ApiClient.convertToType(data['orchestratorType'], 'String');
            }
            if (data.hasOwnProperty('orchestratorVersion')) {
                obj['orchestratorVersion'] = ApiClient.convertToType(data['orchestratorVersion'], 'String');
            }
            if (data.hasOwnProperty('upgrades')) {
                obj['upgrades'] = ApiClient.convertToType(data['upgrades'], [OrchestratorProfile]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrchestratorVersionProfile</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrchestratorVersionProfile</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrchestratorVersionProfile.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['orchestratorType'] && !(typeof data['orchestratorType'] === 'string' || data['orchestratorType'] instanceof String)) {
            throw new Error("Expected the field `orchestratorType` to be a primitive type in the JSON string but got " + data['orchestratorType']);
        }
        // ensure the json data is a string
        if (data['orchestratorVersion'] && !(typeof data['orchestratorVersion'] === 'string' || data['orchestratorVersion'] instanceof String)) {
            throw new Error("Expected the field `orchestratorVersion` to be a primitive type in the JSON string but got " + data['orchestratorVersion']);
        }
        if (data['upgrades']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['upgrades'])) {
                throw new Error("Expected the field `upgrades` to be an array in the JSON data but got " + data['upgrades']);
            }
            // validate the optional field `upgrades` (array)
            for (const item of data['upgrades']) {
                OrchestratorProfile.validateJSON(item);
            };
        }

        return true;
    }


}

OrchestratorVersionProfile.RequiredProperties = ["orchestratorType", "orchestratorVersion"];

/**
 * Installed by default if version is not specified.
 * @member {Boolean} default
 */
OrchestratorVersionProfile.prototype['default'] = undefined;

/**
 * Whether Kubernetes version is currently in preview.
 * @member {Boolean} isPreview
 */
OrchestratorVersionProfile.prototype['isPreview'] = undefined;

/**
 * Orchestrator type.
 * @member {String} orchestratorType
 */
OrchestratorVersionProfile.prototype['orchestratorType'] = undefined;

/**
 * Orchestrator version (major, minor, patch).
 * @member {String} orchestratorVersion
 */
OrchestratorVersionProfile.prototype['orchestratorVersion'] = undefined;

/**
 * The list of available upgrade versions.
 * @member {Array.<module:model/OrchestratorProfile>} upgrades
 */
OrchestratorVersionProfile.prototype['upgrades'] = undefined;






export default OrchestratorVersionProfile;

