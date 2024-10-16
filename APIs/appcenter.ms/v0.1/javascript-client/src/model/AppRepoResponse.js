/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppRepoResponse model module.
 * @module model/AppRepoResponse
 * @version v0.1
 */
class AppRepoResponse {
    /**
     * Constructs a new <code>AppRepoResponse</code>.
     * @alias module:model/AppRepoResponse
     * @param appId {String} The unique id (UUID) of the app that this repository integration belongs to
     * @param id {String} The unique id (UUID) of the repository integration
     * @param repoUrl {String} The absolute URL of the repository
     * @param userId {String} The unique id (UUID) of the user who configured the repository
     */
    constructor(appId, id, repoUrl, userId) { 
        
        AppRepoResponse.initialize(this, appId, id, repoUrl, userId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, appId, id, repoUrl, userId) { 
        obj['app_id'] = appId;
        obj['id'] = id;
        obj['repo_url'] = repoUrl;
        obj['user_id'] = userId;
    }

    /**
     * Constructs a <code>AppRepoResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppRepoResponse} obj Optional instance to populate.
     * @return {module:model/AppRepoResponse} The populated <code>AppRepoResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppRepoResponse();

            if (data.hasOwnProperty('app_id')) {
                obj['app_id'] = ApiClient.convertToType(data['app_id'], 'String');
            }
            if (data.hasOwnProperty('external_user_id')) {
                obj['external_user_id'] = ApiClient.convertToType(data['external_user_id'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('installation_id')) {
                obj['installation_id'] = ApiClient.convertToType(data['installation_id'], 'String');
            }
            if (data.hasOwnProperty('repo_id')) {
                obj['repo_id'] = ApiClient.convertToType(data['repo_id'], 'String');
            }
            if (data.hasOwnProperty('repo_provider')) {
                obj['repo_provider'] = ApiClient.convertToType(data['repo_provider'], 'String');
            }
            if (data.hasOwnProperty('repo_url')) {
                obj['repo_url'] = ApiClient.convertToType(data['repo_url'], 'String');
            }
            if (data.hasOwnProperty('service_connection_id')) {
                obj['service_connection_id'] = ApiClient.convertToType(data['service_connection_id'], 'String');
            }
            if (data.hasOwnProperty('user_id')) {
                obj['user_id'] = ApiClient.convertToType(data['user_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppRepoResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppRepoResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AppRepoResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['app_id'] && !(typeof data['app_id'] === 'string' || data['app_id'] instanceof String)) {
            throw new Error("Expected the field `app_id` to be a primitive type in the JSON string but got " + data['app_id']);
        }
        // ensure the json data is a string
        if (data['external_user_id'] && !(typeof data['external_user_id'] === 'string' || data['external_user_id'] instanceof String)) {
            throw new Error("Expected the field `external_user_id` to be a primitive type in the JSON string but got " + data['external_user_id']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['installation_id'] && !(typeof data['installation_id'] === 'string' || data['installation_id'] instanceof String)) {
            throw new Error("Expected the field `installation_id` to be a primitive type in the JSON string but got " + data['installation_id']);
        }
        // ensure the json data is a string
        if (data['repo_id'] && !(typeof data['repo_id'] === 'string' || data['repo_id'] instanceof String)) {
            throw new Error("Expected the field `repo_id` to be a primitive type in the JSON string but got " + data['repo_id']);
        }
        // ensure the json data is a string
        if (data['repo_provider'] && !(typeof data['repo_provider'] === 'string' || data['repo_provider'] instanceof String)) {
            throw new Error("Expected the field `repo_provider` to be a primitive type in the JSON string but got " + data['repo_provider']);
        }
        // ensure the json data is a string
        if (data['repo_url'] && !(typeof data['repo_url'] === 'string' || data['repo_url'] instanceof String)) {
            throw new Error("Expected the field `repo_url` to be a primitive type in the JSON string but got " + data['repo_url']);
        }
        // ensure the json data is a string
        if (data['service_connection_id'] && !(typeof data['service_connection_id'] === 'string' || data['service_connection_id'] instanceof String)) {
            throw new Error("Expected the field `service_connection_id` to be a primitive type in the JSON string but got " + data['service_connection_id']);
        }
        // ensure the json data is a string
        if (data['user_id'] && !(typeof data['user_id'] === 'string' || data['user_id'] instanceof String)) {
            throw new Error("Expected the field `user_id` to be a primitive type in the JSON string but got " + data['user_id']);
        }

        return true;
    }


}

AppRepoResponse.RequiredProperties = ["app_id", "id", "repo_url", "user_id"];

/**
 * The unique id (UUID) of the app that this repository integration belongs to
 * @member {String} app_id
 */
AppRepoResponse.prototype['app_id'] = undefined;

/**
 * User id from the provider
 * @member {String} external_user_id
 */
AppRepoResponse.prototype['external_user_id'] = undefined;

/**
 * The unique id (UUID) of the repository integration
 * @member {String} id
 */
AppRepoResponse.prototype['id'] = undefined;

/**
 * Installation id from the provider
 * @member {String} installation_id
 */
AppRepoResponse.prototype['installation_id'] = undefined;

/**
 * Repository id from the provider
 * @member {String} repo_id
 */
AppRepoResponse.prototype['repo_id'] = undefined;

/**
 * The provider of the repository
 * @member {module:model/AppRepoResponse.RepoProviderEnum} repo_provider
 */
AppRepoResponse.prototype['repo_provider'] = undefined;

/**
 * The absolute URL of the repository
 * @member {String} repo_url
 */
AppRepoResponse.prototype['repo_url'] = undefined;

/**
 * The id of the service connection stored in customer credential store
 * @member {String} service_connection_id
 */
AppRepoResponse.prototype['service_connection_id'] = undefined;

/**
 * The unique id (UUID) of the user who configured the repository
 * @member {String} user_id
 */
AppRepoResponse.prototype['user_id'] = undefined;





/**
 * Allowed values for the <code>repo_provider</code> property.
 * @enum {String}
 * @readonly
 */
AppRepoResponse['RepoProviderEnum'] = {

    /**
     * value: "github"
     * @const
     */
    "github": "github",

    /**
     * value: "bitbucket"
     * @const
     */
    "bitbucket": "bitbucket",

    /**
     * value: "vsts"
     * @const
     */
    "vsts": "vsts",

    /**
     * value: "gitlab"
     * @const
     */
    "gitlab": "gitlab"
};



export default AppRepoResponse;

