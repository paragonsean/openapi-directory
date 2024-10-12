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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.VaccineDose;

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
 * PatientVaccineRecord
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientVaccineRecord {
  public static final String SERIALIZED_NAME_ADMINISTERED_AT = "administered_at";
  @SerializedName(SERIALIZED_NAME_ADMINISTERED_AT)
  private Integer administeredAt;

  public static final String SERIALIZED_NAME_ADMINISTERED_BY = "administered_by";
  @SerializedName(SERIALIZED_NAME_ADMINISTERED_BY)
  private String administeredBy;

  public static final String SERIALIZED_NAME_ADMINISTRATION_START = "administration_start";
  @SerializedName(SERIALIZED_NAME_ADMINISTRATION_START)
  private String administrationStart;

  public static final String SERIALIZED_NAME_AMOUNT = "amount";
  @SerializedName(SERIALIZED_NAME_AMOUNT)
  private BigDecimal amount;

  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  /**
   * Vaccination status, can be &#x60;CP&#x60;(Complete), &#x60;RE&#x60;(Refused), &#x60;NA&#x60;(Not administered), &#x60;PA&#x60;(Partially administered)
   */
  @JsonAdapter(CompletionStatusEnum.Adapter.class)
  public enum CompletionStatusEnum {
    CP("CP"),
    
    RE("RE"),
    
    NA("NA"),
    
    PA("PA");

    private String value;

    CompletionStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CompletionStatusEnum fromValue(String value) {
      for (CompletionStatusEnum b : CompletionStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CompletionStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CompletionStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CompletionStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CompletionStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CompletionStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_COMPLETION_STATUS = "completion_status";
  @SerializedName(SERIALIZED_NAME_COMPLETION_STATUS)
  private CompletionStatusEnum completionStatus;

  public static final String SERIALIZED_NAME_CONSENT_FORM = "consent_form";
  @SerializedName(SERIALIZED_NAME_CONSENT_FORM)
  private Integer consentForm;

  public static final String SERIALIZED_NAME_CPT_CODE = "cpt_code";
  @SerializedName(SERIALIZED_NAME_CPT_CODE)
  private String cptCode;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_CVX_CODE = "cvx_code";
  @SerializedName(SERIALIZED_NAME_CVX_CODE)
  private String cvxCode;

  public static final String SERIALIZED_NAME_DOSES = "doses";
  @SerializedName(SERIALIZED_NAME_DOSES)
  private List<VaccineDose> doses = new ArrayList<>();

  public static final String SERIALIZED_NAME_ENTERED_BY = "entered_by";
  @SerializedName(SERIALIZED_NAME_ENTERED_BY)
  private String enteredBy;

  /**
   * The funding program that should pay for a given immunization
   */
  @JsonAdapter(FundingEligibilityEnum.Adapter.class)
  public enum FundingEligibilityEnum {
    V01("V01"),
    
    V02("V02"),
    
    V03("V03"),
    
    V04("V04"),
    
    V05("V05"),
    
    V07("V07");

    private String value;

    FundingEligibilityEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static FundingEligibilityEnum fromValue(String value) {
      for (FundingEligibilityEnum b : FundingEligibilityEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<FundingEligibilityEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final FundingEligibilityEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public FundingEligibilityEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return FundingEligibilityEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      FundingEligibilityEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_FUNDING_ELIGIBILITY = "funding_eligibility";
  @SerializedName(SERIALIZED_NAME_FUNDING_ELIGIBILITY)
  private FundingEligibilityEnum fundingEligibility;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NEXT_DOSE_DATE = "next_dose_date";
  @SerializedName(SERIALIZED_NAME_NEXT_DOSE_DATE)
  private String nextDoseDate;

  /**
   * 
   */
  @JsonAdapter(ObservedImmunityEnum.Adapter.class)
  public enum ObservedImmunityEnum {
    _398102009("398102009"),
    
    _409498004("409498004"),
    
    _397428000("397428000"),
    
    _18624000("18624000"),
    
    _91428005("91428005"),
    
    _271511000("271511000"),
    
    _240532009("240532009"),
    
    _6142004("6142004"),
    
    _52947006("52947006"),
    
    _14189004("14189004"),
    
    _23511006("23511006"),
    
    _36989005("36989005"),
    
    _27836007("27836007"),
    
    _16814004("16814004"),
    
    _14168008("14168008"),
    
    _36653000("36653000"),
    
    _76902006("76902006"),
    
    _66071002("66071002"),
    
    _4834000("4834000"),
    
    _111852003("111852003"),
    
    _38907003("38907003"),
    
    _40468003("40468003"),
    
    _16541001("16541001");

    private String value;

    ObservedImmunityEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ObservedImmunityEnum fromValue(String value) {
      for (ObservedImmunityEnum b : ObservedImmunityEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ObservedImmunityEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ObservedImmunityEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ObservedImmunityEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ObservedImmunityEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ObservedImmunityEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_OBSERVED_IMMUNITY = "observed_immunity";
  @SerializedName(SERIALIZED_NAME_OBSERVED_IMMUNITY)
  private ObservedImmunityEnum observedImmunity;

  public static final String SERIALIZED_NAME_ORDERING_DOCTOR = "ordering_doctor";
  @SerializedName(SERIALIZED_NAME_ORDERING_DOCTOR)
  private Integer orderingDoctor;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private Integer patient;

  /**
   * 
   */
  @JsonAdapter(RecordSourceEnum.Adapter.class)
  public enum RecordSourceEnum {
    _00("00"),
    
    _01("01"),
    
    _02("02"),
    
    _03("03"),
    
    _04("04"),
    
    _05("05"),
    
    _06("06"),
    
    _07("07"),
    
    _08("08");

    private String value;

    RecordSourceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static RecordSourceEnum fromValue(String value) {
      for (RecordSourceEnum b : RecordSourceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<RecordSourceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final RecordSourceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public RecordSourceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return RecordSourceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      RecordSourceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_RECORD_SOURCE = "record_source";
  @SerializedName(SERIALIZED_NAME_RECORD_SOURCE)
  private RecordSourceEnum recordSource;

  public static final String SERIALIZED_NAME_ROUTE = "route";
  @SerializedName(SERIALIZED_NAME_ROUTE)
  private String route;

  public static final String SERIALIZED_NAME_SITE = "site";
  @SerializedName(SERIALIZED_NAME_SITE)
  private String site;

  public static final String SERIALIZED_NAME_UNITS = "units";
  @SerializedName(SERIALIZED_NAME_UNITS)
  private String units;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public static final String SERIALIZED_NAME_VACCINE_INVENTORY = "vaccine_inventory";
  @SerializedName(SERIALIZED_NAME_VACCINE_INVENTORY)
  private Integer vaccineInventory;

  public static final String SERIALIZED_NAME_VIS = "vis";
  @SerializedName(SERIALIZED_NAME_VIS)
  private String vis;

  public PatientVaccineRecord() {
  }

  public PatientVaccineRecord(
     String createdAt, 
     String enteredBy, 
     Integer id, 
     String updatedAt, 
     String vis
  ) {
    this();
    this.createdAt = createdAt;
    this.enteredBy = enteredBy;
    this.id = id;
    this.updatedAt = updatedAt;
    this.vis = vis;
  }

  public PatientVaccineRecord administeredAt(Integer administeredAt) {
    this.administeredAt = administeredAt;
    return this;
  }

  /**
   * ID of &#x60;/api/offices&#x60; where the administration happened
   * @return administeredAt
   */
  @javax.annotation.Nullable
  public Integer getAdministeredAt() {
    return administeredAt;
  }

  public void setAdministeredAt(Integer administeredAt) {
    this.administeredAt = administeredAt;
  }


  public PatientVaccineRecord administeredBy(String administeredBy) {
    this.administeredBy = administeredBy;
    return this;
  }

  /**
   * ID of &#x60;/api/users&#x60; who performs the administration
   * @return administeredBy
   */
  @javax.annotation.Nullable
  public String getAdministeredBy() {
    return administeredBy;
  }

  public void setAdministeredBy(String administeredBy) {
    this.administeredBy = administeredBy;
  }


  public PatientVaccineRecord administrationStart(String administrationStart) {
    this.administrationStart = administrationStart;
    return this;
  }

  /**
   * Datetime when the administration starts
   * @return administrationStart
   */
  @javax.annotation.Nullable
  public String getAdministrationStart() {
    return administrationStart;
  }

  public void setAdministrationStart(String administrationStart) {
    this.administrationStart = administrationStart;
  }


  public PatientVaccineRecord amount(BigDecimal amount) {
    this.amount = amount;
    return this;
  }

  /**
   * Amount of vaccine administered
   * @return amount
   */
  @javax.annotation.Nullable
  public BigDecimal getAmount() {
    return amount;
  }

  public void setAmount(BigDecimal amount) {
    this.amount = amount;
  }


  public PatientVaccineRecord comments(String comments) {
    this.comments = comments;
    return this;
  }

  /**
   * 
   * @return comments
   */
  @javax.annotation.Nullable
  public String getComments() {
    return comments;
  }

  public void setComments(String comments) {
    this.comments = comments;
  }


  public PatientVaccineRecord completionStatus(CompletionStatusEnum completionStatus) {
    this.completionStatus = completionStatus;
    return this;
  }

  /**
   * Vaccination status, can be &#x60;CP&#x60;(Complete), &#x60;RE&#x60;(Refused), &#x60;NA&#x60;(Not administered), &#x60;PA&#x60;(Partially administered)
   * @return completionStatus
   */
  @javax.annotation.Nullable
  public CompletionStatusEnum getCompletionStatus() {
    return completionStatus;
  }

  public void setCompletionStatus(CompletionStatusEnum completionStatus) {
    this.completionStatus = completionStatus;
  }


  public PatientVaccineRecord consentForm(Integer consentForm) {
    this.consentForm = consentForm;
    return this;
  }

  /**
   * Consent form related with vaccine record
   * @return consentForm
   */
  @javax.annotation.Nullable
  public Integer getConsentForm() {
    return consentForm;
  }

  public void setConsentForm(Integer consentForm) {
    this.consentForm = consentForm;
  }


  public PatientVaccineRecord cptCode(String cptCode) {
    this.cptCode = cptCode;
    return this;
  }

  /**
   * Vaccine cpt code
   * @return cptCode
   */
  @javax.annotation.Nullable
  public String getCptCode() {
    return cptCode;
  }

  public void setCptCode(String cptCode) {
    this.cptCode = cptCode;
  }


  /**
   * 
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }



  public PatientVaccineRecord cvxCode(String cvxCode) {
    this.cvxCode = cvxCode;
    return this;
  }

  /**
   * Vaccine cvx code
   * @return cvxCode
   */
  @javax.annotation.Nonnull
  public String getCvxCode() {
    return cvxCode;
  }

  public void setCvxCode(String cvxCode) {
    this.cvxCode = cvxCode;
  }


  public PatientVaccineRecord doses(List<VaccineDose> doses) {
    this.doses = doses;
    return this;
  }

  public PatientVaccineRecord addDosesItem(VaccineDose dosesItem) {
    if (this.doses == null) {
      this.doses = new ArrayList<>();
    }
    this.doses.add(dosesItem);
    return this;
  }

  /**
   * Vaccine dose IDs received in consent form signed hook
   * @return doses
   */
  @javax.annotation.Nullable
  public List<VaccineDose> getDoses() {
    return doses;
  }

  public void setDoses(List<VaccineDose> doses) {
    this.doses = doses;
  }


  /**
   * ID of user who created the record
   * @return enteredBy
   */
  @javax.annotation.Nullable
  public String getEnteredBy() {
    return enteredBy;
  }



  public PatientVaccineRecord fundingEligibility(FundingEligibilityEnum fundingEligibility) {
    this.fundingEligibility = fundingEligibility;
    return this;
  }

  /**
   * The funding program that should pay for a given immunization
   * @return fundingEligibility
   */
  @javax.annotation.Nullable
  public FundingEligibilityEnum getFundingEligibility() {
    return fundingEligibility;
  }

  public void setFundingEligibility(FundingEligibilityEnum fundingEligibility) {
    this.fundingEligibility = fundingEligibility;
  }


  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public PatientVaccineRecord name(String name) {
    this.name = name;
    return this;
  }

  /**
   * 
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PatientVaccineRecord nextDoseDate(String nextDoseDate) {
    this.nextDoseDate = nextDoseDate;
    return this;
  }

  /**
   * Date for next dose of vaccine
   * @return nextDoseDate
   */
  @javax.annotation.Nullable
  public String getNextDoseDate() {
    return nextDoseDate;
  }

  public void setNextDoseDate(String nextDoseDate) {
    this.nextDoseDate = nextDoseDate;
  }


  public PatientVaccineRecord observedImmunity(ObservedImmunityEnum observedImmunity) {
    this.observedImmunity = observedImmunity;
    return this;
  }

  /**
   * 
   * @return observedImmunity
   */
  @javax.annotation.Nullable
  public ObservedImmunityEnum getObservedImmunity() {
    return observedImmunity;
  }

  public void setObservedImmunity(ObservedImmunityEnum observedImmunity) {
    this.observedImmunity = observedImmunity;
  }


  public PatientVaccineRecord orderingDoctor(Integer orderingDoctor) {
    this.orderingDoctor = orderingDoctor;
    return this;
  }

  /**
   * 
   * @return orderingDoctor
   */
  @javax.annotation.Nullable
  public Integer getOrderingDoctor() {
    return orderingDoctor;
  }

  public void setOrderingDoctor(Integer orderingDoctor) {
    this.orderingDoctor = orderingDoctor;
  }


  public PatientVaccineRecord patient(Integer patient) {
    this.patient = patient;
    return this;
  }

  /**
   * 
   * @return patient
   */
  @javax.annotation.Nonnull
  public Integer getPatient() {
    return patient;
  }

  public void setPatient(Integer patient) {
    this.patient = patient;
  }


  public PatientVaccineRecord recordSource(RecordSourceEnum recordSource) {
    this.recordSource = recordSource;
    return this;
  }

  /**
   * 
   * @return recordSource
   */
  @javax.annotation.Nullable
  public RecordSourceEnum getRecordSource() {
    return recordSource;
  }

  public void setRecordSource(RecordSourceEnum recordSource) {
    this.recordSource = recordSource;
  }


  public PatientVaccineRecord route(String route) {
    this.route = route;
    return this;
  }

  /**
   * 
   * @return route
   */
  @javax.annotation.Nullable
  public String getRoute() {
    return route;
  }

  public void setRoute(String route) {
    this.route = route;
  }


  public PatientVaccineRecord site(String site) {
    this.site = site;
    return this;
  }

  /**
   * 
   * @return site
   */
  @javax.annotation.Nullable
  public String getSite() {
    return site;
  }

  public void setSite(String site) {
    this.site = site;
  }


  public PatientVaccineRecord units(String units) {
    this.units = units;
    return this;
  }

  /**
   * 
   * @return units
   */
  @javax.annotation.Nullable
  public String getUnits() {
    return units;
  }

  public void setUnits(String units) {
    this.units = units;
  }


  /**
   * 
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }



  public PatientVaccineRecord vaccineInventory(Integer vaccineInventory) {
    this.vaccineInventory = vaccineInventory;
    return this;
  }

  /**
   * ID of &#x60;/api/vaccine_inventories&#x60; the vaccine is from
   * @return vaccineInventory
   */
  @javax.annotation.Nullable
  public Integer getVaccineInventory() {
    return vaccineInventory;
  }

  public void setVaccineInventory(Integer vaccineInventory) {
    this.vaccineInventory = vaccineInventory;
  }


  /**
   * Related vaccine information statement
   * @return vis
   */
  @javax.annotation.Nullable
  public String getVis() {
    return vis;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientVaccineRecord patientVaccineRecord = (PatientVaccineRecord) o;
    return Objects.equals(this.administeredAt, patientVaccineRecord.administeredAt) &&
        Objects.equals(this.administeredBy, patientVaccineRecord.administeredBy) &&
        Objects.equals(this.administrationStart, patientVaccineRecord.administrationStart) &&
        Objects.equals(this.amount, patientVaccineRecord.amount) &&
        Objects.equals(this.comments, patientVaccineRecord.comments) &&
        Objects.equals(this.completionStatus, patientVaccineRecord.completionStatus) &&
        Objects.equals(this.consentForm, patientVaccineRecord.consentForm) &&
        Objects.equals(this.cptCode, patientVaccineRecord.cptCode) &&
        Objects.equals(this.createdAt, patientVaccineRecord.createdAt) &&
        Objects.equals(this.cvxCode, patientVaccineRecord.cvxCode) &&
        Objects.equals(this.doses, patientVaccineRecord.doses) &&
        Objects.equals(this.enteredBy, patientVaccineRecord.enteredBy) &&
        Objects.equals(this.fundingEligibility, patientVaccineRecord.fundingEligibility) &&
        Objects.equals(this.id, patientVaccineRecord.id) &&
        Objects.equals(this.name, patientVaccineRecord.name) &&
        Objects.equals(this.nextDoseDate, patientVaccineRecord.nextDoseDate) &&
        Objects.equals(this.observedImmunity, patientVaccineRecord.observedImmunity) &&
        Objects.equals(this.orderingDoctor, patientVaccineRecord.orderingDoctor) &&
        Objects.equals(this.patient, patientVaccineRecord.patient) &&
        Objects.equals(this.recordSource, patientVaccineRecord.recordSource) &&
        Objects.equals(this.route, patientVaccineRecord.route) &&
        Objects.equals(this.site, patientVaccineRecord.site) &&
        Objects.equals(this.units, patientVaccineRecord.units) &&
        Objects.equals(this.updatedAt, patientVaccineRecord.updatedAt) &&
        Objects.equals(this.vaccineInventory, patientVaccineRecord.vaccineInventory) &&
        Objects.equals(this.vis, patientVaccineRecord.vis);
  }

  @Override
  public int hashCode() {
    return Objects.hash(administeredAt, administeredBy, administrationStart, amount, comments, completionStatus, consentForm, cptCode, createdAt, cvxCode, doses, enteredBy, fundingEligibility, id, name, nextDoseDate, observedImmunity, orderingDoctor, patient, recordSource, route, site, units, updatedAt, vaccineInventory, vis);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientVaccineRecord {\n");
    sb.append("    administeredAt: ").append(toIndentedString(administeredAt)).append("\n");
    sb.append("    administeredBy: ").append(toIndentedString(administeredBy)).append("\n");
    sb.append("    administrationStart: ").append(toIndentedString(administrationStart)).append("\n");
    sb.append("    amount: ").append(toIndentedString(amount)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    completionStatus: ").append(toIndentedString(completionStatus)).append("\n");
    sb.append("    consentForm: ").append(toIndentedString(consentForm)).append("\n");
    sb.append("    cptCode: ").append(toIndentedString(cptCode)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    cvxCode: ").append(toIndentedString(cvxCode)).append("\n");
    sb.append("    doses: ").append(toIndentedString(doses)).append("\n");
    sb.append("    enteredBy: ").append(toIndentedString(enteredBy)).append("\n");
    sb.append("    fundingEligibility: ").append(toIndentedString(fundingEligibility)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    nextDoseDate: ").append(toIndentedString(nextDoseDate)).append("\n");
    sb.append("    observedImmunity: ").append(toIndentedString(observedImmunity)).append("\n");
    sb.append("    orderingDoctor: ").append(toIndentedString(orderingDoctor)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    recordSource: ").append(toIndentedString(recordSource)).append("\n");
    sb.append("    route: ").append(toIndentedString(route)).append("\n");
    sb.append("    site: ").append(toIndentedString(site)).append("\n");
    sb.append("    units: ").append(toIndentedString(units)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    vaccineInventory: ").append(toIndentedString(vaccineInventory)).append("\n");
    sb.append("    vis: ").append(toIndentedString(vis)).append("\n");
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
    openapiFields.add("administered_at");
    openapiFields.add("administered_by");
    openapiFields.add("administration_start");
    openapiFields.add("amount");
    openapiFields.add("comments");
    openapiFields.add("completion_status");
    openapiFields.add("consent_form");
    openapiFields.add("cpt_code");
    openapiFields.add("created_at");
    openapiFields.add("cvx_code");
    openapiFields.add("doses");
    openapiFields.add("entered_by");
    openapiFields.add("funding_eligibility");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("next_dose_date");
    openapiFields.add("observed_immunity");
    openapiFields.add("ordering_doctor");
    openapiFields.add("patient");
    openapiFields.add("record_source");
    openapiFields.add("route");
    openapiFields.add("site");
    openapiFields.add("units");
    openapiFields.add("updated_at");
    openapiFields.add("vaccine_inventory");
    openapiFields.add("vis");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("cvx_code");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("patient");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientVaccineRecord
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientVaccineRecord.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientVaccineRecord is not found in the empty JSON string", PatientVaccineRecord.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientVaccineRecord.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientVaccineRecord` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientVaccineRecord.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("administered_by") != null && !jsonObj.get("administered_by").isJsonNull()) && !jsonObj.get("administered_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `administered_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("administered_by").toString()));
      }
      if ((jsonObj.get("administration_start") != null && !jsonObj.get("administration_start").isJsonNull()) && !jsonObj.get("administration_start").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `administration_start` to be a primitive type in the JSON string but got `%s`", jsonObj.get("administration_start").toString()));
      }
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      if ((jsonObj.get("completion_status") != null && !jsonObj.get("completion_status").isJsonNull()) && !jsonObj.get("completion_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `completion_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("completion_status").toString()));
      }
      // validate the optional field `completion_status`
      if (jsonObj.get("completion_status") != null && !jsonObj.get("completion_status").isJsonNull()) {
        CompletionStatusEnum.validateJsonElement(jsonObj.get("completion_status"));
      }
      if ((jsonObj.get("cpt_code") != null && !jsonObj.get("cpt_code").isJsonNull()) && !jsonObj.get("cpt_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cpt_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cpt_code").toString()));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if (!jsonObj.get("cvx_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cvx_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cvx_code").toString()));
      }
      if (jsonObj.get("doses") != null && !jsonObj.get("doses").isJsonNull()) {
        JsonArray jsonArraydoses = jsonObj.getAsJsonArray("doses");
        if (jsonArraydoses != null) {
          // ensure the json data is an array
          if (!jsonObj.get("doses").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `doses` to be an array in the JSON string but got `%s`", jsonObj.get("doses").toString()));
          }

          // validate the optional field `doses` (array)
          for (int i = 0; i < jsonArraydoses.size(); i++) {
            VaccineDose.validateJsonElement(jsonArraydoses.get(i));
          };
        }
      }
      if ((jsonObj.get("entered_by") != null && !jsonObj.get("entered_by").isJsonNull()) && !jsonObj.get("entered_by").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `entered_by` to be a primitive type in the JSON string but got `%s`", jsonObj.get("entered_by").toString()));
      }
      if ((jsonObj.get("funding_eligibility") != null && !jsonObj.get("funding_eligibility").isJsonNull()) && !jsonObj.get("funding_eligibility").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `funding_eligibility` to be a primitive type in the JSON string but got `%s`", jsonObj.get("funding_eligibility").toString()));
      }
      // validate the optional field `funding_eligibility`
      if (jsonObj.get("funding_eligibility") != null && !jsonObj.get("funding_eligibility").isJsonNull()) {
        FundingEligibilityEnum.validateJsonElement(jsonObj.get("funding_eligibility"));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("next_dose_date") != null && !jsonObj.get("next_dose_date").isJsonNull()) && !jsonObj.get("next_dose_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `next_dose_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("next_dose_date").toString()));
      }
      if ((jsonObj.get("observed_immunity") != null && !jsonObj.get("observed_immunity").isJsonNull()) && !jsonObj.get("observed_immunity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `observed_immunity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("observed_immunity").toString()));
      }
      // validate the optional field `observed_immunity`
      if (jsonObj.get("observed_immunity") != null && !jsonObj.get("observed_immunity").isJsonNull()) {
        ObservedImmunityEnum.validateJsonElement(jsonObj.get("observed_immunity"));
      }
      if ((jsonObj.get("record_source") != null && !jsonObj.get("record_source").isJsonNull()) && !jsonObj.get("record_source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `record_source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("record_source").toString()));
      }
      // validate the optional field `record_source`
      if (jsonObj.get("record_source") != null && !jsonObj.get("record_source").isJsonNull()) {
        RecordSourceEnum.validateJsonElement(jsonObj.get("record_source"));
      }
      if ((jsonObj.get("route") != null && !jsonObj.get("route").isJsonNull()) && !jsonObj.get("route").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `route` to be a primitive type in the JSON string but got `%s`", jsonObj.get("route").toString()));
      }
      if ((jsonObj.get("site") != null && !jsonObj.get("site").isJsonNull()) && !jsonObj.get("site").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `site` to be a primitive type in the JSON string but got `%s`", jsonObj.get("site").toString()));
      }
      if ((jsonObj.get("units") != null && !jsonObj.get("units").isJsonNull()) && !jsonObj.get("units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("units").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
      if ((jsonObj.get("vis") != null && !jsonObj.get("vis").isJsonNull()) && !jsonObj.get("vis").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `vis` to be a primitive type in the JSON string but got `%s`", jsonObj.get("vis").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientVaccineRecord.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientVaccineRecord' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientVaccineRecord> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientVaccineRecord.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientVaccineRecord>() {
           @Override
           public void write(JsonWriter out, PatientVaccineRecord value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientVaccineRecord read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientVaccineRecord given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientVaccineRecord
   * @throws IOException if the JSON string is invalid with respect to PatientVaccineRecord
   */
  public static PatientVaccineRecord fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientVaccineRecord.class);
  }

  /**
   * Convert an instance of PatientVaccineRecord to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

