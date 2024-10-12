/*
 * Pricing Hub
 * > This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests).      In the B2B scenario, it is common for stores to have personalized prices per customer and complex pricing systems that require external integrations. Pricing Hub is a system developed for the B2B context that works as an intermediary between VTEX and external pricing systems.     In VTEX, B2B stores have the option to use our internal pricing system or an external one. If the store chooses to operate with an external pricing system, Pricing Hub will query an external price calculation API. The external API should then respond with the price for all items in the shopping cart according to its predefined tax rules.    ![Pricing hub protocal diagram](https://user-images.githubusercontent.com/77292838/211634260-e4f7a516-91df-416e-ab43-d9c79d56bc91.png)    ## Implementation    To connect with external pricing systems using Pricing Hub, it is necessary to build a VTEX IO middleware app. We offer two reference implementation templates to simplify this process:    - [C# template](https://github.com/vtex-apps/external-prices-app)  - [Node template](https://github.com/vtex-apps/external-prices-node)    Read the documentation on each repository to learn more about the required steps to use and customize the app.    > The app used by Pricing Hub to connect must be a `major 0`.     ## Specifications    See below all the specifications of the request and the response expected when communicating with Pricing Hub.    ### Price calculation request    The external prices calculation tool must provide an endpoint that will receive a `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices) request. This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.    >⚠️ Responses from Pricing Hub tend to have a greater delay when compared to other VTEX systems. That is expected, however, due to the complexity of its nested requests. The timeout for this request is 900 milliseconds.    In this request, Pricing Hub provides a body in a specific format, exemplified below. This means that either the endpoint must be prepared to receive this body format, or the app must contain a parser to adapt it to the correct format.    #### Request body example    ```json  {      \"item\":           {              \"index\": 0,              \"skuId\": \"880011\",              \"quantity\": 1          },      \"context\":{          \"email\": \"john@email.com\"      }  }  ```    The request body should have the following properties:    | **Attribute** | **Type** | **Description**                                                                                                                                                                                          |  |---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`        | object   | The item whose price is supposed to be fetched by Pricing Hub.                                                                                                                                           |  | ↪ `index`     | integer  | This is the index of the item at Checkout's cart. It has to be unique in the items array.                                                                                                                |  | ↪ `skuId`     | string   | This is the SKU ID of the item that will be priced.                                                                                                                                                      |  | ↪ `quantity`  | integer  | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price. |  | `context`     | object   | The object that contains the context to inform the query.                                                                                                                                                |  | ↪ `email`     | string   | The customer's email address. If there is no value, use an empty string.                                                                                                                                 |    ### External prices provider response    In response to the request sent by Pricing Hub, we expect an outcome in the following format:    ```json  {      \"item\": {          \"price\": 54035,          \"priceTables\": \"special\",          \"index\": 0,          \"skuId\": \"880011\",          \"listPrice\": 54035,          \"costPrice\": 50000,          \"sellingPrice\": 54035,          \"priceValidUntil\": \"2023-01-27T20:29:57Z\",          \"tradePolicyId\": \"special\"      }  }  ```    The response should have the following properties:    | **Attribute**       | **Type** | **Description**                                                                                                                                        |  |---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`              | object   | The object that contains the price data.                                                                                                               |  | ↪ `price`           | integer  | The price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.                    |  | ↪ `priceTables`     | string   | The price table that was used to price the item.                                                                                                       |  | ↪ `index`           | integer  | The same index referring to Checkout's cart that was passed to the API.                                                                                |  | ↪ `skuId`           | string   | The same SKU ID that was passed to the API.                                                                                                            |  | ↪ `listPrice`       | integer  | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `costPrice`       | integer  | The cost price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `sellingPrice`    | integer  | The computed price before applying coupons, taxes or promotions.                                                                                       |  | ↪ `priceValidUntil` | string   | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339. |  | ↪ `tradePolicyId`   | string   | Trade Policy ID.                                                                                                                                       |    ## Index - Pricing Hub API    `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices)  `PUT` [Configure External Price Source](https://developers.vtex.com/docs/api-reference/pricing-hub#put-/config)  
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.ConfigExternalPriceSourceRequest;
import org.openapitools.client.model.GetPricesRequestObject;
import org.openapitools.client.model.Response2;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PricingHubPricesApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public PricingHubPricesApi() {
        this(Configuration.getDefaultApiClient());
    }

    public PricingHubPricesApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for apiPricingHubPricesPost
     * @param accountName Name of the VTEX account. Used as part of the URL (required)
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param getPricesRequestObject  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiPricingHubPricesPostCall(String accountName, String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, GetPricesRequestObject getPricesRequestObject, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = getPricesRequestObject;

        // create path and map variables
        String localVarPath = "/api/pricing-hub/prices";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (accountName != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("accountName", accountName));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (xVTEXAPIAppKey != null) {
            localVarHeaderParams.put("X-VTEX-API-AppKey", localVarApiClient.parameterToString(xVTEXAPIAppKey));
        }

        if (xVTEXAPIAppToken != null) {
            localVarHeaderParams.put("X-VTEX-API-AppToken", localVarApiClient.parameterToString(xVTEXAPIAppToken));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call apiPricingHubPricesPostValidateBeforeCall(String accountName, String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, GetPricesRequestObject getPricesRequestObject, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accountName' is set
        if (accountName == null) {
            throw new ApiException("Missing the required parameter 'accountName' when calling apiPricingHubPricesPost(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling apiPricingHubPricesPost(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling apiPricingHubPricesPost(Async)");
        }

        // verify the required parameter 'xVTEXAPIAppKey' is set
        if (xVTEXAPIAppKey == null) {
            throw new ApiException("Missing the required parameter 'xVTEXAPIAppKey' when calling apiPricingHubPricesPost(Async)");
        }

        // verify the required parameter 'xVTEXAPIAppToken' is set
        if (xVTEXAPIAppToken == null) {
            throw new ApiException("Missing the required parameter 'xVTEXAPIAppToken' when calling apiPricingHubPricesPost(Async)");
        }

        // verify the required parameter 'getPricesRequestObject' is set
        if (getPricesRequestObject == null) {
            throw new ApiException("Missing the required parameter 'getPricesRequestObject' when calling apiPricingHubPricesPost(Async)");
        }

        return apiPricingHubPricesPostCall(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject, _callback);

    }

    /**
     * Get Prices
     * This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.     &gt;ℹ️ &gt; This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 
     * @param accountName Name of the VTEX account. Used as part of the URL (required)
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param getPricesRequestObject  (required)
     * @return Response2
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public Response2 apiPricingHubPricesPost(String accountName, String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, GetPricesRequestObject getPricesRequestObject) throws ApiException {
        ApiResponse<Response2> localVarResp = apiPricingHubPricesPostWithHttpInfo(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject);
        return localVarResp.getData();
    }

    /**
     * Get Prices
     * This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.     &gt;ℹ️ &gt; This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 
     * @param accountName Name of the VTEX account. Used as part of the URL (required)
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param getPricesRequestObject  (required)
     * @return ApiResponse&lt;Response2&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Response2> apiPricingHubPricesPostWithHttpInfo(String accountName, String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, GetPricesRequestObject getPricesRequestObject) throws ApiException {
        okhttp3.Call localVarCall = apiPricingHubPricesPostValidateBeforeCall(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject, null);
        Type localVarReturnType = new TypeToken<Response2>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Get Prices (asynchronously)
     * This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.     &gt;ℹ️ &gt; This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 
     * @param accountName Name of the VTEX account. Used as part of the URL (required)
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param getPricesRequestObject  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call apiPricingHubPricesPostAsync(String accountName, String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, GetPricesRequestObject getPricesRequestObject, final ApiCallback<Response2> _callback) throws ApiException {

        okhttp3.Call localVarCall = apiPricingHubPricesPostValidateBeforeCall(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject, _callback);
        Type localVarReturnType = new TypeToken<Response2>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for configExternalPriceSource
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param configExternalPriceSourceRequest  (required)
     * @param an Name of the VTEX account (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configExternalPriceSourceCall(String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, ConfigExternalPriceSourceRequest configExternalPriceSourceRequest, String an, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = configExternalPriceSourceRequest;

        // create path and map variables
        String localVarPath = "/config";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (an != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("an", an));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (xVTEXAPIAppKey != null) {
            localVarHeaderParams.put("X-VTEX-API-AppKey", localVarApiClient.parameterToString(xVTEXAPIAppKey));
        }

        if (xVTEXAPIAppToken != null) {
            localVarHeaderParams.put("X-VTEX-API-AppToken", localVarApiClient.parameterToString(xVTEXAPIAppToken));
        }

        final String[] localVarAccepts = {
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "appToken", "appKey" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call configExternalPriceSourceValidateBeforeCall(String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, ConfigExternalPriceSourceRequest configExternalPriceSourceRequest, String an, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling configExternalPriceSource(Async)");
        }

        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling configExternalPriceSource(Async)");
        }

        // verify the required parameter 'xVTEXAPIAppKey' is set
        if (xVTEXAPIAppKey == null) {
            throw new ApiException("Missing the required parameter 'xVTEXAPIAppKey' when calling configExternalPriceSource(Async)");
        }

        // verify the required parameter 'xVTEXAPIAppToken' is set
        if (xVTEXAPIAppToken == null) {
            throw new ApiException("Missing the required parameter 'xVTEXAPIAppToken' when calling configExternalPriceSource(Async)");
        }

        // verify the required parameter 'configExternalPriceSourceRequest' is set
        if (configExternalPriceSourceRequest == null) {
            throw new ApiException("Missing the required parameter 'configExternalPriceSourceRequest' when calling configExternalPriceSource(Async)");
        }

        return configExternalPriceSourceCall(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, an, _callback);

    }

    /**
     * Configure External Price Source
     * This route facilitates setting up an external price source in Pricing Hub. It also allows you to activate or deactivate that source in a given account.     &gt;ℹ️ This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param configExternalPriceSourceRequest  (required)
     * @param an Name of the VTEX account (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void configExternalPriceSource(String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, ConfigExternalPriceSourceRequest configExternalPriceSourceRequest, String an) throws ApiException {
        configExternalPriceSourceWithHttpInfo(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, an);
    }

    /**
     * Configure External Price Source
     * This route facilitates setting up an external price source in Pricing Hub. It also allows you to activate or deactivate that source in a given account.     &gt;ℹ️ This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param configExternalPriceSourceRequest  (required)
     * @param an Name of the VTEX account (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> configExternalPriceSourceWithHttpInfo(String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, ConfigExternalPriceSourceRequest configExternalPriceSourceRequest, String an) throws ApiException {
        okhttp3.Call localVarCall = configExternalPriceSourceValidateBeforeCall(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, an, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Configure External Price Source (asynchronously)
     * This route facilitates setting up an external price source in Pricing Hub. It also allows you to activate or deactivate that source in a given account.     &gt;ℹ️ This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 
     * @param accept HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand (required)
     * @param contentType Describes the type of the content being sent (required)
     * @param xVTEXAPIAppKey The AppKey configured by the merchant (required)
     * @param xVTEXAPIAppToken The AppToken configured by the merchant (required)
     * @param configExternalPriceSourceRequest  (required)
     * @param an Name of the VTEX account (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call configExternalPriceSourceAsync(String accept, String contentType, String xVTEXAPIAppKey, String xVTEXAPIAppToken, ConfigExternalPriceSourceRequest configExternalPriceSourceRequest, String an, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = configExternalPriceSourceValidateBeforeCall(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, an, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
