/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ResponseFive from './ResponseFive';
import ResponseSix from './ResponseSix';

/**
 * The GetDeviceCodeId500Response model module.
 * @module model/GetDeviceCodeId500Response
 * @version 1.0.0
 */
class GetDeviceCodeId500Response {
    /**
     * Constructs a new <code>GetDeviceCodeId500Response</code>.
     * @alias module:model/GetDeviceCodeId500Response
     * @param {(module:model/ResponseFive|module:model/ResponseSix)} instance The actual instance to initialize GetDeviceCodeId500Response.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "ResponseFive") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                ResponseFive.validateJSON(instance); // throw an exception if no match
                // create ResponseFive from JS object
                this.actualInstance = ResponseFive.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into ResponseFive
            errorMessages.push("Failed to construct ResponseFive: " + err)
        }

        try {
            if (typeof instance === "ResponseSix") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                ResponseSix.validateJSON(instance); // throw an exception if no match
                // create ResponseSix from JS object
                this.actualInstance = ResponseSix.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into ResponseSix
            errorMessages.push("Failed to construct ResponseSix: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `GetDeviceCodeId500Response` with oneOf schemas ResponseFive, ResponseSix. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `GetDeviceCodeId500Response` with oneOf schemas ResponseFive, ResponseSix. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>GetDeviceCodeId500Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetDeviceCodeId500Response} obj Optional instance to populate.
     * @return {module:model/GetDeviceCodeId500Response} The populated <code>GetDeviceCodeId500Response</code> instance.
     */
    static constructFromObject(data, obj) {
        return new GetDeviceCodeId500Response(data);
    }

    /**
     * Gets the actual instance, which can be <code>ResponseFive</code>, <code>ResponseSix</code>.
     * @return {(module:model/ResponseFive|module:model/ResponseSix)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>ResponseFive</code>, <code>ResponseSix</code>.
     * @param {(module:model/ResponseFive|module:model/ResponseSix)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = GetDeviceCodeId500Response.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of GetDeviceCodeId500Response from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/GetDeviceCodeId500Response} An instance of GetDeviceCodeId500Response.
     */
    static fromJSON = function(json_string){
        return GetDeviceCodeId500Response.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * unexpected_error
 * @member {String} error
 */
GetDeviceCodeId500Response.prototype['error'] = undefined;

/**
 * Internal server error
 * @member {String} error_description
 */
GetDeviceCodeId500Response.prototype['error_description'] = undefined;


GetDeviceCodeId500Response.OneOf = ["ResponseFive", "ResponseSix"];

export default GetDeviceCodeId500Response;

