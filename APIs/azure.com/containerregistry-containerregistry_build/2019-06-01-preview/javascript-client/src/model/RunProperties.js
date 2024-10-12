/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AgentProperties from './AgentProperties';
import ImageDescriptor from './ImageDescriptor';
import ImageUpdateTrigger from './ImageUpdateTrigger';
import PlatformProperties from './PlatformProperties';
import SourceTriggerDescriptor from './SourceTriggerDescriptor';
import TimerTriggerDescriptor from './TimerTriggerDescriptor';

/**
 * The RunProperties model module.
 * @module model/RunProperties
 * @version 2019-06-01-preview
 */
class RunProperties {
    /**
     * Constructs a new <code>RunProperties</code>.
     * The properties for a run.
     * @alias module:model/RunProperties
     */
    constructor() { 
        
        RunProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['isArchiveEnabled'] = false;
    }

    /**
     * Constructs a <code>RunProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RunProperties} obj Optional instance to populate.
     * @return {module:model/RunProperties} The populated <code>RunProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RunProperties();

            if (data.hasOwnProperty('agentConfiguration')) {
                obj['agentConfiguration'] = AgentProperties.constructFromObject(data['agentConfiguration']);
            }
            if (data.hasOwnProperty('createTime')) {
                obj['createTime'] = ApiClient.convertToType(data['createTime'], 'Date');
            }
            if (data.hasOwnProperty('customRegistries')) {
                obj['customRegistries'] = ApiClient.convertToType(data['customRegistries'], ['String']);
            }
            if (data.hasOwnProperty('finishTime')) {
                obj['finishTime'] = ApiClient.convertToType(data['finishTime'], 'Date');
            }
            if (data.hasOwnProperty('imageUpdateTrigger')) {
                obj['imageUpdateTrigger'] = ImageUpdateTrigger.constructFromObject(data['imageUpdateTrigger']);
            }
            if (data.hasOwnProperty('isArchiveEnabled')) {
                obj['isArchiveEnabled'] = ApiClient.convertToType(data['isArchiveEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('lastUpdatedTime')) {
                obj['lastUpdatedTime'] = ApiClient.convertToType(data['lastUpdatedTime'], 'Date');
            }
            if (data.hasOwnProperty('outputImages')) {
                obj['outputImages'] = ApiClient.convertToType(data['outputImages'], [ImageDescriptor]);
            }
            if (data.hasOwnProperty('platform')) {
                obj['platform'] = PlatformProperties.constructFromObject(data['platform']);
            }
            if (data.hasOwnProperty('provisioningState')) {
                obj['provisioningState'] = ApiClient.convertToType(data['provisioningState'], 'String');
            }
            if (data.hasOwnProperty('runErrorMessage')) {
                obj['runErrorMessage'] = ApiClient.convertToType(data['runErrorMessage'], 'String');
            }
            if (data.hasOwnProperty('runId')) {
                obj['runId'] = ApiClient.convertToType(data['runId'], 'String');
            }
            if (data.hasOwnProperty('runType')) {
                obj['runType'] = ApiClient.convertToType(data['runType'], 'String');
            }
            if (data.hasOwnProperty('sourceRegistryAuth')) {
                obj['sourceRegistryAuth'] = ApiClient.convertToType(data['sourceRegistryAuth'], 'String');
            }
            if (data.hasOwnProperty('sourceTrigger')) {
                obj['sourceTrigger'] = SourceTriggerDescriptor.constructFromObject(data['sourceTrigger']);
            }
            if (data.hasOwnProperty('startTime')) {
                obj['startTime'] = ApiClient.convertToType(data['startTime'], 'Date');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('task')) {
                obj['task'] = ApiClient.convertToType(data['task'], 'String');
            }
            if (data.hasOwnProperty('timerTrigger')) {
                obj['timerTrigger'] = TimerTriggerDescriptor.constructFromObject(data['timerTrigger']);
            }
            if (data.hasOwnProperty('updateTriggerToken')) {
                obj['updateTriggerToken'] = ApiClient.convertToType(data['updateTriggerToken'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RunProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RunProperties</code>.
     */
    static validateJSON(data) {
        // validate the optional field `agentConfiguration`
        if (data['agentConfiguration']) { // data not null
          AgentProperties.validateJSON(data['agentConfiguration']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['customRegistries'])) {
            throw new Error("Expected the field `customRegistries` to be an array in the JSON data but got " + data['customRegistries']);
        }
        // validate the optional field `imageUpdateTrigger`
        if (data['imageUpdateTrigger']) { // data not null
          ImageUpdateTrigger.validateJSON(data['imageUpdateTrigger']);
        }
        if (data['outputImages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['outputImages'])) {
                throw new Error("Expected the field `outputImages` to be an array in the JSON data but got " + data['outputImages']);
            }
            // validate the optional field `outputImages` (array)
            for (const item of data['outputImages']) {
                ImageDescriptor.validateJSON(item);
            };
        }
        // validate the optional field `platform`
        if (data['platform']) { // data not null
          PlatformProperties.validateJSON(data['platform']);
        }
        // ensure the json data is a string
        if (data['provisioningState'] && !(typeof data['provisioningState'] === 'string' || data['provisioningState'] instanceof String)) {
            throw new Error("Expected the field `provisioningState` to be a primitive type in the JSON string but got " + data['provisioningState']);
        }
        // ensure the json data is a string
        if (data['runErrorMessage'] && !(typeof data['runErrorMessage'] === 'string' || data['runErrorMessage'] instanceof String)) {
            throw new Error("Expected the field `runErrorMessage` to be a primitive type in the JSON string but got " + data['runErrorMessage']);
        }
        // ensure the json data is a string
        if (data['runId'] && !(typeof data['runId'] === 'string' || data['runId'] instanceof String)) {
            throw new Error("Expected the field `runId` to be a primitive type in the JSON string but got " + data['runId']);
        }
        // ensure the json data is a string
        if (data['runType'] && !(typeof data['runType'] === 'string' || data['runType'] instanceof String)) {
            throw new Error("Expected the field `runType` to be a primitive type in the JSON string but got " + data['runType']);
        }
        // ensure the json data is a string
        if (data['sourceRegistryAuth'] && !(typeof data['sourceRegistryAuth'] === 'string' || data['sourceRegistryAuth'] instanceof String)) {
            throw new Error("Expected the field `sourceRegistryAuth` to be a primitive type in the JSON string but got " + data['sourceRegistryAuth']);
        }
        // validate the optional field `sourceTrigger`
        if (data['sourceTrigger']) { // data not null
          SourceTriggerDescriptor.validateJSON(data['sourceTrigger']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['task'] && !(typeof data['task'] === 'string' || data['task'] instanceof String)) {
            throw new Error("Expected the field `task` to be a primitive type in the JSON string but got " + data['task']);
        }
        // validate the optional field `timerTrigger`
        if (data['timerTrigger']) { // data not null
          TimerTriggerDescriptor.validateJSON(data['timerTrigger']);
        }
        // ensure the json data is a string
        if (data['updateTriggerToken'] && !(typeof data['updateTriggerToken'] === 'string' || data['updateTriggerToken'] instanceof String)) {
            throw new Error("Expected the field `updateTriggerToken` to be a primitive type in the JSON string but got " + data['updateTriggerToken']);
        }

        return true;
    }


}



/**
 * @member {module:model/AgentProperties} agentConfiguration
 */
RunProperties.prototype['agentConfiguration'] = undefined;

/**
 * The time the run was scheduled.
 * @member {Date} createTime
 */
RunProperties.prototype['createTime'] = undefined;

/**
 * The list of custom registries that were logged in during this run.
 * @member {Array.<String>} customRegistries
 */
RunProperties.prototype['customRegistries'] = undefined;

/**
 * The time the run finished.
 * @member {Date} finishTime
 */
RunProperties.prototype['finishTime'] = undefined;

/**
 * @member {module:model/ImageUpdateTrigger} imageUpdateTrigger
 */
RunProperties.prototype['imageUpdateTrigger'] = undefined;

/**
 * The value that indicates whether archiving is enabled or not.
 * @member {Boolean} isArchiveEnabled
 * @default false
 */
RunProperties.prototype['isArchiveEnabled'] = false;

/**
 * The last updated time for the run.
 * @member {Date} lastUpdatedTime
 */
RunProperties.prototype['lastUpdatedTime'] = undefined;

/**
 * The list of all images that were generated from the run. This is applicable if the run generates base image dependencies.
 * @member {Array.<module:model/ImageDescriptor>} outputImages
 */
RunProperties.prototype['outputImages'] = undefined;

/**
 * @member {module:model/PlatformProperties} platform
 */
RunProperties.prototype['platform'] = undefined;

/**
 * The provisioning state of a run.
 * @member {module:model/RunProperties.ProvisioningStateEnum} provisioningState
 */
RunProperties.prototype['provisioningState'] = undefined;

/**
 * The error message received from backend systems after the run is scheduled.
 * @member {String} runErrorMessage
 */
RunProperties.prototype['runErrorMessage'] = undefined;

/**
 * The unique identifier for the run.
 * @member {String} runId
 */
RunProperties.prototype['runId'] = undefined;

/**
 * The type of run.
 * @member {module:model/RunProperties.RunTypeEnum} runType
 */
RunProperties.prototype['runType'] = undefined;

/**
 * The scope of the credentials that were used to login to the source registry during this run.
 * @member {String} sourceRegistryAuth
 */
RunProperties.prototype['sourceRegistryAuth'] = undefined;

/**
 * @member {module:model/SourceTriggerDescriptor} sourceTrigger
 */
RunProperties.prototype['sourceTrigger'] = undefined;

/**
 * The time the run started.
 * @member {Date} startTime
 */
RunProperties.prototype['startTime'] = undefined;

/**
 * The current status of the run.
 * @member {module:model/RunProperties.StatusEnum} status
 */
RunProperties.prototype['status'] = undefined;

/**
 * The task against which run was scheduled.
 * @member {String} task
 */
RunProperties.prototype['task'] = undefined;

/**
 * @member {module:model/TimerTriggerDescriptor} timerTrigger
 */
RunProperties.prototype['timerTrigger'] = undefined;

/**
 * The update trigger token passed for the Run.
 * @member {String} updateTriggerToken
 */
RunProperties.prototype['updateTriggerToken'] = undefined;





/**
 * Allowed values for the <code>provisioningState</code> property.
 * @enum {String}
 * @readonly
 */
RunProperties['ProvisioningStateEnum'] = {

    /**
     * value: "Creating"
     * @const
     */
    "Creating": "Creating",

    /**
     * value: "Updating"
     * @const
     */
    "Updating": "Updating",

    /**
     * value: "Deleting"
     * @const
     */
    "Deleting": "Deleting",

    /**
     * value: "Succeeded"
     * @const
     */
    "Succeeded": "Succeeded",

    /**
     * value: "Failed"
     * @const
     */
    "Failed": "Failed",

    /**
     * value: "Canceled"
     * @const
     */
    "Canceled": "Canceled"
};


/**
 * Allowed values for the <code>runType</code> property.
 * @enum {String}
 * @readonly
 */
RunProperties['RunTypeEnum'] = {

    /**
     * value: "QuickBuild"
     * @const
     */
    "QuickBuild": "QuickBuild",

    /**
     * value: "QuickRun"
     * @const
     */
    "QuickRun": "QuickRun",

    /**
     * value: "AutoBuild"
     * @const
     */
    "AutoBuild": "AutoBuild",

    /**
     * value: "AutoRun"
     * @const
     */
    "AutoRun": "AutoRun"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
RunProperties['StatusEnum'] = {

    /**
     * value: "Queued"
     * @const
     */
    "Queued": "Queued",

    /**
     * value: "Started"
     * @const
     */
    "Started": "Started",

    /**
     * value: "Running"
     * @const
     */
    "Running": "Running",

    /**
     * value: "Succeeded"
     * @const
     */
    "Succeeded": "Succeeded",

    /**
     * value: "Failed"
     * @const
     */
    "Failed": "Failed",

    /**
     * value: "Canceled"
     * @const
     */
    "Canceled": "Canceled",

    /**
     * value: "Error"
     * @const
     */
    "Error": "Error",

    /**
     * value: "Timeout"
     * @const
     */
    "Timeout": "Timeout"
};



export default RunProperties;

