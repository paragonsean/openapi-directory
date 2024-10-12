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
import CategoryFields from './CategoryFields';
import ImageFields from './ImageFields';
import VariantFields from './VariantFields';

/**
 * The ProductFields model module.
 * @module model/ProductFields
 * @version 1.0.0
 */
class ProductFields {
    /**
     * Constructs a new <code>ProductFields</code>.
     * @alias module:model/ProductFields
     */
    constructor() { 
        
        ProductFields.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['featured'] = false;
        obj['package_format'] = 'box';
        obj['status'] = 'available';
        obj['stock'] = 100;
        obj['weight'] = 1;
    }

    /**
     * Constructs a <code>ProductFields</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductFields} obj Optional instance to populate.
     * @return {module:model/ProductFields} The populated <code>ProductFields</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductFields();

            if (data.hasOwnProperty('barcode')) {
                obj['barcode'] = ApiClient.convertToType(data['barcode'], 'String');
            }
            if (data.hasOwnProperty('categories')) {
                obj['categories'] = ApiClient.convertToType(data['categories'], [CategoryFields]);
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('diameter')) {
                obj['diameter'] = ApiClient.convertToType(data['diameter'], 'Number');
            }
            if (data.hasOwnProperty('discount')) {
                obj['discount'] = ApiClient.convertToType(data['discount'], 'Number');
            }
            if (data.hasOwnProperty('featured')) {
                obj['featured'] = ApiClient.convertToType(data['featured'], 'Boolean');
            }
            if (data.hasOwnProperty('google_product_category')) {
                obj['google_product_category'] = ApiClient.convertToType(data['google_product_category'], 'String');
            }
            if (data.hasOwnProperty('height')) {
                obj['height'] = ApiClient.convertToType(data['height'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('images')) {
                obj['images'] = ApiClient.convertToType(data['images'], [ImageFields]);
            }
            if (data.hasOwnProperty('length')) {
                obj['length'] = ApiClient.convertToType(data['length'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('package_format')) {
                obj['package_format'] = ApiClient.convertToType(data['package_format'], 'String');
            }
            if (data.hasOwnProperty('permalink')) {
                obj['permalink'] = ApiClient.convertToType(data['permalink'], 'String');
            }
            if (data.hasOwnProperty('price')) {
                obj['price'] = ApiClient.convertToType(data['price'], 'Number');
            }
            if (data.hasOwnProperty('sku')) {
                obj['sku'] = ApiClient.convertToType(data['sku'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('stock')) {
                obj['stock'] = ApiClient.convertToType(data['stock'], 'Number');
            }
            if (data.hasOwnProperty('stock_unlimited')) {
                obj['stock_unlimited'] = ApiClient.convertToType(data['stock_unlimited'], 'Boolean');
            }
            if (data.hasOwnProperty('variants')) {
                obj['variants'] = ApiClient.convertToType(data['variants'], [VariantFields]);
            }
            if (data.hasOwnProperty('weight')) {
                obj['weight'] = ApiClient.convertToType(data['weight'], 'Number');
            }
            if (data.hasOwnProperty('width')) {
                obj['width'] = ApiClient.convertToType(data['width'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProductFields</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductFields</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['barcode'] && !(typeof data['barcode'] === 'string' || data['barcode'] instanceof String)) {
            throw new Error("Expected the field `barcode` to be a primitive type in the JSON string but got " + data['barcode']);
        }
        if (data['categories']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['categories'])) {
                throw new Error("Expected the field `categories` to be an array in the JSON data but got " + data['categories']);
            }
            // validate the optional field `categories` (array)
            for (const item of data['categories']) {
                CategoryFields.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['google_product_category'] && !(typeof data['google_product_category'] === 'string' || data['google_product_category'] instanceof String)) {
            throw new Error("Expected the field `google_product_category` to be a primitive type in the JSON string but got " + data['google_product_category']);
        }
        if (data['images']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['images'])) {
                throw new Error("Expected the field `images` to be an array in the JSON data but got " + data['images']);
            }
            // validate the optional field `images` (array)
            for (const item of data['images']) {
                ImageFields.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['package_format'] && !(typeof data['package_format'] === 'string' || data['package_format'] instanceof String)) {
            throw new Error("Expected the field `package_format` to be a primitive type in the JSON string but got " + data['package_format']);
        }
        // ensure the json data is a string
        if (data['permalink'] && !(typeof data['permalink'] === 'string' || data['permalink'] instanceof String)) {
            throw new Error("Expected the field `permalink` to be a primitive type in the JSON string but got " + data['permalink']);
        }
        // ensure the json data is a string
        if (data['sku'] && !(typeof data['sku'] === 'string' || data['sku'] instanceof String)) {
            throw new Error("Expected the field `sku` to be a primitive type in the JSON string but got " + data['sku']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        if (data['variants']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['variants'])) {
                throw new Error("Expected the field `variants` to be an array in the JSON data but got " + data['variants']);
            }
            // validate the optional field `variants` (array)
            for (const item of data['variants']) {
                VariantFields.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Barcode of the product
 * @member {String} barcode
 */
ProductFields.prototype['barcode'] = undefined;

/**
 * @member {Array.<module:model/CategoryFields>} categories
 */
ProductFields.prototype['categories'] = undefined;

/**
 * Date of product creation
 * @member {String} created_at
 */
ProductFields.prototype['created_at'] = undefined;

/**
 * Description of the product
 * @member {String} description
 */
ProductFields.prototype['description'] = undefined;

/**
 * Diameter of the product
 * @member {Number} diameter
 */
ProductFields.prototype['diameter'] = undefined;

/**
 * Discount of the product
 * @member {Number} discount
 */
ProductFields.prototype['discount'] = undefined;

/**
 * True if the product is featured
 * @member {Boolean} featured
 * @default false
 */
ProductFields.prototype['featured'] = false;

/**
 * Category of a Product based on the Google product taxonomy
 * @member {String} google_product_category
 */
ProductFields.prototype['google_product_category'] = undefined;

/**
 * Height of the product
 * @member {Number} height
 */
ProductFields.prototype['height'] = undefined;

/**
 * Unique identifier of the product
 * @member {Number} id
 */
ProductFields.prototype['id'] = undefined;

/**
 * @member {Array.<module:model/ImageFields>} images
 */
ProductFields.prototype['images'] = undefined;

/**
 * Length of the product
 * @member {Number} length
 */
ProductFields.prototype['length'] = undefined;

/**
 * Name of the product
 * @member {String} name
 */
ProductFields.prototype['name'] = undefined;

/**
 * Format the product package
 * @member {module:model/ProductFields.PackageFormatEnum} package_format
 * @default 'box'
 */
ProductFields.prototype['package_format'] = 'box';

/**
 * Product unique URL path
 * @member {String} permalink
 */
ProductFields.prototype['permalink'] = undefined;

/**
 * Price of the product
 * @member {Number} price
 */
ProductFields.prototype['price'] = undefined;

/**
 * Stock Keeping Unit of the product
 * @member {String} sku
 */
ProductFields.prototype['sku'] = undefined;

/**
 * Status of the product
 * @member {module:model/ProductFields.StatusEnum} status
 * @default 'available'
 */
ProductFields.prototype['status'] = 'available';

/**
 * Quantity in stock for the product
 * @member {Number} stock
 * @default 100
 */
ProductFields.prototype['stock'] = 100;

/**
 * True if the Product has unlimited stock
 * @member {Boolean} stock_unlimited
 */
ProductFields.prototype['stock_unlimited'] = undefined;

/**
 * @member {Array.<module:model/VariantFields>} variants
 */
ProductFields.prototype['variants'] = undefined;

/**
 * Weight of the product
 * @member {Number} weight
 * @default 1
 */
ProductFields.prototype['weight'] = 1;

/**
 * Width of the product
 * @member {Number} width
 */
ProductFields.prototype['width'] = undefined;





/**
 * Allowed values for the <code>package_format</code> property.
 * @enum {String}
 * @readonly
 */
ProductFields['PackageFormatEnum'] = {

    /**
     * value: "box"
     * @const
     */
    "box": "box",

    /**
     * value: "cylinder"
     * @const
     */
    "cylinder": "cylinder"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
ProductFields['StatusEnum'] = {

    /**
     * value: "available"
     * @const
     */
    "available": "available",

    /**
     * value: "not-available"
     * @const
     */
    "not-available": "not-available",

    /**
     * value: "disabled"
     * @const
     */
    "disabled": "disabled"
};



export default ProductFields;

