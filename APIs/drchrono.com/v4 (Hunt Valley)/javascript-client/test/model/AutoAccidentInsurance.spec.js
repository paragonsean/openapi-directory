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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.OpenapiJsClient);
  }
}(this, function(expect, OpenapiJsClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OpenapiJsClient.AutoAccidentInsurance();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('AutoAccidentInsurance', function() {
    it('should create an instance of AutoAccidentInsurance', function() {
      // uncomment below and update the code to test AutoAccidentInsurance
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be.a(OpenapiJsClient.AutoAccidentInsurance);
    });

    it('should have the property autoAccidentCaseNumber (base name: "auto_accident_case_number")', function() {
      // uncomment below and update the code to test the property autoAccidentCaseNumber
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentClaimRepAddress (base name: "auto_accident_claim_rep_address")', function() {
      // uncomment below and update the code to test the property autoAccidentClaimRepAddress
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentClaimRepCity (base name: "auto_accident_claim_rep_city")', function() {
      // uncomment below and update the code to test the property autoAccidentClaimRepCity
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentClaimRepIsInsurer (base name: "auto_accident_claim_rep_is_insurer")', function() {
      // uncomment below and update the code to test the property autoAccidentClaimRepIsInsurer
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentClaimRepName (base name: "auto_accident_claim_rep_name")', function() {
      // uncomment below and update the code to test the property autoAccidentClaimRepName
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentClaimRepState (base name: "auto_accident_claim_rep_state")', function() {
      // uncomment below and update the code to test the property autoAccidentClaimRepState
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentClaimRepZip (base name: "auto_accident_claim_rep_zip")', function() {
      // uncomment below and update the code to test the property autoAccidentClaimRepZip
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentCompany (base name: "auto_accident_company")', function() {
      // uncomment below and update the code to test the property autoAccidentCompany
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentDateOfAccident (base name: "auto_accident_date_of_accident")', function() {
      // uncomment below and update the code to test the property autoAccidentDateOfAccident
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentDisabledFromDate (base name: "auto_accident_disabled_from_date")', function() {
      // uncomment below and update the code to test the property autoAccidentDisabledFromDate
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentDisabledToDate (base name: "auto_accident_disabled_to_date")', function() {
      // uncomment below and update the code to test the property autoAccidentDisabledToDate
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentHadSimilarCondition (base name: "auto_accident_had_similar_condition")', function() {
      // uncomment below and update the code to test the property autoAccidentHadSimilarCondition
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentIsSubscriberThePatient (base name: "auto_accident_is_subscriber_the_patient")', function() {
      // uncomment below and update the code to test the property autoAccidentIsSubscriberThePatient
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentNotes (base name: "auto_accident_notes")', function() {
      // uncomment below and update the code to test the property autoAccidentNotes
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentPatientRelationshipToSubscriber (base name: "auto_accident_patient_relationship_to_subscriber")', function() {
      // uncomment below and update the code to test the property autoAccidentPatientRelationshipToSubscriber
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentPayerAddress (base name: "auto_accident_payer_address")', function() {
      // uncomment below and update the code to test the property autoAccidentPayerAddress
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentPayerCity (base name: "auto_accident_payer_city")', function() {
      // uncomment below and update the code to test the property autoAccidentPayerCity
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentPayerId (base name: "auto_accident_payer_id")', function() {
      // uncomment below and update the code to test the property autoAccidentPayerId
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentPayerState (base name: "auto_accident_payer_state")', function() {
      // uncomment below and update the code to test the property autoAccidentPayerState
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentPayerZip (base name: "auto_accident_payer_zip")', function() {
      // uncomment below and update the code to test the property autoAccidentPayerZip
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentPolicyNumber (base name: "auto_accident_policy_number")', function() {
      // uncomment below and update the code to test the property autoAccidentPolicyNumber
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentReturnToWorkDate (base name: "auto_accident_return_to_work_date")', function() {
      // uncomment below and update the code to test the property autoAccidentReturnToWorkDate
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSignificantInjury (base name: "auto_accident_significant_injury")', function() {
      // uncomment below and update the code to test the property autoAccidentSignificantInjury
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSignificantInjuryNotes (base name: "auto_accident_significant_injury_notes")', function() {
      // uncomment below and update the code to test the property autoAccidentSignificantInjuryNotes
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSimilarConditionDate (base name: "auto_accident_similar_condition_date")', function() {
      // uncomment below and update the code to test the property autoAccidentSimilarConditionDate
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSimilarConditionNotes (base name: "auto_accident_similar_condition_notes")', function() {
      // uncomment below and update the code to test the property autoAccidentSimilarConditionNotes
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentStateOfOccurrence (base name: "auto_accident_state_of_occurrence")', function() {
      // uncomment below and update the code to test the property autoAccidentStateOfOccurrence
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentStillUnderCare (base name: "auto_accident_still_under_care")', function() {
      // uncomment below and update the code to test the property autoAccidentStillUnderCare
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberAddress (base name: "auto_accident_subscriber_address")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberAddress
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberCity (base name: "auto_accident_subscriber_city")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberCity
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberDateOfBirth (base name: "auto_accident_subscriber_date_of_birth")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberDateOfBirth
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberFirstName (base name: "auto_accident_subscriber_first_name")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberFirstName
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberLastName (base name: "auto_accident_subscriber_last_name")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberLastName
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberMiddleName (base name: "auto_accident_subscriber_middle_name")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberMiddleName
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberPhoneNumber (base name: "auto_accident_subscriber_phone_number")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberPhoneNumber
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberSocialSecurity (base name: "auto_accident_subscriber_social_security")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberSocialSecurity
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberState (base name: "auto_accident_subscriber_state")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberState
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberSuffix (base name: "auto_accident_subscriber_suffix")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberSuffix
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentSubscriberZipCode (base name: "auto_accident_subscriber_zip_code")', function() {
      // uncomment below and update the code to test the property autoAccidentSubscriberZipCode
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentTreatmentDuration (base name: "auto_accident_treatment_duration")', function() {
      // uncomment below and update the code to test the property autoAccidentTreatmentDuration
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentWillRequireTherapy (base name: "auto_accident_will_require_therapy")', function() {
      // uncomment below and update the code to test the property autoAccidentWillRequireTherapy
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

    it('should have the property autoAccidentWillRequireTherapyRec (base name: "auto_accident_will_require_therapy_rec")', function() {
      // uncomment below and update the code to test the property autoAccidentWillRequireTherapyRec
      //var instance = new OpenapiJsClient.AutoAccidentInsurance();
      //expect(instance).to.be();
    });

  });

}));
