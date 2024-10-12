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
import ContributionsMixinContributorNameName from './ContributionsMixinContributorNameName';

/**
 * The ContributionsMixinContributorName model module.
 * @module model/ContributionsMixinContributorName
 * @version 1.0.0
 */
class ContributionsMixinContributorName {
    /**
     * Constructs a new <code>ContributionsMixinContributorName</code>.
     * @alias module:model/ContributionsMixinContributorName
     * @param name {module:model/ContributionsMixinContributorNameName} 
     */
    constructor(name) { 
        
        ContributionsMixinContributorName.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>ContributionsMixinContributorName</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ContributionsMixinContributorName} obj Optional instance to populate.
     * @return {module:model/ContributionsMixinContributorName} The populated <code>ContributionsMixinContributorName</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ContributionsMixinContributorName();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ContributionsMixinContributorNameName.constructFromObject(data['name']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ContributionsMixinContributorName</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ContributionsMixinContributorName</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ContributionsMixinContributorName.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `name`
        if (data['name']) { // data not null
          ContributionsMixinContributorNameName.validateJSON(data['name']);
        }

        return true;
    }


}

ContributionsMixinContributorName.RequiredProperties = ["name"];

/**
 * @member {module:model/ContributionsMixinContributorNameName} name
 */
ContributionsMixinContributorName.prototype['name'] = undefined;






export default ContributionsMixinContributorName;

