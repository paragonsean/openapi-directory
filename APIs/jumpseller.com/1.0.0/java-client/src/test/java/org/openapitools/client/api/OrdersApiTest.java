/*
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Count;
import org.openapitools.client.model.NotFound;
import org.openapitools.client.model.Order;
import org.openapitools.client.model.OrderCreate;
import org.openapitools.client.model.OrderEdit;
import org.openapitools.client.model.OrderHistory;
import org.openapitools.client.model.OrderHistoryEdit;
import org.openapitools.client.model.StatusInvalid;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for OrdersApi
 */
@Disabled
public class OrdersApiTest {

    private final OrdersApi api = new OrdersApi();

    /**
     * Retrieve orders filtered by Order Id.
     *
     * For example the GET /orders/after/5000 will return Order 5001, 5002, 5003, etc.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersAfterIdJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        Order response = api.ordersAfterIdJsonGet(login, authtoken, id);
        // TODO: test validations
    }

    /**
     * Count all Orders.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersCountJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Count response = api.ordersCountJsonGet(login, authtoken);
        // TODO: test validations
    }

    /**
     * Retrieve all Order History.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersIdHistoryJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        List<OrderHistory> response = api.ordersIdHistoryJsonGet(login, authtoken, id);
        // TODO: test validations
    }

    /**
     * Create a new Order History Entry.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersIdHistoryJsonPostTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        OrderHistoryEdit orderHistoryEdit = null;
        OrderHistory response = api.ordersIdHistoryJsonPost(login, authtoken, id, orderHistoryEdit);
        // TODO: test validations
    }

    /**
     * Retrieve a single Order.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersIdJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        Order response = api.ordersIdJsonGet(login, authtoken, id);
        // TODO: test validations
    }

    /**
     * Modify an existing Order.
     *
     * Only &#x60;status&#x60;, &#x60;shipment_status&#x60;, &#x60;tracking_number&#x60;, &#x60;tracking_company&#x60;, &#x60;tracking_url&#x60;, &#x60;additional_information&#x60; and &#x60;additional_fields&#x60; are available for update. An email is send if &#x60;shipment_status&#x60; changes.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersIdJsonPutTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        OrderEdit orderEdit = null;
        Order response = api.ordersIdJsonPut(login, authtoken, id, orderEdit);
        // TODO: test validations
    }

    /**
     * Retrieve all Orders.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer limit = null;
        Integer page = null;
        List<Order> response = api.ordersJsonGet(login, authtoken, limit, page);
        // TODO: test validations
    }

    /**
     * Create a new Order.
     *
     * Orders created externally keep the given order product&#39;s values (bypassing internal promotion or product amounts).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersJsonPostTest() throws ApiException {
        String login = null;
        String authtoken = null;
        OrderCreate orderCreate = null;
        Order response = api.ordersJsonPost(login, authtoken, orderCreate);
        // TODO: test validations
    }

    /**
     * Retrieve orders filtered by status.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void ordersStatusStatusJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        String status = null;
        List<Order> response = api.ordersStatusStatusJsonGet(login, authtoken, status);
        // TODO: test validations
    }

}
