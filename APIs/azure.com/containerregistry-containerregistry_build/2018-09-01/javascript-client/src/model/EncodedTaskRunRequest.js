/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-09-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AgentProperties from './AgentProperties';
import Credentials from './Credentials';
import PlatformProperties from './PlatformProperties';
import RunRequest from './RunRequest';
import SetValue from './SetValue';

/**
 * The EncodedTaskRunRequest model module.
 * @module model/EncodedTaskRunRequest
 * @version 2018-09-01
 */
class EncodedTaskRunRequest {
    /**
     * Constructs a new <code>EncodedTaskRunRequest</code>.
     * The parameters for a quick task run request.
     * @alias module:model/EncodedTaskRunRequest
     * @extends module:model/RunRequest
     * @implements module:model/RunRequest
     */
    constructor() { 
        RunRequest.initialize(this);
        EncodedTaskRunRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['encodedTaskContent'] = encodedTaskContent;
        obj['platform'] = platform;
        obj['timeout'] = 3600;
    }

    /**
     * Constructs a <code>EncodedTaskRunRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EncodedTaskRunRequest} obj Optional instance to populate.
     * @return {module:model/EncodedTaskRunRequest} The populated <code>EncodedTaskRunRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EncodedTaskRunRequest();
            RunRequest.constructFromObject(data, obj);
            RunRequest.constructFromObject(data, obj);

            if (data.hasOwnProperty('agentConfiguration')) {
                obj['agentConfiguration'] = AgentProperties.constructFromObject(data['agentConfiguration']);
            }
            if (data.hasOwnProperty('credentials')) {
                obj['credentials'] = Credentials.constructFromObject(data['credentials']);
            }
            if (data.hasOwnProperty('encodedTaskContent')) {
                obj['encodedTaskContent'] = ApiClient.convertToType(data['encodedTaskContent'], 'String');
            }
            if (data.hasOwnProperty('encodedValuesContent')) {
                obj['encodedValuesContent'] = ApiClient.convertToType(data['encodedValuesContent'], 'String');
            }
            if (data.hasOwnProperty('platform')) {
                obj['platform'] = PlatformProperties.constructFromObject(data['platform']);
            }
            if (data.hasOwnProperty('sourceLocation')) {
                obj['sourceLocation'] = ApiClient.convertToType(data['sourceLocation'], 'String');
            }
            if (data.hasOwnProperty('timeout')) {
                obj['timeout'] = ApiClient.convertToType(data['timeout'], 'Number');
            }
            if (data.hasOwnProperty('values')) {
                obj['values'] = ApiClient.convertToType(data['values'], [SetValue]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EncodedTaskRunRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EncodedTaskRunRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EncodedTaskRunRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `agentConfiguration`
        if (data['agentConfiguration']) { // data not null
          AgentProperties.validateJSON(data['agentConfiguration']);
        }
        // validate the optional field `credentials`
        if (data['credentials']) { // data not null
          Credentials.validateJSON(data['credentials']);
        }
        // ensure the json data is a string
        if (data['encodedTaskContent'] && !(typeof data['encodedTaskContent'] === 'string' || data['encodedTaskContent'] instanceof String)) {
            throw new Error("Expected the field `encodedTaskContent` to be a primitive type in the JSON string but got " + data['encodedTaskContent']);
        }
        // ensure the json data is a string
        if (data['encodedValuesContent'] && !(typeof data['encodedValuesContent'] === 'string' || data['encodedValuesContent'] instanceof String)) {
            throw new Error("Expected the field `encodedValuesContent` to be a primitive type in the JSON string but got " + data['encodedValuesContent']);
        }
        // validate the optional field `platform`
        if (data['platform']) { // data not null
          PlatformProperties.validateJSON(data['platform']);
        }
        // ensure the json data is a string
        if (data['sourceLocation'] && !(typeof data['sourceLocation'] === 'string' || data['sourceLocation'] instanceof String)) {
            throw new Error("Expected the field `sourceLocation` to be a primitive type in the JSON string but got " + data['sourceLocation']);
        }
        if (data['values']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['values'])) {
                throw new Error("Expected the field `values` to be an array in the JSON data but got " + data['values']);
            }
            // validate the optional field `values` (array)
            for (const item of data['values']) {
                SetValue.validateJSON(item);
            };
        }

        return true;
    }


}

EncodedTaskRunRequest.RequiredProperties = ["encodedTaskContent", "platform"];

/**
 * @member {module:model/AgentProperties} agentConfiguration
 */
EncodedTaskRunRequest.prototype['agentConfiguration'] = undefined;

/**
 * @member {module:model/Credentials} credentials
 */
EncodedTaskRunRequest.prototype['credentials'] = undefined;

/**
 * Base64 encoded value of the template/definition file content.
 * @member {String} encodedTaskContent
 */
EncodedTaskRunRequest.prototype['encodedTaskContent'] = undefined;

/**
 * Base64 encoded value of the parameters/values file content.
 * @member {String} encodedValuesContent
 */
EncodedTaskRunRequest.prototype['encodedValuesContent'] = undefined;

/**
 * @member {module:model/PlatformProperties} platform
 */
EncodedTaskRunRequest.prototype['platform'] = undefined;

/**
 * The URL(absolute or relative) of the source context. It can be an URL to a tar or git repository.  If it is relative URL, the relative path should be obtained from calling listBuildSourceUploadUrl API.
 * @member {String} sourceLocation
 */
EncodedTaskRunRequest.prototype['sourceLocation'] = undefined;

/**
 * Run timeout in seconds.
 * @member {Number} timeout
 * @default 3600
 */
EncodedTaskRunRequest.prototype['timeout'] = 3600;

/**
 * The collection of overridable values that can be passed when running a task.
 * @member {Array.<module:model/SetValue>} values
 */
EncodedTaskRunRequest.prototype['values'] = undefined;


// Implement RunRequest interface:
/**
 * The value that indicates whether archiving is enabled for the run or not.
 * @member {Boolean} isArchiveEnabled
 * @default false
 */
RunRequest.prototype['isArchiveEnabled'] = false;
/**
 * The type of the run request.
 * @member {String} type
 */
RunRequest.prototype['type'] = undefined;




export default EncodedTaskRunRequest;

