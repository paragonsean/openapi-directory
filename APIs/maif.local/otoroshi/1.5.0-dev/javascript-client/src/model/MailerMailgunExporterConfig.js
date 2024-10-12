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

/**
 * The MailerMailgunExporterConfig model module.
 * @module model/MailerMailgunExporterConfig
 * @version 1.5.0-dev
 */
class MailerMailgunExporterConfig {
    /**
     * Constructs a new <code>MailerMailgunExporterConfig</code>.
     * @alias module:model/MailerMailgunExporterConfig
     * @param type {module:model/MailerMailgunExporterConfig.TypeEnum} Type of mailer
     */
    constructor(type) { 
        
        MailerMailgunExporterConfig.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
        obj['type'] = type;
    }

    /**
     * Constructs a <code>MailerMailgunExporterConfig</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MailerMailgunExporterConfig} obj Optional instance to populate.
     * @return {module:model/MailerMailgunExporterConfig} The populated <code>MailerMailgunExporterConfig</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MailerMailgunExporterConfig();

            if (data.hasOwnProperty('apiKey')) {
                obj['apiKey'] = ApiClient.convertToType(data['apiKey'], 'String');
            }
            if (data.hasOwnProperty('domain')) {
                obj['domain'] = ApiClient.convertToType(data['domain'], 'String');
            }
            if (data.hasOwnProperty('eu')) {
                obj['eu'] = ApiClient.convertToType(data['eu'], 'Boolean');
            }
            if (data.hasOwnProperty('to')) {
                obj['to'] = ApiClient.convertToType(data['to'], ['String']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MailerMailgunExporterConfig</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MailerMailgunExporterConfig</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of MailerMailgunExporterConfig.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['apiKey'] && !(typeof data['apiKey'] === 'string' || data['apiKey'] instanceof String)) {
            throw new Error("Expected the field `apiKey` to be a primitive type in the JSON string but got " + data['apiKey']);
        }
        // ensure the json data is a string
        if (data['domain'] && !(typeof data['domain'] === 'string' || data['domain'] instanceof String)) {
            throw new Error("Expected the field `domain` to be a primitive type in the JSON string but got " + data['domain']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['to'])) {
            throw new Error("Expected the field `to` to be an array in the JSON data but got " + data['to']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

MailerMailgunExporterConfig.RequiredProperties = ["type"];

/**
 * Mailgun apiKey
 * @member {String} apiKey
 */
MailerMailgunExporterConfig.prototype['apiKey'] = undefined;

/**
 * Mailgun domain
 * @member {String} domain
 */
MailerMailgunExporterConfig.prototype['domain'] = undefined;

/**
 * Whether the mailgun server is european
 * @member {Boolean} eu
 */
MailerMailgunExporterConfig.prototype['eu'] = undefined;

/**
 * Email adresses of recipents
 * @member {Array.<String>} to
 */
MailerMailgunExporterConfig.prototype['to'] = undefined;

/**
 * Type of mailer
 * @member {module:model/MailerMailgunExporterConfig.TypeEnum} type
 */
MailerMailgunExporterConfig.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
MailerMailgunExporterConfig['TypeEnum'] = {

    /**
     * value: "mailgun"
     * @const
     */
    "mailgun": "mailgun"
};



export default MailerMailgunExporterConfig;

