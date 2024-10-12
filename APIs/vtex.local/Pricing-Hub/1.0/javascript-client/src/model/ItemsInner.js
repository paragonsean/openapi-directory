/**
 * Pricing Hub
 * > This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests).      In the B2B scenario, it is common for stores to have personalized prices per customer and complex pricing systems that require external integrations. Pricing Hub is a system developed for the B2B context that works as an intermediary between VTEX and external pricing systems.     In VTEX, B2B stores have the option to use our internal pricing system or an external one. If the store chooses to operate with an external pricing system, Pricing Hub will query an external price calculation API. The external API should then respond with the price for all items in the shopping cart according to its predefined tax rules.    ![Pricing hub protocal diagram](https://user-images.githubusercontent.com/77292838/211634260-e4f7a516-91df-416e-ab43-d9c79d56bc91.png)    ## Implementation    To connect with external pricing systems using Pricing Hub, it is necessary to build a VTEX IO middleware app. We offer two reference implementation templates to simplify this process:    - [C# template](https://github.com/vtex-apps/external-prices-app)  - [Node template](https://github.com/vtex-apps/external-prices-node)    Read the documentation on each repository to learn more about the required steps to use and customize the app.    > The app used by Pricing Hub to connect must be a `major 0`.     ## Specifications    See below all the specifications of the request and the response expected when communicating with Pricing Hub.    ### Price calculation request    The external prices calculation tool must provide an endpoint that will receive a `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices) request. This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.    >⚠️ Responses from Pricing Hub tend to have a greater delay when compared to other VTEX systems. That is expected, however, due to the complexity of its nested requests. The timeout for this request is 900 milliseconds.    In this request, Pricing Hub provides a body in a specific format, exemplified below. This means that either the endpoint must be prepared to receive this body format, or the app must contain a parser to adapt it to the correct format.    #### Request body example    ```json  {      \"item\":           {              \"index\": 0,              \"skuId\": \"880011\",              \"quantity\": 1          },      \"context\":{          \"email\": \"john@email.com\"      }  }  ```    The request body should have the following properties:    | **Attribute** | **Type** | **Description**                                                                                                                                                                                          |  |---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`        | object   | The item whose price is supposed to be fetched by Pricing Hub.                                                                                                                                           |  | ↪ `index`     | integer  | This is the index of the item at Checkout's cart. It has to be unique in the items array.                                                                                                                |  | ↪ `skuId`     | string   | This is the SKU ID of the item that will be priced.                                                                                                                                                      |  | ↪ `quantity`  | integer  | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price. |  | `context`     | object   | The object that contains the context to inform the query.                                                                                                                                                |  | ↪ `email`     | string   | The customer's email address. If there is no value, use an empty string.                                                                                                                                 |    ### External prices provider response    In response to the request sent by Pricing Hub, we expect an outcome in the following format:    ```json  {      \"item\": {          \"price\": 54035,          \"priceTables\": \"special\",          \"index\": 0,          \"skuId\": \"880011\",          \"listPrice\": 54035,          \"costPrice\": 50000,          \"sellingPrice\": 54035,          \"priceValidUntil\": \"2023-01-27T20:29:57Z\",          \"tradePolicyId\": \"special\"      }  }  ```    The response should have the following properties:    | **Attribute**       | **Type** | **Description**                                                                                                                                        |  |---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`              | object   | The object that contains the price data.                                                                                                               |  | ↪ `price`           | integer  | The price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.                    |  | ↪ `priceTables`     | string   | The price table that was used to price the item.                                                                                                       |  | ↪ `index`           | integer  | The same index referring to Checkout's cart that was passed to the API.                                                                                |  | ↪ `skuId`           | string   | The same SKU ID that was passed to the API.                                                                                                            |  | ↪ `listPrice`       | integer  | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `costPrice`       | integer  | The cost price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `sellingPrice`    | integer  | The computed price before applying coupons, taxes or promotions.                                                                                       |  | ↪ `priceValidUntil` | string   | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339. |  | ↪ `tradePolicyId`   | string   | Trade Policy ID.                                                                                                                                       |    ## Index - Pricing Hub API    `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices)  `PUT` [Configure External Price Source](https://developers.vtex.com/docs/api-reference/pricing-hub#put-/config)  
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ItemsInner model module.
 * @module model/ItemsInner
 * @version 1.0
 */
class ItemsInner {
    /**
     * Constructs a new <code>ItemsInner</code>.
     * Each item to be priced by Pricing Hub
     * @alias module:model/ItemsInner
     * @param brandId {String} This is the brand ID for the item
     * @param categoriesIds {Array.<String>} ID of the categories that will be used to compute the price
     * @param index {Number} This is the index of the item at Checkout's cart. It has to be unique in the items array
     * @param priceTableIds {Array.<String>} IDs of the price tables that will be used to compute the price. More than one price table might be passed to the array. The final price rule might be more complex than the lowest or the highest price
     * @param quantity {Number} This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price
     * @param sellerId {String} This is the seller ID for the item
     * @param skuId {String} This is the sku id of the item that will be priced
     */
    constructor(brandId, categoriesIds, index, priceTableIds, quantity, sellerId, skuId) { 
        
        ItemsInner.initialize(this, brandId, categoriesIds, index, priceTableIds, quantity, sellerId, skuId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, brandId, categoriesIds, index, priceTableIds, quantity, sellerId, skuId) { 
        obj['brandId'] = brandId || '2000000';
        obj['categoriesIds'] = categoriesIds;
        obj['index'] = index || 0;
        obj['priceTableIds'] = priceTableIds;
        obj['quantity'] = quantity || 1;
        obj['sellerId'] = sellerId || '1';
        obj['skuId'] = skuId || '13';
    }

    /**
     * Constructs a <code>ItemsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ItemsInner} obj Optional instance to populate.
     * @return {module:model/ItemsInner} The populated <code>ItemsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ItemsInner();

            if (data.hasOwnProperty('brandId')) {
                obj['brandId'] = ApiClient.convertToType(data['brandId'], 'String');
            }
            if (data.hasOwnProperty('categoriesIds')) {
                obj['categoriesIds'] = ApiClient.convertToType(data['categoriesIds'], ['String']);
            }
            if (data.hasOwnProperty('index')) {
                obj['index'] = ApiClient.convertToType(data['index'], 'Number');
            }
            if (data.hasOwnProperty('priceTableIds')) {
                obj['priceTableIds'] = ApiClient.convertToType(data['priceTableIds'], ['String']);
            }
            if (data.hasOwnProperty('quantity')) {
                obj['quantity'] = ApiClient.convertToType(data['quantity'], 'Number');
            }
            if (data.hasOwnProperty('sellerId')) {
                obj['sellerId'] = ApiClient.convertToType(data['sellerId'], 'String');
            }
            if (data.hasOwnProperty('skuId')) {
                obj['skuId'] = ApiClient.convertToType(data['skuId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ItemsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ItemsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ItemsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['brandId'] && !(typeof data['brandId'] === 'string' || data['brandId'] instanceof String)) {
            throw new Error("Expected the field `brandId` to be a primitive type in the JSON string but got " + data['brandId']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['categoriesIds'])) {
            throw new Error("Expected the field `categoriesIds` to be an array in the JSON data but got " + data['categoriesIds']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['priceTableIds'])) {
            throw new Error("Expected the field `priceTableIds` to be an array in the JSON data but got " + data['priceTableIds']);
        }
        // ensure the json data is a string
        if (data['sellerId'] && !(typeof data['sellerId'] === 'string' || data['sellerId'] instanceof String)) {
            throw new Error("Expected the field `sellerId` to be a primitive type in the JSON string but got " + data['sellerId']);
        }
        // ensure the json data is a string
        if (data['skuId'] && !(typeof data['skuId'] === 'string' || data['skuId'] instanceof String)) {
            throw new Error("Expected the field `skuId` to be a primitive type in the JSON string but got " + data['skuId']);
        }

        return true;
    }


}

ItemsInner.RequiredProperties = ["brandId", "categoriesIds", "index", "priceTableIds", "quantity", "sellerId", "skuId"];

/**
 * This is the brand ID for the item
 * @member {String} brandId
 * @default '2000000'
 */
ItemsInner.prototype['brandId'] = '2000000';

/**
 * ID of the categories that will be used to compute the price
 * @member {Array.<String>} categoriesIds
 */
ItemsInner.prototype['categoriesIds'] = undefined;

/**
 * This is the index of the item at Checkout's cart. It has to be unique in the items array
 * @member {Number} index
 * @default 0
 */
ItemsInner.prototype['index'] = 0;

/**
 * IDs of the price tables that will be used to compute the price. More than one price table might be passed to the array. The final price rule might be more complex than the lowest or the highest price
 * @member {Array.<String>} priceTableIds
 */
ItemsInner.prototype['priceTableIds'] = undefined;

/**
 * This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price
 * @member {Number} quantity
 * @default 1
 */
ItemsInner.prototype['quantity'] = 1;

/**
 * This is the seller ID for the item
 * @member {String} sellerId
 * @default '1'
 */
ItemsInner.prototype['sellerId'] = '1';

/**
 * This is the sku id of the item that will be priced
 * @member {String} skuId
 * @default '13'
 */
ItemsInner.prototype['skuId'] = '13';






export default ItemsInner;

