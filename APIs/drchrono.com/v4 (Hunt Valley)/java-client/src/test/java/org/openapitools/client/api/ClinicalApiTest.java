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

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AllergiesList200Response;
import org.openapitools.client.model.AmendmentsList200Response;
import org.openapitools.client.model.Appointment;
import org.openapitools.client.model.AppointmentProfile;
import org.openapitools.client.model.AppointmentProfilesList200Response;
import org.openapitools.client.model.AppointmentTemplate;
import org.openapitools.client.model.AppointmentTemplatesList200Response;
import org.openapitools.client.model.AppointmentsList200Response;
import org.openapitools.client.model.CarePlan;
import org.openapitools.client.model.CarePlansList200Response;
import org.openapitools.client.model.CareTeamMember;
import org.openapitools.client.model.CareTeamMembersList200Response;
import org.openapitools.client.model.ClaimBillingNotes;
import org.openapitools.client.model.ClaimBillingNotesList200Response;
import org.openapitools.client.model.ClinicalNote;
import org.openapitools.client.model.ClinicalNoteFieldTypesList200Response;
import org.openapitools.client.model.ClinicalNoteFieldValuesList200Response;
import org.openapitools.client.model.ClinicalNoteTemplatesList200Response;
import org.openapitools.client.model.ClinicalNotesList200Response;
import org.openapitools.client.model.ConsentForm;
import org.openapitools.client.model.ConsentFormsList200Response;
import org.openapitools.client.model.CustomAppointmentFieldType;
import org.openapitools.client.model.CustomAppointmentFieldsList200Response;
import org.openapitools.client.model.CustomDemographicsList200Response;
import org.openapitools.client.model.CustomPatientFieldType;
import org.openapitools.client.model.CustomVitalType;
import org.openapitools.client.model.CustomVitalsList200Response;
import org.openapitools.client.model.DoctorFeeSchedule;
import org.openapitools.client.model.DocumentsList200Response;
import org.openapitools.client.model.EOBObject;
import org.openapitools.client.model.EobsList200Response;
import org.openapitools.client.model.FeeSchedulesList200Response;
import org.openapitools.client.model.ImplantableDevice;
import org.openapitools.client.model.ImplantableDevicesList200Response;
import org.openapitools.client.model.Insurance;
import org.openapitools.client.model.InsurancesList200Response;
import org.openapitools.client.model.LabDocumentsList200Response;
import org.openapitools.client.model.LabOrder;
import org.openapitools.client.model.LabOrderDocument;
import org.openapitools.client.model.LabOrdersList200Response;
import org.openapitools.client.model.LabResult;
import org.openapitools.client.model.LabResultsList200Response;
import org.openapitools.client.model.LabTest;
import org.openapitools.client.model.LabTestsList200Response;
import org.openapitools.client.model.LabVendorLocation;
import org.openapitools.client.model.MedicationsList200Response;
import org.openapitools.client.model.Patient;
import org.openapitools.client.model.PatientAllergy;
import org.openapitools.client.model.PatientAmendment;
import org.openapitools.client.model.PatientCommunication;
import org.openapitools.client.model.PatientCommunicationsList200Response;
import org.openapitools.client.model.PatientDrug;
import org.openapitools.client.model.PatientFlagType;
import org.openapitools.client.model.PatientFlagTypesList200Response;
import org.openapitools.client.model.PatientIntervention;
import org.openapitools.client.model.PatientInterventionsList200Response;
import org.openapitools.client.model.PatientLabResultSet;
import org.openapitools.client.model.PatientLabResultsList200Response;
import org.openapitools.client.model.PatientMessage;
import org.openapitools.client.model.PatientMessagesList200Response;
import org.openapitools.client.model.PatientPhysicalExam;
import org.openapitools.client.model.PatientPhysicalExamsList200Response;
import org.openapitools.client.model.PatientProblem;
import org.openapitools.client.model.PatientRiskAssessment;
import org.openapitools.client.model.PatientRiskAssessmentsList200Response;
import org.openapitools.client.model.PatientVaccineRecord;
import org.openapitools.client.model.PatientVaccineRecordsList200Response;
import org.openapitools.client.model.PatientsList200Response;
import org.openapitools.client.model.PrescriptionMessage;
import org.openapitools.client.model.PrescriptionMessagesList200Response;
import org.openapitools.client.model.ProblemsList200Response;
import org.openapitools.client.model.ReminderProfile;
import org.openapitools.client.model.ReminderProfilesList200Response;
import org.openapitools.client.model.ScannedClinicalDocument;
import org.openapitools.client.model.SoapNoteCustomReport;
import org.openapitools.client.model.SoapNoteLineItemFieldType;
import org.openapitools.client.model.SoapNoteLineItemFieldValue;
import org.openapitools.client.model.SublabsList200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ClinicalApi
 */
@Disabled
public class ClinicalApiTest {

    private final ClinicalApi api = new ClinicalApi();

    /**
     * Create patient allergy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void allergiesCreateTest() throws ApiException {
        Integer patient = null;
        Integer doctor = null;
        PatientAllergy response = api.allergiesCreate(patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient allergies
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void allergiesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer doctor = null;
        AllergiesList200Response response = api.allergiesList(cursor, pageSize, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient allergy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void allergiesPartialUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.allergiesPartialUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient allergy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void allergiesReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        PatientAllergy response = api.allergiesRead(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient allergy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void allergiesUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.allergiesUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create patient amendments to a patient&#39;s clinical records
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void amendmentsCreateTest() throws ApiException {
        Integer appointment = null;
        Integer patient = null;
        Integer doctor = null;
        PatientAmendment response = api.amendmentsCreate(appointment, patient, doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing patient amendment, you can only interact with amendments created by your API application
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void amendmentsDeleteTest() throws ApiException {
        String id = null;
        Integer appointment = null;
        Integer patient = null;
        Integer doctor = null;
        api.amendmentsDelete(id, appointment, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient amendments. You can only interact with amendments created by your API application
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void amendmentsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer appointment = null;
        Integer patient = null;
        Integer doctor = null;
        AmendmentsList200Response response = api.amendmentsList(cursor, pageSize, appointment, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient amendment, you can only interact with amendments created by your API application
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void amendmentsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer appointment = null;
        Integer patient = null;
        Integer doctor = null;
        api.amendmentsPartialUpdate(id, appointment, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient amendment, you can only interact with amendments created by your API application
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void amendmentsReadTest() throws ApiException {
        String id = null;
        Integer appointment = null;
        Integer patient = null;
        Integer doctor = null;
        PatientAmendment response = api.amendmentsRead(id, appointment, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient amendment, you can only interact with amendments created by your API application
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void amendmentsUpdateTest() throws ApiException {
        String id = null;
        Integer appointment = null;
        Integer patient = null;
        Integer doctor = null;
        api.amendmentsUpdate(id, appointment, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create appointment profiles for a doctor&#39;s calendar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentProfilesCreateTest() throws ApiException {
        Integer doctor = null;
        AppointmentProfile response = api.appointmentProfilesCreate(doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing appointment profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentProfilesDeleteTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.appointmentProfilesDelete(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search appointment profiles for a doctor&#39;s calendar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentProfilesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        AppointmentProfilesList200Response response = api.appointmentProfilesList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing appointment profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentProfilesPartialUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.appointmentProfilesPartialUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing appointment profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentProfilesReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        AppointmentProfile response = api.appointmentProfilesRead(id, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing appointment profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentProfilesUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.appointmentProfilesUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Create appointment templates for a doctor&#39;s calendar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentTemplatesCreateTest() throws ApiException {
        Integer profile = null;
        Integer office = null;
        Integer doctor = null;
        AppointmentTemplate response = api.appointmentTemplatesCreate(profile, office, doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentTemplatesDeleteTest() throws ApiException {
        String id = null;
        Integer profile = null;
        Integer office = null;
        Integer doctor = null;
        api.appointmentTemplatesDelete(id, profile, office, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search appointment templates for a doctor&#39;s calendar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentTemplatesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer profile = null;
        Integer office = null;
        Integer doctor = null;
        AppointmentTemplatesList200Response response = api.appointmentTemplatesList(cursor, pageSize, profile, office, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentTemplatesPartialUpdateTest() throws ApiException {
        String id = null;
        Integer profile = null;
        Integer office = null;
        Integer doctor = null;
        api.appointmentTemplatesPartialUpdate(id, profile, office, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentTemplatesReadTest() throws ApiException {
        String id = null;
        Integer profile = null;
        Integer office = null;
        Integer doctor = null;
        AppointmentTemplate response = api.appointmentTemplatesRead(id, profile, office, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentTemplatesUpdateTest() throws ApiException {
        String id = null;
        Integer profile = null;
        Integer office = null;
        Integer doctor = null;
        api.appointmentTemplatesUpdate(id, profile, office, doctor);
        // TODO: test validations
    }

    /**
     * Create a new appointment or break on doctor&#39;s calendar
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentsCreateTest() throws ApiException {
        String status = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        Appointment response = api.appointmentsCreate(status, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * Delete an existing appointment or break
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentsDeleteTest() throws ApiException {
        String id = null;
        String status = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        api.appointmentsDelete(id, status, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * Retrieve or search appointment or breaks. &lt;b&gt;Note:&lt;/b&gt; Either &#x60;since&#x60;, &#x60;date&#x60; or &#x60;date_range&#x60; parameter must be specified.             
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String status = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        AppointmentsList200Response response = api.appointmentsList(cursor, pageSize, status, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * Update an existing appointment or break
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentsPartialUpdateTest() throws ApiException {
        String id = null;
        String status = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        api.appointmentsPartialUpdate(id, status, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * Retrieve an existing appointment or break
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentsReadTest() throws ApiException {
        String id = null;
        String status = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        Appointment response = api.appointmentsRead(id, status, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * Update an existing appointment or break
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void appointmentsUpdateTest() throws ApiException {
        String id = null;
        String status = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        api.appointmentsUpdate(id, status, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * Retrieve or search care plans
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void carePlansListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer planType = null;
        Integer doctor = null;
        CarePlansList200Response response = api.carePlansList(cursor, pageSize, patient, planType, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing care plan
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void carePlansReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer planType = null;
        Integer doctor = null;
        CarePlan response = api.carePlansRead(id, patient, planType, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void careTeamMembersListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer appointment = null;
        Integer doctor = null;
        CareTeamMembersList200Response response = api.careTeamMembersList(cursor, pageSize, patient, appointment, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void careTeamMembersReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer appointment = null;
        Integer doctor = null;
        CareTeamMember response = api.careTeamMembersRead(id, patient, appointment, doctor);
        // TODO: test validations
    }

    /**
     * Create a new billing note
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void claimBillingNotesCreateTest() throws ApiException {
        Integer appointment = null;
        Integer doctor = null;
        ClaimBillingNotes response = api.claimBillingNotesCreate(appointment, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search billing notes
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void claimBillingNotesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer appointment = null;
        Integer doctor = null;
        ClaimBillingNotesList200Response response = api.claimBillingNotesList(cursor, pageSize, appointment, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing billing note
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void claimBillingNotesReadTest() throws ApiException {
        String id = null;
        Integer appointment = null;
        Integer doctor = null;
        ClaimBillingNotes response = api.claimBillingNotesRead(id, appointment, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search clinical note field types
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteFieldTypesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer clinicalNoteTemplate = null;
        Integer doctor = null;
        ClinicalNoteFieldTypesList200Response response = api.clinicalNoteFieldTypesList(cursor, pageSize, clinicalNoteTemplate, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing clinial note field type
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteFieldTypesReadTest() throws ApiException {
        String id = null;
        Integer clinicalNoteTemplate = null;
        Integer doctor = null;
        SoapNoteLineItemFieldType response = api.clinicalNoteFieldTypesRead(id, clinicalNoteTemplate, doctor);
        // TODO: test validations
    }

    /**
     * Create clinical note field value
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteFieldValuesCreateTest() throws ApiException {
        Integer clinicalNoteField = null;
        String since = null;
        Integer appointment = null;
        Integer clinicalNoteTemplate = null;
        Integer doctor = null;
        SoapNoteLineItemFieldValue response = api.clinicalNoteFieldValuesCreate(clinicalNoteField, since, appointment, clinicalNoteTemplate, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search clinical note field values
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteFieldValuesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer clinicalNoteField = null;
        String since = null;
        Integer appointment = null;
        Integer clinicalNoteTemplate = null;
        Integer doctor = null;
        ClinicalNoteFieldValuesList200Response response = api.clinicalNoteFieldValuesList(cursor, pageSize, clinicalNoteField, since, appointment, clinicalNoteTemplate, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing clinical note field value
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteFieldValuesPartialUpdateTest() throws ApiException {
        String id = null;
        Integer clinicalNoteField = null;
        String since = null;
        Integer appointment = null;
        Integer clinicalNoteTemplate = null;
        Integer doctor = null;
        api.clinicalNoteFieldValuesPartialUpdate(id, clinicalNoteField, since, appointment, clinicalNoteTemplate, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing clinical note field value
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteFieldValuesReadTest() throws ApiException {
        String id = null;
        Integer clinicalNoteField = null;
        String since = null;
        Integer appointment = null;
        Integer clinicalNoteTemplate = null;
        Integer doctor = null;
        SoapNoteLineItemFieldValue response = api.clinicalNoteFieldValuesRead(id, clinicalNoteField, since, appointment, clinicalNoteTemplate, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing clinical note field value
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteFieldValuesUpdateTest() throws ApiException {
        String id = null;
        Integer clinicalNoteField = null;
        String since = null;
        Integer appointment = null;
        Integer clinicalNoteTemplate = null;
        Integer doctor = null;
        api.clinicalNoteFieldValuesUpdate(id, clinicalNoteField, since, appointment, clinicalNoteTemplate, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search clinical note templates
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteTemplatesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        ClinicalNoteTemplatesList200Response response = api.clinicalNoteTemplatesList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing clinical note tempalte
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNoteTemplatesReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        SoapNoteCustomReport response = api.clinicalNoteTemplatesRead(id, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNotesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        ClinicalNotesList200Response response = api.clinicalNotesList(cursor, pageSize, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void clinicalNotesReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer office = null;
        Integer doctor = null;
        String since = null;
        String dateRange = null;
        String date = null;
        ClinicalNote response = api.clinicalNotesRead(id, patient, office, doctor, since, dateRange, date);
        // TODO: test validations
    }

    /**
     * Assign (apply) a consent form to appointment
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consentFormsApplyToAppointmentTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.consentFormsApplyToAppointment(id, doctor);
        // TODO: test validations
    }

    /**
     * Create a patient consent form
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consentFormsCreateTest() throws ApiException {
        Integer doctor = null;
        ConsentForm response = api.consentFormsCreate(doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient consent forms
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consentFormsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        ConsentFormsList200Response response = api.consentFormsList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient consent form
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consentFormsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.consentFormsPartialUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient consent form
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consentFormsReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        ConsentForm response = api.consentFormsRead(id, doctor);
        // TODO: test validations
    }

    /**
     * Unassign (unapply) a consent form from appointment
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consentFormsUnapplyFromAppointmentTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.consentFormsUnapplyFromAppointment(id, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient consent form
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consentFormsUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.consentFormsUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Create custom appointment fields
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customAppointmentFieldsCreateTest() throws ApiException {
        Integer doctor = null;
        CustomAppointmentFieldType response = api.customAppointmentFieldsCreate(doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search custom appointment fields
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customAppointmentFieldsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        CustomAppointmentFieldsList200Response response = api.customAppointmentFieldsList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing custom appointment field
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customAppointmentFieldsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.customAppointmentFieldsPartialUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing custom appointment field
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customAppointmentFieldsReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        CustomAppointmentFieldType response = api.customAppointmentFieldsRead(id, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing custom appointment field
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customAppointmentFieldsUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.customAppointmentFieldsUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Create custom demographics fields
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customDemographicsCreateTest() throws ApiException {
        Integer doctor = null;
        CustomPatientFieldType response = api.customDemographicsCreate(doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search custom demographics fields
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customDemographicsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        CustomDemographicsList200Response response = api.customDemographicsList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing custom demographics field
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customDemographicsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.customDemographicsPartialUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing custom demographics field
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customDemographicsReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        CustomPatientFieldType response = api.customDemographicsRead(id, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing custom demographics field
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customDemographicsUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.customDemographicsUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search custom vital types
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customVitalsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        CustomVitalsList200Response response = api.customVitalsList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing custom vital type
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customVitalsReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        CustomVitalType response = api.customVitalsRead(id, doctor);
        // TODO: test validations
    }

    /**
     * Create documents
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsCreateTest() throws ApiException {
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        ScannedClinicalDocument response = api.documentsCreate(since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsDeleteTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.documentsDelete(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search documents
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        DocumentsList200Response response = api.documentsList(cursor, pageSize, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsPartialUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.documentsPartialUpdate(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsReadTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        ScannedClinicalDocument response = api.documentsRead(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing appointment template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.documentsUpdate(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create EOB object
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void eobsCreateTest() throws ApiException {
        Integer doctor = null;
        EOBObject response = api.eobsCreate(doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search EOB objects
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void eobsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        EobsList200Response response = api.eobsList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing EOB object
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void eobsReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        EOBObject response = api.eobsRead(id, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void feeSchedulesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String code = null;
        String codeType = null;
        String since = null;
        String payerId = null;
        Integer doctor = null;
        FeeSchedulesList200Response response = api.feeSchedulesList(cursor, pageSize, code, codeType, since, payerId, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void feeSchedulesReadTest() throws ApiException {
        String id = null;
        String code = null;
        String codeType = null;
        String since = null;
        String payerId = null;
        Integer doctor = null;
        DoctorFeeSchedule response = api.feeSchedulesRead(id, code, codeType, since, payerId, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search implantable devices
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void implantableDevicesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String muDate = null;
        Integer patient = null;
        String muDateRange = null;
        Integer doctor = null;
        ImplantableDevicesList200Response response = api.implantableDevicesList(cursor, pageSize, muDate, patient, muDateRange, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing implantable device
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void implantableDevicesReadTest() throws ApiException {
        String id = null;
        String muDate = null;
        Integer patient = null;
        String muDateRange = null;
        Integer doctor = null;
        ImplantableDevice response = api.implantableDevicesRead(id, muDate, patient, muDateRange, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void insurancesListTest() throws ApiException {
        String payerType = null;
        String cursor = null;
        Integer pageSize = null;
        String term = null;
        InsurancesList200Response response = api.insurancesList(payerType, cursor, pageSize, term);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void insurancesReadTest() throws ApiException {
        String id = null;
        String payerType = null;
        String term = null;
        Insurance response = api.insurancesRead(id, payerType, term);
        // TODO: test validations
    }

    /**
     * Create lab order documents. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labDocumentsCreateTest() throws ApiException {
        String since = null;
        Integer doctor = null;
        LabOrderDocument response = api.labDocumentsCreate(since, doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing lab order document
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labDocumentsDeleteTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        api.labDocumentsDelete(id, since, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search lab order documents
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labDocumentsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String since = null;
        Integer doctor = null;
        LabDocumentsList200Response response = api.labDocumentsList(cursor, pageSize, since, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab order document
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labDocumentsPartialUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        api.labDocumentsPartialUpdate(id, since, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing lab order document
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labDocumentsReadTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        LabOrderDocument response = api.labDocumentsRead(id, since, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab order document
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labDocumentsUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        api.labDocumentsUpdate(id, since, doctor);
        // TODO: test validations
    }

    /**
     * Create lab orders. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersCreateTest() throws ApiException {
        String since = null;
        Integer doctor = null;
        LabOrder response = api.labOrdersCreate(since, doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing lab order
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersDeleteTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        api.labOrdersDelete(id, since, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search lab orders
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String since = null;
        Integer doctor = null;
        LabOrdersList200Response response = api.labOrdersList(cursor, pageSize, since, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab order
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersPartialUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        api.labOrdersPartialUpdate(id, since, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing lab order
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersReadTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        LabOrder response = api.labOrdersRead(id, since, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersSummaryListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        LabOrdersList200Response response = api.labOrdersSummaryList(cursor, pageSize, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersSummaryReadTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        LabOrder response = api.labOrdersSummaryRead(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab order
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labOrdersUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer doctor = null;
        api.labOrdersUpdate(id, since, doctor);
        // TODO: test validations
    }

    /**
     * Create lab results. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labResultsCreateTest() throws ApiException {
        Integer order = null;
        Integer doctor = null;
        LabResult response = api.labResultsCreate(order, doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing lab result
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labResultsDeleteTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        api.labResultsDelete(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search lab results
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labResultsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer order = null;
        Integer doctor = null;
        LabResultsList200Response response = api.labResultsList(cursor, pageSize, order, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab result
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labResultsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        api.labResultsPartialUpdate(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing lab result
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labResultsReadTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        LabResult response = api.labResultsRead(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab result
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labResultsUpdateTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        api.labResultsUpdate(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Create lab tests. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labTestsCreateTest() throws ApiException {
        Integer order = null;
        Integer doctor = null;
        LabTest response = api.labTestsCreate(order, doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing lab test
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labTestsDeleteTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        api.labTestsDelete(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search lab tests
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labTestsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer order = null;
        Integer doctor = null;
        LabTestsList200Response response = api.labTestsList(cursor, pageSize, order, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab test
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labTestsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        api.labTestsPartialUpdate(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing lab test
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labTestsReadTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        LabTest response = api.labTestsRead(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing lab test
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void labTestsUpdateTest() throws ApiException {
        String id = null;
        Integer order = null;
        Integer doctor = null;
        api.labTestsUpdate(id, order, doctor);
        // TODO: test validations
    }

    /**
     * Append a message to the \&quot;pharmacy_note\&quot; section of the prescription, in a new paragraph
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void medicationsAppendToPharmacyNoteTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.medicationsAppendToPharmacyNote(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create patient medications
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void medicationsCreateTest() throws ApiException {
        Integer patient = null;
        Integer doctor = null;
        PatientDrug response = api.medicationsCreate(patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient medications
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void medicationsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer doctor = null;
        MedicationsList200Response response = api.medicationsList(cursor, pageSize, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient medications
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void medicationsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.medicationsPartialUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient medications
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void medicationsReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        PatientDrug response = api.medicationsRead(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient medications
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void medicationsUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.medicationsUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create patient communication for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientCommunicationsCreateTest() throws ApiException {
        Integer patient = null;
        Integer doctor = null;
        PatientCommunication response = api.patientCommunicationsCreate(patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient communications for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientCommunicationsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer doctor = null;
        PatientCommunicationsList200Response response = api.patientCommunicationsList(cursor, pageSize, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient communication for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientCommunicationsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientCommunicationsPartialUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient communication for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientCommunicationsReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        PatientCommunication response = api.patientCommunicationsRead(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient communication for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientCommunicationsUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientCommunicationsUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create patient flag types
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientFlagTypesCreateTest() throws ApiException {
        Integer doctor = null;
        PatientFlagType response = api.patientFlagTypesCreate(doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient flag types
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientFlagTypesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        PatientFlagTypesList200Response response = api.patientFlagTypesList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient flag type
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientFlagTypesPartialUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.patientFlagTypesPartialUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient flag type
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientFlagTypesReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        PatientFlagType response = api.patientFlagTypesRead(id, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient flag type
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientFlagTypesUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.patientFlagTypesUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Create patient intervention for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientInterventionsCreateTest() throws ApiException {
        Integer patient = null;
        Integer doctor = null;
        PatientIntervention response = api.patientInterventionsCreate(patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient interventions for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientInterventionsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer doctor = null;
        PatientInterventionsList200Response response = api.patientInterventionsList(cursor, pageSize, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient intervention for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientInterventionsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientInterventionsPartialUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient intervention for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientInterventionsReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        PatientIntervention response = api.patientInterventionsRead(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient intervention for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientInterventionsUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientInterventionsUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientLabResultsCreateTest() throws ApiException {
        Integer orderingDoctor = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PatientLabResultSet response = api.patientLabResultsCreate(orderingDoctor, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientLabResultsDeleteTest() throws ApiException {
        String id = null;
        Integer orderingDoctor = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientLabResultsDelete(id, orderingDoctor, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientLabResultsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer orderingDoctor = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PatientLabResultsList200Response response = api.patientLabResultsList(cursor, pageSize, orderingDoctor, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientLabResultsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer orderingDoctor = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientLabResultsPartialUpdate(id, orderingDoctor, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientLabResultsReadTest() throws ApiException {
        String id = null;
        Integer orderingDoctor = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PatientLabResultSet response = api.patientLabResultsRead(id, orderingDoctor, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientLabResultsUpdateTest() throws ApiException {
        String id = null;
        Integer orderingDoctor = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientLabResultsUpdate(id, orderingDoctor, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientMessagesCreateTest() throws ApiException {
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PatientMessage response = api.patientMessagesCreate(since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientMessagesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PatientMessagesList200Response response = api.patientMessagesList(cursor, pageSize, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientMessagesPartialUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientMessagesPartialUpdate(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientMessagesReadTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PatientMessage response = api.patientMessagesRead(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientMessagesUpdateTest() throws ApiException {
        String id = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientMessagesUpdate(id, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create patient physical exam for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientPhysicalExamsCreateTest() throws ApiException {
        Integer patient = null;
        Integer doctor = null;
        PatientPhysicalExam response = api.patientPhysicalExamsCreate(patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient physical exams for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientPhysicalExamsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer doctor = null;
        PatientPhysicalExamsList200Response response = api.patientPhysicalExamsList(cursor, pageSize, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient physical exam for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientPhysicalExamsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientPhysicalExamsPartialUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient physical exam for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientPhysicalExamsReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        PatientPhysicalExam response = api.patientPhysicalExamsRead(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient physical exam for CQM
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientPhysicalExamsUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientPhysicalExamsUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientRiskAssessmentsCreateTest() throws ApiException {
        Integer patient = null;
        Integer doctor = null;
        PatientRiskAssessment response = api.patientRiskAssessmentsCreate(patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientRiskAssessmentsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer doctor = null;
        PatientRiskAssessmentsList200Response response = api.patientRiskAssessmentsList(cursor, pageSize, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientRiskAssessmentsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientRiskAssessmentsPartialUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientRiskAssessmentsReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        PatientRiskAssessment response = api.patientRiskAssessmentsRead(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientRiskAssessmentsUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.patientRiskAssessmentsUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create patient vaccine records
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientVaccineRecordsCreateTest() throws ApiException {
        String cvxCode = null;
        Integer patient = null;
        String since = null;
        Integer doctor = null;
        PatientVaccineRecord response = api.patientVaccineRecordsCreate(cvxCode, patient, since, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient vaccine records
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientVaccineRecordsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String cvxCode = null;
        Integer patient = null;
        String since = null;
        Integer doctor = null;
        PatientVaccineRecordsList200Response response = api.patientVaccineRecordsList(cursor, pageSize, cvxCode, patient, since, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient vaccine records
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientVaccineRecordsPartialUpdateTest() throws ApiException {
        String id = null;
        String cvxCode = null;
        Integer patient = null;
        String since = null;
        Integer doctor = null;
        api.patientVaccineRecordsPartialUpdate(id, cvxCode, patient, since, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient vaccine records
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientVaccineRecordsReadTest() throws ApiException {
        String id = null;
        String cvxCode = null;
        Integer patient = null;
        String since = null;
        Integer doctor = null;
        PatientVaccineRecord response = api.patientVaccineRecordsRead(id, cvxCode, patient, since, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient vaccine records
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientVaccineRecordsUpdateTest() throws ApiException {
        String id = null;
        String cvxCode = null;
        Integer patient = null;
        String since = null;
        Integer doctor = null;
        api.patientVaccineRecordsUpdate(id, cvxCode, patient, since, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve patient CCDA
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsCcdaTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        Object response = api.patientsCcda(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Create patient
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsCreateTest() throws ApiException {
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        Patient response = api.patientsCreate(firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Delete an existing patient
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsDeleteTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        api.patientsDelete(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Retrieve or search patients
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        PatientsList200Response response = api.patientsList(cursor, pageSize, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Send new onpatient invite to patient
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsOnpatientAccessCreateTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        Patient response = api.patientsOnpatientAccessCreate(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Revoke sent onpatient invites
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsOnpatientAccessDeleteTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        api.patientsOnpatientAccessDelete(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Retrieve or search existing onpatient access invites
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsOnpatientAccessReadTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        Patient response = api.patientsOnpatientAccessRead(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Update an existing patient
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsPartialUpdateTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        api.patientsPartialUpdate(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Retrieve patient QRDA1
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsQrda1Test() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        Object response = api.patientsQrda1(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsReadTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        Patient response = api.patientsRead(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsSummaryCreateTest() throws ApiException {
        String firstName = null;
        String lastName = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        Patient response = api.patientsSummaryCreate(firstName, lastName, doctor, gender, since, dateOfBirth);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsSummaryDeleteTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        api.patientsSummaryDelete(id, firstName, lastName, doctor, gender, since, dateOfBirth);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsSummaryListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        String firstName = null;
        String lastName = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        PatientsList200Response response = api.patientsSummaryList(cursor, pageSize, firstName, lastName, doctor, gender, since, dateOfBirth);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsSummaryPartialUpdateTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        api.patientsSummaryPartialUpdate(id, firstName, lastName, doctor, gender, since, dateOfBirth);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsSummaryReadTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        Patient response = api.patientsSummaryRead(id, firstName, lastName, doctor, gender, since, dateOfBirth);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsSummaryUpdateTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        api.patientsSummaryUpdate(id, firstName, lastName, doctor, gender, since, dateOfBirth);
        // TODO: test validations
    }

    /**
     * Update an existing patient
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patientsUpdateTest() throws ApiException {
        String id = null;
        String firstName = null;
        String lastName = null;
        String preferredLanguage = null;
        Integer doctor = null;
        String gender = null;
        String since = null;
        String dateOfBirth = null;
        String race = null;
        String chartId = null;
        String email = null;
        String ethnicity = null;
        api.patientsUpdate(id, firstName, lastName, preferredLanguage, doctor, gender, since, dateOfBirth, race, chartId, email, ethnicity);
        // TODO: test validations
    }

    /**
     * Retrieve or search prescription messages
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void prescriptionMessagesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer parentMessage = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PrescriptionMessagesList200Response response = api.prescriptionMessagesList(cursor, pageSize, parentMessage, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing prescription message
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void prescriptionMessagesReadTest() throws ApiException {
        String id = null;
        Integer parentMessage = null;
        String since = null;
        Integer patient = null;
        Integer doctor = null;
        PrescriptionMessage response = api.prescriptionMessagesRead(id, parentMessage, since, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create patient problems
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void problemsCreateTest() throws ApiException {
        Integer patient = null;
        Integer doctor = null;
        PatientProblem response = api.problemsCreate(patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search patient problems
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void problemsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer patient = null;
        Integer doctor = null;
        ProblemsList200Response response = api.problemsList(cursor, pageSize, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient problems
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void problemsPartialUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.problemsPartialUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing patient problems
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void problemsReadTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        PatientProblem response = api.problemsRead(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing patient problems
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void problemsUpdateTest() throws ApiException {
        String id = null;
        Integer patient = null;
        Integer doctor = null;
        api.problemsUpdate(id, patient, doctor);
        // TODO: test validations
    }

    /**
     * Create reminder profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reminderProfilesCreateTest() throws ApiException {
        Integer doctor = null;
        ReminderProfile response = api.reminderProfilesCreate(doctor);
        // TODO: test validations
    }

    /**
     * Delete an existing reminder profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reminderProfilesDeleteTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.reminderProfilesDelete(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve or search reminder profiles
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reminderProfilesListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        Integer doctor = null;
        ReminderProfilesList200Response response = api.reminderProfilesList(cursor, pageSize, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing reminder profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reminderProfilesPartialUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.reminderProfilesPartialUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Retrieve an existing reminder profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reminderProfilesReadTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        ReminderProfile response = api.reminderProfilesRead(id, doctor);
        // TODO: test validations
    }

    /**
     * Update an existing reminder profile
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reminderProfilesUpdateTest() throws ApiException {
        String id = null;
        Integer doctor = null;
        api.reminderProfilesUpdate(id, doctor);
        // TODO: test validations
    }

    /**
     * Create sub-vendors  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sublabsCreateTest() throws ApiException {
        LabVendorLocation response = api.sublabsCreate();
        // TODO: test validations
    }

    /**
     * Delete an existing sub vendor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sublabsDeleteTest() throws ApiException {
        Integer id = null;
        api.sublabsDelete(id);
        // TODO: test validations
    }

    /**
     * Retrieve or search sub vendors
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sublabsListTest() throws ApiException {
        String cursor = null;
        Integer pageSize = null;
        SublabsList200Response response = api.sublabsList(cursor, pageSize);
        // TODO: test validations
    }

    /**
     * Update an existing sub vendor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sublabsPartialUpdateTest() throws ApiException {
        Integer id = null;
        api.sublabsPartialUpdate(id);
        // TODO: test validations
    }

    /**
     * Retrieve an existing sub vendor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sublabsReadTest() throws ApiException {
        Integer id = null;
        LabVendorLocation response = api.sublabsRead(id);
        // TODO: test validations
    }

    /**
     * Update an existing sub vendor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sublabsUpdateTest() throws ApiException {
        Integer id = null;
        api.sublabsUpdate(id);
        // TODO: test validations
    }

}
