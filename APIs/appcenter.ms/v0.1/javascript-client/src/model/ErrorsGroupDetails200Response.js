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
import ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner from './ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner';

/**
 * The ErrorsGroupDetails200Response model module.
 * @module model/ErrorsGroupDetails200Response
 * @version v0.1
 */
class ErrorsGroupDetails200Response {
    /**
     * Constructs a new <code>ErrorsGroupDetails200Response</code>.
     * @alias module:model/ErrorsGroupDetails200Response
     * @param state {module:model/ErrorsGroupDetails200Response.StateEnum} 
     */
    constructor(state) { 
        
        ErrorsGroupDetails200Response.initialize(this, state);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, state) { 
        obj['appVersion'] = appVersion;
        obj['count'] = count;
        obj['deviceCount'] = deviceCount;
        obj['errorGroupId'] = errorGroupId;
        obj['firstOccurrence'] = firstOccurrence;
        obj['lastOccurrence'] = lastOccurrence;
        obj['state'] = state;
    }

    /**
     * Constructs a <code>ErrorsGroupDetails200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ErrorsGroupDetails200Response} obj Optional instance to populate.
     * @return {module:model/ErrorsGroupDetails200Response} The populated <code>ErrorsGroupDetails200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ErrorsGroupDetails200Response();

            if (data.hasOwnProperty('appBuild')) {
                obj['appBuild'] = ApiClient.convertToType(data['appBuild'], 'String');
            }
            if (data.hasOwnProperty('appVersion')) {
                obj['appVersion'] = ApiClient.convertToType(data['appVersion'], 'String');
            }
            if (data.hasOwnProperty('codeRaw')) {
                obj['codeRaw'] = ApiClient.convertToType(data['codeRaw'], 'String');
            }
            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('deviceCount')) {
                obj['deviceCount'] = ApiClient.convertToType(data['deviceCount'], 'Number');
            }
            if (data.hasOwnProperty('errorGroupId')) {
                obj['errorGroupId'] = ApiClient.convertToType(data['errorGroupId'], 'String');
            }
            if (data.hasOwnProperty('exceptionAppCode')) {
                obj['exceptionAppCode'] = ApiClient.convertToType(data['exceptionAppCode'], 'Boolean');
            }
            if (data.hasOwnProperty('exceptionClassMethod')) {
                obj['exceptionClassMethod'] = ApiClient.convertToType(data['exceptionClassMethod'], 'Boolean');
            }
            if (data.hasOwnProperty('exceptionClassName')) {
                obj['exceptionClassName'] = ApiClient.convertToType(data['exceptionClassName'], 'String');
            }
            if (data.hasOwnProperty('exceptionFile')) {
                obj['exceptionFile'] = ApiClient.convertToType(data['exceptionFile'], 'String');
            }
            if (data.hasOwnProperty('exceptionLine')) {
                obj['exceptionLine'] = ApiClient.convertToType(data['exceptionLine'], 'String');
            }
            if (data.hasOwnProperty('exceptionMessage')) {
                obj['exceptionMessage'] = ApiClient.convertToType(data['exceptionMessage'], 'String');
            }
            if (data.hasOwnProperty('exceptionMethod')) {
                obj['exceptionMethod'] = ApiClient.convertToType(data['exceptionMethod'], 'String');
            }
            if (data.hasOwnProperty('exceptionType')) {
                obj['exceptionType'] = ApiClient.convertToType(data['exceptionType'], 'String');
            }
            if (data.hasOwnProperty('firstOccurrence')) {
                obj['firstOccurrence'] = ApiClient.convertToType(data['firstOccurrence'], 'Date');
            }
            if (data.hasOwnProperty('hidden')) {
                obj['hidden'] = ApiClient.convertToType(data['hidden'], 'Boolean');
            }
            if (data.hasOwnProperty('lastOccurrence')) {
                obj['lastOccurrence'] = ApiClient.convertToType(data['lastOccurrence'], 'Date');
            }
            if (data.hasOwnProperty('reasonFrames')) {
                obj['reasonFrames'] = ApiClient.convertToType(data['reasonFrames'], [ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner]);
            }
            if (data.hasOwnProperty('annotation')) {
                obj['annotation'] = ApiClient.convertToType(data['annotation'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ErrorsGroupDetails200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ErrorsGroupDetails200Response</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ErrorsGroupDetails200Response.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['appBuild'] && !(typeof data['appBuild'] === 'string' || data['appBuild'] instanceof String)) {
            throw new Error("Expected the field `appBuild` to be a primitive type in the JSON string but got " + data['appBuild']);
        }
        // ensure the json data is a string
        if (data['appVersion'] && !(typeof data['appVersion'] === 'string' || data['appVersion'] instanceof String)) {
            throw new Error("Expected the field `appVersion` to be a primitive type in the JSON string but got " + data['appVersion']);
        }
        // ensure the json data is a string
        if (data['codeRaw'] && !(typeof data['codeRaw'] === 'string' || data['codeRaw'] instanceof String)) {
            throw new Error("Expected the field `codeRaw` to be a primitive type in the JSON string but got " + data['codeRaw']);
        }
        // ensure the json data is a string
        if (data['errorGroupId'] && !(typeof data['errorGroupId'] === 'string' || data['errorGroupId'] instanceof String)) {
            throw new Error("Expected the field `errorGroupId` to be a primitive type in the JSON string but got " + data['errorGroupId']);
        }
        // ensure the json data is a string
        if (data['exceptionClassName'] && !(typeof data['exceptionClassName'] === 'string' || data['exceptionClassName'] instanceof String)) {
            throw new Error("Expected the field `exceptionClassName` to be a primitive type in the JSON string but got " + data['exceptionClassName']);
        }
        // ensure the json data is a string
        if (data['exceptionFile'] && !(typeof data['exceptionFile'] === 'string' || data['exceptionFile'] instanceof String)) {
            throw new Error("Expected the field `exceptionFile` to be a primitive type in the JSON string but got " + data['exceptionFile']);
        }
        // ensure the json data is a string
        if (data['exceptionLine'] && !(typeof data['exceptionLine'] === 'string' || data['exceptionLine'] instanceof String)) {
            throw new Error("Expected the field `exceptionLine` to be a primitive type in the JSON string but got " + data['exceptionLine']);
        }
        // ensure the json data is a string
        if (data['exceptionMessage'] && !(typeof data['exceptionMessage'] === 'string' || data['exceptionMessage'] instanceof String)) {
            throw new Error("Expected the field `exceptionMessage` to be a primitive type in the JSON string but got " + data['exceptionMessage']);
        }
        // ensure the json data is a string
        if (data['exceptionMethod'] && !(typeof data['exceptionMethod'] === 'string' || data['exceptionMethod'] instanceof String)) {
            throw new Error("Expected the field `exceptionMethod` to be a primitive type in the JSON string but got " + data['exceptionMethod']);
        }
        // ensure the json data is a string
        if (data['exceptionType'] && !(typeof data['exceptionType'] === 'string' || data['exceptionType'] instanceof String)) {
            throw new Error("Expected the field `exceptionType` to be a primitive type in the JSON string but got " + data['exceptionType']);
        }
        if (data['reasonFrames']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['reasonFrames'])) {
                throw new Error("Expected the field `reasonFrames` to be an array in the JSON data but got " + data['reasonFrames']);
            }
            // validate the optional field `reasonFrames` (array)
            for (const item of data['reasonFrames']) {
                ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['annotation'] && !(typeof data['annotation'] === 'string' || data['annotation'] instanceof String)) {
            throw new Error("Expected the field `annotation` to be a primitive type in the JSON string but got " + data['annotation']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }

        return true;
    }


}

ErrorsGroupDetails200Response.RequiredProperties = ["appVersion", "count", "deviceCount", "errorGroupId", "firstOccurrence", "lastOccurrence", "state"];

/**
 * @member {String} appBuild
 */
ErrorsGroupDetails200Response.prototype['appBuild'] = undefined;

/**
 * @member {String} appVersion
 */
ErrorsGroupDetails200Response.prototype['appVersion'] = undefined;

/**
 * @member {String} codeRaw
 */
ErrorsGroupDetails200Response.prototype['codeRaw'] = undefined;

/**
 * @member {Number} count
 */
ErrorsGroupDetails200Response.prototype['count'] = undefined;

/**
 * @member {Number} deviceCount
 */
ErrorsGroupDetails200Response.prototype['deviceCount'] = undefined;

/**
 * @member {String} errorGroupId
 */
ErrorsGroupDetails200Response.prototype['errorGroupId'] = undefined;

/**
 * @member {Boolean} exceptionAppCode
 */
ErrorsGroupDetails200Response.prototype['exceptionAppCode'] = undefined;

/**
 * @member {Boolean} exceptionClassMethod
 */
ErrorsGroupDetails200Response.prototype['exceptionClassMethod'] = undefined;

/**
 * @member {String} exceptionClassName
 */
ErrorsGroupDetails200Response.prototype['exceptionClassName'] = undefined;

/**
 * @member {String} exceptionFile
 */
ErrorsGroupDetails200Response.prototype['exceptionFile'] = undefined;

/**
 * @member {String} exceptionLine
 */
ErrorsGroupDetails200Response.prototype['exceptionLine'] = undefined;

/**
 * @member {String} exceptionMessage
 */
ErrorsGroupDetails200Response.prototype['exceptionMessage'] = undefined;

/**
 * @member {String} exceptionMethod
 */
ErrorsGroupDetails200Response.prototype['exceptionMethod'] = undefined;

/**
 * @member {String} exceptionType
 */
ErrorsGroupDetails200Response.prototype['exceptionType'] = undefined;

/**
 * @member {Date} firstOccurrence
 */
ErrorsGroupDetails200Response.prototype['firstOccurrence'] = undefined;

/**
 * @member {Boolean} hidden
 */
ErrorsGroupDetails200Response.prototype['hidden'] = undefined;

/**
 * @member {Date} lastOccurrence
 */
ErrorsGroupDetails200Response.prototype['lastOccurrence'] = undefined;

/**
 * @member {Array.<module:model/ErrorsGroupList200ResponseErrorGroupsInnerAllOfReasonFramesInner>} reasonFrames
 */
ErrorsGroupDetails200Response.prototype['reasonFrames'] = undefined;

/**
 * @member {String} annotation
 */
ErrorsGroupDetails200Response.prototype['annotation'] = undefined;

/**
 * @member {module:model/ErrorsGroupDetails200Response.StateEnum} state
 */
ErrorsGroupDetails200Response.prototype['state'] = undefined;





/**
 * Allowed values for the <code>state</code> property.
 * @enum {String}
 * @readonly
 */
ErrorsGroupDetails200Response['StateEnum'] = {

    /**
     * value: "open"
     * @const
     */
    "open": "open",

    /**
     * value: "closed"
     * @const
     */
    "closed": "closed",

    /**
     * value: "ignored"
     * @const
     */
    "ignored": "ignored"
};



export default ErrorsGroupDetails200Response;

