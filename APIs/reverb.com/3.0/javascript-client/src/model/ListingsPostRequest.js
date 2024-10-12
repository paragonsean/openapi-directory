/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ConversationsConversationIdOfferPostRequestPrice from './ConversationsConversationIdOfferPostRequestPrice';
import ListingsPostRequestCategoriesInner from './ListingsPostRequestCategoriesInner';
import ListingsPostRequestCondition from './ListingsPostRequestCondition';
import ListingsPostRequestLocation from './ListingsPostRequestLocation';
import ListingsPostRequestPreorderInfo from './ListingsPostRequestPreorderInfo';
import ListingsPostRequestSeller from './ListingsPostRequestSeller';
import ListingsPostRequestShipping from './ListingsPostRequestShipping';
import ListingsPostRequestVideosInner from './ListingsPostRequestVideosInner';

/**
 * The ListingsPostRequest model module.
 * @module model/ListingsPostRequest
 * @version 3.0
 */
class ListingsPostRequest {
    /**
     * Constructs a new <code>ListingsPostRequest</code>.
     * @alias module:model/ListingsPostRequest
     */
    constructor() { 
        
        ListingsPostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListingsPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListingsPostRequest} obj Optional instance to populate.
     * @return {module:model/ListingsPostRequest} The populated <code>ListingsPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListingsPostRequest();

            if (data.hasOwnProperty('categories')) {
                obj['categories'] = ApiClient.convertToType(data['categories'], [ListingsPostRequestCategoriesInner]);
            }
            if (data.hasOwnProperty('condition')) {
                obj['condition'] = ListingsPostRequestCondition.constructFromObject(data['condition']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('exclusive_channel')) {
                obj['exclusive_channel'] = ApiClient.convertToType(data['exclusive_channel'], 'String');
            }
            if (data.hasOwnProperty('finish')) {
                obj['finish'] = ApiClient.convertToType(data['finish'], 'String');
            }
            if (data.hasOwnProperty('has_inventory')) {
                obj['has_inventory'] = ApiClient.convertToType(data['has_inventory'], 'Boolean');
            }
            if (data.hasOwnProperty('inventory')) {
                obj['inventory'] = ApiClient.convertToType(data['inventory'], 'Number');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ListingsPostRequestLocation.constructFromObject(data['location']);
            }
            if (data.hasOwnProperty('make')) {
                obj['make'] = ApiClient.convertToType(data['make'], 'String');
            }
            if (data.hasOwnProperty('model')) {
                obj['model'] = ApiClient.convertToType(data['model'], 'String');
            }
            if (data.hasOwnProperty('multi_item')) {
                obj['multi_item'] = ApiClient.convertToType(data['multi_item'], 'Boolean');
            }
            if (data.hasOwnProperty('offers_enabled')) {
                obj['offers_enabled'] = ApiClient.convertToType(data['offers_enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('origin_country_code')) {
                obj['origin_country_code'] = ApiClient.convertToType(data['origin_country_code'], 'String');
            }
            if (data.hasOwnProperty('photos')) {
                obj['photos'] = ApiClient.convertToType(data['photos'], ['String']);
            }
            if (data.hasOwnProperty('preorder_info')) {
                obj['preorder_info'] = ListingsPostRequestPreorderInfo.constructFromObject(data['preorder_info']);
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ConversationsConversationIdOfferPostRequestPrice.constructFromObject(data['price']);
            }
            if (data.hasOwnProperty('prop_65_warning')) {
                obj['prop_65_warning'] = ApiClient.convertToType(data['prop_65_warning'], 'String');
            }
            if (data.hasOwnProperty('publish')) {
                obj['publish'] = ApiClient.convertToType(data['publish'], 'Boolean');
            }
            if (data.hasOwnProperty('seller')) {
                obj['seller'] = ListingsPostRequestSeller.constructFromObject(data['seller']);
            }
            if (data.hasOwnProperty('seller_cost')) {
                obj['seller_cost'] = ApiClient.convertToType(data['seller_cost'], 'String');
            }
            if (data.hasOwnProperty('shipping')) {
                obj['shipping'] = ListingsPostRequestShipping.constructFromObject(data['shipping']);
            }
            if (data.hasOwnProperty('shipping_profile_id')) {
                obj['shipping_profile_id'] = ApiClient.convertToType(data['shipping_profile_id'], 'String');
            }
            if (data.hasOwnProperty('shipping_profile_name')) {
                obj['shipping_profile_name'] = ApiClient.convertToType(data['shipping_profile_name'], 'String');
            }
            if (data.hasOwnProperty('sku')) {
                obj['sku'] = ApiClient.convertToType(data['sku'], 'String');
            }
            if (data.hasOwnProperty('sold_as_is')) {
                obj['sold_as_is'] = ApiClient.convertToType(data['sold_as_is'], 'Boolean');
            }
            if (data.hasOwnProperty('storage_location')) {
                obj['storage_location'] = ApiClient.convertToType(data['storage_location'], 'String');
            }
            if (data.hasOwnProperty('tax_exempt')) {
                obj['tax_exempt'] = ApiClient.convertToType(data['tax_exempt'], 'Boolean');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('upc')) {
                obj['upc'] = ApiClient.convertToType(data['upc'], 'String');
            }
            if (data.hasOwnProperty('upc_does_not_apply')) {
                obj['upc_does_not_apply'] = ApiClient.convertToType(data['upc_does_not_apply'], 'Boolean');
            }
            if (data.hasOwnProperty('videos')) {
                obj['videos'] = ApiClient.convertToType(data['videos'], [ListingsPostRequestVideosInner]);
            }
            if (data.hasOwnProperty('year')) {
                obj['year'] = ApiClient.convertToType(data['year'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListingsPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListingsPostRequest</code>.
     */
    static validateJSON(data) {
        if (data['categories']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['categories'])) {
                throw new Error("Expected the field `categories` to be an array in the JSON data but got " + data['categories']);
            }
            // validate the optional field `categories` (array)
            for (const item of data['categories']) {
                ListingsPostRequestCategoriesInner.validateJSON(item);
            };
        }
        // validate the optional field `condition`
        if (data['condition']) { // data not null
          ListingsPostRequestCondition.validateJSON(data['condition']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['exclusive_channel'] && !(typeof data['exclusive_channel'] === 'string' || data['exclusive_channel'] instanceof String)) {
            throw new Error("Expected the field `exclusive_channel` to be a primitive type in the JSON string but got " + data['exclusive_channel']);
        }
        // ensure the json data is a string
        if (data['finish'] && !(typeof data['finish'] === 'string' || data['finish'] instanceof String)) {
            throw new Error("Expected the field `finish` to be a primitive type in the JSON string but got " + data['finish']);
        }
        // validate the optional field `location`
        if (data['location']) { // data not null
          ListingsPostRequestLocation.validateJSON(data['location']);
        }
        // ensure the json data is a string
        if (data['make'] && !(typeof data['make'] === 'string' || data['make'] instanceof String)) {
            throw new Error("Expected the field `make` to be a primitive type in the JSON string but got " + data['make']);
        }
        // ensure the json data is a string
        if (data['model'] && !(typeof data['model'] === 'string' || data['model'] instanceof String)) {
            throw new Error("Expected the field `model` to be a primitive type in the JSON string but got " + data['model']);
        }
        // ensure the json data is a string
        if (data['origin_country_code'] && !(typeof data['origin_country_code'] === 'string' || data['origin_country_code'] instanceof String)) {
            throw new Error("Expected the field `origin_country_code` to be a primitive type in the JSON string but got " + data['origin_country_code']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['photos'])) {
            throw new Error("Expected the field `photos` to be an array in the JSON data but got " + data['photos']);
        }
        // validate the optional field `preorder_info`
        if (data['preorder_info']) { // data not null
          ListingsPostRequestPreorderInfo.validateJSON(data['preorder_info']);
        }
        // validate the optional field `price`
        if (data['price']) { // data not null
          ConversationsConversationIdOfferPostRequestPrice.validateJSON(data['price']);
        }
        // ensure the json data is a string
        if (data['prop_65_warning'] && !(typeof data['prop_65_warning'] === 'string' || data['prop_65_warning'] instanceof String)) {
            throw new Error("Expected the field `prop_65_warning` to be a primitive type in the JSON string but got " + data['prop_65_warning']);
        }
        // validate the optional field `seller`
        if (data['seller']) { // data not null
          ListingsPostRequestSeller.validateJSON(data['seller']);
        }
        // ensure the json data is a string
        if (data['seller_cost'] && !(typeof data['seller_cost'] === 'string' || data['seller_cost'] instanceof String)) {
            throw new Error("Expected the field `seller_cost` to be a primitive type in the JSON string but got " + data['seller_cost']);
        }
        // validate the optional field `shipping`
        if (data['shipping']) { // data not null
          ListingsPostRequestShipping.validateJSON(data['shipping']);
        }
        // ensure the json data is a string
        if (data['shipping_profile_id'] && !(typeof data['shipping_profile_id'] === 'string' || data['shipping_profile_id'] instanceof String)) {
            throw new Error("Expected the field `shipping_profile_id` to be a primitive type in the JSON string but got " + data['shipping_profile_id']);
        }
        // ensure the json data is a string
        if (data['shipping_profile_name'] && !(typeof data['shipping_profile_name'] === 'string' || data['shipping_profile_name'] instanceof String)) {
            throw new Error("Expected the field `shipping_profile_name` to be a primitive type in the JSON string but got " + data['shipping_profile_name']);
        }
        // ensure the json data is a string
        if (data['sku'] && !(typeof data['sku'] === 'string' || data['sku'] instanceof String)) {
            throw new Error("Expected the field `sku` to be a primitive type in the JSON string but got " + data['sku']);
        }
        // ensure the json data is a string
        if (data['storage_location'] && !(typeof data['storage_location'] === 'string' || data['storage_location'] instanceof String)) {
            throw new Error("Expected the field `storage_location` to be a primitive type in the JSON string but got " + data['storage_location']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['upc'] && !(typeof data['upc'] === 'string' || data['upc'] instanceof String)) {
            throw new Error("Expected the field `upc` to be a primitive type in the JSON string but got " + data['upc']);
        }
        if (data['videos']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['videos'])) {
                throw new Error("Expected the field `videos` to be an array in the JSON data but got " + data['videos']);
            }
            // validate the optional field `videos` (array)
            for (const item of data['videos']) {
                ListingsPostRequestVideosInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['year'] && !(typeof data['year'] === 'string' || data['year'] instanceof String)) {
            throw new Error("Expected the field `year` to be a primitive type in the JSON string but got " + data['year']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ListingsPostRequestCategoriesInner>} categories
 */
ListingsPostRequest.prototype['categories'] = undefined;

/**
 * @member {module:model/ListingsPostRequestCondition} condition
 */
ListingsPostRequest.prototype['condition'] = undefined;

/**
 * Product description. Please keep formatting to a minimum.
 * @member {String} description
 */
ListingsPostRequest.prototype['description'] = undefined;

/**
 * Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'
 * @member {module:model/ListingsPostRequest.ExclusiveChannelEnum} exclusive_channel
 */
ListingsPostRequest.prototype['exclusive_channel'] = undefined;

/**
 * Finish, e.g. 'Sunburst'
 * @member {String} finish
 */
ListingsPostRequest.prototype['finish'] = undefined;

/**
 * Set true if selling more than one
 * @member {Boolean} has_inventory
 */
ListingsPostRequest.prototype['has_inventory'] = undefined;

/**
 * Number of items available for sale. Reverb will increment and decrement automatically.
 * @member {Number} inventory
 */
ListingsPostRequest.prototype['inventory'] = undefined;

/**
 * @member {module:model/ListingsPostRequestLocation} location
 */
ListingsPostRequest.prototype['location'] = undefined;

/**
 * ex: Fender, Gibson
 * @member {String} make
 */
ListingsPostRequest.prototype['make'] = undefined;

/**
 * ex: Stratocaster, SG
 * @member {String} model
 */
ListingsPostRequest.prototype['model'] = undefined;

/**
 * Specifies if the listing is a bundle of multiple individual items
 * @member {Boolean} multi_item
 */
ListingsPostRequest.prototype['multi_item'] = undefined;

/**
 * Whether the listing accepts negotiated offers (default: true)
 * @member {Boolean} offers_enabled
 */
ListingsPostRequest.prototype['offers_enabled'] = undefined;

/**
 * Country of origin/manufacture, ISO code (e.g: US)
 * @member {String} origin_country_code
 */
ListingsPostRequest.prototype['origin_country_code'] = undefined;

/**
 * An array of image URLs. Ex: ['http://my.site.com/image.jpg']
 * @member {Array.<String>} photos
 */
ListingsPostRequest.prototype['photos'] = undefined;

/**
 * @member {module:model/ListingsPostRequestPreorderInfo} preorder_info
 */
ListingsPostRequest.prototype['preorder_info'] = undefined;

/**
 * @member {module:model/ConversationsConversationIdOfferPostRequestPrice} price
 */
ListingsPostRequest.prototype['price'] = undefined;

/**
 * If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required 'Warning' label and link to California's information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings
 * @member {String} prop_65_warning
 */
ListingsPostRequest.prototype['prop_65_warning'] = undefined;

/**
 * Publish your listing if draft
 * @member {Boolean} publish
 */
ListingsPostRequest.prototype['publish'] = undefined;

/**
 * @member {module:model/ListingsPostRequestSeller} seller
 */
ListingsPostRequest.prototype['seller'] = undefined;

/**
 * Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers)
 * @member {String} seller_cost
 */
ListingsPostRequest.prototype['seller_cost'] = undefined;

/**
 * @member {module:model/ListingsPostRequestShipping} shipping
 */
ListingsPostRequest.prototype['shipping'] = undefined;

/**
 * id of a shop's shipping profile
 * @member {String} shipping_profile_id
 */
ListingsPostRequest.prototype['shipping_profile_id'] = undefined;

/**
 * DEPRECATED, please use shipping_profile_id. Name of a shipping profile
 * @member {String} shipping_profile_name
 */
ListingsPostRequest.prototype['shipping_profile_name'] = undefined;

/**
 * Unique identifier for product
 * @member {String} sku
 */
ListingsPostRequest.prototype['sku'] = undefined;

/**
 * This item is sold As-Is and cannot be returned
 * @member {Boolean} sold_as_is
 */
ListingsPostRequest.prototype['sold_as_is'] = undefined;

/**
 * Internal note used by sellers to back reference their catalog system when entering a listing
 * @member {String} storage_location
 */
ListingsPostRequest.prototype['storage_location'] = undefined;

/**
 * Listing is exempt from taxes / VAT
 * @member {Boolean} tax_exempt
 */
ListingsPostRequest.prototype['tax_exempt'] = undefined;

/**
 * Title of your listing
 * @member {String} title
 */
ListingsPostRequest.prototype['title'] = undefined;

/**
 * Valid UPC code
 * @member {String} upc
 */
ListingsPostRequest.prototype['upc'] = undefined;

/**
 * True if a brand new product has no UPC code, ie for a handmade or custom item
 * @member {Boolean} upc_does_not_apply
 */
ListingsPostRequest.prototype['upc_does_not_apply'] = undefined;

/**
 * List of YouTube video urls. Note: ONLY ONE ALLOWED
 * @member {Array.<module:model/ListingsPostRequestVideosInner>} videos
 */
ListingsPostRequest.prototype['videos'] = undefined;

/**
 * Supports many formats. Ex: 1979, mid-70s, late 90s
 * @member {String} year
 */
ListingsPostRequest.prototype['year'] = undefined;





/**
 * Allowed values for the <code>exclusive_channel</code> property.
 * @enum {String}
 * @readonly
 */
ListingsPostRequest['ExclusiveChannelEnum'] = {

    /**
     * value: "seller_site"
     * @const
     */
    "seller_site": "seller_site",

    /**
     * value: "reverb"
     * @const
     */
    "reverb": "reverb",

    /**
     * value: "none"
     * @const
     */
    "none": "none"
};



export default ListingsPostRequest;

