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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AppointmentStatusTransition;
import org.openapitools.client.model.ClaimBillingNotes1;
import org.openapitools.client.model.ClinicalNote1;
import org.openapitools.client.model.CustomAppointmentFieldValue;
import org.openapitools.client.model.CustomVitalValue;
import org.openapitools.client.model.SimpleReminder;
import org.openapitools.client.model.SystemVitals;

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
 * Appointment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Appointment {
  public static final String SERIALIZED_NAME_ALLOW_OVERLAPPING = "allow_overlapping";
  @SerializedName(SERIALIZED_NAME_ALLOW_OVERLAPPING)
  private Boolean allowOverlapping;

  public static final String SERIALIZED_NAME_APPT_IS_BREAK = "appt_is_break";
  @SerializedName(SERIALIZED_NAME_APPT_IS_BREAK)
  private Boolean apptIsBreak;

  public static final String SERIALIZED_NAME_BASE_RECURRING_APPOINTMENT = "base_recurring_appointment";
  @SerializedName(SERIALIZED_NAME_BASE_RECURRING_APPOINTMENT)
  private String baseRecurringAppointment;

  public static final String SERIALIZED_NAME_BILLING_NOTES = "billing_notes";
  @SerializedName(SERIALIZED_NAME_BILLING_NOTES)
  private List<ClaimBillingNotes1> billingNotes = new ArrayList<>();

  public static final String SERIALIZED_NAME_BILLING_PROVIDER = "billing_provider";
  @SerializedName(SERIALIZED_NAME_BILLING_PROVIDER)
  private String billingProvider;

  public static final String SERIALIZED_NAME_BILLING_STATUS = "billing_status";
  @SerializedName(SERIALIZED_NAME_BILLING_STATUS)
  private String billingStatus;

  public static final String SERIALIZED_NAME_CLINICAL_NOTE = "clinical_note";
  @SerializedName(SERIALIZED_NAME_CLINICAL_NOTE)
  private ClinicalNote1 clinicalNote;

  public static final String SERIALIZED_NAME_CLONED_FROM = "cloned_from";
  @SerializedName(SERIALIZED_NAME_CLONED_FROM)
  private Integer clonedFrom;

  public static final String SERIALIZED_NAME_COLOR = "color";
  @SerializedName(SERIALIZED_NAME_COLOR)
  private String color;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_CUSTOM_FIELDS = "custom_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELDS)
  private List<CustomAppointmentFieldValue> customFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOM_VITALS = "custom_vitals";
  @SerializedName(SERIALIZED_NAME_CUSTOM_VITALS)
  private List<CustomVitalValue> customVitals = new ArrayList<>();

  public static final String SERIALIZED_NAME_DELETED_FLAG = "deleted_flag";
  @SerializedName(SERIALIZED_NAME_DELETED_FLAG)
  private Boolean deletedFlag;

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private Integer doctor;

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private Integer duration;

  public static final String SERIALIZED_NAME_EXAM_ROOM = "exam_room";
  @SerializedName(SERIALIZED_NAME_EXAM_ROOM)
  private Integer examRoom;

  public static final String SERIALIZED_NAME_EXTENDED_UPDATED_AT = "extended_updated_at";
  @SerializedName(SERIALIZED_NAME_EXTENDED_UPDATED_AT)
  private String extendedUpdatedAt;

  public static final String SERIALIZED_NAME_FIRST_BILLED_DATE = "first_billed_date";
  @SerializedName(SERIALIZED_NAME_FIRST_BILLED_DATE)
  private String firstBilledDate;

  public static final String SERIALIZED_NAME_ICD10_CODES = "icd10_codes";
  @SerializedName(SERIALIZED_NAME_ICD10_CODES)
  private List<String> icd10Codes = new ArrayList<>();

  public static final String SERIALIZED_NAME_ICD9_CODES = "icd9_codes";
  @SerializedName(SERIALIZED_NAME_ICD9_CODES)
  private List<String> icd9Codes = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  /**
   * Billing status of primary insurer
   */
  @JsonAdapter(Ins1StatusEnum.Adapter.class)
  public enum Ins1StatusEnum {
    EMPTY(""),
    
    INCOMPLETE_INFORMATION("Incomplete Information"),
    
    IN_PROCESS_EMDEON("In Process Emdeon"),
    
    REJECTED_EMDEON("Rejected Emdeon"),
    
    REJECTED_JOPARI("Rejected Jopari"),
    
    IN_PROCESS_PAYOR("In Process Payor"),
    
    REJECTED_WAYSTAR_PROFESSIONAL("Rejected Waystar Professional"),
    
    REJECTED_WAYSTAR_INSTITUTIONAL("Rejected Waystar Institutional"),
    
    IN_PROCESS_PAYER("In Process Payer"),
    
    PAYER_ACKNOWLEDGED("Payer Acknowledged"),
    
    REJECTED_PAYOR("Rejected Payor"),
    
    REJECTED_PAYER("Rejected Payer"),
    
    PAID_IN_FULL("Paid in Full"),
    
    PARTIALLY_PAID("Partially Paid"),
    
    COORDINATION_OF_BENEFITS("Coordination of Benefits"),
    
    ERA_RECEIVED("ERA Received"),
    
    ERA_DENIED("ERA Denied"),
    
    HCFA_FORM_FAXED("HCFA Form Faxed");

    private String value;

    Ins1StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static Ins1StatusEnum fromValue(String value) {
      for (Ins1StatusEnum b : Ins1StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<Ins1StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final Ins1StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public Ins1StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return Ins1StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      Ins1StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_INS1_STATUS = "ins1_status";
  @SerializedName(SERIALIZED_NAME_INS1_STATUS)
  private Ins1StatusEnum ins1Status;

  /**
   * Billing status of secondary insurer
   */
  @JsonAdapter(Ins2StatusEnum.Adapter.class)
  public enum Ins2StatusEnum {
    EMPTY(""),
    
    INCOMPLETE_INFORMATION("Incomplete Information"),
    
    IN_PROCESS_EMDEON("In Process Emdeon"),
    
    REJECTED_EMDEON("Rejected Emdeon"),
    
    REJECTED_JOPARI("Rejected Jopari"),
    
    IN_PROCESS_PAYOR("In Process Payor"),
    
    REJECTED_WAYSTAR_PROFESSIONAL("Rejected Waystar Professional"),
    
    REJECTED_WAYSTAR_INSTITUTIONAL("Rejected Waystar Institutional"),
    
    IN_PROCESS_PAYER("In Process Payer"),
    
    PAYER_ACKNOWLEDGED("Payer Acknowledged"),
    
    REJECTED_PAYOR("Rejected Payor"),
    
    REJECTED_PAYER("Rejected Payer"),
    
    PAID_IN_FULL("Paid in Full"),
    
    PARTIALLY_PAID("Partially Paid"),
    
    COORDINATION_OF_BENEFITS("Coordination of Benefits"),
    
    ERA_RECEIVED("ERA Received"),
    
    ERA_DENIED("ERA Denied"),
    
    HCFA_FORM_FAXED("HCFA Form Faxed");

    private String value;

    Ins2StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static Ins2StatusEnum fromValue(String value) {
      for (Ins2StatusEnum b : Ins2StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<Ins2StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final Ins2StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public Ins2StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return Ins2StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      Ins2StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_INS2_STATUS = "ins2_status";
  @SerializedName(SERIALIZED_NAME_INS2_STATUS)
  private Ins2StatusEnum ins2Status;

  public static final String SERIALIZED_NAME_IS_VIRTUAL_BASE = "is_virtual_base";
  @SerializedName(SERIALIZED_NAME_IS_VIRTUAL_BASE)
  private Boolean isVirtualBase;

  public static final String SERIALIZED_NAME_IS_WALK_IN = "is_walk_in";
  @SerializedName(SERIALIZED_NAME_IS_WALK_IN)
  private Boolean isWalkIn;

  public static final String SERIALIZED_NAME_LAST_BILLED_DATE = "last_billed_date";
  @SerializedName(SERIALIZED_NAME_LAST_BILLED_DATE)
  private String lastBilledDate;

  public static final String SERIALIZED_NAME_NOTES = "notes";
  @SerializedName(SERIALIZED_NAME_NOTES)
  private String notes;

  public static final String SERIALIZED_NAME_OFFICE = "office";
  @SerializedName(SERIALIZED_NAME_OFFICE)
  private Integer office;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private Integer patient;

  public static final String SERIALIZED_NAME_PRIMARY_INSURANCE_ID_NUMBER = "primary_insurance_id_number";
  @SerializedName(SERIALIZED_NAME_PRIMARY_INSURANCE_ID_NUMBER)
  private String primaryInsuranceIdNumber;

  public static final String SERIALIZED_NAME_PRIMARY_INSURER_NAME = "primary_insurer_name";
  @SerializedName(SERIALIZED_NAME_PRIMARY_INSURER_NAME)
  private String primaryInsurerName;

  public static final String SERIALIZED_NAME_PRIMARY_INSURER_PAYER_ID = "primary_insurer_payer_id";
  @SerializedName(SERIALIZED_NAME_PRIMARY_INSURER_PAYER_ID)
  private String primaryInsurerPayerId;

  public static final String SERIALIZED_NAME_PROFILE = "profile";
  @SerializedName(SERIALIZED_NAME_PROFILE)
  private Integer profile;

  public static final String SERIALIZED_NAME_REASON = "reason";
  @SerializedName(SERIALIZED_NAME_REASON)
  private String reason;

  public static final String SERIALIZED_NAME_RECURRING_APPOINTMENT = "recurring_appointment";
  @SerializedName(SERIALIZED_NAME_RECURRING_APPOINTMENT)
  private Boolean recurringAppointment;

  public static final String SERIALIZED_NAME_REMINDER_PROFILE = "reminder_profile";
  @SerializedName(SERIALIZED_NAME_REMINDER_PROFILE)
  private String reminderProfile;

  public static final String SERIALIZED_NAME_REMINDERS = "reminders";
  @SerializedName(SERIALIZED_NAME_REMINDERS)
  private List<SimpleReminder> reminders = new ArrayList<>();

  public static final String SERIALIZED_NAME_SCHEDULED_TIME = "scheduled_time";
  @SerializedName(SERIALIZED_NAME_SCHEDULED_TIME)
  private String scheduledTime;

  public static final String SERIALIZED_NAME_SECONDARY_INSURANCE_ID_NUMBER = "secondary_insurance_id_number";
  @SerializedName(SERIALIZED_NAME_SECONDARY_INSURANCE_ID_NUMBER)
  private String secondaryInsuranceIdNumber;

  public static final String SERIALIZED_NAME_SECONDARY_INSURER_NAME = "secondary_insurer_name";
  @SerializedName(SERIALIZED_NAME_SECONDARY_INSURER_NAME)
  private String secondaryInsurerName;

  public static final String SERIALIZED_NAME_SECONDARY_INSURER_PAYER_ID = "secondary_insurer_payer_id";
  @SerializedName(SERIALIZED_NAME_SECONDARY_INSURER_PAYER_ID)
  private String secondaryInsurerPayerId;

  /**
   * One of &#x60;&#x60;, &#x60;Arrived&#x60;, &#x60;Checked In&#x60;, &#x60;In Room&#x60;, &#x60;Cancelled&#x60;, &#x60;Complete&#x60;, &#x60;Confirmed&#x60;, &#x60;In Session&#x60;, &#x60;No Show&#x60;, &#x60;Not Confirmed&#x60;, or &#x60;Rescheduled&#x60;. Or one of the custom statuses.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    EMPTY(""),
    
    ARRIVED("Arrived"),
    
    CHECKED_IN("Checked In"),
    
    CHECKED_IN_ONLINE("Checked In Online"),
    
    IN_ROOM("In Room"),
    
    IN_SESSION("In Session"),
    
    COMPLETE("Complete"),
    
    CONFIRMED("Confirmed"),
    
    NOT_CONFIRMED("Not Confirmed"),
    
    RESCHEDULED("Rescheduled"),
    
    CANCELLED("Cancelled"),
    
    NO_SHOW("No Show");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_STATUS_TRANSITIONS = "status_transitions";
  @SerializedName(SERIALIZED_NAME_STATUS_TRANSITIONS)
  private List<AppointmentStatusTransition> statusTransitions = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUPERVISING_PROVIDER = "supervising_provider";
  @SerializedName(SERIALIZED_NAME_SUPERVISING_PROVIDER)
  private String supervisingProvider;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public static final String SERIALIZED_NAME_VITALS = "vitals";
  @SerializedName(SERIALIZED_NAME_VITALS)
  private SystemVitals vitals;

  public Appointment() {
  }

  public Appointment(
     String baseRecurringAppointment, 
     List<ClaimBillingNotes1> billingNotes, 
     String billingProvider, 
     String createdAt, 
     Boolean deletedFlag, 
     String extendedUpdatedAt, 
     String firstBilledDate, 
     String id, 
     Ins1StatusEnum ins1Status, 
     Ins2StatusEnum ins2Status, 
     Boolean isVirtualBase, 
     String lastBilledDate, 
     String primaryInsuranceIdNumber, 
     String primaryInsurerName, 
     String primaryInsurerPayerId, 
     Boolean recurringAppointment, 
     List<SimpleReminder> reminders, 
     String secondaryInsuranceIdNumber, 
     String secondaryInsurerName, 
     String secondaryInsurerPayerId, 
     List<AppointmentStatusTransition> statusTransitions, 
     String supervisingProvider, 
     String updatedAt
  ) {
    this();
    this.baseRecurringAppointment = baseRecurringAppointment;
    this.billingNotes = billingNotes;
    this.billingProvider = billingProvider;
    this.createdAt = createdAt;
    this.deletedFlag = deletedFlag;
    this.extendedUpdatedAt = extendedUpdatedAt;
    this.firstBilledDate = firstBilledDate;
    this.id = id;
    this.ins1Status = ins1Status;
    this.ins2Status = ins2Status;
    this.isVirtualBase = isVirtualBase;
    this.lastBilledDate = lastBilledDate;
    this.primaryInsuranceIdNumber = primaryInsuranceIdNumber;
    this.primaryInsurerName = primaryInsurerName;
    this.primaryInsurerPayerId = primaryInsurerPayerId;
    this.recurringAppointment = recurringAppointment;
    this.reminders = reminders;
    this.secondaryInsuranceIdNumber = secondaryInsuranceIdNumber;
    this.secondaryInsurerName = secondaryInsurerName;
    this.secondaryInsurerPayerId = secondaryInsurerPayerId;
    this.statusTransitions = statusTransitions;
    this.supervisingProvider = supervisingProvider;
    this.updatedAt = updatedAt;
  }

  public Appointment allowOverlapping(Boolean allowOverlapping) {
    this.allowOverlapping = allowOverlapping;
    return this;
  }

  /**
   * Bypass overlap check.
   * @return allowOverlapping
   */
  @javax.annotation.Nullable
  public Boolean getAllowOverlapping() {
    return allowOverlapping;
  }

  public void setAllowOverlapping(Boolean allowOverlapping) {
    this.allowOverlapping = allowOverlapping;
  }


  public Appointment apptIsBreak(Boolean apptIsBreak) {
    this.apptIsBreak = apptIsBreak;
    return this;
  }

  /**
   * 
   * @return apptIsBreak
   */
  @javax.annotation.Nullable
  public Boolean getApptIsBreak() {
    return apptIsBreak;
  }

  public void setApptIsBreak(Boolean apptIsBreak) {
    this.apptIsBreak = apptIsBreak;
  }


  /**
   * ID of base appointment of a recurrign series
   * @return baseRecurringAppointment
   */
  @javax.annotation.Nullable
  public String getBaseRecurringAppointment() {
    return baseRecurringAppointment;
  }



  /**
   * Billing notes of the appointment. For writing, check &#x60;/api/claim_billing_notes&#x60;
   * @return billingNotes
   */
  @javax.annotation.Nullable
  public List<ClaimBillingNotes1> getBillingNotes() {
    return billingNotes;
  }



  /**
   * 
   * @return billingProvider
   */
  @javax.annotation.Nullable
  public String getBillingProvider() {
    return billingProvider;
  }



  public Appointment billingStatus(String billingStatus) {
    this.billingStatus = billingStatus;
    return this;
  }

  /**
   * Should be one of &#x60;Auto Accident Claim&#x60;, &#x60;Balance Due&#x60;, &#x60;Bill Insurance&#x60;, &#x60;Bill Secondary Insurance&#x60;, &#x60;Durable Medical Equipment Claim&#x60;, &#x60;Internal Review&#x60;, &#x60;Paid In Full&#x60;, &#x60;Settled&#x60;, &#x60;Worker&#39;s Comp Claim&#x60; or one of the custom billing status
   * @return billingStatus
   */
  @javax.annotation.Nullable
  public String getBillingStatus() {
    return billingStatus;
  }

  public void setBillingStatus(String billingStatus) {
    this.billingStatus = billingStatus;
  }


  public Appointment clinicalNote(ClinicalNote1 clinicalNote) {
    this.clinicalNote = clinicalNote;
    return this;
  }

  /**
   * Get clinicalNote
   * @return clinicalNote
   */
  @javax.annotation.Nullable
  public ClinicalNote1 getClinicalNote() {
    return clinicalNote;
  }

  public void setClinicalNote(ClinicalNote1 clinicalNote) {
    this.clinicalNote = clinicalNote;
  }


  public Appointment clonedFrom(Integer clonedFrom) {
    this.clonedFrom = clonedFrom;
    return this;
  }

  /**
   * ID of the original appointment which this appointment cloned from. Will be null if the appointment is not cloned.
   * @return clonedFrom
   */
  @javax.annotation.Nullable
  public Integer getClonedFrom() {
    return clonedFrom;
  }

  public void setClonedFrom(Integer clonedFrom) {
    this.clonedFrom = clonedFrom;
  }


  public Appointment color(String color) {
    this.color = color;
    return this;
  }

  /**
   * 
   * @return color
   */
  @javax.annotation.Nullable
  public String getColor() {
    return color;
  }

  public void setColor(String color) {
    this.color = color;
  }


  /**
   * 
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }



  public Appointment customFields(List<CustomAppointmentFieldValue> customFields) {
    this.customFields = customFields;
    return this;
  }

  public Appointment addCustomFieldsItem(CustomAppointmentFieldValue customFieldsItem) {
    if (this.customFields == null) {
      this.customFields = new ArrayList<>();
    }
    this.customFields.add(customFieldsItem);
    return this;
  }

  /**
   * Custom appointment fields
   * @return customFields
   */
  @javax.annotation.Nullable
  public List<CustomAppointmentFieldValue> getCustomFields() {
    return customFields;
  }

  public void setCustomFields(List<CustomAppointmentFieldValue> customFields) {
    this.customFields = customFields;
  }


  public Appointment customVitals(List<CustomVitalValue> customVitals) {
    this.customVitals = customVitals;
    return this;
  }

  public Appointment addCustomVitalsItem(CustomVitalValue customVitalsItem) {
    if (this.customVitals == null) {
      this.customVitals = new ArrayList<>();
    }
    this.customVitals.add(customVitalsItem);
    return this;
  }

  /**
   * Custom vitals associated with this appointment.
   * @return customVitals
   */
  @javax.annotation.Nullable
  public List<CustomVitalValue> getCustomVitals() {
    return customVitals;
  }

  public void setCustomVitals(List<CustomVitalValue> customVitals) {
    this.customVitals = customVitals;
  }


  /**
   * Whether the appointmetn is deleted.
   * @return deletedFlag
   */
  @javax.annotation.Nullable
  public Boolean getDeletedFlag() {
    return deletedFlag;
  }



  public Appointment doctor(Integer doctor) {
    this.doctor = doctor;
    return this;
  }

  /**
   * Doctor ID
   * @return doctor
   */
  @javax.annotation.Nonnull
  public Integer getDoctor() {
    return doctor;
  }

  public void setDoctor(Integer doctor) {
    this.doctor = doctor;
  }


  public Appointment duration(Integer duration) {
    this.duration = duration;
    return this;
  }

  /**
   * Length of the appointment in minutes. Optional if &#x60;profile&#x60; is provided.
   * @return duration
   */
  @javax.annotation.Nullable
  public Integer getDuration() {
    return duration;
  }

  public void setDuration(Integer duration) {
    this.duration = duration;
  }


  public Appointment examRoom(Integer examRoom) {
    this.examRoom = examRoom;
    return this;
  }

  /**
   * Index of the exam room that this appointment occurs in. See &#x60;/api/offices&#x60;
   * @return examRoom
   */
  @javax.annotation.Nonnull
  public Integer getExamRoom() {
    return examRoom;
  }

  public void setExamRoom(Integer examRoom) {
    this.examRoom = examRoom;
  }


  /**
   * The most recent update time among appointment itself, its vitals and its custom vitals
   * @return extendedUpdatedAt
   */
  @javax.annotation.Nullable
  public String getExtendedUpdatedAt() {
    return extendedUpdatedAt;
  }



  /**
   * 
   * @return firstBilledDate
   */
  @javax.annotation.Nullable
  public String getFirstBilledDate() {
    return firstBilledDate;
  }



  public Appointment icd10Codes(List<String> icd10Codes) {
    this.icd10Codes = icd10Codes;
    return this;
  }

  public Appointment addIcd10CodesItem(String icd10CodesItem) {
    if (this.icd10Codes == null) {
      this.icd10Codes = new ArrayList<>();
    }
    this.icd10Codes.add(icd10CodesItem);
    return this;
  }

  /**
   * 
   * @return icd10Codes
   */
  @javax.annotation.Nullable
  public List<String> getIcd10Codes() {
    return icd10Codes;
  }

  public void setIcd10Codes(List<String> icd10Codes) {
    this.icd10Codes = icd10Codes;
  }


  public Appointment icd9Codes(List<String> icd9Codes) {
    this.icd9Codes = icd9Codes;
    return this;
  }

  public Appointment addIcd9CodesItem(String icd9CodesItem) {
    if (this.icd9Codes == null) {
      this.icd9Codes = new ArrayList<>();
    }
    this.icd9Codes.add(icd9CodesItem);
    return this;
  }

  /**
   * 
   * @return icd9Codes
   */
  @javax.annotation.Nullable
  public List<String> getIcd9Codes() {
    return icd9Codes;
  }

  public void setIcd9Codes(List<String> icd9Codes) {
    this.icd9Codes = icd9Codes;
  }


  /**
   * Unique identifier. Usually numeric, but not always
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  /**
   * Billing status of primary insurer
   * @return ins1Status
   */
  @javax.annotation.Nullable
  public Ins1StatusEnum getIns1Status() {
    return ins1Status;
  }



  /**
   * Billing status of secondary insurer
   * @return ins2Status
   */
  @javax.annotation.Nullable
  public Ins2StatusEnum getIns2Status() {
    return ins2Status;
  }



  /**
   * 
   * @return isVirtualBase
   */
  @javax.annotation.Nullable
  public Boolean getIsVirtualBase() {
    return isVirtualBase;
  }



  public Appointment isWalkIn(Boolean isWalkIn) {
    this.isWalkIn = isWalkIn;
    return this;
  }

  /**
   * Whether the appointment is a walk-in appointment
   * @return isWalkIn
   */
  @javax.annotation.Nullable
  public Boolean getIsWalkIn() {
    return isWalkIn;
  }

  public void setIsWalkIn(Boolean isWalkIn) {
    this.isWalkIn = isWalkIn;
  }


  /**
   * 
   * @return lastBilledDate
   */
  @javax.annotation.Nullable
  public String getLastBilledDate() {
    return lastBilledDate;
  }



  public Appointment notes(String notes) {
    this.notes = notes;
    return this;
  }

  /**
   * 
   * @return notes
   */
  @javax.annotation.Nullable
  public String getNotes() {
    return notes;
  }

  public void setNotes(String notes) {
    this.notes = notes;
  }


  public Appointment office(Integer office) {
    this.office = office;
    return this;
  }

  /**
   * Office ID
   * @return office
   */
  @javax.annotation.Nonnull
  public Integer getOffice() {
    return office;
  }

  public void setOffice(Integer office) {
    this.office = office;
  }


  public Appointment patient(Integer patient) {
    this.patient = patient;
    return this;
  }

  /**
   * ID of this appointment&#39;s patient. Breaks have a null patient field.
   * @return patient
   */
  @javax.annotation.Nonnull
  public Integer getPatient() {
    return patient;
  }

  public void setPatient(Integer patient) {
    this.patient = patient;
  }


  /**
   * 
   * @return primaryInsuranceIdNumber
   */
  @javax.annotation.Nullable
  public String getPrimaryInsuranceIdNumber() {
    return primaryInsuranceIdNumber;
  }



  /**
   * 
   * @return primaryInsurerName
   */
  @javax.annotation.Nullable
  public String getPrimaryInsurerName() {
    return primaryInsurerName;
  }



  /**
   * 
   * @return primaryInsurerPayerId
   */
  @javax.annotation.Nullable
  public String getPrimaryInsurerPayerId() {
    return primaryInsurerPayerId;
  }



  public Appointment profile(Integer profile) {
    this.profile = profile;
    return this;
  }

  /**
   * ID of an &#x60;/api/appointment_profiles&#x60; instance. The profile sets default values for &#x60;color&#x60;, &#x60;duration&#x60;, and &#x60;reason&#x60; on creation, which can be overriden by setting these values explicitly.
   * @return profile
   */
  @javax.annotation.Nullable
  public Integer getProfile() {
    return profile;
  }

  public void setProfile(Integer profile) {
    this.profile = profile;
  }


  public Appointment reason(String reason) {
    this.reason = reason;
    return this;
  }

  /**
   * Default to &#x60;\&quot;\&quot;&#x60;
   * @return reason
   */
  @javax.annotation.Nullable
  public String getReason() {
    return reason;
  }

  public void setReason(String reason) {
    this.reason = reason;
  }


  /**
   * Whether the appointment is a recurring appointment or not
   * @return recurringAppointment
   */
  @javax.annotation.Nullable
  public Boolean getRecurringAppointment() {
    return recurringAppointment;
  }



  public Appointment reminderProfile(String reminderProfile) {
    this.reminderProfile = reminderProfile;
    return this;
  }

  /**
   * Write-only. ID of an &#x60;/api/reminder_profiles&#x60; instance. Set this to apply a reminder profile to the appointment. Cannot be applied to an appointment with reminders.
   * @return reminderProfile
   */
  @javax.annotation.Nullable
  public String getReminderProfile() {
    return reminderProfile;
  }

  public void setReminderProfile(String reminderProfile) {
    this.reminderProfile = reminderProfile;
  }


  /**
   * Scheduled reminders of the appointment
   * @return reminders
   */
  @javax.annotation.Nullable
  public List<SimpleReminder> getReminders() {
    return reminders;
  }



  public Appointment scheduledTime(String scheduledTime) {
    this.scheduledTime = scheduledTime;
    return this;
  }

  /**
   * The starting time of the appointment
   * @return scheduledTime
   */
  @javax.annotation.Nonnull
  public String getScheduledTime() {
    return scheduledTime;
  }

  public void setScheduledTime(String scheduledTime) {
    this.scheduledTime = scheduledTime;
  }


  /**
   * 
   * @return secondaryInsuranceIdNumber
   */
  @javax.annotation.Nullable
  public String getSecondaryInsuranceIdNumber() {
    return secondaryInsuranceIdNumber;
  }



  /**
   * 
   * @return secondaryInsurerName
   */
  @javax.annotation.Nullable
  public String getSecondaryInsurerName() {
    return secondaryInsurerName;
  }



  /**
   * 
   * @return secondaryInsurerPayerId
   */
  @javax.annotation.Nullable
  public String getSecondaryInsurerPayerId() {
    return secondaryInsurerPayerId;
  }



  public Appointment status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * One of &#x60;&#x60;, &#x60;Arrived&#x60;, &#x60;Checked In&#x60;, &#x60;In Room&#x60;, &#x60;Cancelled&#x60;, &#x60;Complete&#x60;, &#x60;Confirmed&#x60;, &#x60;In Session&#x60;, &#x60;No Show&#x60;, &#x60;Not Confirmed&#x60;, or &#x60;Rescheduled&#x60;. Or one of the custom statuses.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  /**
   * 
   * @return statusTransitions
   */
  @javax.annotation.Nullable
  public List<AppointmentStatusTransition> getStatusTransitions() {
    return statusTransitions;
  }



  /**
   * Supervising provider of appointment if set.
   * @return supervisingProvider
   */
  @javax.annotation.Nullable
  public String getSupervisingProvider() {
    return supervisingProvider;
  }



  /**
   * 
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }



  public Appointment vitals(SystemVitals vitals) {
    this.vitals = vitals;
    return this;
  }

  /**
   * Get vitals
   * @return vitals
   */
  @javax.annotation.Nullable
  public SystemVitals getVitals() {
    return vitals;
  }

  public void setVitals(SystemVitals vitals) {
    this.vitals = vitals;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Appointment appointment = (Appointment) o;
    return Objects.equals(this.allowOverlapping, appointment.allowOverlapping) &&
        Objects.equals(this.apptIsBreak, appointment.apptIsBreak) &&
        Objects.equals(this.baseRecurringAppointment, appointment.baseRecurringAppointment) &&
        Objects.equals(this.billingNotes, appointment.billingNotes) &&
        Objects.equals(this.billingProvider, appointment.billingProvider) &&
        Objects.equals(this.billingStatus, appointment.billingStatus) &&
        Objects.equals(this.clinicalNote, appointment.clinicalNote) &&
        Objects.equals(this.clonedFrom, appointment.clonedFrom) &&
        Objects.equals(this.color, appointment.color) &&
        Objects.equals(this.createdAt, appointment.createdAt) &&
        Objects.equals(this.customFields, appointment.customFields) &&
        Objects.equals(this.customVitals, appointment.customVitals) &&
        Objects.equals(this.deletedFlag, appointment.deletedFlag) &&
        Objects.equals(this.doctor, appointment.doctor) &&
        Objects.equals(this.duration, appointment.duration) &&
        Objects.equals(this.examRoom, appointment.examRoom) &&
        Objects.equals(this.extendedUpdatedAt, appointment.extendedUpdatedAt) &&
        Objects.equals(this.firstBilledDate, appointment.firstBilledDate) &&
        Objects.equals(this.icd10Codes, appointment.icd10Codes) &&
        Objects.equals(this.icd9Codes, appointment.icd9Codes) &&
        Objects.equals(this.id, appointment.id) &&
        Objects.equals(this.ins1Status, appointment.ins1Status) &&
        Objects.equals(this.ins2Status, appointment.ins2Status) &&
        Objects.equals(this.isVirtualBase, appointment.isVirtualBase) &&
        Objects.equals(this.isWalkIn, appointment.isWalkIn) &&
        Objects.equals(this.lastBilledDate, appointment.lastBilledDate) &&
        Objects.equals(this.notes, appointment.notes) &&
        Objects.equals(this.office, appointment.office) &&
        Objects.equals(this.patient, appointment.patient) &&
        Objects.equals(this.primaryInsuranceIdNumber, appointment.primaryInsuranceIdNumber) &&
        Objects.equals(this.primaryInsurerName, appointment.primaryInsurerName) &&
        Objects.equals(this.primaryInsurerPayerId, appointment.primaryInsurerPayerId) &&
        Objects.equals(this.profile, appointment.profile) &&
        Objects.equals(this.reason, appointment.reason) &&
        Objects.equals(this.recurringAppointment, appointment.recurringAppointment) &&
        Objects.equals(this.reminderProfile, appointment.reminderProfile) &&
        Objects.equals(this.reminders, appointment.reminders) &&
        Objects.equals(this.scheduledTime, appointment.scheduledTime) &&
        Objects.equals(this.secondaryInsuranceIdNumber, appointment.secondaryInsuranceIdNumber) &&
        Objects.equals(this.secondaryInsurerName, appointment.secondaryInsurerName) &&
        Objects.equals(this.secondaryInsurerPayerId, appointment.secondaryInsurerPayerId) &&
        Objects.equals(this.status, appointment.status) &&
        Objects.equals(this.statusTransitions, appointment.statusTransitions) &&
        Objects.equals(this.supervisingProvider, appointment.supervisingProvider) &&
        Objects.equals(this.updatedAt, appointment.updatedAt) &&
        Objects.equals(this.vitals, appointment.vitals);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowOverlapping, apptIsBreak, baseRecurringAppointment, billingNotes, billingProvider, billingStatus, clinicalNote, clonedFrom, color, createdAt, customFields, customVitals, deletedFlag, doctor, duration, examRoom, extendedUpdatedAt, firstBilledDate, icd10Codes, icd9Codes, id, ins1Status, ins2Status, isVirtualBase, isWalkIn, lastBilledDate, notes, office, patient, primaryInsuranceIdNumber, primaryInsurerName, primaryInsurerPayerId, profile, reason, recurringAppointment, reminderProfile, reminders, scheduledTime, secondaryInsuranceIdNumber, secondaryInsurerName, secondaryInsurerPayerId, status, statusTransitions, supervisingProvider, updatedAt, vitals);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Appointment {\n");
    sb.append("    allowOverlapping: ").append(toIndentedString(allowOverlapping)).append("\n");
    sb.append("    apptIsBreak: ").append(toIndentedString(apptIsBreak)).append("\n");
    sb.append("    baseRecurringAppointment: ").append(toIndentedString(baseRecurringAppointment)).append("\n");
    sb.append("    billingNotes: ").append(toIndentedString(billingNotes)).append("\n");
    sb.append("    billingProvider: ").append(toIndentedString(billingProvider)).append("\n");
    sb.append("    billingStatus: ").append(toIndentedString(billingStatus)).append("\n");
    sb.append("    clinicalNote: ").append(toIndentedString(clinicalNote)).append("\n");
    sb.append("    clonedFrom: ").append(toIndentedString(clonedFrom)).append("\n");
    sb.append("    color: ").append(toIndentedString(color)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    customFields: ").append(toIndentedString(customFields)).append("\n");
    sb.append("    customVitals: ").append(toIndentedString(customVitals)).append("\n");
    sb.append("    deletedFlag: ").append(toIndentedString(deletedFlag)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    examRoom: ").append(toIndentedString(examRoom)).append("\n");
    sb.append("    extendedUpdatedAt: ").append(toIndentedString(extendedUpdatedAt)).append("\n");
    sb.append("    firstBilledDate: ").append(toIndentedString(firstBilledDate)).append("\n");
    sb.append("    icd10Codes: ").append(toIndentedString(icd10Codes)).append("\n");
    sb.append("    icd9Codes: ").append(toIndentedString(icd9Codes)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    ins1Status: ").append(toIndentedString(ins1Status)).append("\n");
    sb.append("    ins2Status: ").append(toIndentedString(ins2Status)).append("\n");
    sb.append("    isVirtualBase: ").append(toIndentedString(isVirtualBase)).append("\n");
    sb.append("    isWalkIn: ").append(toIndentedString(isWalkIn)).append("\n");
    sb.append("    lastBilledDate: ").append(toIndentedString(lastBilledDate)).append("\n");
    sb.append("    notes: ").append(toIndentedString(notes)).append("\n");
    sb.append("    office: ").append(toIndentedString(office)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    primaryInsuranceIdNumber: ").append(toIndentedString(primaryInsuranceIdNumber)).append("\n");
    sb.append("    primaryInsurerName: ").append(toIndentedString(primaryInsurerName)).append("\n");
    sb.append("    primaryInsurerPayerId: ").append(toIndentedString(primaryInsurerPayerId)).append("\n");
    sb.append("    profile: ").append(toIndentedString(profile)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
    sb.append("    recurringAppointment: ").append(toIndentedString(recurringAppointment)).append("\n");
    sb.append("    reminderProfile: ").append(toIndentedString(reminderProfile)).append("\n");
    sb.append("    reminders: ").append(toIndentedString(reminders)).append("\n");
    sb.append("    scheduledTime: ").append(toIndentedString(scheduledTime)).append("\n");
    sb.append("    secondaryInsuranceIdNumber: ").append(toIndentedString(secondaryInsuranceIdNumber)).append("\n");
    sb.append("    secondaryInsurerName: ").append(toIndentedString(secondaryInsurerName)).append("\n");
    sb.append("    secondaryInsurerPayerId: ").append(toIndentedString(secondaryInsurerPayerId)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    statusTransitions: ").append(toIndentedString(statusTransitions)).append("\n");
    sb.append("    supervisingProvider: ").append(toIndentedString(supervisingProvider)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    vitals: ").append(toIndentedString(vitals)).append("\n");
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
    openapiFields.add("allow_overlapping");
    openapiFields.add("appt_is_break");
    openapiFields.add("base_recurring_appointment");
    openapiFields.add("billing_notes");
    openapiFields.add("billing_provider");
    openapiFields.add("billing_status");
    openapiFields.add("clinical_note");
    openapiFields.add("cloned_from");
    openapiFields.add("color");
    openapiFields.add("created_at");
    openapiFields.add("custom_fields");
    openapiFields.add("custom_vitals");
    openapiFields.add("deleted_flag");
    openapiFields.add("doctor");
    openapiFields.add("duration");
    openapiFields.add("exam_room");
    openapiFields.add("extended_updated_at");
    openapiFields.add("first_billed_date");
    openapiFields.add("icd10_codes");
    openapiFields.add("icd9_codes");
    openapiFields.add("id");
    openapiFields.add("ins1_status");
    openapiFields.add("ins2_status");
    openapiFields.add("is_virtual_base");
    openapiFields.add("is_walk_in");
    openapiFields.add("last_billed_date");
    openapiFields.add("notes");
    openapiFields.add("office");
    openapiFields.add("patient");
    openapiFields.add("primary_insurance_id_number");
    openapiFields.add("primary_insurer_name");
    openapiFields.add("primary_insurer_payer_id");
    openapiFields.add("profile");
    openapiFields.add("reason");
    openapiFields.add("recurring_appointment");
    openapiFields.add("reminder_profile");
    openapiFields.add("reminders");
    openapiFields.add("scheduled_time");
    openapiFields.add("secondary_insurance_id_number");
    openapiFields.add("secondary_insurer_name");
    openapiFields.add("secondary_insurer_payer_id");
    openapiFields.add("status");
    openapiFields.add("status_transitions");
    openapiFields.add("supervising_provider");
    openapiFields.add("updated_at");
    openapiFields.add("vitals");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("doctor");
    openapiRequiredFields.add("exam_room");
    openapiRequiredFields.add("office");
    openapiRequiredFields.add("patient");
    openapiRequiredFields.add("scheduled_time");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Appointment
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Appointment.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Appointment is not found in the empty JSON string", Appointment.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Appointment.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Appointment` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Appointment.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("base_recurring_appointment") != null && !jsonObj.get("base_recurring_appointment").isJsonNull()) && !jsonObj.get("base_recurring_appointment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `base_recurring_appointment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("base_recurring_appointment").toString()));
      }
      if (jsonObj.get("billing_notes") != null && !jsonObj.get("billing_notes").isJsonNull()) {
        JsonArray jsonArraybillingNotes = jsonObj.getAsJsonArray("billing_notes");
        if (jsonArraybillingNotes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("billing_notes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `billing_notes` to be an array in the JSON string but got `%s`", jsonObj.get("billing_notes").toString()));
          }

          // validate the optional field `billing_notes` (array)
          for (int i = 0; i < jsonArraybillingNotes.size(); i++) {
            ClaimBillingNotes1.validateJsonElement(jsonArraybillingNotes.get(i));
          };
        }
      }
      if ((jsonObj.get("billing_provider") != null && !jsonObj.get("billing_provider").isJsonNull()) && !jsonObj.get("billing_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billing_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billing_provider").toString()));
      }
      if ((jsonObj.get("billing_status") != null && !jsonObj.get("billing_status").isJsonNull()) && !jsonObj.get("billing_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billing_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billing_status").toString()));
      }
      // validate the optional field `clinical_note`
      if (jsonObj.get("clinical_note") != null && !jsonObj.get("clinical_note").isJsonNull()) {
        ClinicalNote1.validateJsonElement(jsonObj.get("clinical_note"));
      }
      if ((jsonObj.get("color") != null && !jsonObj.get("color").isJsonNull()) && !jsonObj.get("color").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `color` to be a primitive type in the JSON string but got `%s`", jsonObj.get("color").toString()));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if (jsonObj.get("custom_fields") != null && !jsonObj.get("custom_fields").isJsonNull()) {
        JsonArray jsonArraycustomFields = jsonObj.getAsJsonArray("custom_fields");
        if (jsonArraycustomFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_fields` to be an array in the JSON string but got `%s`", jsonObj.get("custom_fields").toString()));
          }

          // validate the optional field `custom_fields` (array)
          for (int i = 0; i < jsonArraycustomFields.size(); i++) {
            CustomAppointmentFieldValue.validateJsonElement(jsonArraycustomFields.get(i));
          };
        }
      }
      if (jsonObj.get("custom_vitals") != null && !jsonObj.get("custom_vitals").isJsonNull()) {
        JsonArray jsonArraycustomVitals = jsonObj.getAsJsonArray("custom_vitals");
        if (jsonArraycustomVitals != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_vitals").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_vitals` to be an array in the JSON string but got `%s`", jsonObj.get("custom_vitals").toString()));
          }

          // validate the optional field `custom_vitals` (array)
          for (int i = 0; i < jsonArraycustomVitals.size(); i++) {
            CustomVitalValue.validateJsonElement(jsonArraycustomVitals.get(i));
          };
        }
      }
      if ((jsonObj.get("extended_updated_at") != null && !jsonObj.get("extended_updated_at").isJsonNull()) && !jsonObj.get("extended_updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `extended_updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("extended_updated_at").toString()));
      }
      if ((jsonObj.get("first_billed_date") != null && !jsonObj.get("first_billed_date").isJsonNull()) && !jsonObj.get("first_billed_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_billed_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_billed_date").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("icd10_codes") != null && !jsonObj.get("icd10_codes").isJsonNull() && !jsonObj.get("icd10_codes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `icd10_codes` to be an array in the JSON string but got `%s`", jsonObj.get("icd10_codes").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("icd9_codes") != null && !jsonObj.get("icd9_codes").isJsonNull() && !jsonObj.get("icd9_codes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `icd9_codes` to be an array in the JSON string but got `%s`", jsonObj.get("icd9_codes").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("ins1_status") != null && !jsonObj.get("ins1_status").isJsonNull()) && !jsonObj.get("ins1_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ins1_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ins1_status").toString()));
      }
      // validate the optional field `ins1_status`
      if (jsonObj.get("ins1_status") != null && !jsonObj.get("ins1_status").isJsonNull()) {
        Ins1StatusEnum.validateJsonElement(jsonObj.get("ins1_status"));
      }
      if ((jsonObj.get("ins2_status") != null && !jsonObj.get("ins2_status").isJsonNull()) && !jsonObj.get("ins2_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ins2_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ins2_status").toString()));
      }
      // validate the optional field `ins2_status`
      if (jsonObj.get("ins2_status") != null && !jsonObj.get("ins2_status").isJsonNull()) {
        Ins2StatusEnum.validateJsonElement(jsonObj.get("ins2_status"));
      }
      if ((jsonObj.get("last_billed_date") != null && !jsonObj.get("last_billed_date").isJsonNull()) && !jsonObj.get("last_billed_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_billed_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_billed_date").toString()));
      }
      if ((jsonObj.get("notes") != null && !jsonObj.get("notes").isJsonNull()) && !jsonObj.get("notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("notes").toString()));
      }
      if ((jsonObj.get("primary_insurance_id_number") != null && !jsonObj.get("primary_insurance_id_number").isJsonNull()) && !jsonObj.get("primary_insurance_id_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primary_insurance_id_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primary_insurance_id_number").toString()));
      }
      if ((jsonObj.get("primary_insurer_name") != null && !jsonObj.get("primary_insurer_name").isJsonNull()) && !jsonObj.get("primary_insurer_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primary_insurer_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primary_insurer_name").toString()));
      }
      if ((jsonObj.get("primary_insurer_payer_id") != null && !jsonObj.get("primary_insurer_payer_id").isJsonNull()) && !jsonObj.get("primary_insurer_payer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primary_insurer_payer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primary_insurer_payer_id").toString()));
      }
      if ((jsonObj.get("reason") != null && !jsonObj.get("reason").isJsonNull()) && !jsonObj.get("reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reason").toString()));
      }
      if ((jsonObj.get("reminder_profile") != null && !jsonObj.get("reminder_profile").isJsonNull()) && !jsonObj.get("reminder_profile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reminder_profile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reminder_profile").toString()));
      }
      if (jsonObj.get("reminders") != null && !jsonObj.get("reminders").isJsonNull()) {
        JsonArray jsonArrayreminders = jsonObj.getAsJsonArray("reminders");
        if (jsonArrayreminders != null) {
          // ensure the json data is an array
          if (!jsonObj.get("reminders").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `reminders` to be an array in the JSON string but got `%s`", jsonObj.get("reminders").toString()));
          }

          // validate the optional field `reminders` (array)
          for (int i = 0; i < jsonArrayreminders.size(); i++) {
            SimpleReminder.validateJsonElement(jsonArrayreminders.get(i));
          };
        }
      }
      if (!jsonObj.get("scheduled_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scheduled_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scheduled_time").toString()));
      }
      if ((jsonObj.get("secondary_insurance_id_number") != null && !jsonObj.get("secondary_insurance_id_number").isJsonNull()) && !jsonObj.get("secondary_insurance_id_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secondary_insurance_id_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secondary_insurance_id_number").toString()));
      }
      if ((jsonObj.get("secondary_insurer_name") != null && !jsonObj.get("secondary_insurer_name").isJsonNull()) && !jsonObj.get("secondary_insurer_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secondary_insurer_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secondary_insurer_name").toString()));
      }
      if ((jsonObj.get("secondary_insurer_payer_id") != null && !jsonObj.get("secondary_insurer_payer_id").isJsonNull()) && !jsonObj.get("secondary_insurer_payer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `secondary_insurer_payer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("secondary_insurer_payer_id").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if (jsonObj.get("status_transitions") != null && !jsonObj.get("status_transitions").isJsonNull()) {
        JsonArray jsonArraystatusTransitions = jsonObj.getAsJsonArray("status_transitions");
        if (jsonArraystatusTransitions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("status_transitions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `status_transitions` to be an array in the JSON string but got `%s`", jsonObj.get("status_transitions").toString()));
          }

          // validate the optional field `status_transitions` (array)
          for (int i = 0; i < jsonArraystatusTransitions.size(); i++) {
            AppointmentStatusTransition.validateJsonElement(jsonArraystatusTransitions.get(i));
          };
        }
      }
      if ((jsonObj.get("supervising_provider") != null && !jsonObj.get("supervising_provider").isJsonNull()) && !jsonObj.get("supervising_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `supervising_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("supervising_provider").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
      // validate the optional field `vitals`
      if (jsonObj.get("vitals") != null && !jsonObj.get("vitals").isJsonNull()) {
        SystemVitals.validateJsonElement(jsonObj.get("vitals"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Appointment.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Appointment' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Appointment> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Appointment.class));

       return (TypeAdapter<T>) new TypeAdapter<Appointment>() {
           @Override
           public void write(JsonWriter out, Appointment value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Appointment read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Appointment given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Appointment
   * @throws IOException if the JSON string is invalid with respect to Appointment
   */
  public static Appointment fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Appointment.class);
  }

  /**
   * Convert an instance of Appointment to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

