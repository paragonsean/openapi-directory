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
import AKSServiceCreateRequest from './AKSServiceCreateRequest';
import AuthKeys from './AuthKeys';
import CreateServiceRequest from './CreateServiceRequest';
import EnvironmentImageRequest from './EnvironmentImageRequest';

/**
 * The CreateEndpointRequest model module.
 * @module model/CreateEndpointRequest
 * @version 2019-09-30
 */
class CreateEndpointRequest {
    /**
     * Constructs a new <code>CreateEndpointRequest</code>.
     * The request to create an Endpoint in the AKS.
     * @alias module:model/CreateEndpointRequest
     * @extends module:model/CreateServiceRequest
     * @implements module:model/CreateServiceRequest
     * @param computeType {module:model/CreateEndpointRequest.ComputeTypeEnum} The compute environment type for the service.
     * @param name {String} The service name.
     */
    constructor(computeType, name) { 
        CreateServiceRequest.initialize(this, computeType, name);
        CreateEndpointRequest.initialize(this, computeType, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, computeType, name) { 
    }

    /**
     * Constructs a <code>CreateEndpointRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateEndpointRequest} obj Optional instance to populate.
     * @return {module:model/CreateEndpointRequest} The populated <code>CreateEndpointRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateEndpointRequest();
            CreateServiceRequest.constructFromObject(data, obj);
            CreateServiceRequest.constructFromObject(data, obj);

            if (data.hasOwnProperty('aadAuthEnabled')) {
                obj['aadAuthEnabled'] = ApiClient.convertToType(data['aadAuthEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('appInsightsEnabled')) {
                obj['appInsightsEnabled'] = ApiClient.convertToType(data['appInsightsEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('authEnabled')) {
                obj['authEnabled'] = ApiClient.convertToType(data['authEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('computeName')) {
                obj['computeName'] = ApiClient.convertToType(data['computeName'], 'String');
            }
            if (data.hasOwnProperty('namespace')) {
                obj['namespace'] = ApiClient.convertToType(data['namespace'], 'String');
            }
            if (data.hasOwnProperty('variants')) {
                obj['variants'] = ApiClient.convertToType(data['variants'], [AKSServiceCreateRequest]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateEndpointRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateEndpointRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateEndpointRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['computeName'] && !(typeof data['computeName'] === 'string' || data['computeName'] instanceof String)) {
            throw new Error("Expected the field `computeName` to be a primitive type in the JSON string but got " + data['computeName']);
        }
        // ensure the json data is a string
        if (data['namespace'] && !(typeof data['namespace'] === 'string' || data['namespace'] instanceof String)) {
            throw new Error("Expected the field `namespace` to be a primitive type in the JSON string but got " + data['namespace']);
        }
        if (data['variants']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['variants'])) {
                throw new Error("Expected the field `variants` to be an array in the JSON data but got " + data['variants']);
            }
            // validate the optional field `variants` (array)
            for (const item of data['variants']) {
                AKSServiceCreateRequest.validateJSON(item);
            };
        }

        return true;
    }


}

CreateEndpointRequest.RequiredProperties = ["computeType", "name"];

/**
 * Whether or not AAD authentication is enabled.
 * @member {Boolean} aadAuthEnabled
 */
CreateEndpointRequest.prototype['aadAuthEnabled'] = undefined;

/**
 * Whether or not Application Insights is enabled.
 * @member {Boolean} appInsightsEnabled
 */
CreateEndpointRequest.prototype['appInsightsEnabled'] = undefined;

/**
 * Whether or not authentication is enabled.
 * @member {Boolean} authEnabled
 */
CreateEndpointRequest.prototype['authEnabled'] = undefined;

/**
 * The name of the compute resource.
 * @member {String} computeName
 */
CreateEndpointRequest.prototype['computeName'] = undefined;

/**
 * Kubernetes namespace for the service.
 * @member {String} namespace
 */
CreateEndpointRequest.prototype['namespace'] = undefined;

/**
 * The service tag list.
 * @member {Array.<module:model/AKSServiceCreateRequest>} variants
 */
CreateEndpointRequest.prototype['variants'] = undefined;


// Implement CreateServiceRequest interface:
/**
 * The compute environment type for the service.
 * @member {module:model/CreateServiceRequest.ComputeTypeEnum} computeType
 */
CreateServiceRequest.prototype['computeType'] = undefined;
/**
 * The deployment type for the service.
 * @member {module:model/CreateServiceRequest.DeploymentTypeEnum} deploymentType
 */
CreateServiceRequest.prototype['deploymentType'] = undefined;
/**
 * The description of the service.
 * @member {String} description
 */
CreateServiceRequest.prototype['description'] = undefined;
/**
 * @member {module:model/EnvironmentImageRequest} environmentImageRequest
 */
CreateServiceRequest.prototype['environmentImageRequest'] = undefined;
/**
 * The Image Id.
 * @member {String} imageId
 */
CreateServiceRequest.prototype['imageId'] = undefined;
/**
 * @member {module:model/AuthKeys} keys
 */
CreateServiceRequest.prototype['keys'] = undefined;
/**
 * The service tag dictionary. Tags are mutable.
 * @member {Object.<String, String>} kvTags
 */
CreateServiceRequest.prototype['kvTags'] = undefined;
/**
 * The location of the service.
 * @member {String} location
 */
CreateServiceRequest.prototype['location'] = undefined;
/**
 * The service name.
 * @member {String} name
 */
CreateServiceRequest.prototype['name'] = undefined;
/**
 * The service properties dictionary. Properties are immutable.
 * @member {Object.<String, String>} properties
 */
CreateServiceRequest.prototype['properties'] = undefined;




export default CreateEndpointRequest;

