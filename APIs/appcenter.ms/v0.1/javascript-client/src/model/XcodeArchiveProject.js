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
 * The XcodeArchiveProject model module.
 * @module model/XcodeArchiveProject
 * @version v0.1
 */
class XcodeArchiveProject {
    /**
     * Constructs a new <code>XcodeArchiveProject</code>.
     * @alias module:model/XcodeArchiveProject
     * @param archiveTargetId {String} The Id of the target to archive
     * @param projectName {String} The project to archive container name
     */
    constructor(archiveTargetId, projectName) { 
        
        XcodeArchiveProject.initialize(this, archiveTargetId, projectName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, archiveTargetId, projectName) { 
        obj['archiveTargetId'] = archiveTargetId;
        obj['projectName'] = projectName;
    }

    /**
     * Constructs a <code>XcodeArchiveProject</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/XcodeArchiveProject} obj Optional instance to populate.
     * @return {module:model/XcodeArchiveProject} The populated <code>XcodeArchiveProject</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new XcodeArchiveProject();

            if (data.hasOwnProperty('archiveTargetId')) {
                obj['archiveTargetId'] = ApiClient.convertToType(data['archiveTargetId'], 'String');
            }
            if (data.hasOwnProperty('projectName')) {
                obj['projectName'] = ApiClient.convertToType(data['projectName'], 'String');
            }
            if (data.hasOwnProperty('projectPath')) {
                obj['projectPath'] = ApiClient.convertToType(data['projectPath'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>XcodeArchiveProject</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>XcodeArchiveProject</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of XcodeArchiveProject.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['archiveTargetId'] && !(typeof data['archiveTargetId'] === 'string' || data['archiveTargetId'] instanceof String)) {
            throw new Error("Expected the field `archiveTargetId` to be a primitive type in the JSON string but got " + data['archiveTargetId']);
        }
        // ensure the json data is a string
        if (data['projectName'] && !(typeof data['projectName'] === 'string' || data['projectName'] instanceof String)) {
            throw new Error("Expected the field `projectName` to be a primitive type in the JSON string but got " + data['projectName']);
        }
        // ensure the json data is a string
        if (data['projectPath'] && !(typeof data['projectPath'] === 'string' || data['projectPath'] instanceof String)) {
            throw new Error("Expected the field `projectPath` to be a primitive type in the JSON string but got " + data['projectPath']);
        }

        return true;
    }


}

XcodeArchiveProject.RequiredProperties = ["archiveTargetId", "projectName"];

/**
 * The Id of the target to archive
 * @member {String} archiveTargetId
 */
XcodeArchiveProject.prototype['archiveTargetId'] = undefined;

/**
 * The project to archive container name
 * @member {String} projectName
 */
XcodeArchiveProject.prototype['projectName'] = undefined;

/**
 * Full path of the target project
 * @member {String} projectPath
 */
XcodeArchiveProject.prototype['projectPath'] = undefined;






export default XcodeArchiveProject;

