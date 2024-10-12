/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GitCommitTrigger model module.
 * @module model/GitCommitTrigger
 * @version 2018-02-01-preview
 */
class GitCommitTrigger {
    /**
     * Constructs a new <code>GitCommitTrigger</code>.
     * The git commit trigger that caused a build.
     * @alias module:model/GitCommitTrigger
     */
    constructor() { 
        
        GitCommitTrigger.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GitCommitTrigger</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GitCommitTrigger} obj Optional instance to populate.
     * @return {module:model/GitCommitTrigger} The populated <code>GitCommitTrigger</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GitCommitTrigger();

            if (data.hasOwnProperty('branchName')) {
                obj['branchName'] = ApiClient.convertToType(data['branchName'], 'String');
            }
            if (data.hasOwnProperty('commitId')) {
                obj['commitId'] = ApiClient.convertToType(data['commitId'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('providerType')) {
                obj['providerType'] = ApiClient.convertToType(data['providerType'], 'String');
            }
            if (data.hasOwnProperty('repositoryUrl')) {
                obj['repositoryUrl'] = ApiClient.convertToType(data['repositoryUrl'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GitCommitTrigger</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GitCommitTrigger</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['branchName'] && !(typeof data['branchName'] === 'string' || data['branchName'] instanceof String)) {
            throw new Error("Expected the field `branchName` to be a primitive type in the JSON string but got " + data['branchName']);
        }
        // ensure the json data is a string
        if (data['commitId'] && !(typeof data['commitId'] === 'string' || data['commitId'] instanceof String)) {
            throw new Error("Expected the field `commitId` to be a primitive type in the JSON string but got " + data['commitId']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['providerType'] && !(typeof data['providerType'] === 'string' || data['providerType'] instanceof String)) {
            throw new Error("Expected the field `providerType` to be a primitive type in the JSON string but got " + data['providerType']);
        }
        // ensure the json data is a string
        if (data['repositoryUrl'] && !(typeof data['repositoryUrl'] === 'string' || data['repositoryUrl'] instanceof String)) {
            throw new Error("Expected the field `repositoryUrl` to be a primitive type in the JSON string but got " + data['repositoryUrl']);
        }

        return true;
    }


}



/**
 * The branch name in the repository.
 * @member {String} branchName
 */
GitCommitTrigger.prototype['branchName'] = undefined;

/**
 * The unique ID that identifies a commit.
 * @member {String} commitId
 */
GitCommitTrigger.prototype['commitId'] = undefined;

/**
 * The unique ID of the trigger.
 * @member {String} id
 */
GitCommitTrigger.prototype['id'] = undefined;

/**
 * The source control provider type.
 * @member {String} providerType
 */
GitCommitTrigger.prototype['providerType'] = undefined;

/**
 * The repository URL.
 * @member {String} repositoryUrl
 */
GitCommitTrigger.prototype['repositoryUrl'] = undefined;






export default GitCommitTrigger;

