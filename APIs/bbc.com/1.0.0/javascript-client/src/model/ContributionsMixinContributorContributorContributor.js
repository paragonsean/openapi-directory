/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ContributionsMixinContributorName from './ContributionsMixinContributorName';

/**
 * The ContributionsMixinContributorContributorContributor model module.
 * @module model/ContributionsMixinContributorContributorContributor
 * @version 1.0.0
 */
class ContributionsMixinContributorContributorContributor {
    /**
     * Constructs a new <code>ContributionsMixinContributorContributorContributor</code>.
     * @alias module:model/ContributionsMixinContributorContributorContributor
     */
    constructor() { 
        
        ContributionsMixinContributorContributorContributor.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ContributionsMixinContributorContributorContributor</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContributionsMixinContributorContributorContributor} obj Optional instance to populate.
     * @return {module:model/ContributionsMixinContributorContributorContributor} The populated <code>ContributionsMixinContributorContributorContributor</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContributionsMixinContributorContributorContributor();

            if (data.hasOwnProperty('contributions_mixin_contributor_name')) {
                obj['contributions_mixin_contributor_name'] = ContributionsMixinContributorName.constructFromObject(data['contributions_mixin_contributor_name']);
            }
            if (data.hasOwnProperty('href')) {
                obj['href'] = ApiClient.convertToType(data['href'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ContributionsMixinContributorContributorContributor</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContributionsMixinContributorContributorContributor</code>.
     */
    static validateJSON(data) {
        // validate the optional field `contributions_mixin_contributor_name`
        if (data['contributions_mixin_contributor_name']) { // data not null
          ContributionsMixinContributorName.validateJSON(data['contributions_mixin_contributor_name']);
        }
        // ensure the json data is a string
        if (data['href'] && !(typeof data['href'] === 'string' || data['href'] instanceof String)) {
            throw new Error("Expected the field `href` to be a primitive type in the JSON string but got " + data['href']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/ContributionsMixinContributorName} contributions_mixin_contributor_name
 */
ContributionsMixinContributorContributorContributor.prototype['contributions_mixin_contributor_name'] = undefined;

/**
 * @member {String} href
 */
ContributionsMixinContributorContributorContributor.prototype['href'] = undefined;

/**
 * @member {String} type
 */
ContributionsMixinContributorContributorContributor.prototype['type'] = undefined;






export default ContributionsMixinContributorContributorContributor;

