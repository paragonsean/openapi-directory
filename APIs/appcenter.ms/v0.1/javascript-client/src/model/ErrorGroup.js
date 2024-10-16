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
 * The ErrorGroup model module.
 * @module model/ErrorGroup
 * @version v0.1
 */
class ErrorGroup {
    /**
     * Constructs a new <code>ErrorGroup</code>.
     * @alias module:model/ErrorGroup
     * @param state {module:model/ErrorGroup.StateEnum} 
     */
    constructor(state) { 
        
        ErrorGroup.initialize(this, state);
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
     * Constructs a <code>ErrorGroup</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ErrorGroup} obj Optional instance to populate.
     * @return {module:model/ErrorGroup} The populated <code>ErrorGroup</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ErrorGroup();

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
                obj['reasonFrames'] = ApiClient.convertToType(data['reasonFrames'], [Object]);
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
     * Validates the JSON data with respect to <code>ErrorGroup</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ErrorGroup</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ErrorGroup.RequiredProperties) {
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
                Object.validateJSON(item);
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

ErrorGroup.RequiredProperties = ["appVersion", "count", "deviceCount", "errorGroupId", "firstOccurrence", "lastOccurrence", "state"];

/**
 * @member {String} appBuild
 */
ErrorGroup.prototype['appBuild'] = undefined;

/**
 * @member {String} appVersion
 */
ErrorGroup.prototype['appVersion'] = undefined;

/**
 * @member {String} codeRaw
 */
ErrorGroup.prototype['codeRaw'] = undefined;

/**
 * @member {Number} count
 */
ErrorGroup.prototype['count'] = undefined;

/**
 * @member {Number} deviceCount
 */
ErrorGroup.prototype['deviceCount'] = undefined;

/**
 * @member {String} errorGroupId
 */
ErrorGroup.prototype['errorGroupId'] = undefined;

/**
 * @member {Boolean} exceptionAppCode
 */
ErrorGroup.prototype['exceptionAppCode'] = undefined;

/**
 * @member {Boolean} exceptionClassMethod
 */
ErrorGroup.prototype['exceptionClassMethod'] = undefined;

/**
 * @member {String} exceptionClassName
 */
ErrorGroup.prototype['exceptionClassName'] = undefined;

/**
 * @member {String} exceptionFile
 */
ErrorGroup.prototype['exceptionFile'] = undefined;

/**
 * @member {String} exceptionLine
 */
ErrorGroup.prototype['exceptionLine'] = undefined;

/**
 * @member {String} exceptionMessage
 */
ErrorGroup.prototype['exceptionMessage'] = undefined;

/**
 * @member {String} exceptionMethod
 */
ErrorGroup.prototype['exceptionMethod'] = undefined;

/**
 * @member {String} exceptionType
 */
ErrorGroup.prototype['exceptionType'] = undefined;

/**
 * @member {Date} firstOccurrence
 */
ErrorGroup.prototype['firstOccurrence'] = undefined;

/**
 * @member {Boolean} hidden
 */
ErrorGroup.prototype['hidden'] = undefined;

/**
 * @member {Date} lastOccurrence
 */
ErrorGroup.prototype['lastOccurrence'] = undefined;

/**
 * @member {Array.<Object>} reasonFrames
 */
ErrorGroup.prototype['reasonFrames'] = undefined;

/**
 * @member {String} annotation
 */
ErrorGroup.prototype['annotation'] = undefined;

/**
 * @member {module:model/ErrorGroup.StateEnum} state
 */
ErrorGroup.prototype['state'] = undefined;





/**
 * Allowed values for the <code>state</code> property.
 * @enum {String}
 * @readonly
 */
ErrorGroup['StateEnum'] = {

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



export default ErrorGroup;

