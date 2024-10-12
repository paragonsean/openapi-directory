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
import org.openapitools.client.model.Product;
import org.openapitools.client.model.ProductEdit;
import org.openapitools.client.model.StatusInvalid;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProductsApi
 */
@Disabled
public class ProductsApiTest {

    private final ProductsApi api = new ProductsApi();

    /**
     * Retrieves Products after the given id.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsAfterIdJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        String locale = null;
        List<Product> response = api.productsAfterIdJsonGet(login, authtoken, id, locale);
        // TODO: test validations
    }

    /**
     * Count Products filtered by category.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsCategoryCategoryIdCountJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer categoryId = null;
        String locale = null;
        Count response = api.productsCategoryCategoryIdCountJsonGet(login, authtoken, categoryId, locale);
        // TODO: test validations
    }

    /**
     * Retrieve Products filtered by category.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsCategoryCategoryIdJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer categoryId = null;
        String locale = null;
        List<Product> response = api.productsCategoryCategoryIdJsonGet(login, authtoken, categoryId, locale);
        // TODO: test validations
    }

    /**
     * Count all Products.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsCountJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Count response = api.productsCountJsonGet(login, authtoken);
        // TODO: test validations
    }

    /**
     * Delete an existing Product.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsIdJsonDeleteTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        String response = api.productsIdJsonDelete(login, authtoken, id);
        // TODO: test validations
    }

    /**
     * Retrieve a single Product.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsIdJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        String locale = null;
        Product response = api.productsIdJsonGet(login, authtoken, id, locale);
        // TODO: test validations
    }

    /**
     * Modify an existing Product.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsIdJsonPutTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer id = null;
        ProductEdit productEdit = null;
        String locale = null;
        Product response = api.productsIdJsonPut(login, authtoken, id, productEdit, locale);
        // TODO: test validations
    }

    /**
     * Retrieve all Products.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        Integer limit = null;
        Integer page = null;
        String locale = null;
        List<Product> response = api.productsJsonGet(login, authtoken, limit, page, locale);
        // TODO: test validations
    }

    /**
     * Create a new Product.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsJsonPostTest() throws ApiException {
        String login = null;
        String authtoken = null;
        ProductEdit productEdit = null;
        String locale = null;
        Product response = api.productsJsonPost(login, authtoken, productEdit, locale);
        // TODO: test validations
    }

    /**
     * Retrieve a Product List from a query.
     *
     * Endpoint example:   &#x60;&#x60;&#x60;text https://api.jumpseller.com/v1/products/search.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX&amp;query&#x3D;test&amp;fields&#x3D;name,description  &#x60;&#x60;&#x60;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsSearchJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        String query = null;
        String locale = null;
        String fields = null;
        List<Product> response = api.productsSearchJsonGet(login, authtoken, query, locale, fields);
        // TODO: test validations
    }

    /**
     * Count Products filtered by status.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsStatusStatusCountJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        String status = null;
        String locale = null;
        Count response = api.productsStatusStatusCountJsonGet(login, authtoken, status, locale);
        // TODO: test validations
    }

    /**
     * Retrieve Products filtered by status.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void productsStatusStatusJsonGetTest() throws ApiException {
        String login = null;
        String authtoken = null;
        String status = null;
        String locale = null;
        List<Product> response = api.productsStatusStatusJsonGet(login, authtoken, status, locale);
        // TODO: test validations
    }

}
