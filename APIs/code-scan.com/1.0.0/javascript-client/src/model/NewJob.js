/**
 * CodeScan API
 * Manage your Hosted CodeScan Service
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@villagechief.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The NewJob model module.
 * @module model/NewJob
 * @version 1.0.0
 */
class NewJob {
    /**
     * Constructs a new <code>NewJob</code>.
     * @alias module:model/NewJob
     * @param projectKey {String} The key of the project to start
     */
    constructor(projectKey) { 
        
        NewJob.initialize(this, projectKey);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, projectKey) { 
        obj['projectKey'] = projectKey;
    }

    /**
     * Constructs a <code>NewJob</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NewJob} obj Optional instance to populate.
     * @return {module:model/NewJob} The populated <code>NewJob</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NewJob();

            if (data.hasOwnProperty('analysisMode')) {
                obj['analysisMode'] = ApiClient.convertToType(data['analysisMode'], 'String');
            }
            if (data.hasOwnProperty('commitOverride')) {
                obj['commitOverride'] = ApiClient.convertToType(data['commitOverride'], 'String');
            }
            if (data.hasOwnProperty('emailReportTo')) {
                obj['emailReportTo'] = ApiClient.convertToType(data['emailReportTo'], 'String');
            }
            if (data.hasOwnProperty('projectBranch')) {
                obj['projectBranch'] = ApiClient.convertToType(data['projectBranch'], 'String');
            }
            if (data.hasOwnProperty('projectKey')) {
                obj['projectKey'] = ApiClient.convertToType(data['projectKey'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NewJob</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NewJob</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of NewJob.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['analysisMode'] && !(typeof data['analysisMode'] === 'string' || data['analysisMode'] instanceof String)) {
            throw new Error("Expected the field `analysisMode` to be a primitive type in the JSON string but got " + data['analysisMode']);
        }
        // ensure the json data is a string
        if (data['commitOverride'] && !(typeof data['commitOverride'] === 'string' || data['commitOverride'] instanceof String)) {
            throw new Error("Expected the field `commitOverride` to be a primitive type in the JSON string but got " + data['commitOverride']);
        }
        // ensure the json data is a string
        if (data['emailReportTo'] && !(typeof data['emailReportTo'] === 'string' || data['emailReportTo'] instanceof String)) {
            throw new Error("Expected the field `emailReportTo` to be a primitive type in the JSON string but got " + data['emailReportTo']);
        }
        // ensure the json data is a string
        if (data['projectBranch'] && !(typeof data['projectBranch'] === 'string' || data['projectBranch'] instanceof String)) {
            throw new Error("Expected the field `projectBranch` to be a primitive type in the JSON string but got " + data['projectBranch']);
        }
        // ensure the json data is a string
        if (data['projectKey'] && !(typeof data['projectKey'] === 'string' || data['projectKey'] instanceof String)) {
            throw new Error("Expected the field `projectKey` to be a primitive type in the JSON string but got " + data['projectKey']);
        }
        // ensure the json data is a string
        if (data['version'] && !(typeof data['version'] === 'string' || data['version'] instanceof String)) {
            throw new Error("Expected the field `version` to be a primitive type in the JSON string but got " + data['version']);
        }

        return true;
    }


}

NewJob.RequiredProperties = ["projectKey"];

/**
 * When set to preview, analysis is not added to the database
 * @member {String} analysisMode
 */
NewJob.prototype['analysisMode'] = undefined;

/**
 * When the project is based on git, the git commit that this job should run. Leave blank to use the project's default
 * @member {String} commitOverride
 */
NewJob.prototype['commitOverride'] = undefined;

/**
 * List of usernames to email the report to
 * @member {String} emailReportTo
 */
NewJob.prototype['emailReportTo'] = undefined;

/**
 * he project branch that this job is evaluating
 * @member {String} projectBranch
 */
NewJob.prototype['projectBranch'] = undefined;

/**
 * The key of the project to start
 * @member {String} projectKey
 */
NewJob.prototype['projectKey'] = undefined;

/**
 * Use this as the analysis' version. On success the Project's default version will be set to this
 * @member {String} version
 */
NewJob.prototype['version'] = undefined;






export default NewJob;

