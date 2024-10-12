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
import AlternateImagesMixinAlternateImages from './AlternateImagesMixinAlternateImages';

/**
 * The AlternateImagesMixin model module.
 * @module model/AlternateImagesMixin
 * @version 1.0.0
 */
class AlternateImagesMixin {
    /**
     * Constructs a new <code>AlternateImagesMixin</code>.
     * @alias module:model/AlternateImagesMixin
     * @param alternateImages {module:model/AlternateImagesMixinAlternateImages} 
     */
    constructor(alternateImages) { 
        
        AlternateImagesMixin.initialize(this, alternateImages);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, alternateImages) { 
        obj['alternate_images'] = alternateImages;
    }

    /**
     * Constructs a <code>AlternateImagesMixin</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AlternateImagesMixin} obj Optional instance to populate.
     * @return {module:model/AlternateImagesMixin} The populated <code>AlternateImagesMixin</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AlternateImagesMixin();

            if (data.hasOwnProperty('alternate_images')) {
                obj['alternate_images'] = AlternateImagesMixinAlternateImages.constructFromObject(data['alternate_images']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AlternateImagesMixin</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AlternateImagesMixin</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AlternateImagesMixin.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `alternate_images`
        if (data['alternate_images']) { // data not null
          AlternateImagesMixinAlternateImages.validateJSON(data['alternate_images']);
        }

        return true;
    }


}

AlternateImagesMixin.RequiredProperties = ["alternate_images"];

/**
 * @member {module:model/AlternateImagesMixinAlternateImages} alternate_images
 */
AlternateImagesMixin.prototype['alternate_images'] = undefined;






export default AlternateImagesMixin;

