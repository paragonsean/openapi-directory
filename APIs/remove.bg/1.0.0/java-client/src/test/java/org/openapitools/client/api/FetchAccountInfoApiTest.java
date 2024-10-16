/*
 * Background Removal API
 * Remove the background of any image
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
import org.openapitools.client.model.AccountGet200Response;
import org.openapitools.client.model.AuthFailed;
import org.openapitools.client.model.RateLimit;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FetchAccountInfoApi
 */
@Disabled
public class FetchAccountInfoApiTest {

    private final FetchAccountInfoApi api = new FetchAccountInfoApi();

    /**
     * Fetch credit balance and free API calls.
     *
     * Get the current credit balance and number of free API calls.  Notes:  * Balance changes may be delayed by several seconds. To locally keep track of your credit balance, you should therefore only call this endpoint initially (or e.g. when the user manually triggers a refresh), then use the &#x60;X-Credits-Charged&#x60; response header returned with each image processing response to adjust the local balance.  * The \&quot;*sizes*\&quot; field is always \&quot;all\&quot;, is deprecated and will soon be removed. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void accountGetTest() throws ApiException {
        AccountGet200Response response = api.accountGet();
        // TODO: test validations
    }

}
