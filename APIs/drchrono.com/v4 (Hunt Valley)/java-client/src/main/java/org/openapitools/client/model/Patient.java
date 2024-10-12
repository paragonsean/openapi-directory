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
import org.openapitools.client.model.AutoAccidentInsurance;
import org.openapitools.client.model.CustomPatientFieldValue;
import org.openapitools.client.model.Patient1;
import org.openapitools.client.model.PatientFlag;
import org.openapitools.client.model.PatientFlagType1;
import org.openapitools.client.model.PrimaryInsurance;
import org.openapitools.client.model.SecondaryInsurance;
import org.openapitools.client.model.TertiaryInsurance;
import org.openapitools.client.model.WorkerCompInsurance;

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
 * Patient
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Patient {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_INSURANCE = "auto_accident_insurance";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_INSURANCE)
  private AutoAccidentInsurance autoAccidentInsurance;

  public static final String SERIALIZED_NAME_CELL_PHONE = "cell_phone";
  @SerializedName(SERIALIZED_NAME_CELL_PHONE)
  private String cellPhone;

  public static final String SERIALIZED_NAME_CHART_ID = "chart_id";
  @SerializedName(SERIALIZED_NAME_CHART_ID)
  private String chartId;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_COPAY = "copay";
  @SerializedName(SERIALIZED_NAME_COPAY)
  private String copay;

  public static final String SERIALIZED_NAME_CUSTOM_DEMOGRAPHICS = "custom_demographics";
  @SerializedName(SERIALIZED_NAME_CUSTOM_DEMOGRAPHICS)
  private List<CustomPatientFieldValue> customDemographics = new ArrayList<>();

  public static final String SERIALIZED_NAME_DATE_OF_BIRTH = "date_of_birth";
  @SerializedName(SERIALIZED_NAME_DATE_OF_BIRTH)
  private String dateOfBirth;

  public static final String SERIALIZED_NAME_DATE_OF_FIRST_APPOINTMENT = "date_of_first_appointment";
  @SerializedName(SERIALIZED_NAME_DATE_OF_FIRST_APPOINTMENT)
  private String dateOfFirstAppointment;

  public static final String SERIALIZED_NAME_DATE_OF_LAST_APPOINTMENT = "date_of_last_appointment";
  @SerializedName(SERIALIZED_NAME_DATE_OF_LAST_APPOINTMENT)
  private String dateOfLastAppointment;

  public static final String SERIALIZED_NAME_DEFAULT_PHARMACY = "default_pharmacy";
  @SerializedName(SERIALIZED_NAME_DEFAULT_PHARMACY)
  private String defaultPharmacy;

  public static final String SERIALIZED_NAME_DISABLE_SMS_MESSAGES = "disable_sms_messages";
  @SerializedName(SERIALIZED_NAME_DISABLE_SMS_MESSAGES)
  private Boolean disableSmsMessages;

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private Integer doctor;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_EMERGENCY_CONTACT_NAME = "emergency_contact_name";
  @SerializedName(SERIALIZED_NAME_EMERGENCY_CONTACT_NAME)
  private String emergencyContactName;

  public static final String SERIALIZED_NAME_EMERGENCY_CONTACT_PHONE = "emergency_contact_phone";
  @SerializedName(SERIALIZED_NAME_EMERGENCY_CONTACT_PHONE)
  private String emergencyContactPhone;

  public static final String SERIALIZED_NAME_EMERGENCY_CONTACT_RELATION = "emergency_contact_relation";
  @SerializedName(SERIALIZED_NAME_EMERGENCY_CONTACT_RELATION)
  private String emergencyContactRelation;

  public static final String SERIALIZED_NAME_EMPLOYER = "employer";
  @SerializedName(SERIALIZED_NAME_EMPLOYER)
  private String employer;

  public static final String SERIALIZED_NAME_EMPLOYER_ADDRESS = "employer_address";
  @SerializedName(SERIALIZED_NAME_EMPLOYER_ADDRESS)
  private String employerAddress;

  public static final String SERIALIZED_NAME_EMPLOYER_CITY = "employer_city";
  @SerializedName(SERIALIZED_NAME_EMPLOYER_CITY)
  private String employerCity;

  public static final String SERIALIZED_NAME_EMPLOYER_STATE = "employer_state";
  @SerializedName(SERIALIZED_NAME_EMPLOYER_STATE)
  private String employerState;

  public static final String SERIALIZED_NAME_EMPLOYER_ZIP_CODE = "employer_zip_code";
  @SerializedName(SERIALIZED_NAME_EMPLOYER_ZIP_CODE)
  private String employerZipCode;

  /**
   * One of &#x60;\&quot;blank\&quot;&#x60;, &#x60;\&quot;hispanic\&quot;&#x60;, &#x60;\&quot;not_hispanic\&quot;&#x60; or &#x60;\&quot;declined\&quot;&#x60;
   */
  @JsonAdapter(EthnicityEnum.Adapter.class)
  public enum EthnicityEnum {
    BLANK("blank"),
    
    HISPANIC("hispanic"),
    
    NOT_HISPANIC("not_hispanic"),
    
    DECLINED("declined");

    private String value;

    EthnicityEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EthnicityEnum fromValue(String value) {
      for (EthnicityEnum b : EthnicityEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EthnicityEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EthnicityEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EthnicityEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EthnicityEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EthnicityEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ETHNICITY = "ethnicity";
  @SerializedName(SERIALIZED_NAME_ETHNICITY)
  private EthnicityEnum ethnicity;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  /**
   * One of &#x60;\&quot;Male\&quot;&#x60;, &#x60;\&quot;Female\&quot;&#x60;, or &#x60;\&quot;Other\&quot;&#x60;
   */
  @JsonAdapter(GenderEnum.Adapter.class)
  public enum GenderEnum {
    EMPTY(""),
    
    MALE("Male"),
    
    FEMALE("Female"),
    
    OTHER("Other"),
    
    UNK("UNK"),
    
    ASKU("ASKU");

    private String value;

    GenderEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static GenderEnum fromValue(String value) {
      for (GenderEnum b : GenderEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<GenderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final GenderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public GenderEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return GenderEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      GenderEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_GENDER = "gender";
  @SerializedName(SERIALIZED_NAME_GENDER)
  private GenderEnum gender;

  public static final String SERIALIZED_NAME_HOME_PHONE = "home_phone";
  @SerializedName(SERIALIZED_NAME_HOME_PHONE)
  private String homePhone;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_MIDDLE_NAME = "middle_name";
  @SerializedName(SERIALIZED_NAME_MIDDLE_NAME)
  private String middleName;

  public static final String SERIALIZED_NAME_NICK_NAME = "nick_name";
  @SerializedName(SERIALIZED_NAME_NICK_NAME)
  private String nickName;

  public static final String SERIALIZED_NAME_OFFICE_PHONE = "office_phone";
  @SerializedName(SERIALIZED_NAME_OFFICE_PHONE)
  private String officePhone;

  public static final String SERIALIZED_NAME_OFFICES = "offices";
  @SerializedName(SERIALIZED_NAME_OFFICES)
  private List<Integer> offices = new ArrayList<>();

  public static final String SERIALIZED_NAME_PATIENT_FLAGS = "patient_flags";
  @SerializedName(SERIALIZED_NAME_PATIENT_FLAGS)
  private List<PatientFlagType1> patientFlags = new ArrayList<>();

  public static final String SERIALIZED_NAME_PATIENT_FLAGS_ATTACHED = "patient_flags_attached";
  @SerializedName(SERIALIZED_NAME_PATIENT_FLAGS_ATTACHED)
  private List<PatientFlag> patientFlagsAttached = new ArrayList<>();

  /**
   * One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Cash\&quot;&#x60;, &#x60;\&quot;Insurance\&quot;&#x60;, &#x60;\&quot;Insurance Out of Network\&quot;&#x60;, &#x60;\&quot;Auto Accident\&quot;&#x60; or &#x60;\&quot;Worker&#39;s Comp\&quot;&#x60;.&lt;br&gt;**Note:** Patient must already have either &#x60;primary_insurance&#x60; or &#x60;secondary_insurance&#x60; or new &#x60;primary_insurance&#x60; or &#x60;secondary_insurance&#x60; is passed in request if &#x60;Insurance&#x60;, &#x60;Auto Accident&#x60; or &#x60;Worker&#39;s Comp&#x60; payment profiles are chosen.
   */
  @JsonAdapter(PatientPaymentProfileEnum.Adapter.class)
  public enum PatientPaymentProfileEnum {
    EMPTY(""),
    
    CASH("Cash"),
    
    INSURANCE("Insurance"),
    
    INSURANCE_OUT_OF_NETWORK("Insurance Out of Network"),
    
    AUTO_ACCIDENT("Auto Accident"),
    
    WORKER_S_COMP("Worker's Comp");

    private String value;

    PatientPaymentProfileEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PatientPaymentProfileEnum fromValue(String value) {
      for (PatientPaymentProfileEnum b : PatientPaymentProfileEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PatientPaymentProfileEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PatientPaymentProfileEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PatientPaymentProfileEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PatientPaymentProfileEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PatientPaymentProfileEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PATIENT_PAYMENT_PROFILE = "patient_payment_profile";
  @SerializedName(SERIALIZED_NAME_PATIENT_PAYMENT_PROFILE)
  private PatientPaymentProfileEnum patientPaymentProfile;

  public static final String SERIALIZED_NAME_PATIENT_PHOTO = "patient_photo";
  @SerializedName(SERIALIZED_NAME_PATIENT_PHOTO)
  private String patientPhoto;

  public static final String SERIALIZED_NAME_PATIENT_PHOTO_DATE = "patient_photo_date";
  @SerializedName(SERIALIZED_NAME_PATIENT_PHOTO_DATE)
  private String patientPhotoDate;

  /**
   * One of &#x60;\&quot;A\&quot;&#x60; (active), &#x60;\&quot;I\&quot;&#x60; (inactive), &#x60;\&quot;D\&quot;&#x60; (inactive-deceased)
   */
  @JsonAdapter(PatientStatusEnum.Adapter.class)
  public enum PatientStatusEnum {
    A("A"),
    
    I("I"),
    
    D("D");

    private String value;

    PatientStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PatientStatusEnum fromValue(String value) {
      for (PatientStatusEnum b : PatientStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PatientStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PatientStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PatientStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PatientStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PatientStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PATIENT_STATUS = "patient_status";
  @SerializedName(SERIALIZED_NAME_PATIENT_STATUS)
  private PatientStatusEnum patientStatus;

  /**
   * Use ISO 639 alpha-3 codes
   */
  @JsonAdapter(PreferredLanguageEnum.Adapter.class)
  public enum PreferredLanguageEnum {
    BLANK("blank"),
    
    ENG("eng"),
    
    ZHO("zho"),
    
    FRA("fra"),
    
    ITA("ita"),
    
    JPN("jpn"),
    
    POR("por"),
    
    RUS("rus"),
    
    SPA("spa"),
    
    OTHER("other"),
    
    UNKNOWN("unknown"),
    
    DECLINED("declined");

    private String value;

    PreferredLanguageEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PreferredLanguageEnum fromValue(String value) {
      for (PreferredLanguageEnum b : PreferredLanguageEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PreferredLanguageEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PreferredLanguageEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PreferredLanguageEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PreferredLanguageEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PreferredLanguageEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PREFERRED_LANGUAGE = "preferred_language";
  @SerializedName(SERIALIZED_NAME_PREFERRED_LANGUAGE)
  private PreferredLanguageEnum preferredLanguage;

  public static final String SERIALIZED_NAME_PRIMARY_CARE_PHYSICIAN = "primary_care_physician";
  @SerializedName(SERIALIZED_NAME_PRIMARY_CARE_PHYSICIAN)
  private String primaryCarePhysician;

  public static final String SERIALIZED_NAME_PRIMARY_INSURANCE = "primary_insurance";
  @SerializedName(SERIALIZED_NAME_PRIMARY_INSURANCE)
  private PrimaryInsurance primaryInsurance;

  /**
   * One of &#x60;\&quot;blank\&quot;&#x60;, &#x60;\&quot;indian\&quot;&#x60;, &#x60;\&quot;asian\&quot;&#x60;, &#x60;\&quot;black\&quot;&#x60;, &#x60;\&quot;hawaiian\&quot;&#x60;, &#x60;\&quot;white\&quot;&#x60; or &#x60;\&quot;declined\&quot;&#x60;
   */
  @JsonAdapter(RaceEnum.Adapter.class)
  public enum RaceEnum {
    BLANK("blank"),
    
    INDIAN("indian"),
    
    ASIAN("asian"),
    
    BLACK("black"),
    
    HAWAIIAN("hawaiian"),
    
    WHITE("white"),
    
    OTHER("other"),
    
    DECLINED("declined");

    private String value;

    RaceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RaceEnum fromValue(String value) {
      for (RaceEnum b : RaceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RaceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RaceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RaceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RaceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RaceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RACE = "race";
  @SerializedName(SERIALIZED_NAME_RACE)
  private RaceEnum race;

  public static final String SERIALIZED_NAME_REFERRING_DOCTOR = "referring_doctor";
  @SerializedName(SERIALIZED_NAME_REFERRING_DOCTOR)
  private Patient1 referringDoctor;

  public static final String SERIALIZED_NAME_REFERRING_SOURCE = "referring_source";
  @SerializedName(SERIALIZED_NAME_REFERRING_SOURCE)
  private String referringSource;

  public static final String SERIALIZED_NAME_RESPONSIBLE_PARTY_EMAIL = "responsible_party_email";
  @SerializedName(SERIALIZED_NAME_RESPONSIBLE_PARTY_EMAIL)
  private String responsiblePartyEmail;

  public static final String SERIALIZED_NAME_RESPONSIBLE_PARTY_NAME = "responsible_party_name";
  @SerializedName(SERIALIZED_NAME_RESPONSIBLE_PARTY_NAME)
  private String responsiblePartyName;

  public static final String SERIALIZED_NAME_RESPONSIBLE_PARTY_PHONE = "responsible_party_phone";
  @SerializedName(SERIALIZED_NAME_RESPONSIBLE_PARTY_PHONE)
  private String responsiblePartyPhone;

  public static final String SERIALIZED_NAME_RESPONSIBLE_PARTY_RELATION = "responsible_party_relation";
  @SerializedName(SERIALIZED_NAME_RESPONSIBLE_PARTY_RELATION)
  private String responsiblePartyRelation;

  public static final String SERIALIZED_NAME_SECONDARY_INSURANCE = "secondary_insurance";
  @SerializedName(SERIALIZED_NAME_SECONDARY_INSURANCE)
  private SecondaryInsurance secondaryInsurance;

  public static final String SERIALIZED_NAME_SOCIAL_SECURITY_NUMBER = "social_security_number";
  @SerializedName(SERIALIZED_NAME_SOCIAL_SECURITY_NUMBER)
  private String socialSecurityNumber;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private String state;

  public static final String SERIALIZED_NAME_TERTIARY_INSURANCE = "tertiary_insurance";
  @SerializedName(SERIALIZED_NAME_TERTIARY_INSURANCE)
  private TertiaryInsurance tertiaryInsurance;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public static final String SERIALIZED_NAME_WORKERS_COMP_INSURANCE = "workers_comp_insurance";
  @SerializedName(SERIALIZED_NAME_WORKERS_COMP_INSURANCE)
  private WorkerCompInsurance workersCompInsurance;

  public static final String SERIALIZED_NAME_ZIP_CODE = "zip_code";
  @SerializedName(SERIALIZED_NAME_ZIP_CODE)
  private String zipCode;

  public Patient() {
  }

  public Patient(
     Integer id, 
     List<PatientFlagType1> patientFlags, 
     String updatedAt
  ) {
    this();
    this.id = id;
    this.patientFlags = patientFlags;
    this.updatedAt = updatedAt;
  }

  public Patient address(String address) {
    this.address = address;
    return this;
  }

  /**
   * 
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }

  public void setAddress(String address) {
    this.address = address;
  }


  public Patient autoAccidentInsurance(AutoAccidentInsurance autoAccidentInsurance) {
    this.autoAccidentInsurance = autoAccidentInsurance;
    return this;
  }

  /**
   * Get autoAccidentInsurance
   * @return autoAccidentInsurance
   */
  @javax.annotation.Nullable
  public AutoAccidentInsurance getAutoAccidentInsurance() {
    return autoAccidentInsurance;
  }

  public void setAutoAccidentInsurance(AutoAccidentInsurance autoAccidentInsurance) {
    this.autoAccidentInsurance = autoAccidentInsurance;
  }


  public Patient cellPhone(String cellPhone) {
    this.cellPhone = cellPhone;
    return this;
  }

  /**
   * 
   * @return cellPhone
   */
  @javax.annotation.Nullable
  public String getCellPhone() {
    return cellPhone;
  }

  public void setCellPhone(String cellPhone) {
    this.cellPhone = cellPhone;
  }


  public Patient chartId(String chartId) {
    this.chartId = chartId;
    return this;
  }

  /**
   * Automatically set using first &amp; last name if absent
   * @return chartId
   */
  @javax.annotation.Nullable
  public String getChartId() {
    return chartId;
  }

  public void setChartId(String chartId) {
    this.chartId = chartId;
  }


  public Patient city(String city) {
    this.city = city;
    return this;
  }

  /**
   * 
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public Patient copay(String copay) {
    this.copay = copay;
    return this;
  }

  /**
   * 
   * @return copay
   */
  @javax.annotation.Nullable
  public String getCopay() {
    return copay;
  }

  public void setCopay(String copay) {
    this.copay = copay;
  }


  public Patient customDemographics(List<CustomPatientFieldValue> customDemographics) {
    this.customDemographics = customDemographics;
    return this;
  }

  public Patient addCustomDemographicsItem(CustomPatientFieldValue customDemographicsItem) {
    if (this.customDemographics == null) {
      this.customDemographics = new ArrayList<>();
    }
    this.customDemographics.add(customDemographicsItem);
    return this;
  }

  /**
   * 
   * @return customDemographics
   */
  @javax.annotation.Nullable
  public List<CustomPatientFieldValue> getCustomDemographics() {
    return customDemographics;
  }

  public void setCustomDemographics(List<CustomPatientFieldValue> customDemographics) {
    this.customDemographics = customDemographics;
  }


  public Patient dateOfBirth(String dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
    return this;
  }

  /**
   * 
   * @return dateOfBirth
   */
  @javax.annotation.Nullable
  public String getDateOfBirth() {
    return dateOfBirth;
  }

  public void setDateOfBirth(String dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
  }


  public Patient dateOfFirstAppointment(String dateOfFirstAppointment) {
    this.dateOfFirstAppointment = dateOfFirstAppointment;
    return this;
  }

  /**
   * Date of first patient visit.
   * @return dateOfFirstAppointment
   */
  @javax.annotation.Nullable
  public String getDateOfFirstAppointment() {
    return dateOfFirstAppointment;
  }

  public void setDateOfFirstAppointment(String dateOfFirstAppointment) {
    this.dateOfFirstAppointment = dateOfFirstAppointment;
  }


  public Patient dateOfLastAppointment(String dateOfLastAppointment) {
    this.dateOfLastAppointment = dateOfLastAppointment;
    return this;
  }

  /**
   * Date of previous patient visit
   * @return dateOfLastAppointment
   */
  @javax.annotation.Nullable
  public String getDateOfLastAppointment() {
    return dateOfLastAppointment;
  }

  public void setDateOfLastAppointment(String dateOfLastAppointment) {
    this.dateOfLastAppointment = dateOfLastAppointment;
  }


  public Patient defaultPharmacy(String defaultPharmacy) {
    this.defaultPharmacy = defaultPharmacy;
    return this;
  }

  /**
   * ncpdp id of patient&#39;s default pharmacy
   * @return defaultPharmacy
   */
  @javax.annotation.Nullable
  public String getDefaultPharmacy() {
    return defaultPharmacy;
  }

  public void setDefaultPharmacy(String defaultPharmacy) {
    this.defaultPharmacy = defaultPharmacy;
  }


  public Patient disableSmsMessages(Boolean disableSmsMessages) {
    this.disableSmsMessages = disableSmsMessages;
    return this;
  }

  /**
   * If True, suppress SMS/Txt messages to this patient even if we have a cell phone # for them.
   * @return disableSmsMessages
   */
  @javax.annotation.Nullable
  public Boolean getDisableSmsMessages() {
    return disableSmsMessages;
  }

  public void setDisableSmsMessages(Boolean disableSmsMessages) {
    this.disableSmsMessages = disableSmsMessages;
  }


  public Patient doctor(Integer doctor) {
    this.doctor = doctor;
    return this;
  }

  /**
   * 
   * @return doctor
   */
  @javax.annotation.Nonnull
  public Integer getDoctor() {
    return doctor;
  }

  public void setDoctor(Integer doctor) {
    this.doctor = doctor;
  }


  public Patient email(String email) {
    this.email = email;
    return this;
  }

  /**
   * 
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public Patient emergencyContactName(String emergencyContactName) {
    this.emergencyContactName = emergencyContactName;
    return this;
  }

  /**
   * 
   * @return emergencyContactName
   */
  @javax.annotation.Nullable
  public String getEmergencyContactName() {
    return emergencyContactName;
  }

  public void setEmergencyContactName(String emergencyContactName) {
    this.emergencyContactName = emergencyContactName;
  }


  public Patient emergencyContactPhone(String emergencyContactPhone) {
    this.emergencyContactPhone = emergencyContactPhone;
    return this;
  }

  /**
   * 
   * @return emergencyContactPhone
   */
  @javax.annotation.Nullable
  public String getEmergencyContactPhone() {
    return emergencyContactPhone;
  }

  public void setEmergencyContactPhone(String emergencyContactPhone) {
    this.emergencyContactPhone = emergencyContactPhone;
  }


  public Patient emergencyContactRelation(String emergencyContactRelation) {
    this.emergencyContactRelation = emergencyContactRelation;
    return this;
  }

  /**
   * 
   * @return emergencyContactRelation
   */
  @javax.annotation.Nullable
  public String getEmergencyContactRelation() {
    return emergencyContactRelation;
  }

  public void setEmergencyContactRelation(String emergencyContactRelation) {
    this.emergencyContactRelation = emergencyContactRelation;
  }


  public Patient employer(String employer) {
    this.employer = employer;
    return this;
  }

  /**
   * 
   * @return employer
   */
  @javax.annotation.Nullable
  public String getEmployer() {
    return employer;
  }

  public void setEmployer(String employer) {
    this.employer = employer;
  }


  public Patient employerAddress(String employerAddress) {
    this.employerAddress = employerAddress;
    return this;
  }

  /**
   * 
   * @return employerAddress
   */
  @javax.annotation.Nullable
  public String getEmployerAddress() {
    return employerAddress;
  }

  public void setEmployerAddress(String employerAddress) {
    this.employerAddress = employerAddress;
  }


  public Patient employerCity(String employerCity) {
    this.employerCity = employerCity;
    return this;
  }

  /**
   * 
   * @return employerCity
   */
  @javax.annotation.Nullable
  public String getEmployerCity() {
    return employerCity;
  }

  public void setEmployerCity(String employerCity) {
    this.employerCity = employerCity;
  }


  public Patient employerState(String employerState) {
    this.employerState = employerState;
    return this;
  }

  /**
   * Two-letter abbreviation
   * @return employerState
   */
  @javax.annotation.Nullable
  public String getEmployerState() {
    return employerState;
  }

  public void setEmployerState(String employerState) {
    this.employerState = employerState;
  }


  public Patient employerZipCode(String employerZipCode) {
    this.employerZipCode = employerZipCode;
    return this;
  }

  /**
   * 
   * @return employerZipCode
   */
  @javax.annotation.Nullable
  public String getEmployerZipCode() {
    return employerZipCode;
  }

  public void setEmployerZipCode(String employerZipCode) {
    this.employerZipCode = employerZipCode;
  }


  public Patient ethnicity(EthnicityEnum ethnicity) {
    this.ethnicity = ethnicity;
    return this;
  }

  /**
   * One of &#x60;\&quot;blank\&quot;&#x60;, &#x60;\&quot;hispanic\&quot;&#x60;, &#x60;\&quot;not_hispanic\&quot;&#x60; or &#x60;\&quot;declined\&quot;&#x60;
   * @return ethnicity
   */
  @javax.annotation.Nullable
  public EthnicityEnum getEthnicity() {
    return ethnicity;
  }

  public void setEthnicity(EthnicityEnum ethnicity) {
    this.ethnicity = ethnicity;
  }


  public Patient firstName(String firstName) {
    this.firstName = firstName;
    return this;
  }

  /**
   * 
   * @return firstName
   */
  @javax.annotation.Nullable
  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }


  public Patient gender(GenderEnum gender) {
    this.gender = gender;
    return this;
  }

  /**
   * One of &#x60;\&quot;Male\&quot;&#x60;, &#x60;\&quot;Female\&quot;&#x60;, or &#x60;\&quot;Other\&quot;&#x60;
   * @return gender
   */
  @javax.annotation.Nonnull
  public GenderEnum getGender() {
    return gender;
  }

  public void setGender(GenderEnum gender) {
    this.gender = gender;
  }


  public Patient homePhone(String homePhone) {
    this.homePhone = homePhone;
    return this;
  }

  /**
   * 
   * @return homePhone
   */
  @javax.annotation.Nullable
  public String getHomePhone() {
    return homePhone;
  }

  public void setHomePhone(String homePhone) {
    this.homePhone = homePhone;
  }


  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public Patient lastName(String lastName) {
    this.lastName = lastName;
    return this;
  }

  /**
   * 
   * @return lastName
   */
  @javax.annotation.Nullable
  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }


  public Patient middleName(String middleName) {
    this.middleName = middleName;
    return this;
  }

  /**
   * 
   * @return middleName
   */
  @javax.annotation.Nullable
  public String getMiddleName() {
    return middleName;
  }

  public void setMiddleName(String middleName) {
    this.middleName = middleName;
  }


  public Patient nickName(String nickName) {
    this.nickName = nickName;
    return this;
  }

  /**
   * Common name for patient, should be used instead of first name if supplied.
   * @return nickName
   */
  @javax.annotation.Nullable
  public String getNickName() {
    return nickName;
  }

  public void setNickName(String nickName) {
    this.nickName = nickName;
  }


  public Patient officePhone(String officePhone) {
    this.officePhone = officePhone;
    return this;
  }

  /**
   * 
   * @return officePhone
   */
  @javax.annotation.Nullable
  public String getOfficePhone() {
    return officePhone;
  }

  public void setOfficePhone(String officePhone) {
    this.officePhone = officePhone;
  }


  public Patient offices(List<Integer> offices) {
    this.offices = offices;
    return this;
  }

  public Patient addOfficesItem(Integer officesItem) {
    if (this.offices == null) {
      this.offices = new ArrayList<>();
    }
    this.offices.add(officesItem);
    return this;
  }

  /**
   * IDs of every office this patient has been to
   * @return offices
   */
  @javax.annotation.Nullable
  public List<Integer> getOffices() {
    return offices;
  }

  public void setOffices(List<Integer> offices) {
    this.offices = offices;
  }


  /**
   * Possible patient flag type that can be attached to the patient
   * @return patientFlags
   */
  @javax.annotation.Nullable
  public List<PatientFlagType1> getPatientFlags() {
    return patientFlags;
  }



  public Patient patientFlagsAttached(List<PatientFlag> patientFlagsAttached) {
    this.patientFlagsAttached = patientFlagsAttached;
    return this;
  }

  public Patient addPatientFlagsAttachedItem(PatientFlag patientFlagsAttachedItem) {
    if (this.patientFlagsAttached == null) {
      this.patientFlagsAttached = new ArrayList<>();
    }
    this.patientFlagsAttached.add(patientFlagsAttachedItem);
    return this;
  }

  /**
   * Patient flags attached to the patient
   * @return patientFlagsAttached
   */
  @javax.annotation.Nullable
  public List<PatientFlag> getPatientFlagsAttached() {
    return patientFlagsAttached;
  }

  public void setPatientFlagsAttached(List<PatientFlag> patientFlagsAttached) {
    this.patientFlagsAttached = patientFlagsAttached;
  }


  public Patient patientPaymentProfile(PatientPaymentProfileEnum patientPaymentProfile) {
    this.patientPaymentProfile = patientPaymentProfile;
    return this;
  }

  /**
   * One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Cash\&quot;&#x60;, &#x60;\&quot;Insurance\&quot;&#x60;, &#x60;\&quot;Insurance Out of Network\&quot;&#x60;, &#x60;\&quot;Auto Accident\&quot;&#x60; or &#x60;\&quot;Worker&#39;s Comp\&quot;&#x60;.&lt;br&gt;**Note:** Patient must already have either &#x60;primary_insurance&#x60; or &#x60;secondary_insurance&#x60; or new &#x60;primary_insurance&#x60; or &#x60;secondary_insurance&#x60; is passed in request if &#x60;Insurance&#x60;, &#x60;Auto Accident&#x60; or &#x60;Worker&#39;s Comp&#x60; payment profiles are chosen.
   * @return patientPaymentProfile
   */
  @javax.annotation.Nullable
  public PatientPaymentProfileEnum getPatientPaymentProfile() {
    return patientPaymentProfile;
  }

  public void setPatientPaymentProfile(PatientPaymentProfileEnum patientPaymentProfile) {
    this.patientPaymentProfile = patientPaymentProfile;
  }


  public Patient patientPhoto(String patientPhoto) {
    this.patientPhoto = patientPhoto;
    return this;
  }

  /**
   * 
   * @return patientPhoto
   */
  @javax.annotation.Nullable
  public String getPatientPhoto() {
    return patientPhoto;
  }

  public void setPatientPhoto(String patientPhoto) {
    this.patientPhoto = patientPhoto;
  }


  public Patient patientPhotoDate(String patientPhotoDate) {
    this.patientPhotoDate = patientPhotoDate;
    return this;
  }

  /**
   * Cannot be passed without &#x60;patient_photo&#x60;
   * @return patientPhotoDate
   */
  @javax.annotation.Nullable
  public String getPatientPhotoDate() {
    return patientPhotoDate;
  }

  public void setPatientPhotoDate(String patientPhotoDate) {
    this.patientPhotoDate = patientPhotoDate;
  }


  public Patient patientStatus(PatientStatusEnum patientStatus) {
    this.patientStatus = patientStatus;
    return this;
  }

  /**
   * One of &#x60;\&quot;A\&quot;&#x60; (active), &#x60;\&quot;I\&quot;&#x60; (inactive), &#x60;\&quot;D\&quot;&#x60; (inactive-deceased)
   * @return patientStatus
   */
  @javax.annotation.Nullable
  public PatientStatusEnum getPatientStatus() {
    return patientStatus;
  }

  public void setPatientStatus(PatientStatusEnum patientStatus) {
    this.patientStatus = patientStatus;
  }


  public Patient preferredLanguage(PreferredLanguageEnum preferredLanguage) {
    this.preferredLanguage = preferredLanguage;
    return this;
  }

  /**
   * Use ISO 639 alpha-3 codes
   * @return preferredLanguage
   */
  @javax.annotation.Nullable
  public PreferredLanguageEnum getPreferredLanguage() {
    return preferredLanguage;
  }

  public void setPreferredLanguage(PreferredLanguageEnum preferredLanguage) {
    this.preferredLanguage = preferredLanguage;
  }


  public Patient primaryCarePhysician(String primaryCarePhysician) {
    this.primaryCarePhysician = primaryCarePhysician;
    return this;
  }

  /**
   * Referring doctor for this patient
   * @return primaryCarePhysician
   */
  @javax.annotation.Nullable
  public String getPrimaryCarePhysician() {
    return primaryCarePhysician;
  }

  public void setPrimaryCarePhysician(String primaryCarePhysician) {
    this.primaryCarePhysician = primaryCarePhysician;
  }


  public Patient primaryInsurance(PrimaryInsurance primaryInsurance) {
    this.primaryInsurance = primaryInsurance;
    return this;
  }

  /**
   * Get primaryInsurance
   * @return primaryInsurance
   */
  @javax.annotation.Nullable
  public PrimaryInsurance getPrimaryInsurance() {
    return primaryInsurance;
  }

  public void setPrimaryInsurance(PrimaryInsurance primaryInsurance) {
    this.primaryInsurance = primaryInsurance;
  }


  public Patient race(RaceEnum race) {
    this.race = race;
    return this;
  }

  /**
   * One of &#x60;\&quot;blank\&quot;&#x60;, &#x60;\&quot;indian\&quot;&#x60;, &#x60;\&quot;asian\&quot;&#x60;, &#x60;\&quot;black\&quot;&#x60;, &#x60;\&quot;hawaiian\&quot;&#x60;, &#x60;\&quot;white\&quot;&#x60; or &#x60;\&quot;declined\&quot;&#x60;
   * @return race
   */
  @javax.annotation.Nullable
  public RaceEnum getRace() {
    return race;
  }

  public void setRace(RaceEnum race) {
    this.race = race;
  }


  public Patient referringDoctor(Patient1 referringDoctor) {
    this.referringDoctor = referringDoctor;
    return this;
  }

  /**
   * Get referringDoctor
   * @return referringDoctor
   */
  @javax.annotation.Nullable
  public Patient1 getReferringDoctor() {
    return referringDoctor;
  }

  public void setReferringDoctor(Patient1 referringDoctor) {
    this.referringDoctor = referringDoctor;
  }


  public Patient referringSource(String referringSource) {
    this.referringSource = referringSource;
    return this;
  }

  /**
   * Referring source.
   * @return referringSource
   */
  @javax.annotation.Nullable
  public String getReferringSource() {
    return referringSource;
  }

  public void setReferringSource(String referringSource) {
    this.referringSource = referringSource;
  }


  public Patient responsiblePartyEmail(String responsiblePartyEmail) {
    this.responsiblePartyEmail = responsiblePartyEmail;
    return this;
  }

  /**
   * 
   * @return responsiblePartyEmail
   */
  @javax.annotation.Nullable
  public String getResponsiblePartyEmail() {
    return responsiblePartyEmail;
  }

  public void setResponsiblePartyEmail(String responsiblePartyEmail) {
    this.responsiblePartyEmail = responsiblePartyEmail;
  }


  public Patient responsiblePartyName(String responsiblePartyName) {
    this.responsiblePartyName = responsiblePartyName;
    return this;
  }

  /**
   * 
   * @return responsiblePartyName
   */
  @javax.annotation.Nullable
  public String getResponsiblePartyName() {
    return responsiblePartyName;
  }

  public void setResponsiblePartyName(String responsiblePartyName) {
    this.responsiblePartyName = responsiblePartyName;
  }


  public Patient responsiblePartyPhone(String responsiblePartyPhone) {
    this.responsiblePartyPhone = responsiblePartyPhone;
    return this;
  }

  /**
   * 
   * @return responsiblePartyPhone
   */
  @javax.annotation.Nullable
  public String getResponsiblePartyPhone() {
    return responsiblePartyPhone;
  }

  public void setResponsiblePartyPhone(String responsiblePartyPhone) {
    this.responsiblePartyPhone = responsiblePartyPhone;
  }


  public Patient responsiblePartyRelation(String responsiblePartyRelation) {
    this.responsiblePartyRelation = responsiblePartyRelation;
    return this;
  }

  /**
   * 
   * @return responsiblePartyRelation
   */
  @javax.annotation.Nullable
  public String getResponsiblePartyRelation() {
    return responsiblePartyRelation;
  }

  public void setResponsiblePartyRelation(String responsiblePartyRelation) {
    this.responsiblePartyRelation = responsiblePartyRelation;
  }


  public Patient secondaryInsurance(SecondaryInsurance secondaryInsurance) {
    this.secondaryInsurance = secondaryInsurance;
    return this;
  }

  /**
   * Get secondaryInsurance
   * @return secondaryInsurance
   */
  @javax.annotation.Nullable
  public SecondaryInsurance getSecondaryInsurance() {
    return secondaryInsurance;
  }

  public void setSecondaryInsurance(SecondaryInsurance secondaryInsurance) {
    this.secondaryInsurance = secondaryInsurance;
  }


  public Patient socialSecurityNumber(String socialSecurityNumber) {
    this.socialSecurityNumber = socialSecurityNumber;
    return this;
  }

  /**
   * 
   * @return socialSecurityNumber
   */
  @javax.annotation.Nullable
  public String getSocialSecurityNumber() {
    return socialSecurityNumber;
  }

  public void setSocialSecurityNumber(String socialSecurityNumber) {
    this.socialSecurityNumber = socialSecurityNumber;
  }


  public Patient state(String state) {
    this.state = state;
    return this;
  }

  /**
   * Two-letter abbreviation
   * @return state
   */
  @javax.annotation.Nullable
  public String getState() {
    return state;
  }

  public void setState(String state) {
    this.state = state;
  }


  public Patient tertiaryInsurance(TertiaryInsurance tertiaryInsurance) {
    this.tertiaryInsurance = tertiaryInsurance;
    return this;
  }

  /**
   * Get tertiaryInsurance
   * @return tertiaryInsurance
   */
  @javax.annotation.Nullable
  public TertiaryInsurance getTertiaryInsurance() {
    return tertiaryInsurance;
  }

  public void setTertiaryInsurance(TertiaryInsurance tertiaryInsurance) {
    this.tertiaryInsurance = tertiaryInsurance;
  }


  /**
   * 
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }



  public Patient workersCompInsurance(WorkerCompInsurance workersCompInsurance) {
    this.workersCompInsurance = workersCompInsurance;
    return this;
  }

  /**
   * Get workersCompInsurance
   * @return workersCompInsurance
   */
  @javax.annotation.Nullable
  public WorkerCompInsurance getWorkersCompInsurance() {
    return workersCompInsurance;
  }

  public void setWorkersCompInsurance(WorkerCompInsurance workersCompInsurance) {
    this.workersCompInsurance = workersCompInsurance;
  }


  public Patient zipCode(String zipCode) {
    this.zipCode = zipCode;
    return this;
  }

  /**
   * 
   * @return zipCode
   */
  @javax.annotation.Nullable
  public String getZipCode() {
    return zipCode;
  }

  public void setZipCode(String zipCode) {
    this.zipCode = zipCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Patient patient = (Patient) o;
    return Objects.equals(this.address, patient.address) &&
        Objects.equals(this.autoAccidentInsurance, patient.autoAccidentInsurance) &&
        Objects.equals(this.cellPhone, patient.cellPhone) &&
        Objects.equals(this.chartId, patient.chartId) &&
        Objects.equals(this.city, patient.city) &&
        Objects.equals(this.copay, patient.copay) &&
        Objects.equals(this.customDemographics, patient.customDemographics) &&
        Objects.equals(this.dateOfBirth, patient.dateOfBirth) &&
        Objects.equals(this.dateOfFirstAppointment, patient.dateOfFirstAppointment) &&
        Objects.equals(this.dateOfLastAppointment, patient.dateOfLastAppointment) &&
        Objects.equals(this.defaultPharmacy, patient.defaultPharmacy) &&
        Objects.equals(this.disableSmsMessages, patient.disableSmsMessages) &&
        Objects.equals(this.doctor, patient.doctor) &&
        Objects.equals(this.email, patient.email) &&
        Objects.equals(this.emergencyContactName, patient.emergencyContactName) &&
        Objects.equals(this.emergencyContactPhone, patient.emergencyContactPhone) &&
        Objects.equals(this.emergencyContactRelation, patient.emergencyContactRelation) &&
        Objects.equals(this.employer, patient.employer) &&
        Objects.equals(this.employerAddress, patient.employerAddress) &&
        Objects.equals(this.employerCity, patient.employerCity) &&
        Objects.equals(this.employerState, patient.employerState) &&
        Objects.equals(this.employerZipCode, patient.employerZipCode) &&
        Objects.equals(this.ethnicity, patient.ethnicity) &&
        Objects.equals(this.firstName, patient.firstName) &&
        Objects.equals(this.gender, patient.gender) &&
        Objects.equals(this.homePhone, patient.homePhone) &&
        Objects.equals(this.id, patient.id) &&
        Objects.equals(this.lastName, patient.lastName) &&
        Objects.equals(this.middleName, patient.middleName) &&
        Objects.equals(this.nickName, patient.nickName) &&
        Objects.equals(this.officePhone, patient.officePhone) &&
        Objects.equals(this.offices, patient.offices) &&
        Objects.equals(this.patientFlags, patient.patientFlags) &&
        Objects.equals(this.patientFlagsAttached, patient.patientFlagsAttached) &&
        Objects.equals(this.patientPaymentProfile, patient.patientPaymentProfile) &&
        Objects.equals(this.patientPhoto, patient.patientPhoto) &&
        Objects.equals(this.patientPhotoDate, patient.patientPhotoDate) &&
        Objects.equals(this.patientStatus, patient.patientStatus) &&
        Objects.equals(this.preferredLanguage, patient.preferredLanguage) &&
        Objects.equals(this.primaryCarePhysician, patient.primaryCarePhysician) &&
        Objects.equals(this.primaryInsurance, patient.primaryInsurance) &&
        Objects.equals(this.race, patient.race) &&
        Objects.equals(this.referringDoctor, patient.referringDoctor) &&
        Objects.equals(this.referringSource, patient.referringSource) &&
        Objects.equals(this.responsiblePartyEmail, patient.responsiblePartyEmail) &&
        Objects.equals(this.responsiblePartyName, patient.responsiblePartyName) &&
        Objects.equals(this.responsiblePartyPhone, patient.responsiblePartyPhone) &&
        Objects.equals(this.responsiblePartyRelation, patient.responsiblePartyRelation) &&
        Objects.equals(this.secondaryInsurance, patient.secondaryInsurance) &&
        Objects.equals(this.socialSecurityNumber, patient.socialSecurityNumber) &&
        Objects.equals(this.state, patient.state) &&
        Objects.equals(this.tertiaryInsurance, patient.tertiaryInsurance) &&
        Objects.equals(this.updatedAt, patient.updatedAt) &&
        Objects.equals(this.workersCompInsurance, patient.workersCompInsurance) &&
        Objects.equals(this.zipCode, patient.zipCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, autoAccidentInsurance, cellPhone, chartId, city, copay, customDemographics, dateOfBirth, dateOfFirstAppointment, dateOfLastAppointment, defaultPharmacy, disableSmsMessages, doctor, email, emergencyContactName, emergencyContactPhone, emergencyContactRelation, employer, employerAddress, employerCity, employerState, employerZipCode, ethnicity, firstName, gender, homePhone, id, lastName, middleName, nickName, officePhone, offices, patientFlags, patientFlagsAttached, patientPaymentProfile, patientPhoto, patientPhotoDate, patientStatus, preferredLanguage, primaryCarePhysician, primaryInsurance, race, referringDoctor, referringSource, responsiblePartyEmail, responsiblePartyName, responsiblePartyPhone, responsiblePartyRelation, secondaryInsurance, socialSecurityNumber, state, tertiaryInsurance, updatedAt, workersCompInsurance, zipCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Patient {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    autoAccidentInsurance: ").append(toIndentedString(autoAccidentInsurance)).append("\n");
    sb.append("    cellPhone: ").append(toIndentedString(cellPhone)).append("\n");
    sb.append("    chartId: ").append(toIndentedString(chartId)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    copay: ").append(toIndentedString(copay)).append("\n");
    sb.append("    customDemographics: ").append(toIndentedString(customDemographics)).append("\n");
    sb.append("    dateOfBirth: ").append(toIndentedString(dateOfBirth)).append("\n");
    sb.append("    dateOfFirstAppointment: ").append(toIndentedString(dateOfFirstAppointment)).append("\n");
    sb.append("    dateOfLastAppointment: ").append(toIndentedString(dateOfLastAppointment)).append("\n");
    sb.append("    defaultPharmacy: ").append(toIndentedString(defaultPharmacy)).append("\n");
    sb.append("    disableSmsMessages: ").append(toIndentedString(disableSmsMessages)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    emergencyContactName: ").append(toIndentedString(emergencyContactName)).append("\n");
    sb.append("    emergencyContactPhone: ").append(toIndentedString(emergencyContactPhone)).append("\n");
    sb.append("    emergencyContactRelation: ").append(toIndentedString(emergencyContactRelation)).append("\n");
    sb.append("    employer: ").append(toIndentedString(employer)).append("\n");
    sb.append("    employerAddress: ").append(toIndentedString(employerAddress)).append("\n");
    sb.append("    employerCity: ").append(toIndentedString(employerCity)).append("\n");
    sb.append("    employerState: ").append(toIndentedString(employerState)).append("\n");
    sb.append("    employerZipCode: ").append(toIndentedString(employerZipCode)).append("\n");
    sb.append("    ethnicity: ").append(toIndentedString(ethnicity)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    gender: ").append(toIndentedString(gender)).append("\n");
    sb.append("    homePhone: ").append(toIndentedString(homePhone)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    middleName: ").append(toIndentedString(middleName)).append("\n");
    sb.append("    nickName: ").append(toIndentedString(nickName)).append("\n");
    sb.append("    officePhone: ").append(toIndentedString(officePhone)).append("\n");
    sb.append("    offices: ").append(toIndentedString(offices)).append("\n");
    sb.append("    patientFlags: ").append(toIndentedString(patientFlags)).append("\n");
    sb.append("    patientFlagsAttached: ").append(toIndentedString(patientFlagsAttached)).append("\n");
    sb.append("    patientPaymentProfile: ").append(toIndentedString(patientPaymentProfile)).append("\n");
    sb.append("    patientPhoto: ").append(toIndentedString(patientPhoto)).append("\n");
    sb.append("    patientPhotoDate: ").append(toIndentedString(patientPhotoDate)).append("\n");
    sb.append("    patientStatus: ").append(toIndentedString(patientStatus)).append("\n");
    sb.append("    preferredLanguage: ").append(toIndentedString(preferredLanguage)).append("\n");
    sb.append("    primaryCarePhysician: ").append(toIndentedString(primaryCarePhysician)).append("\n");
    sb.append("    primaryInsurance: ").append(toIndentedString(primaryInsurance)).append("\n");
    sb.append("    race: ").append(toIndentedString(race)).append("\n");
    sb.append("    referringDoctor: ").append(toIndentedString(referringDoctor)).append("\n");
    sb.append("    referringSource: ").append(toIndentedString(referringSource)).append("\n");
    sb.append("    responsiblePartyEmail: ").append(toIndentedString(responsiblePartyEmail)).append("\n");
    sb.append("    responsiblePartyName: ").append(toIndentedString(responsiblePartyName)).append("\n");
    sb.append("    responsiblePartyPhone: ").append(toIndentedString(responsiblePartyPhone)).append("\n");
    sb.append("    responsiblePartyRelation: ").append(toIndentedString(responsiblePartyRelation)).append("\n");
    sb.append("    secondaryInsurance: ").append(toIndentedString(secondaryInsurance)).append("\n");
    sb.append("    socialSecurityNumber: ").append(toIndentedString(socialSecurityNumber)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    tertiaryInsurance: ").append(toIndentedString(tertiaryInsurance)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    workersCompInsurance: ").append(toIndentedString(workersCompInsurance)).append("\n");
    sb.append("    zipCode: ").append(toIndentedString(zipCode)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("auto_accident_insurance");
    openapiFields.add("cell_phone");
    openapiFields.add("chart_id");
    openapiFields.add("city");
    openapiFields.add("copay");
    openapiFields.add("custom_demographics");
    openapiFields.add("date_of_birth");
    openapiFields.add("date_of_first_appointment");
    openapiFields.add("date_of_last_appointment");
    openapiFields.add("default_pharmacy");
    openapiFields.add("disable_sms_messages");
    openapiFields.add("doctor");
    openapiFields.add("email");
    openapiFields.add("emergency_contact_name");
    openapiFields.add("emergency_contact_phone");
    openapiFields.add("emergency_contact_relation");
    openapiFields.add("employer");
    openapiFields.add("employer_address");
    openapiFields.add("employer_city");
    openapiFields.add("employer_state");
    openapiFields.add("employer_zip_code");
    openapiFields.add("ethnicity");
    openapiFields.add("first_name");
    openapiFields.add("gender");
    openapiFields.add("home_phone");
    openapiFields.add("id");
    openapiFields.add("last_name");
    openapiFields.add("middle_name");
    openapiFields.add("nick_name");
    openapiFields.add("office_phone");
    openapiFields.add("offices");
    openapiFields.add("patient_flags");
    openapiFields.add("patient_flags_attached");
    openapiFields.add("patient_payment_profile");
    openapiFields.add("patient_photo");
    openapiFields.add("patient_photo_date");
    openapiFields.add("patient_status");
    openapiFields.add("preferred_language");
    openapiFields.add("primary_care_physician");
    openapiFields.add("primary_insurance");
    openapiFields.add("race");
    openapiFields.add("referring_doctor");
    openapiFields.add("referring_source");
    openapiFields.add("responsible_party_email");
    openapiFields.add("responsible_party_name");
    openapiFields.add("responsible_party_phone");
    openapiFields.add("responsible_party_relation");
    openapiFields.add("secondary_insurance");
    openapiFields.add("social_security_number");
    openapiFields.add("state");
    openapiFields.add("tertiary_insurance");
    openapiFields.add("updated_at");
    openapiFields.add("workers_comp_insurance");
    openapiFields.add("zip_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("doctor");
    openapiRequiredFields.add("gender");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Patient
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Patient.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Patient is not found in the empty JSON string", Patient.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Patient.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Patient` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Patient.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) && !jsonObj.get("address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      // validate the optional field `auto_accident_insurance`
      if (jsonObj.get("auto_accident_insurance") != null && !jsonObj.get("auto_accident_insurance").isJsonNull()) {
        AutoAccidentInsurance.validateJsonElement(jsonObj.get("auto_accident_insurance"));
      }
      if ((jsonObj.get("cell_phone") != null && !jsonObj.get("cell_phone").isJsonNull()) && !jsonObj.get("cell_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cell_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cell_phone").toString()));
      }
      if ((jsonObj.get("chart_id") != null && !jsonObj.get("chart_id").isJsonNull()) && !jsonObj.get("chart_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `chart_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("chart_id").toString()));
      }
      if ((jsonObj.get("city") != null && !jsonObj.get("city").isJsonNull()) && !jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if ((jsonObj.get("copay") != null && !jsonObj.get("copay").isJsonNull()) && !jsonObj.get("copay").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `copay` to be a primitive type in the JSON string but got `%s`", jsonObj.get("copay").toString()));
      }
      if (jsonObj.get("custom_demographics") != null && !jsonObj.get("custom_demographics").isJsonNull()) {
        JsonArray jsonArraycustomDemographics = jsonObj.getAsJsonArray("custom_demographics");
        if (jsonArraycustomDemographics != null) {
          // ensure the json data is an array
          if (!jsonObj.get("custom_demographics").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `custom_demographics` to be an array in the JSON string but got `%s`", jsonObj.get("custom_demographics").toString()));
          }

          // validate the optional field `custom_demographics` (array)
          for (int i = 0; i < jsonArraycustomDemographics.size(); i++) {
            CustomPatientFieldValue.validateJsonElement(jsonArraycustomDemographics.get(i));
          };
        }
      }
      if ((jsonObj.get("date_of_birth") != null && !jsonObj.get("date_of_birth").isJsonNull()) && !jsonObj.get("date_of_birth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_of_birth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_of_birth").toString()));
      }
      if ((jsonObj.get("date_of_first_appointment") != null && !jsonObj.get("date_of_first_appointment").isJsonNull()) && !jsonObj.get("date_of_first_appointment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_of_first_appointment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_of_first_appointment").toString()));
      }
      if ((jsonObj.get("date_of_last_appointment") != null && !jsonObj.get("date_of_last_appointment").isJsonNull()) && !jsonObj.get("date_of_last_appointment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date_of_last_appointment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date_of_last_appointment").toString()));
      }
      if ((jsonObj.get("default_pharmacy") != null && !jsonObj.get("default_pharmacy").isJsonNull()) && !jsonObj.get("default_pharmacy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `default_pharmacy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("default_pharmacy").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("emergency_contact_name") != null && !jsonObj.get("emergency_contact_name").isJsonNull()) && !jsonObj.get("emergency_contact_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `emergency_contact_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("emergency_contact_name").toString()));
      }
      if ((jsonObj.get("emergency_contact_phone") != null && !jsonObj.get("emergency_contact_phone").isJsonNull()) && !jsonObj.get("emergency_contact_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `emergency_contact_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("emergency_contact_phone").toString()));
      }
      if ((jsonObj.get("emergency_contact_relation") != null && !jsonObj.get("emergency_contact_relation").isJsonNull()) && !jsonObj.get("emergency_contact_relation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `emergency_contact_relation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("emergency_contact_relation").toString()));
      }
      if ((jsonObj.get("employer") != null && !jsonObj.get("employer").isJsonNull()) && !jsonObj.get("employer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employer").toString()));
      }
      if ((jsonObj.get("employer_address") != null && !jsonObj.get("employer_address").isJsonNull()) && !jsonObj.get("employer_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employer_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employer_address").toString()));
      }
      if ((jsonObj.get("employer_city") != null && !jsonObj.get("employer_city").isJsonNull()) && !jsonObj.get("employer_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employer_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employer_city").toString()));
      }
      if ((jsonObj.get("employer_state") != null && !jsonObj.get("employer_state").isJsonNull()) && !jsonObj.get("employer_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employer_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employer_state").toString()));
      }
      if ((jsonObj.get("employer_zip_code") != null && !jsonObj.get("employer_zip_code").isJsonNull()) && !jsonObj.get("employer_zip_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `employer_zip_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("employer_zip_code").toString()));
      }
      if ((jsonObj.get("ethnicity") != null && !jsonObj.get("ethnicity").isJsonNull()) && !jsonObj.get("ethnicity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ethnicity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ethnicity").toString()));
      }
      // validate the optional field `ethnicity`
      if (jsonObj.get("ethnicity") != null && !jsonObj.get("ethnicity").isJsonNull()) {
        EthnicityEnum.validateJsonElement(jsonObj.get("ethnicity"));
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      if (!jsonObj.get("gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("gender").toString()));
      }
      // validate the required field `gender`
      GenderEnum.validateJsonElement(jsonObj.get("gender"));
      if ((jsonObj.get("home_phone") != null && !jsonObj.get("home_phone").isJsonNull()) && !jsonObj.get("home_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `home_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("home_phone").toString()));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("middle_name") != null && !jsonObj.get("middle_name").isJsonNull()) && !jsonObj.get("middle_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `middle_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("middle_name").toString()));
      }
      if ((jsonObj.get("nick_name") != null && !jsonObj.get("nick_name").isJsonNull()) && !jsonObj.get("nick_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nick_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nick_name").toString()));
      }
      if ((jsonObj.get("office_phone") != null && !jsonObj.get("office_phone").isJsonNull()) && !jsonObj.get("office_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `office_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("office_phone").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("offices") != null && !jsonObj.get("offices").isJsonNull() && !jsonObj.get("offices").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `offices` to be an array in the JSON string but got `%s`", jsonObj.get("offices").toString()));
      }
      if (jsonObj.get("patient_flags") != null && !jsonObj.get("patient_flags").isJsonNull()) {
        JsonArray jsonArraypatientFlags = jsonObj.getAsJsonArray("patient_flags");
        if (jsonArraypatientFlags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("patient_flags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `patient_flags` to be an array in the JSON string but got `%s`", jsonObj.get("patient_flags").toString()));
          }

          // validate the optional field `patient_flags` (array)
          for (int i = 0; i < jsonArraypatientFlags.size(); i++) {
            PatientFlagType1.validateJsonElement(jsonArraypatientFlags.get(i));
          };
        }
      }
      if (jsonObj.get("patient_flags_attached") != null && !jsonObj.get("patient_flags_attached").isJsonNull()) {
        JsonArray jsonArraypatientFlagsAttached = jsonObj.getAsJsonArray("patient_flags_attached");
        if (jsonArraypatientFlagsAttached != null) {
          // ensure the json data is an array
          if (!jsonObj.get("patient_flags_attached").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `patient_flags_attached` to be an array in the JSON string but got `%s`", jsonObj.get("patient_flags_attached").toString()));
          }

          // validate the optional field `patient_flags_attached` (array)
          for (int i = 0; i < jsonArraypatientFlagsAttached.size(); i++) {
            PatientFlag.validateJsonElement(jsonArraypatientFlagsAttached.get(i));
          };
        }
      }
      if ((jsonObj.get("patient_payment_profile") != null && !jsonObj.get("patient_payment_profile").isJsonNull()) && !jsonObj.get("patient_payment_profile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patient_payment_profile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patient_payment_profile").toString()));
      }
      // validate the optional field `patient_payment_profile`
      if (jsonObj.get("patient_payment_profile") != null && !jsonObj.get("patient_payment_profile").isJsonNull()) {
        PatientPaymentProfileEnum.validateJsonElement(jsonObj.get("patient_payment_profile"));
      }
      if ((jsonObj.get("patient_photo") != null && !jsonObj.get("patient_photo").isJsonNull()) && !jsonObj.get("patient_photo").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patient_photo` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patient_photo").toString()));
      }
      if ((jsonObj.get("patient_photo_date") != null && !jsonObj.get("patient_photo_date").isJsonNull()) && !jsonObj.get("patient_photo_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patient_photo_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patient_photo_date").toString()));
      }
      if ((jsonObj.get("patient_status") != null && !jsonObj.get("patient_status").isJsonNull()) && !jsonObj.get("patient_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patient_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patient_status").toString()));
      }
      // validate the optional field `patient_status`
      if (jsonObj.get("patient_status") != null && !jsonObj.get("patient_status").isJsonNull()) {
        PatientStatusEnum.validateJsonElement(jsonObj.get("patient_status"));
      }
      if ((jsonObj.get("preferred_language") != null && !jsonObj.get("preferred_language").isJsonNull()) && !jsonObj.get("preferred_language").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `preferred_language` to be a primitive type in the JSON string but got `%s`", jsonObj.get("preferred_language").toString()));
      }
      // validate the optional field `preferred_language`
      if (jsonObj.get("preferred_language") != null && !jsonObj.get("preferred_language").isJsonNull()) {
        PreferredLanguageEnum.validateJsonElement(jsonObj.get("preferred_language"));
      }
      if ((jsonObj.get("primary_care_physician") != null && !jsonObj.get("primary_care_physician").isJsonNull()) && !jsonObj.get("primary_care_physician").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `primary_care_physician` to be a primitive type in the JSON string but got `%s`", jsonObj.get("primary_care_physician").toString()));
      }
      // validate the optional field `primary_insurance`
      if (jsonObj.get("primary_insurance") != null && !jsonObj.get("primary_insurance").isJsonNull()) {
        PrimaryInsurance.validateJsonElement(jsonObj.get("primary_insurance"));
      }
      if ((jsonObj.get("race") != null && !jsonObj.get("race").isJsonNull()) && !jsonObj.get("race").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `race` to be a primitive type in the JSON string but got `%s`", jsonObj.get("race").toString()));
      }
      // validate the optional field `race`
      if (jsonObj.get("race") != null && !jsonObj.get("race").isJsonNull()) {
        RaceEnum.validateJsonElement(jsonObj.get("race"));
      }
      // validate the optional field `referring_doctor`
      if (jsonObj.get("referring_doctor") != null && !jsonObj.get("referring_doctor").isJsonNull()) {
        Patient1.validateJsonElement(jsonObj.get("referring_doctor"));
      }
      if ((jsonObj.get("referring_source") != null && !jsonObj.get("referring_source").isJsonNull()) && !jsonObj.get("referring_source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referring_source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referring_source").toString()));
      }
      if ((jsonObj.get("responsible_party_email") != null && !jsonObj.get("responsible_party_email").isJsonNull()) && !jsonObj.get("responsible_party_email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `responsible_party_email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("responsible_party_email").toString()));
      }
      if ((jsonObj.get("responsible_party_name") != null && !jsonObj.get("responsible_party_name").isJsonNull()) && !jsonObj.get("responsible_party_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `responsible_party_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("responsible_party_name").toString()));
      }
      if ((jsonObj.get("responsible_party_phone") != null && !jsonObj.get("responsible_party_phone").isJsonNull()) && !jsonObj.get("responsible_party_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `responsible_party_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("responsible_party_phone").toString()));
      }
      if ((jsonObj.get("responsible_party_relation") != null && !jsonObj.get("responsible_party_relation").isJsonNull()) && !jsonObj.get("responsible_party_relation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `responsible_party_relation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("responsible_party_relation").toString()));
      }
      // validate the optional field `secondary_insurance`
      if (jsonObj.get("secondary_insurance") != null && !jsonObj.get("secondary_insurance").isJsonNull()) {
        SecondaryInsurance.validateJsonElement(jsonObj.get("secondary_insurance"));
      }
      if ((jsonObj.get("social_security_number") != null && !jsonObj.get("social_security_number").isJsonNull()) && !jsonObj.get("social_security_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `social_security_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("social_security_number").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      // validate the optional field `tertiary_insurance`
      if (jsonObj.get("tertiary_insurance") != null && !jsonObj.get("tertiary_insurance").isJsonNull()) {
        TertiaryInsurance.validateJsonElement(jsonObj.get("tertiary_insurance"));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
      // validate the optional field `workers_comp_insurance`
      if (jsonObj.get("workers_comp_insurance") != null && !jsonObj.get("workers_comp_insurance").isJsonNull()) {
        WorkerCompInsurance.validateJsonElement(jsonObj.get("workers_comp_insurance"));
      }
      if ((jsonObj.get("zip_code") != null && !jsonObj.get("zip_code").isJsonNull()) && !jsonObj.get("zip_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `zip_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("zip_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Patient.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Patient' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Patient> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Patient.class));

       return (TypeAdapter<T>) new TypeAdapter<Patient>() {
           @Override
           public void write(JsonWriter out, Patient value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Patient read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Patient given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Patient
   * @throws IOException if the JSON string is invalid with respect to Patient
   */
  public static Patient fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Patient.class);
  }

  /**
   * Convert an instance of Patient to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

