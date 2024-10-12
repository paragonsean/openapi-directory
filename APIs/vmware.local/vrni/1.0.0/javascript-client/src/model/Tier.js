/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BaseEntity from './BaseEntity';
import EntityType from './EntityType';
import GroupMembershipCriteria from './GroupMembershipCriteria';
import Reference from './Reference';

/**
 * The Tier model module.
 * @module model/Tier
 * @version 1.0.0
 */
class Tier {
    /**
     * Constructs a new <code>Tier</code>.
     * @alias module:model/Tier
     * @extends module:model/BaseEntity
     * @implements module:model/BaseEntity
     */
    constructor() { 
        BaseEntity.initialize(this);
        Tier.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Tier</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Tier} obj Optional instance to populate.
     * @return {module:model/Tier} The populated <code>Tier</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Tier();
            BaseEntity.constructFromObject(data, obj);
            BaseEntity.constructFromObject(data, obj);

            if (data.hasOwnProperty('application')) {
                obj['application'] = Reference.constructFromObject(data['application']);
            }
            if (data.hasOwnProperty('group_membership_criteria')) {
                obj['group_membership_criteria'] = ApiClient.convertToType(data['group_membership_criteria'], [GroupMembershipCriteria]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Tier</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Tier</code>.
     */
    static validateJSON(data) {
        // validate the optional field `application`
        if (data['application']) { // data not null
          Reference.validateJSON(data['application']);
        }
        if (data['group_membership_criteria']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['group_membership_criteria'])) {
                throw new Error("Expected the field `group_membership_criteria` to be an array in the JSON data but got " + data['group_membership_criteria']);
            }
            // validate the optional field `group_membership_criteria` (array)
            for (const item of data['group_membership_criteria']) {
                GroupMembershipCriteria.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/Reference} application
 */
Tier.prototype['application'] = undefined;

/**
 * @member {Array.<module:model/GroupMembershipCriteria>} group_membership_criteria
 */
Tier.prototype['group_membership_criteria'] = undefined;


// Implement BaseEntity interface:
/**
 * @member {String} entity_id
 */
BaseEntity.prototype['entity_id'] = undefined;
/**
 * @member {module:model/EntityType} entity_type
 */
BaseEntity.prototype['entity_type'] = undefined;
/**
 * @member {String} name
 */
BaseEntity.prototype['name'] = undefined;




export default Tier;

