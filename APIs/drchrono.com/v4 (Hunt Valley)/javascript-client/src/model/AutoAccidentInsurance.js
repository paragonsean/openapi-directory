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

import ApiClient from '../ApiClient';

/**
 * The AutoAccidentInsurance model module.
 * @module model/AutoAccidentInsurance
 * @version v4 (Hunt Valley)
 */
class AutoAccidentInsurance {
    /**
     * Constructs a new <code>AutoAccidentInsurance</code>.
     * 
     * @alias module:model/AutoAccidentInsurance
     */
    constructor() { 
        
        AutoAccidentInsurance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AutoAccidentInsurance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AutoAccidentInsurance} obj Optional instance to populate.
     * @return {module:model/AutoAccidentInsurance} The populated <code>AutoAccidentInsurance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AutoAccidentInsurance();

            if (data.hasOwnProperty('auto_accident_case_number')) {
                obj['auto_accident_case_number'] = ApiClient.convertToType(data['auto_accident_case_number'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_claim_rep_address')) {
                obj['auto_accident_claim_rep_address'] = ApiClient.convertToType(data['auto_accident_claim_rep_address'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_claim_rep_city')) {
                obj['auto_accident_claim_rep_city'] = ApiClient.convertToType(data['auto_accident_claim_rep_city'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_claim_rep_is_insurer')) {
                obj['auto_accident_claim_rep_is_insurer'] = ApiClient.convertToType(data['auto_accident_claim_rep_is_insurer'], 'Boolean');
            }
            if (data.hasOwnProperty('auto_accident_claim_rep_name')) {
                obj['auto_accident_claim_rep_name'] = ApiClient.convertToType(data['auto_accident_claim_rep_name'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_claim_rep_state')) {
                obj['auto_accident_claim_rep_state'] = ApiClient.convertToType(data['auto_accident_claim_rep_state'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_claim_rep_zip')) {
                obj['auto_accident_claim_rep_zip'] = ApiClient.convertToType(data['auto_accident_claim_rep_zip'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_company')) {
                obj['auto_accident_company'] = ApiClient.convertToType(data['auto_accident_company'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_date_of_accident')) {
                obj['auto_accident_date_of_accident'] = ApiClient.convertToType(data['auto_accident_date_of_accident'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_disabled_from_date')) {
                obj['auto_accident_disabled_from_date'] = ApiClient.convertToType(data['auto_accident_disabled_from_date'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_disabled_to_date')) {
                obj['auto_accident_disabled_to_date'] = ApiClient.convertToType(data['auto_accident_disabled_to_date'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_had_similar_condition')) {
                obj['auto_accident_had_similar_condition'] = ApiClient.convertToType(data['auto_accident_had_similar_condition'], 'Boolean');
            }
            if (data.hasOwnProperty('auto_accident_is_subscriber_the_patient')) {
                obj['auto_accident_is_subscriber_the_patient'] = ApiClient.convertToType(data['auto_accident_is_subscriber_the_patient'], 'Boolean');
            }
            if (data.hasOwnProperty('auto_accident_notes')) {
                obj['auto_accident_notes'] = ApiClient.convertToType(data['auto_accident_notes'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_patient_relationship_to_subscriber')) {
                obj['auto_accident_patient_relationship_to_subscriber'] = ApiClient.convertToType(data['auto_accident_patient_relationship_to_subscriber'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_payer_address')) {
                obj['auto_accident_payer_address'] = ApiClient.convertToType(data['auto_accident_payer_address'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_payer_city')) {
                obj['auto_accident_payer_city'] = ApiClient.convertToType(data['auto_accident_payer_city'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_payer_id')) {
                obj['auto_accident_payer_id'] = ApiClient.convertToType(data['auto_accident_payer_id'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_payer_state')) {
                obj['auto_accident_payer_state'] = ApiClient.convertToType(data['auto_accident_payer_state'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_payer_zip')) {
                obj['auto_accident_payer_zip'] = ApiClient.convertToType(data['auto_accident_payer_zip'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_policy_number')) {
                obj['auto_accident_policy_number'] = ApiClient.convertToType(data['auto_accident_policy_number'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_return_to_work_date')) {
                obj['auto_accident_return_to_work_date'] = ApiClient.convertToType(data['auto_accident_return_to_work_date'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_significant_injury')) {
                obj['auto_accident_significant_injury'] = ApiClient.convertToType(data['auto_accident_significant_injury'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_significant_injury_notes')) {
                obj['auto_accident_significant_injury_notes'] = ApiClient.convertToType(data['auto_accident_significant_injury_notes'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_similar_condition_date')) {
                obj['auto_accident_similar_condition_date'] = ApiClient.convertToType(data['auto_accident_similar_condition_date'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_similar_condition_notes')) {
                obj['auto_accident_similar_condition_notes'] = ApiClient.convertToType(data['auto_accident_similar_condition_notes'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_state_of_occurrence')) {
                obj['auto_accident_state_of_occurrence'] = ApiClient.convertToType(data['auto_accident_state_of_occurrence'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_still_under_care')) {
                obj['auto_accident_still_under_care'] = ApiClient.convertToType(data['auto_accident_still_under_care'], 'Boolean');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_address')) {
                obj['auto_accident_subscriber_address'] = ApiClient.convertToType(data['auto_accident_subscriber_address'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_city')) {
                obj['auto_accident_subscriber_city'] = ApiClient.convertToType(data['auto_accident_subscriber_city'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_date_of_birth')) {
                obj['auto_accident_subscriber_date_of_birth'] = ApiClient.convertToType(data['auto_accident_subscriber_date_of_birth'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_first_name')) {
                obj['auto_accident_subscriber_first_name'] = ApiClient.convertToType(data['auto_accident_subscriber_first_name'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_last_name')) {
                obj['auto_accident_subscriber_last_name'] = ApiClient.convertToType(data['auto_accident_subscriber_last_name'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_middle_name')) {
                obj['auto_accident_subscriber_middle_name'] = ApiClient.convertToType(data['auto_accident_subscriber_middle_name'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_phone_number')) {
                obj['auto_accident_subscriber_phone_number'] = ApiClient.convertToType(data['auto_accident_subscriber_phone_number'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_social_security')) {
                obj['auto_accident_subscriber_social_security'] = ApiClient.convertToType(data['auto_accident_subscriber_social_security'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_state')) {
                obj['auto_accident_subscriber_state'] = ApiClient.convertToType(data['auto_accident_subscriber_state'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_suffix')) {
                obj['auto_accident_subscriber_suffix'] = ApiClient.convertToType(data['auto_accident_subscriber_suffix'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_subscriber_zip_code')) {
                obj['auto_accident_subscriber_zip_code'] = ApiClient.convertToType(data['auto_accident_subscriber_zip_code'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_treatment_duration')) {
                obj['auto_accident_treatment_duration'] = ApiClient.convertToType(data['auto_accident_treatment_duration'], 'String');
            }
            if (data.hasOwnProperty('auto_accident_will_require_therapy')) {
                obj['auto_accident_will_require_therapy'] = ApiClient.convertToType(data['auto_accident_will_require_therapy'], 'Boolean');
            }
            if (data.hasOwnProperty('auto_accident_will_require_therapy_rec')) {
                obj['auto_accident_will_require_therapy_rec'] = ApiClient.convertToType(data['auto_accident_will_require_therapy_rec'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AutoAccidentInsurance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AutoAccidentInsurance</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['auto_accident_case_number'] && !(typeof data['auto_accident_case_number'] === 'string' || data['auto_accident_case_number'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_case_number` to be a primitive type in the JSON string but got " + data['auto_accident_case_number']);
        }
        // ensure the json data is a string
        if (data['auto_accident_claim_rep_address'] && !(typeof data['auto_accident_claim_rep_address'] === 'string' || data['auto_accident_claim_rep_address'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_claim_rep_address` to be a primitive type in the JSON string but got " + data['auto_accident_claim_rep_address']);
        }
        // ensure the json data is a string
        if (data['auto_accident_claim_rep_city'] && !(typeof data['auto_accident_claim_rep_city'] === 'string' || data['auto_accident_claim_rep_city'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_claim_rep_city` to be a primitive type in the JSON string but got " + data['auto_accident_claim_rep_city']);
        }
        // ensure the json data is a string
        if (data['auto_accident_claim_rep_name'] && !(typeof data['auto_accident_claim_rep_name'] === 'string' || data['auto_accident_claim_rep_name'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_claim_rep_name` to be a primitive type in the JSON string but got " + data['auto_accident_claim_rep_name']);
        }
        // ensure the json data is a string
        if (data['auto_accident_claim_rep_state'] && !(typeof data['auto_accident_claim_rep_state'] === 'string' || data['auto_accident_claim_rep_state'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_claim_rep_state` to be a primitive type in the JSON string but got " + data['auto_accident_claim_rep_state']);
        }
        // ensure the json data is a string
        if (data['auto_accident_claim_rep_zip'] && !(typeof data['auto_accident_claim_rep_zip'] === 'string' || data['auto_accident_claim_rep_zip'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_claim_rep_zip` to be a primitive type in the JSON string but got " + data['auto_accident_claim_rep_zip']);
        }
        // ensure the json data is a string
        if (data['auto_accident_company'] && !(typeof data['auto_accident_company'] === 'string' || data['auto_accident_company'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_company` to be a primitive type in the JSON string but got " + data['auto_accident_company']);
        }
        // ensure the json data is a string
        if (data['auto_accident_date_of_accident'] && !(typeof data['auto_accident_date_of_accident'] === 'string' || data['auto_accident_date_of_accident'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_date_of_accident` to be a primitive type in the JSON string but got " + data['auto_accident_date_of_accident']);
        }
        // ensure the json data is a string
        if (data['auto_accident_disabled_from_date'] && !(typeof data['auto_accident_disabled_from_date'] === 'string' || data['auto_accident_disabled_from_date'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_disabled_from_date` to be a primitive type in the JSON string but got " + data['auto_accident_disabled_from_date']);
        }
        // ensure the json data is a string
        if (data['auto_accident_disabled_to_date'] && !(typeof data['auto_accident_disabled_to_date'] === 'string' || data['auto_accident_disabled_to_date'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_disabled_to_date` to be a primitive type in the JSON string but got " + data['auto_accident_disabled_to_date']);
        }
        // ensure the json data is a string
        if (data['auto_accident_notes'] && !(typeof data['auto_accident_notes'] === 'string' || data['auto_accident_notes'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_notes` to be a primitive type in the JSON string but got " + data['auto_accident_notes']);
        }
        // ensure the json data is a string
        if (data['auto_accident_patient_relationship_to_subscriber'] && !(typeof data['auto_accident_patient_relationship_to_subscriber'] === 'string' || data['auto_accident_patient_relationship_to_subscriber'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_patient_relationship_to_subscriber` to be a primitive type in the JSON string but got " + data['auto_accident_patient_relationship_to_subscriber']);
        }
        // ensure the json data is a string
        if (data['auto_accident_payer_address'] && !(typeof data['auto_accident_payer_address'] === 'string' || data['auto_accident_payer_address'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_payer_address` to be a primitive type in the JSON string but got " + data['auto_accident_payer_address']);
        }
        // ensure the json data is a string
        if (data['auto_accident_payer_city'] && !(typeof data['auto_accident_payer_city'] === 'string' || data['auto_accident_payer_city'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_payer_city` to be a primitive type in the JSON string but got " + data['auto_accident_payer_city']);
        }
        // ensure the json data is a string
        if (data['auto_accident_payer_id'] && !(typeof data['auto_accident_payer_id'] === 'string' || data['auto_accident_payer_id'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_payer_id` to be a primitive type in the JSON string but got " + data['auto_accident_payer_id']);
        }
        // ensure the json data is a string
        if (data['auto_accident_payer_state'] && !(typeof data['auto_accident_payer_state'] === 'string' || data['auto_accident_payer_state'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_payer_state` to be a primitive type in the JSON string but got " + data['auto_accident_payer_state']);
        }
        // ensure the json data is a string
        if (data['auto_accident_payer_zip'] && !(typeof data['auto_accident_payer_zip'] === 'string' || data['auto_accident_payer_zip'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_payer_zip` to be a primitive type in the JSON string but got " + data['auto_accident_payer_zip']);
        }
        // ensure the json data is a string
        if (data['auto_accident_policy_number'] && !(typeof data['auto_accident_policy_number'] === 'string' || data['auto_accident_policy_number'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_policy_number` to be a primitive type in the JSON string but got " + data['auto_accident_policy_number']);
        }
        // ensure the json data is a string
        if (data['auto_accident_return_to_work_date'] && !(typeof data['auto_accident_return_to_work_date'] === 'string' || data['auto_accident_return_to_work_date'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_return_to_work_date` to be a primitive type in the JSON string but got " + data['auto_accident_return_to_work_date']);
        }
        // ensure the json data is a string
        if (data['auto_accident_significant_injury'] && !(typeof data['auto_accident_significant_injury'] === 'string' || data['auto_accident_significant_injury'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_significant_injury` to be a primitive type in the JSON string but got " + data['auto_accident_significant_injury']);
        }
        // ensure the json data is a string
        if (data['auto_accident_significant_injury_notes'] && !(typeof data['auto_accident_significant_injury_notes'] === 'string' || data['auto_accident_significant_injury_notes'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_significant_injury_notes` to be a primitive type in the JSON string but got " + data['auto_accident_significant_injury_notes']);
        }
        // ensure the json data is a string
        if (data['auto_accident_similar_condition_date'] && !(typeof data['auto_accident_similar_condition_date'] === 'string' || data['auto_accident_similar_condition_date'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_similar_condition_date` to be a primitive type in the JSON string but got " + data['auto_accident_similar_condition_date']);
        }
        // ensure the json data is a string
        if (data['auto_accident_similar_condition_notes'] && !(typeof data['auto_accident_similar_condition_notes'] === 'string' || data['auto_accident_similar_condition_notes'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_similar_condition_notes` to be a primitive type in the JSON string but got " + data['auto_accident_similar_condition_notes']);
        }
        // ensure the json data is a string
        if (data['auto_accident_state_of_occurrence'] && !(typeof data['auto_accident_state_of_occurrence'] === 'string' || data['auto_accident_state_of_occurrence'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_state_of_occurrence` to be a primitive type in the JSON string but got " + data['auto_accident_state_of_occurrence']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_address'] && !(typeof data['auto_accident_subscriber_address'] === 'string' || data['auto_accident_subscriber_address'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_address` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_address']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_city'] && !(typeof data['auto_accident_subscriber_city'] === 'string' || data['auto_accident_subscriber_city'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_city` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_city']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_date_of_birth'] && !(typeof data['auto_accident_subscriber_date_of_birth'] === 'string' || data['auto_accident_subscriber_date_of_birth'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_date_of_birth` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_date_of_birth']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_first_name'] && !(typeof data['auto_accident_subscriber_first_name'] === 'string' || data['auto_accident_subscriber_first_name'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_first_name` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_first_name']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_last_name'] && !(typeof data['auto_accident_subscriber_last_name'] === 'string' || data['auto_accident_subscriber_last_name'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_last_name` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_last_name']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_middle_name'] && !(typeof data['auto_accident_subscriber_middle_name'] === 'string' || data['auto_accident_subscriber_middle_name'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_middle_name` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_middle_name']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_phone_number'] && !(typeof data['auto_accident_subscriber_phone_number'] === 'string' || data['auto_accident_subscriber_phone_number'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_phone_number` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_phone_number']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_social_security'] && !(typeof data['auto_accident_subscriber_social_security'] === 'string' || data['auto_accident_subscriber_social_security'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_social_security` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_social_security']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_state'] && !(typeof data['auto_accident_subscriber_state'] === 'string' || data['auto_accident_subscriber_state'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_state` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_state']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_suffix'] && !(typeof data['auto_accident_subscriber_suffix'] === 'string' || data['auto_accident_subscriber_suffix'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_suffix` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_suffix']);
        }
        // ensure the json data is a string
        if (data['auto_accident_subscriber_zip_code'] && !(typeof data['auto_accident_subscriber_zip_code'] === 'string' || data['auto_accident_subscriber_zip_code'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_subscriber_zip_code` to be a primitive type in the JSON string but got " + data['auto_accident_subscriber_zip_code']);
        }
        // ensure the json data is a string
        if (data['auto_accident_treatment_duration'] && !(typeof data['auto_accident_treatment_duration'] === 'string' || data['auto_accident_treatment_duration'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_treatment_duration` to be a primitive type in the JSON string but got " + data['auto_accident_treatment_duration']);
        }
        // ensure the json data is a string
        if (data['auto_accident_will_require_therapy_rec'] && !(typeof data['auto_accident_will_require_therapy_rec'] === 'string' || data['auto_accident_will_require_therapy_rec'] instanceof String)) {
            throw new Error("Expected the field `auto_accident_will_require_therapy_rec` to be a primitive type in the JSON string but got " + data['auto_accident_will_require_therapy_rec']);
        }

        return true;
    }


}



/**
 * 
 * @member {String} auto_accident_case_number
 */
AutoAccidentInsurance.prototype['auto_accident_case_number'] = undefined;

/**
 * 
 * @member {String} auto_accident_claim_rep_address
 */
AutoAccidentInsurance.prototype['auto_accident_claim_rep_address'] = undefined;

/**
 * 
 * @member {String} auto_accident_claim_rep_city
 */
AutoAccidentInsurance.prototype['auto_accident_claim_rep_city'] = undefined;

/**
 * Is the insurer's claim representative the insurer?
 * @member {Boolean} auto_accident_claim_rep_is_insurer
 */
AutoAccidentInsurance.prototype['auto_accident_claim_rep_is_insurer'] = undefined;

/**
 * 
 * @member {String} auto_accident_claim_rep_name
 */
AutoAccidentInsurance.prototype['auto_accident_claim_rep_name'] = undefined;

/**
 * 
 * @member {module:model/AutoAccidentInsurance.AutoAccidentClaimRepStateEnum} auto_accident_claim_rep_state
 */
AutoAccidentInsurance.prototype['auto_accident_claim_rep_state'] = undefined;

/**
 * 
 * @member {String} auto_accident_claim_rep_zip
 */
AutoAccidentInsurance.prototype['auto_accident_claim_rep_zip'] = undefined;

/**
 * 
 * @member {String} auto_accident_company
 */
AutoAccidentInsurance.prototype['auto_accident_company'] = undefined;

/**
 * 
 * @member {String} auto_accident_date_of_accident
 */
AutoAccidentInsurance.prototype['auto_accident_date_of_accident'] = undefined;

/**
 * Patient was disabled (unable to work) from
 * @member {String} auto_accident_disabled_from_date
 */
AutoAccidentInsurance.prototype['auto_accident_disabled_from_date'] = undefined;

/**
 * Patient was disabled (unable to work) to
 * @member {String} auto_accident_disabled_to_date
 */
AutoAccidentInsurance.prototype['auto_accident_disabled_to_date'] = undefined;

/**
 * Has the patient had same or similar condition?
 * @member {Boolean} auto_accident_had_similar_condition
 */
AutoAccidentInsurance.prototype['auto_accident_had_similar_condition'] = undefined;

/**
 * True if the insurance policy is under patient's own name.
 * @member {Boolean} auto_accident_is_subscriber_the_patient
 */
AutoAccidentInsurance.prototype['auto_accident_is_subscriber_the_patient'] = undefined;

/**
 * 
 * @member {String} auto_accident_notes
 */
AutoAccidentInsurance.prototype['auto_accident_notes'] = undefined;

/**
 * 
 * @member {module:model/AutoAccidentInsurance.AutoAccidentPatientRelationshipToSubscriberEnum} auto_accident_patient_relationship_to_subscriber
 */
AutoAccidentInsurance.prototype['auto_accident_patient_relationship_to_subscriber'] = undefined;

/**
 * 
 * @member {String} auto_accident_payer_address
 */
AutoAccidentInsurance.prototype['auto_accident_payer_address'] = undefined;

/**
 * 
 * @member {String} auto_accident_payer_city
 */
AutoAccidentInsurance.prototype['auto_accident_payer_city'] = undefined;

/**
 * Auto Accident Payer ID
 * @member {String} auto_accident_payer_id
 */
AutoAccidentInsurance.prototype['auto_accident_payer_id'] = undefined;

/**
 * 
 * @member {module:model/AutoAccidentInsurance.AutoAccidentPayerStateEnum} auto_accident_payer_state
 */
AutoAccidentInsurance.prototype['auto_accident_payer_state'] = undefined;

/**
 * 
 * @member {String} auto_accident_payer_zip
 */
AutoAccidentInsurance.prototype['auto_accident_payer_zip'] = undefined;

/**
 * 
 * @member {String} auto_accident_policy_number
 */
AutoAccidentInsurance.prototype['auto_accident_policy_number'] = undefined;

/**
 * If still disabled, patient should be able to return to work on
 * @member {String} auto_accident_return_to_work_date
 */
AutoAccidentInsurance.prototype['auto_accident_return_to_work_date'] = undefined;

/**
 * 
 * @member {module:model/AutoAccidentInsurance.AutoAccidentSignificantInjuryEnum} auto_accident_significant_injury
 */
AutoAccidentInsurance.prototype['auto_accident_significant_injury'] = undefined;

/**
 * 
 * @member {String} auto_accident_significant_injury_notes
 */
AutoAccidentInsurance.prototype['auto_accident_significant_injury_notes'] = undefined;

/**
 * Date of same or similar condition
 * @member {String} auto_accident_similar_condition_date
 */
AutoAccidentInsurance.prototype['auto_accident_similar_condition_date'] = undefined;

/**
 * 
 * @member {String} auto_accident_similar_condition_notes
 */
AutoAccidentInsurance.prototype['auto_accident_similar_condition_notes'] = undefined;

/**
 * 
 * @member {module:model/AutoAccidentInsurance.AutoAccidentStateOfOccurrenceEnum} auto_accident_state_of_occurrence
 */
AutoAccidentInsurance.prototype['auto_accident_state_of_occurrence'] = undefined;

/**
 * Is patient still under your care for this condition?
 * @member {Boolean} auto_accident_still_under_care
 */
AutoAccidentInsurance.prototype['auto_accident_still_under_care'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_address
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_address'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_city
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_city'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_date_of_birth
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_date_of_birth'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_first_name
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_first_name'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_last_name
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_last_name'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_middle_name
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_middle_name'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_phone_number
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_phone_number'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_social_security
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_social_security'] = undefined;

/**
 * 
 * @member {module:model/AutoAccidentInsurance.AutoAccidentSubscriberStateEnum} auto_accident_subscriber_state
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_state'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_suffix
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_suffix'] = undefined;

/**
 * 
 * @member {String} auto_accident_subscriber_zip_code
 */
AutoAccidentInsurance.prototype['auto_accident_subscriber_zip_code'] = undefined;

/**
 * 
 * @member {String} auto_accident_treatment_duration
 */
AutoAccidentInsurance.prototype['auto_accident_treatment_duration'] = undefined;

/**
 * Will the patient require rehabilitation and/or occupational therapy as a result of the injuries sustained in this accident?
 * @member {Boolean} auto_accident_will_require_therapy
 */
AutoAccidentInsurance.prototype['auto_accident_will_require_therapy'] = undefined;

/**
 * 
 * @member {String} auto_accident_will_require_therapy_rec
 */
AutoAccidentInsurance.prototype['auto_accident_will_require_therapy_rec'] = undefined;





/**
 * Allowed values for the <code>auto_accident_claim_rep_state</code> property.
 * @enum {String}
 * @readonly
 */
AutoAccidentInsurance['AutoAccidentClaimRepStateEnum'] = {

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CT"
     * @const
     */
    "CT": "CT",

    /**
     * value: "DE"
     * @const
     */
    "DE": "DE",

    /**
     * value: "DC"
     * @const
     */
    "DC": "DC",

    /**
     * value: "FL"
     * @const
     */
    "FL": "FL",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "HI"
     * @const
     */
    "HI": "HI",

    /**
     * value: "ID"
     * @const
     */
    "ID": "ID",

    /**
     * value: "IL"
     * @const
     */
    "IL": "IL",

    /**
     * value: "IN"
     * @const
     */
    "IN": "IN",

    /**
     * value: "IA"
     * @const
     */
    "IA": "IA",

    /**
     * value: "KS"
     * @const
     */
    "KS": "KS",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "LA"
     * @const
     */
    "LA": "LA",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MD"
     * @const
     */
    "MD": "MD",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MI"
     * @const
     */
    "MI": "MI",

    /**
     * value: "MN"
     * @const
     */
    "MN": "MN",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "MO"
     * @const
     */
    "MO": "MO",

    /**
     * value: "MT"
     * @const
     */
    "MT": "MT",

    /**
     * value: "NE"
     * @const
     */
    "NE": "NE",

    /**
     * value: "NV"
     * @const
     */
    "NV": "NV",

    /**
     * value: "NH"
     * @const
     */
    "NH": "NH",

    /**
     * value: "NJ"
     * @const
     */
    "NJ": "NJ",

    /**
     * value: "NM"
     * @const
     */
    "NM": "NM",

    /**
     * value: "NY"
     * @const
     */
    "NY": "NY",

    /**
     * value: "NC"
     * @const
     */
    "NC": "NC",

    /**
     * value: "ND"
     * @const
     */
    "ND": "ND",

    /**
     * value: "MP"
     * @const
     */
    "MP": "MP",

    /**
     * value: "OH"
     * @const
     */
    "OH": "OH",

    /**
     * value: "OK"
     * @const
     */
    "OK": "OK",

    /**
     * value: "OR"
     * @const
     */
    "OR": "OR",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR",

    /**
     * value: "RI"
     * @const
     */
    "RI": "RI",

    /**
     * value: "SC"
     * @const
     */
    "SC": "SC",

    /**
     * value: "SD"
     * @const
     */
    "SD": "SD",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TX"
     * @const
     */
    "TX": "TX",

    /**
     * value: "UT"
     * @const
     */
    "UT": "UT",

    /**
     * value: "VT"
     * @const
     */
    "VT": "VT",

    /**
     * value: "VI"
     * @const
     */
    "VI": "VI",

    /**
     * value: "VA"
     * @const
     */
    "VA": "VA",

    /**
     * value: "WA"
     * @const
     */
    "WA": "WA",

    /**
     * value: "WV"
     * @const
     */
    "WV": "WV",

    /**
     * value: "WI"
     * @const
     */
    "WI": "WI",

    /**
     * value: "WY"
     * @const
     */
    "WY": "WY"
};


/**
 * Allowed values for the <code>auto_accident_patient_relationship_to_subscriber</code> property.
 * @enum {String}
 * @readonly
 */
AutoAccidentInsurance['AutoAccidentPatientRelationshipToSubscriberEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "01"
     * @const
     */
    "01": "01",

    /**
     * value: "04"
     * @const
     */
    "04": "04",

    /**
     * value: "05"
     * @const
     */
    "05": "05",

    /**
     * value: "07"
     * @const
     */
    "07": "07",

    /**
     * value: "10"
     * @const
     */
    "10": "10",

    /**
     * value: "15"
     * @const
     */
    "15": "15",

    /**
     * value: "17"
     * @const
     */
    "17": "17",

    /**
     * value: "19"
     * @const
     */
    "19": "19",

    /**
     * value: "20"
     * @const
     */
    "20": "20",

    /**
     * value: "21"
     * @const
     */
    "21": "21",

    /**
     * value: "22"
     * @const
     */
    "22": "22",

    /**
     * value: "23"
     * @const
     */
    "23": "23",

    /**
     * value: "24"
     * @const
     */
    "24": "24",

    /**
     * value: "29"
     * @const
     */
    "29": "29",

    /**
     * value: "32"
     * @const
     */
    "32": "32",

    /**
     * value: "33"
     * @const
     */
    "33": "33",

    /**
     * value: "36"
     * @const
     */
    "36": "36",

    /**
     * value: "39"
     * @const
     */
    "39": "39",

    /**
     * value: "40"
     * @const
     */
    "40": "40",

    /**
     * value: "41"
     * @const
     */
    "41": "41",

    /**
     * value: "43"
     * @const
     */
    "43": "43",

    /**
     * value: "53"
     * @const
     */
    "53": "53",

    /**
     * value: "76"
     * @const
     */
    "76": "76",

    /**
     * value: "G8"
     * @const
     */
    "G8": "G8"
};


/**
 * Allowed values for the <code>auto_accident_payer_state</code> property.
 * @enum {String}
 * @readonly
 */
AutoAccidentInsurance['AutoAccidentPayerStateEnum'] = {

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CT"
     * @const
     */
    "CT": "CT",

    /**
     * value: "DE"
     * @const
     */
    "DE": "DE",

    /**
     * value: "DC"
     * @const
     */
    "DC": "DC",

    /**
     * value: "FL"
     * @const
     */
    "FL": "FL",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "HI"
     * @const
     */
    "HI": "HI",

    /**
     * value: "ID"
     * @const
     */
    "ID": "ID",

    /**
     * value: "IL"
     * @const
     */
    "IL": "IL",

    /**
     * value: "IN"
     * @const
     */
    "IN": "IN",

    /**
     * value: "IA"
     * @const
     */
    "IA": "IA",

    /**
     * value: "KS"
     * @const
     */
    "KS": "KS",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "LA"
     * @const
     */
    "LA": "LA",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MD"
     * @const
     */
    "MD": "MD",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MI"
     * @const
     */
    "MI": "MI",

    /**
     * value: "MN"
     * @const
     */
    "MN": "MN",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "MO"
     * @const
     */
    "MO": "MO",

    /**
     * value: "MT"
     * @const
     */
    "MT": "MT",

    /**
     * value: "NE"
     * @const
     */
    "NE": "NE",

    /**
     * value: "NV"
     * @const
     */
    "NV": "NV",

    /**
     * value: "NH"
     * @const
     */
    "NH": "NH",

    /**
     * value: "NJ"
     * @const
     */
    "NJ": "NJ",

    /**
     * value: "NM"
     * @const
     */
    "NM": "NM",

    /**
     * value: "NY"
     * @const
     */
    "NY": "NY",

    /**
     * value: "NC"
     * @const
     */
    "NC": "NC",

    /**
     * value: "ND"
     * @const
     */
    "ND": "ND",

    /**
     * value: "MP"
     * @const
     */
    "MP": "MP",

    /**
     * value: "OH"
     * @const
     */
    "OH": "OH",

    /**
     * value: "OK"
     * @const
     */
    "OK": "OK",

    /**
     * value: "OR"
     * @const
     */
    "OR": "OR",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR",

    /**
     * value: "RI"
     * @const
     */
    "RI": "RI",

    /**
     * value: "SC"
     * @const
     */
    "SC": "SC",

    /**
     * value: "SD"
     * @const
     */
    "SD": "SD",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TX"
     * @const
     */
    "TX": "TX",

    /**
     * value: "UT"
     * @const
     */
    "UT": "UT",

    /**
     * value: "VT"
     * @const
     */
    "VT": "VT",

    /**
     * value: "VI"
     * @const
     */
    "VI": "VI",

    /**
     * value: "VA"
     * @const
     */
    "VA": "VA",

    /**
     * value: "WA"
     * @const
     */
    "WA": "WA",

    /**
     * value: "WV"
     * @const
     */
    "WV": "WV",

    /**
     * value: "WI"
     * @const
     */
    "WI": "WI",

    /**
     * value: "WY"
     * @const
     */
    "WY": "WY"
};


/**
 * Allowed values for the <code>auto_accident_significant_injury</code> property.
 * @enum {String}
 * @readonly
 */
AutoAccidentInsurance['AutoAccidentSignificantInjuryEnum'] = {

    /**
     * value: "true"
     * @const
     */
    "true": "true",

    /**
     * value: "false"
     * @const
     */
    "false": "false",

    /**
     * value: "N\\A"
     * @const
     */
    "N\A": "N\\A"
};


/**
 * Allowed values for the <code>auto_accident_state_of_occurrence</code> property.
 * @enum {String}
 * @readonly
 */
AutoAccidentInsurance['AutoAccidentStateOfOccurrenceEnum'] = {

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CT"
     * @const
     */
    "CT": "CT",

    /**
     * value: "DE"
     * @const
     */
    "DE": "DE",

    /**
     * value: "DC"
     * @const
     */
    "DC": "DC",

    /**
     * value: "FL"
     * @const
     */
    "FL": "FL",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "HI"
     * @const
     */
    "HI": "HI",

    /**
     * value: "ID"
     * @const
     */
    "ID": "ID",

    /**
     * value: "IL"
     * @const
     */
    "IL": "IL",

    /**
     * value: "IN"
     * @const
     */
    "IN": "IN",

    /**
     * value: "IA"
     * @const
     */
    "IA": "IA",

    /**
     * value: "KS"
     * @const
     */
    "KS": "KS",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "LA"
     * @const
     */
    "LA": "LA",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MD"
     * @const
     */
    "MD": "MD",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MI"
     * @const
     */
    "MI": "MI",

    /**
     * value: "MN"
     * @const
     */
    "MN": "MN",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "MO"
     * @const
     */
    "MO": "MO",

    /**
     * value: "MT"
     * @const
     */
    "MT": "MT",

    /**
     * value: "NE"
     * @const
     */
    "NE": "NE",

    /**
     * value: "NV"
     * @const
     */
    "NV": "NV",

    /**
     * value: "NH"
     * @const
     */
    "NH": "NH",

    /**
     * value: "NJ"
     * @const
     */
    "NJ": "NJ",

    /**
     * value: "NM"
     * @const
     */
    "NM": "NM",

    /**
     * value: "NY"
     * @const
     */
    "NY": "NY",

    /**
     * value: "NC"
     * @const
     */
    "NC": "NC",

    /**
     * value: "ND"
     * @const
     */
    "ND": "ND",

    /**
     * value: "MP"
     * @const
     */
    "MP": "MP",

    /**
     * value: "OH"
     * @const
     */
    "OH": "OH",

    /**
     * value: "OK"
     * @const
     */
    "OK": "OK",

    /**
     * value: "OR"
     * @const
     */
    "OR": "OR",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR",

    /**
     * value: "RI"
     * @const
     */
    "RI": "RI",

    /**
     * value: "SC"
     * @const
     */
    "SC": "SC",

    /**
     * value: "SD"
     * @const
     */
    "SD": "SD",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TX"
     * @const
     */
    "TX": "TX",

    /**
     * value: "UT"
     * @const
     */
    "UT": "UT",

    /**
     * value: "VT"
     * @const
     */
    "VT": "VT",

    /**
     * value: "VI"
     * @const
     */
    "VI": "VI",

    /**
     * value: "VA"
     * @const
     */
    "VA": "VA",

    /**
     * value: "WA"
     * @const
     */
    "WA": "WA",

    /**
     * value: "WV"
     * @const
     */
    "WV": "WV",

    /**
     * value: "WI"
     * @const
     */
    "WI": "WI",

    /**
     * value: "WY"
     * @const
     */
    "WY": "WY"
};


/**
 * Allowed values for the <code>auto_accident_subscriber_state</code> property.
 * @enum {String}
 * @readonly
 */
AutoAccidentInsurance['AutoAccidentSubscriberStateEnum'] = {

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CT"
     * @const
     */
    "CT": "CT",

    /**
     * value: "DE"
     * @const
     */
    "DE": "DE",

    /**
     * value: "DC"
     * @const
     */
    "DC": "DC",

    /**
     * value: "FL"
     * @const
     */
    "FL": "FL",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "HI"
     * @const
     */
    "HI": "HI",

    /**
     * value: "ID"
     * @const
     */
    "ID": "ID",

    /**
     * value: "IL"
     * @const
     */
    "IL": "IL",

    /**
     * value: "IN"
     * @const
     */
    "IN": "IN",

    /**
     * value: "IA"
     * @const
     */
    "IA": "IA",

    /**
     * value: "KS"
     * @const
     */
    "KS": "KS",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "LA"
     * @const
     */
    "LA": "LA",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MD"
     * @const
     */
    "MD": "MD",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MI"
     * @const
     */
    "MI": "MI",

    /**
     * value: "MN"
     * @const
     */
    "MN": "MN",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "MO"
     * @const
     */
    "MO": "MO",

    /**
     * value: "MT"
     * @const
     */
    "MT": "MT",

    /**
     * value: "NE"
     * @const
     */
    "NE": "NE",

    /**
     * value: "NV"
     * @const
     */
    "NV": "NV",

    /**
     * value: "NH"
     * @const
     */
    "NH": "NH",

    /**
     * value: "NJ"
     * @const
     */
    "NJ": "NJ",

    /**
     * value: "NM"
     * @const
     */
    "NM": "NM",

    /**
     * value: "NY"
     * @const
     */
    "NY": "NY",

    /**
     * value: "NC"
     * @const
     */
    "NC": "NC",

    /**
     * value: "ND"
     * @const
     */
    "ND": "ND",

    /**
     * value: "MP"
     * @const
     */
    "MP": "MP",

    /**
     * value: "OH"
     * @const
     */
    "OH": "OH",

    /**
     * value: "OK"
     * @const
     */
    "OK": "OK",

    /**
     * value: "OR"
     * @const
     */
    "OR": "OR",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR",

    /**
     * value: "RI"
     * @const
     */
    "RI": "RI",

    /**
     * value: "SC"
     * @const
     */
    "SC": "SC",

    /**
     * value: "SD"
     * @const
     */
    "SD": "SD",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TX"
     * @const
     */
    "TX": "TX",

    /**
     * value: "UT"
     * @const
     */
    "UT": "UT",

    /**
     * value: "VT"
     * @const
     */
    "VT": "VT",

    /**
     * value: "VI"
     * @const
     */
    "VI": "VI",

    /**
     * value: "VA"
     * @const
     */
    "VA": "VA",

    /**
     * value: "WA"
     * @const
     */
    "WA": "WA",

    /**
     * value: "WV"
     * @const
     */
    "WV": "WV",

    /**
     * value: "WI"
     * @const
     */
    "WI": "WI",

    /**
     * value: "WY"
     * @const
     */
    "WY": "WY"
};



export default AutoAccidentInsurance;

