/**
 * 
 * This document is intended as a detailed reference for the precise behavior of the drchrono API. If this is your first time using the API, start with our <a href=\"/api-docs-old/tutorial\">tutorial</a>. If you are upgrading from a previous version, take a look at the changelog section.  # Authorization  ## Initial authorization  There are three main steps in the OAuth 2.0 authentication workflow:  1. Redirect the provider to the authorization page. 2. The provider authorizes your application and is redirected back to    your web application. 3. Your application exchanges the `authorization_code` that came with    the redirect for an `access_token` and `refresh_token`.  ### Step 1: Redirect to drchrono  The first step is redirecting your user to drchrono, typically with a button labeled \"Connect to drchrono\" or \"Login with drchrono\".  This is just a link that takes your user to the following URL:      https://drchrono.com/o/authorize/?redirect_uri=REDIRECT_URI_ENCODED&response_type=code&client_id=CLIENT_ID_ENCODED&scope=SCOPES_ENCODED  - `REDIRECT_URI_ENCODED` is the URL-encoded version of the redirect URI (as registered for your application and used in later steps). - `CLIENT_ID_ENCODED` is the URL-encoded version of your application's client ID. - `SCOPES_ENCODED` is a URL-encoded version of a space-separated list of scopes, which can be found in each endpoint or omitted to default to all scopes.  The `scope` parameter consists of an optional, space-separated list of scopes your application is requesting. If omitted, all scopes will be requested.  Scopes are of the form `BASE_SCOPE:[read|write]` where `BASE_SCOPE` is any of `user`, `calendar`, `patients`, `patients:summary`, `billing`, `clinical` and `labs`. You should request only the scopes you need. For instance, an application which sends \"Happy Birthday!\" emails to a doctor's patients on their birthdays would use the scope parameter `\"patients:summary:read\"`, while one that allows patients to schedule appointments online would need at least `\"patients:summary:read patients:summary:write calendar:read calendar:write clinical:read clinical:write\"`.  ### Step 2: Provider authorization  After logging in (if necessary), the provider will be presented with a screen with your application's name and the list of permissions you requested (via the `scope` parameter).  When they click the \"Authorize\" button, they will be redirected to your redirect URI with a `code` query parameter appended, which contains an authorization code to be used in step 3.  If they click the \"Cancel\" button, they will be redirected to your redirect URI with `error=access_denied` instead.  Note: This authorization code expires extremely quickly, so you must perform step 3 immediately, ideally before rendering the resulting page for the end user.  ### Step 3: Token exchange  The `code` obtained from step 2 is usable exactly once to obtain an access token and refresh token.  Here is an example token exchange in Python:      import datetime, pytz, requests      if 'error' in get_params:         raise ValueError('Error authorizing application: %s' % get_params[error])      response = requests.post('https://drchrono.com/o/token/', data={         'code': get_params['code'],         'grant_type': 'authorization_code',         'redirect_uri': 'http://mytestapp.com/redirect_uri',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     response.raise_for_status()     data = response.json()      # Save these in your database associated with the user     access_token = data['access_token']     refresh_token = data['refresh_token']     expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])  You now have all you need to make API requests authenticated as that provider. When using this access token, you'll only be able to access the data that the user has access to and that you have been granted permissions for.  ## Refreshing an access token  Access tokens only last 48 hours (given in seconds in the `'expires_in'` key in the token exchange step above), so they occasionally need to be refreshed.  It would be inconvenient to ask the user to re-authorize every time, so instead you can use the refresh token like the original authorization to obtain a new access token.  Replace the `code` parameter with `refresh_token`, change the value `grant_type` from `authorization_code` to `refresh_token`, and omit the `redirect_uri` parameter.  Example in Python:      ...     response = requests.post('https://drchrono.com/o/token/', data={         'refresh_token': get_refresh_token(),         'grant_type': 'refresh_token',         'client_id': 'abcdefg12345',         'client_secret': 'abcdefg12345',     })     ...  # Webhooks  In order to use drchrono API webhooks, you first need to have an API application on file (even if it is in Test Model). Each API webhook is associated with one API application, go to <a href=\"/api-management/\" target=\"_blank\">here</a> to set up both API applications and webhooks!  Once you registered an API application, you will see webhook section in each saved API applications. Create a webhook and register some events there and save all the changes, then you are good to go!  ## Webhooks setup  All fields under webhooks section are required.  **Callback URL** Callback URl is used to receive all hooks when subscribed events are triggered. This should be an URL under your control.  **Secret token** Secret token is used to verify webhooks, this is very important, please set something with high entropy. Also we will talk more about this later.  **Events**  Events is used to register events you want to receiver notification when they happen. Currently we support following events.  Event name | Event description ---------- | ----------------- `APPOINTMENT_CREATE` | We will deliver a hook any time an appointment is created `APPOINTMENT_MODIFY` | We will deliver a hook any time an appointment is modified `PATIENT_CREATE` | We will deliver a hook any time a patient is created `PATIENT_MODIFY` | We will deliver a hook any time a patient is modified `PATIENT_PROBLEM_CREATE` | We will deliver a hook any time a patient problem is created `PATIENT_PROBLEM_MODIFY` | We will deliver a hook any time a patient problem is modified `PATIENT_ALLERGY_CREATE` | We will deliver a hook any time a patient allergy is created `PATIENT_ALLERGY_MODIFY` | We will deliver a hook any time a patient allergy is modified `PATIENT_MEDICATION_CREATE` | We will deliver a hook any time a patient medication is created `PATIENT_MEDICATION_MODIFY` | We will deliver a hook any time a patient medication is modified `CLINICAL_NOTE_LOCK` | We will deliver a hook any time a clinical note is locked `CLINICAL_NOTE_UNLOCK` | We will deliver a hook any time a clinical note is unlocked `TASK_CREATE` | We will deliver a hook any time a task is created `TASK_MODIFY` | We will deliver a hook any time a task is modified and any time creation, modification and deletion of task notes, associated task item `TASK_DELETE` | We will deliver a hook any time a task is deleted   ## Webhooks verification  In order to make sure the callback URL in webhook is under your control, we added a verification step before we send any hooks out to you.  Verification can be done by clicking \"Verify webhook\" button in webhooks setup page. After you click the button, we will send a `GET` request to the callback URL, along with a parameter called `msg`.  Please use your webhook's secret token as hash key and SHA-256 as digest constructor, hash the `msg` value with <a href=\"https://tools.ietf.org/html/rfc2104.html\">HMAC algorithm</a>. And we expect a `200` JSON response, in JSON response body, there should be a key called `secret_token` existing, and its value should be equal to the <strong>hashed</strong> `msg`. Otherwise, verification will fail.  Here is an example webhook verification in Python:      import hashlib, hmac      def webhook_verify(request):         secret_token = hmac.new(WEBHOOK_SECRET_TOKEN, request.GET['msg'], hashlib.sha256).hexdigest()         return json_response({             'secret_token': secret_token         })  <div class=\"alert alert-warning\"> <b>Note:</b> Verification will be needed when webhook is first created and anytime callback URl is changed. </div>   ## Webhooks header and body  **Header**  Key | Value --- | ----- `X-drchrono-event` | Event that triggered this hook, could be any one event above or `PING` `X-drchrono-signature` | Secret token associated with this webhook `X-drchrono-delivery` | ID of this delivery  **Body**  Key | Value --- | ----- `receiver` | This will be an JSON representation of the webhook `object` | This will be an JSON representation of the object related to the triggered event, this would share same serializer as drchrono API  ## Webhooks ping and deliveries  Webhooks ping and deliveries will be sent as `POST` requests.  **PING**:  You can always ping your webhook to check things, by clicking the \"Ping webhook\" button in webhook setup page. And a hook with header `X-drchrono-event: PING` would be sent to the callback URL.  **Deliveries**:  You can check recent deliveries by clicking the \"deliveries\" link in webhook setup page. And you can resend a hook by clicking \"redeliver\" button after select a specific delivery.  ## Webhooks delivery mechanism  We will delivery a hook the moment a subscribed event is triggered. We will not record any response header or body you send back after you receive the hook. However we only consider the response status code. We will consider any `2xx` responses as successfully delivered. Any other responses, like `302` would be considered failing. And we will try to redeliver unsuccessfully delivered hooks 3 times, first redeliver happens at 1 hour after the initial event, second receliver happens 3 hours after the initial event, and the third redeliver happens 7 hours after the initial event. After these redeliveries, if the delivery is still unsuccessful, you have to redeliver it by hand.   ## Webhooks security  You may want to secure your webhooks to only consider requests send out from drchrono. And this is where <code>secret_token</code> is needed in request header. Try to set the <code>secret_token</code> to something with high entropy, a good example could be taking the output of <code>ruby -rsecurerandom -e 'puts SecureRandom.hex(20)'</code>. After this, you might want to verify all request headers you received on your server with this token.   # iframe integration  Some API apps provide additional functionality for interacting with patient data not offered by drchrono, and can benefit by being incorporated into drchrono's patient information page via iframe.  We have created a simple API to make this possible.  To make an existing API application accessible via an iframe on the patient page, you need to update either \"Patient iframe\" or \"Clinical note iframe\" section in API management page, to make the iframe to appear on (either the patient page or the clinical note page), with the URL that the iframe will use for each page, and the height it should have. The application will be reviewed before it is approved to ensure that it is functional and secure.  ## Register a Doctor  iframe applications will appear as choices on the left-hand menu of the patient page for doctors registered with your application.  To register a doctor with your application, make a `POST` request to the `/api/iframe_integration` endpoint using the access token for the corresponding doctor. This endpoint does not expect any payload.  To disable your iframe application for a doctor, make a `DELETE` request to the same endpoint.  ## Populating the iframe  There are two places where the iframe can be displayed, either within the patient detail page or the clinical note page, shown below respectively:  <img src=\"{% asset 'public/images/iframe_patient_page.png' %}\" alt=\"Iframe on the patient page\"/>  <img src=\"{% asset 'public/images/iframe_clinical_note.png' %}\" alt=\"Iframe on the clinical note page\"/>  When requesting approval for your iframe app, you must specify a URL for one or both of these pages which will serve as the base URL for your IFrame contents. When a doctor views your iframe, the source URL will have various query parameters appended to it, for example for the patient page the `src` parameter of the IFrame will be:  ``` <iframe_url>?doctor_id=<doctor_id>&patient_id=<patient_id>&practice_id=<practice_id>&iat=<iat>&jwt=<jwt> ```  The `jwt` parameter is crucial if your application transfers any sort of PHI and does not implement its own login system.  It encapsulates the other parameters in a [JSON web token (JWT)](http://jwt.io) and signs them using SHA-256 HMAC with your `client_secret` as the key.  This verifies that the iframe is being loaded within one of drchrono's pages by an authorized user.  In production, you should validate the JWT using an approved library (which are listed on the [official site](http://jwt.io)), and only use the parameters extracted from the JWT.  Using Python and Django, this might look like:      import jwt      CLIENT_SECRET = <client_secret>     MAX_TIME_DRIFT_SECONDS = 60      def validate_parameters(request):         token = request.GET['jwt']          return jwt.decode(token, CLIENT_SECRET, algorithms=['HS256'], leeway=MAX_TIME_DRIFT_SECONDS)  Modern browsers' same-origin policy means that data cannot be passed between your application and drchrono's page through the iframe.  Therefore, interaction must happen through the API, using information provided in JWT.  # Versions and deprecation  ## Stability Policy  Changes to this API version will be limited to adding endpoints, or adding fields to existing endpoints, or adding optional query parameters. Any new fields which are not read-only will be optional.  ## Deprecation Policy  The drchrono API is versioned. Versions can be in the following states:  * **Active:** This is our latest and greatest version of the API. It is actively supported by our API team and is improved upon with new features, bug fixes and optimizations that do not break backwards compatibility.  * **Deprecated:** A deprecated API version is considered second best--having been surpassed by our active API version. An API version remains in this state for one year, after which time it falls to the not supported state. A deprecated API version is passively supported; while it won't be removed until becoming unsupported, it may not receive new features but will likely be subject to security updates and performance improvements.  * **Unsupported:** An API version in the not supported state may be deactivated at any time. An application using an unsupported API version should migrate to an active API version.  ## Version Map | Version Name | Previous Name | Start Date | Deprecation Date | |--------------|---------------|------------|------------------| | v2           | v2015_08      | 08/2015    | TBA              | | v3           | v2016_06      | 06/2016    |                  | | v4           | N/A           | 09/2018    |                  |  If you are looking for documentation for an older version  - [V4(Hunt Valley)](/api-docs-old/v4/documentation) (old V4 documentation) - [V3(Sunnyvale)](/api-docs-old/v3/documentation) - [V2(Mountain View)](/api-docs-old/v2/documentation)  # Changelog  Here's changelog for different versions  - [V4 Changelog](/api-docs-old/v4/changelog) - [V3 changelog](/api-docs-old/v3/changelog)  
 *
 * The version of the OpenAPI document: v4 (Hunt Valley)
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import BillingLineItem from '../model/BillingLineItem';
import BillingProfile from '../model/BillingProfile';
import BillingProfilesList200Response from '../model/BillingProfilesList200Response';
import CashPayment from '../model/CashPayment';
import CashPaymentLog from '../model/CashPaymentLog';
import CommLogsList200Response from '../model/CommLogsList200Response';
import Coverage from '../model/Coverage';
import CustomInsurancePlanName from '../model/CustomInsurancePlanName';
import CustomInsurancePlanNamesList200Response from '../model/CustomInsurancePlanNamesList200Response';
import EligibilityChecksList200Response from '../model/EligibilityChecksList200Response';
import LineItemTransaction from '../model/LineItemTransaction';
import LineItemsList200Response from '../model/LineItemsList200Response';
import PatientPaymentLogList200Response from '../model/PatientPaymentLogList200Response';
import PatientPaymentsList200Response from '../model/PatientPaymentsList200Response';
import PhoneCallLog from '../model/PhoneCallLog';
import TransactionsList200Response from '../model/TransactionsList200Response';

/**
* Billing service.
* @module api/BillingApi
* @version v4 (Hunt Valley)
*/
export default class BillingApi {

    /**
    * Constructs a new BillingApi. 
    * @alias module:api/BillingApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the billingProfilesList operation.
     * @callback module:api/BillingApi~billingProfilesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BillingProfilesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search billing profiles
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~billingProfilesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BillingProfilesList200Response}
     */
    billingProfilesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BillingProfilesList200Response;
      return this.apiClient.callApi(
        '/api/billing_profiles', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the billingProfilesRead operation.
     * @callback module:api/BillingApi~billingProfilesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BillingProfile} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing billing profiles
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~billingProfilesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BillingProfile}
     */
    billingProfilesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling billingProfilesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BillingProfile;
      return this.apiClient.callApi(
        '/api/billing_profiles/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the commLogsCreate operation.
     * @callback module:api/BillingApi~commLogsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PhoneCallLog} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create communication (phone call) logs
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~commLogsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PhoneCallLog}
     */
    commLogsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PhoneCallLog;
      return this.apiClient.callApi(
        '/api/comm_logs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the commLogsList operation.
     * @callback module:api/BillingApi~commLogsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CommLogsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search communicatioin (phone call) logs
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~commLogsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CommLogsList200Response}
     */
    commLogsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CommLogsList200Response;
      return this.apiClient.callApi(
        '/api/comm_logs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the commLogsPartialUpdate operation.
     * @callback module:api/BillingApi~commLogsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing communication (phone call) logs
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~commLogsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    commLogsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling commLogsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/comm_logs/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the commLogsRead operation.
     * @callback module:api/BillingApi~commLogsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PhoneCallLog} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing communication (phone call) logs
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~commLogsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PhoneCallLog}
     */
    commLogsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling commLogsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PhoneCallLog;
      return this.apiClient.callApi(
        '/api/comm_logs/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the commLogsUpdate operation.
     * @callback module:api/BillingApi~commLogsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing communication (phone call) logs
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~commLogsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    commLogsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling commLogsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/comm_logs/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customInsurancePlanNamesList operation.
     * @callback module:api/BillingApi~customInsurancePlanNamesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomInsurancePlanNamesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search custom insurance plan names
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [user] 
     * @param {String} [name] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~customInsurancePlanNamesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomInsurancePlanNamesList200Response}
     */
    customInsurancePlanNamesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'since': opts['since'],
        'user': opts['user'],
        'name': opts['name'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CustomInsurancePlanNamesList200Response;
      return this.apiClient.callApi(
        '/api/custom_insurance_plan_names', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customInsurancePlanNamesRead operation.
     * @callback module:api/BillingApi~customInsurancePlanNamesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomInsurancePlanName} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing custom insurance plan name
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [user] 
     * @param {String} [name] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~customInsurancePlanNamesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomInsurancePlanName}
     */
    customInsurancePlanNamesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customInsurancePlanNamesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since'],
        'user': opts['user'],
        'name': opts['name'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CustomInsurancePlanName;
      return this.apiClient.callApi(
        '/api/custom_insurance_plan_names/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eligibilityChecksList operation.
     * @callback module:api/BillingApi~eligibilityChecksListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EligibilityChecksList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search past eligibility checks for patient
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [appointment] 
     * @param {String} [appointmentDate] 
     * @param {Number} [doctor] 
     * @param {String} [queryDateRange] 
     * @param {String} [appointmentDateRange] 
     * @param {String} [queryDate] 
     * @param {Number} [patient] 
     * @param {module:api/BillingApi~eligibilityChecksListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EligibilityChecksList200Response}
     */
    eligibilityChecksList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'appointment': opts['appointment'],
        'appointment_date': opts['appointmentDate'],
        'doctor': opts['doctor'],
        'query_date_range': opts['queryDateRange'],
        'appointment_date_range': opts['appointmentDateRange'],
        'query_date': opts['queryDate'],
        'patient': opts['patient']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = EligibilityChecksList200Response;
      return this.apiClient.callApi(
        '/api/eligibility_checks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eligibilityChecksRead operation.
     * @callback module:api/BillingApi~eligibilityChecksReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Coverage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing past eligibility check
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {String} [appointmentDate] 
     * @param {Number} [doctor] 
     * @param {String} [queryDateRange] 
     * @param {String} [appointmentDateRange] 
     * @param {String} [queryDate] 
     * @param {Number} [patient] 
     * @param {module:api/BillingApi~eligibilityChecksReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Coverage}
     */
    eligibilityChecksRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling eligibilityChecksRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'appointment': opts['appointment'],
        'appointment_date': opts['appointmentDate'],
        'doctor': opts['doctor'],
        'query_date_range': opts['queryDateRange'],
        'appointment_date_range': opts['appointmentDateRange'],
        'query_date': opts['queryDate'],
        'patient': opts['patient']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Coverage;
      return this.apiClient.callApi(
        '/api/eligibility_checks/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the lineItemsCreate operation.
     * @callback module:api/BillingApi~lineItemsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BillingLineItem} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create billing line item for appointments
     * @param {Object} opts Optional parameters
     * @param {String} [postedDate] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~lineItemsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BillingLineItem}
     */
    lineItemsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'posted_date': opts['postedDate'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BillingLineItem;
      return this.apiClient.callApi(
        '/api/line_items', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the lineItemsDelete operation.
     * @callback module:api/BillingApi~lineItemsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [postedDate] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~lineItemsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    lineItemsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling lineItemsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'posted_date': opts['postedDate'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/line_items/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the lineItemsList operation.
     * @callback module:api/BillingApi~lineItemsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LineItemsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search billing line items
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [postedDate] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~lineItemsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LineItemsList200Response}
     */
    lineItemsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'posted_date': opts['postedDate'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LineItemsList200Response;
      return this.apiClient.callApi(
        '/api/line_items', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the lineItemsPartialUpdate operation.
     * @callback module:api/BillingApi~lineItemsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [postedDate] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~lineItemsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    lineItemsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling lineItemsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'posted_date': opts['postedDate'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/line_items/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the lineItemsRead operation.
     * @callback module:api/BillingApi~lineItemsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BillingLineItem} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing billing line item
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [postedDate] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~lineItemsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BillingLineItem}
     */
    lineItemsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling lineItemsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'posted_date': opts['postedDate'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BillingLineItem;
      return this.apiClient.callApi(
        '/api/line_items/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the lineItemsUpdate operation.
     * @callback module:api/BillingApi~lineItemsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [postedDate] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~lineItemsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    lineItemsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling lineItemsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'posted_date': opts['postedDate'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/line_items/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPaymentLogList operation.
     * @callback module:api/BillingApi~patientPaymentLogListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientPaymentLogList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient payment logs
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~patientPaymentLogListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientPaymentLogList200Response}
     */
    patientPaymentLogList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'since': opts['since'],
        'office': opts['office'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PatientPaymentLogList200Response;
      return this.apiClient.callApi(
        '/api/patient_payment_log', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPaymentLogRead operation.
     * @callback module:api/BillingApi~patientPaymentLogReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CashPaymentLog} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient payment log
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~patientPaymentLogReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CashPaymentLog}
     */
    patientPaymentLogRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientPaymentLogRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since'],
        'office': opts['office'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CashPaymentLog;
      return this.apiClient.callApi(
        '/api/patient_payment_log/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPaymentsCreate operation.
     * @callback module:api/BillingApi~patientPaymentsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CashPayment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient payment
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~patientPaymentsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CashPayment}
     */
    patientPaymentsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CashPayment;
      return this.apiClient.callApi(
        '/api/patient_payments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPaymentsList operation.
     * @callback module:api/BillingApi~patientPaymentsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientPaymentsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient payments
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~patientPaymentsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientPaymentsList200Response}
     */
    patientPaymentsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PatientPaymentsList200Response;
      return this.apiClient.callApi(
        '/api/patient_payments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPaymentsRead operation.
     * @callback module:api/BillingApi~patientPaymentsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CashPayment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient payment
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~patientPaymentsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CashPayment}
     */
    patientPaymentsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientPaymentsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since'],
        'patient': opts['patient'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CashPayment;
      return this.apiClient.callApi(
        '/api/patient_payments/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the proceduresList operation.
     * @callback module:api/BillingApi~proceduresListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LineItemsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [muDate] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {String} [muDateRange] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~proceduresListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LineItemsList200Response}
     */
    proceduresList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'mu_date': opts['muDate'],
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'mu_date_range': opts['muDateRange'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LineItemsList200Response;
      return this.apiClient.callApi(
        '/api/procedures', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the proceduresRead operation.
     * @callback module:api/BillingApi~proceduresReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/BillingLineItem} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [muDate] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {String} [muDateRange] 
     * @param {Number} [appointment] 
     * @param {String} [serviceDate] 
     * @param {module:api/BillingApi~proceduresReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/BillingLineItem}
     */
    proceduresRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling proceduresRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'mu_date': opts['muDate'],
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'mu_date_range': opts['muDateRange'],
        'appointment': opts['appointment'],
        'service_date': opts['serviceDate']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = BillingLineItem;
      return this.apiClient.callApi(
        '/api/procedures/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the transactionsList operation.
     * @callback module:api/BillingApi~transactionsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TransactionsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search insurance transactions associated with billing line items
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [lineItem] 
     * @param {String} [postedDate] 
     * @param {Number} [appointment] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~transactionsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TransactionsList200Response}
     */
    transactionsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'line_item': opts['lineItem'],
        'posted_date': opts['postedDate'],
        'appointment': opts['appointment'],
        'since': opts['since'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TransactionsList200Response;
      return this.apiClient.callApi(
        '/api/transactions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the transactionsRead operation.
     * @callback module:api/BillingApi~transactionsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LineItemTransaction} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing insurance transaction
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [lineItem] 
     * @param {String} [postedDate] 
     * @param {Number} [appointment] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/BillingApi~transactionsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LineItemTransaction}
     */
    transactionsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling transactionsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'line_item': opts['lineItem'],
        'posted_date': opts['postedDate'],
        'appointment': opts['appointment'],
        'since': opts['since'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LineItemTransaction;
      return this.apiClient.callApi(
        '/api/transactions/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
