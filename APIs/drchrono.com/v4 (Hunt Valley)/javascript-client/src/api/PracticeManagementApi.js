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
import DoctorMessage from '../model/DoctorMessage';
import InventoryCategoriesList200Response from '../model/InventoryCategoriesList200Response';
import InventoryCategory from '../model/InventoryCategory';
import InventoryVaccine from '../model/InventoryVaccine';
import InventoryVaccinesList200Response from '../model/InventoryVaccinesList200Response';
import MessagesList200Response from '../model/MessagesList200Response';
import Office from '../model/Office';
import OfficesList200Response from '../model/OfficesList200Response';
import Task from '../model/Task';
import TaskCategoriesList200Response from '../model/TaskCategoriesList200Response';
import TaskCategory from '../model/TaskCategory';
import TaskNote from '../model/TaskNote';
import TaskNotesList200Response from '../model/TaskNotesList200Response';
import TaskStatus from '../model/TaskStatus';
import TaskStatusesList200Response from '../model/TaskStatusesList200Response';
import TaskTemplate from '../model/TaskTemplate';
import TaskTemplatesList200Response from '../model/TaskTemplatesList200Response';
import TasksList200Response from '../model/TasksList200Response';

/**
* PracticeManagement service.
* @module api/PracticeManagementApi
* @version v4 (Hunt Valley)
*/
export default class PracticeManagementApi {

    /**
    * Constructs a new PracticeManagementApi. 
    * @alias module:api/PracticeManagementApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the inventoryCategoriesList operation.
     * @callback module:api/PracticeManagementApi~inventoryCategoriesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InventoryCategoriesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search inventory categories
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~inventoryCategoriesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InventoryCategoriesList200Response}
     */
    inventoryCategoriesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = InventoryCategoriesList200Response;
      return this.apiClient.callApi(
        '/api/inventory_categories', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the inventoryCategoriesRead operation.
     * @callback module:api/PracticeManagementApi~inventoryCategoriesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InventoryCategory} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing inventory category
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~inventoryCategoriesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InventoryCategory}
     */
    inventoryCategoriesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling inventoryCategoriesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = InventoryCategory;
      return this.apiClient.callApi(
        '/api/inventory_categories/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the inventoryVaccinesCreate operation.
     * @callback module:api/PracticeManagementApi~inventoryVaccinesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InventoryVaccine} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create vaccine inventory
     * @param {Object} opts Optional parameters
     * @param {String} [status] 
     * @param {String} [cvxCode] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~inventoryVaccinesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InventoryVaccine}
     */
    inventoryVaccinesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'status': opts['status'],
        'cvx_code': opts['cvxCode'],
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
      let returnType = InventoryVaccine;
      return this.apiClient.callApi(
        '/api/inventory_vaccines', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the inventoryVaccinesList operation.
     * @callback module:api/PracticeManagementApi~inventoryVaccinesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InventoryVaccinesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search vaccine inventories
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [status] 
     * @param {String} [cvxCode] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~inventoryVaccinesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InventoryVaccinesList200Response}
     */
    inventoryVaccinesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'status': opts['status'],
        'cvx_code': opts['cvxCode'],
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
      let returnType = InventoryVaccinesList200Response;
      return this.apiClient.callApi(
        '/api/inventory_vaccines', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the inventoryVaccinesRead operation.
     * @callback module:api/PracticeManagementApi~inventoryVaccinesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InventoryVaccine} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing vaccine inventory
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [status] 
     * @param {String} [cvxCode] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~inventoryVaccinesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InventoryVaccine}
     */
    inventoryVaccinesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling inventoryVaccinesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'cvx_code': opts['cvxCode'],
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
      let returnType = InventoryVaccine;
      return this.apiClient.callApi(
        '/api/inventory_vaccines/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the messagesCreate operation.
     * @callback module:api/PracticeManagementApi~messagesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DoctorMessage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create messages in doctor's message center
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {Number} [responsibleUser] 
     * @param {String} [updatedSince] 
     * @param {String} [receivedSince] 
     * @param {Number} [owner] 
     * @param {String} [type] 
     * @param {module:api/PracticeManagementApi~messagesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DoctorMessage}
     */
    messagesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'responsible_user': opts['responsibleUser'],
        'updated_since': opts['updatedSince'],
        'received_since': opts['receivedSince'],
        'owner': opts['owner'],
        'type': opts['type']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DoctorMessage;
      return this.apiClient.callApi(
        '/api/messages', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the messagesDelete operation.
     * @callback module:api/PracticeManagementApi~messagesDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing message in doctor's message center
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {Number} [responsibleUser] 
     * @param {String} [updatedSince] 
     * @param {String} [receivedSince] 
     * @param {Number} [owner] 
     * @param {String} [type] 
     * @param {module:api/PracticeManagementApi~messagesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    messagesDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling messagesDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'responsible_user': opts['responsibleUser'],
        'updated_since': opts['updatedSince'],
        'received_since': opts['receivedSince'],
        'owner': opts['owner'],
        'type': opts['type']
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
        '/api/messages/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the messagesList operation.
     * @callback module:api/PracticeManagementApi~messagesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MessagesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search messages in doctor's message center
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {Number} [responsibleUser] 
     * @param {String} [updatedSince] 
     * @param {String} [receivedSince] 
     * @param {Number} [owner] 
     * @param {String} [type] 
     * @param {module:api/PracticeManagementApi~messagesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MessagesList200Response}
     */
    messagesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'responsible_user': opts['responsibleUser'],
        'updated_since': opts['updatedSince'],
        'received_since': opts['receivedSince'],
        'owner': opts['owner'],
        'type': opts['type']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = MessagesList200Response;
      return this.apiClient.callApi(
        '/api/messages', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the messagesPartialUpdate operation.
     * @callback module:api/PracticeManagementApi~messagesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing message in doctor's message center
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {Number} [responsibleUser] 
     * @param {String} [updatedSince] 
     * @param {String} [receivedSince] 
     * @param {Number} [owner] 
     * @param {String} [type] 
     * @param {module:api/PracticeManagementApi~messagesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    messagesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling messagesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'responsible_user': opts['responsibleUser'],
        'updated_since': opts['updatedSince'],
        'received_since': opts['receivedSince'],
        'owner': opts['owner'],
        'type': opts['type']
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
        '/api/messages/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the messagesRead operation.
     * @callback module:api/PracticeManagementApi~messagesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DoctorMessage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing message in doctor's message center
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {Number} [responsibleUser] 
     * @param {String} [updatedSince] 
     * @param {String} [receivedSince] 
     * @param {Number} [owner] 
     * @param {String} [type] 
     * @param {module:api/PracticeManagementApi~messagesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DoctorMessage}
     */
    messagesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling messagesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'responsible_user': opts['responsibleUser'],
        'updated_since': opts['updatedSince'],
        'received_since': opts['receivedSince'],
        'owner': opts['owner'],
        'type': opts['type']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DoctorMessage;
      return this.apiClient.callApi(
        '/api/messages/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the messagesUpdate operation.
     * @callback module:api/PracticeManagementApi~messagesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing message in doctor's message center
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {Number} [responsibleUser] 
     * @param {String} [updatedSince] 
     * @param {String} [receivedSince] 
     * @param {Number} [owner] 
     * @param {String} [type] 
     * @param {module:api/PracticeManagementApi~messagesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    messagesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling messagesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'patient': opts['patient'],
        'doctor': opts['doctor'],
        'responsible_user': opts['responsibleUser'],
        'updated_since': opts['updatedSince'],
        'received_since': opts['receivedSince'],
        'owner': opts['owner'],
        'type': opts['type']
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
        '/api/messages/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the officesAddExamRoom operation.
     * @callback module:api/PracticeManagementApi~officesAddExamRoomCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Office} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add an exam room to the office
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~officesAddExamRoomCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Office}
     */
    officesAddExamRoom(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling officesAddExamRoom");
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
      let returnType = Office;
      return this.apiClient.callApi(
        '/api/offices/{id}/add_exam_room', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the officesList operation.
     * @callback module:api/PracticeManagementApi~officesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/OfficesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search offices
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~officesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/OfficesList200Response}
     */
    officesList(opts, callback) {
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
      let returnType = OfficesList200Response;
      return this.apiClient.callApi(
        '/api/offices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the officesPartialUpdate operation.
     * @callback module:api/PracticeManagementApi~officesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing office
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~officesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    officesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling officesPartialUpdate");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/offices/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the officesRead operation.
     * @callback module:api/PracticeManagementApi~officesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Office} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing office
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~officesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Office}
     */
    officesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling officesRead");
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
      let returnType = Office;
      return this.apiClient.callApi(
        '/api/offices/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the officesUpdate operation.
     * @callback module:api/PracticeManagementApi~officesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing office
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/PracticeManagementApi~officesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    officesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling officesUpdate");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/offices/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskCategoriesCreate operation.
     * @callback module:api/PracticeManagementApi~taskCategoriesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskCategory} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a task category
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskCategoriesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskCategory}
     */
    taskCategoriesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskCategory;
      return this.apiClient.callApi(
        '/api/task_categories', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskCategoriesList operation.
     * @callback module:api/PracticeManagementApi~taskCategoriesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskCategoriesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search task categories
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskCategoriesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskCategoriesList200Response}
     */
    taskCategoriesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskCategoriesList200Response;
      return this.apiClient.callApi(
        '/api/task_categories', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskCategoriesPartialUpdate operation.
     * @callback module:api/PracticeManagementApi~taskCategoriesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task category
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskCategoriesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskCategoriesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskCategoriesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since']
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
        '/api/task_categories/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskCategoriesRead operation.
     * @callback module:api/PracticeManagementApi~taskCategoriesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskCategory} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing task category
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskCategoriesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskCategory}
     */
    taskCategoriesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskCategoriesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskCategory;
      return this.apiClient.callApi(
        '/api/task_categories/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskCategoriesUpdate operation.
     * @callback module:api/PracticeManagementApi~taskCategoriesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task category
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskCategoriesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskCategoriesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskCategoriesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since']
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
        '/api/task_categories/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskNotesCreate operation.
     * @callback module:api/PracticeManagementApi~taskNotesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskNote} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a task note
     * @param {Object} opts Optional parameters
     * @param {Number} [task] 
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskNotesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskNote}
     */
    taskNotesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'task': opts['task'],
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskNote;
      return this.apiClient.callApi(
        '/api/task_notes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskNotesList operation.
     * @callback module:api/PracticeManagementApi~taskNotesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskNotesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search task notes
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [task] 
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskNotesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskNotesList200Response}
     */
    taskNotesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'task': opts['task'],
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskNotesList200Response;
      return this.apiClient.callApi(
        '/api/task_notes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskNotesPartialUpdate operation.
     * @callback module:api/PracticeManagementApi~taskNotesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task note
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [task] 
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskNotesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskNotesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskNotesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'task': opts['task'],
        'since': opts['since']
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
        '/api/task_notes/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskNotesRead operation.
     * @callback module:api/PracticeManagementApi~taskNotesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskNote} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing task note
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [task] 
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskNotesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskNote}
     */
    taskNotesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskNotesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'task': opts['task'],
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskNote;
      return this.apiClient.callApi(
        '/api/task_notes/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskNotesUpdate operation.
     * @callback module:api/PracticeManagementApi~taskNotesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task note
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [task] 
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskNotesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskNotesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskNotesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'task': opts['task'],
        'since': opts['since']
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
        '/api/task_notes/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskStatusesCreate operation.
     * @callback module:api/PracticeManagementApi~taskStatusesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskStatus} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a task status
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskStatusesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskStatus}
     */
    taskStatusesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskStatus;
      return this.apiClient.callApi(
        '/api/task_statuses', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskStatusesList operation.
     * @callback module:api/PracticeManagementApi~taskStatusesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskStatusesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search task statuses
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskStatusesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskStatusesList200Response}
     */
    taskStatusesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskStatusesList200Response;
      return this.apiClient.callApi(
        '/api/task_statuses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskStatusesPartialUpdate operation.
     * @callback module:api/PracticeManagementApi~taskStatusesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task status
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskStatusesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskStatusesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskStatusesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since']
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
        '/api/task_statuses/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskStatusesRead operation.
     * @callback module:api/PracticeManagementApi~taskStatusesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskStatus} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing task status
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskStatusesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskStatus}
     */
    taskStatusesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskStatusesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskStatus;
      return this.apiClient.callApi(
        '/api/task_statuses/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskStatusesUpdate operation.
     * @callback module:api/PracticeManagementApi~taskStatusesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task status
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {module:api/PracticeManagementApi~taskStatusesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskStatusesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskStatusesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'since': opts['since']
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
        '/api/task_statuses/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskTemplatesCreate operation.
     * @callback module:api/PracticeManagementApi~taskTemplatesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskTemplate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a task template
     * @param {Object} opts Optional parameters
     * @param {Number} [assigneeUser] 
     * @param {Number} [status] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [since] 
     * @param {Number} [category] 
     * @param {module:api/PracticeManagementApi~taskTemplatesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskTemplate}
     */
    taskTemplatesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'assignee_user': opts['assigneeUser'],
        'status': opts['status'],
        'assignee_group': opts['assigneeGroup'],
        'since': opts['since'],
        'category': opts['category']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskTemplate;
      return this.apiClient.callApi(
        '/api/task_templates', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskTemplatesList operation.
     * @callback module:api/PracticeManagementApi~taskTemplatesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskTemplatesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search task templates
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [assigneeUser] 
     * @param {Number} [status] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [since] 
     * @param {Number} [category] 
     * @param {module:api/PracticeManagementApi~taskTemplatesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskTemplatesList200Response}
     */
    taskTemplatesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'assignee_user': opts['assigneeUser'],
        'status': opts['status'],
        'assignee_group': opts['assigneeGroup'],
        'since': opts['since'],
        'category': opts['category']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskTemplatesList200Response;
      return this.apiClient.callApi(
        '/api/task_templates', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskTemplatesPartialUpdate operation.
     * @callback module:api/PracticeManagementApi~taskTemplatesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [assigneeUser] 
     * @param {Number} [status] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [since] 
     * @param {Number} [category] 
     * @param {module:api/PracticeManagementApi~taskTemplatesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskTemplatesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskTemplatesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'assignee_user': opts['assigneeUser'],
        'status': opts['status'],
        'assignee_group': opts['assigneeGroup'],
        'since': opts['since'],
        'category': opts['category']
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
        '/api/task_templates/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskTemplatesRead operation.
     * @callback module:api/PracticeManagementApi~taskTemplatesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TaskTemplate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing task template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [assigneeUser] 
     * @param {Number} [status] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [since] 
     * @param {Number} [category] 
     * @param {module:api/PracticeManagementApi~taskTemplatesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TaskTemplate}
     */
    taskTemplatesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskTemplatesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'assignee_user': opts['assigneeUser'],
        'status': opts['status'],
        'assignee_group': opts['assigneeGroup'],
        'since': opts['since'],
        'category': opts['category']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TaskTemplate;
      return this.apiClient.callApi(
        '/api/task_templates/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the taskTemplatesUpdate operation.
     * @callback module:api/PracticeManagementApi~taskTemplatesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [assigneeUser] 
     * @param {Number} [status] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [since] 
     * @param {Number} [category] 
     * @param {module:api/PracticeManagementApi~taskTemplatesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    taskTemplatesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling taskTemplatesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'assignee_user': opts['assigneeUser'],
        'status': opts['status'],
        'assignee_group': opts['assigneeGroup'],
        'since': opts['since'],
        'category': opts['category']
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
        '/api/task_templates/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tasksCreate operation.
     * @callback module:api/PracticeManagementApi~tasksCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Task} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a task
     * @param {Object} opts Optional parameters
     * @param {Number} [status] 
     * @param {Number} [category] 
     * @param {String} [dueAtDate] 
     * @param {String} [dueAtUnknown] 
     * @param {String} [since] 
     * @param {String} [dueAtSince] 
     * @param {Number} [assigneeUser] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [dueAtRange] 
     * @param {module:api/PracticeManagementApi~tasksCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Task}
     */
    tasksCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'status': opts['status'],
        'category': opts['category'],
        'due_at_date': opts['dueAtDate'],
        'due_at_unknown': opts['dueAtUnknown'],
        'since': opts['since'],
        'due_at_since': opts['dueAtSince'],
        'assignee_user': opts['assigneeUser'],
        'assignee_group': opts['assigneeGroup'],
        'due_at_range': opts['dueAtRange']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Task;
      return this.apiClient.callApi(
        '/api/tasks', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tasksList operation.
     * @callback module:api/PracticeManagementApi~tasksListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TasksList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search tasks
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [status] 
     * @param {Number} [category] 
     * @param {String} [dueAtDate] 
     * @param {String} [dueAtUnknown] 
     * @param {String} [since] 
     * @param {String} [dueAtSince] 
     * @param {Number} [assigneeUser] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [dueAtRange] 
     * @param {module:api/PracticeManagementApi~tasksListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TasksList200Response}
     */
    tasksList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'status': opts['status'],
        'category': opts['category'],
        'due_at_date': opts['dueAtDate'],
        'due_at_unknown': opts['dueAtUnknown'],
        'since': opts['since'],
        'due_at_since': opts['dueAtSince'],
        'assignee_user': opts['assigneeUser'],
        'assignee_group': opts['assigneeGroup'],
        'due_at_range': opts['dueAtRange']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = TasksList200Response;
      return this.apiClient.callApi(
        '/api/tasks', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tasksPartialUpdate operation.
     * @callback module:api/PracticeManagementApi~tasksPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [status] 
     * @param {Number} [category] 
     * @param {String} [dueAtDate] 
     * @param {String} [dueAtUnknown] 
     * @param {String} [since] 
     * @param {String} [dueAtSince] 
     * @param {Number} [assigneeUser] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [dueAtRange] 
     * @param {module:api/PracticeManagementApi~tasksPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    tasksPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling tasksPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'category': opts['category'],
        'due_at_date': opts['dueAtDate'],
        'due_at_unknown': opts['dueAtUnknown'],
        'since': opts['since'],
        'due_at_since': opts['dueAtSince'],
        'assignee_user': opts['assigneeUser'],
        'assignee_group': opts['assigneeGroup'],
        'due_at_range': opts['dueAtRange']
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
        '/api/tasks/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tasksRead operation.
     * @callback module:api/PracticeManagementApi~tasksReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Task} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing task
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [status] 
     * @param {Number} [category] 
     * @param {String} [dueAtDate] 
     * @param {String} [dueAtUnknown] 
     * @param {String} [since] 
     * @param {String} [dueAtSince] 
     * @param {Number} [assigneeUser] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [dueAtRange] 
     * @param {module:api/PracticeManagementApi~tasksReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Task}
     */
    tasksRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling tasksRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'category': opts['category'],
        'due_at_date': opts['dueAtDate'],
        'due_at_unknown': opts['dueAtUnknown'],
        'since': opts['since'],
        'due_at_since': opts['dueAtSince'],
        'assignee_user': opts['assigneeUser'],
        'assignee_group': opts['assigneeGroup'],
        'due_at_range': opts['dueAtRange']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Task;
      return this.apiClient.callApi(
        '/api/tasks/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the tasksUpdate operation.
     * @callback module:api/PracticeManagementApi~tasksUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing task
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [status] 
     * @param {Number} [category] 
     * @param {String} [dueAtDate] 
     * @param {String} [dueAtUnknown] 
     * @param {String} [since] 
     * @param {String} [dueAtSince] 
     * @param {Number} [assigneeUser] 
     * @param {Number} [assigneeGroup] 
     * @param {String} [dueAtRange] 
     * @param {module:api/PracticeManagementApi~tasksUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    tasksUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling tasksUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'category': opts['category'],
        'due_at_date': opts['dueAtDate'],
        'due_at_unknown': opts['dueAtUnknown'],
        'since': opts['since'],
        'due_at_since': opts['dueAtSince'],
        'assignee_user': opts['assigneeUser'],
        'assignee_group': opts['assigneeGroup'],
        'due_at_range': opts['dueAtRange']
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
        '/api/tasks/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
