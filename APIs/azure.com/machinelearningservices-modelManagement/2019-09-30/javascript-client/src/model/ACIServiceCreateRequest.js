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
import AuthKeys from './AuthKeys';
import ContainerResourceRequirements from './ContainerResourceRequirements';
import CreateServiceRequest from './CreateServiceRequest';
import EnvironmentImageRequest from './EnvironmentImageRequest';
import ModelDataCollection from './ModelDataCollection';

/**
 * The ACIServiceCreateRequest model module.
 * @module model/ACIServiceCreateRequest
 * @version 2019-09-30
 */
class ACIServiceCreateRequest {
    /**
     * Constructs a new <code>ACIServiceCreateRequest</code>.
     * @alias module:model/ACIServiceCreateRequest
     * @extends module:model/CreateServiceRequest
     * @implements module:model/CreateServiceRequest
     * @param computeType {module:model/ACIServiceCreateRequest.ComputeTypeEnum} The compute environment type for the service.
     * @param name {String} The service name.
     */
    constructor(computeType, name) { 
        CreateServiceRequest.initialize(this, computeType, name);
        ACIServiceCreateRequest.initialize(this, computeType, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, computeType, name) { 
        obj['appInsightsEnabled'] = false;
        obj['authEnabled'] = false;
        obj['sslEnabled'] = false;
    }

    /**
     * Constructs a <code>ACIServiceCreateRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ACIServiceCreateRequest} obj Optional instance to populate.
     * @return {module:model/ACIServiceCreateRequest} The populated <code>ACIServiceCreateRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ACIServiceCreateRequest();
            CreateServiceRequest.constructFromObject(data, obj);
            CreateServiceRequest.constructFromObject(data, obj);

            if (data.hasOwnProperty('appInsightsEnabled')) {
                obj['appInsightsEnabled'] = ApiClient.convertToType(data['appInsightsEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('authEnabled')) {
                obj['authEnabled'] = ApiClient.convertToType(data['authEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('cname')) {
                obj['cname'] = ApiClient.convertToType(data['cname'], 'String');
            }
            if (data.hasOwnProperty('containerResourceRequirements')) {
                obj['containerResourceRequirements'] = ContainerResourceRequirements.constructFromObject(data['containerResourceRequirements']);
            }
            if (data.hasOwnProperty('dataCollection')) {
                obj['dataCollection'] = ModelDataCollection.constructFromObject(data['dataCollection']);
            }
            if (data.hasOwnProperty('dnsNameLabel')) {
                obj['dnsNameLabel'] = ApiClient.convertToType(data['dnsNameLabel'], 'String');
            }
            if (data.hasOwnProperty('sslCertificate')) {
                obj['sslCertificate'] = ApiClient.convertToType(data['sslCertificate'], 'String');
            }
            if (data.hasOwnProperty('sslEnabled')) {
                obj['sslEnabled'] = ApiClient.convertToType(data['sslEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('sslKey')) {
                obj['sslKey'] = ApiClient.convertToType(data['sslKey'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ACIServiceCreateRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ACIServiceCreateRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ACIServiceCreateRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['cname'] && !(typeof data['cname'] === 'string' || data['cname'] instanceof String)) {
            throw new Error("Expected the field `cname` to be a primitive type in the JSON string but got " + data['cname']);
        }
        // validate the optional field `containerResourceRequirements`
        if (data['containerResourceRequirements']) { // data not null
          ContainerResourceRequirements.validateJSON(data['containerResourceRequirements']);
        }
        // validate the optional field `dataCollection`
        if (data['dataCollection']) { // data not null
          ModelDataCollection.validateJSON(data['dataCollection']);
        }
        // ensure the json data is a string
        if (data['dnsNameLabel'] && !(typeof data['dnsNameLabel'] === 'string' || data['dnsNameLabel'] instanceof String)) {
            throw new Error("Expected the field `dnsNameLabel` to be a primitive type in the JSON string but got " + data['dnsNameLabel']);
        }
        // ensure the json data is a string
        if (data['sslCertificate'] && !(typeof data['sslCertificate'] === 'string' || data['sslCertificate'] instanceof String)) {
            throw new Error("Expected the field `sslCertificate` to be a primitive type in the JSON string but got " + data['sslCertificate']);
        }
        // ensure the json data is a string
        if (data['sslKey'] && !(typeof data['sslKey'] === 'string' || data['sslKey'] instanceof String)) {
            throw new Error("Expected the field `sslKey` to be a primitive type in the JSON string but got " + data['sslKey']);
        }

        return true;
    }


}

ACIServiceCreateRequest.RequiredProperties = ["computeType", "name"];

/**
 * Whether or not Application Insights is enabled.
 * @member {Boolean} appInsightsEnabled
 * @default false
 */
ACIServiceCreateRequest.prototype['appInsightsEnabled'] = false;

/**
 * Whether or not authentication is enabled on the service.
 * @member {Boolean} authEnabled
 * @default false
 */
ACIServiceCreateRequest.prototype['authEnabled'] = false;

/**
 * The CName for the service.
 * @member {String} cname
 */
ACIServiceCreateRequest.prototype['cname'] = undefined;

/**
 * @member {module:model/ContainerResourceRequirements} containerResourceRequirements
 */
ACIServiceCreateRequest.prototype['containerResourceRequirements'] = undefined;

/**
 * @member {module:model/ModelDataCollection} dataCollection
 */
ACIServiceCreateRequest.prototype['dataCollection'] = undefined;

/**
 * The Dns label for the service.
 * @member {String} dnsNameLabel
 */
ACIServiceCreateRequest.prototype['dnsNameLabel'] = undefined;

/**
 * The SSL certificate to use if SSL is enabled.
 * @member {String} sslCertificate
 */
ACIServiceCreateRequest.prototype['sslCertificate'] = undefined;

/**
 * Whether or not SSL is enabled.
 * @member {Boolean} sslEnabled
 * @default false
 */
ACIServiceCreateRequest.prototype['sslEnabled'] = false;

/**
 * The SSL key for the certificate.
 * @member {String} sslKey
 */
ACIServiceCreateRequest.prototype['sslKey'] = undefined;


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




export default ACIServiceCreateRequest;

