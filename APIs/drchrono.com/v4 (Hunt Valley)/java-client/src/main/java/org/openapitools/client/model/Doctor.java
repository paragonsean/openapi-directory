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
 * Doctor
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Doctor {
  public static final String SERIALIZED_NAME_CELL_PHONE = "cell_phone";
  @SerializedName(SERIALIZED_NAME_CELL_PHONE)
  private String cellPhone;

  /**
   * Two-letter conutry code. Default is &#x60;US&#x60;
   */
  @JsonAdapter(CountryEnum.Adapter.class)
  public enum CountryEnum {
    BD("BD"),
    
    WF("WF"),
    
    BF("BF"),
    
    BG("BG"),
    
    BA("BA"),
    
    BB("BB"),
    
    BE("BE"),
    
    BL("BL"),
    
    BM("BM"),
    
    BN("BN"),
    
    BO("BO"),
    
    JP("JP"),
    
    BI("BI"),
    
    BJ("BJ"),
    
    BT("BT"),
    
    JM("JM"),
    
    BV("BV"),
    
    JO("JO"),
    
    WS("WS"),
    
    BQ("BQ"),
    
    BR("BR"),
    
    BS("BS"),
    
    JE("JE"),
    
    BY("BY"),
    
    BZ("BZ"),
    
    RU("RU"),
    
    RW("RW"),
    
    RS("RS"),
    
    TL("TL"),
    
    RE("RE"),
    
    TM("TM"),
    
    TJ("TJ"),
    
    RO("RO"),
    
    TK("TK"),
    
    GW("GW"),
    
    GU("GU"),
    
    GT("GT"),
    
    GS("GS"),
    
    GR("GR"),
    
    GQ("GQ"),
    
    GP("GP"),
    
    BH("BH"),
    
    GY("GY"),
    
    GG("GG"),
    
    GF("GF"),
    
    GE("GE"),
    
    GD("GD"),
    
    GB("GB"),
    
    GA("GA"),
    
    GN("GN"),
    
    GM("GM"),
    
    GL("GL"),
    
    KW("KW"),
    
    GI("GI"),
    
    GH("GH"),
    
    OM("OM"),
    
    TN("TN"),
    
    BW("BW"),
    
    HR("HR"),
    
    HT("HT"),
    
    HU("HU"),
    
    HK("HK"),
    
    HN("HN"),
    
    HM("HM"),
    
    KR("KR"),
    
    AD("AD"),
    
    PR("PR"),
    
    PS("PS"),
    
    PW("PW"),
    
    PT("PT"),
    
    KN("KN"),
    
    PY("PY"),
    
    AI("AI"),
    
    PA("PA"),
    
    PF("PF"),
    
    PG("PG"),
    
    PE("PE"),
    
    PK("PK"),
    
    PH("PH"),
    
    PN("PN"),
    
    PL("PL"),
    
    PM("PM"),
    
    ZM("ZM"),
    
    EH("EH"),
    
    EE("EE"),
    
    EG("EG"),
    
    ZA("ZA"),
    
    EC("EC"),
    
    AL("AL"),
    
    AO("AO"),
    
    KZ("KZ"),
    
    ET("ET"),
    
    ZW("ZW"),
    
    KY("KY"),
    
    ES("ES"),
    
    ER("ER"),
    
    ME("ME"),
    
    MD("MD"),
    
    MG("MG"),
    
    MF("MF"),
    
    MA("MA"),
    
    MC("MC"),
    
    UZ("UZ"),
    
    MM("MM"),
    
    ML("ML"),
    
    MO("MO"),
    
    MN("MN"),
    
    MH("MH"),
    
    MK("MK"),
    
    MU("MU"),
    
    MT("MT"),
    
    MW("MW"),
    
    MV("MV"),
    
    MQ("MQ"),
    
    MP("MP"),
    
    MS("MS"),
    
    MR("MR"),
    
    AU("AU"),
    
    UG("UG"),
    
    MY("MY"),
    
    MX("MX"),
    
    MZ("MZ"),
    
    FR("FR"),
    
    AW("AW"),
    
    AF("AF"),
    
    AX("AX"),
    
    FI("FI"),
    
    FJ("FJ"),
    
    FK("FK"),
    
    FM("FM"),
    
    FO("FO"),
    
    NI("NI"),
    
    NL("NL"),
    
    FALSE("false"),
    
    NA("NA"),
    
    VU("VU"),
    
    NC("NC"),
    
    NE("NE"),
    
    NF("NF"),
    
    NG("NG"),
    
    NZ("NZ"),
    
    NP("NP"),
    
    NR("NR"),
    
    NU("NU"),
    
    CK("CK"),
    
    CI("CI"),
    
    CH("CH"),
    
    CO("CO"),
    
    CN("CN"),
    
    CM("CM"),
    
    CL("CL"),
    
    CC("CC"),
    
    CA("CA"),
    
    CG("CG"),
    
    CF("CF"),
    
    CD("CD"),
    
    CZ("CZ"),
    
    CY("CY"),
    
    CX("CX"),
    
    CR("CR"),
    
    KP("KP"),
    
    CW("CW"),
    
    CV("CV"),
    
    CU("CU"),
    
    SZ("SZ"),
    
    SY("SY"),
    
    SX("SX"),
    
    KG("KG"),
    
    KE("KE"),
    
    SS("SS"),
    
    SR("SR"),
    
    KI("KI"),
    
    KH("KH"),
    
    SV("SV"),
    
    KM("KM"),
    
    ST("ST"),
    
    SK("SK"),
    
    SJ("SJ"),
    
    SI("SI"),
    
    SH("SH"),
    
    SO("SO"),
    
    SN("SN"),
    
    SM("SM"),
    
    SL("SL"),
    
    SC("SC"),
    
    SB("SB"),
    
    SA("SA"),
    
    SG("SG"),
    
    SE("SE"),
    
    SD("SD"),
    
    DO("DO"),
    
    DM("DM"),
    
    DJ("DJ"),
    
    DK("DK"),
    
    DE("DE"),
    
    YE("YE"),
    
    AT("AT"),
    
    DZ("DZ"),
    
    US("US"),
    
    UY("UY"),
    
    YT("YT"),
    
    UM("UM"),
    
    LB("LB"),
    
    LC("LC"),
    
    LA("LA"),
    
    TV("TV"),
    
    TW("TW"),
    
    TT("TT"),
    
    TR("TR"),
    
    LK("LK"),
    
    LI("LI"),
    
    LV("LV"),
    
    TO("TO"),
    
    LT("LT"),
    
    LU("LU"),
    
    LR("LR"),
    
    LS("LS"),
    
    TH("TH"),
    
    TF("TF"),
    
    TG("TG"),
    
    TD("TD"),
    
    TC("TC"),
    
    LY("LY"),
    
    VA("VA"),
    
    VC("VC"),
    
    AE("AE"),
    
    VE("VE"),
    
    AG("AG"),
    
    VG("VG"),
    
    IQ("IQ"),
    
    VI("VI"),
    
    IS("IS"),
    
    IR("IR"),
    
    AM("AM"),
    
    IT("IT"),
    
    VN("VN"),
    
    AQ("AQ"),
    
    AS("AS"),
    
    AR("AR"),
    
    IM("IM"),
    
    IL("IL"),
    
    IO("IO"),
    
    IN("IN"),
    
    TZ("TZ"),
    
    AZ("AZ"),
    
    IE("IE"),
    
    ID("ID"),
    
    UA("UA"),
    
    QA("QA");

    private String value;

    CountryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CountryEnum fromValue(String value) {
      for (CountryEnum b : CountryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CountryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CountryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CountryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CountryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CountryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private CountryEnum country;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_FIRST_NAME = "first_name";
  @SerializedName(SERIALIZED_NAME_FIRST_NAME)
  private String firstName;

  public static final String SERIALIZED_NAME_GROUP_NPI_NUMBER = "group_npi_number";
  @SerializedName(SERIALIZED_NAME_GROUP_NPI_NUMBER)
  private String groupNpiNumber;

  public static final String SERIALIZED_NAME_HOME_PHONE = "home_phone";
  @SerializedName(SERIALIZED_NAME_HOME_PHONE)
  private String homePhone;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_ACCOUNT_SUSPENDED = "is_account_suspended";
  @SerializedName(SERIALIZED_NAME_IS_ACCOUNT_SUSPENDED)
  private Boolean isAccountSuspended;

  /**
   * 
   */
  @JsonAdapter(JobTitleEnum.Adapter.class)
  public enum JobTitleEnum {
    EMPTY(""),
    
    PROVIDER_STAFF_PRIVATE_PRACTICE_("Provider/Staff (Private Practice)"),
    
    PROVIDER_STAFF_HOSPITAL_("Provider/Staff (Hospital)"),
    
    PATIENTS_INTERVIEW_CANDIDATE("Patients/Interview Candidate"),
    
    EDUCATOR_STUDENT("Educator/Student"),
    
    API_DEVELOPER("API/Developer"),
    
    CONSULTANT("Consultant"),
    
    OTHER("Other");

    private String value;

    JobTitleEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static JobTitleEnum fromValue(String value) {
      for (JobTitleEnum b : JobTitleEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<JobTitleEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final JobTitleEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public JobTitleEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return JobTitleEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      JobTitleEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_JOB_TITLE = "job_title";
  @SerializedName(SERIALIZED_NAME_JOB_TITLE)
  private JobTitleEnum jobTitle;

  public static final String SERIALIZED_NAME_LAST_NAME = "last_name";
  @SerializedName(SERIALIZED_NAME_LAST_NAME)
  private String lastName;

  public static final String SERIALIZED_NAME_NPI_NUMBER = "npi_number";
  @SerializedName(SERIALIZED_NAME_NPI_NUMBER)
  private String npiNumber;

  public static final String SERIALIZED_NAME_OFFICE_PHONE = "office_phone";
  @SerializedName(SERIALIZED_NAME_OFFICE_PHONE)
  private String officePhone;

  public static final String SERIALIZED_NAME_PRACTICE_GROUP = "practice_group";
  @SerializedName(SERIALIZED_NAME_PRACTICE_GROUP)
  private String practiceGroup;

  public static final String SERIALIZED_NAME_PRACTICE_GROUP_NAME = "practice_group_name";
  @SerializedName(SERIALIZED_NAME_PRACTICE_GROUP_NAME)
  private String practiceGroupName;

  public static final String SERIALIZED_NAME_PROFILE_PICTURE = "profile_picture";
  @SerializedName(SERIALIZED_NAME_PROFILE_PICTURE)
  private String profilePicture;

  public static final String SERIALIZED_NAME_SPECIALTY = "specialty";
  @SerializedName(SERIALIZED_NAME_SPECIALTY)
  private String specialty;

  public static final String SERIALIZED_NAME_SUFFIX = "suffix";
  @SerializedName(SERIALIZED_NAME_SUFFIX)
  private String suffix;

  public static final String SERIALIZED_NAME_TIMEZONE = "timezone";
  @SerializedName(SERIALIZED_NAME_TIMEZONE)
  private String timezone;

  public static final String SERIALIZED_NAME_WEBSITE = "website";
  @SerializedName(SERIALIZED_NAME_WEBSITE)
  private String website;

  public Doctor() {
  }

  public Doctor(
     String email, 
     Integer id, 
     String practiceGroup, 
     String practiceGroupName, 
     String profilePicture
  ) {
    this();
    this.email = email;
    this.id = id;
    this.practiceGroup = practiceGroup;
    this.practiceGroupName = practiceGroupName;
    this.profilePicture = profilePicture;
  }

  public Doctor cellPhone(String cellPhone) {
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


  public Doctor country(CountryEnum country) {
    this.country = country;
    return this;
  }

  /**
   * Two-letter conutry code. Default is &#x60;US&#x60;
   * @return country
   */
  @javax.annotation.Nullable
  public CountryEnum getCountry() {
    return country;
  }

  public void setCountry(CountryEnum country) {
    this.country = country;
  }


  /**
   * 
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }



  public Doctor firstName(String firstName) {
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


  public Doctor groupNpiNumber(String groupNpiNumber) {
    this.groupNpiNumber = groupNpiNumber;
    return this;
  }

  /**
   * 
   * @return groupNpiNumber
   */
  @javax.annotation.Nullable
  public String getGroupNpiNumber() {
    return groupNpiNumber;
  }

  public void setGroupNpiNumber(String groupNpiNumber) {
    this.groupNpiNumber = groupNpiNumber;
  }


  public Doctor homePhone(String homePhone) {
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



  public Doctor isAccountSuspended(Boolean isAccountSuspended) {
    this.isAccountSuspended = isAccountSuspended;
    return this;
  }

  /**
   * Indicates the doctor&#39;s account is suspended or not
   * @return isAccountSuspended
   */
  @javax.annotation.Nullable
  public Boolean getIsAccountSuspended() {
    return isAccountSuspended;
  }

  public void setIsAccountSuspended(Boolean isAccountSuspended) {
    this.isAccountSuspended = isAccountSuspended;
  }


  public Doctor jobTitle(JobTitleEnum jobTitle) {
    this.jobTitle = jobTitle;
    return this;
  }

  /**
   * 
   * @return jobTitle
   */
  @javax.annotation.Nullable
  public JobTitleEnum getJobTitle() {
    return jobTitle;
  }

  public void setJobTitle(JobTitleEnum jobTitle) {
    this.jobTitle = jobTitle;
  }


  public Doctor lastName(String lastName) {
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


  public Doctor npiNumber(String npiNumber) {
    this.npiNumber = npiNumber;
    return this;
  }

  /**
   * If both this field and &#x60;group_npi_number&#x60; are set, prefer this field
   * @return npiNumber
   */
  @javax.annotation.Nullable
  public String getNpiNumber() {
    return npiNumber;
  }

  public void setNpiNumber(String npiNumber) {
    this.npiNumber = npiNumber;
  }


  public Doctor officePhone(String officePhone) {
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


  /**
   * The ID of the practice group this user belongs to. This can be used to identify users in the same practice.
   * @return practiceGroup
   */
  @javax.annotation.Nullable
  public String getPracticeGroup() {
    return practiceGroup;
  }



  /**
   * 
   * @return practiceGroupName
   */
  @javax.annotation.Nullable
  public String getPracticeGroupName() {
    return practiceGroupName;
  }



  /**
   * 
   * @return profilePicture
   */
  @javax.annotation.Nullable
  public String getProfilePicture() {
    return profilePicture;
  }



  public Doctor specialty(String specialty) {
    this.specialty = specialty;
    return this;
  }

  /**
   * 
   * @return specialty
   */
  @javax.annotation.Nullable
  public String getSpecialty() {
    return specialty;
  }

  public void setSpecialty(String specialty) {
    this.specialty = specialty;
  }


  public Doctor suffix(String suffix) {
    this.suffix = suffix;
    return this;
  }

  /**
   * 
   * @return suffix
   */
  @javax.annotation.Nullable
  public String getSuffix() {
    return suffix;
  }

  public void setSuffix(String suffix) {
    this.suffix = suffix;
  }


  public Doctor timezone(String timezone) {
    this.timezone = timezone;
    return this;
  }

  /**
   * 
   * @return timezone
   */
  @javax.annotation.Nullable
  public String getTimezone() {
    return timezone;
  }

  public void setTimezone(String timezone) {
    this.timezone = timezone;
  }


  public Doctor website(String website) {
    this.website = website;
    return this;
  }

  /**
   * 
   * @return website
   */
  @javax.annotation.Nullable
  public String getWebsite() {
    return website;
  }

  public void setWebsite(String website) {
    this.website = website;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Doctor doctor = (Doctor) o;
    return Objects.equals(this.cellPhone, doctor.cellPhone) &&
        Objects.equals(this.country, doctor.country) &&
        Objects.equals(this.email, doctor.email) &&
        Objects.equals(this.firstName, doctor.firstName) &&
        Objects.equals(this.groupNpiNumber, doctor.groupNpiNumber) &&
        Objects.equals(this.homePhone, doctor.homePhone) &&
        Objects.equals(this.id, doctor.id) &&
        Objects.equals(this.isAccountSuspended, doctor.isAccountSuspended) &&
        Objects.equals(this.jobTitle, doctor.jobTitle) &&
        Objects.equals(this.lastName, doctor.lastName) &&
        Objects.equals(this.npiNumber, doctor.npiNumber) &&
        Objects.equals(this.officePhone, doctor.officePhone) &&
        Objects.equals(this.practiceGroup, doctor.practiceGroup) &&
        Objects.equals(this.practiceGroupName, doctor.practiceGroupName) &&
        Objects.equals(this.profilePicture, doctor.profilePicture) &&
        Objects.equals(this.specialty, doctor.specialty) &&
        Objects.equals(this.suffix, doctor.suffix) &&
        Objects.equals(this.timezone, doctor.timezone) &&
        Objects.equals(this.website, doctor.website);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cellPhone, country, email, firstName, groupNpiNumber, homePhone, id, isAccountSuspended, jobTitle, lastName, npiNumber, officePhone, practiceGroup, practiceGroupName, profilePicture, specialty, suffix, timezone, website);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Doctor {\n");
    sb.append("    cellPhone: ").append(toIndentedString(cellPhone)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    firstName: ").append(toIndentedString(firstName)).append("\n");
    sb.append("    groupNpiNumber: ").append(toIndentedString(groupNpiNumber)).append("\n");
    sb.append("    homePhone: ").append(toIndentedString(homePhone)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isAccountSuspended: ").append(toIndentedString(isAccountSuspended)).append("\n");
    sb.append("    jobTitle: ").append(toIndentedString(jobTitle)).append("\n");
    sb.append("    lastName: ").append(toIndentedString(lastName)).append("\n");
    sb.append("    npiNumber: ").append(toIndentedString(npiNumber)).append("\n");
    sb.append("    officePhone: ").append(toIndentedString(officePhone)).append("\n");
    sb.append("    practiceGroup: ").append(toIndentedString(practiceGroup)).append("\n");
    sb.append("    practiceGroupName: ").append(toIndentedString(practiceGroupName)).append("\n");
    sb.append("    profilePicture: ").append(toIndentedString(profilePicture)).append("\n");
    sb.append("    specialty: ").append(toIndentedString(specialty)).append("\n");
    sb.append("    suffix: ").append(toIndentedString(suffix)).append("\n");
    sb.append("    timezone: ").append(toIndentedString(timezone)).append("\n");
    sb.append("    website: ").append(toIndentedString(website)).append("\n");
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
    openapiFields.add("cell_phone");
    openapiFields.add("country");
    openapiFields.add("email");
    openapiFields.add("first_name");
    openapiFields.add("group_npi_number");
    openapiFields.add("home_phone");
    openapiFields.add("id");
    openapiFields.add("is_account_suspended");
    openapiFields.add("job_title");
    openapiFields.add("last_name");
    openapiFields.add("npi_number");
    openapiFields.add("office_phone");
    openapiFields.add("practice_group");
    openapiFields.add("practice_group_name");
    openapiFields.add("profile_picture");
    openapiFields.add("specialty");
    openapiFields.add("suffix");
    openapiFields.add("timezone");
    openapiFields.add("website");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Doctor
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Doctor.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Doctor is not found in the empty JSON string", Doctor.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Doctor.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Doctor` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("cell_phone") != null && !jsonObj.get("cell_phone").isJsonNull()) && !jsonObj.get("cell_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cell_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cell_phone").toString()));
      }
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      // validate the optional field `country`
      if (jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) {
        CountryEnum.validateJsonElement(jsonObj.get("country"));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("first_name") != null && !jsonObj.get("first_name").isJsonNull()) && !jsonObj.get("first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_name").toString()));
      }
      if ((jsonObj.get("group_npi_number") != null && !jsonObj.get("group_npi_number").isJsonNull()) && !jsonObj.get("group_npi_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group_npi_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group_npi_number").toString()));
      }
      if ((jsonObj.get("home_phone") != null && !jsonObj.get("home_phone").isJsonNull()) && !jsonObj.get("home_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `home_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("home_phone").toString()));
      }
      if ((jsonObj.get("job_title") != null && !jsonObj.get("job_title").isJsonNull()) && !jsonObj.get("job_title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `job_title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("job_title").toString()));
      }
      // validate the optional field `job_title`
      if (jsonObj.get("job_title") != null && !jsonObj.get("job_title").isJsonNull()) {
        JobTitleEnum.validateJsonElement(jsonObj.get("job_title"));
      }
      if ((jsonObj.get("last_name") != null && !jsonObj.get("last_name").isJsonNull()) && !jsonObj.get("last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("last_name").toString()));
      }
      if ((jsonObj.get("npi_number") != null && !jsonObj.get("npi_number").isJsonNull()) && !jsonObj.get("npi_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `npi_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("npi_number").toString()));
      }
      if ((jsonObj.get("office_phone") != null && !jsonObj.get("office_phone").isJsonNull()) && !jsonObj.get("office_phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `office_phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("office_phone").toString()));
      }
      if ((jsonObj.get("practice_group") != null && !jsonObj.get("practice_group").isJsonNull()) && !jsonObj.get("practice_group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `practice_group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("practice_group").toString()));
      }
      if ((jsonObj.get("practice_group_name") != null && !jsonObj.get("practice_group_name").isJsonNull()) && !jsonObj.get("practice_group_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `practice_group_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("practice_group_name").toString()));
      }
      if ((jsonObj.get("profile_picture") != null && !jsonObj.get("profile_picture").isJsonNull()) && !jsonObj.get("profile_picture").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profile_picture` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profile_picture").toString()));
      }
      if ((jsonObj.get("specialty") != null && !jsonObj.get("specialty").isJsonNull()) && !jsonObj.get("specialty").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `specialty` to be a primitive type in the JSON string but got `%s`", jsonObj.get("specialty").toString()));
      }
      if ((jsonObj.get("suffix") != null && !jsonObj.get("suffix").isJsonNull()) && !jsonObj.get("suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("suffix").toString()));
      }
      if ((jsonObj.get("timezone") != null && !jsonObj.get("timezone").isJsonNull()) && !jsonObj.get("timezone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `timezone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("timezone").toString()));
      }
      if ((jsonObj.get("website") != null && !jsonObj.get("website").isJsonNull()) && !jsonObj.get("website").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `website` to be a primitive type in the JSON string but got `%s`", jsonObj.get("website").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Doctor.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Doctor' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Doctor> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Doctor.class));

       return (TypeAdapter<T>) new TypeAdapter<Doctor>() {
           @Override
           public void write(JsonWriter out, Doctor value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Doctor read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Doctor given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Doctor
   * @throws IOException if the JSON string is invalid with respect to Doctor
   */
  public static Doctor fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Doctor.class);
  }

  /**
   * Convert an instance of Doctor to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

