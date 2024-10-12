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
 * DoctorFeeSchedule
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DoctorFeeSchedule {
  public static final String SERIALIZED_NAME_ALLOWED_AMOUNT = "allowed_amount";
  @SerializedName(SERIALIZED_NAME_ALLOWED_AMOUNT)
  private BigDecimal allowedAmount;

  public static final String SERIALIZED_NAME_BASE_PRICE = "base_price";
  @SerializedName(SERIALIZED_NAME_BASE_PRICE)
  private BigDecimal basePrice;

  public static final String SERIALIZED_NAME_BILLING_DESCRIPTION = "billing_description";
  @SerializedName(SERIALIZED_NAME_BILLING_DESCRIPTION)
  private String billingDescription;

  public static final String SERIALIZED_NAME_CASH_PRICE = "cash_price";
  @SerializedName(SERIALIZED_NAME_CASH_PRICE)
  private BigDecimal cashPrice;

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  /**
   * 
   */
  @JsonAdapter(CodeTypeEnum.Adapter.class)
  public enum CodeTypeEnum {
    CPT("CPT"),
    
    HCPCS("HCPCS"),
    
    CUSTOM("Custom"),
    
    ICD9("ICD9"),
    
    ICD10("ICD10"),
    
    REVENUE("Revenue");

    private String value;

    CodeTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CodeTypeEnum fromValue(String value) {
      for (CodeTypeEnum b : CodeTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CodeTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CodeTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CodeTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CodeTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CodeTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CODE_TYPE = "code_type";
  @SerializedName(SERIALIZED_NAME_CODE_TYPE)
  private CodeTypeEnum codeType;

  public static final String SERIALIZED_NAME_CPT_HCPCS_MODIFIER1 = "cpt_hcpcs_modifier1";
  @SerializedName(SERIALIZED_NAME_CPT_HCPCS_MODIFIER1)
  private String cptHcpcsModifier1;

  /**
   * 
   */
  @JsonAdapter(CptHcpcsModifier2Enum.Adapter.class)
  public enum CptHcpcsModifier2Enum {
    EMPTY(""),
    
    _17("17"),
    
    _1_D("1D"),
    
    _22("22"),
    
    _23("23"),
    
    _24("24"),
    
    _25("25"),
    
    _26("26"),
    
    _29("29"),
    
    _32("32"),
    
    _33("33"),
    
    _47("47"),
    
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
    
    _62("62"),
    
    _63("63"),
    
    _66("66"),
    
    _73("73"),
    
    _74("74"),
    
    _76("76"),
    
    _77("77"),
    
    _78("78"),
    
    _79("79"),
    
    _80("80"),
    
    _81("81"),
    
    _82("82"),
    
    _83("83"),
    
    _90("90"),
    
    _91("91"),
    
    _92("92"),
    
    _93("93"),
    
    _95("95"),
    
    _96("96"),
    
    _97("97"),
    
    _99("99"),
    
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
    
    AD("AD"),
    
    AE("AE"),
    
    AF("AF"),
    
    AG("AG"),
    
    AH("AH"),
    
    AI("AI"),
    
    AJ("AJ"),
    
    AK("AK"),
    
    AM("AM"),
    
    AO("AO"),
    
    AP("AP"),
    
    AQ("AQ"),
    
    AR("AR"),
    
    AS("AS"),
    
    AT("AT"),
    
    AU("AU"),
    
    AV("AV"),
    
    AW("AW"),
    
    AX("AX"),
    
    AY("AY"),
    
    AZ("AZ"),
    
    BA("BA"),
    
    BL("BL"),
    
    BO("BO"),
    
    BP("BP"),
    
    BR("BR"),
    
    BU("BU"),
    
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
    
    CR("CR"),
    
    CS("CS"),
    
    CT("CT"),
    
    DA("DA"),
    
    E1("E1"),
    
    E2("E2"),
    
    E3("E3"),
    
    E4("E4"),
    
    EA("EA"),
    
    EB("EB"),
    
    EC("EC"),
    
    ED("ED"),
    
    EE("EE"),
    
    EJ("EJ"),
    
    EM("EM"),
    
    EP("EP"),
    
    ER("ER"),
    
    ET("ET"),
    
    EX("EX"),
    
    EY("EY"),
    
    F1("F1"),
    
    F2("F2"),
    
    F3("F3"),
    
    F4("F4"),
    
    F5("F5"),
    
    F6("F6"),
    
    F7("F7"),
    
    F8("F8"),
    
    F9("F9"),
    
    FA("FA"),
    
    FB("FB"),
    
    FC("FC"),
    
    FP("FP"),
    
    FX("FX"),
    
    FY("FY"),
    
    G0("G0"),
    
    G1("G1"),
    
    G2("G2"),
    
    G3("G3"),
    
    G4("G4"),
    
    G5("G5"),
    
    G6("G6"),
    
    G7("G7"),
    
    G8("G8"),
    
    G9("G9"),
    
    GA("GA"),
    
    GB("GB"),
    
    GC("GC"),
    
    GD("GD"),
    
    GE("GE"),
    
    GF("GF"),
    
    GG("GG"),
    
    GH("GH"),
    
    GJ("GJ"),
    
    GK("GK"),
    
    GL("GL"),
    
    GM("GM"),
    
    GN("GN"),
    
    GO("GO"),
    
    GP("GP"),
    
    GQ("GQ"),
    
    GR("GR"),
    
    GS("GS"),
    
    GT("GT"),
    
    GU("GU"),
    
    GV("GV"),
    
    GW("GW"),
    
    GX("GX"),
    
    GY("GY"),
    
    GZ("GZ"),
    
    H9("H9"),
    
    HA("HA"),
    
    HB("HB"),
    
    HC("HC"),
    
    HD("HD"),
    
    HE("HE"),
    
    HF("HF"),
    
    HG("HG"),
    
    HH("HH"),
    
    HI("HI"),
    
    HJ("HJ"),
    
    HK("HK"),
    
    HL("HL"),
    
    HM("HM"),
    
    HN("HN"),
    
    HO("HO"),
    
    HP("HP"),
    
    HQ("HQ"),
    
    HR("HR"),
    
    HS("HS"),
    
    HT("HT"),
    
    HU("HU"),
    
    HV("HV"),
    
    HW("HW"),
    
    HX("HX"),
    
    HY("HY"),
    
    HZ("HZ"),
    
    J1("J1"),
    
    J2("J2"),
    
    J3("J3"),
    
    J4("J4"),
    
    JA("JA"),
    
    JB("JB"),
    
    JC("JC"),
    
    JD("JD"),
    
    JE("JE"),
    
    JF("JF"),
    
    JG("JG"),
    
    JW("JW"),
    
    K0("K0"),
    
    K1("K1"),
    
    K2("K2"),
    
    K3("K3"),
    
    K4("K4"),
    
    KA("KA"),
    
    KB("KB"),
    
    KC("KC"),
    
    KD("KD"),
    
    KE("KE"),
    
    KF("KF"),
    
    KG("KG"),
    
    KH("KH"),
    
    KI("KI"),
    
    KJ("KJ"),
    
    KK("KK"),
    
    KL("KL"),
    
    KM("KM"),
    
    KN("KN"),
    
    KO("KO"),
    
    KP("KP"),
    
    KQ("KQ"),
    
    KR("KR"),
    
    KS("KS"),
    
    KT("KT"),
    
    KU("KU"),
    
    KV("KV"),
    
    KW("KW"),
    
    KX("KX"),
    
    KY("KY"),
    
    KZ("KZ"),
    
    L1("L1"),
    
    LC("LC"),
    
    LD("LD"),
    
    LL("LL"),
    
    LM("LM"),
    
    LR("LR"),
    
    LS("LS"),
    
    LT("LT"),
    
    M2("M2"),
    
    ME("ME"),
    
    MI("MI"),
    
    MR("MR"),
    
    MS("MS"),
    
    NB("NB"),
    
    NH("NH"),
    
    NM("NM"),
    
    NR("NR"),
    
    NU("NU"),
    
    P1("P1"),
    
    P2("P2"),
    
    P3("P3"),
    
    P4("P4"),
    
    P5("P5"),
    
    P6("P6"),
    
    PA("PA"),
    
    PB("PB"),
    
    PC("PC"),
    
    PD("PD"),
    
    PE("PE"),
    
    PI("PI"),
    
    PL("PL"),
    
    PM("PM"),
    
    PN("PN"),
    
    PO("PO"),
    
    PS("PS"),
    
    PT("PT"),
    
    Q0("Q0"),
    
    Q1("Q1"),
    
    Q2("Q2"),
    
    Q3("Q3"),
    
    Q4("Q4"),
    
    Q5("Q5"),
    
    Q6("Q6"),
    
    Q7("Q7"),
    
    Q8("Q8"),
    
    Q9("Q9"),
    
    QA("QA"),
    
    QB("QB"),
    
    QC("QC"),
    
    QD("QD"),
    
    QE("QE"),
    
    QF("QF"),
    
    QG("QG"),
    
    QH("QH"),
    
    QJ("QJ"),
    
    QK("QK"),
    
    QL("QL"),
    
    QM("QM"),
    
    QN("QN"),
    
    QP("QP"),
    
    QQ("QQ"),
    
    QR("QR"),
    
    QS("QS"),
    
    QT("QT"),
    
    QU("QU"),
    
    QV("QV"),
    
    QW("QW"),
    
    QX("QX"),
    
    QY("QY"),
    
    QZ("QZ"),
    
    RA("RA"),
    
    RB("RB"),
    
    RC("RC"),
    
    RD("RD"),
    
    RE("RE"),
    
    RI("RI"),
    
    RP("RP"),
    
    RR("RR"),
    
    RT("RT"),
    
    SA("SA"),
    
    SB("SB"),
    
    SC("SC"),
    
    SD("SD"),
    
    SE("SE"),
    
    SF("SF"),
    
    SG("SG"),
    
    SH("SH"),
    
    SJ("SJ"),
    
    SK("SK"),
    
    SL("SL"),
    
    SM("SM"),
    
    SN("SN"),
    
    SP("SP"),
    
    SQ("SQ"),
    
    SS("SS"),
    
    ST("ST"),
    
    SU("SU"),
    
    SV("SV"),
    
    SW("SW"),
    
    SY("SY"),
    
    SZ("SZ"),
    
    T1("T1"),
    
    T2("T2"),
    
    T3("T3"),
    
    T4("T4"),
    
    T5("T5"),
    
    T6("T6"),
    
    T7("T7"),
    
    T8("T8"),
    
    T9("T9"),
    
    TA("TA"),
    
    TB("TB"),
    
    TC("TC"),
    
    TD("TD"),
    
    TE("TE"),
    
    TF("TF"),
    
    TG("TG"),
    
    TH("TH"),
    
    TJ("TJ"),
    
    TK("TK"),
    
    TL("TL"),
    
    TM("TM"),
    
    TN("TN"),
    
    TP("TP"),
    
    TQ("TQ"),
    
    TR("TR"),
    
    TS("TS"),
    
    TT("TT"),
    
    TU("TU"),
    
    TV("TV"),
    
    TW("TW"),
    
    TX("TX"),
    
    U1("U1"),
    
    U2("U2"),
    
    U3("U3"),
    
    U4("U4"),
    
    U5("U5"),
    
    U6("U6"),
    
    U7("U7"),
    
    U8("U8"),
    
    U9("U9"),
    
    UA("UA"),
    
    UB("UB"),
    
    UC("UC"),
    
    UD("UD"),
    
    UE("UE"),
    
    UF("UF"),
    
    UG("UG"),
    
    UH("UH"),
    
    UJ("UJ"),
    
    UK("UK"),
    
    UN("UN"),
    
    UP("UP"),
    
    UQ("UQ"),
    
    UR("UR"),
    
    US("US"),
    
    V1("V1"),
    
    V2("V2"),
    
    V3("V3"),
    
    V4("V4"),
    
    V5("V5"),
    
    V6("V6"),
    
    V7("V7"),
    
    V8("V8"),
    
    V9("V9"),
    
    VP("VP"),
    
    VR("VR"),
    
    W1("W1"),
    
    W5("W5"),
    
    W6("W6"),
    
    W7("W7"),
    
    W8("W8"),
    
    W9("W9"),
    
    WC("WC"),
    
    WH("WH"),
    
    WP("WP"),
    
    X1("X1"),
    
    X2("X2"),
    
    X3("X3"),
    
    X4("X4"),
    
    X5("X5"),
    
    XE("XE"),
    
    XP("XP"),
    
    XS("XS"),
    
    XU("XU"),
    
    VM("VM"),
    
    ZA("ZA"),
    
    ZB("ZB"),
    
    ZL("ZL"),
    
    ZS("ZS"),
    
    _1_P("1P"),
    
    _2_P("2P"),
    
    _3_P("3P"),
    
    _8_P("8P");

    private String value;

    CptHcpcsModifier2Enum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CptHcpcsModifier2Enum fromValue(String value) {
      for (CptHcpcsModifier2Enum b : CptHcpcsModifier2Enum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CptHcpcsModifier2Enum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CptHcpcsModifier2Enum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CptHcpcsModifier2Enum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CptHcpcsModifier2Enum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CptHcpcsModifier2Enum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CPT_HCPCS_MODIFIER2 = "cpt_hcpcs_modifier2";
  @SerializedName(SERIALIZED_NAME_CPT_HCPCS_MODIFIER2)
  private CptHcpcsModifier2Enum cptHcpcsModifier2;

  /**
   * 
   */
  @JsonAdapter(CptHcpcsModifier3Enum.Adapter.class)
  public enum CptHcpcsModifier3Enum {
    EMPTY(""),
    
    _17("17"),
    
    _1_D("1D"),
    
    _22("22"),
    
    _23("23"),
    
    _24("24"),
    
    _25("25"),
    
    _26("26"),
    
    _29("29"),
    
    _32("32"),
    
    _33("33"),
    
    _47("47"),
    
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
    
    _62("62"),
    
    _63("63"),
    
    _66("66"),
    
    _73("73"),
    
    _74("74"),
    
    _76("76"),
    
    _77("77"),
    
    _78("78"),
    
    _79("79"),
    
    _80("80"),
    
    _81("81"),
    
    _82("82"),
    
    _83("83"),
    
    _90("90"),
    
    _91("91"),
    
    _92("92"),
    
    _93("93"),
    
    _95("95"),
    
    _96("96"),
    
    _97("97"),
    
    _99("99"),
    
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
    
    AD("AD"),
    
    AE("AE"),
    
    AF("AF"),
    
    AG("AG"),
    
    AH("AH"),
    
    AI("AI"),
    
    AJ("AJ"),
    
    AK("AK"),
    
    AM("AM"),
    
    AO("AO"),
    
    AP("AP"),
    
    AQ("AQ"),
    
    AR("AR"),
    
    AS("AS"),
    
    AT("AT"),
    
    AU("AU"),
    
    AV("AV"),
    
    AW("AW"),
    
    AX("AX"),
    
    AY("AY"),
    
    AZ("AZ"),
    
    BA("BA"),
    
    BL("BL"),
    
    BO("BO"),
    
    BP("BP"),
    
    BR("BR"),
    
    BU("BU"),
    
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
    
    CR("CR"),
    
    CS("CS"),
    
    CT("CT"),
    
    DA("DA"),
    
    E1("E1"),
    
    E2("E2"),
    
    E3("E3"),
    
    E4("E4"),
    
    EA("EA"),
    
    EB("EB"),
    
    EC("EC"),
    
    ED("ED"),
    
    EE("EE"),
    
    EJ("EJ"),
    
    EM("EM"),
    
    EP("EP"),
    
    ER("ER"),
    
    ET("ET"),
    
    EX("EX"),
    
    EY("EY"),
    
    F1("F1"),
    
    F2("F2"),
    
    F3("F3"),
    
    F4("F4"),
    
    F5("F5"),
    
    F6("F6"),
    
    F7("F7"),
    
    F8("F8"),
    
    F9("F9"),
    
    FA("FA"),
    
    FB("FB"),
    
    FC("FC"),
    
    FP("FP"),
    
    FX("FX"),
    
    FY("FY"),
    
    G0("G0"),
    
    G1("G1"),
    
    G2("G2"),
    
    G3("G3"),
    
    G4("G4"),
    
    G5("G5"),
    
    G6("G6"),
    
    G7("G7"),
    
    G8("G8"),
    
    G9("G9"),
    
    GA("GA"),
    
    GB("GB"),
    
    GC("GC"),
    
    GD("GD"),
    
    GE("GE"),
    
    GF("GF"),
    
    GG("GG"),
    
    GH("GH"),
    
    GJ("GJ"),
    
    GK("GK"),
    
    GL("GL"),
    
    GM("GM"),
    
    GN("GN"),
    
    GO("GO"),
    
    GP("GP"),
    
    GQ("GQ"),
    
    GR("GR"),
    
    GS("GS"),
    
    GT("GT"),
    
    GU("GU"),
    
    GV("GV"),
    
    GW("GW"),
    
    GX("GX"),
    
    GY("GY"),
    
    GZ("GZ"),
    
    H9("H9"),
    
    HA("HA"),
    
    HB("HB"),
    
    HC("HC"),
    
    HD("HD"),
    
    HE("HE"),
    
    HF("HF"),
    
    HG("HG"),
    
    HH("HH"),
    
    HI("HI"),
    
    HJ("HJ"),
    
    HK("HK"),
    
    HL("HL"),
    
    HM("HM"),
    
    HN("HN"),
    
    HO("HO"),
    
    HP("HP"),
    
    HQ("HQ"),
    
    HR("HR"),
    
    HS("HS"),
    
    HT("HT"),
    
    HU("HU"),
    
    HV("HV"),
    
    HW("HW"),
    
    HX("HX"),
    
    HY("HY"),
    
    HZ("HZ"),
    
    J1("J1"),
    
    J2("J2"),
    
    J3("J3"),
    
    J4("J4"),
    
    JA("JA"),
    
    JB("JB"),
    
    JC("JC"),
    
    JD("JD"),
    
    JE("JE"),
    
    JF("JF"),
    
    JG("JG"),
    
    JW("JW"),
    
    K0("K0"),
    
    K1("K1"),
    
    K2("K2"),
    
    K3("K3"),
    
    K4("K4"),
    
    KA("KA"),
    
    KB("KB"),
    
    KC("KC"),
    
    KD("KD"),
    
    KE("KE"),
    
    KF("KF"),
    
    KG("KG"),
    
    KH("KH"),
    
    KI("KI"),
    
    KJ("KJ"),
    
    KK("KK"),
    
    KL("KL"),
    
    KM("KM"),
    
    KN("KN"),
    
    KO("KO"),
    
    KP("KP"),
    
    KQ("KQ"),
    
    KR("KR"),
    
    KS("KS"),
    
    KT("KT"),
    
    KU("KU"),
    
    KV("KV"),
    
    KW("KW"),
    
    KX("KX"),
    
    KY("KY"),
    
    KZ("KZ"),
    
    L1("L1"),
    
    LC("LC"),
    
    LD("LD"),
    
    LL("LL"),
    
    LM("LM"),
    
    LR("LR"),
    
    LS("LS"),
    
    LT("LT"),
    
    M2("M2"),
    
    ME("ME"),
    
    MI("MI"),
    
    MR("MR"),
    
    MS("MS"),
    
    NB("NB"),
    
    NH("NH"),
    
    NM("NM"),
    
    NR("NR"),
    
    NU("NU"),
    
    P1("P1"),
    
    P2("P2"),
    
    P3("P3"),
    
    P4("P4"),
    
    P5("P5"),
    
    P6("P6"),
    
    PA("PA"),
    
    PB("PB"),
    
    PC("PC"),
    
    PD("PD"),
    
    PE("PE"),
    
    PI("PI"),
    
    PL("PL"),
    
    PM("PM"),
    
    PN("PN"),
    
    PO("PO"),
    
    PS("PS"),
    
    PT("PT"),
    
    Q0("Q0"),
    
    Q1("Q1"),
    
    Q2("Q2"),
    
    Q3("Q3"),
    
    Q4("Q4"),
    
    Q5("Q5"),
    
    Q6("Q6"),
    
    Q7("Q7"),
    
    Q8("Q8"),
    
    Q9("Q9"),
    
    QA("QA"),
    
    QB("QB"),
    
    QC("QC"),
    
    QD("QD"),
    
    QE("QE"),
    
    QF("QF"),
    
    QG("QG"),
    
    QH("QH"),
    
    QJ("QJ"),
    
    QK("QK"),
    
    QL("QL"),
    
    QM("QM"),
    
    QN("QN"),
    
    QP("QP"),
    
    QQ("QQ"),
    
    QR("QR"),
    
    QS("QS"),
    
    QT("QT"),
    
    QU("QU"),
    
    QV("QV"),
    
    QW("QW"),
    
    QX("QX"),
    
    QY("QY"),
    
    QZ("QZ"),
    
    RA("RA"),
    
    RB("RB"),
    
    RC("RC"),
    
    RD("RD"),
    
    RE("RE"),
    
    RI("RI"),
    
    RP("RP"),
    
    RR("RR"),
    
    RT("RT"),
    
    SA("SA"),
    
    SB("SB"),
    
    SC("SC"),
    
    SD("SD"),
    
    SE("SE"),
    
    SF("SF"),
    
    SG("SG"),
    
    SH("SH"),
    
    SJ("SJ"),
    
    SK("SK"),
    
    SL("SL"),
    
    SM("SM"),
    
    SN("SN"),
    
    SP("SP"),
    
    SQ("SQ"),
    
    SS("SS"),
    
    ST("ST"),
    
    SU("SU"),
    
    SV("SV"),
    
    SW("SW"),
    
    SY("SY"),
    
    SZ("SZ"),
    
    T1("T1"),
    
    T2("T2"),
    
    T3("T3"),
    
    T4("T4"),
    
    T5("T5"),
    
    T6("T6"),
    
    T7("T7"),
    
    T8("T8"),
    
    T9("T9"),
    
    TA("TA"),
    
    TB("TB"),
    
    TC("TC"),
    
    TD("TD"),
    
    TE("TE"),
    
    TF("TF"),
    
    TG("TG"),
    
    TH("TH"),
    
    TJ("TJ"),
    
    TK("TK"),
    
    TL("TL"),
    
    TM("TM"),
    
    TN("TN"),
    
    TP("TP"),
    
    TQ("TQ"),
    
    TR("TR"),
    
    TS("TS"),
    
    TT("TT"),
    
    TU("TU"),
    
    TV("TV"),
    
    TW("TW"),
    
    TX("TX"),
    
    U1("U1"),
    
    U2("U2"),
    
    U3("U3"),
    
    U4("U4"),
    
    U5("U5"),
    
    U6("U6"),
    
    U7("U7"),
    
    U8("U8"),
    
    U9("U9"),
    
    UA("UA"),
    
    UB("UB"),
    
    UC("UC"),
    
    UD("UD"),
    
    UE("UE"),
    
    UF("UF"),
    
    UG("UG"),
    
    UH("UH"),
    
    UJ("UJ"),
    
    UK("UK"),
    
    UN("UN"),
    
    UP("UP"),
    
    UQ("UQ"),
    
    UR("UR"),
    
    US("US"),
    
    V1("V1"),
    
    V2("V2"),
    
    V3("V3"),
    
    V4("V4"),
    
    V5("V5"),
    
    V6("V6"),
    
    V7("V7"),
    
    V8("V8"),
    
    V9("V9"),
    
    VP("VP"),
    
    VR("VR"),
    
    W1("W1"),
    
    W5("W5"),
    
    W6("W6"),
    
    W7("W7"),
    
    W8("W8"),
    
    W9("W9"),
    
    WC("WC"),
    
    WH("WH"),
    
    WP("WP"),
    
    X1("X1"),
    
    X2("X2"),
    
    X3("X3"),
    
    X4("X4"),
    
    X5("X5"),
    
    XE("XE"),
    
    XP("XP"),
    
    XS("XS"),
    
    XU("XU"),
    
    VM("VM"),
    
    ZA("ZA"),
    
    ZB("ZB"),
    
    ZL("ZL"),
    
    ZS("ZS"),
    
    _1_P("1P"),
    
    _2_P("2P"),
    
    _3_P("3P"),
    
    _8_P("8P");

    private String value;

    CptHcpcsModifier3Enum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CptHcpcsModifier3Enum fromValue(String value) {
      for (CptHcpcsModifier3Enum b : CptHcpcsModifier3Enum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CptHcpcsModifier3Enum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CptHcpcsModifier3Enum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CptHcpcsModifier3Enum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CptHcpcsModifier3Enum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CptHcpcsModifier3Enum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CPT_HCPCS_MODIFIER3 = "cpt_hcpcs_modifier3";
  @SerializedName(SERIALIZED_NAME_CPT_HCPCS_MODIFIER3)
  private CptHcpcsModifier3Enum cptHcpcsModifier3;

  /**
   * 
   */
  @JsonAdapter(CptHcpcsModifier4Enum.Adapter.class)
  public enum CptHcpcsModifier4Enum {
    EMPTY(""),
    
    _17("17"),
    
    _1_D("1D"),
    
    _22("22"),
    
    _23("23"),
    
    _24("24"),
    
    _25("25"),
    
    _26("26"),
    
    _29("29"),
    
    _32("32"),
    
    _33("33"),
    
    _47("47"),
    
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
    
    _62("62"),
    
    _63("63"),
    
    _66("66"),
    
    _73("73"),
    
    _74("74"),
    
    _76("76"),
    
    _77("77"),
    
    _78("78"),
    
    _79("79"),
    
    _80("80"),
    
    _81("81"),
    
    _82("82"),
    
    _83("83"),
    
    _90("90"),
    
    _91("91"),
    
    _92("92"),
    
    _93("93"),
    
    _95("95"),
    
    _96("96"),
    
    _97("97"),
    
    _99("99"),
    
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
    
    AD("AD"),
    
    AE("AE"),
    
    AF("AF"),
    
    AG("AG"),
    
    AH("AH"),
    
    AI("AI"),
    
    AJ("AJ"),
    
    AK("AK"),
    
    AM("AM"),
    
    AO("AO"),
    
    AP("AP"),
    
    AQ("AQ"),
    
    AR("AR"),
    
    AS("AS"),
    
    AT("AT"),
    
    AU("AU"),
    
    AV("AV"),
    
    AW("AW"),
    
    AX("AX"),
    
    AY("AY"),
    
    AZ("AZ"),
    
    BA("BA"),
    
    BL("BL"),
    
    BO("BO"),
    
    BP("BP"),
    
    BR("BR"),
    
    BU("BU"),
    
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
    
    CR("CR"),
    
    CS("CS"),
    
    CT("CT"),
    
    DA("DA"),
    
    E1("E1"),
    
    E2("E2"),
    
    E3("E3"),
    
    E4("E4"),
    
    EA("EA"),
    
    EB("EB"),
    
    EC("EC"),
    
    ED("ED"),
    
    EE("EE"),
    
    EJ("EJ"),
    
    EM("EM"),
    
    EP("EP"),
    
    ER("ER"),
    
    ET("ET"),
    
    EX("EX"),
    
    EY("EY"),
    
    F1("F1"),
    
    F2("F2"),
    
    F3("F3"),
    
    F4("F4"),
    
    F5("F5"),
    
    F6("F6"),
    
    F7("F7"),
    
    F8("F8"),
    
    F9("F9"),
    
    FA("FA"),
    
    FB("FB"),
    
    FC("FC"),
    
    FP("FP"),
    
    FX("FX"),
    
    FY("FY"),
    
    G0("G0"),
    
    G1("G1"),
    
    G2("G2"),
    
    G3("G3"),
    
    G4("G4"),
    
    G5("G5"),
    
    G6("G6"),
    
    G7("G7"),
    
    G8("G8"),
    
    G9("G9"),
    
    GA("GA"),
    
    GB("GB"),
    
    GC("GC"),
    
    GD("GD"),
    
    GE("GE"),
    
    GF("GF"),
    
    GG("GG"),
    
    GH("GH"),
    
    GJ("GJ"),
    
    GK("GK"),
    
    GL("GL"),
    
    GM("GM"),
    
    GN("GN"),
    
    GO("GO"),
    
    GP("GP"),
    
    GQ("GQ"),
    
    GR("GR"),
    
    GS("GS"),
    
    GT("GT"),
    
    GU("GU"),
    
    GV("GV"),
    
    GW("GW"),
    
    GX("GX"),
    
    GY("GY"),
    
    GZ("GZ"),
    
    H9("H9"),
    
    HA("HA"),
    
    HB("HB"),
    
    HC("HC"),
    
    HD("HD"),
    
    HE("HE"),
    
    HF("HF"),
    
    HG("HG"),
    
    HH("HH"),
    
    HI("HI"),
    
    HJ("HJ"),
    
    HK("HK"),
    
    HL("HL"),
    
    HM("HM"),
    
    HN("HN"),
    
    HO("HO"),
    
    HP("HP"),
    
    HQ("HQ"),
    
    HR("HR"),
    
    HS("HS"),
    
    HT("HT"),
    
    HU("HU"),
    
    HV("HV"),
    
    HW("HW"),
    
    HX("HX"),
    
    HY("HY"),
    
    HZ("HZ"),
    
    J1("J1"),
    
    J2("J2"),
    
    J3("J3"),
    
    J4("J4"),
    
    JA("JA"),
    
    JB("JB"),
    
    JC("JC"),
    
    JD("JD"),
    
    JE("JE"),
    
    JF("JF"),
    
    JG("JG"),
    
    JW("JW"),
    
    K0("K0"),
    
    K1("K1"),
    
    K2("K2"),
    
    K3("K3"),
    
    K4("K4"),
    
    KA("KA"),
    
    KB("KB"),
    
    KC("KC"),
    
    KD("KD"),
    
    KE("KE"),
    
    KF("KF"),
    
    KG("KG"),
    
    KH("KH"),
    
    KI("KI"),
    
    KJ("KJ"),
    
    KK("KK"),
    
    KL("KL"),
    
    KM("KM"),
    
    KN("KN"),
    
    KO("KO"),
    
    KP("KP"),
    
    KQ("KQ"),
    
    KR("KR"),
    
    KS("KS"),
    
    KT("KT"),
    
    KU("KU"),
    
    KV("KV"),
    
    KW("KW"),
    
    KX("KX"),
    
    KY("KY"),
    
    KZ("KZ"),
    
    L1("L1"),
    
    LC("LC"),
    
    LD("LD"),
    
    LL("LL"),
    
    LM("LM"),
    
    LR("LR"),
    
    LS("LS"),
    
    LT("LT"),
    
    M2("M2"),
    
    ME("ME"),
    
    MI("MI"),
    
    MR("MR"),
    
    MS("MS"),
    
    NB("NB"),
    
    NH("NH"),
    
    NM("NM"),
    
    NR("NR"),
    
    NU("NU"),
    
    P1("P1"),
    
    P2("P2"),
    
    P3("P3"),
    
    P4("P4"),
    
    P5("P5"),
    
    P6("P6"),
    
    PA("PA"),
    
    PB("PB"),
    
    PC("PC"),
    
    PD("PD"),
    
    PE("PE"),
    
    PI("PI"),
    
    PL("PL"),
    
    PM("PM"),
    
    PN("PN"),
    
    PO("PO"),
    
    PS("PS"),
    
    PT("PT"),
    
    Q0("Q0"),
    
    Q1("Q1"),
    
    Q2("Q2"),
    
    Q3("Q3"),
    
    Q4("Q4"),
    
    Q5("Q5"),
    
    Q6("Q6"),
    
    Q7("Q7"),
    
    Q8("Q8"),
    
    Q9("Q9"),
    
    QA("QA"),
    
    QB("QB"),
    
    QC("QC"),
    
    QD("QD"),
    
    QE("QE"),
    
    QF("QF"),
    
    QG("QG"),
    
    QH("QH"),
    
    QJ("QJ"),
    
    QK("QK"),
    
    QL("QL"),
    
    QM("QM"),
    
    QN("QN"),
    
    QP("QP"),
    
    QQ("QQ"),
    
    QR("QR"),
    
    QS("QS"),
    
    QT("QT"),
    
    QU("QU"),
    
    QV("QV"),
    
    QW("QW"),
    
    QX("QX"),
    
    QY("QY"),
    
    QZ("QZ"),
    
    RA("RA"),
    
    RB("RB"),
    
    RC("RC"),
    
    RD("RD"),
    
    RE("RE"),
    
    RI("RI"),
    
    RP("RP"),
    
    RR("RR"),
    
    RT("RT"),
    
    SA("SA"),
    
    SB("SB"),
    
    SC("SC"),
    
    SD("SD"),
    
    SE("SE"),
    
    SF("SF"),
    
    SG("SG"),
    
    SH("SH"),
    
    SJ("SJ"),
    
    SK("SK"),
    
    SL("SL"),
    
    SM("SM"),
    
    SN("SN"),
    
    SP("SP"),
    
    SQ("SQ"),
    
    SS("SS"),
    
    ST("ST"),
    
    SU("SU"),
    
    SV("SV"),
    
    SW("SW"),
    
    SY("SY"),
    
    SZ("SZ"),
    
    T1("T1"),
    
    T2("T2"),
    
    T3("T3"),
    
    T4("T4"),
    
    T5("T5"),
    
    T6("T6"),
    
    T7("T7"),
    
    T8("T8"),
    
    T9("T9"),
    
    TA("TA"),
    
    TB("TB"),
    
    TC("TC"),
    
    TD("TD"),
    
    TE("TE"),
    
    TF("TF"),
    
    TG("TG"),
    
    TH("TH"),
    
    TJ("TJ"),
    
    TK("TK"),
    
    TL("TL"),
    
    TM("TM"),
    
    TN("TN"),
    
    TP("TP"),
    
    TQ("TQ"),
    
    TR("TR"),
    
    TS("TS"),
    
    TT("TT"),
    
    TU("TU"),
    
    TV("TV"),
    
    TW("TW"),
    
    TX("TX"),
    
    U1("U1"),
    
    U2("U2"),
    
    U3("U3"),
    
    U4("U4"),
    
    U5("U5"),
    
    U6("U6"),
    
    U7("U7"),
    
    U8("U8"),
    
    U9("U9"),
    
    UA("UA"),
    
    UB("UB"),
    
    UC("UC"),
    
    UD("UD"),
    
    UE("UE"),
    
    UF("UF"),
    
    UG("UG"),
    
    UH("UH"),
    
    UJ("UJ"),
    
    UK("UK"),
    
    UN("UN"),
    
    UP("UP"),
    
    UQ("UQ"),
    
    UR("UR"),
    
    US("US"),
    
    V1("V1"),
    
    V2("V2"),
    
    V3("V3"),
    
    V4("V4"),
    
    V5("V5"),
    
    V6("V6"),
    
    V7("V7"),
    
    V8("V8"),
    
    V9("V9"),
    
    VP("VP"),
    
    VR("VR"),
    
    W1("W1"),
    
    W5("W5"),
    
    W6("W6"),
    
    W7("W7"),
    
    W8("W8"),
    
    W9("W9"),
    
    WC("WC"),
    
    WH("WH"),
    
    WP("WP"),
    
    X1("X1"),
    
    X2("X2"),
    
    X3("X3"),
    
    X4("X4"),
    
    X5("X5"),
    
    XE("XE"),
    
    XP("XP"),
    
    XS("XS"),
    
    XU("XU"),
    
    VM("VM"),
    
    ZA("ZA"),
    
    ZB("ZB"),
    
    ZL("ZL"),
    
    ZS("ZS"),
    
    _1_P("1P"),
    
    _2_P("2P"),
    
    _3_P("3P"),
    
    _8_P("8P");

    private String value;

    CptHcpcsModifier4Enum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CptHcpcsModifier4Enum fromValue(String value) {
      for (CptHcpcsModifier4Enum b : CptHcpcsModifier4Enum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CptHcpcsModifier4Enum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CptHcpcsModifier4Enum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CptHcpcsModifier4Enum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CptHcpcsModifier4Enum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CptHcpcsModifier4Enum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CPT_HCPCS_MODIFIER4 = "cpt_hcpcs_modifier4";
  @SerializedName(SERIALIZED_NAME_CPT_HCPCS_MODIFIER4)
  private CptHcpcsModifier4Enum cptHcpcsModifier4;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private Integer doctor;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INSURED_OUT_OF_NETWORK_PRICE = "insured_out_of_network_price";
  @SerializedName(SERIALIZED_NAME_INSURED_OUT_OF_NETWORK_PRICE)
  private BigDecimal insuredOutOfNetworkPrice;

  public static final String SERIALIZED_NAME_INSURED_PRICE = "insured_price";
  @SerializedName(SERIALIZED_NAME_INSURED_PRICE)
  private BigDecimal insuredPrice;

  public static final String SERIALIZED_NAME_NDC_CODE = "ndc_code";
  @SerializedName(SERIALIZED_NAME_NDC_CODE)
  private String ndcCode;

  public static final String SERIALIZED_NAME_NDC_QUANTITY = "ndc_quantity";
  @SerializedName(SERIALIZED_NAME_NDC_QUANTITY)
  private BigDecimal ndcQuantity;

  /**
   * 
   */
  @JsonAdapter(NdcUnitsEnum.Adapter.class)
  public enum NdcUnitsEnum {
    F2("F2"),
    
    GR("GR"),
    
    ME("ME"),
    
    ML("ML"),
    
    UN("UN");

    private String value;

    NdcUnitsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NdcUnitsEnum fromValue(String value) {
      for (NdcUnitsEnum b : NdcUnitsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NdcUnitsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NdcUnitsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NdcUnitsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NdcUnitsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NdcUnitsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NDC_UNITS = "ndc_units";
  @SerializedName(SERIALIZED_NAME_NDC_UNITS)
  private NdcUnitsEnum ndcUnits;

  public static final String SERIALIZED_NAME_OFFICE = "office";
  @SerializedName(SERIALIZED_NAME_OFFICE)
  private Integer office;

  public static final String SERIALIZED_NAME_PAYER_ID = "payer_id";
  @SerializedName(SERIALIZED_NAME_PAYER_ID)
  private String payerId;

  public static final String SERIALIZED_NAME_PICKLIST_CATEGORY = "picklist_category";
  @SerializedName(SERIALIZED_NAME_PICKLIST_CATEGORY)
  private String picklistCategory;

  public static final String SERIALIZED_NAME_PLAN_NAME = "plan_name";
  @SerializedName(SERIALIZED_NAME_PLAN_NAME)
  private String planName;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public DoctorFeeSchedule() {
  }

  public DoctorFeeSchedule(
     String createdAt, 
     Integer id, 
     String updatedAt
  ) {
    this();
    this.createdAt = createdAt;
    this.id = id;
    this.updatedAt = updatedAt;
  }

  public DoctorFeeSchedule allowedAmount(BigDecimal allowedAmount) {
    this.allowedAmount = allowedAmount;
    return this;
  }

  /**
   * Typical allowed amount for payer. Not used if blank.
   * @return allowedAmount
   */
  @javax.annotation.Nullable
  public BigDecimal getAllowedAmount() {
    return allowedAmount;
  }

  public void setAllowedAmount(BigDecimal allowedAmount) {
    this.allowedAmount = allowedAmount;
  }


  public DoctorFeeSchedule basePrice(BigDecimal basePrice) {
    this.basePrice = basePrice;
    return this;
  }

  /**
   * 
   * @return basePrice
   */
  @javax.annotation.Nullable
  public BigDecimal getBasePrice() {
    return basePrice;
  }

  public void setBasePrice(BigDecimal basePrice) {
    this.basePrice = basePrice;
  }


  public DoctorFeeSchedule billingDescription(String billingDescription) {
    this.billingDescription = billingDescription;
    return this;
  }

  /**
   * 
   * @return billingDescription
   */
  @javax.annotation.Nullable
  public String getBillingDescription() {
    return billingDescription;
  }

  public void setBillingDescription(String billingDescription) {
    this.billingDescription = billingDescription;
  }


  public DoctorFeeSchedule cashPrice(BigDecimal cashPrice) {
    this.cashPrice = cashPrice;
    return this;
  }

  /**
   * 
   * @return cashPrice
   */
  @javax.annotation.Nullable
  public BigDecimal getCashPrice() {
    return cashPrice;
  }

  public void setCashPrice(BigDecimal cashPrice) {
    this.cashPrice = cashPrice;
  }


  public DoctorFeeSchedule code(String code) {
    this.code = code;
    return this;
  }

  /**
   * 
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public DoctorFeeSchedule codeType(CodeTypeEnum codeType) {
    this.codeType = codeType;
    return this;
  }

  /**
   * 
   * @return codeType
   */
  @javax.annotation.Nullable
  public CodeTypeEnum getCodeType() {
    return codeType;
  }

  public void setCodeType(CodeTypeEnum codeType) {
    this.codeType = codeType;
  }


  public DoctorFeeSchedule cptHcpcsModifier1(String cptHcpcsModifier1) {
    this.cptHcpcsModifier1 = cptHcpcsModifier1;
    return this;
  }

  /**
   * 
   * @return cptHcpcsModifier1
   */
  @javax.annotation.Nullable
  public String getCptHcpcsModifier1() {
    return cptHcpcsModifier1;
  }

  public void setCptHcpcsModifier1(String cptHcpcsModifier1) {
    this.cptHcpcsModifier1 = cptHcpcsModifier1;
  }


  public DoctorFeeSchedule cptHcpcsModifier2(CptHcpcsModifier2Enum cptHcpcsModifier2) {
    this.cptHcpcsModifier2 = cptHcpcsModifier2;
    return this;
  }

  /**
   * 
   * @return cptHcpcsModifier2
   */
  @javax.annotation.Nullable
  public CptHcpcsModifier2Enum getCptHcpcsModifier2() {
    return cptHcpcsModifier2;
  }

  public void setCptHcpcsModifier2(CptHcpcsModifier2Enum cptHcpcsModifier2) {
    this.cptHcpcsModifier2 = cptHcpcsModifier2;
  }


  public DoctorFeeSchedule cptHcpcsModifier3(CptHcpcsModifier3Enum cptHcpcsModifier3) {
    this.cptHcpcsModifier3 = cptHcpcsModifier3;
    return this;
  }

  /**
   * 
   * @return cptHcpcsModifier3
   */
  @javax.annotation.Nullable
  public CptHcpcsModifier3Enum getCptHcpcsModifier3() {
    return cptHcpcsModifier3;
  }

  public void setCptHcpcsModifier3(CptHcpcsModifier3Enum cptHcpcsModifier3) {
    this.cptHcpcsModifier3 = cptHcpcsModifier3;
  }


  public DoctorFeeSchedule cptHcpcsModifier4(CptHcpcsModifier4Enum cptHcpcsModifier4) {
    this.cptHcpcsModifier4 = cptHcpcsModifier4;
    return this;
  }

  /**
   * 
   * @return cptHcpcsModifier4
   */
  @javax.annotation.Nullable
  public CptHcpcsModifier4Enum getCptHcpcsModifier4() {
    return cptHcpcsModifier4;
  }

  public void setCptHcpcsModifier4(CptHcpcsModifier4Enum cptHcpcsModifier4) {
    this.cptHcpcsModifier4 = cptHcpcsModifier4;
  }


  /**
   * 
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }



  public DoctorFeeSchedule description(String description) {
    this.description = description;
    return this;
  }

  /**
   * 
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public DoctorFeeSchedule doctor(Integer doctor) {
    this.doctor = doctor;
    return this;
  }

  /**
   * 
   * @return doctor
   */
  @javax.annotation.Nullable
  public Integer getDoctor() {
    return doctor;
  }

  public void setDoctor(Integer doctor) {
    this.doctor = doctor;
  }


  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public DoctorFeeSchedule insuredOutOfNetworkPrice(BigDecimal insuredOutOfNetworkPrice) {
    this.insuredOutOfNetworkPrice = insuredOutOfNetworkPrice;
    return this;
  }

  /**
   * 
   * @return insuredOutOfNetworkPrice
   */
  @javax.annotation.Nullable
  public BigDecimal getInsuredOutOfNetworkPrice() {
    return insuredOutOfNetworkPrice;
  }

  public void setInsuredOutOfNetworkPrice(BigDecimal insuredOutOfNetworkPrice) {
    this.insuredOutOfNetworkPrice = insuredOutOfNetworkPrice;
  }


  public DoctorFeeSchedule insuredPrice(BigDecimal insuredPrice) {
    this.insuredPrice = insuredPrice;
    return this;
  }

  /**
   * 
   * @return insuredPrice
   */
  @javax.annotation.Nullable
  public BigDecimal getInsuredPrice() {
    return insuredPrice;
  }

  public void setInsuredPrice(BigDecimal insuredPrice) {
    this.insuredPrice = insuredPrice;
  }


  public DoctorFeeSchedule ndcCode(String ndcCode) {
    this.ndcCode = ndcCode;
    return this;
  }

  /**
   * 
   * @return ndcCode
   */
  @javax.annotation.Nullable
  public String getNdcCode() {
    return ndcCode;
  }

  public void setNdcCode(String ndcCode) {
    this.ndcCode = ndcCode;
  }


  public DoctorFeeSchedule ndcQuantity(BigDecimal ndcQuantity) {
    this.ndcQuantity = ndcQuantity;
    return this;
  }

  /**
   * 
   * @return ndcQuantity
   */
  @javax.annotation.Nullable
  public BigDecimal getNdcQuantity() {
    return ndcQuantity;
  }

  public void setNdcQuantity(BigDecimal ndcQuantity) {
    this.ndcQuantity = ndcQuantity;
  }


  public DoctorFeeSchedule ndcUnits(NdcUnitsEnum ndcUnits) {
    this.ndcUnits = ndcUnits;
    return this;
  }

  /**
   * 
   * @return ndcUnits
   */
  @javax.annotation.Nullable
  public NdcUnitsEnum getNdcUnits() {
    return ndcUnits;
  }

  public void setNdcUnits(NdcUnitsEnum ndcUnits) {
    this.ndcUnits = ndcUnits;
  }


  public DoctorFeeSchedule office(Integer office) {
    this.office = office;
    return this;
  }

  /**
   * 
   * @return office
   */
  @javax.annotation.Nullable
  public Integer getOffice() {
    return office;
  }

  public void setOffice(Integer office) {
    this.office = office;
  }


  public DoctorFeeSchedule payerId(String payerId) {
    this.payerId = payerId;
    return this;
  }

  /**
   * Fee Schedule pricing specific to this payer, if null, then applies as default to all payers without a more specific fee schedule.
   * @return payerId
   */
  @javax.annotation.Nullable
  public String getPayerId() {
    return payerId;
  }

  public void setPayerId(String payerId) {
    this.payerId = payerId;
  }


  public DoctorFeeSchedule picklistCategory(String picklistCategory) {
    this.picklistCategory = picklistCategory;
    return this;
  }

  /**
   * Optional: Category to organize the code into.
   * @return picklistCategory
   */
  @javax.annotation.Nullable
  public String getPicklistCategory() {
    return picklistCategory;
  }

  public void setPicklistCategory(String picklistCategory) {
    this.picklistCategory = picklistCategory;
  }


  public DoctorFeeSchedule planName(String planName) {
    this.planName = planName;
    return this;
  }

  /**
   * Name of insurance plan.
   * @return planName
   */
  @javax.annotation.Nullable
  public String getPlanName() {
    return planName;
  }

  public void setPlanName(String planName) {
    this.planName = planName;
  }


  /**
   * 
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DoctorFeeSchedule doctorFeeSchedule = (DoctorFeeSchedule) o;
    return Objects.equals(this.allowedAmount, doctorFeeSchedule.allowedAmount) &&
        Objects.equals(this.basePrice, doctorFeeSchedule.basePrice) &&
        Objects.equals(this.billingDescription, doctorFeeSchedule.billingDescription) &&
        Objects.equals(this.cashPrice, doctorFeeSchedule.cashPrice) &&
        Objects.equals(this.code, doctorFeeSchedule.code) &&
        Objects.equals(this.codeType, doctorFeeSchedule.codeType) &&
        Objects.equals(this.cptHcpcsModifier1, doctorFeeSchedule.cptHcpcsModifier1) &&
        Objects.equals(this.cptHcpcsModifier2, doctorFeeSchedule.cptHcpcsModifier2) &&
        Objects.equals(this.cptHcpcsModifier3, doctorFeeSchedule.cptHcpcsModifier3) &&
        Objects.equals(this.cptHcpcsModifier4, doctorFeeSchedule.cptHcpcsModifier4) &&
        Objects.equals(this.createdAt, doctorFeeSchedule.createdAt) &&
        Objects.equals(this.description, doctorFeeSchedule.description) &&
        Objects.equals(this.doctor, doctorFeeSchedule.doctor) &&
        Objects.equals(this.id, doctorFeeSchedule.id) &&
        Objects.equals(this.insuredOutOfNetworkPrice, doctorFeeSchedule.insuredOutOfNetworkPrice) &&
        Objects.equals(this.insuredPrice, doctorFeeSchedule.insuredPrice) &&
        Objects.equals(this.ndcCode, doctorFeeSchedule.ndcCode) &&
        Objects.equals(this.ndcQuantity, doctorFeeSchedule.ndcQuantity) &&
        Objects.equals(this.ndcUnits, doctorFeeSchedule.ndcUnits) &&
        Objects.equals(this.office, doctorFeeSchedule.office) &&
        Objects.equals(this.payerId, doctorFeeSchedule.payerId) &&
        Objects.equals(this.picklistCategory, doctorFeeSchedule.picklistCategory) &&
        Objects.equals(this.planName, doctorFeeSchedule.planName) &&
        Objects.equals(this.updatedAt, doctorFeeSchedule.updatedAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowedAmount, basePrice, billingDescription, cashPrice, code, codeType, cptHcpcsModifier1, cptHcpcsModifier2, cptHcpcsModifier3, cptHcpcsModifier4, createdAt, description, doctor, id, insuredOutOfNetworkPrice, insuredPrice, ndcCode, ndcQuantity, ndcUnits, office, payerId, picklistCategory, planName, updatedAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DoctorFeeSchedule {\n");
    sb.append("    allowedAmount: ").append(toIndentedString(allowedAmount)).append("\n");
    sb.append("    basePrice: ").append(toIndentedString(basePrice)).append("\n");
    sb.append("    billingDescription: ").append(toIndentedString(billingDescription)).append("\n");
    sb.append("    cashPrice: ").append(toIndentedString(cashPrice)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    codeType: ").append(toIndentedString(codeType)).append("\n");
    sb.append("    cptHcpcsModifier1: ").append(toIndentedString(cptHcpcsModifier1)).append("\n");
    sb.append("    cptHcpcsModifier2: ").append(toIndentedString(cptHcpcsModifier2)).append("\n");
    sb.append("    cptHcpcsModifier3: ").append(toIndentedString(cptHcpcsModifier3)).append("\n");
    sb.append("    cptHcpcsModifier4: ").append(toIndentedString(cptHcpcsModifier4)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    insuredOutOfNetworkPrice: ").append(toIndentedString(insuredOutOfNetworkPrice)).append("\n");
    sb.append("    insuredPrice: ").append(toIndentedString(insuredPrice)).append("\n");
    sb.append("    ndcCode: ").append(toIndentedString(ndcCode)).append("\n");
    sb.append("    ndcQuantity: ").append(toIndentedString(ndcQuantity)).append("\n");
    sb.append("    ndcUnits: ").append(toIndentedString(ndcUnits)).append("\n");
    sb.append("    office: ").append(toIndentedString(office)).append("\n");
    sb.append("    payerId: ").append(toIndentedString(payerId)).append("\n");
    sb.append("    picklistCategory: ").append(toIndentedString(picklistCategory)).append("\n");
    sb.append("    planName: ").append(toIndentedString(planName)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("allowed_amount");
    openapiFields.add("base_price");
    openapiFields.add("billing_description");
    openapiFields.add("cash_price");
    openapiFields.add("code");
    openapiFields.add("code_type");
    openapiFields.add("cpt_hcpcs_modifier1");
    openapiFields.add("cpt_hcpcs_modifier2");
    openapiFields.add("cpt_hcpcs_modifier3");
    openapiFields.add("cpt_hcpcs_modifier4");
    openapiFields.add("created_at");
    openapiFields.add("description");
    openapiFields.add("doctor");
    openapiFields.add("id");
    openapiFields.add("insured_out_of_network_price");
    openapiFields.add("insured_price");
    openapiFields.add("ndc_code");
    openapiFields.add("ndc_quantity");
    openapiFields.add("ndc_units");
    openapiFields.add("office");
    openapiFields.add("payer_id");
    openapiFields.add("picklist_category");
    openapiFields.add("plan_name");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DoctorFeeSchedule
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DoctorFeeSchedule.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DoctorFeeSchedule is not found in the empty JSON string", DoctorFeeSchedule.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DoctorFeeSchedule.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DoctorFeeSchedule` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("billing_description") != null && !jsonObj.get("billing_description").isJsonNull()) && !jsonObj.get("billing_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `billing_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("billing_description").toString()));
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
      }
      if ((jsonObj.get("code_type") != null && !jsonObj.get("code_type").isJsonNull()) && !jsonObj.get("code_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code_type").toString()));
      }
      // validate the optional field `code_type`
      if (jsonObj.get("code_type") != null && !jsonObj.get("code_type").isJsonNull()) {
        CodeTypeEnum.validateJsonElement(jsonObj.get("code_type"));
      }
      if ((jsonObj.get("cpt_hcpcs_modifier1") != null && !jsonObj.get("cpt_hcpcs_modifier1").isJsonNull()) && !jsonObj.get("cpt_hcpcs_modifier1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cpt_hcpcs_modifier1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cpt_hcpcs_modifier1").toString()));
      }
      if ((jsonObj.get("cpt_hcpcs_modifier2") != null && !jsonObj.get("cpt_hcpcs_modifier2").isJsonNull()) && !jsonObj.get("cpt_hcpcs_modifier2").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cpt_hcpcs_modifier2` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cpt_hcpcs_modifier2").toString()));
      }
      // validate the optional field `cpt_hcpcs_modifier2`
      if (jsonObj.get("cpt_hcpcs_modifier2") != null && !jsonObj.get("cpt_hcpcs_modifier2").isJsonNull()) {
        CptHcpcsModifier2Enum.validateJsonElement(jsonObj.get("cpt_hcpcs_modifier2"));
      }
      if ((jsonObj.get("cpt_hcpcs_modifier3") != null && !jsonObj.get("cpt_hcpcs_modifier3").isJsonNull()) && !jsonObj.get("cpt_hcpcs_modifier3").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cpt_hcpcs_modifier3` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cpt_hcpcs_modifier3").toString()));
      }
      // validate the optional field `cpt_hcpcs_modifier3`
      if (jsonObj.get("cpt_hcpcs_modifier3") != null && !jsonObj.get("cpt_hcpcs_modifier3").isJsonNull()) {
        CptHcpcsModifier3Enum.validateJsonElement(jsonObj.get("cpt_hcpcs_modifier3"));
      }
      if ((jsonObj.get("cpt_hcpcs_modifier4") != null && !jsonObj.get("cpt_hcpcs_modifier4").isJsonNull()) && !jsonObj.get("cpt_hcpcs_modifier4").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cpt_hcpcs_modifier4` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cpt_hcpcs_modifier4").toString()));
      }
      // validate the optional field `cpt_hcpcs_modifier4`
      if (jsonObj.get("cpt_hcpcs_modifier4") != null && !jsonObj.get("cpt_hcpcs_modifier4").isJsonNull()) {
        CptHcpcsModifier4Enum.validateJsonElement(jsonObj.get("cpt_hcpcs_modifier4"));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("ndc_code") != null && !jsonObj.get("ndc_code").isJsonNull()) && !jsonObj.get("ndc_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ndc_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ndc_code").toString()));
      }
      if ((jsonObj.get("ndc_units") != null && !jsonObj.get("ndc_units").isJsonNull()) && !jsonObj.get("ndc_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ndc_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ndc_units").toString()));
      }
      // validate the optional field `ndc_units`
      if (jsonObj.get("ndc_units") != null && !jsonObj.get("ndc_units").isJsonNull()) {
        NdcUnitsEnum.validateJsonElement(jsonObj.get("ndc_units"));
      }
      if ((jsonObj.get("payer_id") != null && !jsonObj.get("payer_id").isJsonNull()) && !jsonObj.get("payer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payer_id").toString()));
      }
      if ((jsonObj.get("picklist_category") != null && !jsonObj.get("picklist_category").isJsonNull()) && !jsonObj.get("picklist_category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `picklist_category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("picklist_category").toString()));
      }
      if ((jsonObj.get("plan_name") != null && !jsonObj.get("plan_name").isJsonNull()) && !jsonObj.get("plan_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `plan_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("plan_name").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DoctorFeeSchedule.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DoctorFeeSchedule' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DoctorFeeSchedule> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DoctorFeeSchedule.class));

       return (TypeAdapter<T>) new TypeAdapter<DoctorFeeSchedule>() {
           @Override
           public void write(JsonWriter out, DoctorFeeSchedule value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DoctorFeeSchedule read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DoctorFeeSchedule given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DoctorFeeSchedule
   * @throws IOException if the JSON string is invalid with respect to DoctorFeeSchedule
   */
  public static DoctorFeeSchedule fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DoctorFeeSchedule.class);
  }

  /**
   * Convert an instance of DoctorFeeSchedule to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

