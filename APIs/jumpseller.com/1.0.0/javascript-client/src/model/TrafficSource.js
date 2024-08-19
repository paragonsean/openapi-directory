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

/**
 * The TrafficSource model module.
 * @module model/TrafficSource
 * @version 1.0.0
 */
class TrafficSource {
    /**
     * Constructs a new <code>TrafficSource</code>.
     * @alias module:model/TrafficSource
     */
    constructor() { 
        
        TrafficSource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TrafficSource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TrafficSource} obj Optional instance to populate.
     * @return {module:model/TrafficSource} The populated <code>TrafficSource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TrafficSource();

            if (data.hasOwnProperty('campaign')) {
                obj['campaign'] = ApiClient.convertToType(data['campaign'], 'String');
            }
            if (data.hasOwnProperty('first_page_visited')) {
                obj['first_page_visited'] = ApiClient.convertToType(data['first_page_visited'], 'String');
            }
            if (data.hasOwnProperty('first_page_visited_at')) {
                obj['first_page_visited_at'] = ApiClient.convertToType(data['first_page_visited_at'], 'String');
            }
            if (data.hasOwnProperty('medium')) {
                obj['medium'] = ApiClient.convertToType(data['medium'], 'String');
            }
            if (data.hasOwnProperty('referral_code')) {
                obj['referral_code'] = ApiClient.convertToType(data['referral_code'], 'String');
            }
            if (data.hasOwnProperty('referral_source')) {
                obj['referral_source'] = ApiClient.convertToType(data['referral_source'], 'String');
            }
            if (data.hasOwnProperty('referral_url')) {
                obj['referral_url'] = ApiClient.convertToType(data['referral_url'], 'String');
            }
            if (data.hasOwnProperty('source_name')) {
                obj['source_name'] = ApiClient.convertToType(data['source_name'], 'String');
            }
            if (data.hasOwnProperty('user_agent')) {
                obj['user_agent'] = ApiClient.convertToType(data['user_agent'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TrafficSource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TrafficSource</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['campaign'] && !(typeof data['campaign'] === 'string' || data['campaign'] instanceof String)) {
            throw new Error("Expected the field `campaign` to be a primitive type in the JSON string but got " + data['campaign']);
        }
        // ensure the json data is a string
        if (data['first_page_visited'] && !(typeof data['first_page_visited'] === 'string' || data['first_page_visited'] instanceof String)) {
            throw new Error("Expected the field `first_page_visited` to be a primitive type in the JSON string but got " + data['first_page_visited']);
        }
        // ensure the json data is a string
        if (data['first_page_visited_at'] && !(typeof data['first_page_visited_at'] === 'string' || data['first_page_visited_at'] instanceof String)) {
            throw new Error("Expected the field `first_page_visited_at` to be a primitive type in the JSON string but got " + data['first_page_visited_at']);
        }
        // ensure the json data is a string
        if (data['medium'] && !(typeof data['medium'] === 'string' || data['medium'] instanceof String)) {
            throw new Error("Expected the field `medium` to be a primitive type in the JSON string but got " + data['medium']);
        }
        // ensure the json data is a string
        if (data['referral_code'] && !(typeof data['referral_code'] === 'string' || data['referral_code'] instanceof String)) {
            throw new Error("Expected the field `referral_code` to be a primitive type in the JSON string but got " + data['referral_code']);
        }
        // ensure the json data is a string
        if (data['referral_source'] && !(typeof data['referral_source'] === 'string' || data['referral_source'] instanceof String)) {
            throw new Error("Expected the field `referral_source` to be a primitive type in the JSON string but got " + data['referral_source']);
        }
        // ensure the json data is a string
        if (data['referral_url'] && !(typeof data['referral_url'] === 'string' || data['referral_url'] instanceof String)) {
            throw new Error("Expected the field `referral_url` to be a primitive type in the JSON string but got " + data['referral_url']);
        }
        // ensure the json data is a string
        if (data['source_name'] && !(typeof data['source_name'] === 'string' || data['source_name'] instanceof String)) {
            throw new Error("Expected the field `source_name` to be a primitive type in the JSON string but got " + data['source_name']);
        }
        // ensure the json data is a string
        if (data['user_agent'] && !(typeof data['user_agent'] === 'string' || data['user_agent'] instanceof String)) {
            throw new Error("Expected the field `user_agent` to be a primitive type in the JSON string but got " + data['user_agent']);
        }

        return true;
    }


}



/**
 * The campaign that referred the customer to the checkout
 * @member {String} campaign
 */
TrafficSource.prototype['campaign'] = undefined;

/**
 * The first url visited by the customer
 * @member {String} first_page_visited
 */
TrafficSource.prototype['first_page_visited'] = undefined;

/**
 * The date when the customer visited the first page
 * @member {String} first_page_visited_at
 */
TrafficSource.prototype['first_page_visited_at'] = undefined;

/**
 * The medium that referred the customer to the checkout
 * @member {String} medium
 */
TrafficSource.prototype['medium'] = undefined;

/**
 * The code that referred the customer to the checkout
 * @member {String} referral_code
 */
TrafficSource.prototype['referral_code'] = undefined;

/**
 * The source that referred the customer to the website
 * @member {String} referral_source
 */
TrafficSource.prototype['referral_source'] = undefined;

/**
 * The website that referred the customer to the checkout
 * @member {String} referral_url
 */
TrafficSource.prototype['referral_url'] = undefined;

/**
 * Where the checkout originated
 * @member {String} source_name
 */
TrafficSource.prototype['source_name'] = undefined;

/**
 * User agent of the referred request to checkout
 * @member {String} user_agent
 */
TrafficSource.prototype['user_agent'] = undefined;






export default TrafficSource;

