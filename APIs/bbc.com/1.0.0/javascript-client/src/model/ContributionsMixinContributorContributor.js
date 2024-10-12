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
import ContributionsMixinContributorContributorContributor from './ContributionsMixinContributorContributorContributor';
import ContributionsMixinContributorName from './ContributionsMixinContributorName';

/**
 * The ContributionsMixinContributorContributor model module.
 * @module model/ContributionsMixinContributorContributor
 * @version 1.0.0
 */
class ContributionsMixinContributorContributor {
    /**
     * Constructs a new <code>ContributionsMixinContributorContributor</code>.
     * @alias module:model/ContributionsMixinContributorContributor
     * @param contributor {module:model/ContributionsMixinContributorContributorContributor} 
     */
    constructor(contributor) { 
        
        ContributionsMixinContributorContributor.initialize(this, contributor);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, contributor) { 
        obj['contributor'] = contributor;
    }

    /**
     * Constructs a <code>ContributionsMixinContributorContributor</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContributionsMixinContributorContributor} obj Optional instance to populate.
     * @return {module:model/ContributionsMixinContributorContributor} The populated <code>ContributionsMixinContributorContributor</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContributionsMixinContributorContributor();

            if (data.hasOwnProperty('contributions_mixin_contributor_name')) {
                obj['contributions_mixin_contributor_name'] = ContributionsMixinContributorName.constructFromObject(data['contributions_mixin_contributor_name']);
            }
            if (data.hasOwnProperty('contributor')) {
                obj['contributor'] = ContributionsMixinContributorContributorContributor.constructFromObject(data['contributor']);
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
     * Validates the JSON data with respect to <code>ContributionsMixinContributorContributor</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContributionsMixinContributorContributor</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ContributionsMixinContributorContributor.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `contributions_mixin_contributor_name`
        if (data['contributions_mixin_contributor_name']) { // data not null
          ContributionsMixinContributorName.validateJSON(data['contributions_mixin_contributor_name']);
        }
        // validate the optional field `contributor`
        if (data['contributor']) { // data not null
          ContributionsMixinContributorContributorContributor.validateJSON(data['contributor']);
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

ContributionsMixinContributorContributor.RequiredProperties = ["contributor"];

/**
 * @member {module:model/ContributionsMixinContributorName} contributions_mixin_contributor_name
 */
ContributionsMixinContributorContributor.prototype['contributions_mixin_contributor_name'] = undefined;

/**
 * @member {module:model/ContributionsMixinContributorContributorContributor} contributor
 */
ContributionsMixinContributorContributor.prototype['contributor'] = undefined;

/**
 * @member {String} href
 */
ContributionsMixinContributorContributor.prototype['href'] = undefined;

/**
 * @member {String} type
 */
ContributionsMixinContributorContributor.prototype['type'] = undefined;






export default ContributionsMixinContributorContributor;

