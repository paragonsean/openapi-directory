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
 * The FulfillmentFields model module.
 * @module model/FulfillmentFields
 * @version 1.0.0
 */
class FulfillmentFields {
    /**
     * Constructs a new <code>FulfillmentFields</code>.
     * @alias module:model/FulfillmentFields
     */
    constructor() { 
        
        FulfillmentFields.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FulfillmentFields</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FulfillmentFields} obj Optional instance to populate.
     * @return {module:model/FulfillmentFields} The populated <code>FulfillmentFields</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FulfillmentFields();

            if (data.hasOwnProperty('external_id')) {
                obj['external_id'] = ApiClient.convertToType(data['external_id'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'String');
            }
            if (data.hasOwnProperty('service_type')) {
                obj['service_type'] = ApiClient.convertToType(data['service_type'], 'String');
            }
            if (data.hasOwnProperty('shipment_status')) {
                obj['shipment_status'] = ApiClient.convertToType(data['shipment_status'], 'String');
            }
            if (data.hasOwnProperty('tracking_company')) {
                obj['tracking_company'] = ApiClient.convertToType(data['tracking_company'], 'String');
            }
            if (data.hasOwnProperty('tracking_number')) {
                obj['tracking_number'] = ApiClient.convertToType(data['tracking_number'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FulfillmentFields</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FulfillmentFields</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['external_id'] && !(typeof data['external_id'] === 'string' || data['external_id'] instanceof String)) {
            throw new Error("Expected the field `external_id` to be a primitive type in the JSON string but got " + data['external_id']);
        }
        // ensure the json data is a string
        if (data['order_id'] && !(typeof data['order_id'] === 'string' || data['order_id'] instanceof String)) {
            throw new Error("Expected the field `order_id` to be a primitive type in the JSON string but got " + data['order_id']);
        }
        // ensure the json data is a string
        if (data['service_type'] && !(typeof data['service_type'] === 'string' || data['service_type'] instanceof String)) {
            throw new Error("Expected the field `service_type` to be a primitive type in the JSON string but got " + data['service_type']);
        }
        // ensure the json data is a string
        if (data['shipment_status'] && !(typeof data['shipment_status'] === 'string' || data['shipment_status'] instanceof String)) {
            throw new Error("Expected the field `shipment_status` to be a primitive type in the JSON string but got " + data['shipment_status']);
        }
        // ensure the json data is a string
        if (data['tracking_company'] && !(typeof data['tracking_company'] === 'string' || data['tracking_company'] instanceof String)) {
            throw new Error("Expected the field `tracking_company` to be a primitive type in the JSON string but got " + data['tracking_company']);
        }
        // ensure the json data is a string
        if (data['tracking_number'] && !(typeof data['tracking_number'] === 'string' || data['tracking_number'] instanceof String)) {
            throw new Error("Expected the field `tracking_number` to be a primitive type in the JSON string but got " + data['tracking_number']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * Unique identifier of the Fulfillment used by the tracking company
 * @member {String} external_id
 */
FulfillmentFields.prototype['external_id'] = undefined;

/**
 * Unique identifier of the Fulfillment
 * @member {Number} id
 */
FulfillmentFields.prototype['id'] = undefined;

/**
 * Order associated with the fulfillment
 * @member {String} order_id
 */
FulfillmentFields.prototype['order_id'] = undefined;

/**
 * Type of Service requested to the tracking company
 * @member {String} service_type
 */
FulfillmentFields.prototype['service_type'] = undefined;

/**
 * Status of the fulfillment
 * @member {String} shipment_status
 */
FulfillmentFields.prototype['shipment_status'] = undefined;

/**
 * Tracking company responsible for the fulfillment
 * @member {String} tracking_company
 */
FulfillmentFields.prototype['tracking_company'] = undefined;

/**
 * Tracking Number associated with the fulfillment
 * @member {String} tracking_number
 */
FulfillmentFields.prototype['tracking_number'] = undefined;

/**
 * Type of fulfillment Service used
 * @member {String} type
 */
FulfillmentFields.prototype['type'] = undefined;






export default FulfillmentFields;

