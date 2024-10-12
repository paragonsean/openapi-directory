/*
 * 
 * This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the `authorization_code` that came with    the redirect for an `access_token` and `refresh_token`.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED  - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`, while one that allows patients to schedule appointments online would need at least `\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application's name and the list of permissions you requested (via the `scope` parameter).  When they click the \"Authorize\" button, they will be redirected to your redirect URI with a `code` query parameter appended, which contains an authorization code to be used in step 3.  If they click the \"Cancel\" button, they will be redirected to your redirect URI with `error=access_denied` instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The `code` obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if 'error' in get_params:         raise ValueError('Error authorizing application: %s' % get_params[error])      response = requests.post('https://drchrono.com/o/token/', data={         'code': get_params['code'],         'grant_type': 'authorization_code',         'redirect_uri': 'http://mytestapp.com/redirect_uri',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     response.raise_for_status()     data = response.json()      # Save these in your database associated with the user     access_token = data['access_token']     refresh_token = data['refresh_token']     expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])  You now have all you need to make API requests authenticated as that provider. When using this access token, you'll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the `code` parameter with `refresh_token`, change the value `grant_type` from `authorization_code` to `refresh_token`, and omit the `redirect_uri` parameter.  Example in Python:      ...     response = requests.post('https://drchrono.com/o/token/', data={         'refresh_token': get_refresh_token(),         'grant_type': 'refresh_token',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to <a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- `APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created `APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified `PATIENT_CREATE` | We will deliver a hook any time a patient is created `PATIENT_MODIFY` | We will deliver a hook any time a patient is modified `PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created `PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified `PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created `PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified `PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created `PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified `CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked `CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked `TASK_CREATE` | We will deliver a hook any time a task is created `TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item `TASK_DELETE` | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.  Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with <a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>. And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()         return json_response({             'secret_token': secret_token         })  <div class=\"alert alert-warning\"> <b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed. </div>   ## Webhooks header and body  **Header**  Key | Value --- | ----- `X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING` `X-drchrono-signature` | Secret token associated with this webhook `X-drchrono-delivery` | ID of this delivery  **Body**  Key | Value --- | ----- `receiver` | This will be an JSON representation of the webhook `object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as `POST` requests.  **PING**:  You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any `2xx` responses as successfully delivered. Any other responses, like `302` would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in request header. Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of <code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono's patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a `POST` request to the `/api/iframe_integration` endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a `DELETE` request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  <img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>  <img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the `src` parameter of the IFrame will be:  ``` <iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt> ```  The `jwt` parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your `client_secret` as the key.  This verifies that the iframe is being loaded within one of drchrono's pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET = <client_secret>     MAX_TIME_DRIFT_SECONDS = 60      def validate_parameters(request):         token = request.GET['jwt']          return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)  Modern browsers' same-origin policy means that data cannot be passed between your application and drchrono's page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won't be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here's changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  
 *
 * The version of the OpenAPI document: v4 (Hunt Valley)
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


import org.openapitools.client.model.BillingLineItem;
import org.openapitools.client.model.BillingProfile;
import org.openapitools.client.model.BillingProfilesList200Response;
import org.openapitools.client.model.CashPayment;
import org.openapitools.client.model.CashPaymentLog;
import org.openapitools.client.model.CommLogsList200Response;
import org.openapitools.client.model.Coverage;
import org.openapitools.client.model.CustomInsurancePlanName;
import org.openapitools.client.model.CustomInsurancePlanNamesList200Response;
import org.openapitools.client.model.EligibilityChecksList200Response;
import org.openapitools.client.model.LineItemTransaction;
import org.openapitools.client.model.LineItemsList200Response;
import org.openapitools.client.model.PatientPaymentLogList200Response;
import org.openapitools.client.model.PatientPaymentsList200Response;
import org.openapitools.client.model.PhoneCallLog;
import org.openapitools.client.model.TransactionsList200Response;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BillingApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public BillingApi() {
        this(Configuration.getDefaultApiClient());
    }

    public BillingApi(ApiClient apiClient) {
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
     * Build call for billingProfilesList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call billingProfilesListCall(String cursor, Integer pageSize, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/billing_profiles";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call billingProfilesListValidateBeforeCall(String cursor, Integer pageSize, Integer doctor, final ApiCallback _callback) throws ApiException {
        return billingProfilesListCall(cursor, pageSize, doctor, _callback);

    }

    /**
     * 
     * Retrieve or search billing profiles
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param doctor  (optional)
     * @return BillingProfilesList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public BillingProfilesList200Response billingProfilesList(String cursor, Integer pageSize, Integer doctor) throws ApiException {
        ApiResponse<BillingProfilesList200Response> localVarResp = billingProfilesListWithHttpInfo(cursor, pageSize, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search billing profiles
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;BillingProfilesList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BillingProfilesList200Response> billingProfilesListWithHttpInfo(String cursor, Integer pageSize, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = billingProfilesListValidateBeforeCall(cursor, pageSize, doctor, null);
        Type localVarReturnType = new TypeToken<BillingProfilesList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search billing profiles
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call billingProfilesListAsync(String cursor, Integer pageSize, Integer doctor, final ApiCallback<BillingProfilesList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = billingProfilesListValidateBeforeCall(cursor, pageSize, doctor, _callback);
        Type localVarReturnType = new TypeToken<BillingProfilesList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for billingProfilesRead
     * @param id  (required)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call billingProfilesReadCall(String id, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/billing_profiles/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call billingProfilesReadValidateBeforeCall(String id, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling billingProfilesRead(Async)");
        }

        return billingProfilesReadCall(id, doctor, _callback);

    }

    /**
     * 
     * Retrieve an existing billing profiles
     * @param id  (required)
     * @param doctor  (optional)
     * @return BillingProfile
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public BillingProfile billingProfilesRead(String id, Integer doctor) throws ApiException {
        ApiResponse<BillingProfile> localVarResp = billingProfilesReadWithHttpInfo(id, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing billing profiles
     * @param id  (required)
     * @param doctor  (optional)
     * @return ApiResponse&lt;BillingProfile&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BillingProfile> billingProfilesReadWithHttpInfo(String id, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = billingProfilesReadValidateBeforeCall(id, doctor, null);
        Type localVarReturnType = new TypeToken<BillingProfile>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing billing profiles
     * @param id  (required)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call billingProfilesReadAsync(String id, Integer doctor, final ApiCallback<BillingProfile> _callback) throws ApiException {

        okhttp3.Call localVarCall = billingProfilesReadValidateBeforeCall(id, doctor, _callback);
        Type localVarReturnType = new TypeToken<BillingProfile>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for commLogsCreate
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsCreateCall(String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/comm_logs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call commLogsCreateValidateBeforeCall(String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        return commLogsCreateCall(since, patient, doctor, _callback);

    }

    /**
     * 
     * Create communication (phone call) logs
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return PhoneCallLog
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public PhoneCallLog commLogsCreate(String since, Integer patient, Integer doctor) throws ApiException {
        ApiResponse<PhoneCallLog> localVarResp = commLogsCreateWithHttpInfo(since, patient, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Create communication (phone call) logs
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;PhoneCallLog&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PhoneCallLog> commLogsCreateWithHttpInfo(String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = commLogsCreateValidateBeforeCall(since, patient, doctor, null);
        Type localVarReturnType = new TypeToken<PhoneCallLog>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Create communication (phone call) logs
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsCreateAsync(String since, Integer patient, Integer doctor, final ApiCallback<PhoneCallLog> _callback) throws ApiException {

        okhttp3.Call localVarCall = commLogsCreateValidateBeforeCall(since, patient, doctor, _callback);
        Type localVarReturnType = new TypeToken<PhoneCallLog>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for commLogsList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsListCall(String cursor, Integer pageSize, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/comm_logs";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call commLogsListValidateBeforeCall(String cursor, Integer pageSize, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        return commLogsListCall(cursor, pageSize, since, patient, doctor, _callback);

    }

    /**
     * 
     * Retrieve or search communicatioin (phone call) logs
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return CommLogsList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public CommLogsList200Response commLogsList(String cursor, Integer pageSize, String since, Integer patient, Integer doctor) throws ApiException {
        ApiResponse<CommLogsList200Response> localVarResp = commLogsListWithHttpInfo(cursor, pageSize, since, patient, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search communicatioin (phone call) logs
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;CommLogsList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CommLogsList200Response> commLogsListWithHttpInfo(String cursor, Integer pageSize, String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = commLogsListValidateBeforeCall(cursor, pageSize, since, patient, doctor, null);
        Type localVarReturnType = new TypeToken<CommLogsList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search communicatioin (phone call) logs
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsListAsync(String cursor, Integer pageSize, String since, Integer patient, Integer doctor, final ApiCallback<CommLogsList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = commLogsListValidateBeforeCall(cursor, pageSize, since, patient, doctor, _callback);
        Type localVarReturnType = new TypeToken<CommLogsList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for commLogsPartialUpdate
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsPartialUpdateCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/comm_logs/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PATCH", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call commLogsPartialUpdateValidateBeforeCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling commLogsPartialUpdate(Async)");
        }

        return commLogsPartialUpdateCall(id, since, patient, doctor, _callback);

    }

    /**
     * 
     * Update an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public void commLogsPartialUpdate(String id, String since, Integer patient, Integer doctor) throws ApiException {
        commLogsPartialUpdateWithHttpInfo(id, since, patient, doctor);
    }

    /**
     * 
     * Update an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> commLogsPartialUpdateWithHttpInfo(String id, String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = commLogsPartialUpdateValidateBeforeCall(id, since, patient, doctor, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Update an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsPartialUpdateAsync(String id, String since, Integer patient, Integer doctor, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = commLogsPartialUpdateValidateBeforeCall(id, since, patient, doctor, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for commLogsRead
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsReadCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/comm_logs/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call commLogsReadValidateBeforeCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling commLogsRead(Async)");
        }

        return commLogsReadCall(id, since, patient, doctor, _callback);

    }

    /**
     * 
     * Retrieve an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return PhoneCallLog
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public PhoneCallLog commLogsRead(String id, String since, Integer patient, Integer doctor) throws ApiException {
        ApiResponse<PhoneCallLog> localVarResp = commLogsReadWithHttpInfo(id, since, patient, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;PhoneCallLog&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PhoneCallLog> commLogsReadWithHttpInfo(String id, String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = commLogsReadValidateBeforeCall(id, since, patient, doctor, null);
        Type localVarReturnType = new TypeToken<PhoneCallLog>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsReadAsync(String id, String since, Integer patient, Integer doctor, final ApiCallback<PhoneCallLog> _callback) throws ApiException {

        okhttp3.Call localVarCall = commLogsReadValidateBeforeCall(id, since, patient, doctor, _callback);
        Type localVarReturnType = new TypeToken<PhoneCallLog>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for commLogsUpdate
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsUpdateCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/comm_logs/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call commLogsUpdateValidateBeforeCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling commLogsUpdate(Async)");
        }

        return commLogsUpdateCall(id, since, patient, doctor, _callback);

    }

    /**
     * 
     * Update an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public void commLogsUpdate(String id, String since, Integer patient, Integer doctor) throws ApiException {
        commLogsUpdateWithHttpInfo(id, since, patient, doctor);
    }

    /**
     * 
     * Update an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> commLogsUpdateWithHttpInfo(String id, String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = commLogsUpdateValidateBeforeCall(id, since, patient, doctor, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * Update an existing communication (phone call) logs
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call commLogsUpdateAsync(String id, String since, Integer patient, Integer doctor, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = commLogsUpdateValidateBeforeCall(id, since, patient, doctor, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for customInsurancePlanNamesList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customInsurancePlanNamesListCall(String cursor, Integer pageSize, String since, Integer user, String name, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/custom_insurance_plan_names";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (user != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("user", user));
        }

        if (name != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("name", name));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call customInsurancePlanNamesListValidateBeforeCall(String cursor, Integer pageSize, String since, Integer user, String name, Integer doctor, final ApiCallback _callback) throws ApiException {
        return customInsurancePlanNamesListCall(cursor, pageSize, since, user, name, doctor, _callback);

    }

    /**
     * 
     * Retrieve or search custom insurance plan names
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @return CustomInsurancePlanNamesList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public CustomInsurancePlanNamesList200Response customInsurancePlanNamesList(String cursor, Integer pageSize, String since, Integer user, String name, Integer doctor) throws ApiException {
        ApiResponse<CustomInsurancePlanNamesList200Response> localVarResp = customInsurancePlanNamesListWithHttpInfo(cursor, pageSize, since, user, name, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search custom insurance plan names
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;CustomInsurancePlanNamesList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CustomInsurancePlanNamesList200Response> customInsurancePlanNamesListWithHttpInfo(String cursor, Integer pageSize, String since, Integer user, String name, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = customInsurancePlanNamesListValidateBeforeCall(cursor, pageSize, since, user, name, doctor, null);
        Type localVarReturnType = new TypeToken<CustomInsurancePlanNamesList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search custom insurance plan names
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customInsurancePlanNamesListAsync(String cursor, Integer pageSize, String since, Integer user, String name, Integer doctor, final ApiCallback<CustomInsurancePlanNamesList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = customInsurancePlanNamesListValidateBeforeCall(cursor, pageSize, since, user, name, doctor, _callback);
        Type localVarReturnType = new TypeToken<CustomInsurancePlanNamesList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for customInsurancePlanNamesRead
     * @param id  (required)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customInsurancePlanNamesReadCall(String id, String since, Integer user, String name, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/custom_insurance_plan_names/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (user != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("user", user));
        }

        if (name != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("name", name));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call customInsurancePlanNamesReadValidateBeforeCall(String id, String since, Integer user, String name, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling customInsurancePlanNamesRead(Async)");
        }

        return customInsurancePlanNamesReadCall(id, since, user, name, doctor, _callback);

    }

    /**
     * 
     * Retrieve an existing custom insurance plan name
     * @param id  (required)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @return CustomInsurancePlanName
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public CustomInsurancePlanName customInsurancePlanNamesRead(String id, String since, Integer user, String name, Integer doctor) throws ApiException {
        ApiResponse<CustomInsurancePlanName> localVarResp = customInsurancePlanNamesReadWithHttpInfo(id, since, user, name, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing custom insurance plan name
     * @param id  (required)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;CustomInsurancePlanName&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CustomInsurancePlanName> customInsurancePlanNamesReadWithHttpInfo(String id, String since, Integer user, String name, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = customInsurancePlanNamesReadValidateBeforeCall(id, since, user, name, doctor, null);
        Type localVarReturnType = new TypeToken<CustomInsurancePlanName>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing custom insurance plan name
     * @param id  (required)
     * @param since  (optional)
     * @param user  (optional)
     * @param name  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call customInsurancePlanNamesReadAsync(String id, String since, Integer user, String name, Integer doctor, final ApiCallback<CustomInsurancePlanName> _callback) throws ApiException {

        okhttp3.Call localVarCall = customInsurancePlanNamesReadValidateBeforeCall(id, since, user, name, doctor, _callback);
        Type localVarReturnType = new TypeToken<CustomInsurancePlanName>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for eligibilityChecksList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call eligibilityChecksListCall(String cursor, Integer pageSize, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/eligibility_checks";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (appointmentDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment_date", appointmentDate));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (queryDateRange != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("query_date_range", queryDateRange));
        }

        if (appointmentDateRange != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment_date_range", appointmentDateRange));
        }

        if (queryDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("query_date", queryDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call eligibilityChecksListValidateBeforeCall(String cursor, Integer pageSize, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient, final ApiCallback _callback) throws ApiException {
        return eligibilityChecksListCall(cursor, pageSize, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient, _callback);

    }

    /**
     * 
     * Retrieve or search past eligibility checks for patient
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @return EligibilityChecksList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public EligibilityChecksList200Response eligibilityChecksList(String cursor, Integer pageSize, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient) throws ApiException {
        ApiResponse<EligibilityChecksList200Response> localVarResp = eligibilityChecksListWithHttpInfo(cursor, pageSize, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search past eligibility checks for patient
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @return ApiResponse&lt;EligibilityChecksList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<EligibilityChecksList200Response> eligibilityChecksListWithHttpInfo(String cursor, Integer pageSize, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient) throws ApiException {
        okhttp3.Call localVarCall = eligibilityChecksListValidateBeforeCall(cursor, pageSize, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient, null);
        Type localVarReturnType = new TypeToken<EligibilityChecksList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search past eligibility checks for patient
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call eligibilityChecksListAsync(String cursor, Integer pageSize, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient, final ApiCallback<EligibilityChecksList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = eligibilityChecksListValidateBeforeCall(cursor, pageSize, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient, _callback);
        Type localVarReturnType = new TypeToken<EligibilityChecksList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for eligibilityChecksRead
     * @param id  (required)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call eligibilityChecksReadCall(String id, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/eligibility_checks/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (appointmentDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment_date", appointmentDate));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (queryDateRange != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("query_date_range", queryDateRange));
        }

        if (appointmentDateRange != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment_date_range", appointmentDateRange));
        }

        if (queryDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("query_date", queryDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call eligibilityChecksReadValidateBeforeCall(String id, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling eligibilityChecksRead(Async)");
        }

        return eligibilityChecksReadCall(id, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient, _callback);

    }

    /**
     * 
     * Retrieve an existing past eligibility check
     * @param id  (required)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @return Coverage
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public Coverage eligibilityChecksRead(String id, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient) throws ApiException {
        ApiResponse<Coverage> localVarResp = eligibilityChecksReadWithHttpInfo(id, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing past eligibility check
     * @param id  (required)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @return ApiResponse&lt;Coverage&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Coverage> eligibilityChecksReadWithHttpInfo(String id, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient) throws ApiException {
        okhttp3.Call localVarCall = eligibilityChecksReadValidateBeforeCall(id, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient, null);
        Type localVarReturnType = new TypeToken<Coverage>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing past eligibility check
     * @param id  (required)
     * @param appointment  (optional)
     * @param appointmentDate  (optional)
     * @param doctor  (optional)
     * @param queryDateRange  (optional)
     * @param appointmentDateRange  (optional)
     * @param queryDate  (optional)
     * @param patient  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call eligibilityChecksReadAsync(String id, Integer appointment, String appointmentDate, Integer doctor, String queryDateRange, String appointmentDateRange, String queryDate, Integer patient, final ApiCallback<Coverage> _callback) throws ApiException {

        okhttp3.Call localVarCall = eligibilityChecksReadValidateBeforeCall(id, appointment, appointmentDate, doctor, queryDateRange, appointmentDateRange, queryDate, patient, _callback);
        Type localVarReturnType = new TypeToken<Coverage>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for lineItemsCreate
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsCreateCall(String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/line_items";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call lineItemsCreateValidateBeforeCall(String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        return lineItemsCreateCall(postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);

    }

    /**
     * 
     * Create billing line item for appointments
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return BillingLineItem
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public BillingLineItem lineItemsCreate(String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        ApiResponse<BillingLineItem> localVarResp = lineItemsCreateWithHttpInfo(postedDate, patient, office, doctor, since, appointment, serviceDate);
        return localVarResp.getData();
    }

    /**
     * 
     * Create billing line item for appointments
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;BillingLineItem&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BillingLineItem> lineItemsCreateWithHttpInfo(String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = lineItemsCreateValidateBeforeCall(postedDate, patient, office, doctor, since, appointment, serviceDate, null);
        Type localVarReturnType = new TypeToken<BillingLineItem>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Create billing line item for appointments
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsCreateAsync(String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback<BillingLineItem> _callback) throws ApiException {

        okhttp3.Call localVarCall = lineItemsCreateValidateBeforeCall(postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);
        Type localVarReturnType = new TypeToken<BillingLineItem>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for lineItemsDelete
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsDeleteCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/line_items/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "DELETE", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call lineItemsDeleteValidateBeforeCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling lineItemsDelete(Async)");
        }

        return lineItemsDeleteCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);

    }

    /**
     * 
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public void lineItemsDelete(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        lineItemsDeleteWithHttpInfo(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
    }

    /**
     * 
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> lineItemsDeleteWithHttpInfo(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = lineItemsDeleteValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsDeleteAsync(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = lineItemsDeleteValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for lineItemsList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsListCall(String cursor, Integer pageSize, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/line_items";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call lineItemsListValidateBeforeCall(String cursor, Integer pageSize, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        return lineItemsListCall(cursor, pageSize, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);

    }

    /**
     * 
     * Retrieve or search billing line items
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return LineItemsList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public LineItemsList200Response lineItemsList(String cursor, Integer pageSize, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        ApiResponse<LineItemsList200Response> localVarResp = lineItemsListWithHttpInfo(cursor, pageSize, postedDate, patient, office, doctor, since, appointment, serviceDate);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search billing line items
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;LineItemsList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LineItemsList200Response> lineItemsListWithHttpInfo(String cursor, Integer pageSize, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = lineItemsListValidateBeforeCall(cursor, pageSize, postedDate, patient, office, doctor, since, appointment, serviceDate, null);
        Type localVarReturnType = new TypeToken<LineItemsList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search billing line items
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsListAsync(String cursor, Integer pageSize, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback<LineItemsList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = lineItemsListValidateBeforeCall(cursor, pageSize, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);
        Type localVarReturnType = new TypeToken<LineItemsList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for lineItemsPartialUpdate
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsPartialUpdateCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/line_items/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PATCH", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call lineItemsPartialUpdateValidateBeforeCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling lineItemsPartialUpdate(Async)");
        }

        return lineItemsPartialUpdateCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);

    }

    /**
     * 
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public void lineItemsPartialUpdate(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        lineItemsPartialUpdateWithHttpInfo(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
    }

    /**
     * 
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> lineItemsPartialUpdateWithHttpInfo(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = lineItemsPartialUpdateValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsPartialUpdateAsync(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = lineItemsPartialUpdateValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for lineItemsRead
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsReadCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/line_items/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call lineItemsReadValidateBeforeCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling lineItemsRead(Async)");
        }

        return lineItemsReadCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);

    }

    /**
     * 
     * Retrieve an existing billing line item
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return BillingLineItem
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public BillingLineItem lineItemsRead(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        ApiResponse<BillingLineItem> localVarResp = lineItemsReadWithHttpInfo(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing billing line item
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;BillingLineItem&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BillingLineItem> lineItemsReadWithHttpInfo(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = lineItemsReadValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, null);
        Type localVarReturnType = new TypeToken<BillingLineItem>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing billing line item
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsReadAsync(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback<BillingLineItem> _callback) throws ApiException {

        okhttp3.Call localVarCall = lineItemsReadValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);
        Type localVarReturnType = new TypeToken<BillingLineItem>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for lineItemsUpdate
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsUpdateCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/line_items/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
        }

        final String[] localVarAccepts = {
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "PUT", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call lineItemsUpdateValidateBeforeCall(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling lineItemsUpdate(Async)");
        }

        return lineItemsUpdateCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);

    }

    /**
     * 
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public void lineItemsUpdate(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        lineItemsUpdateWithHttpInfo(id, postedDate, patient, office, doctor, since, appointment, serviceDate);
    }

    /**
     * 
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;Void&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Void> lineItemsUpdateWithHttpInfo(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = lineItemsUpdateValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, null);
        return localVarApiClient.execute(localVarCall);
    }

    /**
     *  (asynchronously)
     * 
     * @param id  (required)
     * @param postedDate  (optional)
     * @param patient  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param since  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 204 </td><td> No Content </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call lineItemsUpdateAsync(String id, String postedDate, Integer patient, Integer office, Integer doctor, String since, Integer appointment, String serviceDate, final ApiCallback<Void> _callback) throws ApiException {

        okhttp3.Call localVarCall = lineItemsUpdateValidateBeforeCall(id, postedDate, patient, office, doctor, since, appointment, serviceDate, _callback);
        localVarApiClient.executeAsync(localVarCall, _callback);
        return localVarCall;
    }
    /**
     * Build call for patientPaymentLogList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentLogListCall(String cursor, Integer pageSize, String since, Integer office, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/patient_payment_log";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call patientPaymentLogListValidateBeforeCall(String cursor, Integer pageSize, String since, Integer office, Integer doctor, final ApiCallback _callback) throws ApiException {
        return patientPaymentLogListCall(cursor, pageSize, since, office, doctor, _callback);

    }

    /**
     * 
     * Retrieve or search patient payment logs
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @return PatientPaymentLogList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public PatientPaymentLogList200Response patientPaymentLogList(String cursor, Integer pageSize, String since, Integer office, Integer doctor) throws ApiException {
        ApiResponse<PatientPaymentLogList200Response> localVarResp = patientPaymentLogListWithHttpInfo(cursor, pageSize, since, office, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search patient payment logs
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;PatientPaymentLogList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PatientPaymentLogList200Response> patientPaymentLogListWithHttpInfo(String cursor, Integer pageSize, String since, Integer office, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = patientPaymentLogListValidateBeforeCall(cursor, pageSize, since, office, doctor, null);
        Type localVarReturnType = new TypeToken<PatientPaymentLogList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search patient payment logs
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentLogListAsync(String cursor, Integer pageSize, String since, Integer office, Integer doctor, final ApiCallback<PatientPaymentLogList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = patientPaymentLogListValidateBeforeCall(cursor, pageSize, since, office, doctor, _callback);
        Type localVarReturnType = new TypeToken<PatientPaymentLogList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for patientPaymentLogRead
     * @param id  (required)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentLogReadCall(String id, String since, Integer office, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/patient_payment_log/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (office != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("office", office));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call patientPaymentLogReadValidateBeforeCall(String id, String since, Integer office, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling patientPaymentLogRead(Async)");
        }

        return patientPaymentLogReadCall(id, since, office, doctor, _callback);

    }

    /**
     * 
     * Retrieve an existing patient payment log
     * @param id  (required)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @return CashPaymentLog
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public CashPaymentLog patientPaymentLogRead(String id, String since, Integer office, Integer doctor) throws ApiException {
        ApiResponse<CashPaymentLog> localVarResp = patientPaymentLogReadWithHttpInfo(id, since, office, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing patient payment log
     * @param id  (required)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;CashPaymentLog&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CashPaymentLog> patientPaymentLogReadWithHttpInfo(String id, String since, Integer office, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = patientPaymentLogReadValidateBeforeCall(id, since, office, doctor, null);
        Type localVarReturnType = new TypeToken<CashPaymentLog>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing patient payment log
     * @param id  (required)
     * @param since  (optional)
     * @param office  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentLogReadAsync(String id, String since, Integer office, Integer doctor, final ApiCallback<CashPaymentLog> _callback) throws ApiException {

        okhttp3.Call localVarCall = patientPaymentLogReadValidateBeforeCall(id, since, office, doctor, _callback);
        Type localVarReturnType = new TypeToken<CashPaymentLog>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for patientPaymentsCreate
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentsCreateCall(String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/patient_payments";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call patientPaymentsCreateValidateBeforeCall(String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        return patientPaymentsCreateCall(since, patient, doctor, _callback);

    }

    /**
     * 
     * Create patient payment
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return CashPayment
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public CashPayment patientPaymentsCreate(String since, Integer patient, Integer doctor) throws ApiException {
        ApiResponse<CashPayment> localVarResp = patientPaymentsCreateWithHttpInfo(since, patient, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Create patient payment
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;CashPayment&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CashPayment> patientPaymentsCreateWithHttpInfo(String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = patientPaymentsCreateValidateBeforeCall(since, patient, doctor, null);
        Type localVarReturnType = new TypeToken<CashPayment>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Create patient payment
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 201 </td><td> Created </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentsCreateAsync(String since, Integer patient, Integer doctor, final ApiCallback<CashPayment> _callback) throws ApiException {

        okhttp3.Call localVarCall = patientPaymentsCreateValidateBeforeCall(since, patient, doctor, _callback);
        Type localVarReturnType = new TypeToken<CashPayment>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for patientPaymentsList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentsListCall(String cursor, Integer pageSize, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/patient_payments";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call patientPaymentsListValidateBeforeCall(String cursor, Integer pageSize, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        return patientPaymentsListCall(cursor, pageSize, since, patient, doctor, _callback);

    }

    /**
     * 
     * Retrieve or search patient payments
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return PatientPaymentsList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public PatientPaymentsList200Response patientPaymentsList(String cursor, Integer pageSize, String since, Integer patient, Integer doctor) throws ApiException {
        ApiResponse<PatientPaymentsList200Response> localVarResp = patientPaymentsListWithHttpInfo(cursor, pageSize, since, patient, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search patient payments
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;PatientPaymentsList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<PatientPaymentsList200Response> patientPaymentsListWithHttpInfo(String cursor, Integer pageSize, String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = patientPaymentsListValidateBeforeCall(cursor, pageSize, since, patient, doctor, null);
        Type localVarReturnType = new TypeToken<PatientPaymentsList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search patient payments
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentsListAsync(String cursor, Integer pageSize, String since, Integer patient, Integer doctor, final ApiCallback<PatientPaymentsList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = patientPaymentsListValidateBeforeCall(cursor, pageSize, since, patient, doctor, _callback);
        Type localVarReturnType = new TypeToken<PatientPaymentsList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for patientPaymentsRead
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentsReadCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/patient_payments/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call patientPaymentsReadValidateBeforeCall(String id, String since, Integer patient, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling patientPaymentsRead(Async)");
        }

        return patientPaymentsReadCall(id, since, patient, doctor, _callback);

    }

    /**
     * 
     * Retrieve an existing patient payment
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return CashPayment
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public CashPayment patientPaymentsRead(String id, String since, Integer patient, Integer doctor) throws ApiException {
        ApiResponse<CashPayment> localVarResp = patientPaymentsReadWithHttpInfo(id, since, patient, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing patient payment
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;CashPayment&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<CashPayment> patientPaymentsReadWithHttpInfo(String id, String since, Integer patient, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = patientPaymentsReadValidateBeforeCall(id, since, patient, doctor, null);
        Type localVarReturnType = new TypeToken<CashPayment>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing patient payment
     * @param id  (required)
     * @param since  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call patientPaymentsReadAsync(String id, String since, Integer patient, Integer doctor, final ApiCallback<CashPayment> _callback) throws ApiException {

        okhttp3.Call localVarCall = patientPaymentsReadValidateBeforeCall(id, since, patient, doctor, _callback);
        Type localVarReturnType = new TypeToken<CashPayment>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for proceduresList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call proceduresListCall(String cursor, Integer pageSize, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/procedures";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (muDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mu_date", muDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (muDateRange != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mu_date_range", muDateRange));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call proceduresListValidateBeforeCall(String cursor, Integer pageSize, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        return proceduresListCall(cursor, pageSize, muDate, patient, doctor, muDateRange, appointment, serviceDate, _callback);

    }

    /**
     * 
     * 
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return LineItemsList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public LineItemsList200Response proceduresList(String cursor, Integer pageSize, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate) throws ApiException {
        ApiResponse<LineItemsList200Response> localVarResp = proceduresListWithHttpInfo(cursor, pageSize, muDate, patient, doctor, muDateRange, appointment, serviceDate);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;LineItemsList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LineItemsList200Response> proceduresListWithHttpInfo(String cursor, Integer pageSize, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = proceduresListValidateBeforeCall(cursor, pageSize, muDate, patient, doctor, muDateRange, appointment, serviceDate, null);
        Type localVarReturnType = new TypeToken<LineItemsList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call proceduresListAsync(String cursor, Integer pageSize, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate, final ApiCallback<LineItemsList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = proceduresListValidateBeforeCall(cursor, pageSize, muDate, patient, doctor, muDateRange, appointment, serviceDate, _callback);
        Type localVarReturnType = new TypeToken<LineItemsList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for proceduresRead
     * @param id  (required)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call proceduresReadCall(String id, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/procedures/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (muDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mu_date", muDate));
        }

        if (patient != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("patient", patient));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
        }

        if (muDateRange != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("mu_date_range", muDateRange));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (serviceDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("service_date", serviceDate));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call proceduresReadValidateBeforeCall(String id, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling proceduresRead(Async)");
        }

        return proceduresReadCall(id, muDate, patient, doctor, muDateRange, appointment, serviceDate, _callback);

    }

    /**
     * 
     * 
     * @param id  (required)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return BillingLineItem
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public BillingLineItem proceduresRead(String id, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate) throws ApiException {
        ApiResponse<BillingLineItem> localVarResp = proceduresReadWithHttpInfo(id, muDate, patient, doctor, muDateRange, appointment, serviceDate);
        return localVarResp.getData();
    }

    /**
     * 
     * 
     * @param id  (required)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @return ApiResponse&lt;BillingLineItem&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<BillingLineItem> proceduresReadWithHttpInfo(String id, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate) throws ApiException {
        okhttp3.Call localVarCall = proceduresReadValidateBeforeCall(id, muDate, patient, doctor, muDateRange, appointment, serviceDate, null);
        Type localVarReturnType = new TypeToken<BillingLineItem>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * 
     * @param id  (required)
     * @param muDate  (optional)
     * @param patient  (optional)
     * @param doctor  (optional)
     * @param muDateRange  (optional)
     * @param appointment  (optional)
     * @param serviceDate  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call proceduresReadAsync(String id, String muDate, Integer patient, Integer doctor, String muDateRange, Integer appointment, String serviceDate, final ApiCallback<BillingLineItem> _callback) throws ApiException {

        okhttp3.Call localVarCall = proceduresReadValidateBeforeCall(id, muDate, patient, doctor, muDateRange, appointment, serviceDate, _callback);
        Type localVarReturnType = new TypeToken<BillingLineItem>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for transactionsList
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsListCall(String cursor, Integer pageSize, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/transactions";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (cursor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("cursor", cursor));
        }

        if (pageSize != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("page_size", pageSize));
        }

        if (lineItem != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("line_item", lineItem));
        }

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call transactionsListValidateBeforeCall(String cursor, Integer pageSize, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor, final ApiCallback _callback) throws ApiException {
        return transactionsListCall(cursor, pageSize, lineItem, postedDate, appointment, since, doctor, _callback);

    }

    /**
     * 
     * Retrieve or search insurance transactions associated with billing line items
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @return TransactionsList200Response
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public TransactionsList200Response transactionsList(String cursor, Integer pageSize, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor) throws ApiException {
        ApiResponse<TransactionsList200Response> localVarResp = transactionsListWithHttpInfo(cursor, pageSize, lineItem, postedDate, appointment, since, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve or search insurance transactions associated with billing line items
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;TransactionsList200Response&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<TransactionsList200Response> transactionsListWithHttpInfo(String cursor, Integer pageSize, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = transactionsListValidateBeforeCall(cursor, pageSize, lineItem, postedDate, appointment, since, doctor, null);
        Type localVarReturnType = new TypeToken<TransactionsList200Response>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve or search insurance transactions associated with billing line items
     * @param cursor  (optional)
     * @param pageSize  (optional)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsListAsync(String cursor, Integer pageSize, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor, final ApiCallback<TransactionsList200Response> _callback) throws ApiException {

        okhttp3.Call localVarCall = transactionsListValidateBeforeCall(cursor, pageSize, lineItem, postedDate, appointment, since, doctor, _callback);
        Type localVarReturnType = new TypeToken<TransactionsList200Response>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
    /**
     * Build call for transactionsRead
     * @param id  (required)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsReadCall(String id, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor, final ApiCallback _callback) throws ApiException {
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
        String localVarPath = "/api/transactions/{id}"
            .replace("{" + "id" + "}", localVarApiClient.escapeString(id.toString()));

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        if (lineItem != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("line_item", lineItem));
        }

        if (postedDate != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("posted_date", postedDate));
        }

        if (appointment != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("appointment", appointment));
        }

        if (since != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("since", since));
        }

        if (doctor != null) {
            localVarQueryParams.addAll(localVarApiClient.parameterToPair("doctor", doctor));
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

        String[] localVarAuthNames = new String[] { "drchrono_oauth2" };
        return localVarApiClient.buildCall(basePath, localVarPath, "GET", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call transactionsReadValidateBeforeCall(String id, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'id' is set
        if (id == null) {
            throw new ApiException("Missing the required parameter 'id' when calling transactionsRead(Async)");
        }

        return transactionsReadCall(id, lineItem, postedDate, appointment, since, doctor, _callback);

    }

    /**
     * 
     * Retrieve an existing insurance transaction
     * @param id  (required)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @return LineItemTransaction
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public LineItemTransaction transactionsRead(String id, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor) throws ApiException {
        ApiResponse<LineItemTransaction> localVarResp = transactionsReadWithHttpInfo(id, lineItem, postedDate, appointment, since, doctor);
        return localVarResp.getData();
    }

    /**
     * 
     * Retrieve an existing insurance transaction
     * @param id  (required)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @return ApiResponse&lt;LineItemTransaction&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<LineItemTransaction> transactionsReadWithHttpInfo(String id, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor) throws ApiException {
        okhttp3.Call localVarCall = transactionsReadValidateBeforeCall(id, lineItem, postedDate, appointment, since, doctor, null);
        Type localVarReturnType = new TypeToken<LineItemTransaction>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     *  (asynchronously)
     * Retrieve an existing insurance transaction
     * @param id  (required)
     * @param lineItem  (optional)
     * @param postedDate  (optional)
     * @param appointment  (optional)
     * @param since  (optional)
     * @param doctor  (optional)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> OK </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized </td><td>  -  </td></tr>
        <tr><td> 403 </td><td> Permission Denied </td><td>  -  </td></tr>
        <tr><td> 404 </td><td> Not Found </td><td>  -  </td></tr>
        <tr><td> 405 </td><td> Method Not Allowed </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call transactionsReadAsync(String id, Integer lineItem, String postedDate, Integer appointment, String since, Integer doctor, final ApiCallback<LineItemTransaction> _callback) throws ApiException {

        okhttp3.Call localVarCall = transactionsReadValidateBeforeCall(id, lineItem, postedDate, appointment, since, doctor, _callback);
        Type localVarReturnType = new TypeToken<LineItemTransaction>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
