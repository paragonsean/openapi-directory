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
import NewPartnerStore from './NewPartnerStore';
import NewPartnerStoreStore from './NewPartnerStoreStore';
import PartnerStoreStatus from './PartnerStoreStatus';
import PartnerStoreStatusStatus from './PartnerStoreStatusStatus';

/**
 * The StoreCheckStatusJsonGet200Response model module.
 * @module model/StoreCheckStatusJsonGet200Response
 * @version 1.0.0
 */
class StoreCheckStatusJsonGet200Response {
    /**
     * Constructs a new <code>StoreCheckStatusJsonGet200Response</code>.
     * @alias module:model/StoreCheckStatusJsonGet200Response
     * @param {(module:model/NewPartnerStore|module:model/PartnerStoreStatus)} instance The actual instance to initialize StoreCheckStatusJsonGet200Response.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "PartnerStoreStatus") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                PartnerStoreStatus.validateJSON(instance); // throw an exception if no match
                // create PartnerStoreStatus from JS object
                this.actualInstance = PartnerStoreStatus.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into PartnerStoreStatus
            errorMessages.push("Failed to construct PartnerStoreStatus: " + err)
        }

        try {
            if (typeof instance === "NewPartnerStore") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                NewPartnerStore.validateJSON(instance); // throw an exception if no match
                // create NewPartnerStore from JS object
                this.actualInstance = NewPartnerStore.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into NewPartnerStore
            errorMessages.push("Failed to construct NewPartnerStore: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `StoreCheckStatusJsonGet200Response` with oneOf schemas NewPartnerStore, PartnerStoreStatus. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `StoreCheckStatusJsonGet200Response` with oneOf schemas NewPartnerStore, PartnerStoreStatus. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>StoreCheckStatusJsonGet200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StoreCheckStatusJsonGet200Response} obj Optional instance to populate.
     * @return {module:model/StoreCheckStatusJsonGet200Response} The populated <code>StoreCheckStatusJsonGet200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        return new StoreCheckStatusJsonGet200Response(data);
    }

    /**
     * Gets the actual instance, which can be <code>NewPartnerStore</code>, <code>PartnerStoreStatus</code>.
     * @return {(module:model/NewPartnerStore|module:model/PartnerStoreStatus)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>NewPartnerStore</code>, <code>PartnerStoreStatus</code>.
     * @param {(module:model/NewPartnerStore|module:model/PartnerStoreStatus)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = StoreCheckStatusJsonGet200Response.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of StoreCheckStatusJsonGet200Response from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/StoreCheckStatusJsonGet200Response} An instance of StoreCheckStatusJsonGet200Response.
     */
    static fromJSON = function(json_string){
        return StoreCheckStatusJsonGet200Response.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {module:model/PartnerStoreStatusStatus} status
 */
StoreCheckStatusJsonGet200Response.prototype['status'] = undefined;

/**
 * @member {module:model/NewPartnerStoreStore} store
 */
StoreCheckStatusJsonGet200Response.prototype['store'] = undefined;


StoreCheckStatusJsonGet200Response.OneOf = ["NewPartnerStore", "PartnerStoreStatus"];

export default StoreCheckStatusJsonGet200Response;

