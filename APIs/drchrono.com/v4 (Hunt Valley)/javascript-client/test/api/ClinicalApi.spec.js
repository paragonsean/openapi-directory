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
    instance = new OpenapiJsClient.ClinicalApi();
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

  describe('ClinicalApi', function() {
    describe('allergiesCreate', function() {
      it('should call allergiesCreate successfully', function(done) {
        //uncomment below and update the code to test allergiesCreate
        //instance.allergiesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('allergiesList', function() {
      it('should call allergiesList successfully', function(done) {
        //uncomment below and update the code to test allergiesList
        //instance.allergiesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('allergiesPartialUpdate', function() {
      it('should call allergiesPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test allergiesPartialUpdate
        //instance.allergiesPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('allergiesRead', function() {
      it('should call allergiesRead successfully', function(done) {
        //uncomment below and update the code to test allergiesRead
        //instance.allergiesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('allergiesUpdate', function() {
      it('should call allergiesUpdate successfully', function(done) {
        //uncomment below and update the code to test allergiesUpdate
        //instance.allergiesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('amendmentsCreate', function() {
      it('should call amendmentsCreate successfully', function(done) {
        //uncomment below and update the code to test amendmentsCreate
        //instance.amendmentsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('amendmentsDelete', function() {
      it('should call amendmentsDelete successfully', function(done) {
        //uncomment below and update the code to test amendmentsDelete
        //instance.amendmentsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('amendmentsList', function() {
      it('should call amendmentsList successfully', function(done) {
        //uncomment below and update the code to test amendmentsList
        //instance.amendmentsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('amendmentsPartialUpdate', function() {
      it('should call amendmentsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test amendmentsPartialUpdate
        //instance.amendmentsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('amendmentsRead', function() {
      it('should call amendmentsRead successfully', function(done) {
        //uncomment below and update the code to test amendmentsRead
        //instance.amendmentsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('amendmentsUpdate', function() {
      it('should call amendmentsUpdate successfully', function(done) {
        //uncomment below and update the code to test amendmentsUpdate
        //instance.amendmentsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentProfilesCreate', function() {
      it('should call appointmentProfilesCreate successfully', function(done) {
        //uncomment below and update the code to test appointmentProfilesCreate
        //instance.appointmentProfilesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentProfilesDelete', function() {
      it('should call appointmentProfilesDelete successfully', function(done) {
        //uncomment below and update the code to test appointmentProfilesDelete
        //instance.appointmentProfilesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentProfilesList', function() {
      it('should call appointmentProfilesList successfully', function(done) {
        //uncomment below and update the code to test appointmentProfilesList
        //instance.appointmentProfilesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentProfilesPartialUpdate', function() {
      it('should call appointmentProfilesPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test appointmentProfilesPartialUpdate
        //instance.appointmentProfilesPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentProfilesRead', function() {
      it('should call appointmentProfilesRead successfully', function(done) {
        //uncomment below and update the code to test appointmentProfilesRead
        //instance.appointmentProfilesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentProfilesUpdate', function() {
      it('should call appointmentProfilesUpdate successfully', function(done) {
        //uncomment below and update the code to test appointmentProfilesUpdate
        //instance.appointmentProfilesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentTemplatesCreate', function() {
      it('should call appointmentTemplatesCreate successfully', function(done) {
        //uncomment below and update the code to test appointmentTemplatesCreate
        //instance.appointmentTemplatesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentTemplatesDelete', function() {
      it('should call appointmentTemplatesDelete successfully', function(done) {
        //uncomment below and update the code to test appointmentTemplatesDelete
        //instance.appointmentTemplatesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentTemplatesList', function() {
      it('should call appointmentTemplatesList successfully', function(done) {
        //uncomment below and update the code to test appointmentTemplatesList
        //instance.appointmentTemplatesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentTemplatesPartialUpdate', function() {
      it('should call appointmentTemplatesPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test appointmentTemplatesPartialUpdate
        //instance.appointmentTemplatesPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentTemplatesRead', function() {
      it('should call appointmentTemplatesRead successfully', function(done) {
        //uncomment below and update the code to test appointmentTemplatesRead
        //instance.appointmentTemplatesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentTemplatesUpdate', function() {
      it('should call appointmentTemplatesUpdate successfully', function(done) {
        //uncomment below and update the code to test appointmentTemplatesUpdate
        //instance.appointmentTemplatesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentsCreate', function() {
      it('should call appointmentsCreate successfully', function(done) {
        //uncomment below and update the code to test appointmentsCreate
        //instance.appointmentsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentsDelete', function() {
      it('should call appointmentsDelete successfully', function(done) {
        //uncomment below and update the code to test appointmentsDelete
        //instance.appointmentsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentsList', function() {
      it('should call appointmentsList successfully', function(done) {
        //uncomment below and update the code to test appointmentsList
        //instance.appointmentsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentsPartialUpdate', function() {
      it('should call appointmentsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test appointmentsPartialUpdate
        //instance.appointmentsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentsRead', function() {
      it('should call appointmentsRead successfully', function(done) {
        //uncomment below and update the code to test appointmentsRead
        //instance.appointmentsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appointmentsUpdate', function() {
      it('should call appointmentsUpdate successfully', function(done) {
        //uncomment below and update the code to test appointmentsUpdate
        //instance.appointmentsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('carePlansList', function() {
      it('should call carePlansList successfully', function(done) {
        //uncomment below and update the code to test carePlansList
        //instance.carePlansList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('carePlansRead', function() {
      it('should call carePlansRead successfully', function(done) {
        //uncomment below and update the code to test carePlansRead
        //instance.carePlansRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('careTeamMembersList', function() {
      it('should call careTeamMembersList successfully', function(done) {
        //uncomment below and update the code to test careTeamMembersList
        //instance.careTeamMembersList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('careTeamMembersRead', function() {
      it('should call careTeamMembersRead successfully', function(done) {
        //uncomment below and update the code to test careTeamMembersRead
        //instance.careTeamMembersRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('claimBillingNotesCreate', function() {
      it('should call claimBillingNotesCreate successfully', function(done) {
        //uncomment below and update the code to test claimBillingNotesCreate
        //instance.claimBillingNotesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('claimBillingNotesList', function() {
      it('should call claimBillingNotesList successfully', function(done) {
        //uncomment below and update the code to test claimBillingNotesList
        //instance.claimBillingNotesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('claimBillingNotesRead', function() {
      it('should call claimBillingNotesRead successfully', function(done) {
        //uncomment below and update the code to test claimBillingNotesRead
        //instance.claimBillingNotesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteFieldTypesList', function() {
      it('should call clinicalNoteFieldTypesList successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteFieldTypesList
        //instance.clinicalNoteFieldTypesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteFieldTypesRead', function() {
      it('should call clinicalNoteFieldTypesRead successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteFieldTypesRead
        //instance.clinicalNoteFieldTypesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteFieldValuesCreate', function() {
      it('should call clinicalNoteFieldValuesCreate successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteFieldValuesCreate
        //instance.clinicalNoteFieldValuesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteFieldValuesList', function() {
      it('should call clinicalNoteFieldValuesList successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteFieldValuesList
        //instance.clinicalNoteFieldValuesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteFieldValuesPartialUpdate', function() {
      it('should call clinicalNoteFieldValuesPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteFieldValuesPartialUpdate
        //instance.clinicalNoteFieldValuesPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteFieldValuesRead', function() {
      it('should call clinicalNoteFieldValuesRead successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteFieldValuesRead
        //instance.clinicalNoteFieldValuesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteFieldValuesUpdate', function() {
      it('should call clinicalNoteFieldValuesUpdate successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteFieldValuesUpdate
        //instance.clinicalNoteFieldValuesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteTemplatesList', function() {
      it('should call clinicalNoteTemplatesList successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteTemplatesList
        //instance.clinicalNoteTemplatesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNoteTemplatesRead', function() {
      it('should call clinicalNoteTemplatesRead successfully', function(done) {
        //uncomment below and update the code to test clinicalNoteTemplatesRead
        //instance.clinicalNoteTemplatesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNotesList', function() {
      it('should call clinicalNotesList successfully', function(done) {
        //uncomment below and update the code to test clinicalNotesList
        //instance.clinicalNotesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('clinicalNotesRead', function() {
      it('should call clinicalNotesRead successfully', function(done) {
        //uncomment below and update the code to test clinicalNotesRead
        //instance.clinicalNotesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('consentFormsApplyToAppointment', function() {
      it('should call consentFormsApplyToAppointment successfully', function(done) {
        //uncomment below and update the code to test consentFormsApplyToAppointment
        //instance.consentFormsApplyToAppointment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('consentFormsCreate', function() {
      it('should call consentFormsCreate successfully', function(done) {
        //uncomment below and update the code to test consentFormsCreate
        //instance.consentFormsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('consentFormsList', function() {
      it('should call consentFormsList successfully', function(done) {
        //uncomment below and update the code to test consentFormsList
        //instance.consentFormsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('consentFormsPartialUpdate', function() {
      it('should call consentFormsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test consentFormsPartialUpdate
        //instance.consentFormsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('consentFormsRead', function() {
      it('should call consentFormsRead successfully', function(done) {
        //uncomment below and update the code to test consentFormsRead
        //instance.consentFormsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('consentFormsUnapplyFromAppointment', function() {
      it('should call consentFormsUnapplyFromAppointment successfully', function(done) {
        //uncomment below and update the code to test consentFormsUnapplyFromAppointment
        //instance.consentFormsUnapplyFromAppointment(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('consentFormsUpdate', function() {
      it('should call consentFormsUpdate successfully', function(done) {
        //uncomment below and update the code to test consentFormsUpdate
        //instance.consentFormsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customAppointmentFieldsCreate', function() {
      it('should call customAppointmentFieldsCreate successfully', function(done) {
        //uncomment below and update the code to test customAppointmentFieldsCreate
        //instance.customAppointmentFieldsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customAppointmentFieldsList', function() {
      it('should call customAppointmentFieldsList successfully', function(done) {
        //uncomment below and update the code to test customAppointmentFieldsList
        //instance.customAppointmentFieldsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customAppointmentFieldsPartialUpdate', function() {
      it('should call customAppointmentFieldsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test customAppointmentFieldsPartialUpdate
        //instance.customAppointmentFieldsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customAppointmentFieldsRead', function() {
      it('should call customAppointmentFieldsRead successfully', function(done) {
        //uncomment below and update the code to test customAppointmentFieldsRead
        //instance.customAppointmentFieldsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customAppointmentFieldsUpdate', function() {
      it('should call customAppointmentFieldsUpdate successfully', function(done) {
        //uncomment below and update the code to test customAppointmentFieldsUpdate
        //instance.customAppointmentFieldsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customDemographicsCreate', function() {
      it('should call customDemographicsCreate successfully', function(done) {
        //uncomment below and update the code to test customDemographicsCreate
        //instance.customDemographicsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customDemographicsList', function() {
      it('should call customDemographicsList successfully', function(done) {
        //uncomment below and update the code to test customDemographicsList
        //instance.customDemographicsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customDemographicsPartialUpdate', function() {
      it('should call customDemographicsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test customDemographicsPartialUpdate
        //instance.customDemographicsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customDemographicsRead', function() {
      it('should call customDemographicsRead successfully', function(done) {
        //uncomment below and update the code to test customDemographicsRead
        //instance.customDemographicsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customDemographicsUpdate', function() {
      it('should call customDemographicsUpdate successfully', function(done) {
        //uncomment below and update the code to test customDemographicsUpdate
        //instance.customDemographicsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customVitalsList', function() {
      it('should call customVitalsList successfully', function(done) {
        //uncomment below and update the code to test customVitalsList
        //instance.customVitalsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('customVitalsRead', function() {
      it('should call customVitalsRead successfully', function(done) {
        //uncomment below and update the code to test customVitalsRead
        //instance.customVitalsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('documentsCreate', function() {
      it('should call documentsCreate successfully', function(done) {
        //uncomment below and update the code to test documentsCreate
        //instance.documentsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('documentsDelete', function() {
      it('should call documentsDelete successfully', function(done) {
        //uncomment below and update the code to test documentsDelete
        //instance.documentsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('documentsList', function() {
      it('should call documentsList successfully', function(done) {
        //uncomment below and update the code to test documentsList
        //instance.documentsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('documentsPartialUpdate', function() {
      it('should call documentsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test documentsPartialUpdate
        //instance.documentsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('documentsRead', function() {
      it('should call documentsRead successfully', function(done) {
        //uncomment below and update the code to test documentsRead
        //instance.documentsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('documentsUpdate', function() {
      it('should call documentsUpdate successfully', function(done) {
        //uncomment below and update the code to test documentsUpdate
        //instance.documentsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('eobsCreate', function() {
      it('should call eobsCreate successfully', function(done) {
        //uncomment below and update the code to test eobsCreate
        //instance.eobsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('eobsList', function() {
      it('should call eobsList successfully', function(done) {
        //uncomment below and update the code to test eobsList
        //instance.eobsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('eobsRead', function() {
      it('should call eobsRead successfully', function(done) {
        //uncomment below and update the code to test eobsRead
        //instance.eobsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('feeSchedulesList', function() {
      it('should call feeSchedulesList successfully', function(done) {
        //uncomment below and update the code to test feeSchedulesList
        //instance.feeSchedulesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('feeSchedulesRead', function() {
      it('should call feeSchedulesRead successfully', function(done) {
        //uncomment below and update the code to test feeSchedulesRead
        //instance.feeSchedulesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('implantableDevicesList', function() {
      it('should call implantableDevicesList successfully', function(done) {
        //uncomment below and update the code to test implantableDevicesList
        //instance.implantableDevicesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('implantableDevicesRead', function() {
      it('should call implantableDevicesRead successfully', function(done) {
        //uncomment below and update the code to test implantableDevicesRead
        //instance.implantableDevicesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('insurancesList', function() {
      it('should call insurancesList successfully', function(done) {
        //uncomment below and update the code to test insurancesList
        //instance.insurancesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('insurancesRead', function() {
      it('should call insurancesRead successfully', function(done) {
        //uncomment below and update the code to test insurancesRead
        //instance.insurancesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labDocumentsCreate', function() {
      it('should call labDocumentsCreate successfully', function(done) {
        //uncomment below and update the code to test labDocumentsCreate
        //instance.labDocumentsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labDocumentsDelete', function() {
      it('should call labDocumentsDelete successfully', function(done) {
        //uncomment below and update the code to test labDocumentsDelete
        //instance.labDocumentsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labDocumentsList', function() {
      it('should call labDocumentsList successfully', function(done) {
        //uncomment below and update the code to test labDocumentsList
        //instance.labDocumentsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labDocumentsPartialUpdate', function() {
      it('should call labDocumentsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test labDocumentsPartialUpdate
        //instance.labDocumentsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labDocumentsRead', function() {
      it('should call labDocumentsRead successfully', function(done) {
        //uncomment below and update the code to test labDocumentsRead
        //instance.labDocumentsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labDocumentsUpdate', function() {
      it('should call labDocumentsUpdate successfully', function(done) {
        //uncomment below and update the code to test labDocumentsUpdate
        //instance.labDocumentsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersCreate', function() {
      it('should call labOrdersCreate successfully', function(done) {
        //uncomment below and update the code to test labOrdersCreate
        //instance.labOrdersCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersDelete', function() {
      it('should call labOrdersDelete successfully', function(done) {
        //uncomment below and update the code to test labOrdersDelete
        //instance.labOrdersDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersList', function() {
      it('should call labOrdersList successfully', function(done) {
        //uncomment below and update the code to test labOrdersList
        //instance.labOrdersList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersPartialUpdate', function() {
      it('should call labOrdersPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test labOrdersPartialUpdate
        //instance.labOrdersPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersRead', function() {
      it('should call labOrdersRead successfully', function(done) {
        //uncomment below and update the code to test labOrdersRead
        //instance.labOrdersRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersSummaryList', function() {
      it('should call labOrdersSummaryList successfully', function(done) {
        //uncomment below and update the code to test labOrdersSummaryList
        //instance.labOrdersSummaryList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersSummaryRead', function() {
      it('should call labOrdersSummaryRead successfully', function(done) {
        //uncomment below and update the code to test labOrdersSummaryRead
        //instance.labOrdersSummaryRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labOrdersUpdate', function() {
      it('should call labOrdersUpdate successfully', function(done) {
        //uncomment below and update the code to test labOrdersUpdate
        //instance.labOrdersUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labResultsCreate', function() {
      it('should call labResultsCreate successfully', function(done) {
        //uncomment below and update the code to test labResultsCreate
        //instance.labResultsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labResultsDelete', function() {
      it('should call labResultsDelete successfully', function(done) {
        //uncomment below and update the code to test labResultsDelete
        //instance.labResultsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labResultsList', function() {
      it('should call labResultsList successfully', function(done) {
        //uncomment below and update the code to test labResultsList
        //instance.labResultsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labResultsPartialUpdate', function() {
      it('should call labResultsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test labResultsPartialUpdate
        //instance.labResultsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labResultsRead', function() {
      it('should call labResultsRead successfully', function(done) {
        //uncomment below and update the code to test labResultsRead
        //instance.labResultsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labResultsUpdate', function() {
      it('should call labResultsUpdate successfully', function(done) {
        //uncomment below and update the code to test labResultsUpdate
        //instance.labResultsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labTestsCreate', function() {
      it('should call labTestsCreate successfully', function(done) {
        //uncomment below and update the code to test labTestsCreate
        //instance.labTestsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labTestsDelete', function() {
      it('should call labTestsDelete successfully', function(done) {
        //uncomment below and update the code to test labTestsDelete
        //instance.labTestsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labTestsList', function() {
      it('should call labTestsList successfully', function(done) {
        //uncomment below and update the code to test labTestsList
        //instance.labTestsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labTestsPartialUpdate', function() {
      it('should call labTestsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test labTestsPartialUpdate
        //instance.labTestsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labTestsRead', function() {
      it('should call labTestsRead successfully', function(done) {
        //uncomment below and update the code to test labTestsRead
        //instance.labTestsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('labTestsUpdate', function() {
      it('should call labTestsUpdate successfully', function(done) {
        //uncomment below and update the code to test labTestsUpdate
        //instance.labTestsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('medicationsAppendToPharmacyNote', function() {
      it('should call medicationsAppendToPharmacyNote successfully', function(done) {
        //uncomment below and update the code to test medicationsAppendToPharmacyNote
        //instance.medicationsAppendToPharmacyNote(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('medicationsCreate', function() {
      it('should call medicationsCreate successfully', function(done) {
        //uncomment below and update the code to test medicationsCreate
        //instance.medicationsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('medicationsList', function() {
      it('should call medicationsList successfully', function(done) {
        //uncomment below and update the code to test medicationsList
        //instance.medicationsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('medicationsPartialUpdate', function() {
      it('should call medicationsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test medicationsPartialUpdate
        //instance.medicationsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('medicationsRead', function() {
      it('should call medicationsRead successfully', function(done) {
        //uncomment below and update the code to test medicationsRead
        //instance.medicationsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('medicationsUpdate', function() {
      it('should call medicationsUpdate successfully', function(done) {
        //uncomment below and update the code to test medicationsUpdate
        //instance.medicationsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientCommunicationsCreate', function() {
      it('should call patientCommunicationsCreate successfully', function(done) {
        //uncomment below and update the code to test patientCommunicationsCreate
        //instance.patientCommunicationsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientCommunicationsList', function() {
      it('should call patientCommunicationsList successfully', function(done) {
        //uncomment below and update the code to test patientCommunicationsList
        //instance.patientCommunicationsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientCommunicationsPartialUpdate', function() {
      it('should call patientCommunicationsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientCommunicationsPartialUpdate
        //instance.patientCommunicationsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientCommunicationsRead', function() {
      it('should call patientCommunicationsRead successfully', function(done) {
        //uncomment below and update the code to test patientCommunicationsRead
        //instance.patientCommunicationsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientCommunicationsUpdate', function() {
      it('should call patientCommunicationsUpdate successfully', function(done) {
        //uncomment below and update the code to test patientCommunicationsUpdate
        //instance.patientCommunicationsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientFlagTypesCreate', function() {
      it('should call patientFlagTypesCreate successfully', function(done) {
        //uncomment below and update the code to test patientFlagTypesCreate
        //instance.patientFlagTypesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientFlagTypesList', function() {
      it('should call patientFlagTypesList successfully', function(done) {
        //uncomment below and update the code to test patientFlagTypesList
        //instance.patientFlagTypesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientFlagTypesPartialUpdate', function() {
      it('should call patientFlagTypesPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientFlagTypesPartialUpdate
        //instance.patientFlagTypesPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientFlagTypesRead', function() {
      it('should call patientFlagTypesRead successfully', function(done) {
        //uncomment below and update the code to test patientFlagTypesRead
        //instance.patientFlagTypesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientFlagTypesUpdate', function() {
      it('should call patientFlagTypesUpdate successfully', function(done) {
        //uncomment below and update the code to test patientFlagTypesUpdate
        //instance.patientFlagTypesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientInterventionsCreate', function() {
      it('should call patientInterventionsCreate successfully', function(done) {
        //uncomment below and update the code to test patientInterventionsCreate
        //instance.patientInterventionsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientInterventionsList', function() {
      it('should call patientInterventionsList successfully', function(done) {
        //uncomment below and update the code to test patientInterventionsList
        //instance.patientInterventionsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientInterventionsPartialUpdate', function() {
      it('should call patientInterventionsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientInterventionsPartialUpdate
        //instance.patientInterventionsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientInterventionsRead', function() {
      it('should call patientInterventionsRead successfully', function(done) {
        //uncomment below and update the code to test patientInterventionsRead
        //instance.patientInterventionsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientInterventionsUpdate', function() {
      it('should call patientInterventionsUpdate successfully', function(done) {
        //uncomment below and update the code to test patientInterventionsUpdate
        //instance.patientInterventionsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientLabResultsCreate', function() {
      it('should call patientLabResultsCreate successfully', function(done) {
        //uncomment below and update the code to test patientLabResultsCreate
        //instance.patientLabResultsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientLabResultsDelete', function() {
      it('should call patientLabResultsDelete successfully', function(done) {
        //uncomment below and update the code to test patientLabResultsDelete
        //instance.patientLabResultsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientLabResultsList', function() {
      it('should call patientLabResultsList successfully', function(done) {
        //uncomment below and update the code to test patientLabResultsList
        //instance.patientLabResultsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientLabResultsPartialUpdate', function() {
      it('should call patientLabResultsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientLabResultsPartialUpdate
        //instance.patientLabResultsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientLabResultsRead', function() {
      it('should call patientLabResultsRead successfully', function(done) {
        //uncomment below and update the code to test patientLabResultsRead
        //instance.patientLabResultsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientLabResultsUpdate', function() {
      it('should call patientLabResultsUpdate successfully', function(done) {
        //uncomment below and update the code to test patientLabResultsUpdate
        //instance.patientLabResultsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientMessagesCreate', function() {
      it('should call patientMessagesCreate successfully', function(done) {
        //uncomment below and update the code to test patientMessagesCreate
        //instance.patientMessagesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientMessagesList', function() {
      it('should call patientMessagesList successfully', function(done) {
        //uncomment below and update the code to test patientMessagesList
        //instance.patientMessagesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientMessagesPartialUpdate', function() {
      it('should call patientMessagesPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientMessagesPartialUpdate
        //instance.patientMessagesPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientMessagesRead', function() {
      it('should call patientMessagesRead successfully', function(done) {
        //uncomment below and update the code to test patientMessagesRead
        //instance.patientMessagesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientMessagesUpdate', function() {
      it('should call patientMessagesUpdate successfully', function(done) {
        //uncomment below and update the code to test patientMessagesUpdate
        //instance.patientMessagesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientPhysicalExamsCreate', function() {
      it('should call patientPhysicalExamsCreate successfully', function(done) {
        //uncomment below and update the code to test patientPhysicalExamsCreate
        //instance.patientPhysicalExamsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientPhysicalExamsList', function() {
      it('should call patientPhysicalExamsList successfully', function(done) {
        //uncomment below and update the code to test patientPhysicalExamsList
        //instance.patientPhysicalExamsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientPhysicalExamsPartialUpdate', function() {
      it('should call patientPhysicalExamsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientPhysicalExamsPartialUpdate
        //instance.patientPhysicalExamsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientPhysicalExamsRead', function() {
      it('should call patientPhysicalExamsRead successfully', function(done) {
        //uncomment below and update the code to test patientPhysicalExamsRead
        //instance.patientPhysicalExamsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientPhysicalExamsUpdate', function() {
      it('should call patientPhysicalExamsUpdate successfully', function(done) {
        //uncomment below and update the code to test patientPhysicalExamsUpdate
        //instance.patientPhysicalExamsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientRiskAssessmentsCreate', function() {
      it('should call patientRiskAssessmentsCreate successfully', function(done) {
        //uncomment below and update the code to test patientRiskAssessmentsCreate
        //instance.patientRiskAssessmentsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientRiskAssessmentsList', function() {
      it('should call patientRiskAssessmentsList successfully', function(done) {
        //uncomment below and update the code to test patientRiskAssessmentsList
        //instance.patientRiskAssessmentsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientRiskAssessmentsPartialUpdate', function() {
      it('should call patientRiskAssessmentsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientRiskAssessmentsPartialUpdate
        //instance.patientRiskAssessmentsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientRiskAssessmentsRead', function() {
      it('should call patientRiskAssessmentsRead successfully', function(done) {
        //uncomment below and update the code to test patientRiskAssessmentsRead
        //instance.patientRiskAssessmentsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientRiskAssessmentsUpdate', function() {
      it('should call patientRiskAssessmentsUpdate successfully', function(done) {
        //uncomment below and update the code to test patientRiskAssessmentsUpdate
        //instance.patientRiskAssessmentsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientVaccineRecordsCreate', function() {
      it('should call patientVaccineRecordsCreate successfully', function(done) {
        //uncomment below and update the code to test patientVaccineRecordsCreate
        //instance.patientVaccineRecordsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientVaccineRecordsList', function() {
      it('should call patientVaccineRecordsList successfully', function(done) {
        //uncomment below and update the code to test patientVaccineRecordsList
        //instance.patientVaccineRecordsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientVaccineRecordsPartialUpdate', function() {
      it('should call patientVaccineRecordsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientVaccineRecordsPartialUpdate
        //instance.patientVaccineRecordsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientVaccineRecordsRead', function() {
      it('should call patientVaccineRecordsRead successfully', function(done) {
        //uncomment below and update the code to test patientVaccineRecordsRead
        //instance.patientVaccineRecordsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientVaccineRecordsUpdate', function() {
      it('should call patientVaccineRecordsUpdate successfully', function(done) {
        //uncomment below and update the code to test patientVaccineRecordsUpdate
        //instance.patientVaccineRecordsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsCcda', function() {
      it('should call patientsCcda successfully', function(done) {
        //uncomment below and update the code to test patientsCcda
        //instance.patientsCcda(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsCreate', function() {
      it('should call patientsCreate successfully', function(done) {
        //uncomment below and update the code to test patientsCreate
        //instance.patientsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsDelete', function() {
      it('should call patientsDelete successfully', function(done) {
        //uncomment below and update the code to test patientsDelete
        //instance.patientsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsList', function() {
      it('should call patientsList successfully', function(done) {
        //uncomment below and update the code to test patientsList
        //instance.patientsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsOnpatientAccessCreate', function() {
      it('should call patientsOnpatientAccessCreate successfully', function(done) {
        //uncomment below and update the code to test patientsOnpatientAccessCreate
        //instance.patientsOnpatientAccessCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsOnpatientAccessDelete', function() {
      it('should call patientsOnpatientAccessDelete successfully', function(done) {
        //uncomment below and update the code to test patientsOnpatientAccessDelete
        //instance.patientsOnpatientAccessDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsOnpatientAccessRead', function() {
      it('should call patientsOnpatientAccessRead successfully', function(done) {
        //uncomment below and update the code to test patientsOnpatientAccessRead
        //instance.patientsOnpatientAccessRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsPartialUpdate', function() {
      it('should call patientsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientsPartialUpdate
        //instance.patientsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsQrda1', function() {
      it('should call patientsQrda1 successfully', function(done) {
        //uncomment below and update the code to test patientsQrda1
        //instance.patientsQrda1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsRead', function() {
      it('should call patientsRead successfully', function(done) {
        //uncomment below and update the code to test patientsRead
        //instance.patientsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsSummaryCreate', function() {
      it('should call patientsSummaryCreate successfully', function(done) {
        //uncomment below and update the code to test patientsSummaryCreate
        //instance.patientsSummaryCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsSummaryDelete', function() {
      it('should call patientsSummaryDelete successfully', function(done) {
        //uncomment below and update the code to test patientsSummaryDelete
        //instance.patientsSummaryDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsSummaryList', function() {
      it('should call patientsSummaryList successfully', function(done) {
        //uncomment below and update the code to test patientsSummaryList
        //instance.patientsSummaryList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsSummaryPartialUpdate', function() {
      it('should call patientsSummaryPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test patientsSummaryPartialUpdate
        //instance.patientsSummaryPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsSummaryRead', function() {
      it('should call patientsSummaryRead successfully', function(done) {
        //uncomment below and update the code to test patientsSummaryRead
        //instance.patientsSummaryRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsSummaryUpdate', function() {
      it('should call patientsSummaryUpdate successfully', function(done) {
        //uncomment below and update the code to test patientsSummaryUpdate
        //instance.patientsSummaryUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('patientsUpdate', function() {
      it('should call patientsUpdate successfully', function(done) {
        //uncomment below and update the code to test patientsUpdate
        //instance.patientsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('prescriptionMessagesList', function() {
      it('should call prescriptionMessagesList successfully', function(done) {
        //uncomment below and update the code to test prescriptionMessagesList
        //instance.prescriptionMessagesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('prescriptionMessagesRead', function() {
      it('should call prescriptionMessagesRead successfully', function(done) {
        //uncomment below and update the code to test prescriptionMessagesRead
        //instance.prescriptionMessagesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('problemsCreate', function() {
      it('should call problemsCreate successfully', function(done) {
        //uncomment below and update the code to test problemsCreate
        //instance.problemsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('problemsList', function() {
      it('should call problemsList successfully', function(done) {
        //uncomment below and update the code to test problemsList
        //instance.problemsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('problemsPartialUpdate', function() {
      it('should call problemsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test problemsPartialUpdate
        //instance.problemsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('problemsRead', function() {
      it('should call problemsRead successfully', function(done) {
        //uncomment below and update the code to test problemsRead
        //instance.problemsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('problemsUpdate', function() {
      it('should call problemsUpdate successfully', function(done) {
        //uncomment below and update the code to test problemsUpdate
        //instance.problemsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('reminderProfilesCreate', function() {
      it('should call reminderProfilesCreate successfully', function(done) {
        //uncomment below and update the code to test reminderProfilesCreate
        //instance.reminderProfilesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('reminderProfilesDelete', function() {
      it('should call reminderProfilesDelete successfully', function(done) {
        //uncomment below and update the code to test reminderProfilesDelete
        //instance.reminderProfilesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('reminderProfilesList', function() {
      it('should call reminderProfilesList successfully', function(done) {
        //uncomment below and update the code to test reminderProfilesList
        //instance.reminderProfilesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('reminderProfilesPartialUpdate', function() {
      it('should call reminderProfilesPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test reminderProfilesPartialUpdate
        //instance.reminderProfilesPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('reminderProfilesRead', function() {
      it('should call reminderProfilesRead successfully', function(done) {
        //uncomment below and update the code to test reminderProfilesRead
        //instance.reminderProfilesRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('reminderProfilesUpdate', function() {
      it('should call reminderProfilesUpdate successfully', function(done) {
        //uncomment below and update the code to test reminderProfilesUpdate
        //instance.reminderProfilesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sublabsCreate', function() {
      it('should call sublabsCreate successfully', function(done) {
        //uncomment below and update the code to test sublabsCreate
        //instance.sublabsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sublabsDelete', function() {
      it('should call sublabsDelete successfully', function(done) {
        //uncomment below and update the code to test sublabsDelete
        //instance.sublabsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sublabsList', function() {
      it('should call sublabsList successfully', function(done) {
        //uncomment below and update the code to test sublabsList
        //instance.sublabsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sublabsPartialUpdate', function() {
      it('should call sublabsPartialUpdate successfully', function(done) {
        //uncomment below and update the code to test sublabsPartialUpdate
        //instance.sublabsPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sublabsRead', function() {
      it('should call sublabsRead successfully', function(done) {
        //uncomment below and update the code to test sublabsRead
        //instance.sublabsRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sublabsUpdate', function() {
      it('should call sublabsUpdate successfully', function(done) {
        //uncomment below and update the code to test sublabsUpdate
        //instance.sublabsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
