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
 * LineItemTransaction
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LineItemTransaction {
  public static final String SERIALIZED_NAME_ADJUSTMENT = "adjustment";
  @SerializedName(SERIALIZED_NAME_ADJUSTMENT)
  private BigDecimal adjustment;

  /**
   * Group code for adjustment
   */
  @JsonAdapter(AdjustmentGroupCodeEnum.Adapter.class)
  public enum AdjustmentGroupCodeEnum {
    EMPTY(""),
    
    CO("CO"),
    
    OA("OA"),
    
    PI("PI"),
    
    PR("PR");

    private String value;

    AdjustmentGroupCodeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AdjustmentGroupCodeEnum fromValue(String value) {
      for (AdjustmentGroupCodeEnum b : AdjustmentGroupCodeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AdjustmentGroupCodeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AdjustmentGroupCodeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AdjustmentGroupCodeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AdjustmentGroupCodeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AdjustmentGroupCodeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ADJUSTMENT_GROUP_CODE = "adjustment_group_code";
  @SerializedName(SERIALIZED_NAME_ADJUSTMENT_GROUP_CODE)
  private AdjustmentGroupCodeEnum adjustmentGroupCode;

  /**
   * Reason for adjustment
   */
  @JsonAdapter(AdjustmentReasonEnum.Adapter.class)
  public enum AdjustmentReasonEnum {
    _3("-3"),
    
    _2("-2"),
    
    _4("-4"),
    
    _1("-1"),
    
    _0("0"),
    
    _12("1"),
    
    _22("2"),
    
    _32("3"),
    
    _42("4"),
    
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
    
    _18("18"),
    
    _19("19"),
    
    _20("20"),
    
    _21("21"),
    
    _22("22"),
    
    _23("23"),
    
    _24("24"),
    
    _26("26"),
    
    _27("27"),
    
    _29("29"),
    
    _31("31"),
    
    _32("32"),
    
    _33("33"),
    
    _34("34"),
    
    _35("35"),
    
    _39("39"),
    
    _40("40"),
    
    _44("44"),
    
    _45("45"),
    
    _49("49"),
    
    _50("50"),
    
    _51("51"),
    
    _53("53"),
    
    _54("54"),
    
    _55("55"),
    
    _56("56"),
    
    _58("58"),
    
    _59("59"),
    
    _60("60"),
    
    _61("61"),
    
    _66("66"),
    
    _69("69"),
    
    _70("70"),
    
    _74("74"),
    
    _75("75"),
    
    _76("76"),
    
    _78("78"),
    
    _85("85"),
    
    _87("87"),
    
    _89("89"),
    
    _90("90"),
    
    _91("91"),
    
    _94("94"),
    
    _95("95"),
    
    _96("96"),
    
    _97("97"),
    
    _100("100"),
    
    _101("101"),
    
    _102("102"),
    
    _103("103"),
    
    _104("104"),
    
    _105("105"),
    
    _106("106"),
    
    _107("107"),
    
    _108("108"),
    
    _109("109"),
    
    _110("110"),
    
    _111("111"),
    
    _112("112"),
    
    _114("114"),
    
    _115("115"),
    
    _116("116"),
    
    _117("117"),
    
    _118("118"),
    
    _119("119"),
    
    _121("121"),
    
    _122("122"),
    
    _125("125"),
    
    _128("128"),
    
    _129("129"),
    
    _130("130"),
    
    _131("131"),
    
    _132("132"),
    
    _133("133"),
    
    _134("134"),
    
    _135("135"),
    
    _136("136"),
    
    _137("137"),
    
    _138("138"),
    
    _139("139"),
    
    _140("140"),
    
    _142("142"),
    
    _143("143"),
    
    _144("144"),
    
    _146("146"),
    
    _147("147"),
    
    _148("148"),
    
    _149("149"),
    
    _150("150"),
    
    _151("151"),
    
    _152("152"),
    
    _153("153"),
    
    _154("154"),
    
    _155("155"),
    
    _157("157"),
    
    _158("158"),
    
    _159("159"),
    
    _160("160"),
    
    _161("161"),
    
    _162("162"),
    
    _163("163"),
    
    _164("164"),
    
    _165("165"),
    
    _166("166"),
    
    _167("167"),
    
    _168("168"),
    
    _169("169"),
    
    _170("170"),
    
    _171("171"),
    
    _172("172"),
    
    _173("173"),
    
    _174("174"),
    
    _175("175"),
    
    _176("176"),
    
    _177("177"),
    
    _178("178"),
    
    _179("179"),
    
    _180("180"),
    
    _181("181"),
    
    _182("182"),
    
    _183("183"),
    
    _184("184"),
    
    _185("185"),
    
    _186("186"),
    
    _187("187"),
    
    _188("188"),
    
    _189("189"),
    
    _190("190"),
    
    _191("191"),
    
    _192("192"),
    
    _193("193"),
    
    _194("194"),
    
    _195("195"),
    
    _197("197"),
    
    _198("198"),
    
    _199("199"),
    
    _200("200"),
    
    _201("201"),
    
    _202("202"),
    
    _203("203"),
    
    _204("204"),
    
    _205("205"),
    
    _206("206"),
    
    _207("207"),
    
    _208("208"),
    
    _209("209"),
    
    _210("210"),
    
    _211("211"),
    
    _212("212"),
    
    _213("213"),
    
    _214("214"),
    
    _215("215"),
    
    _216("216"),
    
    _217("217"),
    
    _218("218"),
    
    _219("219"),
    
    _220("220"),
    
    _221("221"),
    
    _222("222"),
    
    _223("223"),
    
    _224("224"),
    
    _225("225"),
    
    _226("226"),
    
    _227("227"),
    
    _228("228"),
    
    _229("229"),
    
    _230("230"),
    
    _231("231"),
    
    _232("232"),
    
    _233("233"),
    
    _234("234"),
    
    _235("235"),
    
    _236("236"),
    
    _237("237"),
    
    _238("238"),
    
    _239("239"),
    
    _240("240"),
    
    _241("241"),
    
    _242("242"),
    
    _243("243"),
    
    _244("244"),
    
    _245("245"),
    
    _246("246"),
    
    _247("247"),
    
    _248("248"),
    
    _249("249"),
    
    _250("250"),
    
    _251("251"),
    
    _252("252"),
    
    _253("253"),
    
    _254("254"),
    
    _256("256"),
    
    _257("257"),
    
    _258("258"),
    
    _259("259"),
    
    _260("260"),
    
    _261("261"),
    
    _262("262"),
    
    _263("263"),
    
    _264("264"),
    
    _265("265"),
    
    _266("266"),
    
    _267("267"),
    
    _268("268"),
    
    _269("269"),
    
    _270("270"),
    
    _271("271"),
    
    _272("272"),
    
    _273("273"),
    
    _274("274"),
    
    _275("275"),
    
    _276("276"),
    
    _277("277"),
    
    _287("287"),
    
    _288("288"),
    
    A0("A0"),
    
    A1("A1"),
    
    A5("A5"),
    
    A6("A6"),
    
    A7("A7"),
    
    A8("A8"),
    
    B1("B1"),
    
    B4("B4"),
    
    B5("B5"),
    
    B7("B7"),
    
    B8("B8"),
    
    B9("B9"),
    
    B10("B10"),
    
    B11("B11"),
    
    B12("B12"),
    
    B13("B13"),
    
    B14("B14"),
    
    B15("B15"),
    
    B16("B16"),
    
    B20("B20"),
    
    B22("B22"),
    
    B23("B23"),
    
    P1("P1"),
    
    P2("P2"),
    
    P3("P3"),
    
    P4("P4"),
    
    P5("P5"),
    
    P6("P6"),
    
    P7("P7"),
    
    P8("P8"),
    
    P9("P9"),
    
    P10("P10"),
    
    P11("P11"),
    
    P12("P12"),
    
    P13("P13"),
    
    P14("P14"),
    
    P15("P15"),
    
    P16("P16"),
    
    P17("P17"),
    
    P18("P18"),
    
    P19("P19"),
    
    P20("P20"),
    
    P21("P21"),
    
    P22("P22"),
    
    P23("P23"),
    
    W1("W1"),
    
    W2("W2"),
    
    W3("W3"),
    
    W4("W4"),
    
    Y1("Y1"),
    
    Y2("Y2"),
    
    Y3("Y3");

    private String value;

    AdjustmentReasonEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AdjustmentReasonEnum fromValue(String value) {
      for (AdjustmentReasonEnum b : AdjustmentReasonEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AdjustmentReasonEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AdjustmentReasonEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AdjustmentReasonEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AdjustmentReasonEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AdjustmentReasonEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ADJUSTMENT_REASON = "adjustment_reason";
  @SerializedName(SERIALIZED_NAME_ADJUSTMENT_REASON)
  private AdjustmentReasonEnum adjustmentReason;

  public static final String SERIALIZED_NAME_APPOINTMENT = "appointment";
  @SerializedName(SERIALIZED_NAME_APPOINTMENT)
  private Integer appointment;

  public static final String SERIALIZED_NAME_CHECK_DATE = "check_date";
  @SerializedName(SERIALIZED_NAME_CHECK_DATE)
  private String checkDate;

  /**
   * Status of claim
   */
  @JsonAdapter(ClaimStatusEnum.Adapter.class)
  public enum ClaimStatusEnum {
    EMPTY(""),
    
    _0("0"),
    
    _1("1"),
    
    _2("2"),
    
    _3("3"),
    
    _4("4"),
    
    _5("5"),
    
    _10("10"),
    
    _13("13"),
    
    _15("15"),
    
    _16("16"),
    
    _17("17"),
    
    _19("19"),
    
    _20("20"),
    
    _21("21"),
    
    _22("22"),
    
    _23("23"),
    
    _25("25"),
    
    _27("27");

    private String value;

    ClaimStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ClaimStatusEnum fromValue(String value) {
      for (ClaimStatusEnum b : ClaimStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ClaimStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ClaimStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ClaimStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ClaimStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ClaimStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CLAIM_STATUS = "claim_status";
  @SerializedName(SERIALIZED_NAME_CLAIM_STATUS)
  private ClaimStatusEnum claimStatus;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private Integer doctor;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_INS_NAME = "ins_name";
  @SerializedName(SERIALIZED_NAME_INS_NAME)
  private Integer insName;

  public static final String SERIALIZED_NAME_INS_PAID = "ins_paid";
  @SerializedName(SERIALIZED_NAME_INS_PAID)
  private BigDecimal insPaid;

  public static final String SERIALIZED_NAME_LINE_ITEM = "line_item";
  @SerializedName(SERIALIZED_NAME_LINE_ITEM)
  private Integer lineItem;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private Integer patient;

  public static final String SERIALIZED_NAME_POSTED_DATE = "posted_date";
  @SerializedName(SERIALIZED_NAME_POSTED_DATE)
  private String postedDate;

  public static final String SERIALIZED_NAME_TRACE_NUMBER = "trace_number";
  @SerializedName(SERIALIZED_NAME_TRACE_NUMBER)
  private String traceNumber;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public LineItemTransaction() {
  }

  public LineItemTransaction(
     AdjustmentGroupCodeEnum adjustmentGroupCode, 
     String checkDate, 
     ClaimStatusEnum claimStatus, 
     String createdAt, 
     Integer id, 
     String postedDate, 
     String updatedAt
  ) {
    this();
    this.adjustmentGroupCode = adjustmentGroupCode;
    this.checkDate = checkDate;
    this.claimStatus = claimStatus;
    this.createdAt = createdAt;
    this.id = id;
    this.postedDate = postedDate;
    this.updatedAt = updatedAt;
  }

  public LineItemTransaction adjustment(BigDecimal adjustment) {
    this.adjustment = adjustment;
    return this;
  }

  /**
   * Adjustment from total billed
   * @return adjustment
   */
  @javax.annotation.Nullable
  public BigDecimal getAdjustment() {
    return adjustment;
  }

  public void setAdjustment(BigDecimal adjustment) {
    this.adjustment = adjustment;
  }


  /**
   * Group code for adjustment
   * @return adjustmentGroupCode
   */
  @javax.annotation.Nullable
  public AdjustmentGroupCodeEnum getAdjustmentGroupCode() {
    return adjustmentGroupCode;
  }



  public LineItemTransaction adjustmentReason(AdjustmentReasonEnum adjustmentReason) {
    this.adjustmentReason = adjustmentReason;
    return this;
  }

  /**
   * Reason for adjustment
   * @return adjustmentReason
   */
  @javax.annotation.Nullable
  public AdjustmentReasonEnum getAdjustmentReason() {
    return adjustmentReason;
  }

  public void setAdjustmentReason(AdjustmentReasonEnum adjustmentReason) {
    this.adjustmentReason = adjustmentReason;
  }


  public LineItemTransaction appointment(Integer appointment) {
    this.appointment = appointment;
    return this;
  }

  /**
   * Appointment ID
   * @return appointment
   */
  @javax.annotation.Nullable
  public Integer getAppointment() {
    return appointment;
  }

  public void setAppointment(Integer appointment) {
    this.appointment = appointment;
  }


  /**
   * Date of check
   * @return checkDate
   */
  @javax.annotation.Nullable
  public String getCheckDate() {
    return checkDate;
  }



  /**
   * Status of claim
   * @return claimStatus
   */
  @javax.annotation.Nullable
  public ClaimStatusEnum getClaimStatus() {
    return claimStatus;
  }



  /**
   * 
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }



  public LineItemTransaction doctor(Integer doctor) {
    this.doctor = doctor;
    return this;
  }

  /**
   * Doctor ID
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



  public LineItemTransaction insName(Integer insName) {
    this.insName = insName;
    return this;
  }

  /**
   * Can be one of the following, &#x60;1&#x60;(Primary Insurance), &#x60;2&#x60;(Secondary Insurance)
   * @return insName
   */
  @javax.annotation.Nullable
  public Integer getInsName() {
    return insName;
  }

  public void setInsName(Integer insName) {
    this.insName = insName;
  }


  public LineItemTransaction insPaid(BigDecimal insPaid) {
    this.insPaid = insPaid;
    return this;
  }

  /**
   * 
   * @return insPaid
   */
  @javax.annotation.Nullable
  public BigDecimal getInsPaid() {
    return insPaid;
  }

  public void setInsPaid(BigDecimal insPaid) {
    this.insPaid = insPaid;
  }


  public LineItemTransaction lineItem(Integer lineItem) {
    this.lineItem = lineItem;
    return this;
  }

  /**
   * ID of &#x60;/api/line_item&#x60; object
   * @return lineItem
   */
  @javax.annotation.Nullable
  public Integer getLineItem() {
    return lineItem;
  }

  public void setLineItem(Integer lineItem) {
    this.lineItem = lineItem;
  }


  public LineItemTransaction patient(Integer patient) {
    this.patient = patient;
    return this;
  }

  /**
   * 
   * @return patient
   */
  @javax.annotation.Nullable
  public Integer getPatient() {
    return patient;
  }

  public void setPatient(Integer patient) {
    this.patient = patient;
  }


  /**
   * Date when transaction is created
   * @return postedDate
   */
  @javax.annotation.Nullable
  public String getPostedDate() {
    return postedDate;
  }



  public LineItemTransaction traceNumber(String traceNumber) {
    this.traceNumber = traceNumber;
    return this;
  }

  /**
   * Check number
   * @return traceNumber
   */
  @javax.annotation.Nullable
  public String getTraceNumber() {
    return traceNumber;
  }

  public void setTraceNumber(String traceNumber) {
    this.traceNumber = traceNumber;
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
    LineItemTransaction lineItemTransaction = (LineItemTransaction) o;
    return Objects.equals(this.adjustment, lineItemTransaction.adjustment) &&
        Objects.equals(this.adjustmentGroupCode, lineItemTransaction.adjustmentGroupCode) &&
        Objects.equals(this.adjustmentReason, lineItemTransaction.adjustmentReason) &&
        Objects.equals(this.appointment, lineItemTransaction.appointment) &&
        Objects.equals(this.checkDate, lineItemTransaction.checkDate) &&
        Objects.equals(this.claimStatus, lineItemTransaction.claimStatus) &&
        Objects.equals(this.createdAt, lineItemTransaction.createdAt) &&
        Objects.equals(this.doctor, lineItemTransaction.doctor) &&
        Objects.equals(this.id, lineItemTransaction.id) &&
        Objects.equals(this.insName, lineItemTransaction.insName) &&
        Objects.equals(this.insPaid, lineItemTransaction.insPaid) &&
        Objects.equals(this.lineItem, lineItemTransaction.lineItem) &&
        Objects.equals(this.patient, lineItemTransaction.patient) &&
        Objects.equals(this.postedDate, lineItemTransaction.postedDate) &&
        Objects.equals(this.traceNumber, lineItemTransaction.traceNumber) &&
        Objects.equals(this.updatedAt, lineItemTransaction.updatedAt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(adjustment, adjustmentGroupCode, adjustmentReason, appointment, checkDate, claimStatus, createdAt, doctor, id, insName, insPaid, lineItem, patient, postedDate, traceNumber, updatedAt);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LineItemTransaction {\n");
    sb.append("    adjustment: ").append(toIndentedString(adjustment)).append("\n");
    sb.append("    adjustmentGroupCode: ").append(toIndentedString(adjustmentGroupCode)).append("\n");
    sb.append("    adjustmentReason: ").append(toIndentedString(adjustmentReason)).append("\n");
    sb.append("    appointment: ").append(toIndentedString(appointment)).append("\n");
    sb.append("    checkDate: ").append(toIndentedString(checkDate)).append("\n");
    sb.append("    claimStatus: ").append(toIndentedString(claimStatus)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    insName: ").append(toIndentedString(insName)).append("\n");
    sb.append("    insPaid: ").append(toIndentedString(insPaid)).append("\n");
    sb.append("    lineItem: ").append(toIndentedString(lineItem)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    postedDate: ").append(toIndentedString(postedDate)).append("\n");
    sb.append("    traceNumber: ").append(toIndentedString(traceNumber)).append("\n");
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
    openapiFields.add("adjustment");
    openapiFields.add("adjustment_group_code");
    openapiFields.add("adjustment_reason");
    openapiFields.add("appointment");
    openapiFields.add("check_date");
    openapiFields.add("claim_status");
    openapiFields.add("created_at");
    openapiFields.add("doctor");
    openapiFields.add("id");
    openapiFields.add("ins_name");
    openapiFields.add("ins_paid");
    openapiFields.add("line_item");
    openapiFields.add("patient");
    openapiFields.add("posted_date");
    openapiFields.add("trace_number");
    openapiFields.add("updated_at");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LineItemTransaction
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LineItemTransaction.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LineItemTransaction is not found in the empty JSON string", LineItemTransaction.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LineItemTransaction.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LineItemTransaction` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("adjustment_group_code") != null && !jsonObj.get("adjustment_group_code").isJsonNull()) && !jsonObj.get("adjustment_group_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `adjustment_group_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("adjustment_group_code").toString()));
      }
      // validate the optional field `adjustment_group_code`
      if (jsonObj.get("adjustment_group_code") != null && !jsonObj.get("adjustment_group_code").isJsonNull()) {
        AdjustmentGroupCodeEnum.validateJsonElement(jsonObj.get("adjustment_group_code"));
      }
      if ((jsonObj.get("adjustment_reason") != null && !jsonObj.get("adjustment_reason").isJsonNull()) && !jsonObj.get("adjustment_reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `adjustment_reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("adjustment_reason").toString()));
      }
      // validate the optional field `adjustment_reason`
      if (jsonObj.get("adjustment_reason") != null && !jsonObj.get("adjustment_reason").isJsonNull()) {
        AdjustmentReasonEnum.validateJsonElement(jsonObj.get("adjustment_reason"));
      }
      if ((jsonObj.get("check_date") != null && !jsonObj.get("check_date").isJsonNull()) && !jsonObj.get("check_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `check_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("check_date").toString()));
      }
      if ((jsonObj.get("claim_status") != null && !jsonObj.get("claim_status").isJsonNull()) && !jsonObj.get("claim_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `claim_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("claim_status").toString()));
      }
      // validate the optional field `claim_status`
      if (jsonObj.get("claim_status") != null && !jsonObj.get("claim_status").isJsonNull()) {
        ClaimStatusEnum.validateJsonElement(jsonObj.get("claim_status"));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("posted_date") != null && !jsonObj.get("posted_date").isJsonNull()) && !jsonObj.get("posted_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `posted_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("posted_date").toString()));
      }
      if ((jsonObj.get("trace_number") != null && !jsonObj.get("trace_number").isJsonNull()) && !jsonObj.get("trace_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `trace_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("trace_number").toString()));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LineItemTransaction.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LineItemTransaction' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LineItemTransaction> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LineItemTransaction.class));

       return (TypeAdapter<T>) new TypeAdapter<LineItemTransaction>() {
           @Override
           public void write(JsonWriter out, LineItemTransaction value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LineItemTransaction read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LineItemTransaction given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LineItemTransaction
   * @throws IOException if the JSON string is invalid with respect to LineItemTransaction
   */
  public static LineItemTransaction fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LineItemTransaction.class);
  }

  /**
   * Convert an instance of LineItemTransaction to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

