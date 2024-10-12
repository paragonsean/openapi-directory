/**
 * AWS Proton
 * <p>This is the Proton Service API Reference. It provides descriptions, syntax and usage examples for each of the <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Operations.html\">actions</a> and <a href=\"https://docs.aws.amazon.com/proton/latest/APIReference/API_Types.html\">data types</a> for the Proton service.</p> <p>The documentation for each action shows the Query API request parameters and the XML response.</p> <p>Alternatively, you can use the Amazon Web Services CLI to access an API. For more information, see the <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html\">Amazon Web Services Command Line Interface User Guide</a>.</p> <p>The Proton service is a two-pronged automation framework. Administrators create service templates to provide standardized infrastructure and deployment tooling for serverless and container based applications. Developers, in turn, select from the available service templates to automate their application or service deployments.</p> <p>Because administrators define the infrastructure and tooling that Proton deploys and manages, they need permissions to use all of the listed API operations.</p> <p>When developers select a specific infrastructure and tooling set, Proton deploys their applications. To monitor their applications that are running on Proton, developers need permissions to the service <i>create</i>, <i>list</i>, <i>update</i> and <i>delete</i> API operations and the service instance <i>list</i> and <i>update</i> API operations.</p> <p>To learn more about Proton, see the <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html\">Proton User Guide</a>.</p> <p> <b>Ensuring Idempotency</b> </p> <p>When you make a mutating API request, the request typically returns a result before the asynchronous workflows of the operation are complete. Operations might also time out or encounter other server issues before they're complete, even if the request already returned a result. This might make it difficult to determine whether the request succeeded. Moreover, you might need to retry the request multiple times to ensure that the operation completes successfully. However, if the original request and the subsequent retries are successful, the operation occurs multiple times. This means that you might create more resources than you intended.</p> <p> <i>Idempotency</i> ensures that an API request action completes no more than one time. With an idempotent request, if the original request action completes successfully, any subsequent retries complete successfully without performing any further actions. However, the result might contain updated information, such as the current creation status.</p> <p>The following lists of APIs are grouped according to methods that ensure idempotency.</p> <p> <b>Idempotent create APIs with a client token</b> </p> <p>The API actions in this list support idempotency with the use of a <i>client token</i>. The corresponding Amazon Web Services CLI commands also support idempotency using a client token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request using one of these actions, specify a client token in the request. We recommend that you <i>don't</i> reuse the same client token for other API requests. If you don’t provide a client token for these APIs, a default client token is automatically provided by SDKs.</p> <p>Given a request action that has succeeded:</p> <p>If you retry the request using the same client token and the same parameters, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If you retry the request using the same client token, but one or more of the parameters are different, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Client tokens expire eight hours after a request is made. If you retry the request with the expired token, a new resource is created.</p> <p>If the original resource is deleted and you retry the request, a new resource is created.</p> <p>Idempotent create APIs with a client token:</p> <ul> <li> <p>CreateEnvironmentTemplateVersion</p> </li> <li> <p>CreateServiceTemplateVersion</p> </li> <li> <p>CreateEnvironmentAccountConnection</p> </li> </ul> <p> <b>Idempotent create APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, and the original resource <i>hasn't</i> been modified, the retry succeeds without performing any further actions other than returning the original resource detail data in the response.</p> <p>If the original resource has been modified, the retry throws a <code>ConflictException</code>.</p> <p>If you retry with different input parameters, the retry throws a <code>ValidationException</code> with an <code>IdempotentParameterMismatch</code> error.</p> <p>Idempotent create APIs:</p> <ul> <li> <p>CreateEnvironmentTemplate</p> </li> <li> <p>CreateServiceTemplate</p> </li> <li> <p>CreateEnvironment</p> </li> <li> <p>CreateService</p> </li> </ul> <p> <b>Idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>When you retry the request with an API from this group and the resource was deleted, its metadata is returned in the response.</p> <p>If you retry and the resource doesn't exist, the response is empty.</p> <p>In both cases, the retry succeeds.</p> <p>Idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironmentTemplate</p> </li> <li> <p>DeleteEnvironmentTemplateVersion</p> </li> <li> <p>DeleteServiceTemplate</p> </li> <li> <p>DeleteServiceTemplateVersion</p> </li> <li> <p>DeleteEnvironmentAccountConnection</p> </li> </ul> <p> <b>Asynchronous idempotent delete APIs</b> </p> <p>Given a request action that has succeeded:</p> <p>If you retry the request with an API from this group, if the original request delete operation status is <code>DELETE_IN_PROGRESS</code>, the retry returns the resource detail data in the response without performing any further actions.</p> <p>If the original request delete operation is complete, a retry returns an empty response.</p> <p>Asynchronous idempotent delete APIs:</p> <ul> <li> <p>DeleteEnvironment</p> </li> <li> <p>DeleteService</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2020-07-20
 * Contact: mike.ralphson@gmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Deployment from './Deployment';
import DeploymentInitialState from './DeploymentInitialState';
import DeploymentStatus from './DeploymentStatus';
import DeploymentTargetResourceType from './DeploymentTargetResourceType';
import DeploymentTargetState from './DeploymentTargetState';

/**
 * The GetDeploymentOutputDeployment model module.
 * @module model/GetDeploymentOutputDeployment
 * @version 2020-07-20
 */
class GetDeploymentOutputDeployment {
    /**
     * Constructs a new <code>GetDeploymentOutputDeployment</code>.
     * @alias module:model/GetDeploymentOutputDeployment
     * @implements module:model/Deployment
     * @param arn {String} 
     * @param createdAt {Date} 
     * @param deploymentStatus {module:model/DeploymentStatus} 
     * @param environmentName {String} 
     * @param id {String} 
     * @param lastModifiedAt {Date} 
     * @param targetArn {String} 
     * @param targetResourceCreatedAt {Date} 
     * @param targetResourceType {module:model/DeploymentTargetResourceType} 
     */
    constructor(arn, createdAt, deploymentStatus, environmentName, id, lastModifiedAt, targetArn, targetResourceCreatedAt, targetResourceType) { 
        Deployment.initialize(this, arn, createdAt, deploymentStatus, environmentName, id, lastModifiedAt, targetArn, targetResourceCreatedAt, targetResourceType);
        GetDeploymentOutputDeployment.initialize(this, arn, createdAt, deploymentStatus, environmentName, id, lastModifiedAt, targetArn, targetResourceCreatedAt, targetResourceType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, arn, createdAt, deploymentStatus, environmentName, id, lastModifiedAt, targetArn, targetResourceCreatedAt, targetResourceType) { 
        obj['arn'] = arn;
        obj['createdAt'] = createdAt;
        obj['deploymentStatus'] = deploymentStatus;
        obj['environmentName'] = environmentName;
        obj['id'] = id;
        obj['lastModifiedAt'] = lastModifiedAt;
        obj['targetArn'] = targetArn;
        obj['targetResourceCreatedAt'] = targetResourceCreatedAt;
        obj['targetResourceType'] = targetResourceType;
    }

    /**
     * Constructs a <code>GetDeploymentOutputDeployment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetDeploymentOutputDeployment} obj Optional instance to populate.
     * @return {module:model/GetDeploymentOutputDeployment} The populated <code>GetDeploymentOutputDeployment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetDeploymentOutputDeployment();
            Deployment.constructFromObject(data, obj);

            if (data.hasOwnProperty('arn')) {
                obj['arn'] = ApiClient.convertToType(data['arn'], 'String');
            }
            if (data.hasOwnProperty('completedAt')) {
                obj['completedAt'] = ApiClient.convertToType(data['completedAt'], 'Date');
            }
            if (data.hasOwnProperty('componentName')) {
                obj['componentName'] = ApiClient.convertToType(data['componentName'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('deploymentStatus')) {
                obj['deploymentStatus'] = ApiClient.convertToType(data['deploymentStatus'], DeploymentStatus);
            }
            if (data.hasOwnProperty('deploymentStatusMessage')) {
                obj['deploymentStatusMessage'] = ApiClient.convertToType(data['deploymentStatusMessage'], 'String');
            }
            if (data.hasOwnProperty('environmentName')) {
                obj['environmentName'] = ApiClient.convertToType(data['environmentName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('initialState')) {
                obj['initialState'] = DeploymentInitialState.constructFromObject(data['initialState']);
            }
            if (data.hasOwnProperty('lastAttemptedDeploymentId')) {
                obj['lastAttemptedDeploymentId'] = ApiClient.convertToType(data['lastAttemptedDeploymentId'], 'String');
            }
            if (data.hasOwnProperty('lastModifiedAt')) {
                obj['lastModifiedAt'] = ApiClient.convertToType(data['lastModifiedAt'], 'Date');
            }
            if (data.hasOwnProperty('lastSucceededDeploymentId')) {
                obj['lastSucceededDeploymentId'] = ApiClient.convertToType(data['lastSucceededDeploymentId'], 'String');
            }
            if (data.hasOwnProperty('serviceInstanceName')) {
                obj['serviceInstanceName'] = ApiClient.convertToType(data['serviceInstanceName'], 'String');
            }
            if (data.hasOwnProperty('serviceName')) {
                obj['serviceName'] = ApiClient.convertToType(data['serviceName'], 'String');
            }
            if (data.hasOwnProperty('targetArn')) {
                obj['targetArn'] = ApiClient.convertToType(data['targetArn'], 'String');
            }
            if (data.hasOwnProperty('targetResourceCreatedAt')) {
                obj['targetResourceCreatedAt'] = ApiClient.convertToType(data['targetResourceCreatedAt'], 'Date');
            }
            if (data.hasOwnProperty('targetResourceType')) {
                obj['targetResourceType'] = ApiClient.convertToType(data['targetResourceType'], DeploymentTargetResourceType);
            }
            if (data.hasOwnProperty('targetState')) {
                obj['targetState'] = DeploymentTargetState.constructFromObject(data['targetState']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetDeploymentOutputDeployment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetDeploymentOutputDeployment</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of GetDeploymentOutputDeployment.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `arn`
        if (data['arn']) { // data not null
          String.validateJSON(data['arn']);
        }
        // validate the optional field `completedAt`
        if (data['completedAt']) { // data not null
          Date.validateJSON(data['completedAt']);
        }
        // validate the optional field `componentName`
        if (data['componentName']) { // data not null
          String.validateJSON(data['componentName']);
        }
        // validate the optional field `createdAt`
        if (data['createdAt']) { // data not null
          Date.validateJSON(data['createdAt']);
        }
        // validate the optional field `deploymentStatus`
        if (data['deploymentStatus']) { // data not null
          DeploymentStatus.validateJSON(data['deploymentStatus']);
        }
        // validate the optional field `deploymentStatusMessage`
        if (data['deploymentStatusMessage']) { // data not null
          String.validateJSON(data['deploymentStatusMessage']);
        }
        // validate the optional field `environmentName`
        if (data['environmentName']) { // data not null
          String.validateJSON(data['environmentName']);
        }
        // validate the optional field `id`
        if (data['id']) { // data not null
          String.validateJSON(data['id']);
        }
        // validate the optional field `initialState`
        if (data['initialState']) { // data not null
          DeploymentInitialState.validateJSON(data['initialState']);
        }
        // validate the optional field `lastAttemptedDeploymentId`
        if (data['lastAttemptedDeploymentId']) { // data not null
          String.validateJSON(data['lastAttemptedDeploymentId']);
        }
        // validate the optional field `lastModifiedAt`
        if (data['lastModifiedAt']) { // data not null
          Date.validateJSON(data['lastModifiedAt']);
        }
        // validate the optional field `lastSucceededDeploymentId`
        if (data['lastSucceededDeploymentId']) { // data not null
          String.validateJSON(data['lastSucceededDeploymentId']);
        }
        // validate the optional field `serviceInstanceName`
        if (data['serviceInstanceName']) { // data not null
          String.validateJSON(data['serviceInstanceName']);
        }
        // validate the optional field `serviceName`
        if (data['serviceName']) { // data not null
          String.validateJSON(data['serviceName']);
        }
        // validate the optional field `targetArn`
        if (data['targetArn']) { // data not null
          String.validateJSON(data['targetArn']);
        }
        // validate the optional field `targetResourceCreatedAt`
        if (data['targetResourceCreatedAt']) { // data not null
          Date.validateJSON(data['targetResourceCreatedAt']);
        }
        // validate the optional field `targetResourceType`
        if (data['targetResourceType']) { // data not null
          DeploymentTargetResourceType.validateJSON(data['targetResourceType']);
        }
        // validate the optional field `targetState`
        if (data['targetState']) { // data not null
          DeploymentTargetState.validateJSON(data['targetState']);
        }

        return true;
    }


}

GetDeploymentOutputDeployment.RequiredProperties = ["arn", "createdAt", "deploymentStatus", "environmentName", "id", "lastModifiedAt", "targetArn", "targetResourceCreatedAt", "targetResourceType"];

/**
 * @member {String} arn
 */
GetDeploymentOutputDeployment.prototype['arn'] = undefined;

/**
 * @member {Date} completedAt
 */
GetDeploymentOutputDeployment.prototype['completedAt'] = undefined;

/**
 * @member {String} componentName
 */
GetDeploymentOutputDeployment.prototype['componentName'] = undefined;

/**
 * @member {Date} createdAt
 */
GetDeploymentOutputDeployment.prototype['createdAt'] = undefined;

/**
 * @member {module:model/DeploymentStatus} deploymentStatus
 */
GetDeploymentOutputDeployment.prototype['deploymentStatus'] = undefined;

/**
 * @member {String} deploymentStatusMessage
 */
GetDeploymentOutputDeployment.prototype['deploymentStatusMessage'] = undefined;

/**
 * @member {String} environmentName
 */
GetDeploymentOutputDeployment.prototype['environmentName'] = undefined;

/**
 * @member {String} id
 */
GetDeploymentOutputDeployment.prototype['id'] = undefined;

/**
 * @member {module:model/DeploymentInitialState} initialState
 */
GetDeploymentOutputDeployment.prototype['initialState'] = undefined;

/**
 * @member {String} lastAttemptedDeploymentId
 */
GetDeploymentOutputDeployment.prototype['lastAttemptedDeploymentId'] = undefined;

/**
 * @member {Date} lastModifiedAt
 */
GetDeploymentOutputDeployment.prototype['lastModifiedAt'] = undefined;

/**
 * @member {String} lastSucceededDeploymentId
 */
GetDeploymentOutputDeployment.prototype['lastSucceededDeploymentId'] = undefined;

/**
 * @member {String} serviceInstanceName
 */
GetDeploymentOutputDeployment.prototype['serviceInstanceName'] = undefined;

/**
 * @member {String} serviceName
 */
GetDeploymentOutputDeployment.prototype['serviceName'] = undefined;

/**
 * @member {String} targetArn
 */
GetDeploymentOutputDeployment.prototype['targetArn'] = undefined;

/**
 * @member {Date} targetResourceCreatedAt
 */
GetDeploymentOutputDeployment.prototype['targetResourceCreatedAt'] = undefined;

/**
 * @member {module:model/DeploymentTargetResourceType} targetResourceType
 */
GetDeploymentOutputDeployment.prototype['targetResourceType'] = undefined;

/**
 * @member {module:model/DeploymentTargetState} targetState
 */
GetDeploymentOutputDeployment.prototype['targetState'] = undefined;


// Implement Deployment interface:
/**
 * @member {String} arn
 */
Deployment.prototype['arn'] = undefined;
/**
 * @member {Date} completedAt
 */
Deployment.prototype['completedAt'] = undefined;
/**
 * @member {String} componentName
 */
Deployment.prototype['componentName'] = undefined;
/**
 * @member {Date} createdAt
 */
Deployment.prototype['createdAt'] = undefined;
/**
 * @member {module:model/DeploymentStatus} deploymentStatus
 */
Deployment.prototype['deploymentStatus'] = undefined;
/**
 * @member {String} deploymentStatusMessage
 */
Deployment.prototype['deploymentStatusMessage'] = undefined;
/**
 * @member {String} environmentName
 */
Deployment.prototype['environmentName'] = undefined;
/**
 * @member {String} id
 */
Deployment.prototype['id'] = undefined;
/**
 * @member {module:model/DeploymentInitialState} initialState
 */
Deployment.prototype['initialState'] = undefined;
/**
 * @member {String} lastAttemptedDeploymentId
 */
Deployment.prototype['lastAttemptedDeploymentId'] = undefined;
/**
 * @member {Date} lastModifiedAt
 */
Deployment.prototype['lastModifiedAt'] = undefined;
/**
 * @member {String} lastSucceededDeploymentId
 */
Deployment.prototype['lastSucceededDeploymentId'] = undefined;
/**
 * @member {String} serviceInstanceName
 */
Deployment.prototype['serviceInstanceName'] = undefined;
/**
 * @member {String} serviceName
 */
Deployment.prototype['serviceName'] = undefined;
/**
 * @member {String} targetArn
 */
Deployment.prototype['targetArn'] = undefined;
/**
 * @member {Date} targetResourceCreatedAt
 */
Deployment.prototype['targetResourceCreatedAt'] = undefined;
/**
 * @member {module:model/DeploymentTargetResourceType} targetResourceType
 */
Deployment.prototype['targetResourceType'] = undefined;
/**
 * @member {module:model/DeploymentTargetState} targetState
 */
Deployment.prototype['targetState'] = undefined;




export default GetDeploymentOutputDeployment;

