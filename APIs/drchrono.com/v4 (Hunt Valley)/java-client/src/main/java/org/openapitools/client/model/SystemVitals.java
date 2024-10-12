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
 * Clinical vitals associated with the appointment
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SystemVitals {
  public static final String SERIALIZED_NAME_BLOOD_PRESSURE1 = "blood_pressure_1";
  @SerializedName(SERIALIZED_NAME_BLOOD_PRESSURE1)
  private Integer bloodPressure1;

  public static final String SERIALIZED_NAME_BLOOD_PRESSURE2 = "blood_pressure_2";
  @SerializedName(SERIALIZED_NAME_BLOOD_PRESSURE2)
  private Integer bloodPressure2;

  public static final String SERIALIZED_NAME_BMI = "bmi";
  @SerializedName(SERIALIZED_NAME_BMI)
  private String bmi;

  public static final String SERIALIZED_NAME_HEAD_CIRCUMFERENCE = "head_circumference";
  @SerializedName(SERIALIZED_NAME_HEAD_CIRCUMFERENCE)
  private BigDecimal headCircumference;

  public static final String SERIALIZED_NAME_HEAD_CIRCUMFERENCE_UNITS = "head_circumference_units";
  @SerializedName(SERIALIZED_NAME_HEAD_CIRCUMFERENCE_UNITS)
  private String headCircumferenceUnits;

  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private BigDecimal height;

  public static final String SERIALIZED_NAME_HEIGHT_UNITS = "height_units";
  @SerializedName(SERIALIZED_NAME_HEIGHT_UNITS)
  private String heightUnits;

  public static final String SERIALIZED_NAME_OXYGEN_SATURATION = "oxygen_saturation";
  @SerializedName(SERIALIZED_NAME_OXYGEN_SATURATION)
  private BigDecimal oxygenSaturation;

  public static final String SERIALIZED_NAME_PAIN = "pain";
  @SerializedName(SERIALIZED_NAME_PAIN)
  private String pain;

  public static final String SERIALIZED_NAME_PULSE = "pulse";
  @SerializedName(SERIALIZED_NAME_PULSE)
  private Integer pulse;

  public static final String SERIALIZED_NAME_RESPIRATORY_RATE = "respiratory_rate";
  @SerializedName(SERIALIZED_NAME_RESPIRATORY_RATE)
  private Integer respiratoryRate;

  /**
   * 
   */
  @JsonAdapter(SmokingStatusEnum.Adapter.class)
  public enum SmokingStatusEnum {
    BLANK("blank"),
    
    _449868002("449868002"),
    
    _428041000124106("428041000124106"),
    
    _8517006("8517006"),
    
    _266919005("266919005"),
    
    _77176002("77176002"),
    
    _266927001("266927001"),
    
    _428071000124103("428071000124103"),
    
    _428061000124105("428061000124105");

    private String value;

    SmokingStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SmokingStatusEnum fromValue(String value) {
      for (SmokingStatusEnum b : SmokingStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SmokingStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SmokingStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SmokingStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SmokingStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SmokingStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SMOKING_STATUS = "smoking_status";
  @SerializedName(SERIALIZED_NAME_SMOKING_STATUS)
  private SmokingStatusEnum smokingStatus;

  public static final String SERIALIZED_NAME_TEMPERATURE = "temperature";
  @SerializedName(SERIALIZED_NAME_TEMPERATURE)
  private BigDecimal temperature;

  public static final String SERIALIZED_NAME_TEMPERATURE_UNITS = "temperature_units";
  @SerializedName(SERIALIZED_NAME_TEMPERATURE_UNITS)
  private String temperatureUnits;

  public static final String SERIALIZED_NAME_WEIGHT = "weight";
  @SerializedName(SERIALIZED_NAME_WEIGHT)
  private BigDecimal weight;

  public static final String SERIALIZED_NAME_WEIGHT_UNITS = "weight_units";
  @SerializedName(SERIALIZED_NAME_WEIGHT_UNITS)
  private String weightUnits;

  public SystemVitals() {
  }

  public SystemVitals(
     String bmi
  ) {
    this();
    this.bmi = bmi;
  }

  public SystemVitals bloodPressure1(Integer bloodPressure1) {
    this.bloodPressure1 = bloodPressure1;
    return this;
  }

  /**
   * 
   * @return bloodPressure1
   */
  @javax.annotation.Nullable
  public Integer getBloodPressure1() {
    return bloodPressure1;
  }

  public void setBloodPressure1(Integer bloodPressure1) {
    this.bloodPressure1 = bloodPressure1;
  }


  public SystemVitals bloodPressure2(Integer bloodPressure2) {
    this.bloodPressure2 = bloodPressure2;
    return this;
  }

  /**
   * 
   * @return bloodPressure2
   */
  @javax.annotation.Nullable
  public Integer getBloodPressure2() {
    return bloodPressure2;
  }

  public void setBloodPressure2(Integer bloodPressure2) {
    this.bloodPressure2 = bloodPressure2;
  }


  /**
   * 
   * @return bmi
   */
  @javax.annotation.Nullable
  public String getBmi() {
    return bmi;
  }



  public SystemVitals headCircumference(BigDecimal headCircumference) {
    this.headCircumference = headCircumference;
    return this;
  }

  /**
   * 
   * @return headCircumference
   */
  @javax.annotation.Nullable
  public BigDecimal getHeadCircumference() {
    return headCircumference;
  }

  public void setHeadCircumference(BigDecimal headCircumference) {
    this.headCircumference = headCircumference;
  }


  public SystemVitals headCircumferenceUnits(String headCircumferenceUnits) {
    this.headCircumferenceUnits = headCircumferenceUnits;
    return this;
  }

  /**
   * 
   * @return headCircumferenceUnits
   */
  @javax.annotation.Nullable
  public String getHeadCircumferenceUnits() {
    return headCircumferenceUnits;
  }

  public void setHeadCircumferenceUnits(String headCircumferenceUnits) {
    this.headCircumferenceUnits = headCircumferenceUnits;
  }


  public SystemVitals height(BigDecimal height) {
    this.height = height;
    return this;
  }

  /**
   * 
   * @return height
   */
  @javax.annotation.Nullable
  public BigDecimal getHeight() {
    return height;
  }

  public void setHeight(BigDecimal height) {
    this.height = height;
  }


  public SystemVitals heightUnits(String heightUnits) {
    this.heightUnits = heightUnits;
    return this;
  }

  /**
   * 
   * @return heightUnits
   */
  @javax.annotation.Nullable
  public String getHeightUnits() {
    return heightUnits;
  }

  public void setHeightUnits(String heightUnits) {
    this.heightUnits = heightUnits;
  }


  public SystemVitals oxygenSaturation(BigDecimal oxygenSaturation) {
    this.oxygenSaturation = oxygenSaturation;
    return this;
  }

  /**
   * 
   * @return oxygenSaturation
   */
  @javax.annotation.Nullable
  public BigDecimal getOxygenSaturation() {
    return oxygenSaturation;
  }

  public void setOxygenSaturation(BigDecimal oxygenSaturation) {
    this.oxygenSaturation = oxygenSaturation;
  }


  public SystemVitals pain(String pain) {
    this.pain = pain;
    return this;
  }

  /**
   * 1-10 pain scale.
   * @return pain
   */
  @javax.annotation.Nullable
  public String getPain() {
    return pain;
  }

  public void setPain(String pain) {
    this.pain = pain;
  }


  public SystemVitals pulse(Integer pulse) {
    this.pulse = pulse;
    return this;
  }

  /**
   * Beats per minute.
   * @return pulse
   */
  @javax.annotation.Nullable
  public Integer getPulse() {
    return pulse;
  }

  public void setPulse(Integer pulse) {
    this.pulse = pulse;
  }


  public SystemVitals respiratoryRate(Integer respiratoryRate) {
    this.respiratoryRate = respiratoryRate;
    return this;
  }

  /**
   * Breathes per minute.
   * @return respiratoryRate
   */
  @javax.annotation.Nullable
  public Integer getRespiratoryRate() {
    return respiratoryRate;
  }

  public void setRespiratoryRate(Integer respiratoryRate) {
    this.respiratoryRate = respiratoryRate;
  }


  public SystemVitals smokingStatus(SmokingStatusEnum smokingStatus) {
    this.smokingStatus = smokingStatus;
    return this;
  }

  /**
   * 
   * @return smokingStatus
   */
  @javax.annotation.Nullable
  public SmokingStatusEnum getSmokingStatus() {
    return smokingStatus;
  }

  public void setSmokingStatus(SmokingStatusEnum smokingStatus) {
    this.smokingStatus = smokingStatus;
  }


  public SystemVitals temperature(BigDecimal temperature) {
    this.temperature = temperature;
    return this;
  }

  /**
   * 
   * @return temperature
   */
  @javax.annotation.Nullable
  public BigDecimal getTemperature() {
    return temperature;
  }

  public void setTemperature(BigDecimal temperature) {
    this.temperature = temperature;
  }


  public SystemVitals temperatureUnits(String temperatureUnits) {
    this.temperatureUnits = temperatureUnits;
    return this;
  }

  /**
   * 
   * @return temperatureUnits
   */
  @javax.annotation.Nullable
  public String getTemperatureUnits() {
    return temperatureUnits;
  }

  public void setTemperatureUnits(String temperatureUnits) {
    this.temperatureUnits = temperatureUnits;
  }


  public SystemVitals weight(BigDecimal weight) {
    this.weight = weight;
    return this;
  }

  /**
   * 
   * @return weight
   */
  @javax.annotation.Nullable
  public BigDecimal getWeight() {
    return weight;
  }

  public void setWeight(BigDecimal weight) {
    this.weight = weight;
  }


  public SystemVitals weightUnits(String weightUnits) {
    this.weightUnits = weightUnits;
    return this;
  }

  /**
   * 
   * @return weightUnits
   */
  @javax.annotation.Nullable
  public String getWeightUnits() {
    return weightUnits;
  }

  public void setWeightUnits(String weightUnits) {
    this.weightUnits = weightUnits;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SystemVitals systemVitals = (SystemVitals) o;
    return Objects.equals(this.bloodPressure1, systemVitals.bloodPressure1) &&
        Objects.equals(this.bloodPressure2, systemVitals.bloodPressure2) &&
        Objects.equals(this.bmi, systemVitals.bmi) &&
        Objects.equals(this.headCircumference, systemVitals.headCircumference) &&
        Objects.equals(this.headCircumferenceUnits, systemVitals.headCircumferenceUnits) &&
        Objects.equals(this.height, systemVitals.height) &&
        Objects.equals(this.heightUnits, systemVitals.heightUnits) &&
        Objects.equals(this.oxygenSaturation, systemVitals.oxygenSaturation) &&
        Objects.equals(this.pain, systemVitals.pain) &&
        Objects.equals(this.pulse, systemVitals.pulse) &&
        Objects.equals(this.respiratoryRate, systemVitals.respiratoryRate) &&
        Objects.equals(this.smokingStatus, systemVitals.smokingStatus) &&
        Objects.equals(this.temperature, systemVitals.temperature) &&
        Objects.equals(this.temperatureUnits, systemVitals.temperatureUnits) &&
        Objects.equals(this.weight, systemVitals.weight) &&
        Objects.equals(this.weightUnits, systemVitals.weightUnits);
  }

  @Override
  public int hashCode() {
    return Objects.hash(bloodPressure1, bloodPressure2, bmi, headCircumference, headCircumferenceUnits, height, heightUnits, oxygenSaturation, pain, pulse, respiratoryRate, smokingStatus, temperature, temperatureUnits, weight, weightUnits);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SystemVitals {\n");
    sb.append("    bloodPressure1: ").append(toIndentedString(bloodPressure1)).append("\n");
    sb.append("    bloodPressure2: ").append(toIndentedString(bloodPressure2)).append("\n");
    sb.append("    bmi: ").append(toIndentedString(bmi)).append("\n");
    sb.append("    headCircumference: ").append(toIndentedString(headCircumference)).append("\n");
    sb.append("    headCircumferenceUnits: ").append(toIndentedString(headCircumferenceUnits)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    heightUnits: ").append(toIndentedString(heightUnits)).append("\n");
    sb.append("    oxygenSaturation: ").append(toIndentedString(oxygenSaturation)).append("\n");
    sb.append("    pain: ").append(toIndentedString(pain)).append("\n");
    sb.append("    pulse: ").append(toIndentedString(pulse)).append("\n");
    sb.append("    respiratoryRate: ").append(toIndentedString(respiratoryRate)).append("\n");
    sb.append("    smokingStatus: ").append(toIndentedString(smokingStatus)).append("\n");
    sb.append("    temperature: ").append(toIndentedString(temperature)).append("\n");
    sb.append("    temperatureUnits: ").append(toIndentedString(temperatureUnits)).append("\n");
    sb.append("    weight: ").append(toIndentedString(weight)).append("\n");
    sb.append("    weightUnits: ").append(toIndentedString(weightUnits)).append("\n");
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
    openapiFields.add("blood_pressure_1");
    openapiFields.add("blood_pressure_2");
    openapiFields.add("bmi");
    openapiFields.add("head_circumference");
    openapiFields.add("head_circumference_units");
    openapiFields.add("height");
    openapiFields.add("height_units");
    openapiFields.add("oxygen_saturation");
    openapiFields.add("pain");
    openapiFields.add("pulse");
    openapiFields.add("respiratory_rate");
    openapiFields.add("smoking_status");
    openapiFields.add("temperature");
    openapiFields.add("temperature_units");
    openapiFields.add("weight");
    openapiFields.add("weight_units");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SystemVitals
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SystemVitals.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SystemVitals is not found in the empty JSON string", SystemVitals.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SystemVitals.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SystemVitals` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("bmi") != null && !jsonObj.get("bmi").isJsonNull()) && !jsonObj.get("bmi").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `bmi` to be a primitive type in the JSON string but got `%s`", jsonObj.get("bmi").toString()));
      }
      if ((jsonObj.get("head_circumference_units") != null && !jsonObj.get("head_circumference_units").isJsonNull()) && !jsonObj.get("head_circumference_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `head_circumference_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("head_circumference_units").toString()));
      }
      if ((jsonObj.get("height_units") != null && !jsonObj.get("height_units").isJsonNull()) && !jsonObj.get("height_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `height_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("height_units").toString()));
      }
      if ((jsonObj.get("pain") != null && !jsonObj.get("pain").isJsonNull()) && !jsonObj.get("pain").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pain` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pain").toString()));
      }
      if ((jsonObj.get("smoking_status") != null && !jsonObj.get("smoking_status").isJsonNull()) && !jsonObj.get("smoking_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `smoking_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("smoking_status").toString()));
      }
      // validate the optional field `smoking_status`
      if (jsonObj.get("smoking_status") != null && !jsonObj.get("smoking_status").isJsonNull()) {
        SmokingStatusEnum.validateJsonElement(jsonObj.get("smoking_status"));
      }
      if ((jsonObj.get("temperature_units") != null && !jsonObj.get("temperature_units").isJsonNull()) && !jsonObj.get("temperature_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `temperature_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("temperature_units").toString()));
      }
      if ((jsonObj.get("weight_units") != null && !jsonObj.get("weight_units").isJsonNull()) && !jsonObj.get("weight_units").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `weight_units` to be a primitive type in the JSON string but got `%s`", jsonObj.get("weight_units").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SystemVitals.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SystemVitals' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SystemVitals> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SystemVitals.class));

       return (TypeAdapter<T>) new TypeAdapter<SystemVitals>() {
           @Override
           public void write(JsonWriter out, SystemVitals value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SystemVitals read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SystemVitals given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SystemVitals
   * @throws IOException if the JSON string is invalid with respect to SystemVitals
   */
  public static SystemVitals fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SystemVitals.class);
  }

  /**
   * Convert an instance of SystemVitals to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

