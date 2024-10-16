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
import IDemographicsDependentDomainObject from './IDemographicsDependentDomainObject';
import IFamilyHeadDomainObject from './IFamilyHeadDomainObject';

/**
 * The IDemographicsWithDependentsDomainObject model module.
 * @module model/IDemographicsWithDependentsDomainObject
 * @version v1
 */
class IDemographicsWithDependentsDomainObject {
    /**
     * Constructs a new <code>IDemographicsWithDependentsDomainObject</code>.
     * @alias module:model/IDemographicsWithDependentsDomainObject
     */
    constructor() { 
        
        IDemographicsWithDependentsDomainObject.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IDemographicsWithDependentsDomainObject</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IDemographicsWithDependentsDomainObject} obj Optional instance to populate.
     * @return {module:model/IDemographicsWithDependentsDomainObject} The populated <code>IDemographicsWithDependentsDomainObject</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IDemographicsWithDependentsDomainObject();

            if (data.hasOwnProperty('city')) {
                obj['city'] = ApiClient.convertToType(data['city'], 'String');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('demographicsId')) {
                obj['demographicsId'] = ApiClient.convertToType(data['demographicsId'], 'Number');
            }
            if (data.hasOwnProperty('dependents')) {
                obj['dependents'] = ApiClient.convertToType(data['dependents'], [IDemographicsDependentDomainObject]);
            }
            if (data.hasOwnProperty('externalDestinationId')) {
                obj['externalDestinationId'] = ApiClient.convertToType(data['externalDestinationId'], 'String');
            }
            if (data.hasOwnProperty('externalSourceId')) {
                obj['externalSourceId'] = ApiClient.convertToType(data['externalSourceId'], 'String');
            }
            if (data.hasOwnProperty('factFinderId')) {
                obj['factFinderId'] = ApiClient.convertToType(data['factFinderId'], 'Number');
            }
            if (data.hasOwnProperty('head1')) {
                obj['head1'] = IFamilyHeadDomainObject.constructFromObject(data['head1']);
            }
            if (data.hasOwnProperty('head2')) {
                obj['head2'] = IFamilyHeadDomainObject.constructFromObject(data['head2']);
            }
            if (data.hasOwnProperty('jointAnalysis')) {
                obj['jointAnalysis'] = ApiClient.convertToType(data['jointAnalysis'], 'Boolean');
            }
            if (data.hasOwnProperty('lockRetirement')) {
                obj['lockRetirement'] = ApiClient.convertToType(data['lockRetirement'], 'Boolean');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IDemographicsWithDependentsDomainObject</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IDemographicsWithDependentsDomainObject</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['city'] && !(typeof data['city'] === 'string' || data['city'] instanceof String)) {
            throw new Error("Expected the field `city` to be a primitive type in the JSON string but got " + data['city']);
        }
        if (data['dependents']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['dependents'])) {
                throw new Error("Expected the field `dependents` to be an array in the JSON data but got " + data['dependents']);
            }
            // validate the optional field `dependents` (array)
            for (const item of data['dependents']) {
                IDemographicsDependentDomainObject.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['externalDestinationId'] && !(typeof data['externalDestinationId'] === 'string' || data['externalDestinationId'] instanceof String)) {
            throw new Error("Expected the field `externalDestinationId` to be a primitive type in the JSON string but got " + data['externalDestinationId']);
        }
        // ensure the json data is a string
        if (data['externalSourceId'] && !(typeof data['externalSourceId'] === 'string' || data['externalSourceId'] instanceof String)) {
            throw new Error("Expected the field `externalSourceId` to be a primitive type in the JSON string but got " + data['externalSourceId']);
        }
        // validate the optional field `head1`
        if (data['head1']) { // data not null
          IFamilyHeadDomainObject.validateJSON(data['head1']);
        }
        // validate the optional field `head2`
        if (data['head2']) { // data not null
          IFamilyHeadDomainObject.validateJSON(data['head2']);
        }

        return true;
    }


}



/**
 * @member {String} city
 */
IDemographicsWithDependentsDomainObject.prototype['city'] = undefined;

/**
 * @member {Date} created
 */
IDemographicsWithDependentsDomainObject.prototype['created'] = undefined;

/**
 * @member {Number} demographicsId
 */
IDemographicsWithDependentsDomainObject.prototype['demographicsId'] = undefined;

/**
 * @member {Array.<module:model/IDemographicsDependentDomainObject>} dependents
 */
IDemographicsWithDependentsDomainObject.prototype['dependents'] = undefined;

/**
 * @member {String} externalDestinationId
 */
IDemographicsWithDependentsDomainObject.prototype['externalDestinationId'] = undefined;

/**
 * @member {String} externalSourceId
 */
IDemographicsWithDependentsDomainObject.prototype['externalSourceId'] = undefined;

/**
 * @member {Number} factFinderId
 */
IDemographicsWithDependentsDomainObject.prototype['factFinderId'] = undefined;

/**
 * @member {module:model/IFamilyHeadDomainObject} head1
 */
IDemographicsWithDependentsDomainObject.prototype['head1'] = undefined;

/**
 * @member {module:model/IFamilyHeadDomainObject} head2
 */
IDemographicsWithDependentsDomainObject.prototype['head2'] = undefined;

/**
 * @member {Boolean} jointAnalysis
 */
IDemographicsWithDependentsDomainObject.prototype['jointAnalysis'] = undefined;

/**
 * @member {Boolean} lockRetirement
 */
IDemographicsWithDependentsDomainObject.prototype['lockRetirement'] = undefined;

/**
 * @member {Number} state
 */
IDemographicsWithDependentsDomainObject.prototype['state'] = undefined;






export default IDemographicsWithDependentsDomainObject;

