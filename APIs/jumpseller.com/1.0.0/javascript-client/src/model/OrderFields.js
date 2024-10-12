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
import Customer from './Customer';
import OrderAdditionalFields from './OrderAdditionalFields';
import OrderBillingAddress from './OrderBillingAddress';
import OrderProduct from './OrderProduct';
import OrderShippingAddress from './OrderShippingAddress';
import OrderShippingTax from './OrderShippingTax';
import TrafficSource from './TrafficSource';

/**
 * The OrderFields model module.
 * @module model/OrderFields
 * @version 1.0.0
 */
class OrderFields {
    /**
     * Constructs a new <code>OrderFields</code>.
     * @alias module:model/OrderFields
     */
    constructor() { 
        
        OrderFields.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['shipping_required'] = true;
    }

    /**
     * Constructs a <code>OrderFields</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderFields} obj Optional instance to populate.
     * @return {module:model/OrderFields} The populated <code>OrderFields</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderFields();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], [OrderAdditionalFields]);
            }
            if (data.hasOwnProperty('additional_information')) {
                obj['additional_information'] = ApiClient.convertToType(data['additional_information'], 'String');
            }
            if (data.hasOwnProperty('billing_address')) {
                obj['billing_address'] = OrderBillingAddress.constructFromObject(data['billing_address']);
            }
            if (data.hasOwnProperty('checkout_url')) {
                obj['checkout_url'] = ApiClient.convertToType(data['checkout_url'], 'String');
            }
            if (data.hasOwnProperty('coupons')) {
                obj['coupons'] = ApiClient.convertToType(data['coupons'], 'String');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = ApiClient.convertToType(data['currency'], 'String');
            }
            if (data.hasOwnProperty('customer')) {
                obj['customer'] = Customer.constructFromObject(data['customer']);
            }
            if (data.hasOwnProperty('discount')) {
                obj['discount'] = ApiClient.convertToType(data['discount'], 'Number');
            }
            if (data.hasOwnProperty('duplicate_url')) {
                obj['duplicate_url'] = ApiClient.convertToType(data['duplicate_url'], 'String');
            }
            if (data.hasOwnProperty('external_shipping_rate_id')) {
                obj['external_shipping_rate_id'] = ApiClient.convertToType(data['external_shipping_rate_id'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('payment_information')) {
                obj['payment_information'] = ApiClient.convertToType(data['payment_information'], 'String');
            }
            if (data.hasOwnProperty('payment_method_name')) {
                obj['payment_method_name'] = ApiClient.convertToType(data['payment_method_name'], 'String');
            }
            if (data.hasOwnProperty('payment_method_type')) {
                obj['payment_method_type'] = ApiClient.convertToType(data['payment_method_type'], 'String');
            }
            if (data.hasOwnProperty('products')) {
                obj['products'] = ApiClient.convertToType(data['products'], [OrderProduct]);
            }
            if (data.hasOwnProperty('recovery_url')) {
                obj['recovery_url'] = ApiClient.convertToType(data['recovery_url'], 'String');
            }
            if (data.hasOwnProperty('shipment_status')) {
                obj['shipment_status'] = ApiClient.convertToType(data['shipment_status'], 'String');
            }
            if (data.hasOwnProperty('shipping')) {
                obj['shipping'] = ApiClient.convertToType(data['shipping'], 'Number');
            }
            if (data.hasOwnProperty('shipping_address')) {
                obj['shipping_address'] = OrderShippingAddress.constructFromObject(data['shipping_address']);
            }
            if (data.hasOwnProperty('shipping_discount')) {
                obj['shipping_discount'] = ApiClient.convertToType(data['shipping_discount'], 'Number');
            }
            if (data.hasOwnProperty('shipping_method_id')) {
                obj['shipping_method_id'] = ApiClient.convertToType(data['shipping_method_id'], 'Number');
            }
            if (data.hasOwnProperty('shipping_method_name')) {
                obj['shipping_method_name'] = ApiClient.convertToType(data['shipping_method_name'], 'String');
            }
            if (data.hasOwnProperty('shipping_option')) {
                obj['shipping_option'] = ApiClient.convertToType(data['shipping_option'], 'String');
            }
            if (data.hasOwnProperty('shipping_required')) {
                obj['shipping_required'] = ApiClient.convertToType(data['shipping_required'], 'Boolean');
            }
            if (data.hasOwnProperty('shipping_tax')) {
                obj['shipping_tax'] = ApiClient.convertToType(data['shipping_tax'], 'Number');
            }
            if (data.hasOwnProperty('shipping_taxes')) {
                obj['shipping_taxes'] = ApiClient.convertToType(data['shipping_taxes'], [OrderShippingTax]);
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = TrafficSource.constructFromObject(data['source']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('subtotal')) {
                obj['subtotal'] = ApiClient.convertToType(data['subtotal'], 'Number');
            }
            if (data.hasOwnProperty('tax')) {
                obj['tax'] = ApiClient.convertToType(data['tax'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('tracking_company')) {
                obj['tracking_company'] = ApiClient.convertToType(data['tracking_company'], 'String');
            }
            if (data.hasOwnProperty('tracking_number')) {
                obj['tracking_number'] = ApiClient.convertToType(data['tracking_number'], 'String');
            }
            if (data.hasOwnProperty('tracking_url')) {
                obj['tracking_url'] = ApiClient.convertToType(data['tracking_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderFields</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderFields</code>.
     */
    static validateJSON(data) {
        if (data['additional_fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['additional_fields'])) {
                throw new Error("Expected the field `additional_fields` to be an array in the JSON data but got " + data['additional_fields']);
            }
            // validate the optional field `additional_fields` (array)
            for (const item of data['additional_fields']) {
                OrderAdditionalFields.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['additional_information'] && !(typeof data['additional_information'] === 'string' || data['additional_information'] instanceof String)) {
            throw new Error("Expected the field `additional_information` to be a primitive type in the JSON string but got " + data['additional_information']);
        }
        // validate the optional field `billing_address`
        if (data['billing_address']) { // data not null
          OrderBillingAddress.validateJSON(data['billing_address']);
        }
        // ensure the json data is a string
        if (data['checkout_url'] && !(typeof data['checkout_url'] === 'string' || data['checkout_url'] instanceof String)) {
            throw new Error("Expected the field `checkout_url` to be a primitive type in the JSON string but got " + data['checkout_url']);
        }
        // ensure the json data is a string
        if (data['coupons'] && !(typeof data['coupons'] === 'string' || data['coupons'] instanceof String)) {
            throw new Error("Expected the field `coupons` to be a primitive type in the JSON string but got " + data['coupons']);
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['currency'] && !(typeof data['currency'] === 'string' || data['currency'] instanceof String)) {
            throw new Error("Expected the field `currency` to be a primitive type in the JSON string but got " + data['currency']);
        }
        // validate the optional field `customer`
        if (data['customer']) { // data not null
          Customer.validateJSON(data['customer']);
        }
        // ensure the json data is a string
        if (data['duplicate_url'] && !(typeof data['duplicate_url'] === 'string' || data['duplicate_url'] instanceof String)) {
            throw new Error("Expected the field `duplicate_url` to be a primitive type in the JSON string but got " + data['duplicate_url']);
        }
        // ensure the json data is a string
        if (data['external_shipping_rate_id'] && !(typeof data['external_shipping_rate_id'] === 'string' || data['external_shipping_rate_id'] instanceof String)) {
            throw new Error("Expected the field `external_shipping_rate_id` to be a primitive type in the JSON string but got " + data['external_shipping_rate_id']);
        }
        // ensure the json data is a string
        if (data['payment_information'] && !(typeof data['payment_information'] === 'string' || data['payment_information'] instanceof String)) {
            throw new Error("Expected the field `payment_information` to be a primitive type in the JSON string but got " + data['payment_information']);
        }
        // ensure the json data is a string
        if (data['payment_method_name'] && !(typeof data['payment_method_name'] === 'string' || data['payment_method_name'] instanceof String)) {
            throw new Error("Expected the field `payment_method_name` to be a primitive type in the JSON string but got " + data['payment_method_name']);
        }
        // ensure the json data is a string
        if (data['payment_method_type'] && !(typeof data['payment_method_type'] === 'string' || data['payment_method_type'] instanceof String)) {
            throw new Error("Expected the field `payment_method_type` to be a primitive type in the JSON string but got " + data['payment_method_type']);
        }
        if (data['products']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['products'])) {
                throw new Error("Expected the field `products` to be an array in the JSON data but got " + data['products']);
            }
            // validate the optional field `products` (array)
            for (const item of data['products']) {
                OrderProduct.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['recovery_url'] && !(typeof data['recovery_url'] === 'string' || data['recovery_url'] instanceof String)) {
            throw new Error("Expected the field `recovery_url` to be a primitive type in the JSON string but got " + data['recovery_url']);
        }
        // ensure the json data is a string
        if (data['shipment_status'] && !(typeof data['shipment_status'] === 'string' || data['shipment_status'] instanceof String)) {
            throw new Error("Expected the field `shipment_status` to be a primitive type in the JSON string but got " + data['shipment_status']);
        }
        // validate the optional field `shipping_address`
        if (data['shipping_address']) { // data not null
          OrderShippingAddress.validateJSON(data['shipping_address']);
        }
        // ensure the json data is a string
        if (data['shipping_method_name'] && !(typeof data['shipping_method_name'] === 'string' || data['shipping_method_name'] instanceof String)) {
            throw new Error("Expected the field `shipping_method_name` to be a primitive type in the JSON string but got " + data['shipping_method_name']);
        }
        // ensure the json data is a string
        if (data['shipping_option'] && !(typeof data['shipping_option'] === 'string' || data['shipping_option'] instanceof String)) {
            throw new Error("Expected the field `shipping_option` to be a primitive type in the JSON string but got " + data['shipping_option']);
        }
        if (data['shipping_taxes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['shipping_taxes'])) {
                throw new Error("Expected the field `shipping_taxes` to be an array in the JSON data but got " + data['shipping_taxes']);
            }
            // validate the optional field `shipping_taxes` (array)
            for (const item of data['shipping_taxes']) {
                OrderShippingTax.validateJSON(item);
            };
        }
        // validate the optional field `source`
        if (data['source']) { // data not null
          TrafficSource.validateJSON(data['source']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
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
        if (data['tracking_url'] && !(typeof data['tracking_url'] === 'string' || data['tracking_url'] instanceof String)) {
            throw new Error("Expected the field `tracking_url` to be a primitive type in the JSON string but got " + data['tracking_url']);
        }

        return true;
    }


}



/**
 * Array of additional fields for the given Order
 * @member {Array.<module:model/OrderAdditionalFields>} additional_fields
 */
OrderFields.prototype['additional_fields'] = undefined;

/**
 * Additional information for the given Order
 * @member {String} additional_information
 */
OrderFields.prototype['additional_information'] = undefined;

/**
 * @member {module:model/OrderBillingAddress} billing_address
 */
OrderFields.prototype['billing_address'] = undefined;

/**
 * Store Checkout Order URL for the given Order
 * @member {String} checkout_url
 */
OrderFields.prototype['checkout_url'] = undefined;

/**
 * Promotion Coupons used on the given Order
 * @member {String} coupons
 */
OrderFields.prototype['coupons'] = undefined;

/**
 * Order date
 * @member {String} created_at
 */
OrderFields.prototype['created_at'] = undefined;

/**
 * Currency of the Order
 * @member {String} currency
 */
OrderFields.prototype['currency'] = undefined;

/**
 * @member {module:model/Customer} customer
 */
OrderFields.prototype['customer'] = undefined;

/**
 * Discount value for the given Order
 * @member {Number} discount
 */
OrderFields.prototype['discount'] = undefined;

/**
 * Duplicate Order URL for the given Order
 * @member {String} duplicate_url
 */
OrderFields.prototype['duplicate_url'] = undefined;

/**
 * Rate id for selected External Shipping Method rate
 * @member {String} external_shipping_rate_id
 */
OrderFields.prototype['external_shipping_rate_id'] = undefined;

/**
 * Unique identifier of the Order
 * @member {Number} id
 */
OrderFields.prototype['id'] = undefined;

/**
 * Payment information for the given Order
 * @member {String} payment_information
 */
OrderFields.prototype['payment_information'] = undefined;

/**
 * Payment Method name used e.g. PayPal
 * @member {String} payment_method_name
 */
OrderFields.prototype['payment_method_name'] = undefined;

/**
 * Payment Method type used e.g. paypal
 * @member {String} payment_method_type
 */
OrderFields.prototype['payment_method_type'] = undefined;

/**
 * @member {Array.<module:model/OrderProduct>} products
 */
OrderFields.prototype['products'] = undefined;

/**
 * Recovery Order URL for the given Order
 * @member {String} recovery_url
 */
OrderFields.prototype['recovery_url'] = undefined;

/**
 * Shipment Status for Order Fulfillment.
 * @member {module:model/OrderFields.ShipmentStatusEnum} shipment_status
 */
OrderFields.prototype['shipment_status'] = undefined;

/**
 * Shipping value for the given Order
 * @member {Number} shipping
 */
OrderFields.prototype['shipping'] = undefined;

/**
 * @member {module:model/OrderShippingAddress} shipping_address
 */
OrderFields.prototype['shipping_address'] = undefined;

/**
 * Shipping Discount value for the given order
 * @member {Number} shipping_discount
 */
OrderFields.prototype['shipping_discount'] = undefined;

/**
 * Shipping method e.g. Royal Mail
 * @member {Number} shipping_method_id
 */
OrderFields.prototype['shipping_method_id'] = undefined;

/**
 * Shipping method e.g. Royal Mail
 * @member {String} shipping_method_name
 */
OrderFields.prototype['shipping_method_name'] = undefined;

/**
 * Shipping option for this order.
 * @member {module:model/OrderFields.ShippingOptionEnum} shipping_option
 */
OrderFields.prototype['shipping_option'] = undefined;

/**
 * False if the order is digital.
 * @member {Boolean} shipping_required
 * @default true
 */
OrderFields.prototype['shipping_required'] = true;

/**
 * Shipping Tax value for the given order
 * @member {Number} shipping_tax
 */
OrderFields.prototype['shipping_tax'] = undefined;

/**
 * @member {Array.<module:model/OrderShippingTax>} shipping_taxes
 */
OrderFields.prototype['shipping_taxes'] = undefined;

/**
 * @member {module:model/TrafficSource} source
 */
OrderFields.prototype['source'] = undefined;

/**
 * Status of the Order
 * @member {module:model/OrderFields.StatusEnum} status
 */
OrderFields.prototype['status'] = undefined;

/**
 * Subtotal value for the given Order. Excluding taxes, shipping and discounts
 * @member {Number} subtotal
 */
OrderFields.prototype['subtotal'] = undefined;

/**
 * Tax value for the given order
 * @member {Number} tax
 */
OrderFields.prototype['tax'] = undefined;

/**
 * Total value for the given Order. Including taxes, shipping and discounts
 * @member {Number} total
 */
OrderFields.prototype['total'] = undefined;

/**
 * Company Used for Order Fulfillment.
 * @member {String} tracking_company
 */
OrderFields.prototype['tracking_company'] = undefined;

/**
 * Tracking Number for Order Fulfillment.
 * @member {String} tracking_number
 */
OrderFields.prototype['tracking_number'] = undefined;

/**
 * Tracking URL for Order Fulfillment.
 * @member {String} tracking_url
 */
OrderFields.prototype['tracking_url'] = undefined;





/**
 * Allowed values for the <code>shipment_status</code> property.
 * @enum {String}
 * @readonly
 */
OrderFields['ShipmentStatusEnum'] = {

    /**
     * value: "delivered"
     * @const
     */
    "delivered": "delivered",

    /**
     * value: "requested"
     * @const
     */
    "requested": "requested",

    /**
     * value: "in_transit"
     * @const
     */
    "in_transit": "in_transit",

    /**
     * value: "failed"
     * @const
     */
    "failed": "failed",

    /**
     * value: "pickup_available"
     * @const
     */
    "pickup_available": "pickup_available"
};


/**
 * Allowed values for the <code>shipping_option</code> property.
 * @enum {String}
 * @readonly
 */
OrderFields['ShippingOptionEnum'] = {

    /**
     * value: "delivery"
     * @const
     */
    "delivery": "delivery",

    /**
     * value: "store_pickup"
     * @const
     */
    "store_pickup": "store_pickup",

    /**
     * value: "no_shipping"
     * @const
     */
    "no_shipping": "no_shipping"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
OrderFields['StatusEnum'] = {

    /**
     * value: "Abandoned"
     * @const
     */
    "Abandoned": "Abandoned",

    /**
     * value: "Canceled"
     * @const
     */
    "Canceled": "Canceled",

    /**
     * value: "Pending Payment"
     * @const
     */
    "Pending Payment": "Pending Payment",

    /**
     * value: "Paid"
     * @const
     */
    "Paid": "Paid"
};



export default OrderFields;

