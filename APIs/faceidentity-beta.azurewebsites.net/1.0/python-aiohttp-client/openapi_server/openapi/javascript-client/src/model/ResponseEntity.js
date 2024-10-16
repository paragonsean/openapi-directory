/**
 * Api Documentation
 * Api Documentation
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ResponseEntity model module.
 * @module model/ResponseEntity
 * @version 1.0
 */
class ResponseEntity {
    /**
     * Constructs a new <code>ResponseEntity</code>.
     * @alias module:model/ResponseEntity
     */
    constructor() { 
        
        ResponseEntity.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResponseEntity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResponseEntity} obj Optional instance to populate.
     * @return {module:model/ResponseEntity} The populated <code>ResponseEntity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResponseEntity();

            if (data.hasOwnProperty('body')) {
                obj['body'] = ApiClient.convertToType(data['body'], Object);
            }
            if (data.hasOwnProperty('statusCode')) {
                obj['statusCode'] = ApiClient.convertToType(data['statusCode'], 'String');
            }
            if (data.hasOwnProperty('statusCodeValue')) {
                obj['statusCodeValue'] = ApiClient.convertToType(data['statusCodeValue'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResponseEntity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResponseEntity</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['statusCode'] && !(typeof data['statusCode'] === 'string' || data['statusCode'] instanceof String)) {
            throw new Error("Expected the field `statusCode` to be a primitive type in the JSON string but got " + data['statusCode']);
        }

        return true;
    }


}



/**
 * @member {Object} body
 */
ResponseEntity.prototype['body'] = undefined;

/**
 * @member {module:model/ResponseEntity.StatusCodeEnum} statusCode
 */
ResponseEntity.prototype['statusCode'] = undefined;

/**
 * @member {Number} statusCodeValue
 */
ResponseEntity.prototype['statusCodeValue'] = undefined;





/**
 * Allowed values for the <code>statusCode</code> property.
 * @enum {String}
 * @readonly
 */
ResponseEntity['StatusCodeEnum'] = {

    /**
     * value: "100 CONTINUE"
     * @const
     */
    "100 CONTINUE": "100 CONTINUE",

    /**
     * value: "101 SWITCHING_PROTOCOLS"
     * @const
     */
    "101 SWITCHING_PROTOCOLS": "101 SWITCHING_PROTOCOLS",

    /**
     * value: "102 PROCESSING"
     * @const
     */
    "102 PROCESSING": "102 PROCESSING",

    /**
     * value: "103 CHECKPOINT"
     * @const
     */
    "103 CHECKPOINT": "103 CHECKPOINT",

    /**
     * value: "200 OK"
     * @const
     */
    "200 OK": "200 OK",

    /**
     * value: "201 CREATED"
     * @const
     */
    "201 CREATED": "201 CREATED",

    /**
     * value: "202 ACCEPTED"
     * @const
     */
    "202 ACCEPTED": "202 ACCEPTED",

    /**
     * value: "203 NON_AUTHORITATIVE_INFORMATION"
     * @const
     */
    "203 NON_AUTHORITATIVE_INFORMATION": "203 NON_AUTHORITATIVE_INFORMATION",

    /**
     * value: "204 NO_CONTENT"
     * @const
     */
    "204 NO_CONTENT": "204 NO_CONTENT",

    /**
     * value: "205 RESET_CONTENT"
     * @const
     */
    "205 RESET_CONTENT": "205 RESET_CONTENT",

    /**
     * value: "206 PARTIAL_CONTENT"
     * @const
     */
    "206 PARTIAL_CONTENT": "206 PARTIAL_CONTENT",

    /**
     * value: "207 MULTI_STATUS"
     * @const
     */
    "207 MULTI_STATUS": "207 MULTI_STATUS",

    /**
     * value: "208 ALREADY_REPORTED"
     * @const
     */
    "208 ALREADY_REPORTED": "208 ALREADY_REPORTED",

    /**
     * value: "226 IM_USED"
     * @const
     */
    "226 IM_USED": "226 IM_USED",

    /**
     * value: "300 MULTIPLE_CHOICES"
     * @const
     */
    "300 MULTIPLE_CHOICES": "300 MULTIPLE_CHOICES",

    /**
     * value: "301 MOVED_PERMANENTLY"
     * @const
     */
    "301 MOVED_PERMANENTLY": "301 MOVED_PERMANENTLY",

    /**
     * value: "302 FOUND"
     * @const
     */
    "302 FOUND": "302 FOUND",

    /**
     * value: "302 MOVED_TEMPORARILY"
     * @const
     */
    "302 MOVED_TEMPORARILY": "302 MOVED_TEMPORARILY",

    /**
     * value: "303 SEE_OTHER"
     * @const
     */
    "303 SEE_OTHER": "303 SEE_OTHER",

    /**
     * value: "304 NOT_MODIFIED"
     * @const
     */
    "304 NOT_MODIFIED": "304 NOT_MODIFIED",

    /**
     * value: "305 USE_PROXY"
     * @const
     */
    "305 USE_PROXY": "305 USE_PROXY",

    /**
     * value: "307 TEMPORARY_REDIRECT"
     * @const
     */
    "307 TEMPORARY_REDIRECT": "307 TEMPORARY_REDIRECT",

    /**
     * value: "308 PERMANENT_REDIRECT"
     * @const
     */
    "308 PERMANENT_REDIRECT": "308 PERMANENT_REDIRECT",

    /**
     * value: "400 BAD_REQUEST"
     * @const
     */
    "400 BAD_REQUEST": "400 BAD_REQUEST",

    /**
     * value: "401 UNAUTHORIZED"
     * @const
     */
    "401 UNAUTHORIZED": "401 UNAUTHORIZED",

    /**
     * value: "402 PAYMENT_REQUIRED"
     * @const
     */
    "402 PAYMENT_REQUIRED": "402 PAYMENT_REQUIRED",

    /**
     * value: "403 FORBIDDEN"
     * @const
     */
    "403 FORBIDDEN": "403 FORBIDDEN",

    /**
     * value: "404 NOT_FOUND"
     * @const
     */
    "404 NOT_FOUND": "404 NOT_FOUND",

    /**
     * value: "405 METHOD_NOT_ALLOWED"
     * @const
     */
    "405 METHOD_NOT_ALLOWED": "405 METHOD_NOT_ALLOWED",

    /**
     * value: "406 NOT_ACCEPTABLE"
     * @const
     */
    "406 NOT_ACCEPTABLE": "406 NOT_ACCEPTABLE",

    /**
     * value: "407 PROXY_AUTHENTICATION_REQUIRED"
     * @const
     */
    "407 PROXY_AUTHENTICATION_REQUIRED": "407 PROXY_AUTHENTICATION_REQUIRED",

    /**
     * value: "408 REQUEST_TIMEOUT"
     * @const
     */
    "408 REQUEST_TIMEOUT": "408 REQUEST_TIMEOUT",

    /**
     * value: "409 CONFLICT"
     * @const
     */
    "409 CONFLICT": "409 CONFLICT",

    /**
     * value: "410 GONE"
     * @const
     */
    "410 GONE": "410 GONE",

    /**
     * value: "411 LENGTH_REQUIRED"
     * @const
     */
    "411 LENGTH_REQUIRED": "411 LENGTH_REQUIRED",

    /**
     * value: "412 PRECONDITION_FAILED"
     * @const
     */
    "412 PRECONDITION_FAILED": "412 PRECONDITION_FAILED",

    /**
     * value: "413 PAYLOAD_TOO_LARGE"
     * @const
     */
    "413 PAYLOAD_TOO_LARGE": "413 PAYLOAD_TOO_LARGE",

    /**
     * value: "413 REQUEST_ENTITY_TOO_LARGE"
     * @const
     */
    "413 REQUEST_ENTITY_TOO_LARGE": "413 REQUEST_ENTITY_TOO_LARGE",

    /**
     * value: "414 URI_TOO_LONG"
     * @const
     */
    "414 URI_TOO_LONG": "414 URI_TOO_LONG",

    /**
     * value: "414 REQUEST_URI_TOO_LONG"
     * @const
     */
    "414 REQUEST_URI_TOO_LONG": "414 REQUEST_URI_TOO_LONG",

    /**
     * value: "415 UNSUPPORTED_MEDIA_TYPE"
     * @const
     */
    "415 UNSUPPORTED_MEDIA_TYPE": "415 UNSUPPORTED_MEDIA_TYPE",

    /**
     * value: "416 REQUESTED_RANGE_NOT_SATISFIABLE"
     * @const
     */
    "416 REQUESTED_RANGE_NOT_SATISFIABLE": "416 REQUESTED_RANGE_NOT_SATISFIABLE",

    /**
     * value: "417 EXPECTATION_FAILED"
     * @const
     */
    "417 EXPECTATION_FAILED": "417 EXPECTATION_FAILED",

    /**
     * value: "418 I_AM_A_TEAPOT"
     * @const
     */
    "418 I_AM_A_TEAPOT": "418 I_AM_A_TEAPOT",

    /**
     * value: "419 INSUFFICIENT_SPACE_ON_RESOURCE"
     * @const
     */
    "419 INSUFFICIENT_SPACE_ON_RESOURCE": "419 INSUFFICIENT_SPACE_ON_RESOURCE",

    /**
     * value: "420 METHOD_FAILURE"
     * @const
     */
    "420 METHOD_FAILURE": "420 METHOD_FAILURE",

    /**
     * value: "421 DESTINATION_LOCKED"
     * @const
     */
    "421 DESTINATION_LOCKED": "421 DESTINATION_LOCKED",

    /**
     * value: "422 UNPROCESSABLE_ENTITY"
     * @const
     */
    "422 UNPROCESSABLE_ENTITY": "422 UNPROCESSABLE_ENTITY",

    /**
     * value: "423 LOCKED"
     * @const
     */
    "423 LOCKED": "423 LOCKED",

    /**
     * value: "424 FAILED_DEPENDENCY"
     * @const
     */
    "424 FAILED_DEPENDENCY": "424 FAILED_DEPENDENCY",

    /**
     * value: "425 TOO_EARLY"
     * @const
     */
    "425 TOO_EARLY": "425 TOO_EARLY",

    /**
     * value: "426 UPGRADE_REQUIRED"
     * @const
     */
    "426 UPGRADE_REQUIRED": "426 UPGRADE_REQUIRED",

    /**
     * value: "428 PRECONDITION_REQUIRED"
     * @const
     */
    "428 PRECONDITION_REQUIRED": "428 PRECONDITION_REQUIRED",

    /**
     * value: "429 TOO_MANY_REQUESTS"
     * @const
     */
    "429 TOO_MANY_REQUESTS": "429 TOO_MANY_REQUESTS",

    /**
     * value: "431 REQUEST_HEADER_FIELDS_TOO_LARGE"
     * @const
     */
    "431 REQUEST_HEADER_FIELDS_TOO_LARGE": "431 REQUEST_HEADER_FIELDS_TOO_LARGE",

    /**
     * value: "451 UNAVAILABLE_FOR_LEGAL_REASONS"
     * @const
     */
    "451 UNAVAILABLE_FOR_LEGAL_REASONS": "451 UNAVAILABLE_FOR_LEGAL_REASONS",

    /**
     * value: "500 INTERNAL_SERVER_ERROR"
     * @const
     */
    "500 INTERNAL_SERVER_ERROR": "500 INTERNAL_SERVER_ERROR",

    /**
     * value: "501 NOT_IMPLEMENTED"
     * @const
     */
    "501 NOT_IMPLEMENTED": "501 NOT_IMPLEMENTED",

    /**
     * value: "502 BAD_GATEWAY"
     * @const
     */
    "502 BAD_GATEWAY": "502 BAD_GATEWAY",

    /**
     * value: "503 SERVICE_UNAVAILABLE"
     * @const
     */
    "503 SERVICE_UNAVAILABLE": "503 SERVICE_UNAVAILABLE",

    /**
     * value: "504 GATEWAY_TIMEOUT"
     * @const
     */
    "504 GATEWAY_TIMEOUT": "504 GATEWAY_TIMEOUT",

    /**
     * value: "505 HTTP_VERSION_NOT_SUPPORTED"
     * @const
     */
    "505 HTTP_VERSION_NOT_SUPPORTED": "505 HTTP_VERSION_NOT_SUPPORTED",

    /**
     * value: "506 VARIANT_ALSO_NEGOTIATES"
     * @const
     */
    "506 VARIANT_ALSO_NEGOTIATES": "506 VARIANT_ALSO_NEGOTIATES",

    /**
     * value: "507 INSUFFICIENT_STORAGE"
     * @const
     */
    "507 INSUFFICIENT_STORAGE": "507 INSUFFICIENT_STORAGE",

    /**
     * value: "508 LOOP_DETECTED"
     * @const
     */
    "508 LOOP_DETECTED": "508 LOOP_DETECTED",

    /**
     * value: "509 BANDWIDTH_LIMIT_EXCEEDED"
     * @const
     */
    "509 BANDWIDTH_LIMIT_EXCEEDED": "509 BANDWIDTH_LIMIT_EXCEEDED",

    /**
     * value: "510 NOT_EXTENDED"
     * @const
     */
    "510 NOT_EXTENDED": "510 NOT_EXTENDED",

    /**
     * value: "511 NETWORK_AUTHENTICATION_REQUIRED"
     * @const
     */
    "511 NETWORK_AUTHENTICATION_REQUIRED": "511 NETWORK_AUTHENTICATION_REQUIRED"
};



export default ResponseEntity;

