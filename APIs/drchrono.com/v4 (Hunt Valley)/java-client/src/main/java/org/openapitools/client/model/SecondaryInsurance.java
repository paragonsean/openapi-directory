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
 * **Warning:** Changing insurance information may make past appointments unbillable. Insurance data is also **unvalidated**; you should use the [&#x60;/api/insurances&#x60;](#apiinsurances) endpoint to find the appropriate insurance payer.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SecondaryInsurance {
  public static final String SERIALIZED_NAME_INSURANCE_CLAIM_OFFICE_NUMBER = "insurance_claim_office_number";
  @SerializedName(SERIALIZED_NAME_INSURANCE_CLAIM_OFFICE_NUMBER)
  private String insuranceClaimOfficeNumber;

  public static final String SERIALIZED_NAME_INSURANCE_COMPANY = "insurance_company";
  @SerializedName(SERIALIZED_NAME_INSURANCE_COMPANY)
  private String insuranceCompany;

  public static final String SERIALIZED_NAME_INSURANCE_GROUP_NAME = "insurance_group_name";
  @SerializedName(SERIALIZED_NAME_INSURANCE_GROUP_NAME)
  private String insuranceGroupName;

  public static final String SERIALIZED_NAME_INSURANCE_GROUP_NUMBER = "insurance_group_number";
  @SerializedName(SERIALIZED_NAME_INSURANCE_GROUP_NUMBER)
  private String insuranceGroupNumber;

  public static final String SERIALIZED_NAME_INSURANCE_ID_NUMBER = "insurance_id_number";
  @SerializedName(SERIALIZED_NAME_INSURANCE_ID_NUMBER)
  private String insuranceIdNumber;

  public static final String SERIALIZED_NAME_INSURANCE_PAYER_ID = "insurance_payer_id";
  @SerializedName(SERIALIZED_NAME_INSURANCE_PAYER_ID)
  private String insurancePayerId;

  public static final String SERIALIZED_NAME_INSURANCE_PLAN_NAME = "insurance_plan_name";
  @SerializedName(SERIALIZED_NAME_INSURANCE_PLAN_NAME)
  private String insurancePlanName;

  /**
   * 
   */
  @JsonAdapter(InsurancePlanTypeEnum.Adapter.class)
  public enum InsurancePlanTypeEnum {
    EMPTY(""),
    
    AM("AM"),
    
    BL("BL"),
    
    CH("CH"),
    
    CI("CI"),
    
    _17("17"),
    
    DS("DS"),
    
    _14("14"),
    
    FI("FI"),
    
    HM("HM"),
    
    _16("16"),
    
    _15("15"),
    
    LM("LM"),
    
    MC("MC"),
    
    MA("MA"),
    
    MB("MB"),
    
    ZZ("ZZ"),
    
    OF("OF"),
    
    _11("11"),
    
    _13("13"),
    
    _12("12"),
    
    TV("TV"),
    
    VA("VA"),
    
    WC("WC");

    private String value;

    InsurancePlanTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static InsurancePlanTypeEnum fromValue(String value) {
      for (InsurancePlanTypeEnum b : InsurancePlanTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<InsurancePlanTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final InsurancePlanTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public InsurancePlanTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return InsurancePlanTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      InsurancePlanTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_INSURANCE_PLAN_TYPE = "insurance_plan_type";
  @SerializedName(SERIALIZED_NAME_INSURANCE_PLAN_TYPE)
  private InsurancePlanTypeEnum insurancePlanType;

  public static final String SERIALIZED_NAME_IS_SUBSCRIBER_THE_PATIENT = "is_subscriber_the_patient";
  @SerializedName(SERIALIZED_NAME_IS_SUBSCRIBER_THE_PATIENT)
  private Boolean isSubscriberThePatient;

  /**
   * HCFA/1500 individual relationship code
   */
  @JsonAdapter(PatientRelationshipToSubscriberEnum.Adapter.class)
  public enum PatientRelationshipToSubscriberEnum {
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

    PatientRelationshipToSubscriberEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PatientRelationshipToSubscriberEnum fromValue(String value) {
      for (PatientRelationshipToSubscriberEnum b : PatientRelationshipToSubscriberEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PatientRelationshipToSubscriberEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PatientRelationshipToSubscriberEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PatientRelationshipToSubscriberEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PatientRelationshipToSubscriberEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PatientRelationshipToSubscriberEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PATIENT_RELATIONSHIP_TO_SUBSCRIBER = "patient_relationship_to_subscriber";
  @SerializedName(SERIALIZED_NAME_PATIENT_RELATIONSHIP_TO_SUBSCRIBER)
  private PatientRelationshipToSubscriberEnum patientRelationshipToSubscriber;

  public static final String SERIALIZED_NAME_PHOTO_BACK = "photo_back";
  @SerializedName(SERIALIZED_NAME_PHOTO_BACK)
  private String photoBack;

  public static final String SERIALIZED_NAME_PHOTO_FRONT = "photo_front";
  @SerializedName(SERIALIZED_NAME_PHOTO_FRONT)
  private String photoFront;

  public static final String SERIALIZED_NAME_SUBSCRIBER_ADDRESS = "subscriber_address";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_ADDRESS)
  private String subscriberAddress;

  public static final String SERIALIZED_NAME_SUBSCRIBER_CITY = "subscriber_city";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_CITY)
  private String subscriberCity;

  /**
   * Two-letter country code
   */
  @JsonAdapter(SubscriberCountryEnum.Adapter.class)
  public enum SubscriberCountryEnum {
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

    SubscriberCountryEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SubscriberCountryEnum fromValue(String value) {
      for (SubscriberCountryEnum b : SubscriberCountryEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SubscriberCountryEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SubscriberCountryEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SubscriberCountryEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SubscriberCountryEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SubscriberCountryEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SUBSCRIBER_COUNTRY = "subscriber_country";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_COUNTRY)
  private SubscriberCountryEnum subscriberCountry;

  public static final String SERIALIZED_NAME_SUBSCRIBER_DATE_OF_BIRTH = "subscriber_date_of_birth";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_DATE_OF_BIRTH)
  private String subscriberDateOfBirth;

  public static final String SERIALIZED_NAME_SUBSCRIBER_FIRST_NAME = "subscriber_first_name";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_FIRST_NAME)
  private String subscriberFirstName;

  /**
   * One of &#x60;\&quot;Male\&quot;&#x60; or &#x60;\&quot;Female\&quot;&#x60;
   */
  @JsonAdapter(SubscriberGenderEnum.Adapter.class)
  public enum SubscriberGenderEnum {
    EMPTY(""),
    
    MALE("Male"),
    
    FEMALE("Female"),
    
    OTHER("Other"),
    
    UNK("UNK"),
    
    ASKU("ASKU");

    private String value;

    SubscriberGenderEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SubscriberGenderEnum fromValue(String value) {
      for (SubscriberGenderEnum b : SubscriberGenderEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SubscriberGenderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SubscriberGenderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SubscriberGenderEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SubscriberGenderEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SubscriberGenderEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SUBSCRIBER_GENDER = "subscriber_gender";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_GENDER)
  private SubscriberGenderEnum subscriberGender;

  public static final String SERIALIZED_NAME_SUBSCRIBER_LAST_NAME = "subscriber_last_name";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_LAST_NAME)
  private String subscriberLastName;

  public static final String SERIALIZED_NAME_SUBSCRIBER_MIDDLE_NAME = "subscriber_middle_name";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_MIDDLE_NAME)
  private String subscriberMiddleName;

  public static final String SERIALIZED_NAME_SUBSCRIBER_SOCIAL_SECURITY = "subscriber_social_security";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_SOCIAL_SECURITY)
  private String subscriberSocialSecurity;

  /**
   * Two-letter state code
   */
  @JsonAdapter(SubscriberStateEnum.Adapter.class)
  public enum SubscriberStateEnum {
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

    SubscriberStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SubscriberStateEnum fromValue(String value) {
      for (SubscriberStateEnum b : SubscriberStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SubscriberStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SubscriberStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SubscriberStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SubscriberStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SubscriberStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SUBSCRIBER_STATE = "subscriber_state";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_STATE)
  private SubscriberStateEnum subscriberState;

  public static final String SERIALIZED_NAME_SUBSCRIBER_SUFFIX = "subscriber_suffix";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_SUFFIX)
  private String subscriberSuffix;

  public static final String SERIALIZED_NAME_SUBSCRIBER_ZIP_CODE = "subscriber_zip_code";
  @SerializedName(SERIALIZED_NAME_SUBSCRIBER_ZIP_CODE)
  private String subscriberZipCode;

  public SecondaryInsurance() {
  }

  public SecondaryInsurance insuranceClaimOfficeNumber(String insuranceClaimOfficeNumber) {
    this.insuranceClaimOfficeNumber = insuranceClaimOfficeNumber;
    return this;
  }

  /**
   * Insurance office phone number
   * @return insuranceClaimOfficeNumber
   */
  @javax.annotation.Nullable
  public String getInsuranceClaimOfficeNumber() {
    return insuranceClaimOfficeNumber;
  }

  public void setInsuranceClaimOfficeNumber(String insuranceClaimOfficeNumber) {
    this.insuranceClaimOfficeNumber = insuranceClaimOfficeNumber;
  }


  public SecondaryInsurance insuranceCompany(String insuranceCompany) {
    this.insuranceCompany = insuranceCompany;
    return this;
  }

  /**
   * 
   * @return insuranceCompany
   */
  @javax.annotation.Nullable
  public String getInsuranceCompany() {
    return insuranceCompany;
  }

  public void setInsuranceCompany(String insuranceCompany) {
    this.insuranceCompany = insuranceCompany;
  }


  public SecondaryInsurance insuranceGroupName(String insuranceGroupName) {
    this.insuranceGroupName = insuranceGroupName;
    return this;
  }

  /**
   * 
   * @return insuranceGroupName
   */
  @javax.annotation.Nullable
  public String getInsuranceGroupName() {
    return insuranceGroupName;
  }

  public void setInsuranceGroupName(String insuranceGroupName) {
    this.insuranceGroupName = insuranceGroupName;
  }


  public SecondaryInsurance insuranceGroupNumber(String insuranceGroupNumber) {
    this.insuranceGroupNumber = insuranceGroupNumber;
    return this;
  }

  /**
   * 
   * @return insuranceGroupNumber
   */
  @javax.annotation.Nullable
  public String getInsuranceGroupNumber() {
    return insuranceGroupNumber;
  }

  public void setInsuranceGroupNumber(String insuranceGroupNumber) {
    this.insuranceGroupNumber = insuranceGroupNumber;
  }


  public SecondaryInsurance insuranceIdNumber(String insuranceIdNumber) {
    this.insuranceIdNumber = insuranceIdNumber;
    return this;
  }

  /**
   * 
   * @return insuranceIdNumber
   */
  @javax.annotation.Nullable
  public String getInsuranceIdNumber() {
    return insuranceIdNumber;
  }

  public void setInsuranceIdNumber(String insuranceIdNumber) {
    this.insuranceIdNumber = insuranceIdNumber;
  }


  public SecondaryInsurance insurancePayerId(String insurancePayerId) {
    this.insurancePayerId = insurancePayerId;
    return this;
  }

  /**
   * 
   * @return insurancePayerId
   */
  @javax.annotation.Nullable
  public String getInsurancePayerId() {
    return insurancePayerId;
  }

  public void setInsurancePayerId(String insurancePayerId) {
    this.insurancePayerId = insurancePayerId;
  }


  public SecondaryInsurance insurancePlanName(String insurancePlanName) {
    this.insurancePlanName = insurancePlanName;
    return this;
  }

  /**
   * Name of insurance plan.
   * @return insurancePlanName
   */
  @javax.annotation.Nullable
  public String getInsurancePlanName() {
    return insurancePlanName;
  }

  public void setInsurancePlanName(String insurancePlanName) {
    this.insurancePlanName = insurancePlanName;
  }


  public SecondaryInsurance insurancePlanType(InsurancePlanTypeEnum insurancePlanType) {
    this.insurancePlanType = insurancePlanType;
    return this;
  }

  /**
   * 
   * @return insurancePlanType
   */
  @javax.annotation.Nullable
  public InsurancePlanTypeEnum getInsurancePlanType() {
    return insurancePlanType;
  }

  public void setInsurancePlanType(InsurancePlanTypeEnum insurancePlanType) {
    this.insurancePlanType = insurancePlanType;
  }


  public SecondaryInsurance isSubscriberThePatient(Boolean isSubscriberThePatient) {
    this.isSubscriberThePatient = isSubscriberThePatient;
    return this;
  }

  /**
   * True if the insurance policy is under patient&#39;s own name. Defaults to true
   * @return isSubscriberThePatient
   */
  @javax.annotation.Nullable
  public Boolean getIsSubscriberThePatient() {
    return isSubscriberThePatient;
  }

  public void setIsSubscriberThePatient(Boolean isSubscriberThePatient) {
    this.isSubscriberThePatient = isSubscriberThePatient;
  }


  public SecondaryInsurance patientRelationshipToSubscriber(PatientRelationshipToSubscriberEnum patientRelationshipToSubscriber) {
    this.patientRelationshipToSubscriber = patientRelationshipToSubscriber;
    return this;
  }

  /**
   * HCFA/1500 individual relationship code
   * @return patientRelationshipToSubscriber
   */
  @javax.annotation.Nullable
  public PatientRelationshipToSubscriberEnum getPatientRelationshipToSubscriber() {
    return patientRelationshipToSubscriber;
  }

  public void setPatientRelationshipToSubscriber(PatientRelationshipToSubscriberEnum patientRelationshipToSubscriber) {
    this.patientRelationshipToSubscriber = patientRelationshipToSubscriber;
  }


  public SecondaryInsurance photoBack(String photoBack) {
    this.photoBack = photoBack;
    return this;
  }

  /**
   * Photo of back of insurance card
   * @return photoBack
   */
  @javax.annotation.Nullable
  public String getPhotoBack() {
    return photoBack;
  }

  public void setPhotoBack(String photoBack) {
    this.photoBack = photoBack;
  }


  public SecondaryInsurance photoFront(String photoFront) {
    this.photoFront = photoFront;
    return this;
  }

  /**
   * Photo of front of insurance card
   * @return photoFront
   */
  @javax.annotation.Nullable
  public String getPhotoFront() {
    return photoFront;
  }

  public void setPhotoFront(String photoFront) {
    this.photoFront = photoFront;
  }


  public SecondaryInsurance subscriberAddress(String subscriberAddress) {
    this.subscriberAddress = subscriberAddress;
    return this;
  }

  /**
   * 
   * @return subscriberAddress
   */
  @javax.annotation.Nullable
  public String getSubscriberAddress() {
    return subscriberAddress;
  }

  public void setSubscriberAddress(String subscriberAddress) {
    this.subscriberAddress = subscriberAddress;
  }


  public SecondaryInsurance subscriberCity(String subscriberCity) {
    this.subscriberCity = subscriberCity;
    return this;
  }

  /**
   * 
   * @return subscriberCity
   */
  @javax.annotation.Nullable
  public String getSubscriberCity() {
    return subscriberCity;
  }

  public void setSubscriberCity(String subscriberCity) {
    this.subscriberCity = subscriberCity;
  }


  public SecondaryInsurance subscriberCountry(SubscriberCountryEnum subscriberCountry) {
    this.subscriberCountry = subscriberCountry;
    return this;
  }

  /**
   * Two-letter country code
   * @return subscriberCountry
   */
  @javax.annotation.Nullable
  public SubscriberCountryEnum getSubscriberCountry() {
    return subscriberCountry;
  }

  public void setSubscriberCountry(SubscriberCountryEnum subscriberCountry) {
    this.subscriberCountry = subscriberCountry;
  }


  public SecondaryInsurance subscriberDateOfBirth(String subscriberDateOfBirth) {
    this.subscriberDateOfBirth = subscriberDateOfBirth;
    return this;
  }

  /**
   * 
   * @return subscriberDateOfBirth
   */
  @javax.annotation.Nullable
  public String getSubscriberDateOfBirth() {
    return subscriberDateOfBirth;
  }

  public void setSubscriberDateOfBirth(String subscriberDateOfBirth) {
    this.subscriberDateOfBirth = subscriberDateOfBirth;
  }


  public SecondaryInsurance subscriberFirstName(String subscriberFirstName) {
    this.subscriberFirstName = subscriberFirstName;
    return this;
  }

  /**
   * 
   * @return subscriberFirstName
   */
  @javax.annotation.Nullable
  public String getSubscriberFirstName() {
    return subscriberFirstName;
  }

  public void setSubscriberFirstName(String subscriberFirstName) {
    this.subscriberFirstName = subscriberFirstName;
  }


  public SecondaryInsurance subscriberGender(SubscriberGenderEnum subscriberGender) {
    this.subscriberGender = subscriberGender;
    return this;
  }

  /**
   * One of &#x60;\&quot;Male\&quot;&#x60; or &#x60;\&quot;Female\&quot;&#x60;
   * @return subscriberGender
   */
  @javax.annotation.Nullable
  public SubscriberGenderEnum getSubscriberGender() {
    return subscriberGender;
  }

  public void setSubscriberGender(SubscriberGenderEnum subscriberGender) {
    this.subscriberGender = subscriberGender;
  }


  public SecondaryInsurance subscriberLastName(String subscriberLastName) {
    this.subscriberLastName = subscriberLastName;
    return this;
  }

  /**
   * 
   * @return subscriberLastName
   */
  @javax.annotation.Nullable
  public String getSubscriberLastName() {
    return subscriberLastName;
  }

  public void setSubscriberLastName(String subscriberLastName) {
    this.subscriberLastName = subscriberLastName;
  }


  public SecondaryInsurance subscriberMiddleName(String subscriberMiddleName) {
    this.subscriberMiddleName = subscriberMiddleName;
    return this;
  }

  /**
   * 
   * @return subscriberMiddleName
   */
  @javax.annotation.Nullable
  public String getSubscriberMiddleName() {
    return subscriberMiddleName;
  }

  public void setSubscriberMiddleName(String subscriberMiddleName) {
    this.subscriberMiddleName = subscriberMiddleName;
  }


  public SecondaryInsurance subscriberSocialSecurity(String subscriberSocialSecurity) {
    this.subscriberSocialSecurity = subscriberSocialSecurity;
    return this;
  }

  /**
   * 
   * @return subscriberSocialSecurity
   */
  @javax.annotation.Nullable
  public String getSubscriberSocialSecurity() {
    return subscriberSocialSecurity;
  }

  public void setSubscriberSocialSecurity(String subscriberSocialSecurity) {
    this.subscriberSocialSecurity = subscriberSocialSecurity;
  }


  public SecondaryInsurance subscriberState(SubscriberStateEnum subscriberState) {
    this.subscriberState = subscriberState;
    return this;
  }

  /**
   * Two-letter state code
   * @return subscriberState
   */
  @javax.annotation.Nullable
  public SubscriberStateEnum getSubscriberState() {
    return subscriberState;
  }

  public void setSubscriberState(SubscriberStateEnum subscriberState) {
    this.subscriberState = subscriberState;
  }


  public SecondaryInsurance subscriberSuffix(String subscriberSuffix) {
    this.subscriberSuffix = subscriberSuffix;
    return this;
  }

  /**
   * E.g. &#x60;\&quot;II\&quot;&#x60; or &#x60;\&quot;III\&quot;&#x60;
   * @return subscriberSuffix
   */
  @javax.annotation.Nullable
  public String getSubscriberSuffix() {
    return subscriberSuffix;
  }

  public void setSubscriberSuffix(String subscriberSuffix) {
    this.subscriberSuffix = subscriberSuffix;
  }


  public SecondaryInsurance subscriberZipCode(String subscriberZipCode) {
    this.subscriberZipCode = subscriberZipCode;
    return this;
  }

  /**
   * 
   * @return subscriberZipCode
   */
  @javax.annotation.Nullable
  public String getSubscriberZipCode() {
    return subscriberZipCode;
  }

  public void setSubscriberZipCode(String subscriberZipCode) {
    this.subscriberZipCode = subscriberZipCode;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SecondaryInsurance secondaryInsurance = (SecondaryInsurance) o;
    return Objects.equals(this.insuranceClaimOfficeNumber, secondaryInsurance.insuranceClaimOfficeNumber) &&
        Objects.equals(this.insuranceCompany, secondaryInsurance.insuranceCompany) &&
        Objects.equals(this.insuranceGroupName, secondaryInsurance.insuranceGroupName) &&
        Objects.equals(this.insuranceGroupNumber, secondaryInsurance.insuranceGroupNumber) &&
        Objects.equals(this.insuranceIdNumber, secondaryInsurance.insuranceIdNumber) &&
        Objects.equals(this.insurancePayerId, secondaryInsurance.insurancePayerId) &&
        Objects.equals(this.insurancePlanName, secondaryInsurance.insurancePlanName) &&
        Objects.equals(this.insurancePlanType, secondaryInsurance.insurancePlanType) &&
        Objects.equals(this.isSubscriberThePatient, secondaryInsurance.isSubscriberThePatient) &&
        Objects.equals(this.patientRelationshipToSubscriber, secondaryInsurance.patientRelationshipToSubscriber) &&
        Objects.equals(this.photoBack, secondaryInsurance.photoBack) &&
        Objects.equals(this.photoFront, secondaryInsurance.photoFront) &&
        Objects.equals(this.subscriberAddress, secondaryInsurance.subscriberAddress) &&
        Objects.equals(this.subscriberCity, secondaryInsurance.subscriberCity) &&
        Objects.equals(this.subscriberCountry, secondaryInsurance.subscriberCountry) &&
        Objects.equals(this.subscriberDateOfBirth, secondaryInsurance.subscriberDateOfBirth) &&
        Objects.equals(this.subscriberFirstName, secondaryInsurance.subscriberFirstName) &&
        Objects.equals(this.subscriberGender, secondaryInsurance.subscriberGender) &&
        Objects.equals(this.subscriberLastName, secondaryInsurance.subscriberLastName) &&
        Objects.equals(this.subscriberMiddleName, secondaryInsurance.subscriberMiddleName) &&
        Objects.equals(this.subscriberSocialSecurity, secondaryInsurance.subscriberSocialSecurity) &&
        Objects.equals(this.subscriberState, secondaryInsurance.subscriberState) &&
        Objects.equals(this.subscriberSuffix, secondaryInsurance.subscriberSuffix) &&
        Objects.equals(this.subscriberZipCode, secondaryInsurance.subscriberZipCode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(insuranceClaimOfficeNumber, insuranceCompany, insuranceGroupName, insuranceGroupNumber, insuranceIdNumber, insurancePayerId, insurancePlanName, insurancePlanType, isSubscriberThePatient, patientRelationshipToSubscriber, photoBack, photoFront, subscriberAddress, subscriberCity, subscriberCountry, subscriberDateOfBirth, subscriberFirstName, subscriberGender, subscriberLastName, subscriberMiddleName, subscriberSocialSecurity, subscriberState, subscriberSuffix, subscriberZipCode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SecondaryInsurance {\n");
    sb.append("    insuranceClaimOfficeNumber: ").append(toIndentedString(insuranceClaimOfficeNumber)).append("\n");
    sb.append("    insuranceCompany: ").append(toIndentedString(insuranceCompany)).append("\n");
    sb.append("    insuranceGroupName: ").append(toIndentedString(insuranceGroupName)).append("\n");
    sb.append("    insuranceGroupNumber: ").append(toIndentedString(insuranceGroupNumber)).append("\n");
    sb.append("    insuranceIdNumber: ").append(toIndentedString(insuranceIdNumber)).append("\n");
    sb.append("    insurancePayerId: ").append(toIndentedString(insurancePayerId)).append("\n");
    sb.append("    insurancePlanName: ").append(toIndentedString(insurancePlanName)).append("\n");
    sb.append("    insurancePlanType: ").append(toIndentedString(insurancePlanType)).append("\n");
    sb.append("    isSubscriberThePatient: ").append(toIndentedString(isSubscriberThePatient)).append("\n");
    sb.append("    patientRelationshipToSubscriber: ").append(toIndentedString(patientRelationshipToSubscriber)).append("\n");
    sb.append("    photoBack: ").append(toIndentedString(photoBack)).append("\n");
    sb.append("    photoFront: ").append(toIndentedString(photoFront)).append("\n");
    sb.append("    subscriberAddress: ").append(toIndentedString(subscriberAddress)).append("\n");
    sb.append("    subscriberCity: ").append(toIndentedString(subscriberCity)).append("\n");
    sb.append("    subscriberCountry: ").append(toIndentedString(subscriberCountry)).append("\n");
    sb.append("    subscriberDateOfBirth: ").append(toIndentedString(subscriberDateOfBirth)).append("\n");
    sb.append("    subscriberFirstName: ").append(toIndentedString(subscriberFirstName)).append("\n");
    sb.append("    subscriberGender: ").append(toIndentedString(subscriberGender)).append("\n");
    sb.append("    subscriberLastName: ").append(toIndentedString(subscriberLastName)).append("\n");
    sb.append("    subscriberMiddleName: ").append(toIndentedString(subscriberMiddleName)).append("\n");
    sb.append("    subscriberSocialSecurity: ").append(toIndentedString(subscriberSocialSecurity)).append("\n");
    sb.append("    subscriberState: ").append(toIndentedString(subscriberState)).append("\n");
    sb.append("    subscriberSuffix: ").append(toIndentedString(subscriberSuffix)).append("\n");
    sb.append("    subscriberZipCode: ").append(toIndentedString(subscriberZipCode)).append("\n");
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
    openapiFields.add("insurance_claim_office_number");
    openapiFields.add("insurance_company");
    openapiFields.add("insurance_group_name");
    openapiFields.add("insurance_group_number");
    openapiFields.add("insurance_id_number");
    openapiFields.add("insurance_payer_id");
    openapiFields.add("insurance_plan_name");
    openapiFields.add("insurance_plan_type");
    openapiFields.add("is_subscriber_the_patient");
    openapiFields.add("patient_relationship_to_subscriber");
    openapiFields.add("photo_back");
    openapiFields.add("photo_front");
    openapiFields.add("subscriber_address");
    openapiFields.add("subscriber_city");
    openapiFields.add("subscriber_country");
    openapiFields.add("subscriber_date_of_birth");
    openapiFields.add("subscriber_first_name");
    openapiFields.add("subscriber_gender");
    openapiFields.add("subscriber_last_name");
    openapiFields.add("subscriber_middle_name");
    openapiFields.add("subscriber_social_security");
    openapiFields.add("subscriber_state");
    openapiFields.add("subscriber_suffix");
    openapiFields.add("subscriber_zip_code");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SecondaryInsurance
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SecondaryInsurance.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SecondaryInsurance is not found in the empty JSON string", SecondaryInsurance.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SecondaryInsurance.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SecondaryInsurance` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("insurance_claim_office_number") != null && !jsonObj.get("insurance_claim_office_number").isJsonNull()) && !jsonObj.get("insurance_claim_office_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_claim_office_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_claim_office_number").toString()));
      }
      if ((jsonObj.get("insurance_company") != null && !jsonObj.get("insurance_company").isJsonNull()) && !jsonObj.get("insurance_company").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_company` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_company").toString()));
      }
      if ((jsonObj.get("insurance_group_name") != null && !jsonObj.get("insurance_group_name").isJsonNull()) && !jsonObj.get("insurance_group_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_group_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_group_name").toString()));
      }
      if ((jsonObj.get("insurance_group_number") != null && !jsonObj.get("insurance_group_number").isJsonNull()) && !jsonObj.get("insurance_group_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_group_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_group_number").toString()));
      }
      if ((jsonObj.get("insurance_id_number") != null && !jsonObj.get("insurance_id_number").isJsonNull()) && !jsonObj.get("insurance_id_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_id_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_id_number").toString()));
      }
      if ((jsonObj.get("insurance_payer_id") != null && !jsonObj.get("insurance_payer_id").isJsonNull()) && !jsonObj.get("insurance_payer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_payer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_payer_id").toString()));
      }
      if ((jsonObj.get("insurance_plan_name") != null && !jsonObj.get("insurance_plan_name").isJsonNull()) && !jsonObj.get("insurance_plan_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_plan_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_plan_name").toString()));
      }
      if ((jsonObj.get("insurance_plan_type") != null && !jsonObj.get("insurance_plan_type").isJsonNull()) && !jsonObj.get("insurance_plan_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `insurance_plan_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("insurance_plan_type").toString()));
      }
      // validate the optional field `insurance_plan_type`
      if (jsonObj.get("insurance_plan_type") != null && !jsonObj.get("insurance_plan_type").isJsonNull()) {
        InsurancePlanTypeEnum.validateJsonElement(jsonObj.get("insurance_plan_type"));
      }
      if ((jsonObj.get("patient_relationship_to_subscriber") != null && !jsonObj.get("patient_relationship_to_subscriber").isJsonNull()) && !jsonObj.get("patient_relationship_to_subscriber").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patient_relationship_to_subscriber` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patient_relationship_to_subscriber").toString()));
      }
      // validate the optional field `patient_relationship_to_subscriber`
      if (jsonObj.get("patient_relationship_to_subscriber") != null && !jsonObj.get("patient_relationship_to_subscriber").isJsonNull()) {
        PatientRelationshipToSubscriberEnum.validateJsonElement(jsonObj.get("patient_relationship_to_subscriber"));
      }
      if ((jsonObj.get("photo_back") != null && !jsonObj.get("photo_back").isJsonNull()) && !jsonObj.get("photo_back").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `photo_back` to be a primitive type in the JSON string but got `%s`", jsonObj.get("photo_back").toString()));
      }
      if ((jsonObj.get("photo_front") != null && !jsonObj.get("photo_front").isJsonNull()) && !jsonObj.get("photo_front").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `photo_front` to be a primitive type in the JSON string but got `%s`", jsonObj.get("photo_front").toString()));
      }
      if ((jsonObj.get("subscriber_address") != null && !jsonObj.get("subscriber_address").isJsonNull()) && !jsonObj.get("subscriber_address").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_address` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_address").toString()));
      }
      if ((jsonObj.get("subscriber_city") != null && !jsonObj.get("subscriber_city").isJsonNull()) && !jsonObj.get("subscriber_city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_city").toString()));
      }
      if ((jsonObj.get("subscriber_country") != null && !jsonObj.get("subscriber_country").isJsonNull()) && !jsonObj.get("subscriber_country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_country").toString()));
      }
      // validate the optional field `subscriber_country`
      if (jsonObj.get("subscriber_country") != null && !jsonObj.get("subscriber_country").isJsonNull()) {
        SubscriberCountryEnum.validateJsonElement(jsonObj.get("subscriber_country"));
      }
      if ((jsonObj.get("subscriber_date_of_birth") != null && !jsonObj.get("subscriber_date_of_birth").isJsonNull()) && !jsonObj.get("subscriber_date_of_birth").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_date_of_birth` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_date_of_birth").toString()));
      }
      if ((jsonObj.get("subscriber_first_name") != null && !jsonObj.get("subscriber_first_name").isJsonNull()) && !jsonObj.get("subscriber_first_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_first_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_first_name").toString()));
      }
      if ((jsonObj.get("subscriber_gender") != null && !jsonObj.get("subscriber_gender").isJsonNull()) && !jsonObj.get("subscriber_gender").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_gender` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_gender").toString()));
      }
      // validate the optional field `subscriber_gender`
      if (jsonObj.get("subscriber_gender") != null && !jsonObj.get("subscriber_gender").isJsonNull()) {
        SubscriberGenderEnum.validateJsonElement(jsonObj.get("subscriber_gender"));
      }
      if ((jsonObj.get("subscriber_last_name") != null && !jsonObj.get("subscriber_last_name").isJsonNull()) && !jsonObj.get("subscriber_last_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_last_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_last_name").toString()));
      }
      if ((jsonObj.get("subscriber_middle_name") != null && !jsonObj.get("subscriber_middle_name").isJsonNull()) && !jsonObj.get("subscriber_middle_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_middle_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_middle_name").toString()));
      }
      if ((jsonObj.get("subscriber_social_security") != null && !jsonObj.get("subscriber_social_security").isJsonNull()) && !jsonObj.get("subscriber_social_security").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_social_security` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_social_security").toString()));
      }
      if ((jsonObj.get("subscriber_state") != null && !jsonObj.get("subscriber_state").isJsonNull()) && !jsonObj.get("subscriber_state").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_state` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_state").toString()));
      }
      // validate the optional field `subscriber_state`
      if (jsonObj.get("subscriber_state") != null && !jsonObj.get("subscriber_state").isJsonNull()) {
        SubscriberStateEnum.validateJsonElement(jsonObj.get("subscriber_state"));
      }
      if ((jsonObj.get("subscriber_suffix") != null && !jsonObj.get("subscriber_suffix").isJsonNull()) && !jsonObj.get("subscriber_suffix").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_suffix` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_suffix").toString()));
      }
      if ((jsonObj.get("subscriber_zip_code") != null && !jsonObj.get("subscriber_zip_code").isJsonNull()) && !jsonObj.get("subscriber_zip_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscriber_zip_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscriber_zip_code").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SecondaryInsurance.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SecondaryInsurance' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SecondaryInsurance> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SecondaryInsurance.class));

       return (TypeAdapter<T>) new TypeAdapter<SecondaryInsurance>() {
           @Override
           public void write(JsonWriter out, SecondaryInsurance value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SecondaryInsurance read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SecondaryInsurance given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SecondaryInsurance
   * @throws IOException if the JSON string is invalid with respect to SecondaryInsurance
   */
  public static SecondaryInsurance fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SecondaryInsurance.class);
  }

  /**
   * Convert an instance of SecondaryInsurance to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

