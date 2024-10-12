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
import GlobalJwtVerifierAlgoSettings from './GlobalJwtVerifierAlgoSettings';
import TransformSettings from './TransformSettings';
import VerificationSettings from './VerificationSettings';

/**
 * The Transform model module.
 * @module model/Transform
 * @version 1.5.0-dev
 */
class Transform {
    /**
     * Constructs a new <code>Transform</code>.
     * Strategy where signature and field values are verified, trasnformed and then token si re-signed
     * @alias module:model/Transform
     * @param algoSettings {module:model/GlobalJwtVerifierAlgoSettings} 
     * @param type {String} String with value Transform
     * @param verificationSettings {module:model/VerificationSettings} 
     */
    constructor(algoSettings, type, verificationSettings) { 
        
        Transform.initialize(this, algoSettings, type, verificationSettings);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, algoSettings, type, verificationSettings) { 
        obj['algoSettings'] = algoSettings;
        obj['type'] = type;
        obj['verificationSettings'] = verificationSettings;
    }

    /**
     * Constructs a <code>Transform</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Transform} obj Optional instance to populate.
     * @return {module:model/Transform} The populated <code>Transform</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Transform();

            if (data.hasOwnProperty('algoSettings')) {
                obj['algoSettings'] = GlobalJwtVerifierAlgoSettings.constructFromObject(data['algoSettings']);
            }
            if (data.hasOwnProperty('transformSettings')) {
                obj['transformSettings'] = TransformSettings.constructFromObject(data['transformSettings']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('verificationSettings')) {
                obj['verificationSettings'] = VerificationSettings.constructFromObject(data['verificationSettings']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Transform</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Transform</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Transform.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `algoSettings`
        if (data['algoSettings']) { // data not null
          GlobalJwtVerifierAlgoSettings.validateJSON(data['algoSettings']);
        }
        // validate the optional field `transformSettings`
        if (data['transformSettings']) { // data not null
          TransformSettings.validateJSON(data['transformSettings']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // validate the optional field `verificationSettings`
        if (data['verificationSettings']) { // data not null
          VerificationSettings.validateJSON(data['verificationSettings']);
        }

        return true;
    }


}

Transform.RequiredProperties = ["algoSettings", "type", "verificationSettings"];

/**
 * @member {module:model/GlobalJwtVerifierAlgoSettings} algoSettings
 */
Transform.prototype['algoSettings'] = undefined;

/**
 * @member {module:model/TransformSettings} transformSettings
 */
Transform.prototype['transformSettings'] = undefined;

/**
 * String with value Transform
 * @member {String} type
 */
Transform.prototype['type'] = undefined;

/**
 * @member {module:model/VerificationSettings} verificationSettings
 */
Transform.prototype['verificationSettings'] = undefined;






export default Transform;

