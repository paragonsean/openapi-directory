/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AnonymizationKey model module.
 * @module model/AnonymizationKey
 * @version 2.0
 */
class AnonymizationKey {
    /**
     * Constructs a new <code>AnonymizationKey</code>.
     * @alias module:model/AnonymizationKey
     */
    constructor() { 
        
        AnonymizationKey.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnonymizationKey</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnonymizationKey} obj Optional instance to populate.
     * @return {module:model/AnonymizationKey} The populated <code>AnonymizationKey</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnonymizationKey();

            if (data.hasOwnProperty('anonPatientID')) {
                obj['anonPatientID'] = ApiClient.convertToType(data['anonPatientID'], 'String');
            }
            if (data.hasOwnProperty('anonPatientName')) {
                obj['anonPatientName'] = ApiClient.convertToType(data['anonPatientName'], 'String');
            }
            if (data.hasOwnProperty('anonSOPInstanceUID')) {
                obj['anonSOPInstanceUID'] = ApiClient.convertToType(data['anonSOPInstanceUID'], 'String');
            }
            if (data.hasOwnProperty('anonSeriesInstanceUID')) {
                obj['anonSeriesInstanceUID'] = ApiClient.convertToType(data['anonSeriesInstanceUID'], 'String');
            }
            if (data.hasOwnProperty('anonStudyInstanceUID')) {
                obj['anonStudyInstanceUID'] = ApiClient.convertToType(data['anonStudyInstanceUID'], 'String');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('imageId')) {
                obj['imageId'] = ApiClient.convertToType(data['imageId'], 'Number');
            }
            if (data.hasOwnProperty('patientID')) {
                obj['patientID'] = ApiClient.convertToType(data['patientID'], 'String');
            }
            if (data.hasOwnProperty('patientName')) {
                obj['patientName'] = ApiClient.convertToType(data['patientName'], 'String');
            }
            if (data.hasOwnProperty('seriesInstanceUID')) {
                obj['seriesInstanceUID'] = ApiClient.convertToType(data['seriesInstanceUID'], 'String');
            }
            if (data.hasOwnProperty('sopInstanceUID')) {
                obj['sopInstanceUID'] = ApiClient.convertToType(data['sopInstanceUID'], 'String');
            }
            if (data.hasOwnProperty('studyInstanceUID')) {
                obj['studyInstanceUID'] = ApiClient.convertToType(data['studyInstanceUID'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnonymizationKey</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnonymizationKey</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['anonPatientID'] && !(typeof data['anonPatientID'] === 'string' || data['anonPatientID'] instanceof String)) {
            throw new Error("Expected the field `anonPatientID` to be a primitive type in the JSON string but got " + data['anonPatientID']);
        }
        // ensure the json data is a string
        if (data['anonPatientName'] && !(typeof data['anonPatientName'] === 'string' || data['anonPatientName'] instanceof String)) {
            throw new Error("Expected the field `anonPatientName` to be a primitive type in the JSON string but got " + data['anonPatientName']);
        }
        // ensure the json data is a string
        if (data['anonSOPInstanceUID'] && !(typeof data['anonSOPInstanceUID'] === 'string' || data['anonSOPInstanceUID'] instanceof String)) {
            throw new Error("Expected the field `anonSOPInstanceUID` to be a primitive type in the JSON string but got " + data['anonSOPInstanceUID']);
        }
        // ensure the json data is a string
        if (data['anonSeriesInstanceUID'] && !(typeof data['anonSeriesInstanceUID'] === 'string' || data['anonSeriesInstanceUID'] instanceof String)) {
            throw new Error("Expected the field `anonSeriesInstanceUID` to be a primitive type in the JSON string but got " + data['anonSeriesInstanceUID']);
        }
        // ensure the json data is a string
        if (data['anonStudyInstanceUID'] && !(typeof data['anonStudyInstanceUID'] === 'string' || data['anonStudyInstanceUID'] instanceof String)) {
            throw new Error("Expected the field `anonStudyInstanceUID` to be a primitive type in the JSON string but got " + data['anonStudyInstanceUID']);
        }
        // ensure the json data is a string
        if (data['patientID'] && !(typeof data['patientID'] === 'string' || data['patientID'] instanceof String)) {
            throw new Error("Expected the field `patientID` to be a primitive type in the JSON string but got " + data['patientID']);
        }
        // ensure the json data is a string
        if (data['patientName'] && !(typeof data['patientName'] === 'string' || data['patientName'] instanceof String)) {
            throw new Error("Expected the field `patientName` to be a primitive type in the JSON string but got " + data['patientName']);
        }
        // ensure the json data is a string
        if (data['seriesInstanceUID'] && !(typeof data['seriesInstanceUID'] === 'string' || data['seriesInstanceUID'] instanceof String)) {
            throw new Error("Expected the field `seriesInstanceUID` to be a primitive type in the JSON string but got " + data['seriesInstanceUID']);
        }
        // ensure the json data is a string
        if (data['sopInstanceUID'] && !(typeof data['sopInstanceUID'] === 'string' || data['sopInstanceUID'] instanceof String)) {
            throw new Error("Expected the field `sopInstanceUID` to be a primitive type in the JSON string but got " + data['sopInstanceUID']);
        }
        // ensure the json data is a string
        if (data['studyInstanceUID'] && !(typeof data['studyInstanceUID'] === 'string' || data['studyInstanceUID'] instanceof String)) {
            throw new Error("Expected the field `studyInstanceUID` to be a primitive type in the JSON string but got " + data['studyInstanceUID']);
        }

        return true;
    }


}



/**
 * @member {String} anonPatientID
 */
AnonymizationKey.prototype['anonPatientID'] = undefined;

/**
 * @member {String} anonPatientName
 */
AnonymizationKey.prototype['anonPatientName'] = undefined;

/**
 * @member {String} anonSOPInstanceUID
 */
AnonymizationKey.prototype['anonSOPInstanceUID'] = undefined;

/**
 * @member {String} anonSeriesInstanceUID
 */
AnonymizationKey.prototype['anonSeriesInstanceUID'] = undefined;

/**
 * @member {String} anonStudyInstanceUID
 */
AnonymizationKey.prototype['anonStudyInstanceUID'] = undefined;

/**
 * @member {Number} created
 */
AnonymizationKey.prototype['created'] = undefined;

/**
 * @member {Number} id
 */
AnonymizationKey.prototype['id'] = undefined;

/**
 * @member {Number} imageId
 */
AnonymizationKey.prototype['imageId'] = undefined;

/**
 * @member {String} patientID
 */
AnonymizationKey.prototype['patientID'] = undefined;

/**
 * @member {String} patientName
 */
AnonymizationKey.prototype['patientName'] = undefined;

/**
 * @member {String} seriesInstanceUID
 */
AnonymizationKey.prototype['seriesInstanceUID'] = undefined;

/**
 * @member {String} sopInstanceUID
 */
AnonymizationKey.prototype['sopInstanceUID'] = undefined;

/**
 * @member {String} studyInstanceUID
 */
AnonymizationKey.prototype['studyInstanceUID'] = undefined;






export default AnonymizationKey;

