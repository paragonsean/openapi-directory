/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import DeploymentViewAuthor from './DeploymentViewAuthor';

/**
 * The DeploymentView model module.
 * @module model/DeploymentView
 * @version 1.0.0
 */
class DeploymentView {
    /**
     * Constructs a new <code>DeploymentView</code>.
     * @alias module:model/DeploymentView
     * @param action {String} 
     * @param cause {String} 
     * @param commit {String} 
     * @param date {Date} 
     * @param id {Number} 
     * @param instances {Number} 
     * @param state {String} 
     * @param uuid {String} 
     */
    constructor(action, cause, commit, date, id, instances, state, uuid) { 
        
        DeploymentView.initialize(this, action, cause, commit, date, id, instances, state, uuid);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, action, cause, commit, date, id, instances, state, uuid) { 
        obj['action'] = action;
        obj['cause'] = cause;
        obj['commit'] = commit;
        obj['date'] = date;
        obj['id'] = id;
        obj['instances'] = instances;
        obj['state'] = state;
        obj['uuid'] = uuid;
    }

    /**
     * Constructs a <code>DeploymentView</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeploymentView} obj Optional instance to populate.
     * @return {module:model/DeploymentView} The populated <code>DeploymentView</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeploymentView();

            if (data.hasOwnProperty('action')) {
                obj['action'] = ApiClient.convertToType(data['action'], 'String');
            }
            if (data.hasOwnProperty('author')) {
                obj['author'] = DeploymentViewAuthor.constructFromObject(data['author']);
            }
            if (data.hasOwnProperty('cause')) {
                obj['cause'] = ApiClient.convertToType(data['cause'], 'String');
            }
            if (data.hasOwnProperty('commit')) {
                obj['commit'] = ApiClient.convertToType(data['commit'], 'String');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('instances')) {
                obj['instances'] = ApiClient.convertToType(data['instances'], 'Number');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
            if (data.hasOwnProperty('uuid')) {
                obj['uuid'] = ApiClient.convertToType(data['uuid'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeploymentView</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeploymentView</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeploymentView.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['action'] && !(typeof data['action'] === 'string' || data['action'] instanceof String)) {
            throw new Error("Expected the field `action` to be a primitive type in the JSON string but got " + data['action']);
        }
        // validate the optional field `author`
        if (data['author']) { // data not null
          DeploymentViewAuthor.validateJSON(data['author']);
        }
        // ensure the json data is a string
        if (data['cause'] && !(typeof data['cause'] === 'string' || data['cause'] instanceof String)) {
            throw new Error("Expected the field `cause` to be a primitive type in the JSON string but got " + data['cause']);
        }
        // ensure the json data is a string
        if (data['commit'] && !(typeof data['commit'] === 'string' || data['commit'] instanceof String)) {
            throw new Error("Expected the field `commit` to be a primitive type in the JSON string but got " + data['commit']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }
        // ensure the json data is a string
        if (data['uuid'] && !(typeof data['uuid'] === 'string' || data['uuid'] instanceof String)) {
            throw new Error("Expected the field `uuid` to be a primitive type in the JSON string but got " + data['uuid']);
        }

        return true;
    }


}

DeploymentView.RequiredProperties = ["action", "cause", "commit", "date", "id", "instances", "state", "uuid"];

/**
 * @member {String} action
 */
DeploymentView.prototype['action'] = undefined;

/**
 * @member {module:model/DeploymentViewAuthor} author
 */
DeploymentView.prototype['author'] = undefined;

/**
 * @member {String} cause
 */
DeploymentView.prototype['cause'] = undefined;

/**
 * @member {String} commit
 */
DeploymentView.prototype['commit'] = undefined;

/**
 * @member {Date} date
 */
DeploymentView.prototype['date'] = undefined;

/**
 * @member {Number} id
 */
DeploymentView.prototype['id'] = undefined;

/**
 * @member {Number} instances
 */
DeploymentView.prototype['instances'] = undefined;

/**
 * @member {String} state
 */
DeploymentView.prototype['state'] = undefined;

/**
 * @member {String} uuid
 */
DeploymentView.prototype['uuid'] = undefined;






export default DeploymentView;

