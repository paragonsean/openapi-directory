/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The IAccountHoldingDomainObject model module.
 * @module model/IAccountHoldingDomainObject
 * @version v1
 */
class IAccountHoldingDomainObject {
    /**
     * Constructs a new <code>IAccountHoldingDomainObject</code>.
     * @alias module:model/IAccountHoldingDomainObject
     */
    constructor() { 
        
        IAccountHoldingDomainObject.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IAccountHoldingDomainObject</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IAccountHoldingDomainObject} obj Optional instance to populate.
     * @return {module:model/IAccountHoldingDomainObject} The populated <code>IAccountHoldingDomainObject</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IAccountHoldingDomainObject();

            if (data.hasOwnProperty('accountHoldingId')) {
                obj['accountHoldingId'] = ApiClient.convertToType(data['accountHoldingId'], 'Number');
            }
            if (data.hasOwnProperty('accountId')) {
                obj['accountId'] = ApiClient.convertToType(data['accountId'], 'Number');
            }
            if (data.hasOwnProperty('costBasis')) {
                obj['costBasis'] = ApiClient.convertToType(data['costBasis'], 'Number');
            }
            if (data.hasOwnProperty('cusip')) {
                obj['cusip'] = ApiClient.convertToType(data['cusip'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('externalDestinationId')) {
                obj['externalDestinationId'] = ApiClient.convertToType(data['externalDestinationId'], 'String');
            }
            if (data.hasOwnProperty('heldAway')) {
                obj['heldAway'] = ApiClient.convertToType(data['heldAway'], 'Boolean');
            }
            if (data.hasOwnProperty('marketValue')) {
                obj['marketValue'] = ApiClient.convertToType(data['marketValue'], 'Number');
            }
            if (data.hasOwnProperty('symbol')) {
                obj['symbol'] = ApiClient.convertToType(data['symbol'], 'String');
            }
            if (data.hasOwnProperty('valuationDate')) {
                obj['valuationDate'] = ApiClient.convertToType(data['valuationDate'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IAccountHoldingDomainObject</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IAccountHoldingDomainObject</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['cusip'] && !(typeof data['cusip'] === 'string' || data['cusip'] instanceof String)) {
            throw new Error("Expected the field `cusip` to be a primitive type in the JSON string but got " + data['cusip']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['externalDestinationId'] && !(typeof data['externalDestinationId'] === 'string' || data['externalDestinationId'] instanceof String)) {
            throw new Error("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got " + data['externalDestinationId']);
        }
        // ensure the json data is a string
        if (data['symbol'] && !(typeof data['symbol'] === 'string' || data['symbol'] instanceof String)) {
            throw new Error("Expected the field `symbol` to be a primitive type in the JSON string but got " + data['symbol']);
        }

        return true;
    }


}



/**
 * @member {Number} accountHoldingId
 */
IAccountHoldingDomainObject.prototype['accountHoldingId'] = undefined;

/**
 * @member {Number} accountId
 */
IAccountHoldingDomainObject.prototype['accountId'] = undefined;

/**
 * @member {Number} costBasis
 */
IAccountHoldingDomainObject.prototype['costBasis'] = undefined;

/**
 * @member {String} cusip
 */
IAccountHoldingDomainObject.prototype['cusip'] = undefined;

/**
 * @member {String} description
 */
IAccountHoldingDomainObject.prototype['description'] = undefined;

/**
 * @member {String} externalDestinationId
 */
IAccountHoldingDomainObject.prototype['externalDestinationId'] = undefined;

/**
 * @member {Boolean} heldAway
 */
IAccountHoldingDomainObject.prototype['heldAway'] = undefined;

/**
 * @member {Number} marketValue
 */
IAccountHoldingDomainObject.prototype['marketValue'] = undefined;

/**
 * @member {String} symbol
 */
IAccountHoldingDomainObject.prototype['symbol'] = undefined;

/**
 * @member {Date} valuationDate
 */
IAccountHoldingDomainObject.prototype['valuationDate'] = undefined;






export default IAccountHoldingDomainObject;

