/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ESAlgoSettings from './ESAlgoSettings';
import HSAlgoSettings from './HSAlgoSettings';
import JWKSAlgoSettings from './JWKSAlgoSettings';
import RSAlgoSettings from './RSAlgoSettings';

/**
 * The GlobalJwtVerifierAlgoSettings model module.
 * @module model/GlobalJwtVerifierAlgoSettings
 * @version 1.5.0-dev
 */
class GlobalJwtVerifierAlgoSettings {
    /**
     * Constructs a new <code>GlobalJwtVerifierAlgoSettings</code>.
     * @alias module:model/GlobalJwtVerifierAlgoSettings
     * @param {(module:model/ESAlgoSettings|module:model/HSAlgoSettings|module:model/JWKSAlgoSettings|module:model/RSAlgoSettings)} instance The actual instance to initialize GlobalJwtVerifierAlgoSettings.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "HSAlgoSettings") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                HSAlgoSettings.validateJSON(instance); // throw an exception if no match
                // create HSAlgoSettings from JS object
                this.actualInstance = HSAlgoSettings.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into HSAlgoSettings
            errorMessages.push("Failed to construct HSAlgoSettings: " + err)
        }

        try {
            if (typeof instance === "RSAlgoSettings") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                RSAlgoSettings.validateJSON(instance); // throw an exception if no match
                // create RSAlgoSettings from JS object
                this.actualInstance = RSAlgoSettings.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into RSAlgoSettings
            errorMessages.push("Failed to construct RSAlgoSettings: " + err)
        }

        try {
            if (typeof instance === "ESAlgoSettings") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                ESAlgoSettings.validateJSON(instance); // throw an exception if no match
                // create ESAlgoSettings from JS object
                this.actualInstance = ESAlgoSettings.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into ESAlgoSettings
            errorMessages.push("Failed to construct ESAlgoSettings: " + err)
        }

        try {
            if (typeof instance === "JWKSAlgoSettings") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                JWKSAlgoSettings.validateJSON(instance); // throw an exception if no match
                // create JWKSAlgoSettings from JS object
                this.actualInstance = JWKSAlgoSettings.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into JWKSAlgoSettings
            errorMessages.push("Failed to construct JWKSAlgoSettings: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `GlobalJwtVerifierAlgoSettings` with oneOf schemas ESAlgoSettings, HSAlgoSettings, JWKSAlgoSettings, RSAlgoSettings. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `GlobalJwtVerifierAlgoSettings` with oneOf schemas ESAlgoSettings, HSAlgoSettings, JWKSAlgoSettings, RSAlgoSettings. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>GlobalJwtVerifierAlgoSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GlobalJwtVerifierAlgoSettings} obj Optional instance to populate.
     * @return {module:model/GlobalJwtVerifierAlgoSettings} The populated <code>GlobalJwtVerifierAlgoSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        return new GlobalJwtVerifierAlgoSettings(data);
    }

    /**
     * Gets the actual instance, which can be <code>ESAlgoSettings</code>, <code>HSAlgoSettings</code>, <code>JWKSAlgoSettings</code>, <code>RSAlgoSettings</code>.
     * @return {(module:model/ESAlgoSettings|module:model/HSAlgoSettings|module:model/JWKSAlgoSettings|module:model/RSAlgoSettings)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>ESAlgoSettings</code>, <code>HSAlgoSettings</code>, <code>JWKSAlgoSettings</code>, <code>RSAlgoSettings</code>.
     * @param {(module:model/ESAlgoSettings|module:model/HSAlgoSettings|module:model/JWKSAlgoSettings|module:model/RSAlgoSettings)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = GlobalJwtVerifierAlgoSettings.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of GlobalJwtVerifierAlgoSettings from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/GlobalJwtVerifierAlgoSettings} An instance of GlobalJwtVerifierAlgoSettings.
     */
    static fromJSON = function(json_string){
        return GlobalJwtVerifierAlgoSettings.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * The secret value for the HMAC function
 * @member {String} secret
 */
GlobalJwtVerifierAlgoSettings.prototype['secret'] = undefined;

/**
 * Size for SHA function. can be 256, 384 or 512
 * @member {Number} size
 */
GlobalJwtVerifierAlgoSettings.prototype['size'] = undefined;

/**
 * String with value JWKSAlgoSettings
 * @member {String} type
 */
GlobalJwtVerifierAlgoSettings.prototype['type'] = undefined;

/**
 * The private key for the RSA function
 * @member {String} privateKey
 */
GlobalJwtVerifierAlgoSettings.prototype['privateKey'] = undefined;

/**
 * The public key for the RSA function
 * @member {String} publicKey
 */
GlobalJwtVerifierAlgoSettings.prototype['publicKey'] = undefined;

/**
 * The headers for the http call
 * @member {Object.<String, String>} headers
 */
GlobalJwtVerifierAlgoSettings.prototype['headers'] = undefined;

/**
 * The type of key: RSA or EC
 * @member {String} kty
 */
GlobalJwtVerifierAlgoSettings.prototype['kty'] = undefined;

/**
 * The timeout of the http call
 * @member {Number} timeout
 */
GlobalJwtVerifierAlgoSettings.prototype['timeout'] = undefined;

/**
 * The ttl of the keyset
 * @member {Number} ttl
 */
GlobalJwtVerifierAlgoSettings.prototype['ttl'] = undefined;

/**
 * The url for the http call
 * @member {String} url
 */
GlobalJwtVerifierAlgoSettings.prototype['url'] = undefined;


GlobalJwtVerifierAlgoSettings.OneOf = ["ESAlgoSettings", "HSAlgoSettings", "JWKSAlgoSettings", "RSAlgoSettings"];

export default GlobalJwtVerifierAlgoSettings;

