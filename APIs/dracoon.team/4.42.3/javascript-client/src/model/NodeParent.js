/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The NodeParent model module.
 * @module model/NodeParent
 * @version 4.42.3
 */
class NodeParent {
    /**
     * Constructs a new <code>NodeParent</code>.
     * Parent node
     * @alias module:model/NodeParent
     * @param id {Number} Node ID
     * @param name {String} Node name
     * @param type {String} Node type
     */
    constructor(id, name, type) { 
        
        NodeParent.initialize(this, id, name, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, name, type) { 
        obj['id'] = id;
        obj['name'] = name;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>NodeParent</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NodeParent} obj Optional instance to populate.
     * @return {module:model/NodeParent} The populated <code>NodeParent</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NodeParent();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('parentId')) {
                obj['parentId'] = ApiClient.convertToType(data['parentId'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NodeParent</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NodeParent</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NodeParent.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

NodeParent.RequiredProperties = ["id", "name", "type"];

/**
 * Node ID
 * @member {Number} id
 */
NodeParent.prototype['id'] = undefined;

/**
 * Node name
 * @member {String} name
 */
NodeParent.prototype['name'] = undefined;

/**
 * Parent node ID (room or folder)
 * @member {Number} parentId
 */
NodeParent.prototype['parentId'] = undefined;

/**
 * Node type
 * @member {String} type
 */
NodeParent.prototype['type'] = undefined;






export default NodeParent;

