/*
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
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


import java.math.BigDecimal;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FulfillmentApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public FulfillmentApi() {
        this(Configuration.getDefaultApiClient());
    }

    public FulfillmentApi(ApiClient apiClient) {
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
     * Build call for getAddressByPostalCode
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. (required)
     * @param postalCode Postal code. (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAddressByPostalCodeCall(String contentType, String accept, String countryCode, String postalCode, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/postal-code/{countryCode}/{postalCode}"
            .replace("{" + "countryCode" + "}", localVarApiClient.escapeString(countryCode.toString()))
            .replace("{" + "postalCode" + "}", localVarApiClient.escapeString(postalCode.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call getAddressByPostalCodeValidateBeforeCall(String contentType, String accept, String countryCode, String postalCode, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling getAddressByPostalCode(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling getAddressByPostalCode(Async)");
        }

        // verify the required parameter 'countryCode' is set
        if (countryCode == null) {
            throw new ApiException("Missing the required parameter 'countryCode' when calling getAddressByPostalCode(Async)");
        }

        // verify the required parameter 'postalCode' is set
        if (postalCode == null) {
            throw new ApiException("Missing the required parameter 'postalCode' when calling getAddressByPostalCode(Async)");
        }

        return getAddressByPostalCodeCall(contentType, accept, countryCode, postalCode, _callback);

    }

    /**
     * Get address by postal code
     * Retrieves address information for a given postal code and country.    This request can be used to implement auto complete functionality when a customer needs to fill in an address.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. (required)
     * @param postalCode Postal code. (required)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void getAddressByPostalCode(String contentType, String accept, String countryCode, String postalCode) throws ApiException {
        getAddressByPostalCodeWithHttpInfo(contentType, accept, countryCode, postalCode);
    }

    /**
     * Get address by postal code
     * Retrieves address information for a given postal code and country.    This request can be used to implement auto complete functionality when a customer needs to fill in an address.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. (required)
     * @param postalCode Postal code. (required)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> getAddressByPostalCodeWithHttpInfo(String contentType, String accept, String countryCode, String postalCode) throws ApiException {
        okhttp3.Call localVarCall = getAddressByPostalCodeValidateBeforeCall(contentType, accept, countryCode, postalCode, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * Get address by postal code (asynchronously)
     * Retrieves address information for a given postal code and country.    This request can be used to implement auto complete functionality when a customer needs to fill in an address.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. (required)
     * @param postalCode Postal code. (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call getAddressByPostalCodeAsync(String contentType, String accept, String countryCode, String postalCode, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = getAddressByPostalCodeValidateBeforeCall(contentType, accept, countryCode, postalCode, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for listPickupPpointsByLocation
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param geoCoordinates Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes. (optional)
     * @param postalCode Postal code around which to search for pickup points. If you use this type of search, make sure to pass a &#x60;countryCode&#x60; and do not pass &#x60;geoCoordinates&#x60;. (optional, default to 1234000)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. Pass the country code only if you are searching pickup points by postal code. (optional, default to BRA)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPickupPpointsByLocationCall(String contentType, String accept, List<BigDecimal> geoCoordinates, String postalCode, String countryCode, final ApiCallback _callback) throws ApiException {
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

        Object localVarPostBody = null;

        // create path and map variables
        String localVarPath = "/api/checkout/pub/pickup-points";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (geoCoordinates != null) {
            localVarCollectionQueryParams.addAll(localVarApiClient.parameterToPairs("multi", "geoCoordinates", geoCoordinates));
        }

        if (postalCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("postalCode", postalCode));
        }

        if (countryCode != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("countryCode", countryCode));
        }

        if (contentType != null) {
            localVarHeaderParams.put("Content-Type", localVarApiClient.parameterToString(contentType));
        }

        if (accept != null) {
            localVarHeaderParams.put("Accept", localVarApiClient.parameterToString(accept));
        }

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] {  };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call listPickupPpointsByLocationValidateBeforeCall(String contentType, String accept, List<BigDecimal> geoCoordinates, String postalCode, String countryCode, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'contentType' is set
        if (contentType == null) {
            throw new ApiException("Missing the required parameter 'contentType' when calling listPickupPpointsByLocation(Async)");
        }

        // verify the required parameter 'accept' is set
        if (accept == null) {
            throw new ApiException("Missing the required parameter 'accept' when calling listPickupPpointsByLocation(Async)");
        }

        return listPickupPpointsByLocationCall(contentType, accept, geoCoordinates, postalCode, countryCode, _callback);

    }

    /**
     * List pickup points by location
     * Retrieves information on pickup points close to a given location determined by geocoordinates or postal code.    The pickup points returned are not necessarily all active ones. Make sure to validate the information consumed by integrations.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param geoCoordinates Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes. (optional)
     * @param postalCode Postal code around which to search for pickup points. If you use this type of search, make sure to pass a &#x60;countryCode&#x60; and do not pass &#x60;geoCoordinates&#x60;. (optional, default to 1234000)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. Pass the country code only if you are searching pickup points by postal code. (optional, default to BRA)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public void listPickupPpointsByLocation(String contentType, String accept, List<BigDecimal> geoCoordinates, String postalCode, String countryCode) throws ApiException {
        listPickupPpointsByLocationWithHttpInfo(contentType, accept, geoCoordinates, postalCode, countryCode);
    }

    /**
     * List pickup points by location
     * Retrieves information on pickup points close to a given location determined by geocoordinates or postal code.    The pickup points returned are not necessarily all active ones. Make sure to validate the information consumed by integrations.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param geoCoordinates Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes. (optional)
     * @param postalCode Postal code around which to search for pickup points. If you use this type of search, make sure to pass a &#x60;countryCode&#x60; and do not pass &#x60;geoCoordinates&#x60;. (optional, default to 1234000)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. Pass the country code only if you are searching pickup points by postal code. (optional, default to BRA)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> listPickupPpointsByLocationWithHttpInfo(String contentType, String accept, List<BigDecimal> geoCoordinates, String postalCode, String countryCode) throws ApiException {
        okhttp3.Call localVarCall = listPickupPpointsByLocationValidateBeforeCall(contentType, accept, geoCoordinates, postalCode, countryCode, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     * List pickup points by location (asynchronously)
     * Retrieves information on pickup points close to a given location determined by geocoordinates or postal code.    The pickup points returned are not necessarily all active ones. Make sure to validate the information consumed by integrations.
     * @param contentType Type of the content being sent. (required)
     * @param accept HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. (required)
     * @param geoCoordinates Geocoordinates (first longitude, then latitude) around which to search for pickup points. If you use this type of search, do not pass postal and country codes. (optional)
     * @param postalCode Postal code around which to search for pickup points. If you use this type of search, make sure to pass a &#x60;countryCode&#x60; and do not pass &#x60;geoCoordinates&#x60;. (optional, default to 1234000)
     * @param countryCode Three letter country code refering to the &#x60;postalCode&#x60; field. Pass the country code only if you are searching pickup points by postal code. (optional, default to BRA)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call listPickupPpointsByLocationAsync(String contentType, String accept, List<BigDecimal> geoCoordinates, String postalCode, String countryCode, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = listPickupPpointsByLocationValidateBeforeCall(contentType, accept, geoCoordinates, postalCode, countryCode, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
}
