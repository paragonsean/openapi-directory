/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ShareClassificationPolicies from './ShareClassificationPolicies';

/**
 * The UpdateClassificationPoliciesConfig model module.
 * @module model/UpdateClassificationPoliciesConfig
 * @version 4.42.3
 */
class UpdateClassificationPoliciesConfig {
    /**
     * Constructs a new <code>UpdateClassificationPoliciesConfig</code>.
     * Set of classification policies
     * @alias module:model/UpdateClassificationPoliciesConfig
     */
    constructor() { 
        
        UpdateClassificationPoliciesConfig.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateClassificationPoliciesConfig</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateClassificationPoliciesConfig} obj Optional instance to populate.
     * @return {module:model/UpdateClassificationPoliciesConfig} The populated <code>UpdateClassificationPoliciesConfig</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateClassificationPoliciesConfig();

            if (data.hasOwnProperty('shareClassificationPolicies')) {
                obj['shareClassificationPolicies'] = ShareClassificationPolicies.constructFromObject(data['shareClassificationPolicies']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateClassificationPoliciesConfig</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateClassificationPoliciesConfig</code>.
     */
    static validateJSON(data) {
        // validate the optional field `shareClassificationPolicies`
        if (data['shareClassificationPolicies']) { // data not null
          ShareClassificationPolicies.validateJSON(data['shareClassificationPolicies']);
        }

        return true;
    }


}



/**
 * @member {module:model/ShareClassificationPolicies} shareClassificationPolicies
 */
UpdateClassificationPoliciesConfig.prototype['shareClassificationPolicies'] = undefined;






export default UpdateClassificationPoliciesConfig;

