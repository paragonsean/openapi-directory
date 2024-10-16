/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BuildSystemSharedDTOAgentStatus from './BuildSystemSharedDTOAgentStatus';
import BuildSystemSharedDTOStepConfiguration from './BuildSystemSharedDTOStepConfiguration';

/**
 * The BuildSystemSharedDTOAgent model module.
 * @module model/BuildSystemSharedDTOAgent
 * @version v1
 */
class BuildSystemSharedDTOAgent {
    /**
     * Constructs a new <code>BuildSystemSharedDTOAgent</code>.
     * A DTO for an IAgent
     * @alias module:model/BuildSystemSharedDTOAgent
     * @param keepAliveInterval {Number} The 'Heartbeat Interval' used by the Build Agent.
     * @param machineName {String} The machine name of the computer the agent is running on
     * @param status {module:model/BuildSystemSharedDTOAgentStatus} 
     * @param userID {Number} The UserID of the Agent
     */
    constructor(keepAliveInterval, machineName, status, userID) { 
        
        BuildSystemSharedDTOAgent.initialize(this, keepAliveInterval, machineName, status, userID);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, keepAliveInterval, machineName, status, userID) { 
        obj['KeepAliveInterval'] = keepAliveInterval;
        obj['MachineName'] = machineName;
        obj['Status'] = status;
        obj['UserID'] = userID;
    }

    /**
     * Constructs a <code>BuildSystemSharedDTOAgent</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BuildSystemSharedDTOAgent} obj Optional instance to populate.
     * @return {module:model/BuildSystemSharedDTOAgent} The populated <code>BuildSystemSharedDTOAgent</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BuildSystemSharedDTOAgent();

            if (data.hasOwnProperty('AgentID')) {
                obj['AgentID'] = ApiClient.convertToType(data['AgentID'], 'Number');
            }
            if (data.hasOwnProperty('KeepAliveInterval')) {
                obj['KeepAliveInterval'] = ApiClient.convertToType(data['KeepAliveInterval'], 'Number');
            }
            if (data.hasOwnProperty('MachineName')) {
                obj['MachineName'] = ApiClient.convertToType(data['MachineName'], 'String');
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = BuildSystemSharedDTOAgentStatus.constructFromObject(data['Status']);
            }
            if (data.hasOwnProperty('StepConfigurations')) {
                obj['StepConfigurations'] = ApiClient.convertToType(data['StepConfigurations'], [BuildSystemSharedDTOStepConfiguration]);
            }
            if (data.hasOwnProperty('UserID')) {
                obj['UserID'] = ApiClient.convertToType(data['UserID'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BuildSystemSharedDTOAgent</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BuildSystemSharedDTOAgent</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BuildSystemSharedDTOAgent.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['MachineName'] && !(typeof data['MachineName'] === 'string' || data['MachineName'] instanceof String)) {
            throw new Error("Expected the field `MachineName` to be a primitive type in the JSON string but got " + data['MachineName']);
        }
        // validate the optional field `Status`
        if (data['Status']) { // data not null
          BuildSystemSharedDTOAgentStatus.validateJSON(data['Status']);
        }
        if (data['StepConfigurations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['StepConfigurations'])) {
                throw new Error("Expected the field `StepConfigurations` to be an array in the JSON data but got " + data['StepConfigurations']);
            }
            // validate the optional field `StepConfigurations` (array)
            for (const item of data['StepConfigurations']) {
                BuildSystemSharedDTOStepConfiguration.validateJSON(item);
            };
        }

        return true;
    }


}

BuildSystemSharedDTOAgent.RequiredProperties = ["KeepAliveInterval", "MachineName", "Status", "UserID"];

/**
 * The id of the Agent
 * @member {Number} AgentID
 */
BuildSystemSharedDTOAgent.prototype['AgentID'] = undefined;

/**
 * The 'Heartbeat Interval' used by the Build Agent.
 * @member {Number} KeepAliveInterval
 */
BuildSystemSharedDTOAgent.prototype['KeepAliveInterval'] = undefined;

/**
 * The machine name of the computer the agent is running on
 * @member {String} MachineName
 */
BuildSystemSharedDTOAgent.prototype['MachineName'] = undefined;

/**
 * @member {module:model/BuildSystemSharedDTOAgentStatus} Status
 */
BuildSystemSharedDTOAgent.prototype['Status'] = undefined;

/**
 * The agent's step configurations
 * @member {Array.<module:model/BuildSystemSharedDTOStepConfiguration>} StepConfigurations
 */
BuildSystemSharedDTOAgent.prototype['StepConfigurations'] = undefined;

/**
 * The UserID of the Agent
 * @member {Number} UserID
 */
BuildSystemSharedDTOAgent.prototype['UserID'] = undefined;






export default BuildSystemSharedDTOAgent;

