/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
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
import Id from './Id';

/**
 * The PromotionFields model module.
 * @module model/PromotionFields
 * @version 1.0.0
 */
class PromotionFields {
    /**
     * Constructs a new <code>PromotionFields</code>.
     * @alias module:model/PromotionFields
     */
    constructor() { 
        
        PromotionFields.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['cumulative'] = false;
        obj['enabled'] = true;
    }

    /**
     * Constructs a <code>PromotionFields</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PromotionFields} obj Optional instance to populate.
     * @return {module:model/PromotionFields} The populated <code>PromotionFields</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PromotionFields();

            if (data.hasOwnProperty('begins_at')) {
                obj['begins_at'] = ApiClient.convertToType(data['begins_at'], 'String');
            }
            if (data.hasOwnProperty('categories')) {
                obj['categories'] = ApiClient.convertToType(data['categories'], [Id]);
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('condition_price')) {
                obj['condition_price'] = ApiClient.convertToType(data['condition_price'], 'Number');
            }
            if (data.hasOwnProperty('condition_qty')) {
                obj['condition_qty'] = ApiClient.convertToType(data['condition_qty'], 'Number');
            }
            if (data.hasOwnProperty('cumulative')) {
                obj['cumulative'] = ApiClient.convertToType(data['cumulative'], 'Boolean');
            }
            if (data.hasOwnProperty('customer_categories')) {
                obj['customer_categories'] = ApiClient.convertToType(data['customer_categories'], [Id]);
            }
            if (data.hasOwnProperty('discount_amount_fix')) {
                obj['discount_amount_fix'] = ApiClient.convertToType(data['discount_amount_fix'], 'Number');
            }
            if (data.hasOwnProperty('discount_amount_percent')) {
                obj['discount_amount_percent'] = ApiClient.convertToType(data['discount_amount_percent'], 'Number');
            }
            if (data.hasOwnProperty('discount_target')) {
                obj['discount_target'] = ApiClient.convertToType(data['discount_target'], 'String');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('expires_at')) {
                obj['expires_at'] = ApiClient.convertToType(data['expires_at'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('lasts')) {
                obj['lasts'] = ApiClient.convertToType(data['lasts'], 'String');
            }
            if (data.hasOwnProperty('max_times_used')) {
                obj['max_times_used'] = ApiClient.convertToType(data['max_times_used'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('products')) {
                obj['products'] = ApiClient.convertToType(data['products'], [Id]);
            }
            if (data.hasOwnProperty('products_x')) {
                obj['products_x'] = ApiClient.convertToType(data['products_x'], [Id]);
            }
            if (data.hasOwnProperty('quantity_x')) {
                obj['quantity_x'] = ApiClient.convertToType(data['quantity_x'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('times_used')) {
                obj['times_used'] = ApiClient.convertToType(data['times_used'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PromotionFields</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PromotionFields</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['begins_at'] && !(typeof data['begins_at'] === 'string' || data['begins_at'] instanceof String)) {
            throw new Error("Expected the field `begins_at` to be a primitive type in the JSON string but got " + data['begins_at']);
        }
        if (data['categories']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['categories'])) {
                throw new Error("Expected the field `categories` to be an array in the JSON data but got " + data['categories']);
            }
            // validate the optional field `categories` (array)
            for (const item of data['categories']) {
                Id.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        if (data['customer_categories']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customer_categories'])) {
                throw new Error("Expected the field `customer_categories` to be an array in the JSON data but got " + data['customer_categories']);
            }
            // validate the optional field `customer_categories` (array)
            for (const item of data['customer_categories']) {
                Id.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['discount_target'] && !(typeof data['discount_target'] === 'string' || data['discount_target'] instanceof String)) {
            throw new Error("Expected the field `discount_target` to be a primitive type in the JSON string but got " + data['discount_target']);
        }
        // ensure the json data is a string
        if (data['expires_at'] && !(typeof data['expires_at'] === 'string' || data['expires_at'] instanceof String)) {
            throw new Error("Expected the field `expires_at` to be a primitive type in the JSON string but got " + data['expires_at']);
        }
        // ensure the json data is a string
        if (data['lasts'] && !(typeof data['lasts'] === 'string' || data['lasts'] instanceof String)) {
            throw new Error("Expected the field `lasts` to be a primitive type in the JSON string but got " + data['lasts']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['products']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['products'])) {
                throw new Error("Expected the field `products` to be an array in the JSON data but got " + data['products']);
            }
            // validate the optional field `products` (array)
            for (const item of data['products']) {
                Id.validateJSON(item);
            };
        }
        if (data['products_x']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['products_x'])) {
                throw new Error("Expected the field `products_x` to be an array in the JSON data but got " + data['products_x']);
            }
            // validate the optional field `products_x` (array)
            for (const item of data['products_x']) {
                Id.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * Creation date of the promotion (requires 'lasts' param - 'date')
 * @member {String} begins_at
 */
PromotionFields.prototype['begins_at'] = undefined;

/**
 * Products Categories where the promotion will be applied (requires 'discount_target' param - 'categories')
 * @member {Array.<module:model/Id>} categories
 */
PromotionFields.prototype['categories'] = undefined;

/**
 * Code of the promotion
 * @member {String} code
 */
PromotionFields.prototype['code'] = undefined;

/**
 * Minimum order amount to validate the promotion
 * @member {Number} condition_price
 */
PromotionFields.prototype['condition_price'] = undefined;

/**
 * Minimum quantity of ordered itens to validate the promotion
 * @member {Number} condition_qty
 */
PromotionFields.prototype['condition_qty'] = undefined;

/**
 * True if the promotion can be acumulated with others
 * @member {Boolean} cumulative
 * @default false
 */
PromotionFields.prototype['cumulative'] = false;

/**
 * Customer Categories to whom the promotion will be applied (requires 'customers' param - 'categories')
 * @member {Array.<module:model/Id>} customer_categories
 */
PromotionFields.prototype['customer_categories'] = undefined;

/**
 * Fixed discount amount of the promotion
 * @member {Number} discount_amount_fix
 */
PromotionFields.prototype['discount_amount_fix'] = undefined;

/**
 * Percentual discount amount of the promotion
 * @member {Number} discount_amount_percent
 */
PromotionFields.prototype['discount_amount_percent'] = undefined;

/**
 * Where the promotion will be applied ('order', 'shipping', 'categories', 'buy_x_get_y)
 * @member {String} discount_target
 */
PromotionFields.prototype['discount_target'] = undefined;

/**
 * If the promotion is currently enabled
 * @member {Boolean} enabled
 * @default true
 */
PromotionFields.prototype['enabled'] = true;

/**
 * Expiration date of the promotion (requires 'lasts' param - 'date')
 * @member {String} expires_at
 */
PromotionFields.prototype['expires_at'] = undefined;

/**
 * Unique identifier of the product
 * @member {Number} id
 */
PromotionFields.prototype['id'] = undefined;

/**
 * Controls when the promotion will expire ('none', 'date', 'max_times_used')
 * @member {String} lasts
 */
PromotionFields.prototype['lasts'] = undefined;

/**
 * Maximum amount a promotion can be used (requires 'lasts' param - 'max_times_used')
 * @member {Number} max_times_used
 */
PromotionFields.prototype['max_times_used'] = undefined;

/**
 * Name of the product
 * @member {String} name
 */
PromotionFields.prototype['name'] = undefined;

/**
 * Products where the promotion will be applied (requires 'discount_target' param - 'categories' or 'buy_x_get_y')
 * @member {Array.<module:model/Id>} products
 */
PromotionFields.prototype['products'] = undefined;

/**
 * Products required to apply the promotion (requires 'discount_target' param - 'buy_x_get_y')
 * @member {Array.<module:model/Id>} products_x
 */
PromotionFields.prototype['products_x'] = undefined;

/**
 * Number of sets of products_x needed to be able to apply the promotion (requires 'discount_target' param - 'buy_x_get_y')
 * @member {Number} quantity_x
 */
PromotionFields.prototype['quantity_x'] = undefined;

/**
 * Status of the promotion ('active', 'expired')
 * @member {String} status
 */
PromotionFields.prototype['status'] = undefined;

/**
 * Amount of times the promotion was used
 * @member {Number} times_used
 */
PromotionFields.prototype['times_used'] = undefined;






export default PromotionFields;

