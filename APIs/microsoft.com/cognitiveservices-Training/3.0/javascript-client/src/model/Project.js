/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ProjectSettings from './ProjectSettings';

/**
 * The Project model module.
 * @module model/Project
 * @version 3.0
 */
class Project {
    /**
     * Constructs a new <code>Project</code>.
     * Represents a project.
     * @alias module:model/Project
     * @param description {String} Gets or sets the description of the project.
     * @param name {String} Gets or sets the name of the project.
     * @param settings {module:model/ProjectSettings} 
     */
    constructor(description, name, settings) { 
        
        Project.initialize(this, description, name, settings);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, description, name, settings) { 
        obj['description'] = description;
        obj['name'] = name;
        obj['settings'] = settings;
    }

    /**
     * Constructs a <code>Project</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Project} obj Optional instance to populate.
     * @return {module:model/Project} The populated <code>Project</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Project();

            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('drModeEnabled')) {
                obj['drModeEnabled'] = ApiClient.convertToType(data['drModeEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('lastModified')) {
                obj['lastModified'] = ApiClient.convertToType(data['lastModified'], 'Date');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('settings')) {
                obj['settings'] = ProjectSettings.constructFromObject(data['settings']);
            }
            if (data.hasOwnProperty('thumbnailUri')) {
                obj['thumbnailUri'] = ApiClient.convertToType(data['thumbnailUri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Project</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Project</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Project.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `settings`
        if (data['settings']) { // data not null
          ProjectSettings.validateJSON(data['settings']);
        }
        // ensure the json data is a string
        if (data['thumbnailUri'] && !(typeof data['thumbnailUri'] === 'string' || data['thumbnailUri'] instanceof String)) {
            throw new Error("Expected the field `thumbnailUri` to be a primitive type in the JSON string but got " + data['thumbnailUri']);
        }

        return true;
    }


}

Project.RequiredProperties = ["description", "name", "settings"];

/**
 * Gets the date this project was created.
 * @member {Date} created
 */
Project.prototype['created'] = undefined;

/**
 * Gets or sets the description of the project.
 * @member {String} description
 */
Project.prototype['description'] = undefined;

/**
 * Gets if the DR mode is on.
 * @member {Boolean} drModeEnabled
 */
Project.prototype['drModeEnabled'] = undefined;

/**
 * Gets the project id.
 * @member {String} id
 */
Project.prototype['id'] = undefined;

/**
 * Gets the date this project was last modified.
 * @member {Date} lastModified
 */
Project.prototype['lastModified'] = undefined;

/**
 * Gets or sets the name of the project.
 * @member {String} name
 */
Project.prototype['name'] = undefined;

/**
 * @member {module:model/ProjectSettings} settings
 */
Project.prototype['settings'] = undefined;

/**
 * Gets the thumbnail url representing the image.
 * @member {String} thumbnailUri
 */
Project.prototype['thumbnailUri'] = undefined;






export default Project;

