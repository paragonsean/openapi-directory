/**
 * Chomp Food Database API Documentation
 * ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Subscription Options &raquo;](https://chompthis.com/api/)     * [Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php) 
 *
 * The version of the OpenAPI document: 1.0.0-oas3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BrandedFoodObjectItemsInnerCountryDetails from './BrandedFoodObjectItemsInnerCountryDetails';
import BrandedFoodObjectItemsInnerDietFlagsInner from './BrandedFoodObjectItemsInnerDietFlagsInner';
import BrandedFoodObjectItemsInnerDietLabels from './BrandedFoodObjectItemsInnerDietLabels';
import BrandedFoodObjectItemsInnerNutrientsInner from './BrandedFoodObjectItemsInnerNutrientsInner';
import BrandedFoodObjectItemsInnerPackage from './BrandedFoodObjectItemsInnerPackage';
import BrandedFoodObjectItemsInnerPackagingPhotos from './BrandedFoodObjectItemsInnerPackagingPhotos';
import BrandedFoodObjectItemsInnerServing from './BrandedFoodObjectItemsInnerServing';

/**
 * The BrandedFoodObjectItemsInner model module.
 * @module model/BrandedFoodObjectItemsInner
 * @version 1.0.0-oas3
 */
class BrandedFoodObjectItemsInner {
    /**
     * Constructs a new <code>BrandedFoodObjectItemsInner</code>.
     * An object containing information for this specific item.
     * @alias module:model/BrandedFoodObjectItemsInner
     */
    constructor() { 
        
        BrandedFoodObjectItemsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BrandedFoodObjectItemsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BrandedFoodObjectItemsInner} obj Optional instance to populate.
     * @return {module:model/BrandedFoodObjectItemsInner} The populated <code>BrandedFoodObjectItemsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BrandedFoodObjectItemsInner();

            if (data.hasOwnProperty('allergens')) {
                obj['allergens'] = ApiClient.convertToType(data['allergens'], ['String']);
            }
            if (data.hasOwnProperty('barcode')) {
                obj['barcode'] = ApiClient.convertToType(data['barcode'], 'String');
            }
            if (data.hasOwnProperty('brand')) {
                obj['brand'] = ApiClient.convertToType(data['brand'], 'String');
            }
            if (data.hasOwnProperty('brand_list')) {
                obj['brand_list'] = ApiClient.convertToType(data['brand_list'], ['String']);
            }
            if (data.hasOwnProperty('categories')) {
                obj['categories'] = ApiClient.convertToType(data['categories'], ['String']);
            }
            if (data.hasOwnProperty('countries')) {
                obj['countries'] = ApiClient.convertToType(data['countries'], ['String']);
            }
            if (data.hasOwnProperty('country_details')) {
                obj['country_details'] = BrandedFoodObjectItemsInnerCountryDetails.constructFromObject(data['country_details']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('diet_flags')) {
                obj['diet_flags'] = ApiClient.convertToType(data['diet_flags'], [BrandedFoodObjectItemsInnerDietFlagsInner]);
            }
            if (data.hasOwnProperty('diet_labels')) {
                obj['diet_labels'] = BrandedFoodObjectItemsInnerDietLabels.constructFromObject(data['diet_labels']);
            }
            if (data.hasOwnProperty('has_english_ingredients')) {
                obj['has_english_ingredients'] = ApiClient.convertToType(data['has_english_ingredients'], 'Boolean');
            }
            if (data.hasOwnProperty('ingredient_list')) {
                obj['ingredient_list'] = ApiClient.convertToType(data['ingredient_list'], ['String']);
            }
            if (data.hasOwnProperty('ingredients')) {
                obj['ingredients'] = ApiClient.convertToType(data['ingredients'], 'String');
            }
            if (data.hasOwnProperty('keywords')) {
                obj['keywords'] = ApiClient.convertToType(data['keywords'], ['String']);
            }
            if (data.hasOwnProperty('minerals')) {
                obj['minerals'] = ApiClient.convertToType(data['minerals'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('nutrients')) {
                obj['nutrients'] = ApiClient.convertToType(data['nutrients'], [BrandedFoodObjectItemsInnerNutrientsInner]);
            }
            if (data.hasOwnProperty('package')) {
                obj['package'] = BrandedFoodObjectItemsInnerPackage.constructFromObject(data['package']);
            }
            if (data.hasOwnProperty('packaging_photos')) {
                obj['packaging_photos'] = BrandedFoodObjectItemsInnerPackagingPhotos.constructFromObject(data['packaging_photos']);
            }
            if (data.hasOwnProperty('palm_oil_ingredients')) {
                obj['palm_oil_ingredients'] = ApiClient.convertToType(data['palm_oil_ingredients'], ['String']);
            }
            if (data.hasOwnProperty('serving')) {
                obj['serving'] = BrandedFoodObjectItemsInnerServing.constructFromObject(data['serving']);
            }
            if (data.hasOwnProperty('traces')) {
                obj['traces'] = ApiClient.convertToType(data['traces'], ['String']);
            }
            if (data.hasOwnProperty('vitamins')) {
                obj['vitamins'] = ApiClient.convertToType(data['vitamins'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BrandedFoodObjectItemsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BrandedFoodObjectItemsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['allergens'])) {
            throw new Error("Expected the field `allergens` to be an array in the JSON data but got " + data['allergens']);
        }
        // ensure the json data is a string
        if (data['barcode'] && !(typeof data['barcode'] === 'string' || data['barcode'] instanceof String)) {
            throw new Error("Expected the field `barcode` to be a primitive type in the JSON string but got " + data['barcode']);
        }
        // ensure the json data is a string
        if (data['brand'] && !(typeof data['brand'] === 'string' || data['brand'] instanceof String)) {
            throw new Error("Expected the field `brand` to be a primitive type in the JSON string but got " + data['brand']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['brand_list'])) {
            throw new Error("Expected the field `brand_list` to be an array in the JSON data but got " + data['brand_list']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['categories'])) {
            throw new Error("Expected the field `categories` to be an array in the JSON data but got " + data['categories']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['countries'])) {
            throw new Error("Expected the field `countries` to be an array in the JSON data but got " + data['countries']);
        }
        // validate the optional field `country_details`
        if (data['country_details']) { // data not null
          BrandedFoodObjectItemsInnerCountryDetails.validateJSON(data['country_details']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        if (data['diet_flags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['diet_flags'])) {
                throw new Error("Expected the field `diet_flags` to be an array in the JSON data but got " + data['diet_flags']);
            }
            // validate the optional field `diet_flags` (array)
            for (const item of data['diet_flags']) {
                BrandedFoodObjectItemsInnerDietFlagsInner.validateJSON(item);
            };
        }
        // validate the optional field `diet_labels`
        if (data['diet_labels']) { // data not null
          BrandedFoodObjectItemsInnerDietLabels.validateJSON(data['diet_labels']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['ingredient_list'])) {
            throw new Error("Expected the field `ingredient_list` to be an array in the JSON data but got " + data['ingredient_list']);
        }
        // ensure the json data is a string
        if (data['ingredients'] && !(typeof data['ingredients'] === 'string' || data['ingredients'] instanceof String)) {
            throw new Error("Expected the field `ingredients` to be a primitive type in the JSON string but got " + data['ingredients']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['keywords'])) {
            throw new Error("Expected the field `keywords` to be an array in the JSON data but got " + data['keywords']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['minerals'])) {
            throw new Error("Expected the field `minerals` to be an array in the JSON data but got " + data['minerals']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['nutrients']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['nutrients'])) {
                throw new Error("Expected the field `nutrients` to be an array in the JSON data but got " + data['nutrients']);
            }
            // validate the optional field `nutrients` (array)
            for (const item of data['nutrients']) {
                BrandedFoodObjectItemsInnerNutrientsInner.validateJSON(item);
            };
        }
        // validate the optional field `package`
        if (data['package']) { // data not null
          BrandedFoodObjectItemsInnerPackage.validateJSON(data['package']);
        }
        // validate the optional field `packaging_photos`
        if (data['packaging_photos']) { // data not null
          BrandedFoodObjectItemsInnerPackagingPhotos.validateJSON(data['packaging_photos']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['palm_oil_ingredients'])) {
            throw new Error("Expected the field `palm_oil_ingredients` to be an array in the JSON data but got " + data['palm_oil_ingredients']);
        }
        // validate the optional field `serving`
        if (data['serving']) { // data not null
          BrandedFoodObjectItemsInnerServing.validateJSON(data['serving']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['traces'])) {
            throw new Error("Expected the field `traces` to be an array in the JSON data but got " + data['traces']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['vitamins'])) {
            throw new Error("Expected the field `vitamins` to be an array in the JSON data but got " + data['vitamins']);
        }

        return true;
    }


}



/**
 * An array of ingredients in this item that may cause allergic reactions in people
 * @member {Array.<String>} allergens
 */
BrandedFoodObjectItemsInner.prototype['allergens'] = undefined;

/**
 * EAN/UPC barcode
 * @member {String} barcode
 */
BrandedFoodObjectItemsInner.prototype['barcode'] = undefined;

/**
 * The brand name that owns this item
 * @member {String} brand
 */
BrandedFoodObjectItemsInner.prototype['brand'] = undefined;

/**
 * An array of brands we have associated with this item. Some items are sold by more than 1 brand.
 * @member {Array.<String>} brand_list
 */
BrandedFoodObjectItemsInner.prototype['brand_list'] = undefined;

/**
 * @member {Array.<String>} categories
 */
BrandedFoodObjectItemsInner.prototype['categories'] = undefined;

/**
 * An array of countries where this item is sold
 * @member {Array.<String>} countries
 */
BrandedFoodObjectItemsInner.prototype['countries'] = undefined;

/**
 * @member {module:model/BrandedFoodObjectItemsInnerCountryDetails} country_details
 */
BrandedFoodObjectItemsInner.prototype['country_details'] = undefined;

/**
 * A description of this item
 * @member {String} description
 */
BrandedFoodObjectItemsInner.prototype['description'] = undefined;

/**
 * An array of ingredient objects that were flagged while grading this item for compatibility with each diet
 * @member {Array.<module:model/BrandedFoodObjectItemsInnerDietFlagsInner>} diet_flags
 */
BrandedFoodObjectItemsInner.prototype['diet_flags'] = undefined;

/**
 * @member {module:model/BrandedFoodObjectItemsInnerDietLabels} diet_labels
 */
BrandedFoodObjectItemsInner.prototype['diet_labels'] = undefined;

/**
 * A boolean indicating if we have English ingredients for this item
 * @member {Boolean} has_english_ingredients
 */
BrandedFoodObjectItemsInner.prototype['has_english_ingredients'] = undefined;

/**
 * An array of this item's ingredients
 * @member {Array.<String>} ingredient_list
 */
BrandedFoodObjectItemsInner.prototype['ingredient_list'] = undefined;

/**
 * This food item's ingredients from greatest quantity to least
 * @member {String} ingredients
 */
BrandedFoodObjectItemsInner.prototype['ingredients'] = undefined;

/**
 * An array of keywords that can be used to describe this item
 * @member {Array.<String>} keywords
 */
BrandedFoodObjectItemsInner.prototype['keywords'] = undefined;

/**
 * An array of minerals that this item contains
 * @member {Array.<String>} minerals
 */
BrandedFoodObjectItemsInner.prototype['minerals'] = undefined;

/**
 * Item name as provided by brand owner or as shown on packaging
 * @member {String} name
 */
BrandedFoodObjectItemsInner.prototype['name'] = undefined;

/**
 * An array containing nutrient informatio objects for this food item
 * @member {Array.<module:model/BrandedFoodObjectItemsInnerNutrientsInner>} nutrients
 */
BrandedFoodObjectItemsInner.prototype['nutrients'] = undefined;

/**
 * @member {module:model/BrandedFoodObjectItemsInnerPackage} package
 */
BrandedFoodObjectItemsInner.prototype['package'] = undefined;

/**
 * @member {module:model/BrandedFoodObjectItemsInnerPackagingPhotos} packaging_photos
 */
BrandedFoodObjectItemsInner.prototype['packaging_photos'] = undefined;

/**
 * An array of ingredients made from palm oil
 * @member {Array.<String>} palm_oil_ingredients
 */
BrandedFoodObjectItemsInner.prototype['palm_oil_ingredients'] = undefined;

/**
 * @member {module:model/BrandedFoodObjectItemsInnerServing} serving
 */
BrandedFoodObjectItemsInner.prototype['serving'] = undefined;

/**
 * An array of trace ingredients that may be found in this item
 * @member {Array.<String>} traces
 */
BrandedFoodObjectItemsInner.prototype['traces'] = undefined;

/**
 * An array of vitamins that are found in this item
 * @member {Array.<String>} vitamins
 */
BrandedFoodObjectItemsInner.prototype['vitamins'] = undefined;






export default BrandedFoodObjectItemsInner;

