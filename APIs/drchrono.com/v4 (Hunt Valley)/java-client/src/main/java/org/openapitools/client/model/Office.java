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
import org.openapitools.client.model.OfficeOnlineHours;

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
 * Office
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Office {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private String address;

  public static final String SERIALIZED_NAME_ARCHIVED = "archived";
  @SerializedName(SERIALIZED_NAME_ARCHIVED)
  private Boolean archived;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  /**
   * Two-letter country code
   */
  @JsonAdapter(CountryEnum.Adapter.class)
  public enum CountryEnum {
    EMPTY(""),
    
    AF("AF"),
    
    AX("AX"),
    
    AL("AL"),
    
    DZ("DZ"),
    
    AS("AS"),
    
    AD("AD"),
    
    AO("AO"),
    
    AI("AI"),
    
    AQ("AQ"),
    
    AG("AG"),
    
    AR("AR"),
    
    AM("AM"),
    
    AW("AW"),
    
    AU("AU"),
    
    AT("AT"),
    
    AZ("AZ"),
    
    BS("BS"),
    
    BH("BH"),
    
    BD("BD"),
    
    BB("BB"),
    
    BY("BY"),
    
    BE("BE"),
    
    BZ("BZ"),
    
    BJ("BJ"),
    
    BM("BM"),
    
    BT("BT"),
    
    BO("BO"),
    
    BQ("BQ"),
    
    BA("BA"),
    
    BW("BW"),
    
    BV("BV"),
    
    BR("BR"),
    
    IO("IO"),
    
    BN("BN"),
    
    BG("BG"),
    
    BF("BF"),
    
    BI("BI"),
    
    KH("KH"),
    
    CM("CM"),
    
    CA("CA"),
    
    CV("CV"),
    
    KY("KY"),
    
    CF("CF"),
    
    TD("TD"),
    
    CL("CL"),
    
    CN("CN"),
    
    CX("CX"),
    
    CC("CC"),
    
    CO("CO"),
    
    KM("KM"),
    
    CG("CG"),
    
    CD("CD"),
    
    CK("CK"),
    
    CR("CR"),
    
    CI("CI"),
    
    HR("HR"),
    
    CU("CU"),
    
    CW("CW"),
    
    CY("CY"),
    
    CZ("CZ"),
    
    CYM("CYM"),
    
    DK("DK"),
    
    DJ("DJ"),
    
    DM("DM"),
    
    DO("DO"),
    
    EC("EC"),
    
    EG("EG"),
    
    SV("SV"),
    
    GQ("GQ"),
    
    ER("ER"),
    
    EE("EE"),
    
    ET("ET"),
    
    FK("FK"),
    
    FO("FO"),
    
    FJ("FJ"),
    
    FI("FI"),
    
    FR("FR"),
    
    GF("GF"),
    
    PF("PF"),
    
    TF("TF"),
    
    GA("GA"),
    
    GM("GM"),
    
    GE("GE"),
    
    DE("DE"),
    
    GH("GH"),
    
    GI("GI"),
    
    GR("GR"),
    
    GL("GL"),
    
    GD("GD"),
    
    GP("GP"),
    
    GU("GU"),
    
    GT("GT"),
    
    GG("GG"),
    
    GN("GN"),
    
    GW("GW"),
    
    GY("GY"),
    
    HT("HT"),
    
    HM("HM"),
    
    VA("VA"),
    
    HN("HN"),
    
    HK("HK"),
    
    HU("HU"),
    
    IS("IS"),
    
    IN("IN"),
    
    ID("ID"),
    
    IR("IR"),
    
    IQ("IQ"),
    
    IE("IE"),
    
    IM("IM"),
    
    IL("IL"),
    
    IT("IT"),
    
    JM("JM"),
    
    JP("JP"),
    
    JE("JE"),
    
    JO("JO"),
    
    KZ("KZ"),
    
    KE("KE"),
    
    KI("KI"),
    
    KP("KP"),
    
    KR("KR"),
    
    XK("XK"),
    
    KW("KW"),
    
    KG("KG"),
    
    LA("LA"),
    
    LV("LV"),
    
    LB("LB"),
    
    LS("LS"),
    
    LR("LR"),
    
    LY("LY"),
    
    LI("LI"),
    
    LT("LT"),
    
    LU("LU"),
    
    MO("MO"),
    
    MK("MK"),
    
    MG("MG"),
    
    MW("MW"),
    
    MY("MY"),
    
    MV("MV"),
    
    ML("ML"),
    
    MT("MT"),
    
    MH("MH"),
    
    MQ("MQ"),
    
    MR("MR"),
    
    MU("MU"),
    
    YT("YT"),
    
    MX("MX"),
    
    FM("FM"),
    
    MD("MD"),
    
    MC("MC"),
    
    MN("MN"),
    
    ME("ME"),
    
    MS("MS"),
    
    MA("MA"),
    
    MZ("MZ"),
    
    MM("MM"),
    
    NA("NA"),
    
    NR("NR"),
    
    NP("NP"),
    
    NL("NL"),
    
    NC("NC"),
    
    NZ("NZ"),
    
    NI("NI"),
    
    NE("NE"),
    
    NG("NG"),
    
    NU("NU"),
    
    NF("NF"),
    
    MP("MP"),
    
    FALSE("false"),
    
    OM("OM"),
    
    PK("PK"),
    
    PW("PW"),
    
    PS("PS"),
    
    PA("PA"),
    
    PG("PG"),
    
    PY("PY"),
    
    PE("PE"),
    
    PH("PH"),
    
    PN("PN"),
    
    PL("PL"),
    
    PT("PT"),
    
    PR("PR"),
    
    QA("QA"),
    
    RE("RE"),
    
    RO("RO"),
    
    RU("RU"),
    
    RW("RW"),
    
    BL("BL"),
    
    SH("SH"),
    
    KN("KN"),
    
    LC("LC"),
    
    MF("MF"),
    
    PM("PM"),
    
    VC("VC"),
    
    WS("WS"),
    
    SM("SM"),
    
    ST("ST"),
    
    SA("SA"),
    
    SN("SN"),
    
    RS("RS"),
    
    SC("SC"),
    
    SL("SL"),
    
    SG("SG"),
    
    SX("SX"),
    
    SK("SK"),
    
    SI("SI"),
    
    SB("SB"),
    
    SO("SO"),
    
    ZA("ZA"),
    
    GS("GS"),
    
    SS("SS"),
    
    ES("ES"),
    
    LK("LK"),
    
    SD("SD"),
    
    SR("SR"),
    
    SJ("SJ"),
    
    SZ("SZ"),
    
    SE("SE"),
    
    CH("CH"),
    
    SY("SY"),
    
    TW("TW"),
    
    TJ("TJ"),
    
    TZ("TZ"),
    
    TH("TH"),
    
    TL("TL"),
    
    TG("TG"),
    
    TK("TK"),
    
    TO("TO"),
    
    TT("TT"),
    
    TN("TN"),
    
    TR("TR"),
    
    TM("TM"),
    
    TC("TC"),
    
    TV("TV"),
    
    UG("UG"),
    
    UA("UA"),
    
    AE("AE"),
    
    GB("GB"),
    
    US("US"),
    
    UM("UM"),
    
    UY("UY"),
    
    UZ("UZ"),
    
    VU("VU"),
    
    VE("VE"),
    
    VN("VN"),
    
    VG("VG"),
    
    VI("VI"),
    
    WF("WF"),
    
    EH("EH"),
    
    YE("YE"),
    
    ZM("ZM"),
    
    ZW("ZW");

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

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private String doctor;

  public static final String SERIALIZED_NAME_END_TIME = "end_time";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private String endTime;

  public static final String SERIALIZED_NAME_EXAM_ROOMS = "exam_rooms";
  @SerializedName(SERIALIZED_NAME_EXAM_ROOMS)
  private String examRooms;

  public static final String SERIALIZED_NAME_FAX_NUMBER = "fax_number";
  @SerializedName(SERIALIZED_NAME_FAX_NUMBER)
  private String faxNumber;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_ONLINE_SCHEDULING = "online_scheduling";
  @SerializedName(SERIALIZED_NAME_ONLINE_SCHEDULING)
  private Boolean onlineScheduling;

  public static final String SERIALIZED_NAME_ONLINE_TIMESLOTS = "online_timeslots";
  @SerializedName(SERIALIZED_NAME_ONLINE_TIMESLOTS)
  private List<OfficeOnlineHours> onlineTimeslots = new ArrayList<>();

  public static final String SERIALIZED_NAME_PHONE_NUMBER = "phone_number";
  @SerializedName(SERIALIZED_NAME_PHONE_NUMBER)
  private String phoneNumber;

  public static final String SERIALIZED_NAME_START_TIME = "start_time";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private String startTime;

  /**
   * Two-letter abbreviation
   */
  @JsonAdapter(StateEnum.Adapter.class)
  public enum StateEnum {
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

    StateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StateEnum fromValue(String value) {
      for (StateEnum b : StateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private StateEnum state;

  public static final String SERIALIZED_NAME_TAX_ID_NUMBER_PROFESSIONAL = "tax_id_number_professional";
  @SerializedName(SERIALIZED_NAME_TAX_ID_NUMBER_PROFESSIONAL)
  private String taxIdNumberProfessional;

  public static final String SERIALIZED_NAME_ZIP_CODE = "zip_code";
  @SerializedName(SERIALIZED_NAME_ZIP_CODE)
  private String zipCode;

  public Office() {
  }

  public Office(
     String address, 
     String city, 
     CountryEnum country, 
     String doctor, 
     String examRooms, 
     String faxNumber, 
     Integer id, 
     String name, 
     String phoneNumber, 
     StateEnum state, 
     String taxIdNumberProfessional, 
     String zipCode
  ) {
    this();
    this.address = address;
    this.city = city;
    this.country = country;
    this.doctor = doctor;
    this.examRooms = examRooms;
    this.faxNumber = faxNumber;
    this.id = id;
    this.name = name;
    this.phoneNumber = phoneNumber;
    this.state = state;
    this.taxIdNumberProfessional = taxIdNumberProfessional;
    this.zipCode = zipCode;
  }

  /**
   * 
   * @return address
   */
  @javax.annotation.Nullable
  public String getAddress() {
    return address;
  }



  public Office archived(Boolean archived) {
    this.archived = archived;
    return this;
  }

  /**
   * Indicates that the object has been soft-deleted and should not be used
   * @return archived
   */
  @javax.annotation.Nullable
  public Boolean getArchived() {
    return archived;
  }

  public void setArchived(Boolean archived) {
    this.archived = archived;
  }


  /**
   * 
   * @return city
   */
  @javax.annotation.Nullable
  public String getCity() {
    return city;
  }



  /**
   * Two-letter country code
   * @return country
   */
  @javax.annotation.Nullable
  public CountryEnum getCountry() {
    return country;
  }



  /**
   * ID of the doctor who owns the office
   * @return doctor
   */
  @javax.annotation.Nullable
  public String getDoctor() {
    return doctor;
  }



  public Office endTime(String endTime) {
    this.endTime = endTime;
    return this;
  }

  /**
   * Truncated to the hour. Default is &#x60;24:00&#x60;
   * @return endTime
   */
  @javax.annotation.Nullable
  public String getEndTime() {
    return endTime;
  }

  public void setEndTime(String endTime) {
    this.endTime = endTime;
  }


  /**
   * 
   * @return examRooms
   */
  @javax.annotation.Nullable
  public String getExamRooms() {
    return examRooms;
  }



  /**
   * 
   * @return faxNumber
   */
  @javax.annotation.Nullable
  public String getFaxNumber() {
    return faxNumber;
  }



  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  /**
   * 
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }



  public Office onlineScheduling(Boolean onlineScheduling) {
    this.onlineScheduling = onlineScheduling;
    return this;
  }

  /**
   * Default is &#x60;false&#x60;
   * @return onlineScheduling
   */
  @javax.annotation.Nullable
  public Boolean getOnlineScheduling() {
    return onlineScheduling;
  }

  public void setOnlineScheduling(Boolean onlineScheduling) {
    this.onlineScheduling = onlineScheduling;
  }


  public Office onlineTimeslots(List<OfficeOnlineHours> onlineTimeslots) {
    this.onlineTimeslots = onlineTimeslots;
    return this;
  }

  public Office addOnlineTimeslotsItem(OfficeOnlineHours onlineTimeslotsItem) {
    if (this.onlineTimeslots == null) {
      this.onlineTimeslots = new ArrayList<>();
    }
    this.onlineTimeslots.add(onlineTimeslotsItem);
    return this;
  }

  /**
   * Array of timslots
   * @return onlineTimeslots
   */
  @javax.annotation.Nullable
  public List<OfficeOnlineHours> getOnlineTimeslots() {
    return onlineTimeslots;
  }

  public void setOnlineTimeslots(List<OfficeOnlineHours> onlineTimeslots) {
    this.onlineTimeslots = onlineTimeslots;
  }


  /**
   * 
   * @return phoneNumber
   */
  @javax.annotation.Nullable
  public String getPhoneNumber() {
    return phoneNumber;
  }



  public Office startTime(String startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Truncated to the hour. Default is &#x60;00:00:00&#x60;
   * @return startTime
   */
  @javax.annotation.Nullable
  public String getStartTime() {
    return startTime;
  }

  public void setStartTime(String startTime) {
    this.startTime = startTime;
  }


  /**
   * Two-letter abbreviation
   * @return state
   */
  @javax.annotation.Nullable
  public StateEnum getState() {
    return state;
  }



  /**
   * Billing Tax ID #
   * @return taxIdNumberProfessional
   */
  @javax.annotation.Nullable
  public String getTaxIdNumberProfessional() {
    return taxIdNumberProfessional;
  }



  /**
   * 
   * @return zipCode
   */
  @javax.annotation.Nullable
  public String getZipCode() {
    return zipCode;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Office office = (Office) o;
    return Objects.equals(this.address, office.address) &&
        Objects.equals(this.archived, office.archived) &&
        Objects.equals(this.city, office.city) &&
        Objects.equals(this.country, office.country) &&
        Objects.equals(this.doctor, office.doctor) &&
        Objects.equals(this.endTime, office.endTime) &&
        Objects.equals(this.examRooms, office.examRooms) &&
        Objects.equals(this.faxNumber, office.faxNumber) &&
        Objects.equals(this.id, office.id) &&
        Objects.equals(this.name, office.name) &&
        Objects.equals(this.onlineScheduling, office.onlineScheduling) &&
        Objects.equals(this.onlineTimeslots, office.onlineTimeslots) &&
        Objects.equals(this.phoneNumber, office.phoneNumber) &&
        Objects.equals(this.startTime, office.startTime) &&
        Objects.equals(this.state, office.state) &&
        Objects.equals(this.taxIdNumberProfessional, office.taxIdNumberProfessional) &&
        Objects.equals(this.zipCode, office.zipCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, archived, city, country, doctor, endTime, examRooms, faxNumber, id, name, onlineScheduling, onlineTimeslots, phoneNumber, startTime, state, taxIdNumberProfessional, zipCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Office {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    archived: ").append(toIndentedString(archived)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    examRooms: ").append(toIndentedString(examRooms)).append("\n");
    sb.append("    faxNumber: ").append(toIndentedString(faxNumber)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    onlineScheduling: ").append(toIndentedString(onlineScheduling)).append("\n");
    sb.append("    onlineTimeslots: ").append(toIndentedString(onlineTimeslots)).append("\n");
    sb.append("    phoneNumber: ").append(toIndentedString(phoneNumber)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    taxIdNumberProfessional: ").append(toIndentedString(taxIdNumberProfessional)).append("\n");
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
    openapiFields.add("archived");
    openapiFields.add("city");
    openapiFields.add("country");
    openapiFields.add("doctor");
    openapiFields.add("end_time");
    openapiFields.add("exam_rooms");
    openapiFields.add("fax_number");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("online_scheduling");
    openapiFields.add("online_timeslots");
    openapiFields.add("phone_number");
    openapiFields.add("start_time");
    openapiFields.add("state");
    openapiFields.add("tax_id_number_professional");
    openapiFields.add("zip_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Office
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Office.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Office is not found in the empty JSON string", Office.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Office.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Office` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) && !jsonObj.get("address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("address").toString()));
      }
      if ((jsonObj.get("city") != null && !jsonObj.get("city").isJsonNull()) && !jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if ((jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) && !jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      // validate the optional field `country`
      if (jsonObj.get("country") != null && !jsonObj.get("country").isJsonNull()) {
        CountryEnum.validateJsonElement(jsonObj.get("country"));
      }
      if ((jsonObj.get("doctor") != null && !jsonObj.get("doctor").isJsonNull()) && !jsonObj.get("doctor").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `doctor` to be a primitive type in the JSON string but got `%s`", jsonObj.get("doctor").toString()));
      }
      if ((jsonObj.get("end_time") != null && !jsonObj.get("end_time").isJsonNull()) && !jsonObj.get("end_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("end_time").toString()));
      }
      if ((jsonObj.get("exam_rooms") != null && !jsonObj.get("exam_rooms").isJsonNull()) && !jsonObj.get("exam_rooms").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `exam_rooms` to be a primitive type in the JSON string but got `%s`", jsonObj.get("exam_rooms").toString()));
      }
      if ((jsonObj.get("fax_number") != null && !jsonObj.get("fax_number").isJsonNull()) && !jsonObj.get("fax_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fax_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fax_number").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("online_timeslots") != null && !jsonObj.get("online_timeslots").isJsonNull()) {
        JsonArray jsonArrayonlineTimeslots = jsonObj.getAsJsonArray("online_timeslots");
        if (jsonArrayonlineTimeslots != null) {
          // ensure the json data is an array
          if (!jsonObj.get("online_timeslots").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `online_timeslots` to be an array in the JSON string but got `%s`", jsonObj.get("online_timeslots").toString()));
          }

          // validate the optional field `online_timeslots` (array)
          for (int i = 0; i < jsonArrayonlineTimeslots.size(); i++) {
            OfficeOnlineHours.validateJsonElement(jsonArrayonlineTimeslots.get(i));
          };
        }
      }
      if ((jsonObj.get("phone_number") != null && !jsonObj.get("phone_number").isJsonNull()) && !jsonObj.get("phone_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone_number").toString()));
      }
      if ((jsonObj.get("start_time") != null && !jsonObj.get("start_time").isJsonNull()) && !jsonObj.get("start_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `start_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("start_time").toString()));
      }
      if ((jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) && !jsonObj.get("state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("state").toString()));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        StateEnum.validateJsonElement(jsonObj.get("state"));
      }
      if ((jsonObj.get("tax_id_number_professional") != null && !jsonObj.get("tax_id_number_professional").isJsonNull()) && !jsonObj.get("tax_id_number_professional").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tax_id_number_professional` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tax_id_number_professional").toString()));
      }
      if ((jsonObj.get("zip_code") != null && !jsonObj.get("zip_code").isJsonNull()) && !jsonObj.get("zip_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `zip_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("zip_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Office.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Office' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Office> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Office.class));

       return (TypeAdapter<T>) new TypeAdapter<Office>() {
           @Override
           public void write(JsonWriter out, Office value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Office read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Office given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Office
   * @throws IOException if the JSON string is invalid with respect to Office
   */
  public static Office fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Office.class);
  }

  /**
   * Convert an instance of Office to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

