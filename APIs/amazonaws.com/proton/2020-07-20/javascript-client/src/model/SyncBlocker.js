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
import BlockerStatus from './BlockerStatus';
import BlockerType from './BlockerType';

/**
 * The SyncBlocker model module.
 * @module model/SyncBlocker
 * @version 2020-07-20
 */
class SyncBlocker {
    /**
     * Constructs a new <code>SyncBlocker</code>.
     * Detailed data of the sync blocker.
     * @alias module:model/SyncBlocker
     * @param createdAt {Date} 
     * @param createdReason {String} 
     * @param id {String} 
     * @param status {module:model/BlockerStatus} 
     * @param type {module:model/BlockerType} 
     */
    constructor(createdAt, createdReason, id, status, type) { 
        
        SyncBlocker.initialize(this, createdAt, createdReason, id, status, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, createdAt, createdReason, id, status, type) { 
        obj['createdAt'] = createdAt;
        obj['createdReason'] = createdReason;
        obj['id'] = id;
        obj['status'] = status;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>SyncBlocker</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SyncBlocker} obj Optional instance to populate.
     * @return {module:model/SyncBlocker} The populated <code>SyncBlocker</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SyncBlocker();

            if (data.hasOwnProperty('contexts')) {
                obj['contexts'] = ApiClient.convertToType(data['contexts'], Array);
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('createdReason')) {
                obj['createdReason'] = ApiClient.convertToType(data['createdReason'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('resolvedAt')) {
                obj['resolvedAt'] = ApiClient.convertToType(data['resolvedAt'], 'Date');
            }
            if (data.hasOwnProperty('resolvedReason')) {
                obj['resolvedReason'] = ApiClient.convertToType(data['resolvedReason'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], BlockerStatus);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], BlockerType);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SyncBlocker</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SyncBlocker</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SyncBlocker.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `contexts`
        if (data['contexts']) { // data not null
          Array.validateJSON(data['contexts']);
        }
        // validate the optional field `createdAt`
        if (data['createdAt']) { // data not null
          Date.validateJSON(data['createdAt']);
        }
        // validate the optional field `createdReason`
        if (data['createdReason']) { // data not null
          String.validateJSON(data['createdReason']);
        }
        // validate the optional field `id`
        if (data['id']) { // data not null
          String.validateJSON(data['id']);
        }
        // validate the optional field `resolvedAt`
        if (data['resolvedAt']) { // data not null
          Date.validateJSON(data['resolvedAt']);
        }
        // validate the optional field `resolvedReason`
        if (data['resolvedReason']) { // data not null
          String.validateJSON(data['resolvedReason']);
        }
        // validate the optional field `status`
        if (data['status']) { // data not null
          BlockerStatus.validateJSON(data['status']);
        }
        // validate the optional field `type`
        if (data['type']) { // data not null
          BlockerType.validateJSON(data['type']);
        }

        return true;
    }


}

SyncBlocker.RequiredProperties = ["createdAt", "createdReason", "id", "status", "type"];

/**
 * @member {Array} contexts
 */
SyncBlocker.prototype['contexts'] = undefined;

/**
 * @member {Date} createdAt
 */
SyncBlocker.prototype['createdAt'] = undefined;

/**
 * @member {String} createdReason
 */
SyncBlocker.prototype['createdReason'] = undefined;

/**
 * @member {String} id
 */
SyncBlocker.prototype['id'] = undefined;

/**
 * @member {Date} resolvedAt
 */
SyncBlocker.prototype['resolvedAt'] = undefined;

/**
 * @member {String} resolvedReason
 */
SyncBlocker.prototype['resolvedReason'] = undefined;

/**
 * @member {module:model/BlockerStatus} status
 */
SyncBlocker.prototype['status'] = undefined;

/**
 * @member {module:model/BlockerType} type
 */
SyncBlocker.prototype['type'] = undefined;






export default SyncBlocker;

