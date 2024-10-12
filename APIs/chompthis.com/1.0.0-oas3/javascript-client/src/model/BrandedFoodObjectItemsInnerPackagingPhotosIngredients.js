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

/**
 * The BrandedFoodObjectItemsInnerPackagingPhotosIngredients model module.
 * @module model/BrandedFoodObjectItemsInnerPackagingPhotosIngredients
 * @version 1.0.0-oas3
 */
class BrandedFoodObjectItemsInnerPackagingPhotosIngredients {
    /**
     * Constructs a new <code>BrandedFoodObjectItemsInnerPackagingPhotosIngredients</code>.
     * An object containing photos of the ingredients on this item&#39;s packaging
     * @alias module:model/BrandedFoodObjectItemsInnerPackagingPhotosIngredients
     */
    constructor() { 
        
        BrandedFoodObjectItemsInnerPackagingPhotosIngredients.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BrandedFoodObjectItemsInnerPackagingPhotosIngredients</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BrandedFoodObjectItemsInnerPackagingPhotosIngredients} obj Optional instance to populate.
     * @return {module:model/BrandedFoodObjectItemsInnerPackagingPhotosIngredients} The populated <code>BrandedFoodObjectItemsInnerPackagingPhotosIngredients</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BrandedFoodObjectItemsInnerPackagingPhotosIngredients();

            if (data.hasOwnProperty('display')) {
                obj['display'] = ApiClient.convertToType(data['display'], 'String');
            }
            if (data.hasOwnProperty('small')) {
                obj['small'] = ApiClient.convertToType(data['small'], 'String');
            }
            if (data.hasOwnProperty('thumb')) {
                obj['thumb'] = ApiClient.convertToType(data['thumb'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BrandedFoodObjectItemsInnerPackagingPhotosIngredients</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BrandedFoodObjectItemsInnerPackagingPhotosIngredients</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['display'] && !(typeof data['display'] === 'string' || data['display'] instanceof String)) {
            throw new Error("Expected the field `display` to be a primitive type in the JSON string but got " + data['display']);
        }
        // ensure the json data is a string
        if (data['small'] && !(typeof data['small'] === 'string' || data['small'] instanceof String)) {
            throw new Error("Expected the field `small` to be a primitive type in the JSON string but got " + data['small']);
        }
        // ensure the json data is a string
        if (data['thumb'] && !(typeof data['thumb'] === 'string' || data['thumb'] instanceof String)) {
            throw new Error("Expected the field `thumb` to be a primitive type in the JSON string but got " + data['thumb']);
        }

        return true;
    }


}



/**
 * Full-sized photo of the ingredients on this item's packaging
 * @member {String} display
 */
BrandedFoodObjectItemsInnerPackagingPhotosIngredients.prototype['display'] = undefined;

/**
 * Small photo of the ingredients on this item's packaging
 * @member {String} small
 */
BrandedFoodObjectItemsInnerPackagingPhotosIngredients.prototype['small'] = undefined;

/**
 * Thumbnail photo of the ingredients on this item's packaging
 * @member {String} thumb
 */
BrandedFoodObjectItemsInnerPackagingPhotosIngredients.prototype['thumb'] = undefined;






export default BrandedFoodObjectItemsInnerPackagingPhotosIngredients;

