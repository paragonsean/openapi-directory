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
 * The DoctorFeeSchedule model module.
 * @module model/DoctorFeeSchedule
 * @version v4 (Hunt Valley)
 */
class DoctorFeeSchedule {
    /**
     * Constructs a new <code>DoctorFeeSchedule</code>.
     * @alias module:model/DoctorFeeSchedule
     */
    constructor() { 
        
        DoctorFeeSchedule.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DoctorFeeSchedule</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DoctorFeeSchedule} obj Optional instance to populate.
     * @return {module:model/DoctorFeeSchedule} The populated <code>DoctorFeeSchedule</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DoctorFeeSchedule();

            if (data.hasOwnProperty('allowed_amount')) {
                obj['allowed_amount'] = ApiClient.convertToType(data['allowed_amount'], 'Number');
            }
            if (data.hasOwnProperty('base_price')) {
                obj['base_price'] = ApiClient.convertToType(data['base_price'], 'Number');
            }
            if (data.hasOwnProperty('billing_description')) {
                obj['billing_description'] = ApiClient.convertToType(data['billing_description'], 'String');
            }
            if (data.hasOwnProperty('cash_price')) {
                obj['cash_price'] = ApiClient.convertToType(data['cash_price'], 'Number');
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('code_type')) {
                obj['code_type'] = ApiClient.convertToType(data['code_type'], 'String');
            }
            if (data.hasOwnProperty('cpt_hcpcs_modifier1')) {
                obj['cpt_hcpcs_modifier1'] = ApiClient.convertToType(data['cpt_hcpcs_modifier1'], 'String');
            }
            if (data.hasOwnProperty('cpt_hcpcs_modifier2')) {
                obj['cpt_hcpcs_modifier2'] = ApiClient.convertToType(data['cpt_hcpcs_modifier2'], 'String');
            }
            if (data.hasOwnProperty('cpt_hcpcs_modifier3')) {
                obj['cpt_hcpcs_modifier3'] = ApiClient.convertToType(data['cpt_hcpcs_modifier3'], 'String');
            }
            if (data.hasOwnProperty('cpt_hcpcs_modifier4')) {
                obj['cpt_hcpcs_modifier4'] = ApiClient.convertToType(data['cpt_hcpcs_modifier4'], 'String');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('doctor')) {
                obj['doctor'] = ApiClient.convertToType(data['doctor'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('insured_out_of_network_price')) {
                obj['insured_out_of_network_price'] = ApiClient.convertToType(data['insured_out_of_network_price'], 'Number');
            }
            if (data.hasOwnProperty('insured_price')) {
                obj['insured_price'] = ApiClient.convertToType(data['insured_price'], 'Number');
            }
            if (data.hasOwnProperty('ndc_code')) {
                obj['ndc_code'] = ApiClient.convertToType(data['ndc_code'], 'String');
            }
            if (data.hasOwnProperty('ndc_quantity')) {
                obj['ndc_quantity'] = ApiClient.convertToType(data['ndc_quantity'], 'Number');
            }
            if (data.hasOwnProperty('ndc_units')) {
                obj['ndc_units'] = ApiClient.convertToType(data['ndc_units'], 'String');
            }
            if (data.hasOwnProperty('office')) {
                obj['office'] = ApiClient.convertToType(data['office'], 'Number');
            }
            if (data.hasOwnProperty('payer_id')) {
                obj['payer_id'] = ApiClient.convertToType(data['payer_id'], 'String');
            }
            if (data.hasOwnProperty('picklist_category')) {
                obj['picklist_category'] = ApiClient.convertToType(data['picklist_category'], 'String');
            }
            if (data.hasOwnProperty('plan_name')) {
                obj['plan_name'] = ApiClient.convertToType(data['plan_name'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DoctorFeeSchedule</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DoctorFeeSchedule</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['billing_description'] && !(typeof data['billing_description'] === 'string' || data['billing_description'] instanceof String)) {
            throw new Error("Expected the field `billing_description` to be a primitive type in the JSON string but got " + data['billing_description']);
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['code_type'] && !(typeof data['code_type'] === 'string' || data['code_type'] instanceof String)) {
            throw new Error("Expected the field `code_type` to be a primitive type in the JSON string but got " + data['code_type']);
        }
        // ensure the json data is a string
        if (data['cpt_hcpcs_modifier1'] && !(typeof data['cpt_hcpcs_modifier1'] === 'string' || data['cpt_hcpcs_modifier1'] instanceof String)) {
            throw new Error("Expected the field `cpt_hcpcs_modifier1` to be a primitive type in the JSON string but got " + data['cpt_hcpcs_modifier1']);
        }
        // ensure the json data is a string
        if (data['cpt_hcpcs_modifier2'] && !(typeof data['cpt_hcpcs_modifier2'] === 'string' || data['cpt_hcpcs_modifier2'] instanceof String)) {
            throw new Error("Expected the field `cpt_hcpcs_modifier2` to be a primitive type in the JSON string but got " + data['cpt_hcpcs_modifier2']);
        }
        // ensure the json data is a string
        if (data['cpt_hcpcs_modifier3'] && !(typeof data['cpt_hcpcs_modifier3'] === 'string' || data['cpt_hcpcs_modifier3'] instanceof String)) {
            throw new Error("Expected the field `cpt_hcpcs_modifier3` to be a primitive type in the JSON string but got " + data['cpt_hcpcs_modifier3']);
        }
        // ensure the json data is a string
        if (data['cpt_hcpcs_modifier4'] && !(typeof data['cpt_hcpcs_modifier4'] === 'string' || data['cpt_hcpcs_modifier4'] instanceof String)) {
            throw new Error("Expected the field `cpt_hcpcs_modifier4` to be a primitive type in the JSON string but got " + data['cpt_hcpcs_modifier4']);
        }
        // ensure the json data is a string
        if (data['created_at'] && !(typeof data['created_at'] === 'string' || data['created_at'] instanceof String)) {
            throw new Error("Expected the field `created_at` to be a primitive type in the JSON string but got " + data['created_at']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['ndc_code'] && !(typeof data['ndc_code'] === 'string' || data['ndc_code'] instanceof String)) {
            throw new Error("Expected the field `ndc_code` to be a primitive type in the JSON string but got " + data['ndc_code']);
        }
        // ensure the json data is a string
        if (data['ndc_units'] && !(typeof data['ndc_units'] === 'string' || data['ndc_units'] instanceof String)) {
            throw new Error("Expected the field `ndc_units` to be a primitive type in the JSON string but got " + data['ndc_units']);
        }
        // ensure the json data is a string
        if (data['payer_id'] && !(typeof data['payer_id'] === 'string' || data['payer_id'] instanceof String)) {
            throw new Error("Expected the field `payer_id` to be a primitive type in the JSON string but got " + data['payer_id']);
        }
        // ensure the json data is a string
        if (data['picklist_category'] && !(typeof data['picklist_category'] === 'string' || data['picklist_category'] instanceof String)) {
            throw new Error("Expected the field `picklist_category` to be a primitive type in the JSON string but got " + data['picklist_category']);
        }
        // ensure the json data is a string
        if (data['plan_name'] && !(typeof data['plan_name'] === 'string' || data['plan_name'] instanceof String)) {
            throw new Error("Expected the field `plan_name` to be a primitive type in the JSON string but got " + data['plan_name']);
        }
        // ensure the json data is a string
        if (data['updated_at'] && !(typeof data['updated_at'] === 'string' || data['updated_at'] instanceof String)) {
            throw new Error("Expected the field `updated_at` to be a primitive type in the JSON string but got " + data['updated_at']);
        }

        return true;
    }


}



/**
 * Typical allowed amount for payer. Not used if blank.
 * @member {Number} allowed_amount
 */
DoctorFeeSchedule.prototype['allowed_amount'] = undefined;

/**
 * 
 * @member {Number} base_price
 */
DoctorFeeSchedule.prototype['base_price'] = undefined;

/**
 * 
 * @member {String} billing_description
 */
DoctorFeeSchedule.prototype['billing_description'] = undefined;

/**
 * 
 * @member {Number} cash_price
 */
DoctorFeeSchedule.prototype['cash_price'] = undefined;

/**
 * 
 * @member {String} code
 */
DoctorFeeSchedule.prototype['code'] = undefined;

/**
 * 
 * @member {module:model/DoctorFeeSchedule.CodeTypeEnum} code_type
 */
DoctorFeeSchedule.prototype['code_type'] = undefined;

/**
 * 
 * @member {String} cpt_hcpcs_modifier1
 */
DoctorFeeSchedule.prototype['cpt_hcpcs_modifier1'] = undefined;

/**
 * 
 * @member {module:model/DoctorFeeSchedule.CptHcpcsModifier2Enum} cpt_hcpcs_modifier2
 */
DoctorFeeSchedule.prototype['cpt_hcpcs_modifier2'] = undefined;

/**
 * 
 * @member {module:model/DoctorFeeSchedule.CptHcpcsModifier3Enum} cpt_hcpcs_modifier3
 */
DoctorFeeSchedule.prototype['cpt_hcpcs_modifier3'] = undefined;

/**
 * 
 * @member {module:model/DoctorFeeSchedule.CptHcpcsModifier4Enum} cpt_hcpcs_modifier4
 */
DoctorFeeSchedule.prototype['cpt_hcpcs_modifier4'] = undefined;

/**
 * 
 * @member {String} created_at
 */
DoctorFeeSchedule.prototype['created_at'] = undefined;

/**
 * 
 * @member {String} description
 */
DoctorFeeSchedule.prototype['description'] = undefined;

/**
 * 
 * @member {Number} doctor
 */
DoctorFeeSchedule.prototype['doctor'] = undefined;

/**
 * 
 * @member {Number} id
 */
DoctorFeeSchedule.prototype['id'] = undefined;

/**
 * 
 * @member {Number} insured_out_of_network_price
 */
DoctorFeeSchedule.prototype['insured_out_of_network_price'] = undefined;

/**
 * 
 * @member {Number} insured_price
 */
DoctorFeeSchedule.prototype['insured_price'] = undefined;

/**
 * 
 * @member {String} ndc_code
 */
DoctorFeeSchedule.prototype['ndc_code'] = undefined;

/**
 * 
 * @member {Number} ndc_quantity
 */
DoctorFeeSchedule.prototype['ndc_quantity'] = undefined;

/**
 * 
 * @member {module:model/DoctorFeeSchedule.NdcUnitsEnum} ndc_units
 */
DoctorFeeSchedule.prototype['ndc_units'] = undefined;

/**
 * 
 * @member {Number} office
 */
DoctorFeeSchedule.prototype['office'] = undefined;

/**
 * Fee Schedule pricing specific to this payer, if null, then applies as default to all payers without a more specific fee schedule.
 * @member {String} payer_id
 */
DoctorFeeSchedule.prototype['payer_id'] = undefined;

/**
 * Optional: Category to organize the code into.
 * @member {String} picklist_category
 */
DoctorFeeSchedule.prototype['picklist_category'] = undefined;

/**
 * Name of insurance plan.
 * @member {String} plan_name
 */
DoctorFeeSchedule.prototype['plan_name'] = undefined;

/**
 * 
 * @member {String} updated_at
 */
DoctorFeeSchedule.prototype['updated_at'] = undefined;





/**
 * Allowed values for the <code>code_type</code> property.
 * @enum {String}
 * @readonly
 */
DoctorFeeSchedule['CodeTypeEnum'] = {

    /**
     * value: "CPT"
     * @const
     */
    "CPT": "CPT",

    /**
     * value: "HCPCS"
     * @const
     */
    "HCPCS": "HCPCS",

    /**
     * value: "Custom"
     * @const
     */
    "Custom": "Custom",

    /**
     * value: "ICD9"
     * @const
     */
    "ICD9": "ICD9",

    /**
     * value: "ICD10"
     * @const
     */
    "ICD10": "ICD10",

    /**
     * value: "Revenue"
     * @const
     */
    "Revenue": "Revenue"
};


/**
 * Allowed values for the <code>cpt_hcpcs_modifier2</code> property.
 * @enum {String}
 * @readonly
 */
DoctorFeeSchedule['CptHcpcsModifier2Enum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "17"
     * @const
     */
    "17": "17",

    /**
     * value: "1D"
     * @const
     */
    "1D": "1D",

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
     * value: "25"
     * @const
     */
    "25": "25",

    /**
     * value: "26"
     * @const
     */
    "26": "26",

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
     * value: "47"
     * @const
     */
    "47": "47",

    /**
     * value: "50"
     * @const
     */
    "50": "50",

    /**
     * value: "51"
     * @const
     */
    "51": "51",

    /**
     * value: "52"
     * @const
     */
    "52": "52",

    /**
     * value: "53"
     * @const
     */
    "53": "53",

    /**
     * value: "54"
     * @const
     */
    "54": "54",

    /**
     * value: "55"
     * @const
     */
    "55": "55",

    /**
     * value: "56"
     * @const
     */
    "56": "56",

    /**
     * value: "57"
     * @const
     */
    "57": "57",

    /**
     * value: "58"
     * @const
     */
    "58": "58",

    /**
     * value: "59"
     * @const
     */
    "59": "59",

    /**
     * value: "62"
     * @const
     */
    "62": "62",

    /**
     * value: "63"
     * @const
     */
    "63": "63",

    /**
     * value: "66"
     * @const
     */
    "66": "66",

    /**
     * value: "73"
     * @const
     */
    "73": "73",

    /**
     * value: "74"
     * @const
     */
    "74": "74",

    /**
     * value: "76"
     * @const
     */
    "76": "76",

    /**
     * value: "77"
     * @const
     */
    "77": "77",

    /**
     * value: "78"
     * @const
     */
    "78": "78",

    /**
     * value: "79"
     * @const
     */
    "79": "79",

    /**
     * value: "80"
     * @const
     */
    "80": "80",

    /**
     * value: "81"
     * @const
     */
    "81": "81",

    /**
     * value: "82"
     * @const
     */
    "82": "82",

    /**
     * value: "83"
     * @const
     */
    "83": "83",

    /**
     * value: "90"
     * @const
     */
    "90": "90",

    /**
     * value: "91"
     * @const
     */
    "91": "91",

    /**
     * value: "92"
     * @const
     */
    "92": "92",

    /**
     * value: "93"
     * @const
     */
    "93": "93",

    /**
     * value: "95"
     * @const
     */
    "95": "95",

    /**
     * value: "96"
     * @const
     */
    "96": "96",

    /**
     * value: "97"
     * @const
     */
    "97": "97",

    /**
     * value: "99"
     * @const
     */
    "99": "99",

    /**
     * value: "A1"
     * @const
     */
    "A1": "A1",

    /**
     * value: "A2"
     * @const
     */
    "A2": "A2",

    /**
     * value: "A3"
     * @const
     */
    "A3": "A3",

    /**
     * value: "A4"
     * @const
     */
    "A4": "A4",

    /**
     * value: "A5"
     * @const
     */
    "A5": "A5",

    /**
     * value: "A6"
     * @const
     */
    "A6": "A6",

    /**
     * value: "A7"
     * @const
     */
    "A7": "A7",

    /**
     * value: "A8"
     * @const
     */
    "A8": "A8",

    /**
     * value: "A9"
     * @const
     */
    "A9": "A9",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AD"
     * @const
     */
    "AD": "AD",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AF"
     * @const
     */
    "AF": "AF",

    /**
     * value: "AG"
     * @const
     */
    "AG": "AG",

    /**
     * value: "AH"
     * @const
     */
    "AH": "AH",

    /**
     * value: "AI"
     * @const
     */
    "AI": "AI",

    /**
     * value: "AJ"
     * @const
     */
    "AJ": "AJ",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "AO"
     * @const
     */
    "AO": "AO",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "AQ"
     * @const
     */
    "AQ": "AQ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AT"
     * @const
     */
    "AT": "AT",

    /**
     * value: "AU"
     * @const
     */
    "AU": "AU",

    /**
     * value: "AV"
     * @const
     */
    "AV": "AV",

    /**
     * value: "AW"
     * @const
     */
    "AW": "AW",

    /**
     * value: "AX"
     * @const
     */
    "AX": "AX",

    /**
     * value: "AY"
     * @const
     */
    "AY": "AY",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "BA"
     * @const
     */
    "BA": "BA",

    /**
     * value: "BL"
     * @const
     */
    "BL": "BL",

    /**
     * value: "BO"
     * @const
     */
    "BO": "BO",

    /**
     * value: "BP"
     * @const
     */
    "BP": "BP",

    /**
     * value: "BR"
     * @const
     */
    "BR": "BR",

    /**
     * value: "BU"
     * @const
     */
    "BU": "BU",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CB"
     * @const
     */
    "CB": "CB",

    /**
     * value: "CC"
     * @const
     */
    "CC": "CC",

    /**
     * value: "CD"
     * @const
     */
    "CD": "CD",

    /**
     * value: "CE"
     * @const
     */
    "CE": "CE",

    /**
     * value: "CF"
     * @const
     */
    "CF": "CF",

    /**
     * value: "CG"
     * @const
     */
    "CG": "CG",

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
     * value: "CJ"
     * @const
     */
    "CJ": "CJ",

    /**
     * value: "CK"
     * @const
     */
    "CK": "CK",

    /**
     * value: "CL"
     * @const
     */
    "CL": "CL",

    /**
     * value: "CM"
     * @const
     */
    "CM": "CM",

    /**
     * value: "CN"
     * @const
     */
    "CN": "CN",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CP"
     * @const
     */
    "CP": "CP",

    /**
     * value: "CQ"
     * @const
     */
    "CQ": "CQ",

    /**
     * value: "CR"
     * @const
     */
    "CR": "CR",

    /**
     * value: "CS"
     * @const
     */
    "CS": "CS",

    /**
     * value: "CT"
     * @const
     */
    "CT": "CT",

    /**
     * value: "DA"
     * @const
     */
    "DA": "DA",

    /**
     * value: "E1"
     * @const
     */
    "E1": "E1",

    /**
     * value: "E2"
     * @const
     */
    "E2": "E2",

    /**
     * value: "E3"
     * @const
     */
    "E3": "E3",

    /**
     * value: "E4"
     * @const
     */
    "E4": "E4",

    /**
     * value: "EA"
     * @const
     */
    "EA": "EA",

    /**
     * value: "EB"
     * @const
     */
    "EB": "EB",

    /**
     * value: "EC"
     * @const
     */
    "EC": "EC",

    /**
     * value: "ED"
     * @const
     */
    "ED": "ED",

    /**
     * value: "EE"
     * @const
     */
    "EE": "EE",

    /**
     * value: "EJ"
     * @const
     */
    "EJ": "EJ",

    /**
     * value: "EM"
     * @const
     */
    "EM": "EM",

    /**
     * value: "EP"
     * @const
     */
    "EP": "EP",

    /**
     * value: "ER"
     * @const
     */
    "ER": "ER",

    /**
     * value: "ET"
     * @const
     */
    "ET": "ET",

    /**
     * value: "EX"
     * @const
     */
    "EX": "EX",

    /**
     * value: "EY"
     * @const
     */
    "EY": "EY",

    /**
     * value: "F1"
     * @const
     */
    "F1": "F1",

    /**
     * value: "F2"
     * @const
     */
    "F2": "F2",

    /**
     * value: "F3"
     * @const
     */
    "F3": "F3",

    /**
     * value: "F4"
     * @const
     */
    "F4": "F4",

    /**
     * value: "F5"
     * @const
     */
    "F5": "F5",

    /**
     * value: "F6"
     * @const
     */
    "F6": "F6",

    /**
     * value: "F7"
     * @const
     */
    "F7": "F7",

    /**
     * value: "F8"
     * @const
     */
    "F8": "F8",

    /**
     * value: "F9"
     * @const
     */
    "F9": "F9",

    /**
     * value: "FA"
     * @const
     */
    "FA": "FA",

    /**
     * value: "FB"
     * @const
     */
    "FB": "FB",

    /**
     * value: "FC"
     * @const
     */
    "FC": "FC",

    /**
     * value: "FP"
     * @const
     */
    "FP": "FP",

    /**
     * value: "FX"
     * @const
     */
    "FX": "FX",

    /**
     * value: "FY"
     * @const
     */
    "FY": "FY",

    /**
     * value: "G0"
     * @const
     */
    "G0": "G0",

    /**
     * value: "G1"
     * @const
     */
    "G1": "G1",

    /**
     * value: "G2"
     * @const
     */
    "G2": "G2",

    /**
     * value: "G3"
     * @const
     */
    "G3": "G3",

    /**
     * value: "G4"
     * @const
     */
    "G4": "G4",

    /**
     * value: "G5"
     * @const
     */
    "G5": "G5",

    /**
     * value: "G6"
     * @const
     */
    "G6": "G6",

    /**
     * value: "G7"
     * @const
     */
    "G7": "G7",

    /**
     * value: "G8"
     * @const
     */
    "G8": "G8",

    /**
     * value: "G9"
     * @const
     */
    "G9": "G9",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GB"
     * @const
     */
    "GB": "GB",

    /**
     * value: "GC"
     * @const
     */
    "GC": "GC",

    /**
     * value: "GD"
     * @const
     */
    "GD": "GD",

    /**
     * value: "GE"
     * @const
     */
    "GE": "GE",

    /**
     * value: "GF"
     * @const
     */
    "GF": "GF",

    /**
     * value: "GG"
     * @const
     */
    "GG": "GG",

    /**
     * value: "GH"
     * @const
     */
    "GH": "GH",

    /**
     * value: "GJ"
     * @const
     */
    "GJ": "GJ",

    /**
     * value: "GK"
     * @const
     */
    "GK": "GK",

    /**
     * value: "GL"
     * @const
     */
    "GL": "GL",

    /**
     * value: "GM"
     * @const
     */
    "GM": "GM",

    /**
     * value: "GN"
     * @const
     */
    "GN": "GN",

    /**
     * value: "GO"
     * @const
     */
    "GO": "GO",

    /**
     * value: "GP"
     * @const
     */
    "GP": "GP",

    /**
     * value: "GQ"
     * @const
     */
    "GQ": "GQ",

    /**
     * value: "GR"
     * @const
     */
    "GR": "GR",

    /**
     * value: "GS"
     * @const
     */
    "GS": "GS",

    /**
     * value: "GT"
     * @const
     */
    "GT": "GT",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "GV"
     * @const
     */
    "GV": "GV",

    /**
     * value: "GW"
     * @const
     */
    "GW": "GW",

    /**
     * value: "GX"
     * @const
     */
    "GX": "GX",

    /**
     * value: "GY"
     * @const
     */
    "GY": "GY",

    /**
     * value: "GZ"
     * @const
     */
    "GZ": "GZ",

    /**
     * value: "H9"
     * @const
     */
    "H9": "H9",

    /**
     * value: "HA"
     * @const
     */
    "HA": "HA",

    /**
     * value: "HB"
     * @const
     */
    "HB": "HB",

    /**
     * value: "HC"
     * @const
     */
    "HC": "HC",

    /**
     * value: "HD"
     * @const
     */
    "HD": "HD",

    /**
     * value: "HE"
     * @const
     */
    "HE": "HE",

    /**
     * value: "HF"
     * @const
     */
    "HF": "HF",

    /**
     * value: "HG"
     * @const
     */
    "HG": "HG",

    /**
     * value: "HH"
     * @const
     */
    "HH": "HH",

    /**
     * value: "HI"
     * @const
     */
    "HI": "HI",

    /**
     * value: "HJ"
     * @const
     */
    "HJ": "HJ",

    /**
     * value: "HK"
     * @const
     */
    "HK": "HK",

    /**
     * value: "HL"
     * @const
     */
    "HL": "HL",

    /**
     * value: "HM"
     * @const
     */
    "HM": "HM",

    /**
     * value: "HN"
     * @const
     */
    "HN": "HN",

    /**
     * value: "HO"
     * @const
     */
    "HO": "HO",

    /**
     * value: "HP"
     * @const
     */
    "HP": "HP",

    /**
     * value: "HQ"
     * @const
     */
    "HQ": "HQ",

    /**
     * value: "HR"
     * @const
     */
    "HR": "HR",

    /**
     * value: "HS"
     * @const
     */
    "HS": "HS",

    /**
     * value: "HT"
     * @const
     */
    "HT": "HT",

    /**
     * value: "HU"
     * @const
     */
    "HU": "HU",

    /**
     * value: "HV"
     * @const
     */
    "HV": "HV",

    /**
     * value: "HW"
     * @const
     */
    "HW": "HW",

    /**
     * value: "HX"
     * @const
     */
    "HX": "HX",

    /**
     * value: "HY"
     * @const
     */
    "HY": "HY",

    /**
     * value: "HZ"
     * @const
     */
    "HZ": "HZ",

    /**
     * value: "J1"
     * @const
     */
    "J1": "J1",

    /**
     * value: "J2"
     * @const
     */
    "J2": "J2",

    /**
     * value: "J3"
     * @const
     */
    "J3": "J3",

    /**
     * value: "J4"
     * @const
     */
    "J4": "J4",

    /**
     * value: "JA"
     * @const
     */
    "JA": "JA",

    /**
     * value: "JB"
     * @const
     */
    "JB": "JB",

    /**
     * value: "JC"
     * @const
     */
    "JC": "JC",

    /**
     * value: "JD"
     * @const
     */
    "JD": "JD",

    /**
     * value: "JE"
     * @const
     */
    "JE": "JE",

    /**
     * value: "JF"
     * @const
     */
    "JF": "JF",

    /**
     * value: "JG"
     * @const
     */
    "JG": "JG",

    /**
     * value: "JW"
     * @const
     */
    "JW": "JW",

    /**
     * value: "K0"
     * @const
     */
    "K0": "K0",

    /**
     * value: "K1"
     * @const
     */
    "K1": "K1",

    /**
     * value: "K2"
     * @const
     */
    "K2": "K2",

    /**
     * value: "K3"
     * @const
     */
    "K3": "K3",

    /**
     * value: "K4"
     * @const
     */
    "K4": "K4",

    /**
     * value: "KA"
     * @const
     */
    "KA": "KA",

    /**
     * value: "KB"
     * @const
     */
    "KB": "KB",

    /**
     * value: "KC"
     * @const
     */
    "KC": "KC",

    /**
     * value: "KD"
     * @const
     */
    "KD": "KD",

    /**
     * value: "KE"
     * @const
     */
    "KE": "KE",

    /**
     * value: "KF"
     * @const
     */
    "KF": "KF",

    /**
     * value: "KG"
     * @const
     */
    "KG": "KG",

    /**
     * value: "KH"
     * @const
     */
    "KH": "KH",

    /**
     * value: "KI"
     * @const
     */
    "KI": "KI",

    /**
     * value: "KJ"
     * @const
     */
    "KJ": "KJ",

    /**
     * value: "KK"
     * @const
     */
    "KK": "KK",

    /**
     * value: "KL"
     * @const
     */
    "KL": "KL",

    /**
     * value: "KM"
     * @const
     */
    "KM": "KM",

    /**
     * value: "KN"
     * @const
     */
    "KN": "KN",

    /**
     * value: "KO"
     * @const
     */
    "KO": "KO",

    /**
     * value: "KP"
     * @const
     */
    "KP": "KP",

    /**
     * value: "KQ"
     * @const
     */
    "KQ": "KQ",

    /**
     * value: "KR"
     * @const
     */
    "KR": "KR",

    /**
     * value: "KS"
     * @const
     */
    "KS": "KS",

    /**
     * value: "KT"
     * @const
     */
    "KT": "KT",

    /**
     * value: "KU"
     * @const
     */
    "KU": "KU",

    /**
     * value: "KV"
     * @const
     */
    "KV": "KV",

    /**
     * value: "KW"
     * @const
     */
    "KW": "KW",

    /**
     * value: "KX"
     * @const
     */
    "KX": "KX",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "KZ"
     * @const
     */
    "KZ": "KZ",

    /**
     * value: "L1"
     * @const
     */
    "L1": "L1",

    /**
     * value: "LC"
     * @const
     */
    "LC": "LC",

    /**
     * value: "LD"
     * @const
     */
    "LD": "LD",

    /**
     * value: "LL"
     * @const
     */
    "LL": "LL",

    /**
     * value: "LM"
     * @const
     */
    "LM": "LM",

    /**
     * value: "LR"
     * @const
     */
    "LR": "LR",

    /**
     * value: "LS"
     * @const
     */
    "LS": "LS",

    /**
     * value: "LT"
     * @const
     */
    "LT": "LT",

    /**
     * value: "M2"
     * @const
     */
    "M2": "M2",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MI"
     * @const
     */
    "MI": "MI",

    /**
     * value: "MR"
     * @const
     */
    "MR": "MR",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "NB"
     * @const
     */
    "NB": "NB",

    /**
     * value: "NH"
     * @const
     */
    "NH": "NH",

    /**
     * value: "NM"
     * @const
     */
    "NM": "NM",

    /**
     * value: "NR"
     * @const
     */
    "NR": "NR",

    /**
     * value: "NU"
     * @const
     */
    "NU": "NU",

    /**
     * value: "P1"
     * @const
     */
    "P1": "P1",

    /**
     * value: "P2"
     * @const
     */
    "P2": "P2",

    /**
     * value: "P3"
     * @const
     */
    "P3": "P3",

    /**
     * value: "P4"
     * @const
     */
    "P4": "P4",

    /**
     * value: "P5"
     * @const
     */
    "P5": "P5",

    /**
     * value: "P6"
     * @const
     */
    "P6": "P6",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PB"
     * @const
     */
    "PB": "PB",

    /**
     * value: "PC"
     * @const
     */
    "PC": "PC",

    /**
     * value: "PD"
     * @const
     */
    "PD": "PD",

    /**
     * value: "PE"
     * @const
     */
    "PE": "PE",

    /**
     * value: "PI"
     * @const
     */
    "PI": "PI",

    /**
     * value: "PL"
     * @const
     */
    "PL": "PL",

    /**
     * value: "PM"
     * @const
     */
    "PM": "PM",

    /**
     * value: "PN"
     * @const
     */
    "PN": "PN",

    /**
     * value: "PO"
     * @const
     */
    "PO": "PO",

    /**
     * value: "PS"
     * @const
     */
    "PS": "PS",

    /**
     * value: "PT"
     * @const
     */
    "PT": "PT",

    /**
     * value: "Q0"
     * @const
     */
    "Q0": "Q0",

    /**
     * value: "Q1"
     * @const
     */
    "Q1": "Q1",

    /**
     * value: "Q2"
     * @const
     */
    "Q2": "Q2",

    /**
     * value: "Q3"
     * @const
     */
    "Q3": "Q3",

    /**
     * value: "Q4"
     * @const
     */
    "Q4": "Q4",

    /**
     * value: "Q5"
     * @const
     */
    "Q5": "Q5",

    /**
     * value: "Q6"
     * @const
     */
    "Q6": "Q6",

    /**
     * value: "Q7"
     * @const
     */
    "Q7": "Q7",

    /**
     * value: "Q8"
     * @const
     */
    "Q8": "Q8",

    /**
     * value: "Q9"
     * @const
     */
    "Q9": "Q9",

    /**
     * value: "QA"
     * @const
     */
    "QA": "QA",

    /**
     * value: "QB"
     * @const
     */
    "QB": "QB",

    /**
     * value: "QC"
     * @const
     */
    "QC": "QC",

    /**
     * value: "QD"
     * @const
     */
    "QD": "QD",

    /**
     * value: "QE"
     * @const
     */
    "QE": "QE",

    /**
     * value: "QF"
     * @const
     */
    "QF": "QF",

    /**
     * value: "QG"
     * @const
     */
    "QG": "QG",

    /**
     * value: "QH"
     * @const
     */
    "QH": "QH",

    /**
     * value: "QJ"
     * @const
     */
    "QJ": "QJ",

    /**
     * value: "QK"
     * @const
     */
    "QK": "QK",

    /**
     * value: "QL"
     * @const
     */
    "QL": "QL",

    /**
     * value: "QM"
     * @const
     */
    "QM": "QM",

    /**
     * value: "QN"
     * @const
     */
    "QN": "QN",

    /**
     * value: "QP"
     * @const
     */
    "QP": "QP",

    /**
     * value: "QQ"
     * @const
     */
    "QQ": "QQ",

    /**
     * value: "QR"
     * @const
     */
    "QR": "QR",

    /**
     * value: "QS"
     * @const
     */
    "QS": "QS",

    /**
     * value: "QT"
     * @const
     */
    "QT": "QT",

    /**
     * value: "QU"
     * @const
     */
    "QU": "QU",

    /**
     * value: "QV"
     * @const
     */
    "QV": "QV",

    /**
     * value: "QW"
     * @const
     */
    "QW": "QW",

    /**
     * value: "QX"
     * @const
     */
    "QX": "QX",

    /**
     * value: "QY"
     * @const
     */
    "QY": "QY",

    /**
     * value: "QZ"
     * @const
     */
    "QZ": "QZ",

    /**
     * value: "RA"
     * @const
     */
    "RA": "RA",

    /**
     * value: "RB"
     * @const
     */
    "RB": "RB",

    /**
     * value: "RC"
     * @const
     */
    "RC": "RC",

    /**
     * value: "RD"
     * @const
     */
    "RD": "RD",

    /**
     * value: "RE"
     * @const
     */
    "RE": "RE",

    /**
     * value: "RI"
     * @const
     */
    "RI": "RI",

    /**
     * value: "RP"
     * @const
     */
    "RP": "RP",

    /**
     * value: "RR"
     * @const
     */
    "RR": "RR",

    /**
     * value: "RT"
     * @const
     */
    "RT": "RT",

    /**
     * value: "SA"
     * @const
     */
    "SA": "SA",

    /**
     * value: "SB"
     * @const
     */
    "SB": "SB",

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
     * value: "SE"
     * @const
     */
    "SE": "SE",

    /**
     * value: "SF"
     * @const
     */
    "SF": "SF",

    /**
     * value: "SG"
     * @const
     */
    "SG": "SG",

    /**
     * value: "SH"
     * @const
     */
    "SH": "SH",

    /**
     * value: "SJ"
     * @const
     */
    "SJ": "SJ",

    /**
     * value: "SK"
     * @const
     */
    "SK": "SK",

    /**
     * value: "SL"
     * @const
     */
    "SL": "SL",

    /**
     * value: "SM"
     * @const
     */
    "SM": "SM",

    /**
     * value: "SN"
     * @const
     */
    "SN": "SN",

    /**
     * value: "SP"
     * @const
     */
    "SP": "SP",

    /**
     * value: "SQ"
     * @const
     */
    "SQ": "SQ",

    /**
     * value: "SS"
     * @const
     */
    "SS": "SS",

    /**
     * value: "ST"
     * @const
     */
    "ST": "ST",

    /**
     * value: "SU"
     * @const
     */
    "SU": "SU",

    /**
     * value: "SV"
     * @const
     */
    "SV": "SV",

    /**
     * value: "SW"
     * @const
     */
    "SW": "SW",

    /**
     * value: "SY"
     * @const
     */
    "SY": "SY",

    /**
     * value: "SZ"
     * @const
     */
    "SZ": "SZ",

    /**
     * value: "T1"
     * @const
     */
    "T1": "T1",

    /**
     * value: "T2"
     * @const
     */
    "T2": "T2",

    /**
     * value: "T3"
     * @const
     */
    "T3": "T3",

    /**
     * value: "T4"
     * @const
     */
    "T4": "T4",

    /**
     * value: "T5"
     * @const
     */
    "T5": "T5",

    /**
     * value: "T6"
     * @const
     */
    "T6": "T6",

    /**
     * value: "T7"
     * @const
     */
    "T7": "T7",

    /**
     * value: "T8"
     * @const
     */
    "T8": "T8",

    /**
     * value: "T9"
     * @const
     */
    "T9": "T9",

    /**
     * value: "TA"
     * @const
     */
    "TA": "TA",

    /**
     * value: "TB"
     * @const
     */
    "TB": "TB",

    /**
     * value: "TC"
     * @const
     */
    "TC": "TC",

    /**
     * value: "TD"
     * @const
     */
    "TD": "TD",

    /**
     * value: "TE"
     * @const
     */
    "TE": "TE",

    /**
     * value: "TF"
     * @const
     */
    "TF": "TF",

    /**
     * value: "TG"
     * @const
     */
    "TG": "TG",

    /**
     * value: "TH"
     * @const
     */
    "TH": "TH",

    /**
     * value: "TJ"
     * @const
     */
    "TJ": "TJ",

    /**
     * value: "TK"
     * @const
     */
    "TK": "TK",

    /**
     * value: "TL"
     * @const
     */
    "TL": "TL",

    /**
     * value: "TM"
     * @const
     */
    "TM": "TM",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TP"
     * @const
     */
    "TP": "TP",

    /**
     * value: "TQ"
     * @const
     */
    "TQ": "TQ",

    /**
     * value: "TR"
     * @const
     */
    "TR": "TR",

    /**
     * value: "TS"
     * @const
     */
    "TS": "TS",

    /**
     * value: "TT"
     * @const
     */
    "TT": "TT",

    /**
     * value: "TU"
     * @const
     */
    "TU": "TU",

    /**
     * value: "TV"
     * @const
     */
    "TV": "TV",

    /**
     * value: "TW"
     * @const
     */
    "TW": "TW",

    /**
     * value: "TX"
     * @const
     */
    "TX": "TX",

    /**
     * value: "U1"
     * @const
     */
    "U1": "U1",

    /**
     * value: "U2"
     * @const
     */
    "U2": "U2",

    /**
     * value: "U3"
     * @const
     */
    "U3": "U3",

    /**
     * value: "U4"
     * @const
     */
    "U4": "U4",

    /**
     * value: "U5"
     * @const
     */
    "U5": "U5",

    /**
     * value: "U6"
     * @const
     */
    "U6": "U6",

    /**
     * value: "U7"
     * @const
     */
    "U7": "U7",

    /**
     * value: "U8"
     * @const
     */
    "U8": "U8",

    /**
     * value: "U9"
     * @const
     */
    "U9": "U9",

    /**
     * value: "UA"
     * @const
     */
    "UA": "UA",

    /**
     * value: "UB"
     * @const
     */
    "UB": "UB",

    /**
     * value: "UC"
     * @const
     */
    "UC": "UC",

    /**
     * value: "UD"
     * @const
     */
    "UD": "UD",

    /**
     * value: "UE"
     * @const
     */
    "UE": "UE",

    /**
     * value: "UF"
     * @const
     */
    "UF": "UF",

    /**
     * value: "UG"
     * @const
     */
    "UG": "UG",

    /**
     * value: "UH"
     * @const
     */
    "UH": "UH",

    /**
     * value: "UJ"
     * @const
     */
    "UJ": "UJ",

    /**
     * value: "UK"
     * @const
     */
    "UK": "UK",

    /**
     * value: "UN"
     * @const
     */
    "UN": "UN",

    /**
     * value: "UP"
     * @const
     */
    "UP": "UP",

    /**
     * value: "UQ"
     * @const
     */
    "UQ": "UQ",

    /**
     * value: "UR"
     * @const
     */
    "UR": "UR",

    /**
     * value: "US"
     * @const
     */
    "US": "US",

    /**
     * value: "V1"
     * @const
     */
    "V1": "V1",

    /**
     * value: "V2"
     * @const
     */
    "V2": "V2",

    /**
     * value: "V3"
     * @const
     */
    "V3": "V3",

    /**
     * value: "V4"
     * @const
     */
    "V4": "V4",

    /**
     * value: "V5"
     * @const
     */
    "V5": "V5",

    /**
     * value: "V6"
     * @const
     */
    "V6": "V6",

    /**
     * value: "V7"
     * @const
     */
    "V7": "V7",

    /**
     * value: "V8"
     * @const
     */
    "V8": "V8",

    /**
     * value: "V9"
     * @const
     */
    "V9": "V9",

    /**
     * value: "VP"
     * @const
     */
    "VP": "VP",

    /**
     * value: "VR"
     * @const
     */
    "VR": "VR",

    /**
     * value: "W1"
     * @const
     */
    "W1": "W1",

    /**
     * value: "W5"
     * @const
     */
    "W5": "W5",

    /**
     * value: "W6"
     * @const
     */
    "W6": "W6",

    /**
     * value: "W7"
     * @const
     */
    "W7": "W7",

    /**
     * value: "W8"
     * @const
     */
    "W8": "W8",

    /**
     * value: "W9"
     * @const
     */
    "W9": "W9",

    /**
     * value: "WC"
     * @const
     */
    "WC": "WC",

    /**
     * value: "WH"
     * @const
     */
    "WH": "WH",

    /**
     * value: "WP"
     * @const
     */
    "WP": "WP",

    /**
     * value: "X1"
     * @const
     */
    "X1": "X1",

    /**
     * value: "X2"
     * @const
     */
    "X2": "X2",

    /**
     * value: "X3"
     * @const
     */
    "X3": "X3",

    /**
     * value: "X4"
     * @const
     */
    "X4": "X4",

    /**
     * value: "X5"
     * @const
     */
    "X5": "X5",

    /**
     * value: "XE"
     * @const
     */
    "XE": "XE",

    /**
     * value: "XP"
     * @const
     */
    "XP": "XP",

    /**
     * value: "XS"
     * @const
     */
    "XS": "XS",

    /**
     * value: "XU"
     * @const
     */
    "XU": "XU",

    /**
     * value: "VM"
     * @const
     */
    "VM": "VM",

    /**
     * value: "ZA"
     * @const
     */
    "ZA": "ZA",

    /**
     * value: "ZB"
     * @const
     */
    "ZB": "ZB",

    /**
     * value: "ZL"
     * @const
     */
    "ZL": "ZL",

    /**
     * value: "ZS"
     * @const
     */
    "ZS": "ZS",

    /**
     * value: "1P"
     * @const
     */
    "1P": "1P",

    /**
     * value: "2P"
     * @const
     */
    "2P": "2P",

    /**
     * value: "3P"
     * @const
     */
    "3P": "3P",

    /**
     * value: "8P"
     * @const
     */
    "8P": "8P"
};


/**
 * Allowed values for the <code>cpt_hcpcs_modifier3</code> property.
 * @enum {String}
 * @readonly
 */
DoctorFeeSchedule['CptHcpcsModifier3Enum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "17"
     * @const
     */
    "17": "17",

    /**
     * value: "1D"
     * @const
     */
    "1D": "1D",

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
     * value: "25"
     * @const
     */
    "25": "25",

    /**
     * value: "26"
     * @const
     */
    "26": "26",

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
     * value: "47"
     * @const
     */
    "47": "47",

    /**
     * value: "50"
     * @const
     */
    "50": "50",

    /**
     * value: "51"
     * @const
     */
    "51": "51",

    /**
     * value: "52"
     * @const
     */
    "52": "52",

    /**
     * value: "53"
     * @const
     */
    "53": "53",

    /**
     * value: "54"
     * @const
     */
    "54": "54",

    /**
     * value: "55"
     * @const
     */
    "55": "55",

    /**
     * value: "56"
     * @const
     */
    "56": "56",

    /**
     * value: "57"
     * @const
     */
    "57": "57",

    /**
     * value: "58"
     * @const
     */
    "58": "58",

    /**
     * value: "59"
     * @const
     */
    "59": "59",

    /**
     * value: "62"
     * @const
     */
    "62": "62",

    /**
     * value: "63"
     * @const
     */
    "63": "63",

    /**
     * value: "66"
     * @const
     */
    "66": "66",

    /**
     * value: "73"
     * @const
     */
    "73": "73",

    /**
     * value: "74"
     * @const
     */
    "74": "74",

    /**
     * value: "76"
     * @const
     */
    "76": "76",

    /**
     * value: "77"
     * @const
     */
    "77": "77",

    /**
     * value: "78"
     * @const
     */
    "78": "78",

    /**
     * value: "79"
     * @const
     */
    "79": "79",

    /**
     * value: "80"
     * @const
     */
    "80": "80",

    /**
     * value: "81"
     * @const
     */
    "81": "81",

    /**
     * value: "82"
     * @const
     */
    "82": "82",

    /**
     * value: "83"
     * @const
     */
    "83": "83",

    /**
     * value: "90"
     * @const
     */
    "90": "90",

    /**
     * value: "91"
     * @const
     */
    "91": "91",

    /**
     * value: "92"
     * @const
     */
    "92": "92",

    /**
     * value: "93"
     * @const
     */
    "93": "93",

    /**
     * value: "95"
     * @const
     */
    "95": "95",

    /**
     * value: "96"
     * @const
     */
    "96": "96",

    /**
     * value: "97"
     * @const
     */
    "97": "97",

    /**
     * value: "99"
     * @const
     */
    "99": "99",

    /**
     * value: "A1"
     * @const
     */
    "A1": "A1",

    /**
     * value: "A2"
     * @const
     */
    "A2": "A2",

    /**
     * value: "A3"
     * @const
     */
    "A3": "A3",

    /**
     * value: "A4"
     * @const
     */
    "A4": "A4",

    /**
     * value: "A5"
     * @const
     */
    "A5": "A5",

    /**
     * value: "A6"
     * @const
     */
    "A6": "A6",

    /**
     * value: "A7"
     * @const
     */
    "A7": "A7",

    /**
     * value: "A8"
     * @const
     */
    "A8": "A8",

    /**
     * value: "A9"
     * @const
     */
    "A9": "A9",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AD"
     * @const
     */
    "AD": "AD",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AF"
     * @const
     */
    "AF": "AF",

    /**
     * value: "AG"
     * @const
     */
    "AG": "AG",

    /**
     * value: "AH"
     * @const
     */
    "AH": "AH",

    /**
     * value: "AI"
     * @const
     */
    "AI": "AI",

    /**
     * value: "AJ"
     * @const
     */
    "AJ": "AJ",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "AO"
     * @const
     */
    "AO": "AO",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "AQ"
     * @const
     */
    "AQ": "AQ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AT"
     * @const
     */
    "AT": "AT",

    /**
     * value: "AU"
     * @const
     */
    "AU": "AU",

    /**
     * value: "AV"
     * @const
     */
    "AV": "AV",

    /**
     * value: "AW"
     * @const
     */
    "AW": "AW",

    /**
     * value: "AX"
     * @const
     */
    "AX": "AX",

    /**
     * value: "AY"
     * @const
     */
    "AY": "AY",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "BA"
     * @const
     */
    "BA": "BA",

    /**
     * value: "BL"
     * @const
     */
    "BL": "BL",

    /**
     * value: "BO"
     * @const
     */
    "BO": "BO",

    /**
     * value: "BP"
     * @const
     */
    "BP": "BP",

    /**
     * value: "BR"
     * @const
     */
    "BR": "BR",

    /**
     * value: "BU"
     * @const
     */
    "BU": "BU",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CB"
     * @const
     */
    "CB": "CB",

    /**
     * value: "CC"
     * @const
     */
    "CC": "CC",

    /**
     * value: "CD"
     * @const
     */
    "CD": "CD",

    /**
     * value: "CE"
     * @const
     */
    "CE": "CE",

    /**
     * value: "CF"
     * @const
     */
    "CF": "CF",

    /**
     * value: "CG"
     * @const
     */
    "CG": "CG",

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
     * value: "CJ"
     * @const
     */
    "CJ": "CJ",

    /**
     * value: "CK"
     * @const
     */
    "CK": "CK",

    /**
     * value: "CL"
     * @const
     */
    "CL": "CL",

    /**
     * value: "CM"
     * @const
     */
    "CM": "CM",

    /**
     * value: "CN"
     * @const
     */
    "CN": "CN",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CP"
     * @const
     */
    "CP": "CP",

    /**
     * value: "CQ"
     * @const
     */
    "CQ": "CQ",

    /**
     * value: "CR"
     * @const
     */
    "CR": "CR",

    /**
     * value: "CS"
     * @const
     */
    "CS": "CS",

    /**
     * value: "CT"
     * @const
     */
    "CT": "CT",

    /**
     * value: "DA"
     * @const
     */
    "DA": "DA",

    /**
     * value: "E1"
     * @const
     */
    "E1": "E1",

    /**
     * value: "E2"
     * @const
     */
    "E2": "E2",

    /**
     * value: "E3"
     * @const
     */
    "E3": "E3",

    /**
     * value: "E4"
     * @const
     */
    "E4": "E4",

    /**
     * value: "EA"
     * @const
     */
    "EA": "EA",

    /**
     * value: "EB"
     * @const
     */
    "EB": "EB",

    /**
     * value: "EC"
     * @const
     */
    "EC": "EC",

    /**
     * value: "ED"
     * @const
     */
    "ED": "ED",

    /**
     * value: "EE"
     * @const
     */
    "EE": "EE",

    /**
     * value: "EJ"
     * @const
     */
    "EJ": "EJ",

    /**
     * value: "EM"
     * @const
     */
    "EM": "EM",

    /**
     * value: "EP"
     * @const
     */
    "EP": "EP",

    /**
     * value: "ER"
     * @const
     */
    "ER": "ER",

    /**
     * value: "ET"
     * @const
     */
    "ET": "ET",

    /**
     * value: "EX"
     * @const
     */
    "EX": "EX",

    /**
     * value: "EY"
     * @const
     */
    "EY": "EY",

    /**
     * value: "F1"
     * @const
     */
    "F1": "F1",

    /**
     * value: "F2"
     * @const
     */
    "F2": "F2",

    /**
     * value: "F3"
     * @const
     */
    "F3": "F3",

    /**
     * value: "F4"
     * @const
     */
    "F4": "F4",

    /**
     * value: "F5"
     * @const
     */
    "F5": "F5",

    /**
     * value: "F6"
     * @const
     */
    "F6": "F6",

    /**
     * value: "F7"
     * @const
     */
    "F7": "F7",

    /**
     * value: "F8"
     * @const
     */
    "F8": "F8",

    /**
     * value: "F9"
     * @const
     */
    "F9": "F9",

    /**
     * value: "FA"
     * @const
     */
    "FA": "FA",

    /**
     * value: "FB"
     * @const
     */
    "FB": "FB",

    /**
     * value: "FC"
     * @const
     */
    "FC": "FC",

    /**
     * value: "FP"
     * @const
     */
    "FP": "FP",

    /**
     * value: "FX"
     * @const
     */
    "FX": "FX",

    /**
     * value: "FY"
     * @const
     */
    "FY": "FY",

    /**
     * value: "G0"
     * @const
     */
    "G0": "G0",

    /**
     * value: "G1"
     * @const
     */
    "G1": "G1",

    /**
     * value: "G2"
     * @const
     */
    "G2": "G2",

    /**
     * value: "G3"
     * @const
     */
    "G3": "G3",

    /**
     * value: "G4"
     * @const
     */
    "G4": "G4",

    /**
     * value: "G5"
     * @const
     */
    "G5": "G5",

    /**
     * value: "G6"
     * @const
     */
    "G6": "G6",

    /**
     * value: "G7"
     * @const
     */
    "G7": "G7",

    /**
     * value: "G8"
     * @const
     */
    "G8": "G8",

    /**
     * value: "G9"
     * @const
     */
    "G9": "G9",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GB"
     * @const
     */
    "GB": "GB",

    /**
     * value: "GC"
     * @const
     */
    "GC": "GC",

    /**
     * value: "GD"
     * @const
     */
    "GD": "GD",

    /**
     * value: "GE"
     * @const
     */
    "GE": "GE",

    /**
     * value: "GF"
     * @const
     */
    "GF": "GF",

    /**
     * value: "GG"
     * @const
     */
    "GG": "GG",

    /**
     * value: "GH"
     * @const
     */
    "GH": "GH",

    /**
     * value: "GJ"
     * @const
     */
    "GJ": "GJ",

    /**
     * value: "GK"
     * @const
     */
    "GK": "GK",

    /**
     * value: "GL"
     * @const
     */
    "GL": "GL",

    /**
     * value: "GM"
     * @const
     */
    "GM": "GM",

    /**
     * value: "GN"
     * @const
     */
    "GN": "GN",

    /**
     * value: "GO"
     * @const
     */
    "GO": "GO",

    /**
     * value: "GP"
     * @const
     */
    "GP": "GP",

    /**
     * value: "GQ"
     * @const
     */
    "GQ": "GQ",

    /**
     * value: "GR"
     * @const
     */
    "GR": "GR",

    /**
     * value: "GS"
     * @const
     */
    "GS": "GS",

    /**
     * value: "GT"
     * @const
     */
    "GT": "GT",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "GV"
     * @const
     */
    "GV": "GV",

    /**
     * value: "GW"
     * @const
     */
    "GW": "GW",

    /**
     * value: "GX"
     * @const
     */
    "GX": "GX",

    /**
     * value: "GY"
     * @const
     */
    "GY": "GY",

    /**
     * value: "GZ"
     * @const
     */
    "GZ": "GZ",

    /**
     * value: "H9"
     * @const
     */
    "H9": "H9",

    /**
     * value: "HA"
     * @const
     */
    "HA": "HA",

    /**
     * value: "HB"
     * @const
     */
    "HB": "HB",

    /**
     * value: "HC"
     * @const
     */
    "HC": "HC",

    /**
     * value: "HD"
     * @const
     */
    "HD": "HD",

    /**
     * value: "HE"
     * @const
     */
    "HE": "HE",

    /**
     * value: "HF"
     * @const
     */
    "HF": "HF",

    /**
     * value: "HG"
     * @const
     */
    "HG": "HG",

    /**
     * value: "HH"
     * @const
     */
    "HH": "HH",

    /**
     * value: "HI"
     * @const
     */
    "HI": "HI",

    /**
     * value: "HJ"
     * @const
     */
    "HJ": "HJ",

    /**
     * value: "HK"
     * @const
     */
    "HK": "HK",

    /**
     * value: "HL"
     * @const
     */
    "HL": "HL",

    /**
     * value: "HM"
     * @const
     */
    "HM": "HM",

    /**
     * value: "HN"
     * @const
     */
    "HN": "HN",

    /**
     * value: "HO"
     * @const
     */
    "HO": "HO",

    /**
     * value: "HP"
     * @const
     */
    "HP": "HP",

    /**
     * value: "HQ"
     * @const
     */
    "HQ": "HQ",

    /**
     * value: "HR"
     * @const
     */
    "HR": "HR",

    /**
     * value: "HS"
     * @const
     */
    "HS": "HS",

    /**
     * value: "HT"
     * @const
     */
    "HT": "HT",

    /**
     * value: "HU"
     * @const
     */
    "HU": "HU",

    /**
     * value: "HV"
     * @const
     */
    "HV": "HV",

    /**
     * value: "HW"
     * @const
     */
    "HW": "HW",

    /**
     * value: "HX"
     * @const
     */
    "HX": "HX",

    /**
     * value: "HY"
     * @const
     */
    "HY": "HY",

    /**
     * value: "HZ"
     * @const
     */
    "HZ": "HZ",

    /**
     * value: "J1"
     * @const
     */
    "J1": "J1",

    /**
     * value: "J2"
     * @const
     */
    "J2": "J2",

    /**
     * value: "J3"
     * @const
     */
    "J3": "J3",

    /**
     * value: "J4"
     * @const
     */
    "J4": "J4",

    /**
     * value: "JA"
     * @const
     */
    "JA": "JA",

    /**
     * value: "JB"
     * @const
     */
    "JB": "JB",

    /**
     * value: "JC"
     * @const
     */
    "JC": "JC",

    /**
     * value: "JD"
     * @const
     */
    "JD": "JD",

    /**
     * value: "JE"
     * @const
     */
    "JE": "JE",

    /**
     * value: "JF"
     * @const
     */
    "JF": "JF",

    /**
     * value: "JG"
     * @const
     */
    "JG": "JG",

    /**
     * value: "JW"
     * @const
     */
    "JW": "JW",

    /**
     * value: "K0"
     * @const
     */
    "K0": "K0",

    /**
     * value: "K1"
     * @const
     */
    "K1": "K1",

    /**
     * value: "K2"
     * @const
     */
    "K2": "K2",

    /**
     * value: "K3"
     * @const
     */
    "K3": "K3",

    /**
     * value: "K4"
     * @const
     */
    "K4": "K4",

    /**
     * value: "KA"
     * @const
     */
    "KA": "KA",

    /**
     * value: "KB"
     * @const
     */
    "KB": "KB",

    /**
     * value: "KC"
     * @const
     */
    "KC": "KC",

    /**
     * value: "KD"
     * @const
     */
    "KD": "KD",

    /**
     * value: "KE"
     * @const
     */
    "KE": "KE",

    /**
     * value: "KF"
     * @const
     */
    "KF": "KF",

    /**
     * value: "KG"
     * @const
     */
    "KG": "KG",

    /**
     * value: "KH"
     * @const
     */
    "KH": "KH",

    /**
     * value: "KI"
     * @const
     */
    "KI": "KI",

    /**
     * value: "KJ"
     * @const
     */
    "KJ": "KJ",

    /**
     * value: "KK"
     * @const
     */
    "KK": "KK",

    /**
     * value: "KL"
     * @const
     */
    "KL": "KL",

    /**
     * value: "KM"
     * @const
     */
    "KM": "KM",

    /**
     * value: "KN"
     * @const
     */
    "KN": "KN",

    /**
     * value: "KO"
     * @const
     */
    "KO": "KO",

    /**
     * value: "KP"
     * @const
     */
    "KP": "KP",

    /**
     * value: "KQ"
     * @const
     */
    "KQ": "KQ",

    /**
     * value: "KR"
     * @const
     */
    "KR": "KR",

    /**
     * value: "KS"
     * @const
     */
    "KS": "KS",

    /**
     * value: "KT"
     * @const
     */
    "KT": "KT",

    /**
     * value: "KU"
     * @const
     */
    "KU": "KU",

    /**
     * value: "KV"
     * @const
     */
    "KV": "KV",

    /**
     * value: "KW"
     * @const
     */
    "KW": "KW",

    /**
     * value: "KX"
     * @const
     */
    "KX": "KX",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "KZ"
     * @const
     */
    "KZ": "KZ",

    /**
     * value: "L1"
     * @const
     */
    "L1": "L1",

    /**
     * value: "LC"
     * @const
     */
    "LC": "LC",

    /**
     * value: "LD"
     * @const
     */
    "LD": "LD",

    /**
     * value: "LL"
     * @const
     */
    "LL": "LL",

    /**
     * value: "LM"
     * @const
     */
    "LM": "LM",

    /**
     * value: "LR"
     * @const
     */
    "LR": "LR",

    /**
     * value: "LS"
     * @const
     */
    "LS": "LS",

    /**
     * value: "LT"
     * @const
     */
    "LT": "LT",

    /**
     * value: "M2"
     * @const
     */
    "M2": "M2",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MI"
     * @const
     */
    "MI": "MI",

    /**
     * value: "MR"
     * @const
     */
    "MR": "MR",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "NB"
     * @const
     */
    "NB": "NB",

    /**
     * value: "NH"
     * @const
     */
    "NH": "NH",

    /**
     * value: "NM"
     * @const
     */
    "NM": "NM",

    /**
     * value: "NR"
     * @const
     */
    "NR": "NR",

    /**
     * value: "NU"
     * @const
     */
    "NU": "NU",

    /**
     * value: "P1"
     * @const
     */
    "P1": "P1",

    /**
     * value: "P2"
     * @const
     */
    "P2": "P2",

    /**
     * value: "P3"
     * @const
     */
    "P3": "P3",

    /**
     * value: "P4"
     * @const
     */
    "P4": "P4",

    /**
     * value: "P5"
     * @const
     */
    "P5": "P5",

    /**
     * value: "P6"
     * @const
     */
    "P6": "P6",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PB"
     * @const
     */
    "PB": "PB",

    /**
     * value: "PC"
     * @const
     */
    "PC": "PC",

    /**
     * value: "PD"
     * @const
     */
    "PD": "PD",

    /**
     * value: "PE"
     * @const
     */
    "PE": "PE",

    /**
     * value: "PI"
     * @const
     */
    "PI": "PI",

    /**
     * value: "PL"
     * @const
     */
    "PL": "PL",

    /**
     * value: "PM"
     * @const
     */
    "PM": "PM",

    /**
     * value: "PN"
     * @const
     */
    "PN": "PN",

    /**
     * value: "PO"
     * @const
     */
    "PO": "PO",

    /**
     * value: "PS"
     * @const
     */
    "PS": "PS",

    /**
     * value: "PT"
     * @const
     */
    "PT": "PT",

    /**
     * value: "Q0"
     * @const
     */
    "Q0": "Q0",

    /**
     * value: "Q1"
     * @const
     */
    "Q1": "Q1",

    /**
     * value: "Q2"
     * @const
     */
    "Q2": "Q2",

    /**
     * value: "Q3"
     * @const
     */
    "Q3": "Q3",

    /**
     * value: "Q4"
     * @const
     */
    "Q4": "Q4",

    /**
     * value: "Q5"
     * @const
     */
    "Q5": "Q5",

    /**
     * value: "Q6"
     * @const
     */
    "Q6": "Q6",

    /**
     * value: "Q7"
     * @const
     */
    "Q7": "Q7",

    /**
     * value: "Q8"
     * @const
     */
    "Q8": "Q8",

    /**
     * value: "Q9"
     * @const
     */
    "Q9": "Q9",

    /**
     * value: "QA"
     * @const
     */
    "QA": "QA",

    /**
     * value: "QB"
     * @const
     */
    "QB": "QB",

    /**
     * value: "QC"
     * @const
     */
    "QC": "QC",

    /**
     * value: "QD"
     * @const
     */
    "QD": "QD",

    /**
     * value: "QE"
     * @const
     */
    "QE": "QE",

    /**
     * value: "QF"
     * @const
     */
    "QF": "QF",

    /**
     * value: "QG"
     * @const
     */
    "QG": "QG",

    /**
     * value: "QH"
     * @const
     */
    "QH": "QH",

    /**
     * value: "QJ"
     * @const
     */
    "QJ": "QJ",

    /**
     * value: "QK"
     * @const
     */
    "QK": "QK",

    /**
     * value: "QL"
     * @const
     */
    "QL": "QL",

    /**
     * value: "QM"
     * @const
     */
    "QM": "QM",

    /**
     * value: "QN"
     * @const
     */
    "QN": "QN",

    /**
     * value: "QP"
     * @const
     */
    "QP": "QP",

    /**
     * value: "QQ"
     * @const
     */
    "QQ": "QQ",

    /**
     * value: "QR"
     * @const
     */
    "QR": "QR",

    /**
     * value: "QS"
     * @const
     */
    "QS": "QS",

    /**
     * value: "QT"
     * @const
     */
    "QT": "QT",

    /**
     * value: "QU"
     * @const
     */
    "QU": "QU",

    /**
     * value: "QV"
     * @const
     */
    "QV": "QV",

    /**
     * value: "QW"
     * @const
     */
    "QW": "QW",

    /**
     * value: "QX"
     * @const
     */
    "QX": "QX",

    /**
     * value: "QY"
     * @const
     */
    "QY": "QY",

    /**
     * value: "QZ"
     * @const
     */
    "QZ": "QZ",

    /**
     * value: "RA"
     * @const
     */
    "RA": "RA",

    /**
     * value: "RB"
     * @const
     */
    "RB": "RB",

    /**
     * value: "RC"
     * @const
     */
    "RC": "RC",

    /**
     * value: "RD"
     * @const
     */
    "RD": "RD",

    /**
     * value: "RE"
     * @const
     */
    "RE": "RE",

    /**
     * value: "RI"
     * @const
     */
    "RI": "RI",

    /**
     * value: "RP"
     * @const
     */
    "RP": "RP",

    /**
     * value: "RR"
     * @const
     */
    "RR": "RR",

    /**
     * value: "RT"
     * @const
     */
    "RT": "RT",

    /**
     * value: "SA"
     * @const
     */
    "SA": "SA",

    /**
     * value: "SB"
     * @const
     */
    "SB": "SB",

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
     * value: "SE"
     * @const
     */
    "SE": "SE",

    /**
     * value: "SF"
     * @const
     */
    "SF": "SF",

    /**
     * value: "SG"
     * @const
     */
    "SG": "SG",

    /**
     * value: "SH"
     * @const
     */
    "SH": "SH",

    /**
     * value: "SJ"
     * @const
     */
    "SJ": "SJ",

    /**
     * value: "SK"
     * @const
     */
    "SK": "SK",

    /**
     * value: "SL"
     * @const
     */
    "SL": "SL",

    /**
     * value: "SM"
     * @const
     */
    "SM": "SM",

    /**
     * value: "SN"
     * @const
     */
    "SN": "SN",

    /**
     * value: "SP"
     * @const
     */
    "SP": "SP",

    /**
     * value: "SQ"
     * @const
     */
    "SQ": "SQ",

    /**
     * value: "SS"
     * @const
     */
    "SS": "SS",

    /**
     * value: "ST"
     * @const
     */
    "ST": "ST",

    /**
     * value: "SU"
     * @const
     */
    "SU": "SU",

    /**
     * value: "SV"
     * @const
     */
    "SV": "SV",

    /**
     * value: "SW"
     * @const
     */
    "SW": "SW",

    /**
     * value: "SY"
     * @const
     */
    "SY": "SY",

    /**
     * value: "SZ"
     * @const
     */
    "SZ": "SZ",

    /**
     * value: "T1"
     * @const
     */
    "T1": "T1",

    /**
     * value: "T2"
     * @const
     */
    "T2": "T2",

    /**
     * value: "T3"
     * @const
     */
    "T3": "T3",

    /**
     * value: "T4"
     * @const
     */
    "T4": "T4",

    /**
     * value: "T5"
     * @const
     */
    "T5": "T5",

    /**
     * value: "T6"
     * @const
     */
    "T6": "T6",

    /**
     * value: "T7"
     * @const
     */
    "T7": "T7",

    /**
     * value: "T8"
     * @const
     */
    "T8": "T8",

    /**
     * value: "T9"
     * @const
     */
    "T9": "T9",

    /**
     * value: "TA"
     * @const
     */
    "TA": "TA",

    /**
     * value: "TB"
     * @const
     */
    "TB": "TB",

    /**
     * value: "TC"
     * @const
     */
    "TC": "TC",

    /**
     * value: "TD"
     * @const
     */
    "TD": "TD",

    /**
     * value: "TE"
     * @const
     */
    "TE": "TE",

    /**
     * value: "TF"
     * @const
     */
    "TF": "TF",

    /**
     * value: "TG"
     * @const
     */
    "TG": "TG",

    /**
     * value: "TH"
     * @const
     */
    "TH": "TH",

    /**
     * value: "TJ"
     * @const
     */
    "TJ": "TJ",

    /**
     * value: "TK"
     * @const
     */
    "TK": "TK",

    /**
     * value: "TL"
     * @const
     */
    "TL": "TL",

    /**
     * value: "TM"
     * @const
     */
    "TM": "TM",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TP"
     * @const
     */
    "TP": "TP",

    /**
     * value: "TQ"
     * @const
     */
    "TQ": "TQ",

    /**
     * value: "TR"
     * @const
     */
    "TR": "TR",

    /**
     * value: "TS"
     * @const
     */
    "TS": "TS",

    /**
     * value: "TT"
     * @const
     */
    "TT": "TT",

    /**
     * value: "TU"
     * @const
     */
    "TU": "TU",

    /**
     * value: "TV"
     * @const
     */
    "TV": "TV",

    /**
     * value: "TW"
     * @const
     */
    "TW": "TW",

    /**
     * value: "TX"
     * @const
     */
    "TX": "TX",

    /**
     * value: "U1"
     * @const
     */
    "U1": "U1",

    /**
     * value: "U2"
     * @const
     */
    "U2": "U2",

    /**
     * value: "U3"
     * @const
     */
    "U3": "U3",

    /**
     * value: "U4"
     * @const
     */
    "U4": "U4",

    /**
     * value: "U5"
     * @const
     */
    "U5": "U5",

    /**
     * value: "U6"
     * @const
     */
    "U6": "U6",

    /**
     * value: "U7"
     * @const
     */
    "U7": "U7",

    /**
     * value: "U8"
     * @const
     */
    "U8": "U8",

    /**
     * value: "U9"
     * @const
     */
    "U9": "U9",

    /**
     * value: "UA"
     * @const
     */
    "UA": "UA",

    /**
     * value: "UB"
     * @const
     */
    "UB": "UB",

    /**
     * value: "UC"
     * @const
     */
    "UC": "UC",

    /**
     * value: "UD"
     * @const
     */
    "UD": "UD",

    /**
     * value: "UE"
     * @const
     */
    "UE": "UE",

    /**
     * value: "UF"
     * @const
     */
    "UF": "UF",

    /**
     * value: "UG"
     * @const
     */
    "UG": "UG",

    /**
     * value: "UH"
     * @const
     */
    "UH": "UH",

    /**
     * value: "UJ"
     * @const
     */
    "UJ": "UJ",

    /**
     * value: "UK"
     * @const
     */
    "UK": "UK",

    /**
     * value: "UN"
     * @const
     */
    "UN": "UN",

    /**
     * value: "UP"
     * @const
     */
    "UP": "UP",

    /**
     * value: "UQ"
     * @const
     */
    "UQ": "UQ",

    /**
     * value: "UR"
     * @const
     */
    "UR": "UR",

    /**
     * value: "US"
     * @const
     */
    "US": "US",

    /**
     * value: "V1"
     * @const
     */
    "V1": "V1",

    /**
     * value: "V2"
     * @const
     */
    "V2": "V2",

    /**
     * value: "V3"
     * @const
     */
    "V3": "V3",

    /**
     * value: "V4"
     * @const
     */
    "V4": "V4",

    /**
     * value: "V5"
     * @const
     */
    "V5": "V5",

    /**
     * value: "V6"
     * @const
     */
    "V6": "V6",

    /**
     * value: "V7"
     * @const
     */
    "V7": "V7",

    /**
     * value: "V8"
     * @const
     */
    "V8": "V8",

    /**
     * value: "V9"
     * @const
     */
    "V9": "V9",

    /**
     * value: "VP"
     * @const
     */
    "VP": "VP",

    /**
     * value: "VR"
     * @const
     */
    "VR": "VR",

    /**
     * value: "W1"
     * @const
     */
    "W1": "W1",

    /**
     * value: "W5"
     * @const
     */
    "W5": "W5",

    /**
     * value: "W6"
     * @const
     */
    "W6": "W6",

    /**
     * value: "W7"
     * @const
     */
    "W7": "W7",

    /**
     * value: "W8"
     * @const
     */
    "W8": "W8",

    /**
     * value: "W9"
     * @const
     */
    "W9": "W9",

    /**
     * value: "WC"
     * @const
     */
    "WC": "WC",

    /**
     * value: "WH"
     * @const
     */
    "WH": "WH",

    /**
     * value: "WP"
     * @const
     */
    "WP": "WP",

    /**
     * value: "X1"
     * @const
     */
    "X1": "X1",

    /**
     * value: "X2"
     * @const
     */
    "X2": "X2",

    /**
     * value: "X3"
     * @const
     */
    "X3": "X3",

    /**
     * value: "X4"
     * @const
     */
    "X4": "X4",

    /**
     * value: "X5"
     * @const
     */
    "X5": "X5",

    /**
     * value: "XE"
     * @const
     */
    "XE": "XE",

    /**
     * value: "XP"
     * @const
     */
    "XP": "XP",

    /**
     * value: "XS"
     * @const
     */
    "XS": "XS",

    /**
     * value: "XU"
     * @const
     */
    "XU": "XU",

    /**
     * value: "VM"
     * @const
     */
    "VM": "VM",

    /**
     * value: "ZA"
     * @const
     */
    "ZA": "ZA",

    /**
     * value: "ZB"
     * @const
     */
    "ZB": "ZB",

    /**
     * value: "ZL"
     * @const
     */
    "ZL": "ZL",

    /**
     * value: "ZS"
     * @const
     */
    "ZS": "ZS",

    /**
     * value: "1P"
     * @const
     */
    "1P": "1P",

    /**
     * value: "2P"
     * @const
     */
    "2P": "2P",

    /**
     * value: "3P"
     * @const
     */
    "3P": "3P",

    /**
     * value: "8P"
     * @const
     */
    "8P": "8P"
};


/**
 * Allowed values for the <code>cpt_hcpcs_modifier4</code> property.
 * @enum {String}
 * @readonly
 */
DoctorFeeSchedule['CptHcpcsModifier4Enum'] = {

    /**
     * value: ""
     * @const
     */
    "empty": "",

    /**
     * value: "17"
     * @const
     */
    "17": "17",

    /**
     * value: "1D"
     * @const
     */
    "1D": "1D",

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
     * value: "25"
     * @const
     */
    "25": "25",

    /**
     * value: "26"
     * @const
     */
    "26": "26",

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
     * value: "47"
     * @const
     */
    "47": "47",

    /**
     * value: "50"
     * @const
     */
    "50": "50",

    /**
     * value: "51"
     * @const
     */
    "51": "51",

    /**
     * value: "52"
     * @const
     */
    "52": "52",

    /**
     * value: "53"
     * @const
     */
    "53": "53",

    /**
     * value: "54"
     * @const
     */
    "54": "54",

    /**
     * value: "55"
     * @const
     */
    "55": "55",

    /**
     * value: "56"
     * @const
     */
    "56": "56",

    /**
     * value: "57"
     * @const
     */
    "57": "57",

    /**
     * value: "58"
     * @const
     */
    "58": "58",

    /**
     * value: "59"
     * @const
     */
    "59": "59",

    /**
     * value: "62"
     * @const
     */
    "62": "62",

    /**
     * value: "63"
     * @const
     */
    "63": "63",

    /**
     * value: "66"
     * @const
     */
    "66": "66",

    /**
     * value: "73"
     * @const
     */
    "73": "73",

    /**
     * value: "74"
     * @const
     */
    "74": "74",

    /**
     * value: "76"
     * @const
     */
    "76": "76",

    /**
     * value: "77"
     * @const
     */
    "77": "77",

    /**
     * value: "78"
     * @const
     */
    "78": "78",

    /**
     * value: "79"
     * @const
     */
    "79": "79",

    /**
     * value: "80"
     * @const
     */
    "80": "80",

    /**
     * value: "81"
     * @const
     */
    "81": "81",

    /**
     * value: "82"
     * @const
     */
    "82": "82",

    /**
     * value: "83"
     * @const
     */
    "83": "83",

    /**
     * value: "90"
     * @const
     */
    "90": "90",

    /**
     * value: "91"
     * @const
     */
    "91": "91",

    /**
     * value: "92"
     * @const
     */
    "92": "92",

    /**
     * value: "93"
     * @const
     */
    "93": "93",

    /**
     * value: "95"
     * @const
     */
    "95": "95",

    /**
     * value: "96"
     * @const
     */
    "96": "96",

    /**
     * value: "97"
     * @const
     */
    "97": "97",

    /**
     * value: "99"
     * @const
     */
    "99": "99",

    /**
     * value: "A1"
     * @const
     */
    "A1": "A1",

    /**
     * value: "A2"
     * @const
     */
    "A2": "A2",

    /**
     * value: "A3"
     * @const
     */
    "A3": "A3",

    /**
     * value: "A4"
     * @const
     */
    "A4": "A4",

    /**
     * value: "A5"
     * @const
     */
    "A5": "A5",

    /**
     * value: "A6"
     * @const
     */
    "A6": "A6",

    /**
     * value: "A7"
     * @const
     */
    "A7": "A7",

    /**
     * value: "A8"
     * @const
     */
    "A8": "A8",

    /**
     * value: "A9"
     * @const
     */
    "A9": "A9",

    /**
     * value: "AA"
     * @const
     */
    "AA": "AA",

    /**
     * value: "AD"
     * @const
     */
    "AD": "AD",

    /**
     * value: "AE"
     * @const
     */
    "AE": "AE",

    /**
     * value: "AF"
     * @const
     */
    "AF": "AF",

    /**
     * value: "AG"
     * @const
     */
    "AG": "AG",

    /**
     * value: "AH"
     * @const
     */
    "AH": "AH",

    /**
     * value: "AI"
     * @const
     */
    "AI": "AI",

    /**
     * value: "AJ"
     * @const
     */
    "AJ": "AJ",

    /**
     * value: "AK"
     * @const
     */
    "AK": "AK",

    /**
     * value: "AM"
     * @const
     */
    "AM": "AM",

    /**
     * value: "AO"
     * @const
     */
    "AO": "AO",

    /**
     * value: "AP"
     * @const
     */
    "AP": "AP",

    /**
     * value: "AQ"
     * @const
     */
    "AQ": "AQ",

    /**
     * value: "AR"
     * @const
     */
    "AR": "AR",

    /**
     * value: "AS"
     * @const
     */
    "AS": "AS",

    /**
     * value: "AT"
     * @const
     */
    "AT": "AT",

    /**
     * value: "AU"
     * @const
     */
    "AU": "AU",

    /**
     * value: "AV"
     * @const
     */
    "AV": "AV",

    /**
     * value: "AW"
     * @const
     */
    "AW": "AW",

    /**
     * value: "AX"
     * @const
     */
    "AX": "AX",

    /**
     * value: "AY"
     * @const
     */
    "AY": "AY",

    /**
     * value: "AZ"
     * @const
     */
    "AZ": "AZ",

    /**
     * value: "BA"
     * @const
     */
    "BA": "BA",

    /**
     * value: "BL"
     * @const
     */
    "BL": "BL",

    /**
     * value: "BO"
     * @const
     */
    "BO": "BO",

    /**
     * value: "BP"
     * @const
     */
    "BP": "BP",

    /**
     * value: "BR"
     * @const
     */
    "BR": "BR",

    /**
     * value: "BU"
     * @const
     */
    "BU": "BU",

    /**
     * value: "CA"
     * @const
     */
    "CA": "CA",

    /**
     * value: "CB"
     * @const
     */
    "CB": "CB",

    /**
     * value: "CC"
     * @const
     */
    "CC": "CC",

    /**
     * value: "CD"
     * @const
     */
    "CD": "CD",

    /**
     * value: "CE"
     * @const
     */
    "CE": "CE",

    /**
     * value: "CF"
     * @const
     */
    "CF": "CF",

    /**
     * value: "CG"
     * @const
     */
    "CG": "CG",

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
     * value: "CJ"
     * @const
     */
    "CJ": "CJ",

    /**
     * value: "CK"
     * @const
     */
    "CK": "CK",

    /**
     * value: "CL"
     * @const
     */
    "CL": "CL",

    /**
     * value: "CM"
     * @const
     */
    "CM": "CM",

    /**
     * value: "CN"
     * @const
     */
    "CN": "CN",

    /**
     * value: "CO"
     * @const
     */
    "CO": "CO",

    /**
     * value: "CP"
     * @const
     */
    "CP": "CP",

    /**
     * value: "CQ"
     * @const
     */
    "CQ": "CQ",

    /**
     * value: "CR"
     * @const
     */
    "CR": "CR",

    /**
     * value: "CS"
     * @const
     */
    "CS": "CS",

    /**
     * value: "CT"
     * @const
     */
    "CT": "CT",

    /**
     * value: "DA"
     * @const
     */
    "DA": "DA",

    /**
     * value: "E1"
     * @const
     */
    "E1": "E1",

    /**
     * value: "E2"
     * @const
     */
    "E2": "E2",

    /**
     * value: "E3"
     * @const
     */
    "E3": "E3",

    /**
     * value: "E4"
     * @const
     */
    "E4": "E4",

    /**
     * value: "EA"
     * @const
     */
    "EA": "EA",

    /**
     * value: "EB"
     * @const
     */
    "EB": "EB",

    /**
     * value: "EC"
     * @const
     */
    "EC": "EC",

    /**
     * value: "ED"
     * @const
     */
    "ED": "ED",

    /**
     * value: "EE"
     * @const
     */
    "EE": "EE",

    /**
     * value: "EJ"
     * @const
     */
    "EJ": "EJ",

    /**
     * value: "EM"
     * @const
     */
    "EM": "EM",

    /**
     * value: "EP"
     * @const
     */
    "EP": "EP",

    /**
     * value: "ER"
     * @const
     */
    "ER": "ER",

    /**
     * value: "ET"
     * @const
     */
    "ET": "ET",

    /**
     * value: "EX"
     * @const
     */
    "EX": "EX",

    /**
     * value: "EY"
     * @const
     */
    "EY": "EY",

    /**
     * value: "F1"
     * @const
     */
    "F1": "F1",

    /**
     * value: "F2"
     * @const
     */
    "F2": "F2",

    /**
     * value: "F3"
     * @const
     */
    "F3": "F3",

    /**
     * value: "F4"
     * @const
     */
    "F4": "F4",

    /**
     * value: "F5"
     * @const
     */
    "F5": "F5",

    /**
     * value: "F6"
     * @const
     */
    "F6": "F6",

    /**
     * value: "F7"
     * @const
     */
    "F7": "F7",

    /**
     * value: "F8"
     * @const
     */
    "F8": "F8",

    /**
     * value: "F9"
     * @const
     */
    "F9": "F9",

    /**
     * value: "FA"
     * @const
     */
    "FA": "FA",

    /**
     * value: "FB"
     * @const
     */
    "FB": "FB",

    /**
     * value: "FC"
     * @const
     */
    "FC": "FC",

    /**
     * value: "FP"
     * @const
     */
    "FP": "FP",

    /**
     * value: "FX"
     * @const
     */
    "FX": "FX",

    /**
     * value: "FY"
     * @const
     */
    "FY": "FY",

    /**
     * value: "G0"
     * @const
     */
    "G0": "G0",

    /**
     * value: "G1"
     * @const
     */
    "G1": "G1",

    /**
     * value: "G2"
     * @const
     */
    "G2": "G2",

    /**
     * value: "G3"
     * @const
     */
    "G3": "G3",

    /**
     * value: "G4"
     * @const
     */
    "G4": "G4",

    /**
     * value: "G5"
     * @const
     */
    "G5": "G5",

    /**
     * value: "G6"
     * @const
     */
    "G6": "G6",

    /**
     * value: "G7"
     * @const
     */
    "G7": "G7",

    /**
     * value: "G8"
     * @const
     */
    "G8": "G8",

    /**
     * value: "G9"
     * @const
     */
    "G9": "G9",

    /**
     * value: "GA"
     * @const
     */
    "GA": "GA",

    /**
     * value: "GB"
     * @const
     */
    "GB": "GB",

    /**
     * value: "GC"
     * @const
     */
    "GC": "GC",

    /**
     * value: "GD"
     * @const
     */
    "GD": "GD",

    /**
     * value: "GE"
     * @const
     */
    "GE": "GE",

    /**
     * value: "GF"
     * @const
     */
    "GF": "GF",

    /**
     * value: "GG"
     * @const
     */
    "GG": "GG",

    /**
     * value: "GH"
     * @const
     */
    "GH": "GH",

    /**
     * value: "GJ"
     * @const
     */
    "GJ": "GJ",

    /**
     * value: "GK"
     * @const
     */
    "GK": "GK",

    /**
     * value: "GL"
     * @const
     */
    "GL": "GL",

    /**
     * value: "GM"
     * @const
     */
    "GM": "GM",

    /**
     * value: "GN"
     * @const
     */
    "GN": "GN",

    /**
     * value: "GO"
     * @const
     */
    "GO": "GO",

    /**
     * value: "GP"
     * @const
     */
    "GP": "GP",

    /**
     * value: "GQ"
     * @const
     */
    "GQ": "GQ",

    /**
     * value: "GR"
     * @const
     */
    "GR": "GR",

    /**
     * value: "GS"
     * @const
     */
    "GS": "GS",

    /**
     * value: "GT"
     * @const
     */
    "GT": "GT",

    /**
     * value: "GU"
     * @const
     */
    "GU": "GU",

    /**
     * value: "GV"
     * @const
     */
    "GV": "GV",

    /**
     * value: "GW"
     * @const
     */
    "GW": "GW",

    /**
     * value: "GX"
     * @const
     */
    "GX": "GX",

    /**
     * value: "GY"
     * @const
     */
    "GY": "GY",

    /**
     * value: "GZ"
     * @const
     */
    "GZ": "GZ",

    /**
     * value: "H9"
     * @const
     */
    "H9": "H9",

    /**
     * value: "HA"
     * @const
     */
    "HA": "HA",

    /**
     * value: "HB"
     * @const
     */
    "HB": "HB",

    /**
     * value: "HC"
     * @const
     */
    "HC": "HC",

    /**
     * value: "HD"
     * @const
     */
    "HD": "HD",

    /**
     * value: "HE"
     * @const
     */
    "HE": "HE",

    /**
     * value: "HF"
     * @const
     */
    "HF": "HF",

    /**
     * value: "HG"
     * @const
     */
    "HG": "HG",

    /**
     * value: "HH"
     * @const
     */
    "HH": "HH",

    /**
     * value: "HI"
     * @const
     */
    "HI": "HI",

    /**
     * value: "HJ"
     * @const
     */
    "HJ": "HJ",

    /**
     * value: "HK"
     * @const
     */
    "HK": "HK",

    /**
     * value: "HL"
     * @const
     */
    "HL": "HL",

    /**
     * value: "HM"
     * @const
     */
    "HM": "HM",

    /**
     * value: "HN"
     * @const
     */
    "HN": "HN",

    /**
     * value: "HO"
     * @const
     */
    "HO": "HO",

    /**
     * value: "HP"
     * @const
     */
    "HP": "HP",

    /**
     * value: "HQ"
     * @const
     */
    "HQ": "HQ",

    /**
     * value: "HR"
     * @const
     */
    "HR": "HR",

    /**
     * value: "HS"
     * @const
     */
    "HS": "HS",

    /**
     * value: "HT"
     * @const
     */
    "HT": "HT",

    /**
     * value: "HU"
     * @const
     */
    "HU": "HU",

    /**
     * value: "HV"
     * @const
     */
    "HV": "HV",

    /**
     * value: "HW"
     * @const
     */
    "HW": "HW",

    /**
     * value: "HX"
     * @const
     */
    "HX": "HX",

    /**
     * value: "HY"
     * @const
     */
    "HY": "HY",

    /**
     * value: "HZ"
     * @const
     */
    "HZ": "HZ",

    /**
     * value: "J1"
     * @const
     */
    "J1": "J1",

    /**
     * value: "J2"
     * @const
     */
    "J2": "J2",

    /**
     * value: "J3"
     * @const
     */
    "J3": "J3",

    /**
     * value: "J4"
     * @const
     */
    "J4": "J4",

    /**
     * value: "JA"
     * @const
     */
    "JA": "JA",

    /**
     * value: "JB"
     * @const
     */
    "JB": "JB",

    /**
     * value: "JC"
     * @const
     */
    "JC": "JC",

    /**
     * value: "JD"
     * @const
     */
    "JD": "JD",

    /**
     * value: "JE"
     * @const
     */
    "JE": "JE",

    /**
     * value: "JF"
     * @const
     */
    "JF": "JF",

    /**
     * value: "JG"
     * @const
     */
    "JG": "JG",

    /**
     * value: "JW"
     * @const
     */
    "JW": "JW",

    /**
     * value: "K0"
     * @const
     */
    "K0": "K0",

    /**
     * value: "K1"
     * @const
     */
    "K1": "K1",

    /**
     * value: "K2"
     * @const
     */
    "K2": "K2",

    /**
     * value: "K3"
     * @const
     */
    "K3": "K3",

    /**
     * value: "K4"
     * @const
     */
    "K4": "K4",

    /**
     * value: "KA"
     * @const
     */
    "KA": "KA",

    /**
     * value: "KB"
     * @const
     */
    "KB": "KB",

    /**
     * value: "KC"
     * @const
     */
    "KC": "KC",

    /**
     * value: "KD"
     * @const
     */
    "KD": "KD",

    /**
     * value: "KE"
     * @const
     */
    "KE": "KE",

    /**
     * value: "KF"
     * @const
     */
    "KF": "KF",

    /**
     * value: "KG"
     * @const
     */
    "KG": "KG",

    /**
     * value: "KH"
     * @const
     */
    "KH": "KH",

    /**
     * value: "KI"
     * @const
     */
    "KI": "KI",

    /**
     * value: "KJ"
     * @const
     */
    "KJ": "KJ",

    /**
     * value: "KK"
     * @const
     */
    "KK": "KK",

    /**
     * value: "KL"
     * @const
     */
    "KL": "KL",

    /**
     * value: "KM"
     * @const
     */
    "KM": "KM",

    /**
     * value: "KN"
     * @const
     */
    "KN": "KN",

    /**
     * value: "KO"
     * @const
     */
    "KO": "KO",

    /**
     * value: "KP"
     * @const
     */
    "KP": "KP",

    /**
     * value: "KQ"
     * @const
     */
    "KQ": "KQ",

    /**
     * value: "KR"
     * @const
     */
    "KR": "KR",

    /**
     * value: "KS"
     * @const
     */
    "KS": "KS",

    /**
     * value: "KT"
     * @const
     */
    "KT": "KT",

    /**
     * value: "KU"
     * @const
     */
    "KU": "KU",

    /**
     * value: "KV"
     * @const
     */
    "KV": "KV",

    /**
     * value: "KW"
     * @const
     */
    "KW": "KW",

    /**
     * value: "KX"
     * @const
     */
    "KX": "KX",

    /**
     * value: "KY"
     * @const
     */
    "KY": "KY",

    /**
     * value: "KZ"
     * @const
     */
    "KZ": "KZ",

    /**
     * value: "L1"
     * @const
     */
    "L1": "L1",

    /**
     * value: "LC"
     * @const
     */
    "LC": "LC",

    /**
     * value: "LD"
     * @const
     */
    "LD": "LD",

    /**
     * value: "LL"
     * @const
     */
    "LL": "LL",

    /**
     * value: "LM"
     * @const
     */
    "LM": "LM",

    /**
     * value: "LR"
     * @const
     */
    "LR": "LR",

    /**
     * value: "LS"
     * @const
     */
    "LS": "LS",

    /**
     * value: "LT"
     * @const
     */
    "LT": "LT",

    /**
     * value: "M2"
     * @const
     */
    "M2": "M2",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "MI"
     * @const
     */
    "MI": "MI",

    /**
     * value: "MR"
     * @const
     */
    "MR": "MR",

    /**
     * value: "MS"
     * @const
     */
    "MS": "MS",

    /**
     * value: "NB"
     * @const
     */
    "NB": "NB",

    /**
     * value: "NH"
     * @const
     */
    "NH": "NH",

    /**
     * value: "NM"
     * @const
     */
    "NM": "NM",

    /**
     * value: "NR"
     * @const
     */
    "NR": "NR",

    /**
     * value: "NU"
     * @const
     */
    "NU": "NU",

    /**
     * value: "P1"
     * @const
     */
    "P1": "P1",

    /**
     * value: "P2"
     * @const
     */
    "P2": "P2",

    /**
     * value: "P3"
     * @const
     */
    "P3": "P3",

    /**
     * value: "P4"
     * @const
     */
    "P4": "P4",

    /**
     * value: "P5"
     * @const
     */
    "P5": "P5",

    /**
     * value: "P6"
     * @const
     */
    "P6": "P6",

    /**
     * value: "PA"
     * @const
     */
    "PA": "PA",

    /**
     * value: "PB"
     * @const
     */
    "PB": "PB",

    /**
     * value: "PC"
     * @const
     */
    "PC": "PC",

    /**
     * value: "PD"
     * @const
     */
    "PD": "PD",

    /**
     * value: "PE"
     * @const
     */
    "PE": "PE",

    /**
     * value: "PI"
     * @const
     */
    "PI": "PI",

    /**
     * value: "PL"
     * @const
     */
    "PL": "PL",

    /**
     * value: "PM"
     * @const
     */
    "PM": "PM",

    /**
     * value: "PN"
     * @const
     */
    "PN": "PN",

    /**
     * value: "PO"
     * @const
     */
    "PO": "PO",

    /**
     * value: "PS"
     * @const
     */
    "PS": "PS",

    /**
     * value: "PT"
     * @const
     */
    "PT": "PT",

    /**
     * value: "Q0"
     * @const
     */
    "Q0": "Q0",

    /**
     * value: "Q1"
     * @const
     */
    "Q1": "Q1",

    /**
     * value: "Q2"
     * @const
     */
    "Q2": "Q2",

    /**
     * value: "Q3"
     * @const
     */
    "Q3": "Q3",

    /**
     * value: "Q4"
     * @const
     */
    "Q4": "Q4",

    /**
     * value: "Q5"
     * @const
     */
    "Q5": "Q5",

    /**
     * value: "Q6"
     * @const
     */
    "Q6": "Q6",

    /**
     * value: "Q7"
     * @const
     */
    "Q7": "Q7",

    /**
     * value: "Q8"
     * @const
     */
    "Q8": "Q8",

    /**
     * value: "Q9"
     * @const
     */
    "Q9": "Q9",

    /**
     * value: "QA"
     * @const
     */
    "QA": "QA",

    /**
     * value: "QB"
     * @const
     */
    "QB": "QB",

    /**
     * value: "QC"
     * @const
     */
    "QC": "QC",

    /**
     * value: "QD"
     * @const
     */
    "QD": "QD",

    /**
     * value: "QE"
     * @const
     */
    "QE": "QE",

    /**
     * value: "QF"
     * @const
     */
    "QF": "QF",

    /**
     * value: "QG"
     * @const
     */
    "QG": "QG",

    /**
     * value: "QH"
     * @const
     */
    "QH": "QH",

    /**
     * value: "QJ"
     * @const
     */
    "QJ": "QJ",

    /**
     * value: "QK"
     * @const
     */
    "QK": "QK",

    /**
     * value: "QL"
     * @const
     */
    "QL": "QL",

    /**
     * value: "QM"
     * @const
     */
    "QM": "QM",

    /**
     * value: "QN"
     * @const
     */
    "QN": "QN",

    /**
     * value: "QP"
     * @const
     */
    "QP": "QP",

    /**
     * value: "QQ"
     * @const
     */
    "QQ": "QQ",

    /**
     * value: "QR"
     * @const
     */
    "QR": "QR",

    /**
     * value: "QS"
     * @const
     */
    "QS": "QS",

    /**
     * value: "QT"
     * @const
     */
    "QT": "QT",

    /**
     * value: "QU"
     * @const
     */
    "QU": "QU",

    /**
     * value: "QV"
     * @const
     */
    "QV": "QV",

    /**
     * value: "QW"
     * @const
     */
    "QW": "QW",

    /**
     * value: "QX"
     * @const
     */
    "QX": "QX",

    /**
     * value: "QY"
     * @const
     */
    "QY": "QY",

    /**
     * value: "QZ"
     * @const
     */
    "QZ": "QZ",

    /**
     * value: "RA"
     * @const
     */
    "RA": "RA",

    /**
     * value: "RB"
     * @const
     */
    "RB": "RB",

    /**
     * value: "RC"
     * @const
     */
    "RC": "RC",

    /**
     * value: "RD"
     * @const
     */
    "RD": "RD",

    /**
     * value: "RE"
     * @const
     */
    "RE": "RE",

    /**
     * value: "RI"
     * @const
     */
    "RI": "RI",

    /**
     * value: "RP"
     * @const
     */
    "RP": "RP",

    /**
     * value: "RR"
     * @const
     */
    "RR": "RR",

    /**
     * value: "RT"
     * @const
     */
    "RT": "RT",

    /**
     * value: "SA"
     * @const
     */
    "SA": "SA",

    /**
     * value: "SB"
     * @const
     */
    "SB": "SB",

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
     * value: "SE"
     * @const
     */
    "SE": "SE",

    /**
     * value: "SF"
     * @const
     */
    "SF": "SF",

    /**
     * value: "SG"
     * @const
     */
    "SG": "SG",

    /**
     * value: "SH"
     * @const
     */
    "SH": "SH",

    /**
     * value: "SJ"
     * @const
     */
    "SJ": "SJ",

    /**
     * value: "SK"
     * @const
     */
    "SK": "SK",

    /**
     * value: "SL"
     * @const
     */
    "SL": "SL",

    /**
     * value: "SM"
     * @const
     */
    "SM": "SM",

    /**
     * value: "SN"
     * @const
     */
    "SN": "SN",

    /**
     * value: "SP"
     * @const
     */
    "SP": "SP",

    /**
     * value: "SQ"
     * @const
     */
    "SQ": "SQ",

    /**
     * value: "SS"
     * @const
     */
    "SS": "SS",

    /**
     * value: "ST"
     * @const
     */
    "ST": "ST",

    /**
     * value: "SU"
     * @const
     */
    "SU": "SU",

    /**
     * value: "SV"
     * @const
     */
    "SV": "SV",

    /**
     * value: "SW"
     * @const
     */
    "SW": "SW",

    /**
     * value: "SY"
     * @const
     */
    "SY": "SY",

    /**
     * value: "SZ"
     * @const
     */
    "SZ": "SZ",

    /**
     * value: "T1"
     * @const
     */
    "T1": "T1",

    /**
     * value: "T2"
     * @const
     */
    "T2": "T2",

    /**
     * value: "T3"
     * @const
     */
    "T3": "T3",

    /**
     * value: "T4"
     * @const
     */
    "T4": "T4",

    /**
     * value: "T5"
     * @const
     */
    "T5": "T5",

    /**
     * value: "T6"
     * @const
     */
    "T6": "T6",

    /**
     * value: "T7"
     * @const
     */
    "T7": "T7",

    /**
     * value: "T8"
     * @const
     */
    "T8": "T8",

    /**
     * value: "T9"
     * @const
     */
    "T9": "T9",

    /**
     * value: "TA"
     * @const
     */
    "TA": "TA",

    /**
     * value: "TB"
     * @const
     */
    "TB": "TB",

    /**
     * value: "TC"
     * @const
     */
    "TC": "TC",

    /**
     * value: "TD"
     * @const
     */
    "TD": "TD",

    /**
     * value: "TE"
     * @const
     */
    "TE": "TE",

    /**
     * value: "TF"
     * @const
     */
    "TF": "TF",

    /**
     * value: "TG"
     * @const
     */
    "TG": "TG",

    /**
     * value: "TH"
     * @const
     */
    "TH": "TH",

    /**
     * value: "TJ"
     * @const
     */
    "TJ": "TJ",

    /**
     * value: "TK"
     * @const
     */
    "TK": "TK",

    /**
     * value: "TL"
     * @const
     */
    "TL": "TL",

    /**
     * value: "TM"
     * @const
     */
    "TM": "TM",

    /**
     * value: "TN"
     * @const
     */
    "TN": "TN",

    /**
     * value: "TP"
     * @const
     */
    "TP": "TP",

    /**
     * value: "TQ"
     * @const
     */
    "TQ": "TQ",

    /**
     * value: "TR"
     * @const
     */
    "TR": "TR",

    /**
     * value: "TS"
     * @const
     */
    "TS": "TS",

    /**
     * value: "TT"
     * @const
     */
    "TT": "TT",

    /**
     * value: "TU"
     * @const
     */
    "TU": "TU",

    /**
     * value: "TV"
     * @const
     */
    "TV": "TV",

    /**
     * value: "TW"
     * @const
     */
    "TW": "TW",

    /**
     * value: "TX"
     * @const
     */
    "TX": "TX",

    /**
     * value: "U1"
     * @const
     */
    "U1": "U1",

    /**
     * value: "U2"
     * @const
     */
    "U2": "U2",

    /**
     * value: "U3"
     * @const
     */
    "U3": "U3",

    /**
     * value: "U4"
     * @const
     */
    "U4": "U4",

    /**
     * value: "U5"
     * @const
     */
    "U5": "U5",

    /**
     * value: "U6"
     * @const
     */
    "U6": "U6",

    /**
     * value: "U7"
     * @const
     */
    "U7": "U7",

    /**
     * value: "U8"
     * @const
     */
    "U8": "U8",

    /**
     * value: "U9"
     * @const
     */
    "U9": "U9",

    /**
     * value: "UA"
     * @const
     */
    "UA": "UA",

    /**
     * value: "UB"
     * @const
     */
    "UB": "UB",

    /**
     * value: "UC"
     * @const
     */
    "UC": "UC",

    /**
     * value: "UD"
     * @const
     */
    "UD": "UD",

    /**
     * value: "UE"
     * @const
     */
    "UE": "UE",

    /**
     * value: "UF"
     * @const
     */
    "UF": "UF",

    /**
     * value: "UG"
     * @const
     */
    "UG": "UG",

    /**
     * value: "UH"
     * @const
     */
    "UH": "UH",

    /**
     * value: "UJ"
     * @const
     */
    "UJ": "UJ",

    /**
     * value: "UK"
     * @const
     */
    "UK": "UK",

    /**
     * value: "UN"
     * @const
     */
    "UN": "UN",

    /**
     * value: "UP"
     * @const
     */
    "UP": "UP",

    /**
     * value: "UQ"
     * @const
     */
    "UQ": "UQ",

    /**
     * value: "UR"
     * @const
     */
    "UR": "UR",

    /**
     * value: "US"
     * @const
     */
    "US": "US",

    /**
     * value: "V1"
     * @const
     */
    "V1": "V1",

    /**
     * value: "V2"
     * @const
     */
    "V2": "V2",

    /**
     * value: "V3"
     * @const
     */
    "V3": "V3",

    /**
     * value: "V4"
     * @const
     */
    "V4": "V4",

    /**
     * value: "V5"
     * @const
     */
    "V5": "V5",

    /**
     * value: "V6"
     * @const
     */
    "V6": "V6",

    /**
     * value: "V7"
     * @const
     */
    "V7": "V7",

    /**
     * value: "V8"
     * @const
     */
    "V8": "V8",

    /**
     * value: "V9"
     * @const
     */
    "V9": "V9",

    /**
     * value: "VP"
     * @const
     */
    "VP": "VP",

    /**
     * value: "VR"
     * @const
     */
    "VR": "VR",

    /**
     * value: "W1"
     * @const
     */
    "W1": "W1",

    /**
     * value: "W5"
     * @const
     */
    "W5": "W5",

    /**
     * value: "W6"
     * @const
     */
    "W6": "W6",

    /**
     * value: "W7"
     * @const
     */
    "W7": "W7",

    /**
     * value: "W8"
     * @const
     */
    "W8": "W8",

    /**
     * value: "W9"
     * @const
     */
    "W9": "W9",

    /**
     * value: "WC"
     * @const
     */
    "WC": "WC",

    /**
     * value: "WH"
     * @const
     */
    "WH": "WH",

    /**
     * value: "WP"
     * @const
     */
    "WP": "WP",

    /**
     * value: "X1"
     * @const
     */
    "X1": "X1",

    /**
     * value: "X2"
     * @const
     */
    "X2": "X2",

    /**
     * value: "X3"
     * @const
     */
    "X3": "X3",

    /**
     * value: "X4"
     * @const
     */
    "X4": "X4",

    /**
     * value: "X5"
     * @const
     */
    "X5": "X5",

    /**
     * value: "XE"
     * @const
     */
    "XE": "XE",

    /**
     * value: "XP"
     * @const
     */
    "XP": "XP",

    /**
     * value: "XS"
     * @const
     */
    "XS": "XS",

    /**
     * value: "XU"
     * @const
     */
    "XU": "XU",

    /**
     * value: "VM"
     * @const
     */
    "VM": "VM",

    /**
     * value: "ZA"
     * @const
     */
    "ZA": "ZA",

    /**
     * value: "ZB"
     * @const
     */
    "ZB": "ZB",

    /**
     * value: "ZL"
     * @const
     */
    "ZL": "ZL",

    /**
     * value: "ZS"
     * @const
     */
    "ZS": "ZS",

    /**
     * value: "1P"
     * @const
     */
    "1P": "1P",

    /**
     * value: "2P"
     * @const
     */
    "2P": "2P",

    /**
     * value: "3P"
     * @const
     */
    "3P": "3P",

    /**
     * value: "8P"
     * @const
     */
    "8P": "8P"
};


/**
 * Allowed values for the <code>ndc_units</code> property.
 * @enum {String}
 * @readonly
 */
DoctorFeeSchedule['NdcUnitsEnum'] = {

    /**
     * value: "F2"
     * @const
     */
    "F2": "F2",

    /**
     * value: "GR"
     * @const
     */
    "GR": "GR",

    /**
     * value: "ME"
     * @const
     */
    "ME": "ME",

    /**
     * value: "ML"
     * @const
     */
    "ML": "ML",

    /**
     * value: "UN"
     * @const
     */
    "UN": "UN"
};



export default DoctorFeeSchedule;

