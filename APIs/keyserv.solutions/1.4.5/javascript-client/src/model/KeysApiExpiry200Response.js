/**
 * KeyServ
 * KeyServ API
 *
 * The version of the OpenAPI document: 1.4.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Expiry from './Expiry';

/**
 * The KeysApiExpiry200Response model module.
 * @module model/KeysApiExpiry200Response
 * @version 1.4.5
 */
class KeysApiExpiry200Response {
    /**
     * Constructs a new <code>KeysApiExpiry200Response</code>.
     * @alias module:model/KeysApiExpiry200Response
     * @param {(module:model/Expiry)} instance The actual instance to initialize KeysApiExpiry200Response.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "Expiry") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                Expiry.validateJSON(instance); // throw an exception if no match
                // create Expiry from JS object
                this.actualInstance = Expiry.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into Expiry
            errorMessages.push("Failed to construct Expiry: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `KeysApiExpiry200Response` with oneOf schemas Expiry. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `KeysApiExpiry200Response` with oneOf schemas Expiry. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>KeysApiExpiry200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/KeysApiExpiry200Response} obj Optional instance to populate.
     * @return {module:model/KeysApiExpiry200Response} The populated <code>KeysApiExpiry200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        return new KeysApiExpiry200Response(data);
    }

    /**
     * Gets the actual instance, which can be <code>Expiry</code>.
     * @return {(module:model/Expiry)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>Expiry</code>.
     * @param {(module:model/Expiry)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = KeysApiExpiry200Response.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of KeysApiExpiry200Response from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/KeysApiExpiry200Response} An instance of KeysApiExpiry200Response.
     */
    static fromJSON = function(json_string){
        return KeysApiExpiry200Response.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {Date} expires
 */
KeysApiExpiry200Response.prototype['expires'] = undefined;

/**
 * @member {String} time
 */
KeysApiExpiry200Response.prototype['time'] = undefined;


KeysApiExpiry200Response.OneOf = ["Expiry"];

export default KeysApiExpiry200Response;

