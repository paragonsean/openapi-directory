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
 * LabResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LabResult {
  /**
   *  Value | Notes ----- | ----- &#x60;&#39;L&#39;&#x60; | &#x60;&#39;low&#39;&#x60; &#x60;&#39;LL&#39;&#x60; | &#x60;&#39;alert low&#39;&#x60; &#x60;&#39;H&#39;&#x60; | &#x60;&#39;high&#39;&#x60; &#x60;&#39;HH&#39;&#x60; | &#x60;&#39;alert high&#39;&#x60; &#x60;&#39;&lt;&#39;&#x60; | &#x60;&#39;panic low&#39;&#x60; &#x60;&#39;&gt;&#39;&#x60; | &#x60;&#39;panic high&#39;&#x60; &#x60;&#39;A&#39;&#x60; | &#x60;&#39;abnormal&#39;&#x60; &#x60;&#39;AA&#39;&#x60; | &#x60;&#39;very abnormal&#39;&#x60; &#x60;&#39;S&#39;&#x60; | &#x60;&#39;susceptible&#39;&#x60; &#x60;&#39;R&#39;&#x60; | &#x60;&#39;resistant&#39;&#x60; &#x60;&#39;I&#39;&#x60; | &#x60;&#39;intermediate&#39;&#x60; &#x60;&#39;NEG&#39;&#x60; | &#x60;&#39;negative&#39;&#x60; &#x60;&#39;POS&#39;&#x60; | &#x60;&#39;positive&#39;&#x60; &#x60;&#39;N&#39;&#x60; | &#x60;&#39;normal&#39;&#x60; &#x60;&#39;&#39;&#x60; | &#x60;&#39;no comment&#39;&#x60; 
   */
  @JsonAdapter(AbnormalStatusEnum.Adapter.class)
  public enum AbnormalStatusEnum {
    L("L"),
    
    LL("LL"),
    
    H("H"),
    
    HH("HH"),
    
    LESS_THAN("<"),
    
    GREATER_THAN(">"),
    
    A("A"),
    
    AA("AA"),
    
    S("S"),
    
    R("R"),
    
    I("I"),
    
    NEG("NEG"),
    
    POS("POS"),
    
    N("N"),
    
    EMPTY("");

    private String value;

    AbnormalStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AbnormalStatusEnum fromValue(String value) {
      for (AbnormalStatusEnum b : AbnormalStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AbnormalStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AbnormalStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AbnormalStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AbnormalStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AbnormalStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ABNORMAL_STATUS = "abnormal_status";
  @SerializedName(SERIALIZED_NAME_ABNORMAL_STATUS)
  private AbnormalStatusEnum abnormalStatus;

  public static final String SERIALIZED_NAME_COMMENTS = "comments";
  @SerializedName(SERIALIZED_NAME_COMMENTS)
  private String comments;

  public static final String SERIALIZED_NAME_DOCUMENT = "document";
  @SerializedName(SERIALIZED_NAME_DOCUMENT)
  private Integer document;

  public static final String SERIALIZED_NAME_GROUP_CODE = "group_code";
  @SerializedName(SERIALIZED_NAME_GROUP_CODE)
  private String groupCode;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IS_ABNORMAL = "is_abnormal";
  @SerializedName(SERIALIZED_NAME_IS_ABNORMAL)
  private String isAbnormal;

  public static final String SERIALIZED_NAME_LAB_ORDER = "lab_order";
  @SerializedName(SERIALIZED_NAME_LAB_ORDER)
  private String labOrder;

  public static final String SERIALIZED_NAME_LAB_TEST = "lab_test";
  @SerializedName(SERIALIZED_NAME_LAB_TEST)
  private Integer labTest;

  public static final String SERIALIZED_NAME_NORMAL_RANGE = "normal_range";
  @SerializedName(SERIALIZED_NAME_NORMAL_RANGE)
  private String normalRange;

  public static final String SERIALIZED_NAME_OBSERVATION_CODE = "observation_code";
  @SerializedName(SERIALIZED_NAME_OBSERVATION_CODE)
  private String observationCode;

  public static final String SERIALIZED_NAME_OBSERVATION_DESCRIPTION = "observation_description";
  @SerializedName(SERIALIZED_NAME_OBSERVATION_DESCRIPTION)
  private String observationDescription;

  public static final String SERIALIZED_NAME_SPECIMEN_RECEIVED = "specimen_received";
  @SerializedName(SERIALIZED_NAME_SPECIMEN_RECEIVED)
  private String specimenReceived;

  /**
   *  Value | Notes ----- | ----- &#x60;&#39;P&#39;&#x60; | &#x60;&#39;preliminary&#39;&#x60; &#x60;&#39;I&#39;&#x60; | &#x60;&#39;pending&#39;&#x60; &#x60;&#39;C&#39;&#x60; | &#x60;&#39;correction&#39;&#x60; &#x60;&#39;F&#39;&#x60; | &#x60;&#39;final&#39;&#x60; &#x60;&#39;X&#39;&#x60; | &#x60;&#39;canceled&#39;&#x60; 
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    P("P"),
    
    I("I"),
    
    C("C"),
    
    F("F"),
    
    X("X");

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

  public static final String SERIALIZED_NAME_TEST_PERFORMED = "test_performed";
  @SerializedName(SERIALIZED_NAME_TEST_PERFORMED)
  private String testPerformed;

  public static final String SERIALIZED_NAME_UNIT = "unit";
  @SerializedName(SERIALIZED_NAME_UNIT)
  private String unit;

  public static final String SERIALIZED_NAME_VALUE = "value";
  @SerializedName(SERIALIZED_NAME_VALUE)
  private String value;

  public static final String SERIALIZED_NAME_VALUE_IS_NUMERIC = "value_is_numeric";
  @SerializedName(SERIALIZED_NAME_VALUE_IS_NUMERIC)
  private Boolean valueIsNumeric;

  public LabResult() {
  }

  public LabResult(
     Integer id, 
     String labOrder
  ) {
    this();
    this.id = id;
    this.labOrder = labOrder;
  }

  public LabResult abnormalStatus(AbnormalStatusEnum abnormalStatus) {
    this.abnormalStatus = abnormalStatus;
    return this;
  }

  /**
   *  Value | Notes ----- | ----- &#x60;&#39;L&#39;&#x60; | &#x60;&#39;low&#39;&#x60; &#x60;&#39;LL&#39;&#x60; | &#x60;&#39;alert low&#39;&#x60; &#x60;&#39;H&#39;&#x60; | &#x60;&#39;high&#39;&#x60; &#x60;&#39;HH&#39;&#x60; | &#x60;&#39;alert high&#39;&#x60; &#x60;&#39;&lt;&#39;&#x60; | &#x60;&#39;panic low&#39;&#x60; &#x60;&#39;&gt;&#39;&#x60; | &#x60;&#39;panic high&#39;&#x60; &#x60;&#39;A&#39;&#x60; | &#x60;&#39;abnormal&#39;&#x60; &#x60;&#39;AA&#39;&#x60; | &#x60;&#39;very abnormal&#39;&#x60; &#x60;&#39;S&#39;&#x60; | &#x60;&#39;susceptible&#39;&#x60; &#x60;&#39;R&#39;&#x60; | &#x60;&#39;resistant&#39;&#x60; &#x60;&#39;I&#39;&#x60; | &#x60;&#39;intermediate&#39;&#x60; &#x60;&#39;NEG&#39;&#x60; | &#x60;&#39;negative&#39;&#x60; &#x60;&#39;POS&#39;&#x60; | &#x60;&#39;positive&#39;&#x60; &#x60;&#39;N&#39;&#x60; | &#x60;&#39;normal&#39;&#x60; &#x60;&#39;&#39;&#x60; | &#x60;&#39;no comment&#39;&#x60; 
   * @return abnormalStatus
   */
  @javax.annotation.Nullable
  public AbnormalStatusEnum getAbnormalStatus() {
    return abnormalStatus;
  }

  public void setAbnormalStatus(AbnormalStatusEnum abnormalStatus) {
    this.abnormalStatus = abnormalStatus;
  }


  public LabResult comments(String comments) {
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


  public LabResult document(Integer document) {
    this.document = document;
    return this;
  }

  /**
   * ID of &#x60;/lab_documents&#x60; object for the result
   * @return document
   */
  @javax.annotation.Nonnull
  public Integer getDocument() {
    return document;
  }

  public void setDocument(Integer document) {
    this.document = document;
  }


  public LabResult groupCode(String groupCode) {
    this.groupCode = groupCode;
    return this;
  }

  /**
   * This is the code used for grouping result data.
   * @return groupCode
   */
  @javax.annotation.Nullable
  public String getGroupCode() {
    return groupCode;
  }

  public void setGroupCode(String groupCode) {
    this.groupCode = groupCode;
  }


  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public LabResult isAbnormal(String isAbnormal) {
    this.isAbnormal = isAbnormal;
    return this;
  }

  /**
   * If true, the result will be flagged for the doctor&#39;s attention
   * @return isAbnormal
   */
  @javax.annotation.Nullable
  public String getIsAbnormal() {
    return isAbnormal;
  }

  public void setIsAbnormal(String isAbnormal) {
    this.isAbnormal = isAbnormal;
  }


  /**
   * ID of &#x60;/lab_orders&#x60; object the result belongs to
   * @return labOrder
   */
  @javax.annotation.Nullable
  public String getLabOrder() {
    return labOrder;
  }



  public LabResult labTest(Integer labTest) {
    this.labTest = labTest;
    return this;
  }

  /**
   * ID of &#x60;/lab_tests&#x60; object for the result
   * @return labTest
   */
  @javax.annotation.Nonnull
  public Integer getLabTest() {
    return labTest;
  }

  public void setLabTest(Integer labTest) {
    this.labTest = labTest;
  }


  public LabResult normalRange(String normalRange) {
    this.normalRange = normalRange;
    return this;
  }

  /**
   * When &#x60;&#x60;value_is_numeric&#x60;&#x60; is True, this parameter must be a string of the form &#x60;&#x60;\&quot;&lt;lower&gt; &lt;upper&gt;\&quot;, where both lower and upper are numerical&#x60;&#x60;
   * @return normalRange
   */
  @javax.annotation.Nullable
  public String getNormalRange() {
    return normalRange;
  }

  public void setNormalRange(String normalRange) {
    this.normalRange = normalRange;
  }


  public LabResult observationCode(String observationCode) {
    this.observationCode = observationCode;
    return this;
  }

  /**
   * 
   * @return observationCode
   */
  @javax.annotation.Nullable
  public String getObservationCode() {
    return observationCode;
  }

  public void setObservationCode(String observationCode) {
    this.observationCode = observationCode;
  }


  public LabResult observationDescription(String observationDescription) {
    this.observationDescription = observationDescription;
    return this;
  }

  /**
   * For example, &#x60;&#x60;\&quot;Blood Urea Nitrogen (BUN)\&quot;&#x60;&#x60;
   * @return observationDescription
   */
  @javax.annotation.Nullable
  public String getObservationDescription() {
    return observationDescription;
  }

  public void setObservationDescription(String observationDescription) {
    this.observationDescription = observationDescription;
  }


  public LabResult specimenReceived(String specimenReceived) {
    this.specimenReceived = specimenReceived;
    return this;
  }

  /**
   * 
   * @return specimenReceived
   */
  @javax.annotation.Nullable
  public String getSpecimenReceived() {
    return specimenReceived;
  }

  public void setSpecimenReceived(String specimenReceived) {
    this.specimenReceived = specimenReceived;
  }


  public LabResult status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   *  Value | Notes ----- | ----- &#x60;&#39;P&#39;&#x60; | &#x60;&#39;preliminary&#39;&#x60; &#x60;&#39;I&#39;&#x60; | &#x60;&#39;pending&#39;&#x60; &#x60;&#39;C&#39;&#x60; | &#x60;&#39;correction&#39;&#x60; &#x60;&#39;F&#39;&#x60; | &#x60;&#39;final&#39;&#x60; &#x60;&#39;X&#39;&#x60; | &#x60;&#39;canceled&#39;&#x60; 
   * @return status
   */
  @javax.annotation.Nonnull
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public LabResult testPerformed(String testPerformed) {
    this.testPerformed = testPerformed;
    return this;
  }

  /**
   * 
   * @return testPerformed
   */
  @javax.annotation.Nonnull
  public String getTestPerformed() {
    return testPerformed;
  }

  public void setTestPerformed(String testPerformed) {
    this.testPerformed = testPerformed;
  }


  public LabResult unit(String unit) {
    this.unit = unit;
    return this;
  }

  /**
   * Unit used for the value
   * @return unit
   */
  @javax.annotation.Nullable
  public String getUnit() {
    return unit;
  }

  public void setUnit(String unit) {
    this.unit = unit;
  }


  public LabResult value(String value) {
    this.value = value;
    return this;
  }

  /**
   * 
   * @return value
   */
  @javax.annotation.Nonnull
  public String getValue() {
    return value;
  }

  public void setValue(String value) {
    this.value = value;
  }


  public LabResult valueIsNumeric(Boolean valueIsNumeric) {
    this.valueIsNumeric = valueIsNumeric;
    return this;
  }

  /**
   * Default to &#x60;False&#x60;
   * @return valueIsNumeric
   */
  @javax.annotation.Nullable
  public Boolean getValueIsNumeric() {
    return valueIsNumeric;
  }

  public void setValueIsNumeric(Boolean valueIsNumeric) {
    this.valueIsNumeric = valueIsNumeric;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LabResult labResult = (LabResult) o;
    return Objects.equals(this.abnormalStatus, labResult.abnormalStatus) &&
        Objects.equals(this.comments, labResult.comments) &&
        Objects.equals(this.document, labResult.document) &&
        Objects.equals(this.groupCode, labResult.groupCode) &&
        Objects.equals(this.id, labResult.id) &&
        Objects.equals(this.isAbnormal, labResult.isAbnormal) &&
        Objects.equals(this.labOrder, labResult.labOrder) &&
        Objects.equals(this.labTest, labResult.labTest) &&
        Objects.equals(this.normalRange, labResult.normalRange) &&
        Objects.equals(this.observationCode, labResult.observationCode) &&
        Objects.equals(this.observationDescription, labResult.observationDescription) &&
        Objects.equals(this.specimenReceived, labResult.specimenReceived) &&
        Objects.equals(this.status, labResult.status) &&
        Objects.equals(this.testPerformed, labResult.testPerformed) &&
        Objects.equals(this.unit, labResult.unit) &&
        Objects.equals(this.value, labResult.value) &&
        Objects.equals(this.valueIsNumeric, labResult.valueIsNumeric);
  }

  @Override
  public int hashCode() {
    return Objects.hash(abnormalStatus, comments, document, groupCode, id, isAbnormal, labOrder, labTest, normalRange, observationCode, observationDescription, specimenReceived, status, testPerformed, unit, value, valueIsNumeric);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LabResult {\n");
    sb.append("    abnormalStatus: ").append(toIndentedString(abnormalStatus)).append("\n");
    sb.append("    comments: ").append(toIndentedString(comments)).append("\n");
    sb.append("    document: ").append(toIndentedString(document)).append("\n");
    sb.append("    groupCode: ").append(toIndentedString(groupCode)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isAbnormal: ").append(toIndentedString(isAbnormal)).append("\n");
    sb.append("    labOrder: ").append(toIndentedString(labOrder)).append("\n");
    sb.append("    labTest: ").append(toIndentedString(labTest)).append("\n");
    sb.append("    normalRange: ").append(toIndentedString(normalRange)).append("\n");
    sb.append("    observationCode: ").append(toIndentedString(observationCode)).append("\n");
    sb.append("    observationDescription: ").append(toIndentedString(observationDescription)).append("\n");
    sb.append("    specimenReceived: ").append(toIndentedString(specimenReceived)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    testPerformed: ").append(toIndentedString(testPerformed)).append("\n");
    sb.append("    unit: ").append(toIndentedString(unit)).append("\n");
    sb.append("    value: ").append(toIndentedString(value)).append("\n");
    sb.append("    valueIsNumeric: ").append(toIndentedString(valueIsNumeric)).append("\n");
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
    openapiFields.add("abnormal_status");
    openapiFields.add("comments");
    openapiFields.add("document");
    openapiFields.add("group_code");
    openapiFields.add("id");
    openapiFields.add("is_abnormal");
    openapiFields.add("lab_order");
    openapiFields.add("lab_test");
    openapiFields.add("normal_range");
    openapiFields.add("observation_code");
    openapiFields.add("observation_description");
    openapiFields.add("specimen_received");
    openapiFields.add("status");
    openapiFields.add("test_performed");
    openapiFields.add("unit");
    openapiFields.add("value");
    openapiFields.add("value_is_numeric");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("document");
    openapiRequiredFields.add("lab_test");
    openapiRequiredFields.add("status");
    openapiRequiredFields.add("test_performed");
    openapiRequiredFields.add("value");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LabResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LabResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LabResult is not found in the empty JSON string", LabResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LabResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LabResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : LabResult.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("abnormal_status") != null && !jsonObj.get("abnormal_status").isJsonNull()) && !jsonObj.get("abnormal_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `abnormal_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("abnormal_status").toString()));
      }
      // validate the optional field `abnormal_status`
      if (jsonObj.get("abnormal_status") != null && !jsonObj.get("abnormal_status").isJsonNull()) {
        AbnormalStatusEnum.validateJsonElement(jsonObj.get("abnormal_status"));
      }
      if ((jsonObj.get("comments") != null && !jsonObj.get("comments").isJsonNull()) && !jsonObj.get("comments").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comments` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comments").toString()));
      }
      if ((jsonObj.get("group_code") != null && !jsonObj.get("group_code").isJsonNull()) && !jsonObj.get("group_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group_code").toString()));
      }
      if ((jsonObj.get("is_abnormal") != null && !jsonObj.get("is_abnormal").isJsonNull()) && !jsonObj.get("is_abnormal").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_abnormal` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_abnormal").toString()));
      }
      if ((jsonObj.get("lab_order") != null && !jsonObj.get("lab_order").isJsonNull()) && !jsonObj.get("lab_order").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lab_order` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lab_order").toString()));
      }
      if ((jsonObj.get("normal_range") != null && !jsonObj.get("normal_range").isJsonNull()) && !jsonObj.get("normal_range").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `normal_range` to be a primitive type in the JSON string but got `%s`", jsonObj.get("normal_range").toString()));
      }
      if ((jsonObj.get("observation_code") != null && !jsonObj.get("observation_code").isJsonNull()) && !jsonObj.get("observation_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `observation_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("observation_code").toString()));
      }
      if ((jsonObj.get("observation_description") != null && !jsonObj.get("observation_description").isJsonNull()) && !jsonObj.get("observation_description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `observation_description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("observation_description").toString()));
      }
      if ((jsonObj.get("specimen_received") != null && !jsonObj.get("specimen_received").isJsonNull()) && !jsonObj.get("specimen_received").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `specimen_received` to be a primitive type in the JSON string but got `%s`", jsonObj.get("specimen_received").toString()));
      }
      if (!jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the required field `status`
      StatusEnum.validateJsonElement(jsonObj.get("status"));
      if (!jsonObj.get("test_performed").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `test_performed` to be a primitive type in the JSON string but got `%s`", jsonObj.get("test_performed").toString()));
      }
      if ((jsonObj.get("unit") != null && !jsonObj.get("unit").isJsonNull()) && !jsonObj.get("unit").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `unit` to be a primitive type in the JSON string but got `%s`", jsonObj.get("unit").toString()));
      }
      if (!jsonObj.get("value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("value").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LabResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LabResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LabResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LabResult.class));

       return (TypeAdapter<T>) new TypeAdapter<LabResult>() {
           @Override
           public void write(JsonWriter out, LabResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LabResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LabResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LabResult
   * @throws IOException if the JSON string is invalid with respect to LabResult
   */
  public static LabResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LabResult.class);
  }

  /**
   * Convert an instance of LabResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

