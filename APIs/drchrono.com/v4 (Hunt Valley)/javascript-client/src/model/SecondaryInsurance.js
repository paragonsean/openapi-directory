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
 * The SecondaryInsurance model module.
 * @module model/SecondaryInsurance
 * @version v4 (Hunt Valley)
 */
class SecondaryInsurance {
    /**
     * Constructs a new <code>SecondaryInsurance</code>.
     * **Warning:** Changing insurance information may make past appointments unbillable. Insurance data is also **unvalidated**; you should use the [&#x60;/api/insurances&#x60;](#apiinsurances) endpoint to find the appropriate insurance payer.
     * @alias module:model/SecondaryInsurance
     */
    constructor() { 
        
        SecondaryInsurance.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SecondaryInsurance</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SecondaryInsurance} obj Optional instance to populate.
     * @return {module:model/SecondaryInsurance} The populated <code>SecondaryInsurance</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SecondaryInsurance();

            if (data.hasOwnProperty('insurance_claim_office_number')) {
                obj['insurance_claim_office_number'] = ApiClient.convertToType(data['insurance_claim_office_number'], 'String');
            }
            if (data.hasOwnProperty('insurance_company')) {
                obj['insurance_company'] = ApiClient.convertToType(data['insurance_company'], 'String');
            }
            if (data.hasOwnProperty('insurance_group_name')) {
                obj['insurance_group_name'] = ApiClient.convertToType(data['insurance_group_name'], 'String');
            }
            if (data.hasOwnProperty('insurance_group_number')) {
                obj['insurance_group_number'] = ApiClient.convertToType(data['insurance_group_number'], 'String');
            }
            if (data.hasOwnProperty('insurance_id_number')) {
                obj['insurance_id_number'] = ApiClient.convertToType(data['insurance_id_number'], 'String');
            }
            if (data.hasOwnProperty('insurance_payer_id')) {
                obj['insurance_payer_id'] = ApiClient.convertToType(data['insurance_payer_id'], 'String');
            }
            if (data.hasOwnProperty('insurance_plan_name')) {
                obj['insurance_plan_name'] = ApiClient.convertToType(data['insurance_plan_name'], 'String');
            }
            if (data.hasOwnProperty('insurance_plan_type')) {
                obj['insurance_plan_type'] = ApiClient.convertToType(data['insurance_plan_type'], 'String');
            }
            if (data.hasOwnProperty('is_subscriber_the_patient')) {
                obj['is_subscriber_the_patient'] = ApiClient.convertToType(data['is_subscriber_the_patient'], 'Boolean');
            }
            if (data.hasOwnProperty('patient_relationship_to_subscriber')) {
                obj['patient_relationship_to_subscriber'] = ApiClient.convertToType(data['patient_relationship_to_subscriber'], 'String');
            }
            if (data.hasOwnProperty('photo_back')) {
                obj['photo_back'] = ApiClient.convertToType(data['photo_back'], 'String');
            }
            if (data.hasOwnProperty('photo_front')) {
                obj['photo_front'] = ApiClient.convertToType(data['photo_front'], 'String');
            }
            if (data.hasOwnProperty('subscriber_address')) {
                obj['subscriber_address'] = ApiClient.convertToType(data['subscriber_address'], 'String');
            }
            if (data.hasOwnProperty('subscriber_city')) {
                obj['subscriber_city'] = ApiClient.convertToType(data['subscriber_city'], 'String');
            }
            if (data.hasOwnProperty('subscriber_country')) {
                obj['subscriber_country'] = ApiClient.convertToType(data['subscriber_country'], 'String');
            }
            if (data.hasOwnProperty('subscriber_date_of_birth')) {
                obj['subscriber_date_of_birth'] = ApiClient.convertToType(data['subscriber_date_of_birth'], 'String');
            }
            if (data.hasOwnProperty('subscriber_first_name')) {
                obj['subscriber_first_name'] = ApiClient.convertToType(data['subscriber_first_name'], 'String');
            }
            if (data.hasOwnProperty('subscriber_gender')) {
                obj['subscriber_gender'] = ApiClient.convertToType(data['subscriber_gender'], 'String');
            }
            if (data.hasOwnProperty('subscriber_last_name')) {
                obj['subscriber_last_name'] = ApiClient.convertToType(data['subscriber_last_name'], 'String');
            }
            if (data.hasOwnProperty('subscriber_middle_name')) {
                obj['subscriber_middle_name'] = ApiClient.convertToType(data['subscriber_middle_name'], 'String');
            }
            if (data.hasOwnProperty('subscriber_social_security')) {
                obj['subscriber_social_security'] = ApiClient.convertToType(data['subscriber_social_security'], 'String');
            }
            if (data.hasOwnProperty('subscriber_state')) {
                obj['subscriber_state'] = ApiClient.convertToType(data['subscriber_state'], 'String');
            }
            if (data.hasOwnProperty('subscriber_suffix')) {
                obj['subscriber_suffix'] = ApiClient.convertToType(data['subscriber_suffix'], 'String');
            }
            if (data.hasOwnProperty('subscriber_zip_code')) {
                obj['subscriber_zip_code'] = ApiClient.convertToType(data['subscriber_zip_code'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SecondaryInsurance</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SecondaryInsurance</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['insurance_claim_office_number'] && !(typeof data['insurance_claim_office_number'] === 'string' || data['insurance_claim_office_number'] instanceof String)) {
            throw new Error("Expected the field `insurance_claim_office_number` to be a primitive type in the JSON string but got " + data['insurance_claim_office_number']);
        }
        // ensure the json data is a string
        if (data['insurance_company'] && !(typeof data['insurance_company'] === 'string' || data['insurance_company'] instanceof String)) {
            throw new Error("Expected the field `insurance_company` to be a primitive type in the JSON string but got " + data['insurance_company']);
        }
        // ensure the json data is a string
        if (data['insurance_group_name'] && !(typeof data['insurance_group_name'] === 'string' || data['insurance_group_name'] instanceof String)) {
            throw new Error("Expected the field `insurance_group_name` to be a primitive type in the JSON string but got " + data['insurance_group_name']);
        }
        // ensure the json data is a string
        if (data['insurance_group_number'] && !(typeof data['insurance_group_number'] === 'string' || data['insurance_group_number'] instanceof String)) {
            throw new Error("Expected the field `insurance_group_number` to be a primitive type in the JSON string but got " + data['insurance_group_number']);
        }
        // ensure the json data is a string
        if (data['insurance_id_number'] && !(typeof data['insurance_id_number'] === 'string' || data['insurance_id_number'] instanceof String)) {
            throw new Error("Expected the field `insurance_id_number` to be a primitive type in the JSON string but got " + data['insurance_id_number']);
        }
        // ensure the json data is a string
        if (data['insurance_payer_id'] && !(typeof data['insurance_payer_id'] === 'string' || data['insurance_payer_id'] instanceof String)) {
            throw new Error("Expected the field `insurance_payer_id` to be a primitive type in the JSON string but got " + data['insurance_payer_id']);
        }
        // ensure the json data is a string
        if (data['insurance_plan_name'] && !(typeof data['insurance_plan_name'] === 'string' || data['insurance_plan_name'] instanceof String)) {
            throw new Error("Expected the field `insurance_plan_name` to be a primitive type in the JSON string but got " + data['insurance_plan_name']);
        }
        // ensure the json data is a string
        if (data['insurance_plan_type'] && !(typeof data['insurance_plan_type'] === 'string' || data['insurance_plan_type'] instanceof String)) {
            throw new Error("Expected the field `insurance_plan_type` to be a primitive type in the JSON string but got " + data['insurance_plan_type']);
        }
        // ensure the json data is a string
        if (data['patient_relationship_to_subscriber'] && !(typeof data['patient_relationship_to_subscriber'] === 'string' || data['patient_relationship_to_subscriber'] instanceof String)) {
            throw new Error("Expected the field `patient_relationship_to_subscriber` to be a primitive type in the JSON string but got " + data['patient_relationship_to_subscriber']);
        }
        // ensure the json data is a string
        if (data['photo_back'] && !(typeof data['photo_back'] === 'string' || data['photo_back'] instanceof String)) {
            throw new Error("Expected the field `photo_back` to be a primitive type in the JSON string but got " + data['photo_back']);
        }
        // ensure the json data is a string
        if (data['photo_front'] && !(typeof data['photo_front'] === 'string' || data['photo_front'] instanceof String)) {
            throw new Error("Expected the field `photo_front` to be a primitive type in the JSON string but got " + data['photo_front']);
        }
        // ensure the json data is a string
        if (data['subscriber_address'] && !(typeof data['subscriber_address'] === 'string' || data['subscriber_address'] instanceof String)) {
            throw new Error("Expected the field `subscriber_address` to be a primitive type in the JSON string but got " + data['subscriber_address']);
        }
        // ensure the json data is a string
        if (data['subscriber_city'] && !(typeof data['subscriber_city'] === 'string' || data['subscriber_city'] instanceof String)) {
            throw new Error("Expected the field `subscriber_city` to be a primitive type in the JSON string but got " + data['subscriber_city']);
        }
        // ensure the json data is a string
        if (data['subscriber_country'] && !(typeof data['subscriber_country'] === 'string' || data['subscriber_country'] instanceof String)) {
            throw new Error("Expected the field `subscriber_country` to be a primitive type in the JSON string but got " + data['subscriber_country']);
        }
        // ensure the json data is a string
        if (data['subscriber_date_of_birth'] && !(typeof data['subscriber_date_of_birth'] === 'string' || data['subscriber_date_of_birth'] instanceof String)) {
            throw new Error("Expected the field `subscriber_date_of_birth` to be a primitive type in the JSON string but got " + data['subscriber_date_of_birth']);
        }
        // ensure the json data is a string
        if (data['subscriber_first_name'] && !(typeof data['subscriber_first_name'] === 'string' || data['subscriber_first_name'] instanceof String)) {
            throw new Error("Expected the field `subscriber_first_name` to be a primitive type in the JSON string but got " + data['subscriber_first_name']);
        }
        // ensure the json data is a string
        if (data['subscriber_gender'] && !(typeof data['subscriber_gender'] === 'string' || data['subscriber_gender'] instanceof String)) {
            throw new Error("Expected the field `subscriber_gender` to be a primitive type in the JSON string but got " + data['subscriber_gender']);
        }
        // ensure the json data is a string
        if (data['subscriber_last_name'] && !(typeof data['subscriber_last_name'] === 'string' || data['subscriber_last_name'] instanceof String)) {
            throw new Error("Expected the field `subscriber_last_name` to be a primitive type in the JSON string but got " + data['subscriber_last_name']);
        }
        // ensure the json data is a string
        if (data['subscriber_middle_name'] && !(typeof data['subscriber_middle_name'] === 'string' || data['subscriber_middle_name'] instanceof String)) {
            throw new Error("Expected the field `subscriber_middle_name` to be a primitive type in the JSON string but got " + data['subscriber_middle_name']);
        }
        // ensure the json data is a string
        if (data['subscriber_social_security'] && !(typeof data['subscriber_social_security'] === 'string' || data['subscriber_social_security'] instanceof String)) {
            throw new Error("Expected the field `subscriber_social_security` to be a primitive type in the JSON string but got " + data['subscriber_social_security']);
        }
        // ensure the json data is a string
        if (data['subscriber_state'] && !(typeof data['subscriber_state'] === 'string' || data['subscriber_state'] instanceof String)) {
            throw new Error("Expected the field `subscriber_state` to be a primitive type in the JSON string but got " + data['subscriber_state']);
        }
        // ensure the json data is a string
        if (data['subscriber_suffix'] && !(typeof data['subscriber_suffix'] === 'string' || data['subscriber_suffix'] instanceof String)) {
            throw new Error("Expected the field `subscriber_suffix` to be a primitive type in the JSON string but got " + data['subscriber_suffix']);
        }
        // ensure the json data is a string
        if (data['subscriber_zip_code'] && !(typeof data['subscriber_zip_code'] === 'string' || data['subscriber_zip_code'] instanceof String)) {
            throw new Error("Expected the field `subscriber_zip_code` to be a primitive type in the JSON string but got " + data['subscriber_zip_code']);
        }

        return true;
    }


}



/**
 * Insurance office phone number
 * @member {String} insurance_claim_office_number
 */
SecondaryInsurance.prototype['insurance_claim_office_number'] = undefined;

/**
 * 
 * @member {String} insurance_company
 */
SecondaryInsurance.prototype['insurance_company'] = undefined;

/**
 * 
 * @member {String} insurance_group_name
 */
SecondaryInsurance.prototype['insurance_group_name'] = undefined;

/**
 * 
 * @member {String} insurance_group_number
 */
SecondaryInsurance.prototype['insurance_group_number'] = undefined;

/**
 * 
 * @member {String} insurance_id_number
 */
SecondaryInsurance.prototype['insurance_id_number'] = undefined;

/**
 * 
 * @member {String} insurance_payer_id
 */
SecondaryInsurance.prototype['insurance_payer_id'] = undefined;

/**
 * Name of insurance plan.
 * @member {String} insurance_plan_name
 */
SecondaryInsurance.prototype['insurance_plan_name'] = undefined;

/**
 * 
 * @member {module:model/SecondaryInsurance.InsurancePlanTypeEnum} insurance_plan_type
 */
SecondaryInsurance.prototype['insurance_plan_type'] = undefined;

/**
 * True if the insurance policy is under patient's own name. Defaults to true
 * @member {Boolean} is_subscriber_the_patient
 */
SecondaryInsurance.prototype['is_subscriber_the_patient'] = undefined;

/**
 * HCFA/1500 individual relationship code
 * @member {module:model/SecondaryInsurance.PatientRelationshipToSubscriberEnum} patient_relationship_to_subscriber
 */
SecondaryInsurance.prototype['patient_relationship_to_subscriber'] = undefined;

/**
 * Photo of back of insurance card
 * @member {String} photo_back
 */
SecondaryInsurance.prototype['photo_back'] = undefined;

/**
 * Photo of front of insurance card
 * @member {String} photo_front
 */
SecondaryInsurance.prototype['photo_front'] = undefined;

/**
 * 
 * @member {String} subscriber_address
 */
SecondaryInsurance.prototype['subscriber_address'] = undefined;

/**
 * 
 * @member {String} subscriber_city
 */
SecondaryInsurance.prototype['subscriber_city'] = undefined;

/**
 * Two-letter country code
 * @member {module:model/SecondaryInsurance.SubscriberCountryEnum} subscriber_country
 */
SecondaryInsurance.prototype['subscriber_country'] = undefined;

/**
 * 
 * @member {String} subscriber_date_of_birth
 */
SecondaryInsurance.prototype['subscriber_date_of_birth'] = undefined;

/**
 * 
 * @member {String} subscriber_first_name
 */
SecondaryInsurance.prototype['subscriber_first_name'] = undefined;

/**
 * One of `\"Male\"` or `\"Female\"`
 * @member {module:model/SecondaryInsurance.SubscriberGenderEnum} subscriber_gender
 */
SecondaryInsurance.prototype['subscriber_gender'] = undefined;

/**
 * 
 * @member {String} subscriber_last_name
 */
SecondaryInsurance.prototype['subscriber_last_name'] = undefined;

/**
 * 
 * @member {String} subscriber_middle_name
 */
SecondaryInsurance.prototype['subscriber_middle_name'] = undefined;

/**
 * 
 * @member {String} subscriber_social_security
 */
SecondaryInsurance.prototype['subscriber_social_security'] = undefined;

/**
 * Two-letter state code
 * @member {module:model/SecondaryInsurance.SubscriberStateEnum} subscriber_state
 */
SecondaryInsurance.prototype['subscriber_state'] = undefined;

/**
 * E.g. `\"II\"` or `\"III\"`
 * @member {String} subscriber_suffix
 */
SecondaryInsurance.prototype['subscriber_suffix'] = undefined;

/**
 * 
 * @member {String} subscriber_zip_code
 */
SecondaryInsurance.prototype['subscriber_zip_code'] = undefined;





/**
 * Allowed values for the <code>insurance_plan_type</code> property.
 * @enum {String}
 * @readonly
 */
SecondaryInsurance['InsurancePlanTypeEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "BL"
     * @const
     */
    "BL": "BL",

    /**
     * value: "CH"
     * @const
     */
    "CH": "CH",

    /**
     * value: "CI"
     * @const
     */
    "CI": "CI",

    /**
     * value: "17"
     * @const
     */
    "17": "17",

    /**
     * value: "DS"
     * @const
     */
    "DS": "DS",

    /**
     * value: "14"
     * @const
     */
    "14": "14",

    /**
     * value: "FI"
     * @const
     */
    "FI": "FI",

    /**
     * value: "HM"
     * @const
     */
    "HM": "HM",

    /**
     * value: "16"
     * @const
     */
    "16": "16",

    /**
     * value: "15"
     * @const
     */
    "15": "15",

    /**
     * value: "LM"
     * @const
     */
    "LM": "LM",

    /**
     * value: "MC"
     * @const
     */
    "MC": "MC",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MB"
     * @const
     */
    "MB": "MB",

    /**
     * value: "ZZ"
     * @const
     */
    "ZZ": "ZZ",

    /**
     * value: "OF"
     * @const
     */
    "OF": "OF",

    /**
     * value: "11"
     * @const
     */
    "11": "11",

    /**
     * value: "13"
     * @const
     */
    "13": "13",

    /**
     * value: "12"
     * @const
     */
    "12": "12",

    /**
     * value: "TV"
     * @const
     */
    "TV": "TV",

    /**
     * value: "VA"
     * @const
     */
    "VA": "VA",

    /**
     * value: "WC"
     * @const
     */
    "WC": "WC"
};


/**
 * Allowed values for the <code>patient_relationship_to_subscriber</code> property.
 * @enum {String}
 * @readonly
 */
SecondaryInsurance['PatientRelationshipToSubscriberEnum'] = {

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
 * Allowed values for the <code>subscriber_country</code> property.
 * @enum {String}
 * @readonly
 */
SecondaryInsurance['SubscriberCountryEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "AF"
     * @const
     */
    "AF": "AF",

    /**
     * value: "AX"
     * @const
     */
    "AX": "AX",

    /**
     * value: "AL"
     * @const
     */
    "AL": "AL",

    /**
     * value: "DZ"
     * @const
     */
    "DZ": "DZ",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AD"
     * @const
     */
    "AD": "AD",

    /**
     * value: "AO"
     * @const
     */
    "AO": "AO",

    /**
     * value: "AI"
     * @const
     */
    "AI": "AI",

    /**
     * value: "AQ"
     * @const
     */
    "AQ": "AQ",

    /**
     * value: "AG"
     * @const
     */
    "AG": "AG",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "AW"
     * @const
     */
    "AW": "AW",

    /**
     * value: "AU"
     * @const
     */
    "AU": "AU",

    /**
     * value: "AT"
     * @const
     */
    "AT": "AT",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "BS"
     * @const
     */
    "BS": "BS",

    /**
     * value: "BH"
     * @const
     */
    "BH": "BH",

    /**
     * value: "BD"
     * @const
     */
    "BD": "BD",

    /**
     * value: "BB"
     * @const
     */
    "BB": "BB",

    /**
     * value: "BY"
     * @const
     */
    "BY": "BY",

    /**
     * value: "BE"
     * @const
     */
    "BE": "BE",

    /**
     * value: "BZ"
     * @const
     */
    "BZ": "BZ",

    /**
     * value: "BJ"
     * @const
     */
    "BJ": "BJ",

    /**
     * value: "BM"
     * @const
     */
    "BM": "BM",

    /**
     * value: "BT"
     * @const
     */
    "BT": "BT",

    /**
     * value: "BO"
     * @const
     */
    "BO": "BO",

    /**
     * value: "BQ"
     * @const
     */
    "BQ": "BQ",

    /**
     * value: "BA"
     * @const
     */
    "BA": "BA",

    /**
     * value: "BW"
     * @const
     */
    "BW": "BW",

    /**
     * value: "BV"
     * @const
     */
    "BV": "BV",

    /**
     * value: "BR"
     * @const
     */
    "BR": "BR",

    /**
     * value: "IO"
     * @const
     */
    "IO": "IO",

    /**
     * value: "BN"
     * @const
     */
    "BN": "BN",

    /**
     * value: "BG"
     * @const
     */
    "BG": "BG",

    /**
     * value: "BF"
     * @const
     */
    "BF": "BF",

    /**
     * value: "BI"
     * @const
     */
    "BI": "BI",

    /**
     * value: "KH"
     * @const
     */
    "KH": "KH",

    /**
     * value: "CM"
     * @const
     */
    "CM": "CM",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CV"
     * @const
     */
    "CV": "CV",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "CF"
     * @const
     */
    "CF": "CF",

    /**
     * value: "TD"
     * @const
     */
    "TD": "TD",

    /**
     * value: "CL"
     * @const
     */
    "CL": "CL",

    /**
     * value: "CN"
     * @const
     */
    "CN": "CN",

    /**
     * value: "CX"
     * @const
     */
    "CX": "CX",

    /**
     * value: "CC"
     * @const
     */
    "CC": "CC",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "KM"
     * @const
     */
    "KM": "KM",

    /**
     * value: "CG"
     * @const
     */
    "CG": "CG",

    /**
     * value: "CD"
     * @const
     */
    "CD": "CD",

    /**
     * value: "CK"
     * @const
     */
    "CK": "CK",

    /**
     * value: "CR"
     * @const
     */
    "CR": "CR",

    /**
     * value: "CI"
     * @const
     */
    "CI": "CI",

    /**
     * value: "HR"
     * @const
     */
    "HR": "HR",

    /**
     * value: "CU"
     * @const
     */
    "CU": "CU",

    /**
     * value: "CW"
     * @const
     */
    "CW": "CW",

    /**
     * value: "CY"
     * @const
     */
    "CY": "CY",

    /**
     * value: "CZ"
     * @const
     */
    "CZ": "CZ",

    /**
     * value: "CYM"
     * @const
     */
    "CYM": "CYM",

    /**
     * value: "DK"
     * @const
     */
    "DK": "DK",

    /**
     * value: "DJ"
     * @const
     */
    "DJ": "DJ",

    /**
     * value: "DM"
     * @const
     */
    "DM": "DM",

    /**
     * value: "DO"
     * @const
     */
    "DO": "DO",

    /**
     * value: "EC"
     * @const
     */
    "EC": "EC",

    /**
     * value: "EG"
     * @const
     */
    "EG": "EG",

    /**
     * value: "SV"
     * @const
     */
    "SV": "SV",

    /**
     * value: "GQ"
     * @const
     */
    "GQ": "GQ",

    /**
     * value: "ER"
     * @const
     */
    "ER": "ER",

    /**
     * value: "EE"
     * @const
     */
    "EE": "EE",

    /**
     * value: "ET"
     * @const
     */
    "ET": "ET",

    /**
     * value: "FK"
     * @const
     */
    "FK": "FK",

    /**
     * value: "FO"
     * @const
     */
    "FO": "FO",

    /**
     * value: "FJ"
     * @const
     */
    "FJ": "FJ",

    /**
     * value: "FI"
     * @const
     */
    "FI": "FI",

    /**
     * value: "FR"
     * @const
     */
    "FR": "FR",

    /**
     * value: "GF"
     * @const
     */
    "GF": "GF",

    /**
     * value: "PF"
     * @const
     */
    "PF": "PF",

    /**
     * value: "TF"
     * @const
     */
    "TF": "TF",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GM"
     * @const
     */
    "GM": "GM",

    /**
     * value: "GE"
     * @const
     */
    "GE": "GE",

    /**
     * value: "DE"
     * @const
     */
    "DE": "DE",

    /**
     * value: "GH"
     * @const
     */
    "GH": "GH",

    /**
     * value: "GI"
     * @const
     */
    "GI": "GI",

    /**
     * value: "GR"
     * @const
     */
    "GR": "GR",

    /**
     * value: "GL"
     * @const
     */
    "GL": "GL",

    /**
     * value: "GD"
     * @const
     */
    "GD": "GD",

    /**
     * value: "GP"
     * @const
     */
    "GP": "GP",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "GT"
     * @const
     */
    "GT": "GT",

    /**
     * value: "GG"
     * @const
     */
    "GG": "GG",

    /**
     * value: "GN"
     * @const
     */
    "GN": "GN",

    /**
     * value: "GW"
     * @const
     */
    "GW": "GW",

    /**
     * value: "GY"
     * @const
     */
    "GY": "GY",

    /**
     * value: "HT"
     * @const
     */
    "HT": "HT",

    /**
     * value: "HM"
     * @const
     */
    "HM": "HM",

    /**
     * value: "VA"
     * @const
     */
    "VA": "VA",

    /**
     * value: "HN"
     * @const
     */
    "HN": "HN",

    /**
     * value: "HK"
     * @const
     */
    "HK": "HK",

    /**
     * value: "HU"
     * @const
     */
    "HU": "HU",

    /**
     * value: "IS"
     * @const
     */
    "IS": "IS",

    /**
     * value: "IN"
     * @const
     */
    "IN": "IN",

    /**
     * value: "ID"
     * @const
     */
    "ID": "ID",

    /**
     * value: "IR"
     * @const
     */
    "IR": "IR",

    /**
     * value: "IQ"
     * @const
     */
    "IQ": "IQ",

    /**
     * value: "IE"
     * @const
     */
    "IE": "IE",

    /**
     * value: "IM"
     * @const
     */
    "IM": "IM",

    /**
     * value: "IL"
     * @const
     */
    "IL": "IL",

    /**
     * value: "IT"
     * @const
     */
    "IT": "IT",

    /**
     * value: "JM"
     * @const
     */
    "JM": "JM",

    /**
     * value: "JP"
     * @const
     */
    "JP": "JP",

    /**
     * value: "JE"
     * @const
     */
    "JE": "JE",

    /**
     * value: "JO"
     * @const
     */
    "JO": "JO",

    /**
     * value: "KZ"
     * @const
     */
    "KZ": "KZ",

    /**
     * value: "KE"
     * @const
     */
    "KE": "KE",

    /**
     * value: "KI"
     * @const
     */
    "KI": "KI",

    /**
     * value: "KP"
     * @const
     */
    "KP": "KP",

    /**
     * value: "KR"
     * @const
     */
    "KR": "KR",

    /**
     * value: "XK"
     * @const
     */
    "XK": "XK",

    /**
     * value: "KW"
     * @const
     */
    "KW": "KW",

    /**
     * value: "KG"
     * @const
     */
    "KG": "KG",

    /**
     * value: "LA"
     * @const
     */
    "LA": "LA",

    /**
     * value: "LV"
     * @const
     */
    "LV": "LV",

    /**
     * value: "LB"
     * @const
     */
    "LB": "LB",

    /**
     * value: "LS"
     * @const
     */
    "LS": "LS",

    /**
     * value: "LR"
     * @const
     */
    "LR": "LR",

    /**
     * value: "LY"
     * @const
     */
    "LY": "LY",

    /**
     * value: "LI"
     * @const
     */
    "LI": "LI",

    /**
     * value: "LT"
     * @const
     */
    "LT": "LT",

    /**
     * value: "LU"
     * @const
     */
    "LU": "LU",

    /**
     * value: "MO"
     * @const
     */
    "MO": "MO",

    /**
     * value: "MK"
     * @const
     */
    "MK": "MK",

    /**
     * value: "MG"
     * @const
     */
    "MG": "MG",

    /**
     * value: "MW"
     * @const
     */
    "MW": "MW",

    /**
     * value: "MY"
     * @const
     */
    "MY": "MY",

    /**
     * value: "MV"
     * @const
     */
    "MV": "MV",

    /**
     * value: "ML"
     * @const
     */
    "ML": "ML",

    /**
     * value: "MT"
     * @const
     */
    "MT": "MT",

    /**
     * value: "MH"
     * @const
     */
    "MH": "MH",

    /**
     * value: "MQ"
     * @const
     */
    "MQ": "MQ",

    /**
     * value: "MR"
     * @const
     */
    "MR": "MR",

    /**
     * value: "MU"
     * @const
     */
    "MU": "MU",

    /**
     * value: "YT"
     * @const
     */
    "YT": "YT",

    /**
     * value: "MX"
     * @const
     */
    "MX": "MX",

    /**
     * value: "FM"
     * @const
     */
    "FM": "FM",

    /**
     * value: "MD"
     * @const
     */
    "MD": "MD",

    /**
     * value: "MC"
     * @const
     */
    "MC": "MC",

    /**
     * value: "MN"
     * @const
     */
    "MN": "MN",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "MA"
     * @const
     */
    "MA": "MA",

    /**
     * value: "MZ"
     * @const
     */
    "MZ": "MZ",

    /**
     * value: "MM"
     * @const
     */
    "MM": "MM",

    /**
     * value: "NA"
     * @const
     */
    "NA": "NA",

    /**
     * value: "NR"
     * @const
     */
    "NR": "NR",

    /**
     * value: "NP"
     * @const
     */
    "NP": "NP",

    /**
     * value: "NL"
     * @const
     */
    "NL": "NL",

    /**
     * value: "NC"
     * @const
     */
    "NC": "NC",

    /**
     * value: "NZ"
     * @const
     */
    "NZ": "NZ",

    /**
     * value: "NI"
     * @const
     */
    "NI": "NI",

    /**
     * value: "NE"
     * @const
     */
    "NE": "NE",

    /**
     * value: "NG"
     * @const
     */
    "NG": "NG",

    /**
     * value: "NU"
     * @const
     */
    "NU": "NU",

    /**
     * value: "NF"
     * @const
     */
    "NF": "NF",

    /**
     * value: "MP"
     * @const
     */
    "MP": "MP",

    /**
     * value: "false"
     * @const
     */
    "false": "false",

    /**
     * value: "OM"
     * @const
     */
    "OM": "OM",

    /**
     * value: "PK"
     * @const
     */
    "PK": "PK",

    /**
     * value: "PW"
     * @const
     */
    "PW": "PW",

    /**
     * value: "PS"
     * @const
     */
    "PS": "PS",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PG"
     * @const
     */
    "PG": "PG",

    /**
     * value: "PY"
     * @const
     */
    "PY": "PY",

    /**
     * value: "PE"
     * @const
     */
    "PE": "PE",

    /**
     * value: "PH"
     * @const
     */
    "PH": "PH",

    /**
     * value: "PN"
     * @const
     */
    "PN": "PN",

    /**
     * value: "PL"
     * @const
     */
    "PL": "PL",

    /**
     * value: "PT"
     * @const
     */
    "PT": "PT",

    /**
     * value: "PR"
     * @const
     */
    "PR": "PR",

    /**
     * value: "QA"
     * @const
     */
    "QA": "QA",

    /**
     * value: "RE"
     * @const
     */
    "RE": "RE",

    /**
     * value: "RO"
     * @const
     */
    "RO": "RO",

    /**
     * value: "RU"
     * @const
     */
    "RU": "RU",

    /**
     * value: "RW"
     * @const
     */
    "RW": "RW",

    /**
     * value: "BL"
     * @const
     */
    "BL": "BL",

    /**
     * value: "SH"
     * @const
     */
    "SH": "SH",

    /**
     * value: "KN"
     * @const
     */
    "KN": "KN",

    /**
     * value: "LC"
     * @const
     */
    "LC": "LC",

    /**
     * value: "MF"
     * @const
     */
    "MF": "MF",

    /**
     * value: "PM"
     * @const
     */
    "PM": "PM",

    /**
     * value: "VC"
     * @const
     */
    "VC": "VC",

    /**
     * value: "WS"
     * @const
     */
    "WS": "WS",

    /**
     * value: "SM"
     * @const
     */
    "SM": "SM",

    /**
     * value: "ST"
     * @const
     */
    "ST": "ST",

    /**
     * value: "SA"
     * @const
     */
    "SA": "SA",

    /**
     * value: "SN"
     * @const
     */
    "SN": "SN",

    /**
     * value: "RS"
     * @const
     */
    "RS": "RS",

    /**
     * value: "SC"
     * @const
     */
    "SC": "SC",

    /**
     * value: "SL"
     * @const
     */
    "SL": "SL",

    /**
     * value: "SG"
     * @const
     */
    "SG": "SG",

    /**
     * value: "SX"
     * @const
     */
    "SX": "SX",

    /**
     * value: "SK"
     * @const
     */
    "SK": "SK",

    /**
     * value: "SI"
     * @const
     */
    "SI": "SI",

    /**
     * value: "SB"
     * @const
     */
    "SB": "SB",

    /**
     * value: "SO"
     * @const
     */
    "SO": "SO",

    /**
     * value: "ZA"
     * @const
     */
    "ZA": "ZA",

    /**
     * value: "GS"
     * @const
     */
    "GS": "GS",

    /**
     * value: "SS"
     * @const
     */
    "SS": "SS",

    /**
     * value: "ES"
     * @const
     */
    "ES": "ES",

    /**
     * value: "LK"
     * @const
     */
    "LK": "LK",

    /**
     * value: "SD"
     * @const
     */
    "SD": "SD",

    /**
     * value: "SR"
     * @const
     */
    "SR": "SR",

    /**
     * value: "SJ"
     * @const
     */
    "SJ": "SJ",

    /**
     * value: "SZ"
     * @const
     */
    "SZ": "SZ",

    /**
     * value: "SE"
     * @const
     */
    "SE": "SE",

    /**
     * value: "CH"
     * @const
     */
    "CH": "CH",

    /**
     * value: "SY"
     * @const
     */
    "SY": "SY",

    /**
     * value: "TW"
     * @const
     */
    "TW": "TW",

    /**
     * value: "TJ"
     * @const
     */
    "TJ": "TJ",

    /**
     * value: "TZ"
     * @const
     */
    "TZ": "TZ",

    /**
     * value: "TH"
     * @const
     */
    "TH": "TH",

    /**
     * value: "TL"
     * @const
     */
    "TL": "TL",

    /**
     * value: "TG"
     * @const
     */
    "TG": "TG",

    /**
     * value: "TK"
     * @const
     */
    "TK": "TK",

    /**
     * value: "TO"
     * @const
     */
    "TO": "TO",

    /**
     * value: "TT"
     * @const
     */
    "TT": "TT",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TR"
     * @const
     */
    "TR": "TR",

    /**
     * value: "TM"
     * @const
     */
    "TM": "TM",

    /**
     * value: "TC"
     * @const
     */
    "TC": "TC",

    /**
     * value: "TV"
     * @const
     */
    "TV": "TV",

    /**
     * value: "UG"
     * @const
     */
    "UG": "UG",

    /**
     * value: "UA"
     * @const
     */
    "UA": "UA",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "GB"
     * @const
     */
    "GB": "GB",

    /**
     * value: "US"
     * @const
     */
    "US": "US",

    /**
     * value: "UM"
     * @const
     */
    "UM": "UM",

    /**
     * value: "UY"
     * @const
     */
    "UY": "UY",

    /**
     * value: "UZ"
     * @const
     */
    "UZ": "UZ",

    /**
     * value: "VU"
     * @const
     */
    "VU": "VU",

    /**
     * value: "VE"
     * @const
     */
    "VE": "VE",

    /**
     * value: "VN"
     * @const
     */
    "VN": "VN",

    /**
     * value: "VG"
     * @const
     */
    "VG": "VG",

    /**
     * value: "VI"
     * @const
     */
    "VI": "VI",

    /**
     * value: "WF"
     * @const
     */
    "WF": "WF",

    /**
     * value: "EH"
     * @const
     */
    "EH": "EH",

    /**
     * value: "YE"
     * @const
     */
    "YE": "YE",

    /**
     * value: "ZM"
     * @const
     */
    "ZM": "ZM",

    /**
     * value: "ZW"
     * @const
     */
    "ZW": "ZW"
};


/**
 * Allowed values for the <code>subscriber_gender</code> property.
 * @enum {String}
 * @readonly
 */
SecondaryInsurance['SubscriberGenderEnum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "Male"
     * @const
     */
    "Male": "Male",

    /**
     * value: "Female"
     * @const
     */
    "Female": "Female",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other",

    /**
     * value: "UNK"
     * @const
     */
    "UNK": "UNK",

    /**
     * value: "ASKU"
     * @const
     */
    "ASKU": "ASKU"
};


/**
 * Allowed values for the <code>subscriber_state</code> property.
 * @enum {String}
 * @readonly
 */
SecondaryInsurance['SubscriberStateEnum'] = {

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



export default SecondaryInsurance;

