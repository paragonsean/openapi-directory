/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2019-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IssueListByService200ResponseValueInnerProperties from './IssueListByService200ResponseValueInnerProperties';

/**
 * The IssueListByService200ResponseValueInner model module.
 * @module model/IssueListByService200ResponseValueInner
 * @version 2019-01-01
 */
class IssueListByService200ResponseValueInner {
    /**
     * Constructs a new <code>IssueListByService200ResponseValueInner</code>.
     * Issue Contract details.
     * @alias module:model/IssueListByService200ResponseValueInner
     */
    constructor() { 
        
        IssueListByService200ResponseValueInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IssueListByService200ResponseValueInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IssueListByService200ResponseValueInner} obj Optional instance to populate.
     * @return {module:model/IssueListByService200ResponseValueInner} The populated <code>IssueListByService200ResponseValueInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IssueListByService200ResponseValueInner();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = IssueListByService200ResponseValueInnerProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IssueListByService200ResponseValueInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IssueListByService200ResponseValueInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          IssueListByService200ResponseValueInnerProperties.validateJSON(data['properties']);
        }

        return true;
    }


}



/**
 * @member {module:model/IssueListByService200ResponseValueInnerProperties} properties
 */
IssueListByService200ResponseValueInner.prototype['properties'] = undefined;






export default IssueListByService200ResponseValueInner;

