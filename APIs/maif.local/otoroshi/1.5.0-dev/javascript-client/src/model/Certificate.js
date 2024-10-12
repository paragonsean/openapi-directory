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
 * The Certificate model module.
 * @module model/Certificate
 * @version 1.5.0-dev
 */
class Certificate {
    /**
     * Constructs a new <code>Certificate</code>.
     * A SSL/TLS X509 certificate
     * @alias module:model/Certificate
     * @param autoRenew {String} Allow Otoroshi to renew the certificate (if self signed)
     * @param ca {String} Certificate is a CA (read only)
     * @param caRef {String} Reference for a CA certificate in otoroshi
     * @param chain {String} Certificate chain of trust in PEM format
     * @param domain {String} Domain of the certificate (read only)
     * @param from {String} Start date of validity
     * @param id {String} Id of the certificate
     * @param privateKey {String} PKCS8 private key in PEM format
     * @param selfSigned {String} Certificate is self signed  read only)
     * @param subject {String} Subject of the certificate (read only)
     * @param to {String} End date of validity
     * @param valid {String} Certificate is valid (read only)
     */
    constructor(autoRenew, ca, caRef, chain, domain, from, id, privateKey, selfSigned, subject, to, valid) { 
        
        Certificate.initialize(this, autoRenew, ca, caRef, chain, domain, from, id, privateKey, selfSigned, subject, to, valid);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, autoRenew, ca, caRef, chain, domain, from, id, privateKey, selfSigned, subject, to, valid) { 
        obj['autoRenew'] = autoRenew;
        obj['ca'] = ca;
        obj['caRef'] = caRef;
        obj['chain'] = chain;
        obj['domain'] = domain;
        obj['from'] = from;
        obj['id'] = id;
        obj['privateKey'] = privateKey;
        obj['selfSigned'] = selfSigned;
        obj['subject'] = subject;
        obj['to'] = to;
        obj['valid'] = valid;
    }

    /**
     * Constructs a <code>Certificate</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Certificate} obj Optional instance to populate.
     * @return {module:model/Certificate} The populated <code>Certificate</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Certificate();

            if (data.hasOwnProperty('autoRenew')) {
                obj['autoRenew'] = ApiClient.convertToType(data['autoRenew'], 'String');
            }
            if (data.hasOwnProperty('ca')) {
                obj['ca'] = ApiClient.convertToType(data['ca'], 'String');
            }
            if (data.hasOwnProperty('caRef')) {
                obj['caRef'] = ApiClient.convertToType(data['caRef'], 'String');
            }
            if (data.hasOwnProperty('chain')) {
                obj['chain'] = ApiClient.convertToType(data['chain'], 'String');
            }
            if (data.hasOwnProperty('domain')) {
                obj['domain'] = ApiClient.convertToType(data['domain'], 'String');
            }
            if (data.hasOwnProperty('from')) {
                obj['from'] = ApiClient.convertToType(data['from'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('privateKey')) {
                obj['privateKey'] = ApiClient.convertToType(data['privateKey'], 'String');
            }
            if (data.hasOwnProperty('selfSigned')) {
                obj['selfSigned'] = ApiClient.convertToType(data['selfSigned'], 'String');
            }
            if (data.hasOwnProperty('subject')) {
                obj['subject'] = ApiClient.convertToType(data['subject'], 'String');
            }
            if (data.hasOwnProperty('to')) {
                obj['to'] = ApiClient.convertToType(data['to'], 'String');
            }
            if (data.hasOwnProperty('valid')) {
                obj['valid'] = ApiClient.convertToType(data['valid'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Certificate</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Certificate</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Certificate.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['autoRenew'] && !(typeof data['autoRenew'] === 'string' || data['autoRenew'] instanceof String)) {
            throw new Error("Expected the field `autoRenew` to be a primitive type in the JSON string but got " + data['autoRenew']);
        }
        // ensure the json data is a string
        if (data['ca'] && !(typeof data['ca'] === 'string' || data['ca'] instanceof String)) {
            throw new Error("Expected the field `ca` to be a primitive type in the JSON string but got " + data['ca']);
        }
        // ensure the json data is a string
        if (data['caRef'] && !(typeof data['caRef'] === 'string' || data['caRef'] instanceof String)) {
            throw new Error("Expected the field `caRef` to be a primitive type in the JSON string but got " + data['caRef']);
        }
        // ensure the json data is a string
        if (data['chain'] && !(typeof data['chain'] === 'string' || data['chain'] instanceof String)) {
            throw new Error("Expected the field `chain` to be a primitive type in the JSON string but got " + data['chain']);
        }
        // ensure the json data is a string
        if (data['domain'] && !(typeof data['domain'] === 'string' || data['domain'] instanceof String)) {
            throw new Error("Expected the field `domain` to be a primitive type in the JSON string but got " + data['domain']);
        }
        // ensure the json data is a string
        if (data['from'] && !(typeof data['from'] === 'string' || data['from'] instanceof String)) {
            throw new Error("Expected the field `from` to be a primitive type in the JSON string but got " + data['from']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['privateKey'] && !(typeof data['privateKey'] === 'string' || data['privateKey'] instanceof String)) {
            throw new Error("Expected the field `privateKey` to be a primitive type in the JSON string but got " + data['privateKey']);
        }
        // ensure the json data is a string
        if (data['selfSigned'] && !(typeof data['selfSigned'] === 'string' || data['selfSigned'] instanceof String)) {
            throw new Error("Expected the field `selfSigned` to be a primitive type in the JSON string but got " + data['selfSigned']);
        }
        // ensure the json data is a string
        if (data['subject'] && !(typeof data['subject'] === 'string' || data['subject'] instanceof String)) {
            throw new Error("Expected the field `subject` to be a primitive type in the JSON string but got " + data['subject']);
        }
        // ensure the json data is a string
        if (data['to'] && !(typeof data['to'] === 'string' || data['to'] instanceof String)) {
            throw new Error("Expected the field `to` to be a primitive type in the JSON string but got " + data['to']);
        }
        // ensure the json data is a string
        if (data['valid'] && !(typeof data['valid'] === 'string' || data['valid'] instanceof String)) {
            throw new Error("Expected the field `valid` to be a primitive type in the JSON string but got " + data['valid']);
        }

        return true;
    }


}

Certificate.RequiredProperties = ["autoRenew", "ca", "caRef", "chain", "domain", "from", "id", "privateKey", "selfSigned", "subject", "to", "valid"];

/**
 * Allow Otoroshi to renew the certificate (if self signed)
 * @member {String} autoRenew
 */
Certificate.prototype['autoRenew'] = undefined;

/**
 * Certificate is a CA (read only)
 * @member {String} ca
 */
Certificate.prototype['ca'] = undefined;

/**
 * Reference for a CA certificate in otoroshi
 * @member {String} caRef
 */
Certificate.prototype['caRef'] = undefined;

/**
 * Certificate chain of trust in PEM format
 * @member {String} chain
 */
Certificate.prototype['chain'] = undefined;

/**
 * Domain of the certificate (read only)
 * @member {String} domain
 */
Certificate.prototype['domain'] = undefined;

/**
 * Start date of validity
 * @member {String} from
 */
Certificate.prototype['from'] = undefined;

/**
 * Id of the certificate
 * @member {String} id
 */
Certificate.prototype['id'] = undefined;

/**
 * PKCS8 private key in PEM format
 * @member {String} privateKey
 */
Certificate.prototype['privateKey'] = undefined;

/**
 * Certificate is self signed  read only)
 * @member {String} selfSigned
 */
Certificate.prototype['selfSigned'] = undefined;

/**
 * Subject of the certificate (read only)
 * @member {String} subject
 */
Certificate.prototype['subject'] = undefined;

/**
 * End date of validity
 * @member {String} to
 */
Certificate.prototype['to'] = undefined;

/**
 * Certificate is valid (read only)
 * @member {String} valid
 */
Certificate.prototype['valid'] = undefined;






export default Certificate;

