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


package org.openapitools.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.Arrays;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * Coverage
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Coverage {
  public static final String SERIALIZED_NAME_APPOINTMENT = "appointment";
  @SerializedName(SERIALIZED_NAME_APPOINTMENT)
  private String appointment;

  public static final String SERIALIZED_NAME_COB_LEVEL = "cob_level";
  @SerializedName(SERIALIZED_NAME_COB_LEVEL)
  private String cobLevel;

  public static final String SERIALIZED_NAME_COVERAGE_DETAILS = "coverage_details";
  @SerializedName(SERIALIZED_NAME_COVERAGE_DETAILS)
  private String coverageDetails;

  public static final String SERIALIZED_NAME_COVERAGE_SUBSCRIBER = "coverage_subscriber";
  @SerializedName(SERIALIZED_NAME_COVERAGE_SUBSCRIBER)
  private String coverageSubscriber;

  public static final String SERIALIZED_NAME_ELIGIBILITY = "eligibility";
  @SerializedName(SERIALIZED_NAME_ELIGIBILITY)
  private String eligibility;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private String patient;

  public static final String SERIALIZED_NAME_PAYER_NAME = "payer_name";
  @SerializedName(SERIALIZED_NAME_PAYER_NAME)
  private String payerName;

  public static final String SERIALIZED_NAME_QUERY_DATE = "query_date";
  @SerializedName(SERIALIZED_NAME_QUERY_DATE)
  private String queryDate;

  /**
   *  Value | Description --- | ---- &#x60;&#39;1&#39;&#x60; | Medical Care &#x60;&#39;2&#39;&#x60; | Surgical &#x60;&#39;3&#39;&#x60; | Consultation &#x60;&#39;4&#39;&#x60; | Diagnostic X-Ray &#x60;&#39;5&#39;&#x60; | Diagnostic Lab &#x60;&#39;6&#39;&#x60; | Radiation Therapy &#x60;&#39;7&#39;&#x60; | Anesthesia &#x60;&#39;8&#39;&#x60; | Surgical Assistance &#x60;&#39;9&#39;&#x60; | Other Medical &#x60;&#39;10&#39;&#x60; | Blood Charges &#x60;&#39;11&#39;&#x60; | Used Durable Medical Equipment &#x60;&#39;12&#39;&#x60; | Durable Medical Equipment Purchase &#x60;&#39;13&#39;&#x60; | Ambulatory Service Center Facility &#x60;&#39;14&#39;&#x60; | Renal Supplies in the Home &#x60;&#39;15&#39;&#x60; | Alternate Method Dialysis &#x60;&#39;16&#39;&#x60; | Chronic Renal Disease (CRD) Equipment &#x60;&#39;17&#39;&#x60; | Pre-Admission Testing &#x60;&#39;18&#39;&#x60; | Durable Medical Equipment Rental &#x60;&#39;19&#39;&#x60; | Pneumonia Vaccine &#x60;&#39;20&#39;&#x60; | Second Surgical Opinion &#x60;&#39;21&#39;&#x60; | Third Surgical Opinion &#x60;&#39;22&#39;&#x60; | Social Work &#x60;&#39;23&#39;&#x60; | Diagnostic Dental &#x60;&#39;24&#39;&#x60; | Periodontics &#x60;&#39;25&#39;&#x60; | Restorative &#x60;&#39;26&#39;&#x60; | Endodontics &#x60;&#39;27&#39;&#x60; | Maxillofacial Prosthetics &#x60;&#39;28&#39;&#x60; | Adjunctive Dental Services &#x60;&#39;30&#39;&#x60; | Health Benefit Plan Coverage &#x60;&#39;32&#39;&#x60; | Plan Waiting Period &#x60;&#39;33&#39;&#x60; | Chiropractic &#x60;&#39;34&#39;&#x60; | Chiropractic Office Visits &#x60;&#39;35&#39;&#x60; | Dental Care &#x60;&#39;36&#39;&#x60; | Dental Crowns &#x60;&#39;37&#39;&#x60; | Dental Accident &#x60;&#39;38&#39;&#x60; | Orthodontics &#x60;&#39;39&#39;&#x60; | Prosthodontics &#x60;&#39;40&#39;&#x60; | Oral Surgery &#x60;&#39;41&#39;&#x60; | Routine (Preventive) Dental &#x60;&#39;42&#39;&#x60; | Home Health Care &#x60;&#39;43&#39;&#x60; | Home Health Prescriptions &#x60;&#39;44&#39;&#x60; | Home Health Visits &#x60;&#39;45&#39;&#x60; | Hospice &#x60;&#39;46&#39;&#x60; | Respite Care &#x60;&#39;47&#39;&#x60; | Hospital &#x60;&#39;48&#39;&#x60; | Hospital - Inpatient &#x60;&#39;49&#39;&#x60; | Hospital - Room and Board &#x60;&#39;50&#39;&#x60; | Hospital - Outpatient &#x60;&#39;51&#39;&#x60; | Hospital - Emergency Accident &#x60;&#39;52&#39;&#x60; | Hospital - Emergency Medical &#x60;&#39;53&#39;&#x60; | Hospital - Ambulatory Surgical &#x60;&#39;54&#39;&#x60; | Long Term Care &#x60;&#39;55&#39;&#x60; | Major Medical &#x60;&#39;56&#39;&#x60; | Medically Related Transportation &#x60;&#39;57&#39;&#x60; | Air Transportation &#x60;&#39;58&#39;&#x60; | Cabulance &#x60;&#39;59&#39;&#x60; | Licensed Ambulance &#x60;&#39;60&#39;&#x60; | General Benefits &#x60;&#39;61&#39;&#x60; | In-vitro Fertilization &#x60;&#39;62&#39;&#x60; | MRI/CAT Scan &#x60;&#39;63&#39;&#x60; | Donor Procedures &#x60;&#39;64&#39;&#x60; | Acupuncture &#x60;&#39;65&#39;&#x60; | Newborn Care &#x60;&#39;66&#39;&#x60; | Pathology &#x60;&#39;67&#39;&#x60; | Smoking Cessation &#x60;&#39;68&#39;&#x60; | Well Baby Care &#x60;&#39;69&#39;&#x60; | Maternity &#x60;&#39;70&#39;&#x60; | Transplants &#x60;&#39;71&#39;&#x60; | Audiology Exam &#x60;&#39;72&#39;&#x60; | Inhalation Therapy &#x60;&#39;73&#39;&#x60; | Diagnostic Medical &#x60;&#39;74&#39;&#x60; | Private Duty Nursing &#x60;&#39;75&#39;&#x60; | Prosthetic Device &#x60;&#39;76&#39;&#x60; | Dialysis &#x60;&#39;77&#39;&#x60; | Otological Exam &#x60;&#39;78&#39;&#x60; | Chemotherapy &#x60;&#39;79&#39;&#x60; | Allergy Testing &#x60;&#39;80&#39;&#x60; | Immunizations &#x60;&#39;81&#39;&#x60; | Routine Physical &#x60;&#39;82&#39;&#x60; | Family Planning &#x60;&#39;83&#39;&#x60; | Infertility &#x60;&#39;84&#39;&#x60; | Abortion &#x60;&#39;85&#39;&#x60; | AIDS &#x60;&#39;86&#39;&#x60; | Emergency Services &#x60;&#39;87&#39;&#x60; | Cancer &#x60;&#39;88&#39;&#x60; | Pharmacy &#x60;&#39;89&#39;&#x60; | Free Standing Prescription Drug &#x60;&#39;90&#39;&#x60; | Mail Order Prescription Drug &#x60;&#39;91&#39;&#x60; | Brand Name Prescription Drug &#x60;&#39;92&#39;&#x60; | Generic Prescription Drug &#x60;&#39;93&#39;&#x60; | Podiatry &#x60;&#39;94&#39;&#x60; | Podiatry - Office Visits &#x60;&#39;95&#39;&#x60; | Podiatry - Nursing Home Visits &#x60;&#39;96&#39;&#x60; | Professional (Physician) &#x60;&#39;97&#39;&#x60; | Anesthesiologist &#x60;&#39;98&#39;&#x60; | Professional (Physician) Visit - Office &#x60;&#39;99&#39;&#x60; | Professional (Physician) Visit - Inpatient &#x60;&#39;A0&#39;&#x60; | Professional (Physician) Visit - Outpatient &#x60;&#39;A1&#39;&#x60; | Professional (Physician) Visit - Nursing Home &#x60;&#39;A2&#39;&#x60; | Professional (Physician) Visit - Skilled Nursing Facility &#x60;&#39;A3&#39;&#x60; | Professional (Physician) Visit - Home &#x60;&#39;A4&#39;&#x60; | Psychiatric &#x60;&#39;A5&#39;&#x60; | Psychiatric - Room and Board &#x60;&#39;A6&#39;&#x60; | Psychotherapy &#x60;&#39;A7&#39;&#x60; | Psychiatric - Inpatient &#x60;&#39;A8&#39;&#x60; | Psychiatric - Outpatient &#x60;&#39;A9&#39;&#x60; | Rehabilitation &#x60;&#39;AA&#39;&#x60; | Rehabilitation - Room and Board &#x60;&#39;AB&#39;&#x60; | Rehabilitation - Inpatient &#x60;&#39;AC&#39;&#x60; | Rehabilitation - Outpatient &#x60;&#39;AD&#39;&#x60; | Occupational Therapy &#x60;&#39;AE&#39;&#x60; | Physical Medicine &#x60;&#39;AF&#39;&#x60; | Speech Therapy &#x60;&#39;AG&#39;&#x60; | Skilled Nursing Care &#x60;&#39;AH&#39;&#x60; | Skilled Nursing Care - Room and Board &#x60;&#39;AI&#39;&#x60; | Substance Abuse &#x60;&#39;AJ&#39;&#x60; | Alcoholism &#x60;&#39;AK&#39;&#x60; | Drug Addiction &#x60;&#39;AL&#39;&#x60; | Vision (Optometry) &#x60;&#39;AM&#39;&#x60; | Frames &#x60;&#39;AN&#39;&#x60; | Routine Exam &#x60;&#39;AO&#39;&#x60; | Lenses &#x60;&#39;AQ&#39;&#x60; | Nonmedically Necessary Physical &#x60;&#39;AR&#39;&#x60; | Experimental Drug Therapy &#x60;&#39;B1&#39;&#x60; | Burn Care &#x60;&#39;B2&#39;&#x60; | Brand Name Prescription Drug - Formulary &#x60;&#39;B3&#39;&#x60; | Brand Name Prescription Drug - Non-Formulary &#x60;&#39;BA&#39;&#x60; | Independent Medical Evaluation &#x60;&#39;BB&#39;&#x60; | Partial Hospitalization (Psychiatric) &#x60;&#39;BC&#39;&#x60; | Day Care (Psychiatric) &#x60;&#39;BD&#39;&#x60; | Cognitive Therapy &#x60;&#39;BE&#39;&#x60; | Massage Therapy &#x60;&#39;BF&#39;&#x60; | Pulmonary Rehabilitation &#x60;&#39;BG&#39;&#x60; | Cardiac Rehabilitation &#x60;&#39;BH&#39;&#x60; | Pediatric &#x60;&#39;BI&#39;&#x60; | Nursery &#x60;&#39;BJ&#39;&#x60; | Skin &#x60;&#39;BK&#39;&#x60; | Orthopedic &#x60;&#39;BL&#39;&#x60; | Cardiac &#x60;&#39;BM&#39;&#x60; | Lymphatic &#x60;&#39;BN&#39;&#x60; | Gastrointestinal &#x60;&#39;BP&#39;&#x60; | Endocrine &#x60;&#39;BQ&#39;&#x60; | Neurology &#x60;&#39;BR&#39;&#x60; | Eye &#x60;&#39;BS&#39;&#x60; | Invasive Procedures &#x60;&#39;BT&#39;&#x60; | Gynecological &#x60;&#39;BU&#39;&#x60; | Obstetrical &#x60;&#39;BV&#39;&#x60; | Obstetrical/Gynecological &#x60;&#39;BW&#39;&#x60; | Mail Order Prescription Drug: Brand Name &#x60;&#39;BX&#39;&#x60; | Mail Order Prescription Drug: Generic &#x60;&#39;BY&#39;&#x60; | Physician Visit - Office: Sick &#x60;&#39;BZ&#39;&#x60; | Physician Visit - Office: Well &#x60;&#39;C1&#39;&#x60; | Coronary Care &#x60;&#39;CA&#39;&#x60; | Private Duty Nursing - Inpatient &#x60;&#39;CB&#39;&#x60; | Private Duty Nursing - Home &#x60;&#39;CC&#39;&#x60; | Surgical Benefits - Professional (Physician) &#x60;&#39;CD&#39;&#x60; | Surgical Benefits - Facility &#x60;&#39;CE&#39;&#x60; | Mental Health Provider - Inpatient &#x60;&#39;CF&#39;&#x60; | Mental Health Provider - Outpatient &#x60;&#39;CG&#39;&#x60; | Mental Health Facility - Inpatient &#x60;&#39;CH&#39;&#x60; | Mental Health Facility - Outpatient &#x60;&#39;CI&#39;&#x60; | Substance Abuse Facility - Inpatient &#x60;&#39;CJ&#39;&#x60; | Substance Abuse Facility - Outpatient &#x60;&#39;CK&#39;&#x60; | Screening X-ray &#x60;&#39;CL&#39;&#x60; | Screening laboratory &#x60;&#39;CM&#39;&#x60; | Mammogram, High Risk Patient &#x60;&#39;CN&#39;&#x60; | Mammogram, Low Risk Patient &#x60;&#39;CO&#39;&#x60; | Flu Vaccination &#x60;&#39;CP&#39;&#x60; | Eyewear and Eyewear Accessories &#x60;&#39;CQ&#39;&#x60; | Case Management &#x60;&#39;DG&#39;&#x60; | Dermatology &#x60;&#39;DM&#39;&#x60; | Durable Medical Equipment &#x60;&#39;DS&#39;&#x60; | Diabetic Supplies &#x60;&#39;GF&#39;&#x60; | Generic Prescription Drug - Formulary &#x60;&#39;GN&#39;&#x60; | Generic Prescription Drug - Non-Formulary &#x60;&#39;GY&#39;&#x60; | Allergy &#x60;&#39;IC&#39;&#x60; | Intensive Care &#x60;&#39;MH&#39;&#x60; | Mental Health &#x60;&#39;NI&#39;&#x60; | Neonatal Intensive Care &#x60;&#39;ON&#39;&#x60; | Oncology &#x60;&#39;PT&#39;&#x60; | Physical Therapy &#x60;&#39;PU&#39;&#x60; | Pulmonary &#x60;&#39;RN&#39;&#x60; | Renal &#x60;&#39;RT&#39;&#x60; | Residential Psychiatric Treatment &#x60;&#39;TC&#39;&#x60; | Transitional Care &#x60;&#39;TN&#39;&#x60; | Transitional Nursery Care &#x60;&#39;UC&#39;&#x60; | Urgent Care 
   */
  @JsonAdapter(RequestServiceTypeEnum.Adapter.class)
  public enum RequestServiceTypeEnum {
    _1("1"),
    
    _2("2"),
    
    _3("3"),
    
    _4("4"),
    
    _5("5"),
    
    _6("6"),
    
    _7("7"),
    
    _8("8"),
    
    _9("9"),
    
    _10("10"),
    
    _11("11"),
    
    _12("12"),
    
    _13("13"),
    
    _14("14"),
    
    _15("15"),
    
    _16("16"),
    
    _17("17"),
    
    _18("18"),
    
    _19("19"),
    
    _20("20"),
    
    _21("21"),
    
    _22("22"),
    
    _23("23"),
    
    _24("24"),
    
    _25("25"),
    
    _26("26"),
    
    _27("27"),
    
    _28("28"),
    
    _30("30"),
    
    _32("32"),
    
    _33("33"),
    
    _34("34"),
    
    _35("35"),
    
    _36("36"),
    
    _37("37"),
    
    _38("38"),
    
    _39("39"),
    
    _40("40"),
    
    _41("41"),
    
    _42("42"),
    
    _43("43"),
    
    _44("44"),
    
    _45("45"),
    
    _46("46"),
    
    _47("47"),
    
    _48("48"),
    
    _49("49"),
    
    _50("50"),
    
    _51("51"),
    
    _52("52"),
    
    _53("53"),
    
    _54("54"),
    
    _55("55"),
    
    _56("56"),
    
    _57("57"),
    
    _58("58"),
    
    _59("59"),
    
    _60("60"),
    
    _61("61"),
    
    _62("62"),
    
    _63("63"),
    
    _64("64"),
    
    _65("65"),
    
    _66("66"),
    
    _67("67"),
    
    _68("68"),
    
    _69("69"),
    
    _70("70"),
    
    _71("71"),
    
    _72("72"),
    
    _73("73"),
    
    _74("74"),
    
    _75("75"),
    
    _76("76"),
    
    _77("77"),
    
    _78("78"),
    
    _79("79"),
    
    _80("80"),
    
    _81("81"),
    
    _82("82"),
    
    _83("83"),
    
    _84("84"),
    
    _85("85"),
    
    _86("86"),
    
    _87("87"),
    
    _88("88"),
    
    _89("89"),
    
    _90("90"),
    
    _91("91"),
    
    _92("92"),
    
    _93("93"),
    
    _94("94"),
    
    _95("95"),
    
    _96("96"),
    
    _97("97"),
    
    _98("98"),
    
    _99("99"),
    
    A0("A0"),
    
    A1("A1"),
    
    A2("A2"),
    
    A3("A3"),
    
    A4("A4"),
    
    A5("A5"),
    
    A6("A6"),
    
    A7("A7"),
    
    A8("A8"),
    
    A9("A9"),
    
    AA("AA"),
    
    AB("AB"),
    
    AC("AC"),
    
    AD("AD"),
    
    AE("AE"),
    
    AF("AF"),
    
    AG("AG"),
    
    AH("AH"),
    
    AI("AI"),
    
    AJ("AJ"),
    
    AK("AK"),
    
    AL("AL"),
    
    AM("AM"),
    
    AN("AN"),
    
    AO("AO"),
    
    AQ("AQ"),
    
    AR("AR"),
    
    B1("B1"),
    
    B2("B2"),
    
    B3("B3"),
    
    BA("BA"),
    
    BB("BB"),
    
    BC("BC"),
    
    BD("BD"),
    
    BE("BE"),
    
    BF("BF"),
    
    BG("BG"),
    
    BH("BH"),
    
    BI("BI"),
    
    BJ("BJ"),
    
    BK("BK"),
    
    BL("BL"),
    
    BM("BM"),
    
    BN("BN"),
    
    BP("BP"),
    
    BQ("BQ"),
    
    BR("BR"),
    
    BS("BS"),
    
    BT("BT"),
    
    BU("BU"),
    
    BV("BV"),
    
    BW("BW"),
    
    BX("BX"),
    
    BY("BY"),
    
    BZ("BZ"),
    
    C1("C1"),
    
    CA("CA"),
    
    CB("CB"),
    
    CC("CC"),
    
    CD("CD"),
    
    CE("CE"),
    
    CF("CF"),
    
    CG("CG"),
    
    CH("CH"),
    
    CI("CI"),
    
    CJ("CJ"),
    
    CK("CK"),
    
    CL("CL"),
    
    CM("CM"),
    
    CN("CN"),
    
    CO("CO"),
    
    CP("CP"),
    
    CQ("CQ"),
    
    DG("DG"),
    
    DM("DM"),
    
    DS("DS"),
    
    GF("GF"),
    
    GN("GN"),
    
    GY("GY"),
    
    IC("IC"),
    
    MH("MH"),
    
    NI("NI"),
    
    TRUE("true"),
    
    PT("PT"),
    
    PU("PU"),
    
    RN("RN"),
    
    RT("RT"),
    
    TC("TC"),
    
    TN("TN"),
    
    UC("UC");

    private String value;

    RequestServiceTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RequestServiceTypeEnum fromValue(String value) {
      for (RequestServiceTypeEnum b : RequestServiceTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RequestServiceTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RequestServiceTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RequestServiceTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RequestServiceTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RequestServiceTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_REQUEST_SERVICE_TYPE = "request_service_type";
  @SerializedName(SERIALIZED_NAME_REQUEST_SERVICE_TYPE)
  private RequestServiceTypeEnum requestServiceType;

  public static final String SERIALIZED_NAME_SERVICE_TYPE_DESCRIPTION = "service_type_description";
  @SerializedName(SERIALIZED_NAME_SERVICE_TYPE_DESCRIPTION)
  private String serviceTypeDescription;

  public Coverage() {
  }

  public Coverage(
     String appointment, 
     String cobLevel, 
     String coverageDetails, 
     String coverageSubscriber, 
     String patient, 
     String queryDate, 
     String serviceTypeDescription
  ) {
    this();
    this.appointment = appointment;
    this.cobLevel = cobLevel;
    this.coverageDetails = coverageDetails;
    this.coverageSubscriber = coverageSubscriber;
    this.patient = patient;
    this.queryDate = queryDate;
    this.serviceTypeDescription = serviceTypeDescription;
  }

  /**
   * 
   * @return appointment
   */
  @javax.annotation.Nullable
  public String getAppointment() {
    return appointment;
  }



  /**
   * The level of insurance the eligibility check was run on. Can be one of the following: &#x60;Primary Insurance&#x60; or &#x60;Secondary Insurance&#x60;
   * @return cobLevel
   */
  @javax.annotation.Nullable
  public String getCobLevel() {
    return cobLevel;
  }



  /**
   * A variable size object containing the details of the eligibility check, if returned by the clearinghouse that ran the eligibility check
   * @return coverageDetails
   */
  @javax.annotation.Nullable
  public String getCoverageDetails() {
    return coverageDetails;
  }



  /**
   * A variable size object containing subscriber information, if returned by the clearinghouse that ran the eligibility check
   * @return coverageSubscriber
   */
  @javax.annotation.Nullable
  public String getCoverageSubscriber() {
    return coverageSubscriber;
  }



  public Coverage eligibility(String eligibility) {
    this.eligibility = eligibility;
    return this;
  }

  /**
   *  Value | Description --- | ---- &#x60;&#39;1&#39;&#x60; | Active Coverage &#x60;&#39;2&#39;&#x60; | Active - Full Risk Capitation &#x60;&#39;3&#39;&#x60; | Active - Services Capitated &#x60;&#39;4&#39;&#x60; | Active - Services Capitated to Primary Care Physician &#x60;&#39;5&#39;&#x60; | Active - Pending Investigation &#x60;&#39;6&#39;&#x60; | Inactive &#x60;&#39;7&#39;&#x60; | Inactive - Pending Eligibility Update &#x60;&#39;8&#39;&#x60; | Inactive - Pending Investigation &#x60;&#39;A&#39;&#x60; | Co-Insurance &#x60;&#39;B&#39;&#x60; | Co-Payment &#x60;&#39;C&#39;&#x60; | Deductible &#x60;&#39;CB&#39;&#x60; | Coverage Basis &#x60;&#39;D&#39;&#x60; | Benefit Description &#x60;&#39;E&#39;&#x60; | Exclusions &#x60;&#39;F&#39;&#x60; | Limitations &#x60;&#39;G&#39;&#x60; | Out of Pocket (Stop Loss) &#x60;&#39;H&#39;&#x60; | Unlimited &#x60;&#39;I&#39;&#x60; | Non-Covered &#x60;&#39;J&#39;&#x60; | Cost Containment &#x60;&#39;K&#39;&#x60; | Reserve &#x60;&#39;L&#39;&#x60; | Primary Care Provider &#x60;&#39;M&#39;&#x60; | Pre-existing Condition &#x60;&#39;MC&#39;&#x60; | Managed Care Coordinator &#x60;&#39;N&#39;&#x60; | Services Restricted to Following Provider &#x60;&#39;O&#39;&#x60; | Not Deemed a Medical Necessity &#x60;&#39;P&#39;&#x60; | Benefit Disclaimer &#x60;&#39;Q&#39;&#x60; | Second Surgical Opinion Required &#x60;&#39;R&#39;&#x60; | Other or Additional Payor &#x60;&#39;S&#39;&#x60; | Prior Year(s) History &#x60;&#39;T&#39;&#x60; | Card(s) Reported Lost/Stolen &#x60;&#39;U&#39;&#x60; | Contact Following Entity for Eligibility or Benefit Information &#x60;&#39;V&#39;&#x60; | Cannot Process &#x60;&#39;W&#39;&#x60; | Other Source of Data &#x60;&#39;X&#39;&#x60; | Health Care Facility &#x60;&#39;Y&#39;&#x60; | Spend Down 
   * @return eligibility
   */
  @javax.annotation.Nullable
  public String getEligibility() {
    return eligibility;
  }

  public void setEligibility(String eligibility) {
    this.eligibility = eligibility;
  }


  /**
   * 
   * @return patient
   */
  @javax.annotation.Nullable
  public String getPatient() {
    return patient;
  }



  public Coverage payerName(String payerName) {
    this.payerName = payerName;
    return this;
  }

  /**
   * The name of the payer as returned by the clearinghouse that ran the eligibility check
   * @return payerName
   */
  @javax.annotation.Nullable
  public String getPayerName() {
    return payerName;
  }

  public void setPayerName(String payerName) {
    this.payerName = payerName;
  }


  /**
   * The time at which the request was made
   * @return queryDate
   */
  @javax.annotation.Nullable
  public String getQueryDate() {
    return queryDate;
  }



  public Coverage requestServiceType(RequestServiceTypeEnum requestServiceType) {
    this.requestServiceType = requestServiceType;
    return this;
  }

  /**
   *  Value | Description --- | ---- &#x60;&#39;1&#39;&#x60; | Medical Care &#x60;&#39;2&#39;&#x60; | Surgical &#x60;&#39;3&#39;&#x60; | Consultation &#x60;&#39;4&#39;&#x60; | Diagnostic X-Ray &#x60;&#39;5&#39;&#x60; | Diagnostic Lab &#x60;&#39;6&#39;&#x60; | Radiation Therapy &#x60;&#39;7&#39;&#x60; | Anesthesia &#x60;&#39;8&#39;&#x60; | Surgical Assistance &#x60;&#39;9&#39;&#x60; | Other Medical &#x60;&#39;10&#39;&#x60; | Blood Charges &#x60;&#39;11&#39;&#x60; | Used Durable Medical Equipment &#x60;&#39;12&#39;&#x60; | Durable Medical Equipment Purchase &#x60;&#39;13&#39;&#x60; | Ambulatory Service Center Facility &#x60;&#39;14&#39;&#x60; | Renal Supplies in the Home &#x60;&#39;15&#39;&#x60; | Alternate Method Dialysis &#x60;&#39;16&#39;&#x60; | Chronic Renal Disease (CRD) Equipment &#x60;&#39;17&#39;&#x60; | Pre-Admission Testing &#x60;&#39;18&#39;&#x60; | Durable Medical Equipment Rental &#x60;&#39;19&#39;&#x60; | Pneumonia Vaccine &#x60;&#39;20&#39;&#x60; | Second Surgical Opinion &#x60;&#39;21&#39;&#x60; | Third Surgical Opinion &#x60;&#39;22&#39;&#x60; | Social Work &#x60;&#39;23&#39;&#x60; | Diagnostic Dental &#x60;&#39;24&#39;&#x60; | Periodontics &#x60;&#39;25&#39;&#x60; | Restorative &#x60;&#39;26&#39;&#x60; | Endodontics &#x60;&#39;27&#39;&#x60; | Maxillofacial Prosthetics &#x60;&#39;28&#39;&#x60; | Adjunctive Dental Services &#x60;&#39;30&#39;&#x60; | Health Benefit Plan Coverage &#x60;&#39;32&#39;&#x60; | Plan Waiting Period &#x60;&#39;33&#39;&#x60; | Chiropractic &#x60;&#39;34&#39;&#x60; | Chiropractic Office Visits &#x60;&#39;35&#39;&#x60; | Dental Care &#x60;&#39;36&#39;&#x60; | Dental Crowns &#x60;&#39;37&#39;&#x60; | Dental Accident &#x60;&#39;38&#39;&#x60; | Orthodontics &#x60;&#39;39&#39;&#x60; | Prosthodontics &#x60;&#39;40&#39;&#x60; | Oral Surgery &#x60;&#39;41&#39;&#x60; | Routine (Preventive) Dental &#x60;&#39;42&#39;&#x60; | Home Health Care &#x60;&#39;43&#39;&#x60; | Home Health Prescriptions &#x60;&#39;44&#39;&#x60; | Home Health Visits &#x60;&#39;45&#39;&#x60; | Hospice &#x60;&#39;46&#39;&#x60; | Respite Care &#x60;&#39;47&#39;&#x60; | Hospital &#x60;&#39;48&#39;&#x60; | Hospital - Inpatient &#x60;&#39;49&#39;&#x60; | Hospital - Room and Board &#x60;&#39;50&#39;&#x60; | Hospital - Outpatient &#x60;&#39;51&#39;&#x60; | Hospital - Emergency Accident &#x60;&#39;52&#39;&#x60; | Hospital - Emergency Medical &#x60;&#39;53&#39;&#x60; | Hospital - Ambulatory Surgical &#x60;&#39;54&#39;&#x60; | Long Term Care &#x60;&#39;55&#39;&#x60; | Major Medical &#x60;&#39;56&#39;&#x60; | Medically Related Transportation &#x60;&#39;57&#39;&#x60; | Air Transportation &#x60;&#39;58&#39;&#x60; | Cabulance &#x60;&#39;59&#39;&#x60; | Licensed Ambulance &#x60;&#39;60&#39;&#x60; | General Benefits &#x60;&#39;61&#39;&#x60; | In-vitro Fertilization &#x60;&#39;62&#39;&#x60; | MRI/CAT Scan &#x60;&#39;63&#39;&#x60; | Donor Procedures &#x60;&#39;64&#39;&#x60; | Acupuncture &#x60;&#39;65&#39;&#x60; | Newborn Care &#x60;&#39;66&#39;&#x60; | Pathology &#x60;&#39;67&#39;&#x60; | Smoking Cessation &#x60;&#39;68&#39;&#x60; | Well Baby Care &#x60;&#39;69&#39;&#x60; | Maternity &#x60;&#39;70&#39;&#x60; | Transplants &#x60;&#39;71&#39;&#x60; | Audiology Exam &#x60;&#39;72&#39;&#x60; | Inhalation Therapy &#x60;&#39;73&#39;&#x60; | Diagnostic Medical &#x60;&#39;74&#39;&#x60; | Private Duty Nursing &#x60;&#39;75&#39;&#x60; | Prosthetic Device &#x60;&#39;76&#39;&#x60; | Dialysis &#x60;&#39;77&#39;&#x60; | Otological Exam &#x60;&#39;78&#39;&#x60; | Chemotherapy &#x60;&#39;79&#39;&#x60; | Allergy Testing &#x60;&#39;80&#39;&#x60; | Immunizations &#x60;&#39;81&#39;&#x60; | Routine Physical &#x60;&#39;82&#39;&#x60; | Family Planning &#x60;&#39;83&#39;&#x60; | Infertility &#x60;&#39;84&#39;&#x60; | Abortion &#x60;&#39;85&#39;&#x60; | AIDS &#x60;&#39;86&#39;&#x60; | Emergency Services &#x60;&#39;87&#39;&#x60; | Cancer &#x60;&#39;88&#39;&#x60; | Pharmacy &#x60;&#39;89&#39;&#x60; | Free Standing Prescription Drug &#x60;&#39;90&#39;&#x60; | Mail Order Prescription Drug &#x60;&#39;91&#39;&#x60; | Brand Name Prescription Drug &#x60;&#39;92&#39;&#x60; | Generic Prescription Drug &#x60;&#39;93&#39;&#x60; | Podiatry &#x60;&#39;94&#39;&#x60; | Podiatry - Office Visits &#x60;&#39;95&#39;&#x60; | Podiatry - Nursing Home Visits &#x60;&#39;96&#39;&#x60; | Professional (Physician) &#x60;&#39;97&#39;&#x60; | Anesthesiologist &#x60;&#39;98&#39;&#x60; | Professional (Physician) Visit - Office &#x60;&#39;99&#39;&#x60; | Professional (Physician) Visit - Inpatient &#x60;&#39;A0&#39;&#x60; | Professional (Physician) Visit - Outpatient &#x60;&#39;A1&#39;&#x60; | Professional (Physician) Visit - Nursing Home &#x60;&#39;A2&#39;&#x60; | Professional (Physician) Visit - Skilled Nursing Facility &#x60;&#39;A3&#39;&#x60; | Professional (Physician) Visit - Home &#x60;&#39;A4&#39;&#x60; | Psychiatric &#x60;&#39;A5&#39;&#x60; | Psychiatric - Room and Board &#x60;&#39;A6&#39;&#x60; | Psychotherapy &#x60;&#39;A7&#39;&#x60; | Psychiatric - Inpatient &#x60;&#39;A8&#39;&#x60; | Psychiatric - Outpatient &#x60;&#39;A9&#39;&#x60; | Rehabilitation &#x60;&#39;AA&#39;&#x60; | Rehabilitation - Room and Board &#x60;&#39;AB&#39;&#x60; | Rehabilitation - Inpatient &#x60;&#39;AC&#39;&#x60; | Rehabilitation - Outpatient &#x60;&#39;AD&#39;&#x60; | Occupational Therapy &#x60;&#39;AE&#39;&#x60; | Physical Medicine &#x60;&#39;AF&#39;&#x60; | Speech Therapy &#x60;&#39;AG&#39;&#x60; | Skilled Nursing Care &#x60;&#39;AH&#39;&#x60; | Skilled Nursing Care - Room and Board &#x60;&#39;AI&#39;&#x60; | Substance Abuse &#x60;&#39;AJ&#39;&#x60; | Alcoholism &#x60;&#39;AK&#39;&#x60; | Drug Addiction &#x60;&#39;AL&#39;&#x60; | Vision (Optometry) &#x60;&#39;AM&#39;&#x60; | Frames &#x60;&#39;AN&#39;&#x60; | Routine Exam &#x60;&#39;AO&#39;&#x60; | Lenses &#x60;&#39;AQ&#39;&#x60; | Nonmedically Necessary Physical &#x60;&#39;AR&#39;&#x60; | Experimental Drug Therapy &#x60;&#39;B1&#39;&#x60; | Burn Care &#x60;&#39;B2&#39;&#x60; | Brand Name Prescription Drug - Formulary &#x60;&#39;B3&#39;&#x60; | Brand Name Prescription Drug - Non-Formulary &#x60;&#39;BA&#39;&#x60; | Independent Medical Evaluation &#x60;&#39;BB&#39;&#x60; | Partial Hospitalization (Psychiatric) &#x60;&#39;BC&#39;&#x60; | Day Care (Psychiatric) &#x60;&#39;BD&#39;&#x60; | Cognitive Therapy &#x60;&#39;BE&#39;&#x60; | Massage Therapy &#x60;&#39;BF&#39;&#x60; | Pulmonary Rehabilitation &#x60;&#39;BG&#39;&#x60; | Cardiac Rehabilitation &#x60;&#39;BH&#39;&#x60; | Pediatric &#x60;&#39;BI&#39;&#x60; | Nursery &#x60;&#39;BJ&#39;&#x60; | Skin &#x60;&#39;BK&#39;&#x60; | Orthopedic &#x60;&#39;BL&#39;&#x60; | Cardiac &#x60;&#39;BM&#39;&#x60; | Lymphatic &#x60;&#39;BN&#39;&#x60; | Gastrointestinal &#x60;&#39;BP&#39;&#x60; | Endocrine &#x60;&#39;BQ&#39;&#x60; | Neurology &#x60;&#39;BR&#39;&#x60; | Eye &#x60;&#39;BS&#39;&#x60; | Invasive Procedures &#x60;&#39;BT&#39;&#x60; | Gynecological &#x60;&#39;BU&#39;&#x60; | Obstetrical &#x60;&#39;BV&#39;&#x60; | Obstetrical/Gynecological &#x60;&#39;BW&#39;&#x60; | Mail Order Prescription Drug: Brand Name &#x60;&#39;BX&#39;&#x60; | Mail Order Prescription Drug: Generic &#x60;&#39;BY&#39;&#x60; | Physician Visit - Office: Sick &#x60;&#39;BZ&#39;&#x60; | Physician Visit - Office: Well &#x60;&#39;C1&#39;&#x60; | Coronary Care &#x60;&#39;CA&#39;&#x60; | Private Duty Nursing - Inpatient &#x60;&#39;CB&#39;&#x60; | Private Duty Nursing - Home &#x60;&#39;CC&#39;&#x60; | Surgical Benefits - Professional (Physician) &#x60;&#39;CD&#39;&#x60; | Surgical Benefits - Facility &#x60;&#39;CE&#39;&#x60; | Mental Health Provider - Inpatient &#x60;&#39;CF&#39;&#x60; | Mental Health Provider - Outpatient &#x60;&#39;CG&#39;&#x60; | Mental Health Facility - Inpatient &#x60;&#39;CH&#39;&#x60; | Mental Health Facility - Outpatient &#x60;&#39;CI&#39;&#x60; | Substance Abuse Facility - Inpatient &#x60;&#39;CJ&#39;&#x60; | Substance Abuse Facility - Outpatient &#x60;&#39;CK&#39;&#x60; | Screening X-ray &#x60;&#39;CL&#39;&#x60; | Screening laboratory &#x60;&#39;CM&#39;&#x60; | Mammogram, High Risk Patient &#x60;&#39;CN&#39;&#x60; | Mammogram, Low Risk Patient &#x60;&#39;CO&#39;&#x60; | Flu Vaccination &#x60;&#39;CP&#39;&#x60; | Eyewear and Eyewear Accessories &#x60;&#39;CQ&#39;&#x60; | Case Management &#x60;&#39;DG&#39;&#x60; | Dermatology &#x60;&#39;DM&#39;&#x60; | Durable Medical Equipment &#x60;&#39;DS&#39;&#x60; | Diabetic Supplies &#x60;&#39;GF&#39;&#x60; | Generic Prescription Drug - Formulary &#x60;&#39;GN&#39;&#x60; | Generic Prescription Drug - Non-Formulary &#x60;&#39;GY&#39;&#x60; | Allergy &#x60;&#39;IC&#39;&#x60; | Intensive Care &#x60;&#39;MH&#39;&#x60; | Mental Health &#x60;&#39;NI&#39;&#x60; | Neonatal Intensive Care &#x60;&#39;ON&#39;&#x60; | Oncology &#x60;&#39;PT&#39;&#x60; | Physical Therapy &#x60;&#39;PU&#39;&#x60; | Pulmonary &#x60;&#39;RN&#39;&#x60; | Renal &#x60;&#39;RT&#39;&#x60; | Residential Psychiatric Treatment &#x60;&#39;TC&#39;&#x60; | Transitional Care &#x60;&#39;TN&#39;&#x60; | Transitional Nursery Care &#x60;&#39;UC&#39;&#x60; | Urgent Care 
   * @return requestServiceType
   */
  @javax.annotation.Nullable
  public RequestServiceTypeEnum getRequestServiceType() {
    return requestServiceType;
  }

  public void setRequestServiceType(RequestServiceTypeEnum requestServiceType) {
    this.requestServiceType = requestServiceType;
  }


  /**
   * 
   * @return serviceTypeDescription
   */
  @javax.annotation.Nullable
  public String getServiceTypeDescription() {
    return serviceTypeDescription;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Coverage coverage = (Coverage) o;
    return Objects.equals(this.appointment, coverage.appointment) &&
        Objects.equals(this.cobLevel, coverage.cobLevel) &&
        Objects.equals(this.coverageDetails, coverage.coverageDetails) &&
        Objects.equals(this.coverageSubscriber, coverage.coverageSubscriber) &&
        Objects.equals(this.eligibility, coverage.eligibility) &&
        Objects.equals(this.patient, coverage.patient) &&
        Objects.equals(this.payerName, coverage.payerName) &&
        Objects.equals(this.queryDate, coverage.queryDate) &&
        Objects.equals(this.requestServiceType, coverage.requestServiceType) &&
        Objects.equals(this.serviceTypeDescription, coverage.serviceTypeDescription);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appointment, cobLevel, coverageDetails, coverageSubscriber, eligibility, patient, payerName, queryDate, requestServiceType, serviceTypeDescription);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Coverage {\n");
    sb.append("    appointment: ").append(toIndentedString(appointment)).append("\n");
    sb.append("    cobLevel: ").append(toIndentedString(cobLevel)).append("\n");
    sb.append("    coverageDetails: ").append(toIndentedString(coverageDetails)).append("\n");
    sb.append("    coverageSubscriber: ").append(toIndentedString(coverageSubscriber)).append("\n");
    sb.append("    eligibility: ").append(toIndentedString(eligibility)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    payerName: ").append(toIndentedString(payerName)).append("\n");
    sb.append("    queryDate: ").append(toIndentedString(queryDate)).append("\n");
    sb.append("    requestServiceType: ").append(toIndentedString(requestServiceType)).append("\n");
    sb.append("    serviceTypeDescription: ").append(toIndentedString(serviceTypeDescription)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("appointment");
    openapiFields.add("cob_level");
    openapiFields.add("coverage_details");
    openapiFields.add("coverage_subscriber");
    openapiFields.add("eligibility");
    openapiFields.add("patient");
    openapiFields.add("payer_name");
    openapiFields.add("query_date");
    openapiFields.add("request_service_type");
    openapiFields.add("service_type_description");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Coverage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Coverage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Coverage is not found in the empty JSON string", Coverage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Coverage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Coverage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("appointment") != null && !jsonObj.get("appointment").isJsonNull()) && !jsonObj.get("appointment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `appointment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("appointment").toString()));
      }
      if ((jsonObj.get("cob_level") != null && !jsonObj.get("cob_level").isJsonNull()) && !jsonObj.get("cob_level").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cob_level` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cob_level").toString()));
      }
      if ((jsonObj.get("coverage_details") != null && !jsonObj.get("coverage_details").isJsonNull()) && !jsonObj.get("coverage_details").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `coverage_details` to be a primitive type in the JSON string but got `%s`", jsonObj.get("coverage_details").toString()));
      }
      if ((jsonObj.get("coverage_subscriber") != null && !jsonObj.get("coverage_subscriber").isJsonNull()) && !jsonObj.get("coverage_subscriber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `coverage_subscriber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("coverage_subscriber").toString()));
      }
      if ((jsonObj.get("eligibility") != null && !jsonObj.get("eligibility").isJsonNull()) && !jsonObj.get("eligibility").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eligibility` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eligibility").toString()));
      }
      if ((jsonObj.get("patient") != null && !jsonObj.get("patient").isJsonNull()) && !jsonObj.get("patient").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patient` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patient").toString()));
      }
      if ((jsonObj.get("payer_name") != null && !jsonObj.get("payer_name").isJsonNull()) && !jsonObj.get("payer_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payer_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payer_name").toString()));
      }
      if ((jsonObj.get("query_date") != null && !jsonObj.get("query_date").isJsonNull()) && !jsonObj.get("query_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `query_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("query_date").toString()));
      }
      if ((jsonObj.get("request_service_type") != null && !jsonObj.get("request_service_type").isJsonNull()) && !jsonObj.get("request_service_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `request_service_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("request_service_type").toString()));
      }
      // validate the optional field `request_service_type`
      if (jsonObj.get("request_service_type") != null && !jsonObj.get("request_service_type").isJsonNull()) {
        RequestServiceTypeEnum.validateJsonElement(jsonObj.get("request_service_type"));
      }
      if ((jsonObj.get("service_type_description") != null && !jsonObj.get("service_type_description").isJsonNull()) && !jsonObj.get("service_type_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `service_type_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("service_type_description").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Coverage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Coverage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Coverage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Coverage.class));

       return (TypeAdapter<T>) new TypeAdapter<Coverage>() {
           @Override
           public void write(JsonWriter out, Coverage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Coverage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Coverage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Coverage
   * @throws IOException if the JSON string is invalid with respect to Coverage
   */
  public static Coverage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Coverage.class);
  }

  /**
   * Convert an instance of Coverage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

