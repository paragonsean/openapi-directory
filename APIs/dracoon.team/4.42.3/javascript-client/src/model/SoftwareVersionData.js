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
 * The SoftwareVersionData model module.
 * @module model/SoftwareVersionData
 * @version 4.42.3
 */
class SoftwareVersionData {
    /**
     * Constructs a new <code>SoftwareVersionData</code>.
     * Software version information
     * @alias module:model/SoftwareVersionData
     * @param buildDate {Date} Build date
     * @param restApiVersion {String} REST API version
     * @param scmRevisionNumber {String} Revision number
     * @param sdsServerVersion {String} DRACOON server version
     */
    constructor(buildDate, restApiVersion, scmRevisionNumber, sdsServerVersion) { 
        
        SoftwareVersionData.initialize(this, buildDate, restApiVersion, scmRevisionNumber, sdsServerVersion);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, buildDate, restApiVersion, scmRevisionNumber, sdsServerVersion) { 
        obj['buildDate'] = buildDate;
        obj['restApiVersion'] = restApiVersion;
        obj['scmRevisionNumber'] = scmRevisionNumber;
        obj['sdsServerVersion'] = sdsServerVersion;
    }

    /**
     * Constructs a <code>SoftwareVersionData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SoftwareVersionData} obj Optional instance to populate.
     * @return {module:model/SoftwareVersionData} The populated <code>SoftwareVersionData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SoftwareVersionData();

            if (data.hasOwnProperty('buildDate')) {
                obj['buildDate'] = ApiClient.convertToType(data['buildDate'], 'Date');
            }
            if (data.hasOwnProperty('isDracoonCloud')) {
                obj['isDracoonCloud'] = ApiClient.convertToType(data['isDracoonCloud'], 'Boolean');
            }
            if (data.hasOwnProperty('restApiVersion')) {
                obj['restApiVersion'] = ApiClient.convertToType(data['restApiVersion'], 'String');
            }
            if (data.hasOwnProperty('scmRevisionNumber')) {
                obj['scmRevisionNumber'] = ApiClient.convertToType(data['scmRevisionNumber'], 'String');
            }
            if (data.hasOwnProperty('sdsServerVersion')) {
                obj['sdsServerVersion'] = ApiClient.convertToType(data['sdsServerVersion'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SoftwareVersionData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SoftwareVersionData</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SoftwareVersionData.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['restApiVersion'] && !(typeof data['restApiVersion'] === 'string' || data['restApiVersion'] instanceof String)) {
            throw new Error("Expected the field `restApiVersion` to be a primitive type in the JSON string but got " + data['restApiVersion']);
        }
        // ensure the json data is a string
        if (data['scmRevisionNumber'] && !(typeof data['scmRevisionNumber'] === 'string' || data['scmRevisionNumber'] instanceof String)) {
            throw new Error("Expected the field `scmRevisionNumber` to be a primitive type in the JSON string but got " + data['scmRevisionNumber']);
        }
        // ensure the json data is a string
        if (data['sdsServerVersion'] && !(typeof data['sdsServerVersion'] === 'string' || data['sdsServerVersion'] instanceof String)) {
            throw new Error("Expected the field `sdsServerVersion` to be a primitive type in the JSON string but got " + data['sdsServerVersion']);
        }

        return true;
    }


}

SoftwareVersionData.RequiredProperties = ["buildDate", "restApiVersion", "scmRevisionNumber", "sdsServerVersion"];

/**
 * Build date
 * @member {Date} buildDate
 */
SoftwareVersionData.prototype['buildDate'] = undefined;

/**
 * &#128640; Since v4.24.0  Determines if the DRACOON Core is deployed in the cloud environment
 * @member {Boolean} isDracoonCloud
 */
SoftwareVersionData.prototype['isDracoonCloud'] = undefined;

/**
 * REST API version
 * @member {String} restApiVersion
 */
SoftwareVersionData.prototype['restApiVersion'] = undefined;

/**
 * Revision number
 * @member {String} scmRevisionNumber
 */
SoftwareVersionData.prototype['scmRevisionNumber'] = undefined;

/**
 * DRACOON server version
 * @member {String} sdsServerVersion
 */
SoftwareVersionData.prototype['sdsServerVersion'] = undefined;






export default SoftwareVersionData;

