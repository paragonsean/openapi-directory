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
 * 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AutoAccidentInsurance {
  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_CASE_NUMBER = "auto_accident_case_number";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_CASE_NUMBER)
  private String autoAccidentCaseNumber;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_ADDRESS = "auto_accident_claim_rep_address";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_ADDRESS)
  private String autoAccidentClaimRepAddress;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_CITY = "auto_accident_claim_rep_city";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_CITY)
  private String autoAccidentClaimRepCity;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_IS_INSURER = "auto_accident_claim_rep_is_insurer";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_IS_INSURER)
  private Boolean autoAccidentClaimRepIsInsurer;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_NAME = "auto_accident_claim_rep_name";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_NAME)
  private String autoAccidentClaimRepName;

  /**
   * 
   */
  @JsonAdapter(AutoAccidentClaimRepStateEnum.Adapter.class)
  public enum AutoAccidentClaimRepStateEnum {
    AL("AL"),
    
    AK("AK"),
    
    AS("AS"),
    
    AZ("AZ"),
    
    AR("AR"),
    
    AA("AA"),
    
    AE("AE"),
    
    AP("AP"),
    
    CA("CA"),
    
    CO("CO"),
    
    CT("CT"),
    
    DE("DE"),
    
    DC("DC"),
    
    FL("FL"),
    
    GA("GA"),
    
    GU("GU"),
    
    HI("HI"),
    
    ID("ID"),
    
    IL("IL"),
    
    IN("IN"),
    
    IA("IA"),
    
    KS("KS"),
    
    KY("KY"),
    
    LA("LA"),
    
    ME("ME"),
    
    MD("MD"),
    
    MA("MA"),
    
    MI("MI"),
    
    MN("MN"),
    
    MS("MS"),
    
    MO("MO"),
    
    MT("MT"),
    
    NE("NE"),
    
    NV("NV"),
    
    NH("NH"),
    
    NJ("NJ"),
    
    NM("NM"),
    
    NY("NY"),
    
    NC("NC"),
    
    ND("ND"),
    
    MP("MP"),
    
    OH("OH"),
    
    OK("OK"),
    
    OR("OR"),
    
    PA("PA"),
    
    PR("PR"),
    
    RI("RI"),
    
    SC("SC"),
    
    SD("SD"),
    
    TN("TN"),
    
    TX("TX"),
    
    UT("UT"),
    
    VT("VT"),
    
    VI("VI"),
    
    VA("VA"),
    
    WA("WA"),
    
    WV("WV"),
    
    WI("WI"),
    
    WY("WY");

    private String value;

    AutoAccidentClaimRepStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AutoAccidentClaimRepStateEnum fromValue(String value) {
      for (AutoAccidentClaimRepStateEnum b : AutoAccidentClaimRepStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AutoAccidentClaimRepStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AutoAccidentClaimRepStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AutoAccidentClaimRepStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AutoAccidentClaimRepStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AutoAccidentClaimRepStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_STATE = "auto_accident_claim_rep_state";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_STATE)
  private AutoAccidentClaimRepStateEnum autoAccidentClaimRepState;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_ZIP = "auto_accident_claim_rep_zip";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_CLAIM_REP_ZIP)
  private String autoAccidentClaimRepZip;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_COMPANY = "auto_accident_company";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_COMPANY)
  private String autoAccidentCompany;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_DATE_OF_ACCIDENT = "auto_accident_date_of_accident";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_DATE_OF_ACCIDENT)
  private String autoAccidentDateOfAccident;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_DISABLED_FROM_DATE = "auto_accident_disabled_from_date";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_DISABLED_FROM_DATE)
  private String autoAccidentDisabledFromDate;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_DISABLED_TO_DATE = "auto_accident_disabled_to_date";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_DISABLED_TO_DATE)
  private String autoAccidentDisabledToDate;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_HAD_SIMILAR_CONDITION = "auto_accident_had_similar_condition";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_HAD_SIMILAR_CONDITION)
  private Boolean autoAccidentHadSimilarCondition;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_IS_SUBSCRIBER_THE_PATIENT = "auto_accident_is_subscriber_the_patient";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_IS_SUBSCRIBER_THE_PATIENT)
  private Boolean autoAccidentIsSubscriberThePatient;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_NOTES = "auto_accident_notes";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_NOTES)
  private String autoAccidentNotes;

  /**
   * 
   */
  @JsonAdapter(AutoAccidentPatientRelationshipToSubscriberEnum.Adapter.class)
  public enum AutoAccidentPatientRelationshipToSubscriberEnum {
    EMPTY(""),
    
    _01("01"),
    
    _04("04"),
    
    _05("05"),
    
    _07("07"),
    
    _10("10"),
    
    _15("15"),
    
    _17("17"),
    
    _19("19"),
    
    _20("20"),
    
    _21("21"),
    
    _22("22"),
    
    _23("23"),
    
    _24("24"),
    
    _29("29"),
    
    _32("32"),
    
    _33("33"),
    
    _36("36"),
    
    _39("39"),
    
    _40("40"),
    
    _41("41"),
    
    _43("43"),
    
    _53("53"),
    
    _76("76"),
    
    G8("G8");

    private String value;

    AutoAccidentPatientRelationshipToSubscriberEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AutoAccidentPatientRelationshipToSubscriberEnum fromValue(String value) {
      for (AutoAccidentPatientRelationshipToSubscriberEnum b : AutoAccidentPatientRelationshipToSubscriberEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AutoAccidentPatientRelationshipToSubscriberEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AutoAccidentPatientRelationshipToSubscriberEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AutoAccidentPatientRelationshipToSubscriberEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AutoAccidentPatientRelationshipToSubscriberEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AutoAccidentPatientRelationshipToSubscriberEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_PATIENT_RELATIONSHIP_TO_SUBSCRIBER = "auto_accident_patient_relationship_to_subscriber";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_PATIENT_RELATIONSHIP_TO_SUBSCRIBER)
  private AutoAccidentPatientRelationshipToSubscriberEnum autoAccidentPatientRelationshipToSubscriber;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_ADDRESS = "auto_accident_payer_address";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_ADDRESS)
  private String autoAccidentPayerAddress;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_CITY = "auto_accident_payer_city";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_CITY)
  private String autoAccidentPayerCity;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_ID = "auto_accident_payer_id";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_ID)
  private String autoAccidentPayerId;

  /**
   * 
   */
  @JsonAdapter(AutoAccidentPayerStateEnum.Adapter.class)
  public enum AutoAccidentPayerStateEnum {
    AL("AL"),
    
    AK("AK"),
    
    AS("AS"),
    
    AZ("AZ"),
    
    AR("AR"),
    
    AA("AA"),
    
    AE("AE"),
    
    AP("AP"),
    
    CA("CA"),
    
    CO("CO"),
    
    CT("CT"),
    
    DE("DE"),
    
    DC("DC"),
    
    FL("FL"),
    
    GA("GA"),
    
    GU("GU"),
    
    HI("HI"),
    
    ID("ID"),
    
    IL("IL"),
    
    IN("IN"),
    
    IA("IA"),
    
    KS("KS"),
    
    KY("KY"),
    
    LA("LA"),
    
    ME("ME"),
    
    MD("MD"),
    
    MA("MA"),
    
    MI("MI"),
    
    MN("MN"),
    
    MS("MS"),
    
    MO("MO"),
    
    MT("MT"),
    
    NE("NE"),
    
    NV("NV"),
    
    NH("NH"),
    
    NJ("NJ"),
    
    NM("NM"),
    
    NY("NY"),
    
    NC("NC"),
    
    ND("ND"),
    
    MP("MP"),
    
    OH("OH"),
    
    OK("OK"),
    
    OR("OR"),
    
    PA("PA"),
    
    PR("PR"),
    
    RI("RI"),
    
    SC("SC"),
    
    SD("SD"),
    
    TN("TN"),
    
    TX("TX"),
    
    UT("UT"),
    
    VT("VT"),
    
    VI("VI"),
    
    VA("VA"),
    
    WA("WA"),
    
    WV("WV"),
    
    WI("WI"),
    
    WY("WY");

    private String value;

    AutoAccidentPayerStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AutoAccidentPayerStateEnum fromValue(String value) {
      for (AutoAccidentPayerStateEnum b : AutoAccidentPayerStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AutoAccidentPayerStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AutoAccidentPayerStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AutoAccidentPayerStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AutoAccidentPayerStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AutoAccidentPayerStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_STATE = "auto_accident_payer_state";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_STATE)
  private AutoAccidentPayerStateEnum autoAccidentPayerState;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_ZIP = "auto_accident_payer_zip";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_PAYER_ZIP)
  private String autoAccidentPayerZip;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_POLICY_NUMBER = "auto_accident_policy_number";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_POLICY_NUMBER)
  private String autoAccidentPolicyNumber;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_RETURN_TO_WORK_DATE = "auto_accident_return_to_work_date";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_RETURN_TO_WORK_DATE)
  private String autoAccidentReturnToWorkDate;

  /**
   * 
   */
  @JsonAdapter(AutoAccidentSignificantInjuryEnum.Adapter.class)
  public enum AutoAccidentSignificantInjuryEnum {
    TRUE("true"),
    
    FALSE("false"),
    
    N_A("N\\A");

    private String value;

    AutoAccidentSignificantInjuryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AutoAccidentSignificantInjuryEnum fromValue(String value) {
      for (AutoAccidentSignificantInjuryEnum b : AutoAccidentSignificantInjuryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AutoAccidentSignificantInjuryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AutoAccidentSignificantInjuryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AutoAccidentSignificantInjuryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AutoAccidentSignificantInjuryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AutoAccidentSignificantInjuryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SIGNIFICANT_INJURY = "auto_accident_significant_injury";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SIGNIFICANT_INJURY)
  private AutoAccidentSignificantInjuryEnum autoAccidentSignificantInjury;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SIGNIFICANT_INJURY_NOTES = "auto_accident_significant_injury_notes";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SIGNIFICANT_INJURY_NOTES)
  private String autoAccidentSignificantInjuryNotes;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SIMILAR_CONDITION_DATE = "auto_accident_similar_condition_date";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SIMILAR_CONDITION_DATE)
  private String autoAccidentSimilarConditionDate;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SIMILAR_CONDITION_NOTES = "auto_accident_similar_condition_notes";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SIMILAR_CONDITION_NOTES)
  private String autoAccidentSimilarConditionNotes;

  /**
   * 
   */
  @JsonAdapter(AutoAccidentStateOfOccurrenceEnum.Adapter.class)
  public enum AutoAccidentStateOfOccurrenceEnum {
    AL("AL"),
    
    AK("AK"),
    
    AS("AS"),
    
    AZ("AZ"),
    
    AR("AR"),
    
    AA("AA"),
    
    AE("AE"),
    
    AP("AP"),
    
    CA("CA"),
    
    CO("CO"),
    
    CT("CT"),
    
    DE("DE"),
    
    DC("DC"),
    
    FL("FL"),
    
    GA("GA"),
    
    GU("GU"),
    
    HI("HI"),
    
    ID("ID"),
    
    IL("IL"),
    
    IN("IN"),
    
    IA("IA"),
    
    KS("KS"),
    
    KY("KY"),
    
    LA("LA"),
    
    ME("ME"),
    
    MD("MD"),
    
    MA("MA"),
    
    MI("MI"),
    
    MN("MN"),
    
    MS("MS"),
    
    MO("MO"),
    
    MT("MT"),
    
    NE("NE"),
    
    NV("NV"),
    
    NH("NH"),
    
    NJ("NJ"),
    
    NM("NM"),
    
    NY("NY"),
    
    NC("NC"),
    
    ND("ND"),
    
    MP("MP"),
    
    OH("OH"),
    
    OK("OK"),
    
    OR("OR"),
    
    PA("PA"),
    
    PR("PR"),
    
    RI("RI"),
    
    SC("SC"),
    
    SD("SD"),
    
    TN("TN"),
    
    TX("TX"),
    
    UT("UT"),
    
    VT("VT"),
    
    VI("VI"),
    
    VA("VA"),
    
    WA("WA"),
    
    WV("WV"),
    
    WI("WI"),
    
    WY("WY");

    private String value;

    AutoAccidentStateOfOccurrenceEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AutoAccidentStateOfOccurrenceEnum fromValue(String value) {
      for (AutoAccidentStateOfOccurrenceEnum b : AutoAccidentStateOfOccurrenceEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AutoAccidentStateOfOccurrenceEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AutoAccidentStateOfOccurrenceEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AutoAccidentStateOfOccurrenceEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AutoAccidentStateOfOccurrenceEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AutoAccidentStateOfOccurrenceEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_STATE_OF_OCCURRENCE = "auto_accident_state_of_occurrence";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_STATE_OF_OCCURRENCE)
  private AutoAccidentStateOfOccurrenceEnum autoAccidentStateOfOccurrence;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_STILL_UNDER_CARE = "auto_accident_still_under_care";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_STILL_UNDER_CARE)
  private Boolean autoAccidentStillUnderCare;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_ADDRESS = "auto_accident_subscriber_address";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_ADDRESS)
  private String autoAccidentSubscriberAddress;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_CITY = "auto_accident_subscriber_city";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_CITY)
  private String autoAccidentSubscriberCity;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_DATE_OF_BIRTH = "auto_accident_subscriber_date_of_birth";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_DATE_OF_BIRTH)
  private String autoAccidentSubscriberDateOfBirth;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_FIRST_NAME = "auto_accident_subscriber_first_name";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_FIRST_NAME)
  private String autoAccidentSubscriberFirstName;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_LAST_NAME = "auto_accident_subscriber_last_name";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_LAST_NAME)
  private String autoAccidentSubscriberLastName;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_MIDDLE_NAME = "auto_accident_subscriber_middle_name";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_MIDDLE_NAME)
  private String autoAccidentSubscriberMiddleName;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_PHONE_NUMBER = "auto_accident_subscriber_phone_number";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_PHONE_NUMBER)
  private String autoAccidentSubscriberPhoneNumber;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_SOCIAL_SECURITY = "auto_accident_subscriber_social_security";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_SOCIAL_SECURITY)
  private String autoAccidentSubscriberSocialSecurity;

  /**
   * 
   */
  @JsonAdapter(AutoAccidentSubscriberStateEnum.Adapter.class)
  public enum AutoAccidentSubscriberStateEnum {
    AL("AL"),
    
    AK("AK"),
    
    AS("AS"),
    
    AZ("AZ"),
    
    AR("AR"),
    
    AA("AA"),
    
    AE("AE"),
    
    AP("AP"),
    
    CA("CA"),
    
    CO("CO"),
    
    CT("CT"),
    
    DE("DE"),
    
    DC("DC"),
    
    FL("FL"),
    
    GA("GA"),
    
    GU("GU"),
    
    HI("HI"),
    
    ID("ID"),
    
    IL("IL"),
    
    IN("IN"),
    
    IA("IA"),
    
    KS("KS"),
    
    KY("KY"),
    
    LA("LA"),
    
    ME("ME"),
    
    MD("MD"),
    
    MA("MA"),
    
    MI("MI"),
    
    MN("MN"),
    
    MS("MS"),
    
    MO("MO"),
    
    MT("MT"),
    
    NE("NE"),
    
    NV("NV"),
    
    NH("NH"),
    
    NJ("NJ"),
    
    NM("NM"),
    
    NY("NY"),
    
    NC("NC"),
    
    ND("ND"),
    
    MP("MP"),
    
    OH("OH"),
    
    OK("OK"),
    
    OR("OR"),
    
    PA("PA"),
    
    PR("PR"),
    
    RI("RI"),
    
    SC("SC"),
    
    SD("SD"),
    
    TN("TN"),
    
    TX("TX"),
    
    UT("UT"),
    
    VT("VT"),
    
    VI("VI"),
    
    VA("VA"),
    
    WA("WA"),
    
    WV("WV"),
    
    WI("WI"),
    
    WY("WY");

    private String value;

    AutoAccidentSubscriberStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AutoAccidentSubscriberStateEnum fromValue(String value) {
      for (AutoAccidentSubscriberStateEnum b : AutoAccidentSubscriberStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AutoAccidentSubscriberStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AutoAccidentSubscriberStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AutoAccidentSubscriberStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AutoAccidentSubscriberStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AutoAccidentSubscriberStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_STATE = "auto_accident_subscriber_state";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_STATE)
  private AutoAccidentSubscriberStateEnum autoAccidentSubscriberState;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_SUFFIX = "auto_accident_subscriber_suffix";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_SUFFIX)
  private String autoAccidentSubscriberSuffix;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_ZIP_CODE = "auto_accident_subscriber_zip_code";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_SUBSCRIBER_ZIP_CODE)
  private String autoAccidentSubscriberZipCode;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_TREATMENT_DURATION = "auto_accident_treatment_duration";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_TREATMENT_DURATION)
  private String autoAccidentTreatmentDuration;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_WILL_REQUIRE_THERAPY = "auto_accident_will_require_therapy";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_WILL_REQUIRE_THERAPY)
  private Boolean autoAccidentWillRequireTherapy;

  public static final String SERIALIZED_NAME_AUTO_ACCIDENT_WILL_REQUIRE_THERAPY_REC = "auto_accident_will_require_therapy_rec";
  @SerializedName(SERIALIZED_NAME_AUTO_ACCIDENT_WILL_REQUIRE_THERAPY_REC)
  private String autoAccidentWillRequireTherapyRec;

  public AutoAccidentInsurance() {
  }

  public AutoAccidentInsurance autoAccidentCaseNumber(String autoAccidentCaseNumber) {
    this.autoAccidentCaseNumber = autoAccidentCaseNumber;
    return this;
  }

  /**
   * 
   * @return autoAccidentCaseNumber
   */
  @javax.annotation.Nullable
  public String getAutoAccidentCaseNumber() {
    return autoAccidentCaseNumber;
  }

  public void setAutoAccidentCaseNumber(String autoAccidentCaseNumber) {
    this.autoAccidentCaseNumber = autoAccidentCaseNumber;
  }


  public AutoAccidentInsurance autoAccidentClaimRepAddress(String autoAccidentClaimRepAddress) {
    this.autoAccidentClaimRepAddress = autoAccidentClaimRepAddress;
    return this;
  }

  /**
   * 
   * @return autoAccidentClaimRepAddress
   */
  @javax.annotation.Nullable
  public String getAutoAccidentClaimRepAddress() {
    return autoAccidentClaimRepAddress;
  }

  public void setAutoAccidentClaimRepAddress(String autoAccidentClaimRepAddress) {
    this.autoAccidentClaimRepAddress = autoAccidentClaimRepAddress;
  }


  public AutoAccidentInsurance autoAccidentClaimRepCity(String autoAccidentClaimRepCity) {
    this.autoAccidentClaimRepCity = autoAccidentClaimRepCity;
    return this;
  }

  /**
   * 
   * @return autoAccidentClaimRepCity
   */
  @javax.annotation.Nullable
  public String getAutoAccidentClaimRepCity() {
    return autoAccidentClaimRepCity;
  }

  public void setAutoAccidentClaimRepCity(String autoAccidentClaimRepCity) {
    this.autoAccidentClaimRepCity = autoAccidentClaimRepCity;
  }


  public AutoAccidentInsurance autoAccidentClaimRepIsInsurer(Boolean autoAccidentClaimRepIsInsurer) {
    this.autoAccidentClaimRepIsInsurer = autoAccidentClaimRepIsInsurer;
    return this;
  }

  /**
   * Is the insurer&#39;s claim representative the insurer?
   * @return autoAccidentClaimRepIsInsurer
   */
  @javax.annotation.Nullable
  public Boolean getAutoAccidentClaimRepIsInsurer() {
    return autoAccidentClaimRepIsInsurer;
  }

  public void setAutoAccidentClaimRepIsInsurer(Boolean autoAccidentClaimRepIsInsurer) {
    this.autoAccidentClaimRepIsInsurer = autoAccidentClaimRepIsInsurer;
  }


  public AutoAccidentInsurance autoAccidentClaimRepName(String autoAccidentClaimRepName) {
    this.autoAccidentClaimRepName = autoAccidentClaimRepName;
    return this;
  }

  /**
   * 
   * @return autoAccidentClaimRepName
   */
  @javax.annotation.Nullable
  public String getAutoAccidentClaimRepName() {
    return autoAccidentClaimRepName;
  }

  public void setAutoAccidentClaimRepName(String autoAccidentClaimRepName) {
    this.autoAccidentClaimRepName = autoAccidentClaimRepName;
  }


  public AutoAccidentInsurance autoAccidentClaimRepState(AutoAccidentClaimRepStateEnum autoAccidentClaimRepState) {
    this.autoAccidentClaimRepState = autoAccidentClaimRepState;
    return this;
  }

  /**
   * 
   * @return autoAccidentClaimRepState
   */
  @javax.annotation.Nullable
  public AutoAccidentClaimRepStateEnum getAutoAccidentClaimRepState() {
    return autoAccidentClaimRepState;
  }

  public void setAutoAccidentClaimRepState(AutoAccidentClaimRepStateEnum autoAccidentClaimRepState) {
    this.autoAccidentClaimRepState = autoAccidentClaimRepState;
  }


  public AutoAccidentInsurance autoAccidentClaimRepZip(String autoAccidentClaimRepZip) {
    this.autoAccidentClaimRepZip = autoAccidentClaimRepZip;
    return this;
  }

  /**
   * 
   * @return autoAccidentClaimRepZip
   */
  @javax.annotation.Nullable
  public String getAutoAccidentClaimRepZip() {
    return autoAccidentClaimRepZip;
  }

  public void setAutoAccidentClaimRepZip(String autoAccidentClaimRepZip) {
    this.autoAccidentClaimRepZip = autoAccidentClaimRepZip;
  }


  public AutoAccidentInsurance autoAccidentCompany(String autoAccidentCompany) {
    this.autoAccidentCompany = autoAccidentCompany;
    return this;
  }

  /**
   * 
   * @return autoAccidentCompany
   */
  @javax.annotation.Nullable
  public String getAutoAccidentCompany() {
    return autoAccidentCompany;
  }

  public void setAutoAccidentCompany(String autoAccidentCompany) {
    this.autoAccidentCompany = autoAccidentCompany;
  }


  public AutoAccidentInsurance autoAccidentDateOfAccident(String autoAccidentDateOfAccident) {
    this.autoAccidentDateOfAccident = autoAccidentDateOfAccident;
    return this;
  }

  /**
   * 
   * @return autoAccidentDateOfAccident
   */
  @javax.annotation.Nullable
  public String getAutoAccidentDateOfAccident() {
    return autoAccidentDateOfAccident;
  }

  public void setAutoAccidentDateOfAccident(String autoAccidentDateOfAccident) {
    this.autoAccidentDateOfAccident = autoAccidentDateOfAccident;
  }


  public AutoAccidentInsurance autoAccidentDisabledFromDate(String autoAccidentDisabledFromDate) {
    this.autoAccidentDisabledFromDate = autoAccidentDisabledFromDate;
    return this;
  }

  /**
   * Patient was disabled (unable to work) from
   * @return autoAccidentDisabledFromDate
   */
  @javax.annotation.Nullable
  public String getAutoAccidentDisabledFromDate() {
    return autoAccidentDisabledFromDate;
  }

  public void setAutoAccidentDisabledFromDate(String autoAccidentDisabledFromDate) {
    this.autoAccidentDisabledFromDate = autoAccidentDisabledFromDate;
  }


  public AutoAccidentInsurance autoAccidentDisabledToDate(String autoAccidentDisabledToDate) {
    this.autoAccidentDisabledToDate = autoAccidentDisabledToDate;
    return this;
  }

  /**
   * Patient was disabled (unable to work) to
   * @return autoAccidentDisabledToDate
   */
  @javax.annotation.Nullable
  public String getAutoAccidentDisabledToDate() {
    return autoAccidentDisabledToDate;
  }

  public void setAutoAccidentDisabledToDate(String autoAccidentDisabledToDate) {
    this.autoAccidentDisabledToDate = autoAccidentDisabledToDate;
  }


  public AutoAccidentInsurance autoAccidentHadSimilarCondition(Boolean autoAccidentHadSimilarCondition) {
    this.autoAccidentHadSimilarCondition = autoAccidentHadSimilarCondition;
    return this;
  }

  /**
   * Has the patient had same or similar condition?
   * @return autoAccidentHadSimilarCondition
   */
  @javax.annotation.Nullable
  public Boolean getAutoAccidentHadSimilarCondition() {
    return autoAccidentHadSimilarCondition;
  }

  public void setAutoAccidentHadSimilarCondition(Boolean autoAccidentHadSimilarCondition) {
    this.autoAccidentHadSimilarCondition = autoAccidentHadSimilarCondition;
  }


  public AutoAccidentInsurance autoAccidentIsSubscriberThePatient(Boolean autoAccidentIsSubscriberThePatient) {
    this.autoAccidentIsSubscriberThePatient = autoAccidentIsSubscriberThePatient;
    return this;
  }

  /**
   * True if the insurance policy is under patient&#39;s own name.
   * @return autoAccidentIsSubscriberThePatient
   */
  @javax.annotation.Nullable
  public Boolean getAutoAccidentIsSubscriberThePatient() {
    return autoAccidentIsSubscriberThePatient;
  }

  public void setAutoAccidentIsSubscriberThePatient(Boolean autoAccidentIsSubscriberThePatient) {
    this.autoAccidentIsSubscriberThePatient = autoAccidentIsSubscriberThePatient;
  }


  public AutoAccidentInsurance autoAccidentNotes(String autoAccidentNotes) {
    this.autoAccidentNotes = autoAccidentNotes;
    return this;
  }

  /**
   * 
   * @return autoAccidentNotes
   */
  @javax.annotation.Nullable
  public String getAutoAccidentNotes() {
    return autoAccidentNotes;
  }

  public void setAutoAccidentNotes(String autoAccidentNotes) {
    this.autoAccidentNotes = autoAccidentNotes;
  }


  public AutoAccidentInsurance autoAccidentPatientRelationshipToSubscriber(AutoAccidentPatientRelationshipToSubscriberEnum autoAccidentPatientRelationshipToSubscriber) {
    this.autoAccidentPatientRelationshipToSubscriber = autoAccidentPatientRelationshipToSubscriber;
    return this;
  }

  /**
   * 
   * @return autoAccidentPatientRelationshipToSubscriber
   */
  @javax.annotation.Nullable
  public AutoAccidentPatientRelationshipToSubscriberEnum getAutoAccidentPatientRelationshipToSubscriber() {
    return autoAccidentPatientRelationshipToSubscriber;
  }

  public void setAutoAccidentPatientRelationshipToSubscriber(AutoAccidentPatientRelationshipToSubscriberEnum autoAccidentPatientRelationshipToSubscriber) {
    this.autoAccidentPatientRelationshipToSubscriber = autoAccidentPatientRelationshipToSubscriber;
  }


  public AutoAccidentInsurance autoAccidentPayerAddress(String autoAccidentPayerAddress) {
    this.autoAccidentPayerAddress = autoAccidentPayerAddress;
    return this;
  }

  /**
   * 
   * @return autoAccidentPayerAddress
   */
  @javax.annotation.Nullable
  public String getAutoAccidentPayerAddress() {
    return autoAccidentPayerAddress;
  }

  public void setAutoAccidentPayerAddress(String autoAccidentPayerAddress) {
    this.autoAccidentPayerAddress = autoAccidentPayerAddress;
  }


  public AutoAccidentInsurance autoAccidentPayerCity(String autoAccidentPayerCity) {
    this.autoAccidentPayerCity = autoAccidentPayerCity;
    return this;
  }

  /**
   * 
   * @return autoAccidentPayerCity
   */
  @javax.annotation.Nullable
  public String getAutoAccidentPayerCity() {
    return autoAccidentPayerCity;
  }

  public void setAutoAccidentPayerCity(String autoAccidentPayerCity) {
    this.autoAccidentPayerCity = autoAccidentPayerCity;
  }


  public AutoAccidentInsurance autoAccidentPayerId(String autoAccidentPayerId) {
    this.autoAccidentPayerId = autoAccidentPayerId;
    return this;
  }

  /**
   * Auto Accident Payer ID
   * @return autoAccidentPayerId
   */
  @javax.annotation.Nullable
  public String getAutoAccidentPayerId() {
    return autoAccidentPayerId;
  }

  public void setAutoAccidentPayerId(String autoAccidentPayerId) {
    this.autoAccidentPayerId = autoAccidentPayerId;
  }


  public AutoAccidentInsurance autoAccidentPayerState(AutoAccidentPayerStateEnum autoAccidentPayerState) {
    this.autoAccidentPayerState = autoAccidentPayerState;
    return this;
  }

  /**
   * 
   * @return autoAccidentPayerState
   */
  @javax.annotation.Nullable
  public AutoAccidentPayerStateEnum getAutoAccidentPayerState() {
    return autoAccidentPayerState;
  }

  public void setAutoAccidentPayerState(AutoAccidentPayerStateEnum autoAccidentPayerState) {
    this.autoAccidentPayerState = autoAccidentPayerState;
  }


  public AutoAccidentInsurance autoAccidentPayerZip(String autoAccidentPayerZip) {
    this.autoAccidentPayerZip = autoAccidentPayerZip;
    return this;
  }

  /**
   * 
   * @return autoAccidentPayerZip
   */
  @javax.annotation.Nullable
  public String getAutoAccidentPayerZip() {
    return autoAccidentPayerZip;
  }

  public void setAutoAccidentPayerZip(String autoAccidentPayerZip) {
    this.autoAccidentPayerZip = autoAccidentPayerZip;
  }


  public AutoAccidentInsurance autoAccidentPolicyNumber(String autoAccidentPolicyNumber) {
    this.autoAccidentPolicyNumber = autoAccidentPolicyNumber;
    return this;
  }

  /**
   * 
   * @return autoAccidentPolicyNumber
   */
  @javax.annotation.Nullable
  public String getAutoAccidentPolicyNumber() {
    return autoAccidentPolicyNumber;
  }

  public void setAutoAccidentPolicyNumber(String autoAccidentPolicyNumber) {
    this.autoAccidentPolicyNumber = autoAccidentPolicyNumber;
  }


  public AutoAccidentInsurance autoAccidentReturnToWorkDate(String autoAccidentReturnToWorkDate) {
    this.autoAccidentReturnToWorkDate = autoAccidentReturnToWorkDate;
    return this;
  }

  /**
   * If still disabled, patient should be able to return to work on
   * @return autoAccidentReturnToWorkDate
   */
  @javax.annotation.Nullable
  public String getAutoAccidentReturnToWorkDate() {
    return autoAccidentReturnToWorkDate;
  }

  public void setAutoAccidentReturnToWorkDate(String autoAccidentReturnToWorkDate) {
    this.autoAccidentReturnToWorkDate = autoAccidentReturnToWorkDate;
  }


  public AutoAccidentInsurance autoAccidentSignificantInjury(AutoAccidentSignificantInjuryEnum autoAccidentSignificantInjury) {
    this.autoAccidentSignificantInjury = autoAccidentSignificantInjury;
    return this;
  }

  /**
   * 
   * @return autoAccidentSignificantInjury
   */
  @javax.annotation.Nullable
  public AutoAccidentSignificantInjuryEnum getAutoAccidentSignificantInjury() {
    return autoAccidentSignificantInjury;
  }

  public void setAutoAccidentSignificantInjury(AutoAccidentSignificantInjuryEnum autoAccidentSignificantInjury) {
    this.autoAccidentSignificantInjury = autoAccidentSignificantInjury;
  }


  public AutoAccidentInsurance autoAccidentSignificantInjuryNotes(String autoAccidentSignificantInjuryNotes) {
    this.autoAccidentSignificantInjuryNotes = autoAccidentSignificantInjuryNotes;
    return this;
  }

  /**
   * 
   * @return autoAccidentSignificantInjuryNotes
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSignificantInjuryNotes() {
    return autoAccidentSignificantInjuryNotes;
  }

  public void setAutoAccidentSignificantInjuryNotes(String autoAccidentSignificantInjuryNotes) {
    this.autoAccidentSignificantInjuryNotes = autoAccidentSignificantInjuryNotes;
  }


  public AutoAccidentInsurance autoAccidentSimilarConditionDate(String autoAccidentSimilarConditionDate) {
    this.autoAccidentSimilarConditionDate = autoAccidentSimilarConditionDate;
    return this;
  }

  /**
   * Date of same or similar condition
   * @return autoAccidentSimilarConditionDate
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSimilarConditionDate() {
    return autoAccidentSimilarConditionDate;
  }

  public void setAutoAccidentSimilarConditionDate(String autoAccidentSimilarConditionDate) {
    this.autoAccidentSimilarConditionDate = autoAccidentSimilarConditionDate;
  }


  public AutoAccidentInsurance autoAccidentSimilarConditionNotes(String autoAccidentSimilarConditionNotes) {
    this.autoAccidentSimilarConditionNotes = autoAccidentSimilarConditionNotes;
    return this;
  }

  /**
   * 
   * @return autoAccidentSimilarConditionNotes
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSimilarConditionNotes() {
    return autoAccidentSimilarConditionNotes;
  }

  public void setAutoAccidentSimilarConditionNotes(String autoAccidentSimilarConditionNotes) {
    this.autoAccidentSimilarConditionNotes = autoAccidentSimilarConditionNotes;
  }


  public AutoAccidentInsurance autoAccidentStateOfOccurrence(AutoAccidentStateOfOccurrenceEnum autoAccidentStateOfOccurrence) {
    this.autoAccidentStateOfOccurrence = autoAccidentStateOfOccurrence;
    return this;
  }

  /**
   * 
   * @return autoAccidentStateOfOccurrence
   */
  @javax.annotation.Nullable
  public AutoAccidentStateOfOccurrenceEnum getAutoAccidentStateOfOccurrence() {
    return autoAccidentStateOfOccurrence;
  }

  public void setAutoAccidentStateOfOccurrence(AutoAccidentStateOfOccurrenceEnum autoAccidentStateOfOccurrence) {
    this.autoAccidentStateOfOccurrence = autoAccidentStateOfOccurrence;
  }


  public AutoAccidentInsurance autoAccidentStillUnderCare(Boolean autoAccidentStillUnderCare) {
    this.autoAccidentStillUnderCare = autoAccidentStillUnderCare;
    return this;
  }

  /**
   * Is patient still under your care for this condition?
   * @return autoAccidentStillUnderCare
   */
  @javax.annotation.Nullable
  public Boolean getAutoAccidentStillUnderCare() {
    return autoAccidentStillUnderCare;
  }

  public void setAutoAccidentStillUnderCare(Boolean autoAccidentStillUnderCare) {
    this.autoAccidentStillUnderCare = autoAccidentStillUnderCare;
  }


  public AutoAccidentInsurance autoAccidentSubscriberAddress(String autoAccidentSubscriberAddress) {
    this.autoAccidentSubscriberAddress = autoAccidentSubscriberAddress;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberAddress
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberAddress() {
    return autoAccidentSubscriberAddress;
  }

  public void setAutoAccidentSubscriberAddress(String autoAccidentSubscriberAddress) {
    this.autoAccidentSubscriberAddress = autoAccidentSubscriberAddress;
  }


  public AutoAccidentInsurance autoAccidentSubscriberCity(String autoAccidentSubscriberCity) {
    this.autoAccidentSubscriberCity = autoAccidentSubscriberCity;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberCity
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberCity() {
    return autoAccidentSubscriberCity;
  }

  public void setAutoAccidentSubscriberCity(String autoAccidentSubscriberCity) {
    this.autoAccidentSubscriberCity = autoAccidentSubscriberCity;
  }


  public AutoAccidentInsurance autoAccidentSubscriberDateOfBirth(String autoAccidentSubscriberDateOfBirth) {
    this.autoAccidentSubscriberDateOfBirth = autoAccidentSubscriberDateOfBirth;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberDateOfBirth
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberDateOfBirth() {
    return autoAccidentSubscriberDateOfBirth;
  }

  public void setAutoAccidentSubscriberDateOfBirth(String autoAccidentSubscriberDateOfBirth) {
    this.autoAccidentSubscriberDateOfBirth = autoAccidentSubscriberDateOfBirth;
  }


  public AutoAccidentInsurance autoAccidentSubscriberFirstName(String autoAccidentSubscriberFirstName) {
    this.autoAccidentSubscriberFirstName = autoAccidentSubscriberFirstName;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberFirstName
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberFirstName() {
    return autoAccidentSubscriberFirstName;
  }

  public void setAutoAccidentSubscriberFirstName(String autoAccidentSubscriberFirstName) {
    this.autoAccidentSubscriberFirstName = autoAccidentSubscriberFirstName;
  }


  public AutoAccidentInsurance autoAccidentSubscriberLastName(String autoAccidentSubscriberLastName) {
    this.autoAccidentSubscriberLastName = autoAccidentSubscriberLastName;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberLastName
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberLastName() {
    return autoAccidentSubscriberLastName;
  }

  public void setAutoAccidentSubscriberLastName(String autoAccidentSubscriberLastName) {
    this.autoAccidentSubscriberLastName = autoAccidentSubscriberLastName;
  }


  public AutoAccidentInsurance autoAccidentSubscriberMiddleName(String autoAccidentSubscriberMiddleName) {
    this.autoAccidentSubscriberMiddleName = autoAccidentSubscriberMiddleName;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberMiddleName
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberMiddleName() {
    return autoAccidentSubscriberMiddleName;
  }

  public void setAutoAccidentSubscriberMiddleName(String autoAccidentSubscriberMiddleName) {
    this.autoAccidentSubscriberMiddleName = autoAccidentSubscriberMiddleName;
  }


  public AutoAccidentInsurance autoAccidentSubscriberPhoneNumber(String autoAccidentSubscriberPhoneNumber) {
    this.autoAccidentSubscriberPhoneNumber = autoAccidentSubscriberPhoneNumber;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberPhoneNumber
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberPhoneNumber() {
    return autoAccidentSubscriberPhoneNumber;
  }

  public void setAutoAccidentSubscriberPhoneNumber(String autoAccidentSubscriberPhoneNumber) {
    this.autoAccidentSubscriberPhoneNumber = autoAccidentSubscriberPhoneNumber;
  }


  public AutoAccidentInsurance autoAccidentSubscriberSocialSecurity(String autoAccidentSubscriberSocialSecurity) {
    this.autoAccidentSubscriberSocialSecurity = autoAccidentSubscriberSocialSecurity;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberSocialSecurity
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberSocialSecurity() {
    return autoAccidentSubscriberSocialSecurity;
  }

  public void setAutoAccidentSubscriberSocialSecurity(String autoAccidentSubscriberSocialSecurity) {
    this.autoAccidentSubscriberSocialSecurity = autoAccidentSubscriberSocialSecurity;
  }


  public AutoAccidentInsurance autoAccidentSubscriberState(AutoAccidentSubscriberStateEnum autoAccidentSubscriberState) {
    this.autoAccidentSubscriberState = autoAccidentSubscriberState;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberState
   */
  @javax.annotation.Nullable
  public AutoAccidentSubscriberStateEnum getAutoAccidentSubscriberState() {
    return autoAccidentSubscriberState;
  }

  public void setAutoAccidentSubscriberState(AutoAccidentSubscriberStateEnum autoAccidentSubscriberState) {
    this.autoAccidentSubscriberState = autoAccidentSubscriberState;
  }


  public AutoAccidentInsurance autoAccidentSubscriberSuffix(String autoAccidentSubscriberSuffix) {
    this.autoAccidentSubscriberSuffix = autoAccidentSubscriberSuffix;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberSuffix
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberSuffix() {
    return autoAccidentSubscriberSuffix;
  }

  public void setAutoAccidentSubscriberSuffix(String autoAccidentSubscriberSuffix) {
    this.autoAccidentSubscriberSuffix = autoAccidentSubscriberSuffix;
  }


  public AutoAccidentInsurance autoAccidentSubscriberZipCode(String autoAccidentSubscriberZipCode) {
    this.autoAccidentSubscriberZipCode = autoAccidentSubscriberZipCode;
    return this;
  }

  /**
   * 
   * @return autoAccidentSubscriberZipCode
   */
  @javax.annotation.Nullable
  public String getAutoAccidentSubscriberZipCode() {
    return autoAccidentSubscriberZipCode;
  }

  public void setAutoAccidentSubscriberZipCode(String autoAccidentSubscriberZipCode) {
    this.autoAccidentSubscriberZipCode = autoAccidentSubscriberZipCode;
  }


  public AutoAccidentInsurance autoAccidentTreatmentDuration(String autoAccidentTreatmentDuration) {
    this.autoAccidentTreatmentDuration = autoAccidentTreatmentDuration;
    return this;
  }

  /**
   * 
   * @return autoAccidentTreatmentDuration
   */
  @javax.annotation.Nullable
  public String getAutoAccidentTreatmentDuration() {
    return autoAccidentTreatmentDuration;
  }

  public void setAutoAccidentTreatmentDuration(String autoAccidentTreatmentDuration) {
    this.autoAccidentTreatmentDuration = autoAccidentTreatmentDuration;
  }


  public AutoAccidentInsurance autoAccidentWillRequireTherapy(Boolean autoAccidentWillRequireTherapy) {
    this.autoAccidentWillRequireTherapy = autoAccidentWillRequireTherapy;
    return this;
  }

  /**
   * Will the patient require rehabilitation and/or occupational therapy as a result of the injuries sustained in this accident?
   * @return autoAccidentWillRequireTherapy
   */
  @javax.annotation.Nullable
  public Boolean getAutoAccidentWillRequireTherapy() {
    return autoAccidentWillRequireTherapy;
  }

  public void setAutoAccidentWillRequireTherapy(Boolean autoAccidentWillRequireTherapy) {
    this.autoAccidentWillRequireTherapy = autoAccidentWillRequireTherapy;
  }


  public AutoAccidentInsurance autoAccidentWillRequireTherapyRec(String autoAccidentWillRequireTherapyRec) {
    this.autoAccidentWillRequireTherapyRec = autoAccidentWillRequireTherapyRec;
    return this;
  }

  /**
   * 
   * @return autoAccidentWillRequireTherapyRec
   */
  @javax.annotation.Nullable
  public String getAutoAccidentWillRequireTherapyRec() {
    return autoAccidentWillRequireTherapyRec;
  }

  public void setAutoAccidentWillRequireTherapyRec(String autoAccidentWillRequireTherapyRec) {
    this.autoAccidentWillRequireTherapyRec = autoAccidentWillRequireTherapyRec;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AutoAccidentInsurance autoAccidentInsurance = (AutoAccidentInsurance) o;
    return Objects.equals(this.autoAccidentCaseNumber, autoAccidentInsurance.autoAccidentCaseNumber) &&
        Objects.equals(this.autoAccidentClaimRepAddress, autoAccidentInsurance.autoAccidentClaimRepAddress) &&
        Objects.equals(this.autoAccidentClaimRepCity, autoAccidentInsurance.autoAccidentClaimRepCity) &&
        Objects.equals(this.autoAccidentClaimRepIsInsurer, autoAccidentInsurance.autoAccidentClaimRepIsInsurer) &&
        Objects.equals(this.autoAccidentClaimRepName, autoAccidentInsurance.autoAccidentClaimRepName) &&
        Objects.equals(this.autoAccidentClaimRepState, autoAccidentInsurance.autoAccidentClaimRepState) &&
        Objects.equals(this.autoAccidentClaimRepZip, autoAccidentInsurance.autoAccidentClaimRepZip) &&
        Objects.equals(this.autoAccidentCompany, autoAccidentInsurance.autoAccidentCompany) &&
        Objects.equals(this.autoAccidentDateOfAccident, autoAccidentInsurance.autoAccidentDateOfAccident) &&
        Objects.equals(this.autoAccidentDisabledFromDate, autoAccidentInsurance.autoAccidentDisabledFromDate) &&
        Objects.equals(this.autoAccidentDisabledToDate, autoAccidentInsurance.autoAccidentDisabledToDate) &&
        Objects.equals(this.autoAccidentHadSimilarCondition, autoAccidentInsurance.autoAccidentHadSimilarCondition) &&
        Objects.equals(this.autoAccidentIsSubscriberThePatient, autoAccidentInsurance.autoAccidentIsSubscriberThePatient) &&
        Objects.equals(this.autoAccidentNotes, autoAccidentInsurance.autoAccidentNotes) &&
        Objects.equals(this.autoAccidentPatientRelationshipToSubscriber, autoAccidentInsurance.autoAccidentPatientRelationshipToSubscriber) &&
        Objects.equals(this.autoAccidentPayerAddress, autoAccidentInsurance.autoAccidentPayerAddress) &&
        Objects.equals(this.autoAccidentPayerCity, autoAccidentInsurance.autoAccidentPayerCity) &&
        Objects.equals(this.autoAccidentPayerId, autoAccidentInsurance.autoAccidentPayerId) &&
        Objects.equals(this.autoAccidentPayerState, autoAccidentInsurance.autoAccidentPayerState) &&
        Objects.equals(this.autoAccidentPayerZip, autoAccidentInsurance.autoAccidentPayerZip) &&
        Objects.equals(this.autoAccidentPolicyNumber, autoAccidentInsurance.autoAccidentPolicyNumber) &&
        Objects.equals(this.autoAccidentReturnToWorkDate, autoAccidentInsurance.autoAccidentReturnToWorkDate) &&
        Objects.equals(this.autoAccidentSignificantInjury, autoAccidentInsurance.autoAccidentSignificantInjury) &&
        Objects.equals(this.autoAccidentSignificantInjuryNotes, autoAccidentInsurance.autoAccidentSignificantInjuryNotes) &&
        Objects.equals(this.autoAccidentSimilarConditionDate, autoAccidentInsurance.autoAccidentSimilarConditionDate) &&
        Objects.equals(this.autoAccidentSimilarConditionNotes, autoAccidentInsurance.autoAccidentSimilarConditionNotes) &&
        Objects.equals(this.autoAccidentStateOfOccurrence, autoAccidentInsurance.autoAccidentStateOfOccurrence) &&
        Objects.equals(this.autoAccidentStillUnderCare, autoAccidentInsurance.autoAccidentStillUnderCare) &&
        Objects.equals(this.autoAccidentSubscriberAddress, autoAccidentInsurance.autoAccidentSubscriberAddress) &&
        Objects.equals(this.autoAccidentSubscriberCity, autoAccidentInsurance.autoAccidentSubscriberCity) &&
        Objects.equals(this.autoAccidentSubscriberDateOfBirth, autoAccidentInsurance.autoAccidentSubscriberDateOfBirth) &&
        Objects.equals(this.autoAccidentSubscriberFirstName, autoAccidentInsurance.autoAccidentSubscriberFirstName) &&
        Objects.equals(this.autoAccidentSubscriberLastName, autoAccidentInsurance.autoAccidentSubscriberLastName) &&
        Objects.equals(this.autoAccidentSubscriberMiddleName, autoAccidentInsurance.autoAccidentSubscriberMiddleName) &&
        Objects.equals(this.autoAccidentSubscriberPhoneNumber, autoAccidentInsurance.autoAccidentSubscriberPhoneNumber) &&
        Objects.equals(this.autoAccidentSubscriberSocialSecurity, autoAccidentInsurance.autoAccidentSubscriberSocialSecurity) &&
        Objects.equals(this.autoAccidentSubscriberState, autoAccidentInsurance.autoAccidentSubscriberState) &&
        Objects.equals(this.autoAccidentSubscriberSuffix, autoAccidentInsurance.autoAccidentSubscriberSuffix) &&
        Objects.equals(this.autoAccidentSubscriberZipCode, autoAccidentInsurance.autoAccidentSubscriberZipCode) &&
        Objects.equals(this.autoAccidentTreatmentDuration, autoAccidentInsurance.autoAccidentTreatmentDuration) &&
        Objects.equals(this.autoAccidentWillRequireTherapy, autoAccidentInsurance.autoAccidentWillRequireTherapy) &&
        Objects.equals(this.autoAccidentWillRequireTherapyRec, autoAccidentInsurance.autoAccidentWillRequireTherapyRec);
  }

  @Override
  public int hashCode() {
    return Objects.hash(autoAccidentCaseNumber, autoAccidentClaimRepAddress, autoAccidentClaimRepCity, autoAccidentClaimRepIsInsurer, autoAccidentClaimRepName, autoAccidentClaimRepState, autoAccidentClaimRepZip, autoAccidentCompany, autoAccidentDateOfAccident, autoAccidentDisabledFromDate, autoAccidentDisabledToDate, autoAccidentHadSimilarCondition, autoAccidentIsSubscriberThePatient, autoAccidentNotes, autoAccidentPatientRelationshipToSubscriber, autoAccidentPayerAddress, autoAccidentPayerCity, autoAccidentPayerId, autoAccidentPayerState, autoAccidentPayerZip, autoAccidentPolicyNumber, autoAccidentReturnToWorkDate, autoAccidentSignificantInjury, autoAccidentSignificantInjuryNotes, autoAccidentSimilarConditionDate, autoAccidentSimilarConditionNotes, autoAccidentStateOfOccurrence, autoAccidentStillUnderCare, autoAccidentSubscriberAddress, autoAccidentSubscriberCity, autoAccidentSubscriberDateOfBirth, autoAccidentSubscriberFirstName, autoAccidentSubscriberLastName, autoAccidentSubscriberMiddleName, autoAccidentSubscriberPhoneNumber, autoAccidentSubscriberSocialSecurity, autoAccidentSubscriberState, autoAccidentSubscriberSuffix, autoAccidentSubscriberZipCode, autoAccidentTreatmentDuration, autoAccidentWillRequireTherapy, autoAccidentWillRequireTherapyRec);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AutoAccidentInsurance {\n");
    sb.append("    autoAccidentCaseNumber: ").append(toIndentedString(autoAccidentCaseNumber)).append("\n");
    sb.append("    autoAccidentClaimRepAddress: ").append(toIndentedString(autoAccidentClaimRepAddress)).append("\n");
    sb.append("    autoAccidentClaimRepCity: ").append(toIndentedString(autoAccidentClaimRepCity)).append("\n");
    sb.append("    autoAccidentClaimRepIsInsurer: ").append(toIndentedString(autoAccidentClaimRepIsInsurer)).append("\n");
    sb.append("    autoAccidentClaimRepName: ").append(toIndentedString(autoAccidentClaimRepName)).append("\n");
    sb.append("    autoAccidentClaimRepState: ").append(toIndentedString(autoAccidentClaimRepState)).append("\n");
    sb.append("    autoAccidentClaimRepZip: ").append(toIndentedString(autoAccidentClaimRepZip)).append("\n");
    sb.append("    autoAccidentCompany: ").append(toIndentedString(autoAccidentCompany)).append("\n");
    sb.append("    autoAccidentDateOfAccident: ").append(toIndentedString(autoAccidentDateOfAccident)).append("\n");
    sb.append("    autoAccidentDisabledFromDate: ").append(toIndentedString(autoAccidentDisabledFromDate)).append("\n");
    sb.append("    autoAccidentDisabledToDate: ").append(toIndentedString(autoAccidentDisabledToDate)).append("\n");
    sb.append("    autoAccidentHadSimilarCondition: ").append(toIndentedString(autoAccidentHadSimilarCondition)).append("\n");
    sb.append("    autoAccidentIsSubscriberThePatient: ").append(toIndentedString(autoAccidentIsSubscriberThePatient)).append("\n");
    sb.append("    autoAccidentNotes: ").append(toIndentedString(autoAccidentNotes)).append("\n");
    sb.append("    autoAccidentPatientRelationshipToSubscriber: ").append(toIndentedString(autoAccidentPatientRelationshipToSubscriber)).append("\n");
    sb.append("    autoAccidentPayerAddress: ").append(toIndentedString(autoAccidentPayerAddress)).append("\n");
    sb.append("    autoAccidentPayerCity: ").append(toIndentedString(autoAccidentPayerCity)).append("\n");
    sb.append("    autoAccidentPayerId: ").append(toIndentedString(autoAccidentPayerId)).append("\n");
    sb.append("    autoAccidentPayerState: ").append(toIndentedString(autoAccidentPayerState)).append("\n");
    sb.append("    autoAccidentPayerZip: ").append(toIndentedString(autoAccidentPayerZip)).append("\n");
    sb.append("    autoAccidentPolicyNumber: ").append(toIndentedString(autoAccidentPolicyNumber)).append("\n");
    sb.append("    autoAccidentReturnToWorkDate: ").append(toIndentedString(autoAccidentReturnToWorkDate)).append("\n");
    sb.append("    autoAccidentSignificantInjury: ").append(toIndentedString(autoAccidentSignificantInjury)).append("\n");
    sb.append("    autoAccidentSignificantInjuryNotes: ").append(toIndentedString(autoAccidentSignificantInjuryNotes)).append("\n");
    sb.append("    autoAccidentSimilarConditionDate: ").append(toIndentedString(autoAccidentSimilarConditionDate)).append("\n");
    sb.append("    autoAccidentSimilarConditionNotes: ").append(toIndentedString(autoAccidentSimilarConditionNotes)).append("\n");
    sb.append("    autoAccidentStateOfOccurrence: ").append(toIndentedString(autoAccidentStateOfOccurrence)).append("\n");
    sb.append("    autoAccidentStillUnderCare: ").append(toIndentedString(autoAccidentStillUnderCare)).append("\n");
    sb.append("    autoAccidentSubscriberAddress: ").append(toIndentedString(autoAccidentSubscriberAddress)).append("\n");
    sb.append("    autoAccidentSubscriberCity: ").append(toIndentedString(autoAccidentSubscriberCity)).append("\n");
    sb.append("    autoAccidentSubscriberDateOfBirth: ").append(toIndentedString(autoAccidentSubscriberDateOfBirth)).append("\n");
    sb.append("    autoAccidentSubscriberFirstName: ").append(toIndentedString(autoAccidentSubscriberFirstName)).append("\n");
    sb.append("    autoAccidentSubscriberLastName: ").append(toIndentedString(autoAccidentSubscriberLastName)).append("\n");
    sb.append("    autoAccidentSubscriberMiddleName: ").append(toIndentedString(autoAccidentSubscriberMiddleName)).append("\n");
    sb.append("    autoAccidentSubscriberPhoneNumber: ").append(toIndentedString(autoAccidentSubscriberPhoneNumber)).append("\n");
    sb.append("    autoAccidentSubscriberSocialSecurity: ").append(toIndentedString(autoAccidentSubscriberSocialSecurity)).append("\n");
    sb.append("    autoAccidentSubscriberState: ").append(toIndentedString(autoAccidentSubscriberState)).append("\n");
    sb.append("    autoAccidentSubscriberSuffix: ").append(toIndentedString(autoAccidentSubscriberSuffix)).append("\n");
    sb.append("    autoAccidentSubscriberZipCode: ").append(toIndentedString(autoAccidentSubscriberZipCode)).append("\n");
    sb.append("    autoAccidentTreatmentDuration: ").append(toIndentedString(autoAccidentTreatmentDuration)).append("\n");
    sb.append("    autoAccidentWillRequireTherapy: ").append(toIndentedString(autoAccidentWillRequireTherapy)).append("\n");
    sb.append("    autoAccidentWillRequireTherapyRec: ").append(toIndentedString(autoAccidentWillRequireTherapyRec)).append("\n");
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
    openapiFields.add("auto_accident_case_number");
    openapiFields.add("auto_accident_claim_rep_address");
    openapiFields.add("auto_accident_claim_rep_city");
    openapiFields.add("auto_accident_claim_rep_is_insurer");
    openapiFields.add("auto_accident_claim_rep_name");
    openapiFields.add("auto_accident_claim_rep_state");
    openapiFields.add("auto_accident_claim_rep_zip");
    openapiFields.add("auto_accident_company");
    openapiFields.add("auto_accident_date_of_accident");
    openapiFields.add("auto_accident_disabled_from_date");
    openapiFields.add("auto_accident_disabled_to_date");
    openapiFields.add("auto_accident_had_similar_condition");
    openapiFields.add("auto_accident_is_subscriber_the_patient");
    openapiFields.add("auto_accident_notes");
    openapiFields.add("auto_accident_patient_relationship_to_subscriber");
    openapiFields.add("auto_accident_payer_address");
    openapiFields.add("auto_accident_payer_city");
    openapiFields.add("auto_accident_payer_id");
    openapiFields.add("auto_accident_payer_state");
    openapiFields.add("auto_accident_payer_zip");
    openapiFields.add("auto_accident_policy_number");
    openapiFields.add("auto_accident_return_to_work_date");
    openapiFields.add("auto_accident_significant_injury");
    openapiFields.add("auto_accident_significant_injury_notes");
    openapiFields.add("auto_accident_similar_condition_date");
    openapiFields.add("auto_accident_similar_condition_notes");
    openapiFields.add("auto_accident_state_of_occurrence");
    openapiFields.add("auto_accident_still_under_care");
    openapiFields.add("auto_accident_subscriber_address");
    openapiFields.add("auto_accident_subscriber_city");
    openapiFields.add("auto_accident_subscriber_date_of_birth");
    openapiFields.add("auto_accident_subscriber_first_name");
    openapiFields.add("auto_accident_subscriber_last_name");
    openapiFields.add("auto_accident_subscriber_middle_name");
    openapiFields.add("auto_accident_subscriber_phone_number");
    openapiFields.add("auto_accident_subscriber_social_security");
    openapiFields.add("auto_accident_subscriber_state");
    openapiFields.add("auto_accident_subscriber_suffix");
    openapiFields.add("auto_accident_subscriber_zip_code");
    openapiFields.add("auto_accident_treatment_duration");
    openapiFields.add("auto_accident_will_require_therapy");
    openapiFields.add("auto_accident_will_require_therapy_rec");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AutoAccidentInsurance
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AutoAccidentInsurance.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AutoAccidentInsurance is not found in the empty JSON string", AutoAccidentInsurance.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AutoAccidentInsurance.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AutoAccidentInsurance` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("auto_accident_case_number") != null && !jsonObj.get("auto_accident_case_number").isJsonNull()) && !jsonObj.get("auto_accident_case_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_case_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_case_number").toString()));
      }
      if ((jsonObj.get("auto_accident_claim_rep_address") != null && !jsonObj.get("auto_accident_claim_rep_address").isJsonNull()) && !jsonObj.get("auto_accident_claim_rep_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_claim_rep_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_claim_rep_address").toString()));
      }
      if ((jsonObj.get("auto_accident_claim_rep_city") != null && !jsonObj.get("auto_accident_claim_rep_city").isJsonNull()) && !jsonObj.get("auto_accident_claim_rep_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_claim_rep_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_claim_rep_city").toString()));
      }
      if ((jsonObj.get("auto_accident_claim_rep_name") != null && !jsonObj.get("auto_accident_claim_rep_name").isJsonNull()) && !jsonObj.get("auto_accident_claim_rep_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_claim_rep_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_claim_rep_name").toString()));
      }
      if ((jsonObj.get("auto_accident_claim_rep_state") != null && !jsonObj.get("auto_accident_claim_rep_state").isJsonNull()) && !jsonObj.get("auto_accident_claim_rep_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_claim_rep_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_claim_rep_state").toString()));
      }
      // validate the optional field `auto_accident_claim_rep_state`
      if (jsonObj.get("auto_accident_claim_rep_state") != null && !jsonObj.get("auto_accident_claim_rep_state").isJsonNull()) {
        AutoAccidentClaimRepStateEnum.validateJsonElement(jsonObj.get("auto_accident_claim_rep_state"));
      }
      if ((jsonObj.get("auto_accident_claim_rep_zip") != null && !jsonObj.get("auto_accident_claim_rep_zip").isJsonNull()) && !jsonObj.get("auto_accident_claim_rep_zip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_claim_rep_zip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_claim_rep_zip").toString()));
      }
      if ((jsonObj.get("auto_accident_company") != null && !jsonObj.get("auto_accident_company").isJsonNull()) && !jsonObj.get("auto_accident_company").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_company` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_company").toString()));
      }
      if ((jsonObj.get("auto_accident_date_of_accident") != null && !jsonObj.get("auto_accident_date_of_accident").isJsonNull()) && !jsonObj.get("auto_accident_date_of_accident").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_date_of_accident` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_date_of_accident").toString()));
      }
      if ((jsonObj.get("auto_accident_disabled_from_date") != null && !jsonObj.get("auto_accident_disabled_from_date").isJsonNull()) && !jsonObj.get("auto_accident_disabled_from_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_disabled_from_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_disabled_from_date").toString()));
      }
      if ((jsonObj.get("auto_accident_disabled_to_date") != null && !jsonObj.get("auto_accident_disabled_to_date").isJsonNull()) && !jsonObj.get("auto_accident_disabled_to_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_disabled_to_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_disabled_to_date").toString()));
      }
      if ((jsonObj.get("auto_accident_notes") != null && !jsonObj.get("auto_accident_notes").isJsonNull()) && !jsonObj.get("auto_accident_notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_notes").toString()));
      }
      if ((jsonObj.get("auto_accident_patient_relationship_to_subscriber") != null && !jsonObj.get("auto_accident_patient_relationship_to_subscriber").isJsonNull()) && !jsonObj.get("auto_accident_patient_relationship_to_subscriber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_patient_relationship_to_subscriber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_patient_relationship_to_subscriber").toString()));
      }
      // validate the optional field `auto_accident_patient_relationship_to_subscriber`
      if (jsonObj.get("auto_accident_patient_relationship_to_subscriber") != null && !jsonObj.get("auto_accident_patient_relationship_to_subscriber").isJsonNull()) {
        AutoAccidentPatientRelationshipToSubscriberEnum.validateJsonElement(jsonObj.get("auto_accident_patient_relationship_to_subscriber"));
      }
      if ((jsonObj.get("auto_accident_payer_address") != null && !jsonObj.get("auto_accident_payer_address").isJsonNull()) && !jsonObj.get("auto_accident_payer_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_payer_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_payer_address").toString()));
      }
      if ((jsonObj.get("auto_accident_payer_city") != null && !jsonObj.get("auto_accident_payer_city").isJsonNull()) && !jsonObj.get("auto_accident_payer_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_payer_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_payer_city").toString()));
      }
      if ((jsonObj.get("auto_accident_payer_id") != null && !jsonObj.get("auto_accident_payer_id").isJsonNull()) && !jsonObj.get("auto_accident_payer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_payer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_payer_id").toString()));
      }
      if ((jsonObj.get("auto_accident_payer_state") != null && !jsonObj.get("auto_accident_payer_state").isJsonNull()) && !jsonObj.get("auto_accident_payer_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_payer_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_payer_state").toString()));
      }
      // validate the optional field `auto_accident_payer_state`
      if (jsonObj.get("auto_accident_payer_state") != null && !jsonObj.get("auto_accident_payer_state").isJsonNull()) {
        AutoAccidentPayerStateEnum.validateJsonElement(jsonObj.get("auto_accident_payer_state"));
      }
      if ((jsonObj.get("auto_accident_payer_zip") != null && !jsonObj.get("auto_accident_payer_zip").isJsonNull()) && !jsonObj.get("auto_accident_payer_zip").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_payer_zip` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_payer_zip").toString()));
      }
      if ((jsonObj.get("auto_accident_policy_number") != null && !jsonObj.get("auto_accident_policy_number").isJsonNull()) && !jsonObj.get("auto_accident_policy_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_policy_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_policy_number").toString()));
      }
      if ((jsonObj.get("auto_accident_return_to_work_date") != null && !jsonObj.get("auto_accident_return_to_work_date").isJsonNull()) && !jsonObj.get("auto_accident_return_to_work_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_return_to_work_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_return_to_work_date").toString()));
      }
      if ((jsonObj.get("auto_accident_significant_injury") != null && !jsonObj.get("auto_accident_significant_injury").isJsonNull()) && !jsonObj.get("auto_accident_significant_injury").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_significant_injury` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_significant_injury").toString()));
      }
      // validate the optional field `auto_accident_significant_injury`
      if (jsonObj.get("auto_accident_significant_injury") != null && !jsonObj.get("auto_accident_significant_injury").isJsonNull()) {
        AutoAccidentSignificantInjuryEnum.validateJsonElement(jsonObj.get("auto_accident_significant_injury"));
      }
      if ((jsonObj.get("auto_accident_significant_injury_notes") != null && !jsonObj.get("auto_accident_significant_injury_notes").isJsonNull()) && !jsonObj.get("auto_accident_significant_injury_notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_significant_injury_notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_significant_injury_notes").toString()));
      }
      if ((jsonObj.get("auto_accident_similar_condition_date") != null && !jsonObj.get("auto_accident_similar_condition_date").isJsonNull()) && !jsonObj.get("auto_accident_similar_condition_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_similar_condition_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_similar_condition_date").toString()));
      }
      if ((jsonObj.get("auto_accident_similar_condition_notes") != null && !jsonObj.get("auto_accident_similar_condition_notes").isJsonNull()) && !jsonObj.get("auto_accident_similar_condition_notes").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_similar_condition_notes` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_similar_condition_notes").toString()));
      }
      if ((jsonObj.get("auto_accident_state_of_occurrence") != null && !jsonObj.get("auto_accident_state_of_occurrence").isJsonNull()) && !jsonObj.get("auto_accident_state_of_occurrence").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_state_of_occurrence` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_state_of_occurrence").toString()));
      }
      // validate the optional field `auto_accident_state_of_occurrence`
      if (jsonObj.get("auto_accident_state_of_occurrence") != null && !jsonObj.get("auto_accident_state_of_occurrence").isJsonNull()) {
        AutoAccidentStateOfOccurrenceEnum.validateJsonElement(jsonObj.get("auto_accident_state_of_occurrence"));
      }
      if ((jsonObj.get("auto_accident_subscriber_address") != null && !jsonObj.get("auto_accident_subscriber_address").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_address").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_city") != null && !jsonObj.get("auto_accident_subscriber_city").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_city").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_date_of_birth") != null && !jsonObj.get("auto_accident_subscriber_date_of_birth").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_date_of_birth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_date_of_birth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_date_of_birth").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_first_name") != null && !jsonObj.get("auto_accident_subscriber_first_name").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_first_name").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_last_name") != null && !jsonObj.get("auto_accident_subscriber_last_name").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_last_name").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_middle_name") != null && !jsonObj.get("auto_accident_subscriber_middle_name").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_middle_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_middle_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_middle_name").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_phone_number") != null && !jsonObj.get("auto_accident_subscriber_phone_number").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_phone_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_phone_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_phone_number").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_social_security") != null && !jsonObj.get("auto_accident_subscriber_social_security").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_social_security").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_social_security` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_social_security").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_state") != null && !jsonObj.get("auto_accident_subscriber_state").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_state").toString()));
      }
      // validate the optional field `auto_accident_subscriber_state`
      if (jsonObj.get("auto_accident_subscriber_state") != null && !jsonObj.get("auto_accident_subscriber_state").isJsonNull()) {
        AutoAccidentSubscriberStateEnum.validateJsonElement(jsonObj.get("auto_accident_subscriber_state"));
      }
      if ((jsonObj.get("auto_accident_subscriber_suffix") != null && !jsonObj.get("auto_accident_subscriber_suffix").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_suffix").toString()));
      }
      if ((jsonObj.get("auto_accident_subscriber_zip_code") != null && !jsonObj.get("auto_accident_subscriber_zip_code").isJsonNull()) && !jsonObj.get("auto_accident_subscriber_zip_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_subscriber_zip_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_subscriber_zip_code").toString()));
      }
      if ((jsonObj.get("auto_accident_treatment_duration") != null && !jsonObj.get("auto_accident_treatment_duration").isJsonNull()) && !jsonObj.get("auto_accident_treatment_duration").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_treatment_duration` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_treatment_duration").toString()));
      }
      if ((jsonObj.get("auto_accident_will_require_therapy_rec") != null && !jsonObj.get("auto_accident_will_require_therapy_rec").isJsonNull()) && !jsonObj.get("auto_accident_will_require_therapy_rec").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `auto_accident_will_require_therapy_rec` to be a primitive type in the JSON string but got `%s`", jsonObj.get("auto_accident_will_require_therapy_rec").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AutoAccidentInsurance.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AutoAccidentInsurance' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AutoAccidentInsurance> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AutoAccidentInsurance.class));

       return (TypeAdapter<T>) new TypeAdapter<AutoAccidentInsurance>() {
           @Override
           public void write(JsonWriter out, AutoAccidentInsurance value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AutoAccidentInsurance read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AutoAccidentInsurance given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AutoAccidentInsurance
   * @throws IOException if the JSON string is invalid with respect to AutoAccidentInsurance
   */
  public static AutoAccidentInsurance fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AutoAccidentInsurance.class);
  }

  /**
   * Convert an instance of AutoAccidentInsurance to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

