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
import PageCategory from './PageCategory';
import PageFieldsImage from './PageFieldsImage';

/**
 * The PageModifyFields model module.
 * @module model/PageModifyFields
 * @version 1.0.0
 */
class PageModifyFields {
    /**
     * Constructs a new <code>PageModifyFields</code>.
     * @alias module:model/PageModifyFields
     */
    constructor() { 
        
        PageModifyFields.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PageModifyFields</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PageModifyFields} obj Optional instance to populate.
     * @return {module:model/PageModifyFields} The populated <code>PageModifyFields</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PageModifyFields();

            if (data.hasOwnProperty('body')) {
                obj['body'] = ApiClient.convertToType(data['body'], 'String');
            }
            if (data.hasOwnProperty('categories')) {
                obj['categories'] = ApiClient.convertToType(data['categories'], [PageCategory]);
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = PageFieldsImage.constructFromObject(data['image']);
            }
            if (data.hasOwnProperty('meta_description')) {
                obj['meta_description'] = ApiClient.convertToType(data['meta_description'], 'String');
            }
            if (data.hasOwnProperty('page_title')) {
                obj['page_title'] = ApiClient.convertToType(data['page_title'], 'String');
            }
            if (data.hasOwnProperty('permalink')) {
                obj['permalink'] = ApiClient.convertToType(data['permalink'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('template')) {
                obj['template'] = ApiClient.convertToType(data['template'], 'Number');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PageModifyFields</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PageModifyFields</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['body'] && !(typeof data['body'] === 'string' || data['body'] instanceof String)) {
            throw new Error("Expected the field `body` to be a primitive type in the JSON string but got " + data['body']);
        }
        if (data['categories']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['categories'])) {
                throw new Error("Expected the field `categories` to be an array in the JSON data but got " + data['categories']);
            }
            // validate the optional field `categories` (array)
            for (const item of data['categories']) {
                PageCategory.validateJSON(item);
            };
        }
        // validate the optional field `image`
        if (data['image']) { // data not null
          PageFieldsImage.validateJSON(data['image']);
        }
        // ensure the json data is a string
        if (data['meta_description'] && !(typeof data['meta_description'] === 'string' || data['meta_description'] instanceof String)) {
            throw new Error("Expected the field `meta_description` to be a primitive type in the JSON string but got " + data['meta_description']);
        }
        // ensure the json data is a string
        if (data['page_title'] && !(typeof data['page_title'] === 'string' || data['page_title'] instanceof String)) {
            throw new Error("Expected the field `page_title` to be a primitive type in the JSON string but got " + data['page_title']);
        }
        // ensure the json data is a string
        if (data['permalink'] && !(typeof data['permalink'] === 'string' || data['permalink'] instanceof String)) {
            throw new Error("Expected the field `permalink` to be a primitive type in the JSON string but got " + data['permalink']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}



/**
 * Body of the Page
 * @member {String} body
 */
PageModifyFields.prototype['body'] = undefined;

/**
 * Page categories to which the Page belongs to
 * @member {Array.<module:model/PageCategory>} categories
 */
PageModifyFields.prototype['categories'] = undefined;

/**
 * @member {module:model/PageFieldsImage} image
 */
PageModifyFields.prototype['image'] = undefined;

/**
 * Meta description of the Page
 * @member {String} meta_description
 */
PageModifyFields.prototype['meta_description'] = undefined;

/**
 * Meta title of the Page
 * @member {String} page_title
 */
PageModifyFields.prototype['page_title'] = undefined;

/**
 * URL of the Page
 * @member {String} permalink
 */
PageModifyFields.prototype['permalink'] = undefined;

/**
 * Status of the Page
 * @member {module:model/PageModifyFields.StatusEnum} status
 */
PageModifyFields.prototype['status'] = undefined;

/**
 * ID of the Page template. Use null for the blank layout ('None')
 * @member {Number} template
 */
PageModifyFields.prototype['template'] = undefined;

/**
 * Title of the Page
 * @member {String} title
 */
PageModifyFields.prototype['title'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
PageModifyFields['StatusEnum'] = {

    /**
     * value: "public"
     * @const
     */
    "public": "public",

    /**
     * value: "draft"
     * @const
     */
    "draft": "draft",

    /**
     * value: "hidden"
     * @const
     */
    "hidden": "hidden"
};



export default PageModifyFields;

