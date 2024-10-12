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
import AllergiesList200Response from '../model/AllergiesList200Response';
import AmendmentsList200Response from '../model/AmendmentsList200Response';
import Appointment from '../model/Appointment';
import AppointmentProfile from '../model/AppointmentProfile';
import AppointmentProfilesList200Response from '../model/AppointmentProfilesList200Response';
import AppointmentTemplate from '../model/AppointmentTemplate';
import AppointmentTemplatesList200Response from '../model/AppointmentTemplatesList200Response';
import AppointmentsList200Response from '../model/AppointmentsList200Response';
import CarePlan from '../model/CarePlan';
import CarePlansList200Response from '../model/CarePlansList200Response';
import CareTeamMember from '../model/CareTeamMember';
import CareTeamMembersList200Response from '../model/CareTeamMembersList200Response';
import ClaimBillingNotes from '../model/ClaimBillingNotes';
import ClaimBillingNotesList200Response from '../model/ClaimBillingNotesList200Response';
import ClinicalNote from '../model/ClinicalNote';
import ClinicalNoteFieldTypesList200Response from '../model/ClinicalNoteFieldTypesList200Response';
import ClinicalNoteFieldValuesList200Response from '../model/ClinicalNoteFieldValuesList200Response';
import ClinicalNoteTemplatesList200Response from '../model/ClinicalNoteTemplatesList200Response';
import ClinicalNotesList200Response from '../model/ClinicalNotesList200Response';
import ConsentForm from '../model/ConsentForm';
import ConsentFormsList200Response from '../model/ConsentFormsList200Response';
import CustomAppointmentFieldType from '../model/CustomAppointmentFieldType';
import CustomAppointmentFieldsList200Response from '../model/CustomAppointmentFieldsList200Response';
import CustomDemographicsList200Response from '../model/CustomDemographicsList200Response';
import CustomPatientFieldType from '../model/CustomPatientFieldType';
import CustomVitalType from '../model/CustomVitalType';
import CustomVitalsList200Response from '../model/CustomVitalsList200Response';
import DoctorFeeSchedule from '../model/DoctorFeeSchedule';
import DocumentsList200Response from '../model/DocumentsList200Response';
import EOBObject from '../model/EOBObject';
import EobsList200Response from '../model/EobsList200Response';
import FeeSchedulesList200Response from '../model/FeeSchedulesList200Response';
import ImplantableDevice from '../model/ImplantableDevice';
import ImplantableDevicesList200Response from '../model/ImplantableDevicesList200Response';
import Insurance from '../model/Insurance';
import InsurancesList200Response from '../model/InsurancesList200Response';
import LabDocumentsList200Response from '../model/LabDocumentsList200Response';
import LabOrder from '../model/LabOrder';
import LabOrderDocument from '../model/LabOrderDocument';
import LabOrdersList200Response from '../model/LabOrdersList200Response';
import LabResult from '../model/LabResult';
import LabResultsList200Response from '../model/LabResultsList200Response';
import LabTest from '../model/LabTest';
import LabTestsList200Response from '../model/LabTestsList200Response';
import LabVendorLocation from '../model/LabVendorLocation';
import MedicationsList200Response from '../model/MedicationsList200Response';
import Patient from '../model/Patient';
import PatientAllergy from '../model/PatientAllergy';
import PatientAmendment from '../model/PatientAmendment';
import PatientCommunication from '../model/PatientCommunication';
import PatientCommunicationsList200Response from '../model/PatientCommunicationsList200Response';
import PatientDrug from '../model/PatientDrug';
import PatientFlagType from '../model/PatientFlagType';
import PatientFlagTypesList200Response from '../model/PatientFlagTypesList200Response';
import PatientIntervention from '../model/PatientIntervention';
import PatientInterventionsList200Response from '../model/PatientInterventionsList200Response';
import PatientLabResultSet from '../model/PatientLabResultSet';
import PatientLabResultsList200Response from '../model/PatientLabResultsList200Response';
import PatientMessage from '../model/PatientMessage';
import PatientMessagesList200Response from '../model/PatientMessagesList200Response';
import PatientPhysicalExam from '../model/PatientPhysicalExam';
import PatientPhysicalExamsList200Response from '../model/PatientPhysicalExamsList200Response';
import PatientProblem from '../model/PatientProblem';
import PatientRiskAssessment from '../model/PatientRiskAssessment';
import PatientRiskAssessmentsList200Response from '../model/PatientRiskAssessmentsList200Response';
import PatientVaccineRecord from '../model/PatientVaccineRecord';
import PatientVaccineRecordsList200Response from '../model/PatientVaccineRecordsList200Response';
import PatientsList200Response from '../model/PatientsList200Response';
import PrescriptionMessage from '../model/PrescriptionMessage';
import PrescriptionMessagesList200Response from '../model/PrescriptionMessagesList200Response';
import ProblemsList200Response from '../model/ProblemsList200Response';
import ReminderProfile from '../model/ReminderProfile';
import ReminderProfilesList200Response from '../model/ReminderProfilesList200Response';
import ScannedClinicalDocument from '../model/ScannedClinicalDocument';
import SoapNoteCustomReport from '../model/SoapNoteCustomReport';
import SoapNoteLineItemFieldType from '../model/SoapNoteLineItemFieldType';
import SoapNoteLineItemFieldValue from '../model/SoapNoteLineItemFieldValue';
import SublabsList200Response from '../model/SublabsList200Response';

/**
* Clinical service.
* @module api/ClinicalApi
* @version v4 (Hunt Valley)
*/
export default class ClinicalApi {

    /**
    * Constructs a new ClinicalApi. 
    * @alias module:api/ClinicalApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the allergiesCreate operation.
     * @callback module:api/ClinicalApi~allergiesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientAllergy} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient allergy
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~allergiesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientAllergy}
     */
    allergiesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = PatientAllergy;
      return this.apiClient.callApi(
        '/api/allergies', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the allergiesList operation.
     * @callback module:api/ClinicalApi~allergiesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AllergiesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient allergies
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~allergiesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AllergiesList200Response}
     */
    allergiesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = AllergiesList200Response;
      return this.apiClient.callApi(
        '/api/allergies', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the allergiesPartialUpdate operation.
     * @callback module:api/ClinicalApi~allergiesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient allergy
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~allergiesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    allergiesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling allergiesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/allergies/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the allergiesRead operation.
     * @callback module:api/ClinicalApi~allergiesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientAllergy} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient allergy
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~allergiesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientAllergy}
     */
    allergiesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling allergiesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = PatientAllergy;
      return this.apiClient.callApi(
        '/api/allergies/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the allergiesUpdate operation.
     * @callback module:api/ClinicalApi~allergiesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient allergy
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~allergiesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    allergiesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling allergiesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/allergies/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the amendmentsCreate operation.
     * @callback module:api/ClinicalApi~amendmentsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientAmendment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient amendments to a patient's clinical records
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~amendmentsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientAmendment}
     */
    amendmentsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'appointment': opts['appointment'],
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
      let returnType = PatientAmendment;
      return this.apiClient.callApi(
        '/api/amendments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the amendmentsDelete operation.
     * @callback module:api/ClinicalApi~amendmentsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing patient amendment, you can only interact with amendments created by your API application
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~amendmentsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    amendmentsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling amendmentsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'appointment': opts['appointment'],
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
        '/api/amendments/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the amendmentsList operation.
     * @callback module:api/ClinicalApi~amendmentsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AmendmentsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient amendments. You can only interact with amendments created by your API application
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [appointment] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~amendmentsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AmendmentsList200Response}
     */
    amendmentsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'appointment': opts['appointment'],
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
      let returnType = AmendmentsList200Response;
      return this.apiClient.callApi(
        '/api/amendments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the amendmentsPartialUpdate operation.
     * @callback module:api/ClinicalApi~amendmentsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient amendment, you can only interact with amendments created by your API application
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~amendmentsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    amendmentsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling amendmentsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'appointment': opts['appointment'],
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
        '/api/amendments/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the amendmentsRead operation.
     * @callback module:api/ClinicalApi~amendmentsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientAmendment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient amendment, you can only interact with amendments created by your API application
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~amendmentsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientAmendment}
     */
    amendmentsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling amendmentsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'appointment': opts['appointment'],
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
      let returnType = PatientAmendment;
      return this.apiClient.callApi(
        '/api/amendments/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the amendmentsUpdate operation.
     * @callback module:api/ClinicalApi~amendmentsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient amendment, you can only interact with amendments created by your API application
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~amendmentsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    amendmentsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling amendmentsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'appointment': opts['appointment'],
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
        '/api/amendments/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentProfilesCreate operation.
     * @callback module:api/ClinicalApi~appointmentProfilesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AppointmentProfile} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create appointment profiles for a doctor's calendar
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentProfilesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AppointmentProfile}
     */
    appointmentProfilesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = AppointmentProfile;
      return this.apiClient.callApi(
        '/api/appointment_profiles', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentProfilesDelete operation.
     * @callback module:api/ClinicalApi~appointmentProfilesDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing appointment profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentProfilesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentProfilesDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentProfilesDelete");
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
        '/api/appointment_profiles/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentProfilesList operation.
     * @callback module:api/ClinicalApi~appointmentProfilesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AppointmentProfilesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search appointment profiles for a doctor's calendar
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentProfilesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AppointmentProfilesList200Response}
     */
    appointmentProfilesList(opts, callback) {
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
      let returnType = AppointmentProfilesList200Response;
      return this.apiClient.callApi(
        '/api/appointment_profiles', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentProfilesPartialUpdate operation.
     * @callback module:api/ClinicalApi~appointmentProfilesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentProfilesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentProfilesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentProfilesPartialUpdate");
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
        '/api/appointment_profiles/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentProfilesRead operation.
     * @callback module:api/ClinicalApi~appointmentProfilesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AppointmentProfile} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing appointment profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentProfilesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AppointmentProfile}
     */
    appointmentProfilesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentProfilesRead");
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
      let returnType = AppointmentProfile;
      return this.apiClient.callApi(
        '/api/appointment_profiles/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentProfilesUpdate operation.
     * @callback module:api/ClinicalApi~appointmentProfilesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentProfilesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentProfilesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentProfilesUpdate");
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
        '/api/appointment_profiles/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentTemplatesCreate operation.
     * @callback module:api/ClinicalApi~appointmentTemplatesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AppointmentTemplate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create appointment templates for a doctor's calendar
     * @param {Object} opts Optional parameters
     * @param {Number} [profile] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentTemplatesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AppointmentTemplate}
     */
    appointmentTemplatesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'profile': opts['profile'],
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
      let returnType = AppointmentTemplate;
      return this.apiClient.callApi(
        '/api/appointment_templates', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentTemplatesDelete operation.
     * @callback module:api/ClinicalApi~appointmentTemplatesDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [profile] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentTemplatesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentTemplatesDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentTemplatesDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'profile': opts['profile'],
        'office': opts['office'],
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
        '/api/appointment_templates/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentTemplatesList operation.
     * @callback module:api/ClinicalApi~appointmentTemplatesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AppointmentTemplatesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search appointment templates for a doctor's calendar
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [profile] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentTemplatesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AppointmentTemplatesList200Response}
     */
    appointmentTemplatesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'profile': opts['profile'],
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
      let returnType = AppointmentTemplatesList200Response;
      return this.apiClient.callApi(
        '/api/appointment_templates', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentTemplatesPartialUpdate operation.
     * @callback module:api/ClinicalApi~appointmentTemplatesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [profile] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentTemplatesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentTemplatesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentTemplatesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'profile': opts['profile'],
        'office': opts['office'],
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
        '/api/appointment_templates/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentTemplatesRead operation.
     * @callback module:api/ClinicalApi~appointmentTemplatesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AppointmentTemplate} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [profile] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentTemplatesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AppointmentTemplate}
     */
    appointmentTemplatesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentTemplatesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'profile': opts['profile'],
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
      let returnType = AppointmentTemplate;
      return this.apiClient.callApi(
        '/api/appointment_templates/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentTemplatesUpdate operation.
     * @callback module:api/ClinicalApi~appointmentTemplatesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [profile] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~appointmentTemplatesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentTemplatesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentTemplatesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'profile': opts['profile'],
        'office': opts['office'],
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
        '/api/appointment_templates/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentsCreate operation.
     * @callback module:api/ClinicalApi~appointmentsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Appointment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new appointment or break on doctor's calendar
     * @param {Object} opts Optional parameters
     * @param {String} [status] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~appointmentsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Appointment}
     */
    appointmentsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'status': opts['status'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Appointment;
      return this.apiClient.callApi(
        '/api/appointments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentsDelete operation.
     * @callback module:api/ClinicalApi~appointmentsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing appointment or break
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [status] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~appointmentsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
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
        '/api/appointments/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentsList operation.
     * @callback module:api/ClinicalApi~appointmentsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AppointmentsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search appointment or breaks. <b>Note:</b> Either `since`, `date` or `date_range` parameter must be specified.             
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [status] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~appointmentsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AppointmentsList200Response}
     */
    appointmentsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'status': opts['status'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AppointmentsList200Response;
      return this.apiClient.callApi(
        '/api/appointments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentsPartialUpdate operation.
     * @callback module:api/ClinicalApi~appointmentsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment or break
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [status] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~appointmentsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
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
        '/api/appointments/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentsRead operation.
     * @callback module:api/ClinicalApi~appointmentsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Appointment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing appointment or break
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [status] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~appointmentsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Appointment}
     */
    appointmentsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Appointment;
      return this.apiClient.callApi(
        '/api/appointments/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the appointmentsUpdate operation.
     * @callback module:api/ClinicalApi~appointmentsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment or break
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [status] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~appointmentsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    appointmentsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling appointmentsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'status': opts['status'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
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
        '/api/appointments/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the carePlansList operation.
     * @callback module:api/ClinicalApi~carePlansListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CarePlansList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search care plans
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [planType] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~carePlansListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CarePlansList200Response}
     */
    carePlansList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'patient': opts['patient'],
        'plan_type': opts['planType'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CarePlansList200Response;
      return this.apiClient.callApi(
        '/api/care_plans', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the carePlansRead operation.
     * @callback module:api/ClinicalApi~carePlansReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CarePlan} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing care plan
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [planType] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~carePlansReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CarePlan}
     */
    carePlansRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling carePlansRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'patient': opts['patient'],
        'plan_type': opts['planType'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CarePlan;
      return this.apiClient.callApi(
        '/api/care_plans/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the careTeamMembersList operation.
     * @callback module:api/ClinicalApi~careTeamMembersListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CareTeamMembersList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [appointment] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~careTeamMembersListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CareTeamMembersList200Response}
     */
    careTeamMembersList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'patient': opts['patient'],
        'appointment': opts['appointment'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CareTeamMembersList200Response;
      return this.apiClient.callApi(
        '/api/care_team_members', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the careTeamMembersRead operation.
     * @callback module:api/ClinicalApi~careTeamMembersReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CareTeamMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [appointment] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~careTeamMembersReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CareTeamMember}
     */
    careTeamMembersRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling careTeamMembersRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'patient': opts['patient'],
        'appointment': opts['appointment'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CareTeamMember;
      return this.apiClient.callApi(
        '/api/care_team_members/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the claimBillingNotesCreate operation.
     * @callback module:api/ClinicalApi~claimBillingNotesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClaimBillingNotes} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new billing note
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~claimBillingNotesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClaimBillingNotes}
     */
    claimBillingNotesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'appointment': opts['appointment'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClaimBillingNotes;
      return this.apiClient.callApi(
        '/api/claim_billing_notes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the claimBillingNotesList operation.
     * @callback module:api/ClinicalApi~claimBillingNotesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClaimBillingNotesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search billing notes
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [appointment] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~claimBillingNotesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClaimBillingNotesList200Response}
     */
    claimBillingNotesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'appointment': opts['appointment'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClaimBillingNotesList200Response;
      return this.apiClient.callApi(
        '/api/claim_billing_notes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the claimBillingNotesRead operation.
     * @callback module:api/ClinicalApi~claimBillingNotesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClaimBillingNotes} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing billing note
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [appointment] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~claimBillingNotesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClaimBillingNotes}
     */
    claimBillingNotesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling claimBillingNotesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'appointment': opts['appointment'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClaimBillingNotes;
      return this.apiClient.callApi(
        '/api/claim_billing_notes/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteFieldTypesList operation.
     * @callback module:api/ClinicalApi~clinicalNoteFieldTypesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClinicalNoteFieldTypesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search clinical note field types
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [clinicalNoteTemplate] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteFieldTypesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClinicalNoteFieldTypesList200Response}
     */
    clinicalNoteFieldTypesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'clinical_note_template': opts['clinicalNoteTemplate'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClinicalNoteFieldTypesList200Response;
      return this.apiClient.callApi(
        '/api/clinical_note_field_types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteFieldTypesRead operation.
     * @callback module:api/ClinicalApi~clinicalNoteFieldTypesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SoapNoteLineItemFieldType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing clinial note field type
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [clinicalNoteTemplate] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteFieldTypesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SoapNoteLineItemFieldType}
     */
    clinicalNoteFieldTypesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling clinicalNoteFieldTypesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'clinical_note_template': opts['clinicalNoteTemplate'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SoapNoteLineItemFieldType;
      return this.apiClient.callApi(
        '/api/clinical_note_field_types/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteFieldValuesCreate operation.
     * @callback module:api/ClinicalApi~clinicalNoteFieldValuesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SoapNoteLineItemFieldValue} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create clinical note field value
     * @param {Object} opts Optional parameters
     * @param {Number} [clinicalNoteField] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {Number} [clinicalNoteTemplate] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteFieldValuesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SoapNoteLineItemFieldValue}
     */
    clinicalNoteFieldValuesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'clinical_note_field': opts['clinicalNoteField'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'clinical_note_template': opts['clinicalNoteTemplate'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SoapNoteLineItemFieldValue;
      return this.apiClient.callApi(
        '/api/clinical_note_field_values', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteFieldValuesList operation.
     * @callback module:api/ClinicalApi~clinicalNoteFieldValuesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClinicalNoteFieldValuesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search clinical note field values
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [clinicalNoteField] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {Number} [clinicalNoteTemplate] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteFieldValuesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClinicalNoteFieldValuesList200Response}
     */
    clinicalNoteFieldValuesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'clinical_note_field': opts['clinicalNoteField'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'clinical_note_template': opts['clinicalNoteTemplate'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClinicalNoteFieldValuesList200Response;
      return this.apiClient.callApi(
        '/api/clinical_note_field_values', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteFieldValuesPartialUpdate operation.
     * @callback module:api/ClinicalApi~clinicalNoteFieldValuesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing clinical note field value
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [clinicalNoteField] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {Number} [clinicalNoteTemplate] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteFieldValuesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    clinicalNoteFieldValuesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling clinicalNoteFieldValuesPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'clinical_note_field': opts['clinicalNoteField'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'clinical_note_template': opts['clinicalNoteTemplate'],
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
        '/api/clinical_note_field_values/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteFieldValuesRead operation.
     * @callback module:api/ClinicalApi~clinicalNoteFieldValuesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SoapNoteLineItemFieldValue} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing clinical note field value
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [clinicalNoteField] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {Number} [clinicalNoteTemplate] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteFieldValuesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SoapNoteLineItemFieldValue}
     */
    clinicalNoteFieldValuesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling clinicalNoteFieldValuesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'clinical_note_field': opts['clinicalNoteField'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'clinical_note_template': opts['clinicalNoteTemplate'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SoapNoteLineItemFieldValue;
      return this.apiClient.callApi(
        '/api/clinical_note_field_values/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteFieldValuesUpdate operation.
     * @callback module:api/ClinicalApi~clinicalNoteFieldValuesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing clinical note field value
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [clinicalNoteField] 
     * @param {String} [since] 
     * @param {Number} [appointment] 
     * @param {Number} [clinicalNoteTemplate] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteFieldValuesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    clinicalNoteFieldValuesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling clinicalNoteFieldValuesUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'clinical_note_field': opts['clinicalNoteField'],
        'since': opts['since'],
        'appointment': opts['appointment'],
        'clinical_note_template': opts['clinicalNoteTemplate'],
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
        '/api/clinical_note_field_values/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteTemplatesList operation.
     * @callback module:api/ClinicalApi~clinicalNoteTemplatesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClinicalNoteTemplatesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search clinical note templates
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteTemplatesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClinicalNoteTemplatesList200Response}
     */
    clinicalNoteTemplatesList(opts, callback) {
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
      let returnType = ClinicalNoteTemplatesList200Response;
      return this.apiClient.callApi(
        '/api/clinical_note_templates', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNoteTemplatesRead operation.
     * @callback module:api/ClinicalApi~clinicalNoteTemplatesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SoapNoteCustomReport} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing clinical note tempalte
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~clinicalNoteTemplatesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SoapNoteCustomReport}
     */
    clinicalNoteTemplatesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling clinicalNoteTemplatesRead");
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
      let returnType = SoapNoteCustomReport;
      return this.apiClient.callApi(
        '/api/clinical_note_templates/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNotesList operation.
     * @callback module:api/ClinicalApi~clinicalNotesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClinicalNotesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~clinicalNotesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClinicalNotesList200Response}
     */
    clinicalNotesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClinicalNotesList200Response;
      return this.apiClient.callApi(
        '/api/clinical_notes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the clinicalNotesRead operation.
     * @callback module:api/ClinicalApi~clinicalNotesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ClinicalNote} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [office] 
     * @param {Number} [doctor] 
     * @param {String} [since] 
     * @param {String} [dateRange] 
     * @param {String} [date] 
     * @param {module:api/ClinicalApi~clinicalNotesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ClinicalNote}
     */
    clinicalNotesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling clinicalNotesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'patient': opts['patient'],
        'office': opts['office'],
        'doctor': opts['doctor'],
        'since': opts['since'],
        'date_range': opts['dateRange'],
        'date': opts['date']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ClinicalNote;
      return this.apiClient.callApi(
        '/api/clinical_notes/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consentFormsApplyToAppointment operation.
     * @callback module:api/ClinicalApi~consentFormsApplyToAppointmentCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Assign (apply) a consent form to appointment
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~consentFormsApplyToAppointmentCallback} callback The callback function, accepting three arguments: error, data, response
     */
    consentFormsApplyToAppointment(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consentFormsApplyToAppointment");
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
        '/api/consent_forms/{id}/apply_to_appointment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consentFormsCreate operation.
     * @callback module:api/ClinicalApi~consentFormsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConsentForm} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a patient consent form
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~consentFormsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConsentForm}
     */
    consentFormsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = ConsentForm;
      return this.apiClient.callApi(
        '/api/consent_forms', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consentFormsList operation.
     * @callback module:api/ClinicalApi~consentFormsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConsentFormsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient consent forms
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~consentFormsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConsentFormsList200Response}
     */
    consentFormsList(opts, callback) {
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
      let returnType = ConsentFormsList200Response;
      return this.apiClient.callApi(
        '/api/consent_forms', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consentFormsPartialUpdate operation.
     * @callback module:api/ClinicalApi~consentFormsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient consent form
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~consentFormsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    consentFormsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consentFormsPartialUpdate");
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
        '/api/consent_forms/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consentFormsRead operation.
     * @callback module:api/ClinicalApi~consentFormsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ConsentForm} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient consent form
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~consentFormsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ConsentForm}
     */
    consentFormsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consentFormsRead");
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
      let returnType = ConsentForm;
      return this.apiClient.callApi(
        '/api/consent_forms/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consentFormsUnapplyFromAppointment operation.
     * @callback module:api/ClinicalApi~consentFormsUnapplyFromAppointmentCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Unassign (unapply) a consent form from appointment
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~consentFormsUnapplyFromAppointmentCallback} callback The callback function, accepting three arguments: error, data, response
     */
    consentFormsUnapplyFromAppointment(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consentFormsUnapplyFromAppointment");
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
        '/api/consent_forms/{id}/unapply_from_appointment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the consentFormsUpdate operation.
     * @callback module:api/ClinicalApi~consentFormsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient consent form
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~consentFormsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    consentFormsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling consentFormsUpdate");
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
        '/api/consent_forms/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customAppointmentFieldsCreate operation.
     * @callback module:api/ClinicalApi~customAppointmentFieldsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomAppointmentFieldType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create custom appointment fields
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customAppointmentFieldsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomAppointmentFieldType}
     */
    customAppointmentFieldsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = CustomAppointmentFieldType;
      return this.apiClient.callApi(
        '/api/custom_appointment_fields', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customAppointmentFieldsList operation.
     * @callback module:api/ClinicalApi~customAppointmentFieldsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomAppointmentFieldsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search custom appointment fields
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customAppointmentFieldsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomAppointmentFieldsList200Response}
     */
    customAppointmentFieldsList(opts, callback) {
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
      let returnType = CustomAppointmentFieldsList200Response;
      return this.apiClient.callApi(
        '/api/custom_appointment_fields', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customAppointmentFieldsPartialUpdate operation.
     * @callback module:api/ClinicalApi~customAppointmentFieldsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing custom appointment field
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customAppointmentFieldsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    customAppointmentFieldsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customAppointmentFieldsPartialUpdate");
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
        '/api/custom_appointment_fields/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customAppointmentFieldsRead operation.
     * @callback module:api/ClinicalApi~customAppointmentFieldsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomAppointmentFieldType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing custom appointment field
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customAppointmentFieldsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomAppointmentFieldType}
     */
    customAppointmentFieldsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customAppointmentFieldsRead");
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
      let returnType = CustomAppointmentFieldType;
      return this.apiClient.callApi(
        '/api/custom_appointment_fields/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customAppointmentFieldsUpdate operation.
     * @callback module:api/ClinicalApi~customAppointmentFieldsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing custom appointment field
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customAppointmentFieldsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    customAppointmentFieldsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customAppointmentFieldsUpdate");
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
        '/api/custom_appointment_fields/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customDemographicsCreate operation.
     * @callback module:api/ClinicalApi~customDemographicsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomPatientFieldType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create custom demographics fields
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customDemographicsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomPatientFieldType}
     */
    customDemographicsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = CustomPatientFieldType;
      return this.apiClient.callApi(
        '/api/custom_demographics', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customDemographicsList operation.
     * @callback module:api/ClinicalApi~customDemographicsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomDemographicsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search custom demographics fields
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customDemographicsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomDemographicsList200Response}
     */
    customDemographicsList(opts, callback) {
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
      let returnType = CustomDemographicsList200Response;
      return this.apiClient.callApi(
        '/api/custom_demographics', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customDemographicsPartialUpdate operation.
     * @callback module:api/ClinicalApi~customDemographicsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing custom demographics field
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customDemographicsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    customDemographicsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customDemographicsPartialUpdate");
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
        '/api/custom_demographics/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customDemographicsRead operation.
     * @callback module:api/ClinicalApi~customDemographicsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomPatientFieldType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing custom demographics field
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customDemographicsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomPatientFieldType}
     */
    customDemographicsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customDemographicsRead");
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
      let returnType = CustomPatientFieldType;
      return this.apiClient.callApi(
        '/api/custom_demographics/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customDemographicsUpdate operation.
     * @callback module:api/ClinicalApi~customDemographicsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing custom demographics field
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customDemographicsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    customDemographicsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customDemographicsUpdate");
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
        '/api/custom_demographics/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customVitalsList operation.
     * @callback module:api/ClinicalApi~customVitalsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomVitalsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search custom vital types
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customVitalsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomVitalsList200Response}
     */
    customVitalsList(opts, callback) {
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
      let returnType = CustomVitalsList200Response;
      return this.apiClient.callApi(
        '/api/custom_vitals', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the customVitalsRead operation.
     * @callback module:api/ClinicalApi~customVitalsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CustomVitalType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing custom vital type
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~customVitalsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CustomVitalType}
     */
    customVitalsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling customVitalsRead");
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
      let returnType = CustomVitalType;
      return this.apiClient.callApi(
        '/api/custom_vitals/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the documentsCreate operation.
     * @callback module:api/ClinicalApi~documentsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScannedClinicalDocument} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create documents
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~documentsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScannedClinicalDocument}
     */
    documentsCreate(opts, callback) {
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
      let returnType = ScannedClinicalDocument;
      return this.apiClient.callApi(
        '/api/documents', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the documentsDelete operation.
     * @callback module:api/ClinicalApi~documentsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~documentsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    documentsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling documentsDelete");
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
        '/api/documents/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the documentsList operation.
     * @callback module:api/ClinicalApi~documentsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DocumentsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search documents
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~documentsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DocumentsList200Response}
     */
    documentsList(opts, callback) {
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
      let returnType = DocumentsList200Response;
      return this.apiClient.callApi(
        '/api/documents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the documentsPartialUpdate operation.
     * @callback module:api/ClinicalApi~documentsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~documentsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    documentsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling documentsPartialUpdate");
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
        '/api/documents/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the documentsRead operation.
     * @callback module:api/ClinicalApi~documentsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScannedClinicalDocument} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~documentsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScannedClinicalDocument}
     */
    documentsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling documentsRead");
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
      let returnType = ScannedClinicalDocument;
      return this.apiClient.callApi(
        '/api/documents/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the documentsUpdate operation.
     * @callback module:api/ClinicalApi~documentsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing appointment template
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~documentsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    documentsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling documentsUpdate");
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
        '/api/documents/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eobsCreate operation.
     * @callback module:api/ClinicalApi~eobsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EOBObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create EOB object
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~eobsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EOBObject}
     */
    eobsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = EOBObject;
      return this.apiClient.callApi(
        '/api/eobs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eobsList operation.
     * @callback module:api/ClinicalApi~eobsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EobsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search EOB objects
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~eobsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EobsList200Response}
     */
    eobsList(opts, callback) {
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
      let returnType = EobsList200Response;
      return this.apiClient.callApi(
        '/api/eobs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the eobsRead operation.
     * @callback module:api/ClinicalApi~eobsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EOBObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing EOB object
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~eobsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EOBObject}
     */
    eobsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling eobsRead");
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
      let returnType = EOBObject;
      return this.apiClient.callApi(
        '/api/eobs/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the feeSchedulesList operation.
     * @callback module:api/ClinicalApi~feeSchedulesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/FeeSchedulesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [code] 
     * @param {String} [codeType] 
     * @param {String} [since] 
     * @param {String} [payerId] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~feeSchedulesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/FeeSchedulesList200Response}
     */
    feeSchedulesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'code': opts['code'],
        'code_type': opts['codeType'],
        'since': opts['since'],
        'payer_id': opts['payerId'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = FeeSchedulesList200Response;
      return this.apiClient.callApi(
        '/api/fee_schedules', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the feeSchedulesRead operation.
     * @callback module:api/ClinicalApi~feeSchedulesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DoctorFeeSchedule} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [code] 
     * @param {String} [codeType] 
     * @param {String} [since] 
     * @param {String} [payerId] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~feeSchedulesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DoctorFeeSchedule}
     */
    feeSchedulesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling feeSchedulesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'code': opts['code'],
        'code_type': opts['codeType'],
        'since': opts['since'],
        'payer_id': opts['payerId'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = DoctorFeeSchedule;
      return this.apiClient.callApi(
        '/api/fee_schedules/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the implantableDevicesList operation.
     * @callback module:api/ClinicalApi~implantableDevicesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImplantableDevicesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search implantable devices
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [muDate] 
     * @param {Number} [patient] 
     * @param {String} [muDateRange] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~implantableDevicesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImplantableDevicesList200Response}
     */
    implantableDevicesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'mu_date': opts['muDate'],
        'patient': opts['patient'],
        'mu_date_range': opts['muDateRange'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ImplantableDevicesList200Response;
      return this.apiClient.callApi(
        '/api/implantable_devices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the implantableDevicesRead operation.
     * @callback module:api/ClinicalApi~implantableDevicesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ImplantableDevice} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing implantable device
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [muDate] 
     * @param {Number} [patient] 
     * @param {String} [muDateRange] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~implantableDevicesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ImplantableDevice}
     */
    implantableDevicesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling implantableDevicesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'mu_date': opts['muDate'],
        'patient': opts['patient'],
        'mu_date_range': opts['muDateRange'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ImplantableDevice;
      return this.apiClient.callApi(
        '/api/implantable_devices/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the insurancesList operation.
     * @callback module:api/ClinicalApi~insurancesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/InsurancesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} payerType One of `\"emdeon\"`, `\"gateway\"`, `\"ihcfa\"`
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [term] Search term, which can be either a partial name, partial ID or the state.
     * @param {module:api/ClinicalApi~insurancesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/InsurancesList200Response}
     */
    insurancesList(payerType, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'payerType' is set
      if (payerType === undefined || payerType === null) {
        throw new Error("Missing the required parameter 'payerType' when calling insurancesList");
      }

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'payer_type': payerType,
        'term': opts['term']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = InsurancesList200Response;
      return this.apiClient.callApi(
        '/api/insurances', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the insurancesRead operation.
     * @callback module:api/ClinicalApi~insurancesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Insurance} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {String} payerType One of `\"emdeon\"`, `\"gateway\"`, `\"ihcfa\"`
     * @param {Object} opts Optional parameters
     * @param {String} [term] Search term, which can be either a partial name, partial ID or the state.
     * @param {module:api/ClinicalApi~insurancesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Insurance}
     */
    insurancesRead(id, payerType, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling insurancesRead");
      }
      // verify the required parameter 'payerType' is set
      if (payerType === undefined || payerType === null) {
        throw new Error("Missing the required parameter 'payerType' when calling insurancesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'payer_type': payerType,
        'term': opts['term']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Insurance;
      return this.apiClient.callApi(
        '/api/insurances/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labDocumentsCreate operation.
     * @callback module:api/ClinicalApi~labDocumentsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabOrderDocument} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create lab order documents. An example lab workflow is as following:  - When you get orders, submit them via `/api/lab_orders`, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via `/api/lab_documents` and submit the results data via `/api/lab_results`  - Update `/api/lab_orders` status 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labDocumentsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabOrderDocument}
     */
    labDocumentsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = LabOrderDocument;
      return this.apiClient.callApi(
        '/api/lab_documents', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labDocumentsDelete operation.
     * @callback module:api/ClinicalApi~labDocumentsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing lab order document
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labDocumentsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labDocumentsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labDocumentsDelete");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/lab_documents/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labDocumentsList operation.
     * @callback module:api/ClinicalApi~labDocumentsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabDocumentsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search lab order documents
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labDocumentsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabDocumentsList200Response}
     */
    labDocumentsList(opts, callback) {
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
      let returnType = LabDocumentsList200Response;
      return this.apiClient.callApi(
        '/api/lab_documents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labDocumentsPartialUpdate operation.
     * @callback module:api/ClinicalApi~labDocumentsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab order document
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labDocumentsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labDocumentsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labDocumentsPartialUpdate");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/lab_documents/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labDocumentsRead operation.
     * @callback module:api/ClinicalApi~labDocumentsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabOrderDocument} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing lab order document
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labDocumentsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabOrderDocument}
     */
    labDocumentsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labDocumentsRead");
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
      let returnType = LabOrderDocument;
      return this.apiClient.callApi(
        '/api/lab_documents/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labDocumentsUpdate operation.
     * @callback module:api/ClinicalApi~labDocumentsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab order document
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labDocumentsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labDocumentsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labDocumentsUpdate");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/lab_documents/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersCreate operation.
     * @callback module:api/ClinicalApi~labOrdersCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabOrder} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create lab orders. An example lab workflow is as following:  - When you get orders, submit them via `/api/lab_orders`, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via `/api/lab_documents` and submit the results data via `/api/lab_results`  - Update `/api/lab_orders` status 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabOrder}
     */
    labOrdersCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = LabOrder;
      return this.apiClient.callApi(
        '/api/lab_orders', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersDelete operation.
     * @callback module:api/ClinicalApi~labOrdersDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing lab order
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labOrdersDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labOrdersDelete");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/lab_orders/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersList operation.
     * @callback module:api/ClinicalApi~labOrdersListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabOrdersList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search lab orders
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabOrdersList200Response}
     */
    labOrdersList(opts, callback) {
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
      let returnType = LabOrdersList200Response;
      return this.apiClient.callApi(
        '/api/lab_orders', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersPartialUpdate operation.
     * @callback module:api/ClinicalApi~labOrdersPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab order
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labOrdersPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labOrdersPartialUpdate");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/lab_orders/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersRead operation.
     * @callback module:api/ClinicalApi~labOrdersReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabOrder} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing lab order
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabOrder}
     */
    labOrdersRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labOrdersRead");
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
      let returnType = LabOrder;
      return this.apiClient.callApi(
        '/api/lab_orders/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersSummaryList operation.
     * @callback module:api/ClinicalApi~labOrdersSummaryListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabOrdersList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersSummaryListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabOrdersList200Response}
     */
    labOrdersSummaryList(opts, callback) {
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
      let returnType = LabOrdersList200Response;
      return this.apiClient.callApi(
        '/api/lab_orders_summary', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersSummaryRead operation.
     * @callback module:api/ClinicalApi~labOrdersSummaryReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabOrder} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersSummaryReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabOrder}
     */
    labOrdersSummaryRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labOrdersSummaryRead");
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
      let returnType = LabOrder;
      return this.apiClient.callApi(
        '/api/lab_orders_summary/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labOrdersUpdate operation.
     * @callback module:api/ClinicalApi~labOrdersUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab order
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labOrdersUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labOrdersUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labOrdersUpdate");
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/lab_orders/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labResultsCreate operation.
     * @callback module:api/ClinicalApi~labResultsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create lab results. An example lab workflow is as following:  - When you get orders, submit them via `/api/lab_orders`, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via `/api/lab_documents` and submit the results data via `/api/lab_results`  - Update `/api/lab_orders` status 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labResultsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabResult}
     */
    labResultsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'order': opts['order'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabResult;
      return this.apiClient.callApi(
        '/api/lab_results', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labResultsDelete operation.
     * @callback module:api/ClinicalApi~labResultsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing lab result
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labResultsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labResultsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labResultsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
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
        '/api/lab_results/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labResultsList operation.
     * @callback module:api/ClinicalApi~labResultsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabResultsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search lab results
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labResultsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabResultsList200Response}
     */
    labResultsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'order': opts['order'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabResultsList200Response;
      return this.apiClient.callApi(
        '/api/lab_results', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labResultsPartialUpdate operation.
     * @callback module:api/ClinicalApi~labResultsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab result
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labResultsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labResultsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labResultsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
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
        '/api/lab_results/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labResultsRead operation.
     * @callback module:api/ClinicalApi~labResultsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing lab result
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labResultsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabResult}
     */
    labResultsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labResultsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabResult;
      return this.apiClient.callApi(
        '/api/lab_results/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labResultsUpdate operation.
     * @callback module:api/ClinicalApi~labResultsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab result
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labResultsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labResultsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labResultsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
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
        '/api/lab_results/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labTestsCreate operation.
     * @callback module:api/ClinicalApi~labTestsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabTest} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create lab tests. An example lab workflow is as following:  - When you get orders, submit them via `/api/lab_orders`, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via `/api/lab_documents` and submit the results data via `/api/lab_results`  - Update `/api/lab_orders` status 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labTestsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabTest}
     */
    labTestsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'order': opts['order'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabTest;
      return this.apiClient.callApi(
        '/api/lab_tests', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labTestsDelete operation.
     * @callback module:api/ClinicalApi~labTestsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing lab test
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labTestsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labTestsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labTestsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
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
        '/api/lab_tests/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labTestsList operation.
     * @callback module:api/ClinicalApi~labTestsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabTestsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search lab tests
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labTestsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabTestsList200Response}
     */
    labTestsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'order': opts['order'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabTestsList200Response;
      return this.apiClient.callApi(
        '/api/lab_tests', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labTestsPartialUpdate operation.
     * @callback module:api/ClinicalApi~labTestsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab test
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labTestsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labTestsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labTestsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
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
        '/api/lab_tests/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labTestsRead operation.
     * @callback module:api/ClinicalApi~labTestsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabTest} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing lab test
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labTestsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabTest}
     */
    labTestsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labTestsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
        'doctor': opts['doctor']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabTest;
      return this.apiClient.callApi(
        '/api/lab_tests/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the labTestsUpdate operation.
     * @callback module:api/ClinicalApi~labTestsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing lab test
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [order] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~labTestsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    labTestsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling labTestsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'order': opts['order'],
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
        '/api/lab_tests/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the medicationsAppendToPharmacyNote operation.
     * @callback module:api/ClinicalApi~medicationsAppendToPharmacyNoteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Append a message to the \"pharmacy_note\" section of the prescription, in a new paragraph
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~medicationsAppendToPharmacyNoteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    medicationsAppendToPharmacyNote(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling medicationsAppendToPharmacyNote");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/medications/{id}/append_to_pharmacy_note', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the medicationsCreate operation.
     * @callback module:api/ClinicalApi~medicationsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientDrug} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient medications
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~medicationsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientDrug}
     */
    medicationsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = PatientDrug;
      return this.apiClient.callApi(
        '/api/medications', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the medicationsList operation.
     * @callback module:api/ClinicalApi~medicationsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MedicationsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient medications
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~medicationsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MedicationsList200Response}
     */
    medicationsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = MedicationsList200Response;
      return this.apiClient.callApi(
        '/api/medications', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the medicationsPartialUpdate operation.
     * @callback module:api/ClinicalApi~medicationsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient medications
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~medicationsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    medicationsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling medicationsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/medications/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the medicationsRead operation.
     * @callback module:api/ClinicalApi~medicationsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientDrug} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient medications
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~medicationsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientDrug}
     */
    medicationsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling medicationsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = PatientDrug;
      return this.apiClient.callApi(
        '/api/medications/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the medicationsUpdate operation.
     * @callback module:api/ClinicalApi~medicationsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient medications
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~medicationsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    medicationsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling medicationsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/medications/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientCommunicationsCreate operation.
     * @callback module:api/ClinicalApi~patientCommunicationsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientCommunication} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient communication for CQM
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientCommunicationsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientCommunication}
     */
    patientCommunicationsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = PatientCommunication;
      return this.apiClient.callApi(
        '/api/patient_communications', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientCommunicationsList operation.
     * @callback module:api/ClinicalApi~patientCommunicationsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientCommunicationsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient communications for CQM
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientCommunicationsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientCommunicationsList200Response}
     */
    patientCommunicationsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = PatientCommunicationsList200Response;
      return this.apiClient.callApi(
        '/api/patient_communications', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientCommunicationsPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientCommunicationsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient communication for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientCommunicationsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientCommunicationsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientCommunicationsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_communications/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientCommunicationsRead operation.
     * @callback module:api/ClinicalApi~patientCommunicationsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientCommunication} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient communication for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientCommunicationsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientCommunication}
     */
    patientCommunicationsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientCommunicationsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = PatientCommunication;
      return this.apiClient.callApi(
        '/api/patient_communications/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientCommunicationsUpdate operation.
     * @callback module:api/ClinicalApi~patientCommunicationsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient communication for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientCommunicationsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientCommunicationsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientCommunicationsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_communications/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientFlagTypesCreate operation.
     * @callback module:api/ClinicalApi~patientFlagTypesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientFlagType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient flag types
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientFlagTypesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientFlagType}
     */
    patientFlagTypesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = PatientFlagType;
      return this.apiClient.callApi(
        '/api/patient_flag_types', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientFlagTypesList operation.
     * @callback module:api/ClinicalApi~patientFlagTypesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientFlagTypesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient flag types
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientFlagTypesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientFlagTypesList200Response}
     */
    patientFlagTypesList(opts, callback) {
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
      let returnType = PatientFlagTypesList200Response;
      return this.apiClient.callApi(
        '/api/patient_flag_types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientFlagTypesPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientFlagTypesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient flag type
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientFlagTypesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientFlagTypesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientFlagTypesPartialUpdate");
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
        '/api/patient_flag_types/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientFlagTypesRead operation.
     * @callback module:api/ClinicalApi~patientFlagTypesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientFlagType} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient flag type
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientFlagTypesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientFlagType}
     */
    patientFlagTypesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientFlagTypesRead");
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
      let returnType = PatientFlagType;
      return this.apiClient.callApi(
        '/api/patient_flag_types/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientFlagTypesUpdate operation.
     * @callback module:api/ClinicalApi~patientFlagTypesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient flag type
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientFlagTypesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientFlagTypesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientFlagTypesUpdate");
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
        '/api/patient_flag_types/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientInterventionsCreate operation.
     * @callback module:api/ClinicalApi~patientInterventionsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientIntervention} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient intervention for CQM
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientInterventionsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientIntervention}
     */
    patientInterventionsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = PatientIntervention;
      return this.apiClient.callApi(
        '/api/patient_interventions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientInterventionsList operation.
     * @callback module:api/ClinicalApi~patientInterventionsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientInterventionsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient interventions for CQM
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientInterventionsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientInterventionsList200Response}
     */
    patientInterventionsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = PatientInterventionsList200Response;
      return this.apiClient.callApi(
        '/api/patient_interventions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientInterventionsPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientInterventionsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient intervention for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientInterventionsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientInterventionsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientInterventionsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_interventions/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientInterventionsRead operation.
     * @callback module:api/ClinicalApi~patientInterventionsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientIntervention} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient intervention for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientInterventionsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientIntervention}
     */
    patientInterventionsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientInterventionsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = PatientIntervention;
      return this.apiClient.callApi(
        '/api/patient_interventions/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientInterventionsUpdate operation.
     * @callback module:api/ClinicalApi~patientInterventionsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient intervention for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientInterventionsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientInterventionsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientInterventionsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_interventions/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientLabResultsCreate operation.
     * @callback module:api/ClinicalApi~patientLabResultsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientLabResultSet} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {Number} [orderingDoctor] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientLabResultsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientLabResultSet}
     */
    patientLabResultsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'ordering_doctor': opts['orderingDoctor'],
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
      let returnType = PatientLabResultSet;
      return this.apiClient.callApi(
        '/api/patient_lab_results', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientLabResultsDelete operation.
     * @callback module:api/ClinicalApi~patientLabResultsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [orderingDoctor] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientLabResultsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientLabResultsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientLabResultsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'ordering_doctor': opts['orderingDoctor'],
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
        '/api/patient_lab_results/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientLabResultsList operation.
     * @callback module:api/ClinicalApi~patientLabResultsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientLabResultsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [orderingDoctor] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientLabResultsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientLabResultsList200Response}
     */
    patientLabResultsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'ordering_doctor': opts['orderingDoctor'],
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
      let returnType = PatientLabResultsList200Response;
      return this.apiClient.callApi(
        '/api/patient_lab_results', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientLabResultsPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientLabResultsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [orderingDoctor] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientLabResultsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientLabResultsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientLabResultsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'ordering_doctor': opts['orderingDoctor'],
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
        '/api/patient_lab_results/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientLabResultsRead operation.
     * @callback module:api/ClinicalApi~patientLabResultsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientLabResultSet} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [orderingDoctor] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientLabResultsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientLabResultSet}
     */
    patientLabResultsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientLabResultsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'ordering_doctor': opts['orderingDoctor'],
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
      let returnType = PatientLabResultSet;
      return this.apiClient.callApi(
        '/api/patient_lab_results/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientLabResultsUpdate operation.
     * @callback module:api/ClinicalApi~patientLabResultsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [orderingDoctor] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientLabResultsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientLabResultsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientLabResultsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'ordering_doctor': opts['orderingDoctor'],
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
        '/api/patient_lab_results/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientMessagesCreate operation.
     * @callback module:api/ClinicalApi~patientMessagesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientMessage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientMessagesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientMessage}
     */
    patientMessagesCreate(opts, callback) {
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
      let returnType = PatientMessage;
      return this.apiClient.callApi(
        '/api/patient_messages', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientMessagesList operation.
     * @callback module:api/ClinicalApi~patientMessagesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientMessagesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientMessagesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientMessagesList200Response}
     */
    patientMessagesList(opts, callback) {
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
      let returnType = PatientMessagesList200Response;
      return this.apiClient.callApi(
        '/api/patient_messages', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientMessagesPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientMessagesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientMessagesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientMessagesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientMessagesPartialUpdate");
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
        '/api/patient_messages/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientMessagesRead operation.
     * @callback module:api/ClinicalApi~patientMessagesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientMessage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientMessagesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientMessage}
     */
    patientMessagesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientMessagesRead");
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
      let returnType = PatientMessage;
      return this.apiClient.callApi(
        '/api/patient_messages/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientMessagesUpdate operation.
     * @callback module:api/ClinicalApi~patientMessagesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientMessagesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientMessagesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientMessagesUpdate");
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
        '/api/patient_messages/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPhysicalExamsCreate operation.
     * @callback module:api/ClinicalApi~patientPhysicalExamsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientPhysicalExam} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient physical exam for CQM
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientPhysicalExamsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientPhysicalExam}
     */
    patientPhysicalExamsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = PatientPhysicalExam;
      return this.apiClient.callApi(
        '/api/patient_physical_exams', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPhysicalExamsList operation.
     * @callback module:api/ClinicalApi~patientPhysicalExamsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientPhysicalExamsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient physical exams for CQM
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientPhysicalExamsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientPhysicalExamsList200Response}
     */
    patientPhysicalExamsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = PatientPhysicalExamsList200Response;
      return this.apiClient.callApi(
        '/api/patient_physical_exams', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPhysicalExamsPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientPhysicalExamsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient physical exam for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientPhysicalExamsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientPhysicalExamsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientPhysicalExamsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_physical_exams/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPhysicalExamsRead operation.
     * @callback module:api/ClinicalApi~patientPhysicalExamsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientPhysicalExam} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient physical exam for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientPhysicalExamsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientPhysicalExam}
     */
    patientPhysicalExamsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientPhysicalExamsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = PatientPhysicalExam;
      return this.apiClient.callApi(
        '/api/patient_physical_exams/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientPhysicalExamsUpdate operation.
     * @callback module:api/ClinicalApi~patientPhysicalExamsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient physical exam for CQM
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientPhysicalExamsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientPhysicalExamsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientPhysicalExamsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_physical_exams/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientRiskAssessmentsCreate operation.
     * @callback module:api/ClinicalApi~patientRiskAssessmentsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientRiskAssessment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientRiskAssessmentsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientRiskAssessment}
     */
    patientRiskAssessmentsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = PatientRiskAssessment;
      return this.apiClient.callApi(
        '/api/patient_risk_assessments', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientRiskAssessmentsList operation.
     * @callback module:api/ClinicalApi~patientRiskAssessmentsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientRiskAssessmentsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientRiskAssessmentsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientRiskAssessmentsList200Response}
     */
    patientRiskAssessmentsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = PatientRiskAssessmentsList200Response;
      return this.apiClient.callApi(
        '/api/patient_risk_assessments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientRiskAssessmentsPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientRiskAssessmentsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientRiskAssessmentsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientRiskAssessmentsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientRiskAssessmentsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_risk_assessments/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientRiskAssessmentsRead operation.
     * @callback module:api/ClinicalApi~patientRiskAssessmentsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientRiskAssessment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientRiskAssessmentsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientRiskAssessment}
     */
    patientRiskAssessmentsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientRiskAssessmentsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = PatientRiskAssessment;
      return this.apiClient.callApi(
        '/api/patient_risk_assessments/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientRiskAssessmentsUpdate operation.
     * @callback module:api/ClinicalApi~patientRiskAssessmentsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientRiskAssessmentsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientRiskAssessmentsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientRiskAssessmentsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/patient_risk_assessments/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientVaccineRecordsCreate operation.
     * @callback module:api/ClinicalApi~patientVaccineRecordsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientVaccineRecord} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient vaccine records
     * @param {Object} opts Optional parameters
     * @param {String} [cvxCode] 
     * @param {Number} [patient] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientVaccineRecordsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientVaccineRecord}
     */
    patientVaccineRecordsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cvx_code': opts['cvxCode'],
        'patient': opts['patient'],
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
      let returnType = PatientVaccineRecord;
      return this.apiClient.callApi(
        '/api/patient_vaccine_records', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientVaccineRecordsList operation.
     * @callback module:api/ClinicalApi~patientVaccineRecordsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientVaccineRecordsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient vaccine records
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [cvxCode] 
     * @param {Number} [patient] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientVaccineRecordsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientVaccineRecordsList200Response}
     */
    patientVaccineRecordsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'cvx_code': opts['cvxCode'],
        'patient': opts['patient'],
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
      let returnType = PatientVaccineRecordsList200Response;
      return this.apiClient.callApi(
        '/api/patient_vaccine_records', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientVaccineRecordsPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientVaccineRecordsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient vaccine records
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [cvxCode] 
     * @param {Number} [patient] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientVaccineRecordsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientVaccineRecordsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientVaccineRecordsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'cvx_code': opts['cvxCode'],
        'patient': opts['patient'],
        'since': opts['since'],
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
        '/api/patient_vaccine_records/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientVaccineRecordsRead operation.
     * @callback module:api/ClinicalApi~patientVaccineRecordsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientVaccineRecord} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient vaccine records
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [cvxCode] 
     * @param {Number} [patient] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientVaccineRecordsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientVaccineRecord}
     */
    patientVaccineRecordsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientVaccineRecordsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'cvx_code': opts['cvxCode'],
        'patient': opts['patient'],
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
      let returnType = PatientVaccineRecord;
      return this.apiClient.callApi(
        '/api/patient_vaccine_records/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientVaccineRecordsUpdate operation.
     * @callback module:api/ClinicalApi~patientVaccineRecordsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient vaccine records
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [cvxCode] 
     * @param {Number} [patient] 
     * @param {String} [since] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~patientVaccineRecordsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientVaccineRecordsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientVaccineRecordsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'cvx_code': opts['cvxCode'],
        'patient': opts['patient'],
        'since': opts['since'],
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
        '/api/patient_vaccine_records/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsCcda operation.
     * @callback module:api/ClinicalApi~patientsCcdaCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve patient CCDA
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsCcdaCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    patientsCcda(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsCcda");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/api/patients/{id}/ccda', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsCreate operation.
     * @callback module:api/ClinicalApi~patientsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Patient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Patient}
     */
    patientsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Patient;
      return this.apiClient.callApi(
        '/api/patients', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsDelete operation.
     * @callback module:api/ClinicalApi~patientsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing patient
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientsDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
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
        '/api/patients/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsList operation.
     * @callback module:api/ClinicalApi~patientsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patients
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientsList200Response}
     */
    patientsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PatientsList200Response;
      return this.apiClient.callApi(
        '/api/patients', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsOnpatientAccessCreate operation.
     * @callback module:api/ClinicalApi~patientsOnpatientAccessCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Patient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Send new onpatient invite to patient
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsOnpatientAccessCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Patient}
     */
    patientsOnpatientAccessCreate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsOnpatientAccessCreate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Patient;
      return this.apiClient.callApi(
        '/api/patients/{id}/onpatient_access', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsOnpatientAccessDelete operation.
     * @callback module:api/ClinicalApi~patientsOnpatientAccessDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Revoke sent onpatient invites
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsOnpatientAccessDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientsOnpatientAccessDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsOnpatientAccessDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
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
        '/api/patients/{id}/onpatient_access', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsOnpatientAccessRead operation.
     * @callback module:api/ClinicalApi~patientsOnpatientAccessReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Patient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search existing onpatient access invites
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsOnpatientAccessReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Patient}
     */
    patientsOnpatientAccessRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsOnpatientAccessRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Patient;
      return this.apiClient.callApi(
        '/api/patients/{id}/onpatient_access', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
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
        '/api/patients/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsQrda1 operation.
     * @callback module:api/ClinicalApi~patientsQrda1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve patient QRDA1
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsQrda1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    patientsQrda1(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsQrda1");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/api/patients/{id}/qrda1', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsRead operation.
     * @callback module:api/ClinicalApi~patientsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Patient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Patient}
     */
    patientsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Patient;
      return this.apiClient.callApi(
        '/api/patients/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsSummaryCreate operation.
     * @callback module:api/ClinicalApi~patientsSummaryCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Patient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {module:api/ClinicalApi~patientsSummaryCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Patient}
     */
    patientsSummaryCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Patient;
      return this.apiClient.callApi(
        '/api/patients_summary', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsSummaryDelete operation.
     * @callback module:api/ClinicalApi~patientsSummaryDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {module:api/ClinicalApi~patientsSummaryDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientsSummaryDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsSummaryDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth']
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
        '/api/patients_summary/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsSummaryList operation.
     * @callback module:api/ClinicalApi~patientsSummaryListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {module:api/ClinicalApi~patientsSummaryListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientsList200Response}
     */
    patientsSummaryList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PatientsList200Response;
      return this.apiClient.callApi(
        '/api/patients_summary', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsSummaryPartialUpdate operation.
     * @callback module:api/ClinicalApi~patientsSummaryPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {module:api/ClinicalApi~patientsSummaryPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientsSummaryPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsSummaryPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth']
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
        '/api/patients_summary/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsSummaryRead operation.
     * @callback module:api/ClinicalApi~patientsSummaryReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Patient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {module:api/ClinicalApi~patientsSummaryReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Patient}
     */
    patientsSummaryRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsSummaryRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Patient;
      return this.apiClient.callApi(
        '/api/patients_summary/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsSummaryUpdate operation.
     * @callback module:api/ClinicalApi~patientsSummaryUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {module:api/ClinicalApi~patientsSummaryUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientsSummaryUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsSummaryUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth']
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
        '/api/patients_summary/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patientsUpdate operation.
     * @callback module:api/ClinicalApi~patientsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {String} [firstName] 
     * @param {String} [lastName] 
     * @param {String} [preferredLanguage] 
     * @param {Number} [doctor] 
     * @param {String} [gender] 
     * @param {String} [since] 
     * @param {String} [dateOfBirth] 
     * @param {String} [race] 
     * @param {String} [chartId] 
     * @param {String} [email] 
     * @param {String} [ethnicity] 
     * @param {module:api/ClinicalApi~patientsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    patientsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling patientsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'first_name': opts['firstName'],
        'last_name': opts['lastName'],
        'preferred_language': opts['preferredLanguage'],
        'doctor': opts['doctor'],
        'gender': opts['gender'],
        'since': opts['since'],
        'date_of_birth': opts['dateOfBirth'],
        'race': opts['race'],
        'chart_id': opts['chartId'],
        'email': opts['email'],
        'ethnicity': opts['ethnicity']
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
        '/api/patients/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the prescriptionMessagesList operation.
     * @callback module:api/ClinicalApi~prescriptionMessagesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PrescriptionMessagesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search prescription messages
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [parentMessage] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~prescriptionMessagesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PrescriptionMessagesList200Response}
     */
    prescriptionMessagesList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
        'parent_message': opts['parentMessage'],
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
      let returnType = PrescriptionMessagesList200Response;
      return this.apiClient.callApi(
        '/api/prescription_messages', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the prescriptionMessagesRead operation.
     * @callback module:api/ClinicalApi~prescriptionMessagesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PrescriptionMessage} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing prescription message
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [parentMessage] 
     * @param {String} [since] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~prescriptionMessagesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PrescriptionMessage}
     */
    prescriptionMessagesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling prescriptionMessagesRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
        'parent_message': opts['parentMessage'],
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
      let returnType = PrescriptionMessage;
      return this.apiClient.callApi(
        '/api/prescription_messages/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the problemsCreate operation.
     * @callback module:api/ClinicalApi~problemsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientProblem} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create patient problems
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~problemsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientProblem}
     */
    problemsCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = PatientProblem;
      return this.apiClient.callApi(
        '/api/problems', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the problemsList operation.
     * @callback module:api/ClinicalApi~problemsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ProblemsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search patient problems
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~problemsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ProblemsList200Response}
     */
    problemsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize'],
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
      let returnType = ProblemsList200Response;
      return this.apiClient.callApi(
        '/api/problems', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the problemsPartialUpdate operation.
     * @callback module:api/ClinicalApi~problemsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient problems
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~problemsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    problemsPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling problemsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/problems/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the problemsRead operation.
     * @callback module:api/ClinicalApi~problemsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PatientProblem} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing patient problems
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~problemsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PatientProblem}
     */
    problemsRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling problemsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
      let returnType = PatientProblem;
      return this.apiClient.callApi(
        '/api/problems/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the problemsUpdate operation.
     * @callback module:api/ClinicalApi~problemsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing patient problems
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [patient] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~problemsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    problemsUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling problemsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/problems/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reminderProfilesCreate operation.
     * @callback module:api/ClinicalApi~reminderProfilesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReminderProfile} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create reminder profile
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~reminderProfilesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReminderProfile}
     */
    reminderProfilesCreate(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
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
      let returnType = ReminderProfile;
      return this.apiClient.callApi(
        '/api/reminder_profiles', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reminderProfilesDelete operation.
     * @callback module:api/ClinicalApi~reminderProfilesDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing reminder profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~reminderProfilesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reminderProfilesDelete(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling reminderProfilesDelete");
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
        '/api/reminder_profiles/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reminderProfilesList operation.
     * @callback module:api/ClinicalApi~reminderProfilesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReminderProfilesList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search reminder profiles
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~reminderProfilesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReminderProfilesList200Response}
     */
    reminderProfilesList(opts, callback) {
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
      let returnType = ReminderProfilesList200Response;
      return this.apiClient.callApi(
        '/api/reminder_profiles', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reminderProfilesPartialUpdate operation.
     * @callback module:api/ClinicalApi~reminderProfilesPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing reminder profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~reminderProfilesPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reminderProfilesPartialUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling reminderProfilesPartialUpdate");
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
        '/api/reminder_profiles/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reminderProfilesRead operation.
     * @callback module:api/ClinicalApi~reminderProfilesReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ReminderProfile} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing reminder profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~reminderProfilesReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ReminderProfile}
     */
    reminderProfilesRead(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling reminderProfilesRead");
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
      let returnType = ReminderProfile;
      return this.apiClient.callApi(
        '/api/reminder_profiles/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the reminderProfilesUpdate operation.
     * @callback module:api/ClinicalApi~reminderProfilesUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing reminder profile
     * @param {String} id 
     * @param {Object} opts Optional parameters
     * @param {Number} [doctor] 
     * @param {module:api/ClinicalApi~reminderProfilesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    reminderProfilesUpdate(id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling reminderProfilesUpdate");
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
        '/api/reminder_profiles/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sublabsCreate operation.
     * @callback module:api/ClinicalApi~sublabsCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabVendorLocation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create sub-vendors  - When you get orders, submit them via `/api/lab_orders`, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via `/api/lab_documents` and submit the results data via `/api/lab_results`  - Update `/api/lab_orders` status 
     * @param {module:api/ClinicalApi~sublabsCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabVendorLocation}
     */
    sublabsCreate(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabVendorLocation;
      return this.apiClient.callApi(
        '/api/sublabs', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sublabsDelete operation.
     * @callback module:api/ClinicalApi~sublabsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an existing sub vendor
     * @param {Number} id 
     * @param {module:api/ClinicalApi~sublabsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    sublabsDelete(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling sublabsDelete");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/sublabs/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sublabsList operation.
     * @callback module:api/ClinicalApi~sublabsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SublabsList200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve or search sub vendors
     * @param {Object} opts Optional parameters
     * @param {String} [cursor] 
     * @param {Number} [pageSize] 
     * @param {module:api/ClinicalApi~sublabsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SublabsList200Response}
     */
    sublabsList(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'cursor': opts['cursor'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = SublabsList200Response;
      return this.apiClient.callApi(
        '/api/sublabs', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sublabsPartialUpdate operation.
     * @callback module:api/ClinicalApi~sublabsPartialUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing sub vendor
     * @param {Number} id 
     * @param {module:api/ClinicalApi~sublabsPartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    sublabsPartialUpdate(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling sublabsPartialUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/sublabs/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sublabsRead operation.
     * @callback module:api/ClinicalApi~sublabsReadCallback
     * @param {String} error Error message, if any.
     * @param {module:model/LabVendorLocation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve an existing sub vendor
     * @param {Number} id 
     * @param {module:api/ClinicalApi~sublabsReadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/LabVendorLocation}
     */
    sublabsRead(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling sublabsRead");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['drchrono_oauth2'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = LabVendorLocation;
      return this.apiClient.callApi(
        '/api/sublabs/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the sublabsUpdate operation.
     * @callback module:api/ClinicalApi~sublabsUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an existing sub vendor
     * @param {Number} id 
     * @param {module:api/ClinicalApi~sublabsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    sublabsUpdate(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling sublabsUpdate");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
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
        '/api/sublabs/{id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
