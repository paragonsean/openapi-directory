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
 * The CopyNode model module.
 * @module model/CopyNode
 * @version 4.42.3
 */
class CopyNode {
    /**
     * Constructs a new <code>CopyNode</code>.
     * Copied node information
     * @alias module:model/CopyNode
     * @param id {Number} Source node ID
     */
    constructor(id) { 
        
        CopyNode.initialize(this, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id) { 
        obj['id'] = id;
    }

    /**
     * Constructs a <code>CopyNode</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CopyNode} obj Optional instance to populate.
     * @return {module:model/CopyNode} The populated <code>CopyNode</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CopyNode();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('timestampCreation')) {
                obj['timestampCreation'] = ApiClient.convertToType(data['timestampCreation'], 'Date');
            }
            if (data.hasOwnProperty('timestampModification')) {
                obj['timestampModification'] = ApiClient.convertToType(data['timestampModification'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CopyNode</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CopyNode</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CopyNode.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

CopyNode.RequiredProperties = ["id"];

/**
 * Source node ID
 * @member {Number} id
 */
CopyNode.prototype['id'] = undefined;

/**
 * New node name
 * @member {String} name
 */
CopyNode.prototype['name'] = undefined;

/**
 * &#128640; Since v4.22.0  Time the node was created on external file system  (default: current server datetime in UTC format)
 * @member {Date} timestampCreation
 */
CopyNode.prototype['timestampCreation'] = undefined;

/**
 * &#128640; Since v4.22.0  Time the content of a node was last modified on external file system  (default: current server datetime in UTC format)
 * @member {Date} timestampModification
 */
CopyNode.prototype['timestampModification'] = undefined;






export default CopyNode;

