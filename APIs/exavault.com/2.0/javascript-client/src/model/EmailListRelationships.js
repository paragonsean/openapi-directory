/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import EmailListOwnerUser from './EmailListOwnerUser';

/**
 * The EmailListRelationships model module.
 * @module model/EmailListRelationships
 * @version 2.0
 */
class EmailListRelationships {
    /**
     * Constructs a new <code>EmailListRelationships</code>.
     * Related record summary info
     * @alias module:model/EmailListRelationships
     */
    constructor() { 
        
        EmailListRelationships.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EmailListRelationships</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EmailListRelationships} obj Optional instance to populate.
     * @return {module:model/EmailListRelationships} The populated <code>EmailListRelationships</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EmailListRelationships();

            if (data.hasOwnProperty('ownerUser')) {
                obj['ownerUser'] = EmailListOwnerUser.constructFromObject(data['ownerUser']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EmailListRelationships</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EmailListRelationships</code>.
     */
    static validateJSON(data) {
        // validate the optional field `ownerUser`
        if (data['ownerUser']) { // data not null
          EmailListOwnerUser.validateJSON(data['ownerUser']);
        }

        return true;
    }


}



/**
 * @member {module:model/EmailListOwnerUser} ownerUser
 */
EmailListRelationships.prototype['ownerUser'] = undefined;






export default EmailListRelationships;

