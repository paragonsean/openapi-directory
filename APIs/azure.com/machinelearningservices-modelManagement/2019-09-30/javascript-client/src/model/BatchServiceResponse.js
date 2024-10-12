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
import ModelDataCollection from './ModelDataCollection';
import ModelErrorResponse from './ModelErrorResponse';
import ServiceResponseBase from './ServiceResponseBase';

/**
 * The BatchServiceResponse model module.
 * @module model/BatchServiceResponse
 * @version 2019-09-30
 */
class BatchServiceResponse {
    /**
     * Constructs a new <code>BatchServiceResponse</code>.
     * @alias module:model/BatchServiceResponse
     * @extends module:model/ServiceResponseBase
     * @implements module:model/ServiceResponseBase
     * @param computeType {module:model/BatchServiceResponse.ComputeTypeEnum} The compute environment type for the service.
     */
    constructor(computeType) { 
        ServiceResponseBase.initialize(this, computeType);
        BatchServiceResponse.initialize(this, computeType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, computeType) { 
    }

    /**
     * Constructs a <code>BatchServiceResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BatchServiceResponse} obj Optional instance to populate.
     * @return {module:model/BatchServiceResponse} The populated <code>BatchServiceResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BatchServiceResponse();
            ServiceResponseBase.constructFromObject(data, obj);
            ServiceResponseBase.constructFromObject(data, obj);

            if (data.hasOwnProperty('appInsightsEnabled')) {
                obj['appInsightsEnabled'] = ApiClient.convertToType(data['appInsightsEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('computeName')) {
                obj['computeName'] = ApiClient.convertToType(data['computeName'], 'String');
            }
            if (data.hasOwnProperty('entryScript')) {
                obj['entryScript'] = ApiClient.convertToType(data['entryScript'], 'String');
            }
            if (data.hasOwnProperty('environmentName')) {
                obj['environmentName'] = ApiClient.convertToType(data['environmentName'], 'String');
            }
            if (data.hasOwnProperty('environmentVersion')) {
                obj['environmentVersion'] = ApiClient.convertToType(data['environmentVersion'], 'String');
            }
            if (data.hasOwnProperty('errorThreshold')) {
                obj['errorThreshold'] = ApiClient.convertToType(data['errorThreshold'], 'Number');
            }
            if (data.hasOwnProperty('inputFormat')) {
                obj['inputFormat'] = ApiClient.convertToType(data['inputFormat'], 'String');
            }
            if (data.hasOwnProperty('miniBatchSize')) {
                obj['miniBatchSize'] = ApiClient.convertToType(data['miniBatchSize'], 'Number');
            }
            if (data.hasOwnProperty('modelDataCollection')) {
                obj['modelDataCollection'] = ModelDataCollection.constructFromObject(data['modelDataCollection']);
            }
            if (data.hasOwnProperty('modelIds')) {
                obj['modelIds'] = ApiClient.convertToType(data['modelIds'], ['String']);
            }
            if (data.hasOwnProperty('nodeCount')) {
                obj['nodeCount'] = ApiClient.convertToType(data['nodeCount'], 'Number');
            }
            if (data.hasOwnProperty('outputAction')) {
                obj['outputAction'] = ApiClient.convertToType(data['outputAction'], 'String');
            }
            if (data.hasOwnProperty('processCountPerNode')) {
                obj['processCountPerNode'] = ApiClient.convertToType(data['processCountPerNode'], 'Number');
            }
            if (data.hasOwnProperty('scoringUri')) {
                obj['scoringUri'] = ApiClient.convertToType(data['scoringUri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BatchServiceResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BatchServiceResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BatchServiceResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['computeName'] && !(typeof data['computeName'] === 'string' || data['computeName'] instanceof String)) {
            throw new Error("Expected the field `computeName` to be a primitive type in the JSON string but got " + data['computeName']);
        }
        // ensure the json data is a string
        if (data['entryScript'] && !(typeof data['entryScript'] === 'string' || data['entryScript'] instanceof String)) {
            throw new Error("Expected the field `entryScript` to be a primitive type in the JSON string but got " + data['entryScript']);
        }
        // ensure the json data is a string
        if (data['environmentName'] && !(typeof data['environmentName'] === 'string' || data['environmentName'] instanceof String)) {
            throw new Error("Expected the field `environmentName` to be a primitive type in the JSON string but got " + data['environmentName']);
        }
        // ensure the json data is a string
        if (data['environmentVersion'] && !(typeof data['environmentVersion'] === 'string' || data['environmentVersion'] instanceof String)) {
            throw new Error("Expected the field `environmentVersion` to be a primitive type in the JSON string but got " + data['environmentVersion']);
        }
        // ensure the json data is a string
        if (data['inputFormat'] && !(typeof data['inputFormat'] === 'string' || data['inputFormat'] instanceof String)) {
            throw new Error("Expected the field `inputFormat` to be a primitive type in the JSON string but got " + data['inputFormat']);
        }
        // validate the optional field `modelDataCollection`
        if (data['modelDataCollection']) { // data not null
          ModelDataCollection.validateJSON(data['modelDataCollection']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['modelIds'])) {
            throw new Error("Expected the field `modelIds` to be an array in the JSON data but got " + data['modelIds']);
        }
        // ensure the json data is a string
        if (data['outputAction'] && !(typeof data['outputAction'] === 'string' || data['outputAction'] instanceof String)) {
            throw new Error("Expected the field `outputAction` to be a primitive type in the JSON string but got " + data['outputAction']);
        }
        // ensure the json data is a string
        if (data['scoringUri'] && !(typeof data['scoringUri'] === 'string' || data['scoringUri'] instanceof String)) {
            throw new Error("Expected the field `scoringUri` to be a primitive type in the JSON string but got " + data['scoringUri']);
        }

        return true;
    }


}

BatchServiceResponse.RequiredProperties = ["computeType"];

/**
 * @member {Boolean} appInsightsEnabled
 */
BatchServiceResponse.prototype['appInsightsEnabled'] = undefined;

/**
 * @member {String} computeName
 */
BatchServiceResponse.prototype['computeName'] = undefined;

/**
 * @member {String} entryScript
 */
BatchServiceResponse.prototype['entryScript'] = undefined;

/**
 * @member {String} environmentName
 */
BatchServiceResponse.prototype['environmentName'] = undefined;

/**
 * @member {String} environmentVersion
 */
BatchServiceResponse.prototype['environmentVersion'] = undefined;

/**
 * @member {Number} errorThreshold
 */
BatchServiceResponse.prototype['errorThreshold'] = undefined;

/**
 * @member {String} inputFormat
 */
BatchServiceResponse.prototype['inputFormat'] = undefined;

/**
 * @member {Number} miniBatchSize
 */
BatchServiceResponse.prototype['miniBatchSize'] = undefined;

/**
 * @member {module:model/ModelDataCollection} modelDataCollection
 */
BatchServiceResponse.prototype['modelDataCollection'] = undefined;

/**
 * @member {Array.<String>} modelIds
 */
BatchServiceResponse.prototype['modelIds'] = undefined;

/**
 * @member {Number} nodeCount
 */
BatchServiceResponse.prototype['nodeCount'] = undefined;

/**
 * @member {String} outputAction
 */
BatchServiceResponse.prototype['outputAction'] = undefined;

/**
 * @member {Number} processCountPerNode
 */
BatchServiceResponse.prototype['processCountPerNode'] = undefined;

/**
 * @member {String} scoringUri
 */
BatchServiceResponse.prototype['scoringUri'] = undefined;


// Implement ServiceResponseBase interface:
/**
 * The compute environment type for the service.
 * @member {module:model/ServiceResponseBase.ComputeTypeEnum} computeType
 */
ServiceResponseBase.prototype['computeType'] = undefined;
/**
 * The time the service was created.
 * @member {Date} createdTime
 */
ServiceResponseBase.prototype['createdTime'] = undefined;
/**
 * The deployment type for the service.
 * @member {module:model/ServiceResponseBase.DeploymentTypeEnum} deploymentType
 */
ServiceResponseBase.prototype['deploymentType'] = undefined;
/**
 * The service description.
 * @member {String} description
 */
ServiceResponseBase.prototype['description'] = undefined;
/**
 * @member {module:model/ModelErrorResponse} error
 */
ServiceResponseBase.prototype['error'] = undefined;
/**
 * The service Id.
 * @member {String} id
 */
ServiceResponseBase.prototype['id'] = undefined;
/**
 * The service tag dictionary. Tags are mutable.
 * @member {Object.<String, String>} kvTags
 */
ServiceResponseBase.prototype['kvTags'] = undefined;
/**
 * The service name.
 * @member {String} name
 */
ServiceResponseBase.prototype['name'] = undefined;
/**
 * The ID of the latest asynchronous operation for this service.
 * @member {String} operationId
 */
ServiceResponseBase.prototype['operationId'] = undefined;
/**
 * The service property dictionary. Properties are immutable.
 * @member {Object.<String, String>} properties
 */
ServiceResponseBase.prototype['properties'] = undefined;
/**
 * The current state of the service.
 * @member {module:model/ServiceResponseBase.StateEnum} state
 */
ServiceResponseBase.prototype['state'] = undefined;
/**
 * The time the service was updated.
 * @member {Date} updatedTime
 */
ServiceResponseBase.prototype['updatedTime'] = undefined;




export default BatchServiceResponse;

