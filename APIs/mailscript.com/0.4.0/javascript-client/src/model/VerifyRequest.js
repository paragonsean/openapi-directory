/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import VerifyEmailRequest from './VerifyEmailRequest';
import VerifySmsRequest from './VerifySmsRequest';

/**
 * The VerifyRequest model module.
 * @module model/VerifyRequest
 * @version 0.4.0
 */
class VerifyRequest {
    /**
     * Constructs a new <code>VerifyRequest</code>.
     * @alias module:model/VerifyRequest
     * @param {(module:model/VerifyEmailRequest|module:model/VerifySmsRequest)} instance The actual instance to initialize VerifyRequest.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "VerifyEmailRequest") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VerifyEmailRequest.validateJSON(instance); // throw an exception if no match
                // create VerifyEmailRequest from JS object
                this.actualInstance = VerifyEmailRequest.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VerifyEmailRequest
            errorMessages.push("Failed to construct VerifyEmailRequest: " + err)
        }

        try {
            if (typeof instance === "VerifySmsRequest") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VerifySmsRequest.validateJSON(instance); // throw an exception if no match
                // create VerifySmsRequest from JS object
                this.actualInstance = VerifySmsRequest.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VerifySmsRequest
            errorMessages.push("Failed to construct VerifySmsRequest: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `VerifyRequest` with oneOf schemas VerifyEmailRequest, VerifySmsRequest. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `VerifyRequest` with oneOf schemas VerifyEmailRequest, VerifySmsRequest. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>VerifyRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VerifyRequest} obj Optional instance to populate.
     * @return {module:model/VerifyRequest} The populated <code>VerifyRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        return new VerifyRequest(data);
    }

    /**
     * Gets the actual instance, which can be <code>VerifyEmailRequest</code>, <code>VerifySmsRequest</code>.
     * @return {(module:model/VerifyEmailRequest|module:model/VerifySmsRequest)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>VerifyEmailRequest</code>, <code>VerifySmsRequest</code>.
     * @param {(module:model/VerifyEmailRequest|module:model/VerifySmsRequest)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = VerifyRequest.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of VerifyRequest from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/VerifyRequest} An instance of VerifyRequest.
     */
    static fromJSON = function(json_string){
        return VerifyRequest.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {String} code
 */
VerifyRequest.prototype['code'] = undefined;

/**
 * @member {String} email
 */
VerifyRequest.prototype['email'] = undefined;

/**
 * @member {String} sms
 */
VerifyRequest.prototype['sms'] = undefined;


VerifyRequest.OneOf = ["VerifyEmailRequest", "VerifySmsRequest"];

export default VerifyRequest;

