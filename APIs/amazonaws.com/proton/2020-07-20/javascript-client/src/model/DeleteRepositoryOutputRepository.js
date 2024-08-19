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
import Repository from './Repository';
import RepositoryProvider from './RepositoryProvider';

/**
 * The DeleteRepositoryOutputRepository model module.
 * @module model/DeleteRepositoryOutputRepository
 * @version 2020-07-20
 */
class DeleteRepositoryOutputRepository {
    /**
     * Constructs a new <code>DeleteRepositoryOutputRepository</code>.
     * @alias module:model/DeleteRepositoryOutputRepository
     * @implements module:model/Repository
     * @param arn {String} 
     * @param connectionArn {String} 
     * @param name {String} 
     * @param provider {module:model/RepositoryProvider} 
     */
    constructor(arn, connectionArn, name, provider) { 
        Repository.initialize(this, arn, connectionArn, name, provider);
        DeleteRepositoryOutputRepository.initialize(this, arn, connectionArn, name, provider);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, arn, connectionArn, name, provider) { 
        obj['arn'] = arn;
        obj['connectionArn'] = connectionArn;
        obj['name'] = name;
        obj['provider'] = provider;
    }

    /**
     * Constructs a <code>DeleteRepositoryOutputRepository</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeleteRepositoryOutputRepository} obj Optional instance to populate.
     * @return {module:model/DeleteRepositoryOutputRepository} The populated <code>DeleteRepositoryOutputRepository</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeleteRepositoryOutputRepository();
            Repository.constructFromObject(data, obj);

            if (data.hasOwnProperty('arn')) {
                obj['arn'] = ApiClient.convertToType(data['arn'], 'String');
            }
            if (data.hasOwnProperty('connectionArn')) {
                obj['connectionArn'] = ApiClient.convertToType(data['connectionArn'], 'String');
            }
            if (data.hasOwnProperty('encryptionKey')) {
                obj['encryptionKey'] = ApiClient.convertToType(data['encryptionKey'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('provider')) {
                obj['provider'] = ApiClient.convertToType(data['provider'], RepositoryProvider);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeleteRepositoryOutputRepository</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeleteRepositoryOutputRepository</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeleteRepositoryOutputRepository.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `arn`
        if (data['arn']) { // data not null
          String.validateJSON(data['arn']);
        }
        // validate the optional field `connectionArn`
        if (data['connectionArn']) { // data not null
          String.validateJSON(data['connectionArn']);
        }
        // validate the optional field `encryptionKey`
        if (data['encryptionKey']) { // data not null
          String.validateJSON(data['encryptionKey']);
        }
        // validate the optional field `name`
        if (data['name']) { // data not null
          String.validateJSON(data['name']);
        }
        // validate the optional field `provider`
        if (data['provider']) { // data not null
          RepositoryProvider.validateJSON(data['provider']);
        }

        return true;
    }


}

DeleteRepositoryOutputRepository.RequiredProperties = ["arn", "connectionArn", "name", "provider"];

/**
 * @member {String} arn
 */
DeleteRepositoryOutputRepository.prototype['arn'] = undefined;

/**
 * @member {String} connectionArn
 */
DeleteRepositoryOutputRepository.prototype['connectionArn'] = undefined;

/**
 * @member {String} encryptionKey
 */
DeleteRepositoryOutputRepository.prototype['encryptionKey'] = undefined;

/**
 * @member {String} name
 */
DeleteRepositoryOutputRepository.prototype['name'] = undefined;

/**
 * @member {module:model/RepositoryProvider} provider
 */
DeleteRepositoryOutputRepository.prototype['provider'] = undefined;


// Implement Repository interface:
/**
 * @member {String} arn
 */
Repository.prototype['arn'] = undefined;
/**
 * @member {String} connectionArn
 */
Repository.prototype['connectionArn'] = undefined;
/**
 * @member {String} encryptionKey
 */
Repository.prototype['encryptionKey'] = undefined;
/**
 * @member {String} name
 */
Repository.prototype['name'] = undefined;
/**
 * @member {module:model/RepositoryProvider} provider
 */
Repository.prototype['provider'] = undefined;




export default DeleteRepositoryOutputRepository;

