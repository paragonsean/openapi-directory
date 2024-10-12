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
import org.openapitools.client.model.MessageNote;

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
 * DoctorMessage
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:50.017060-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DoctorMessage {
  public static final String SERIALIZED_NAME_ARCHIVED = "archived";
  @SerializedName(SERIALIZED_NAME_ARCHIVED)
  private Boolean archived;

  public static final String SERIALIZED_NAME_ATTACHMENT = "attachment";
  @SerializedName(SERIALIZED_NAME_ATTACHMENT)
  private String attachment;

  public static final String SERIALIZED_NAME_DOCTOR = "doctor";
  @SerializedName(SERIALIZED_NAME_DOCTOR)
  private Integer doctor;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_MESSAGE_NOTES = "message_notes";
  @SerializedName(SERIALIZED_NAME_MESSAGE_NOTES)
  private List<MessageNote> messageNotes = new ArrayList<>();

  public static final String SERIALIZED_NAME_OWNER = "owner";
  @SerializedName(SERIALIZED_NAME_OWNER)
  private String owner;

  public static final String SERIALIZED_NAME_PATIENT = "patient";
  @SerializedName(SERIALIZED_NAME_PATIENT)
  private Integer patient;

  public static final String SERIALIZED_NAME_READ = "read";
  @SerializedName(SERIALIZED_NAME_READ)
  private Boolean read;

  public static final String SERIALIZED_NAME_RECEIVED_AT = "received_at";
  @SerializedName(SERIALIZED_NAME_RECEIVED_AT)
  private String receivedAt;

  public static final String SERIALIZED_NAME_RESPONSIBLE_USER = "responsible_user";
  @SerializedName(SERIALIZED_NAME_RESPONSIBLE_USER)
  private String responsibleUser;

  public static final String SERIALIZED_NAME_STARRED = "starred";
  @SerializedName(SERIALIZED_NAME_STARRED)
  private Boolean starred;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  /**
   *  Value | Description ----- | ----------- &#x60;\&quot;GP\&quot;&#x60; | Generated PDF &#x60;\&quot;GC\&quot;&#x60; | Generated CSV &#x60;\&quot;GZ\&quot;&#x60; | Generated ZIP &#x60;\&quot;IF\&quot;&#x60; | Incoming Fax &#x60;\&quot;OF\&quot;&#x60; | Outgoing Fax &#x60;\&quot;IL\&quot;&#x60; | Incoming Labs &#x60;\&quot;IR\&quot;&#x60; | Inbound Referrals &#x60;\&quot;OR\&quot;&#x60; | Outbound Referrals &#x60;\&quot;IE\&quot;&#x60; | Incoming eRx &#x60;\&quot;OA\&quot;&#x60; | Online Appointments &#x60;\&quot;PO\&quot;&#x60; | Patient Onboarding &#x60;\&quot;PI\&quot;&#x60; | Patient Incoming Message &#x60;\&quot;PM\&quot;&#x60; | Patient Outgoing Message &#x60;\&quot;OO\&quot;&#x60; | Demo Meeting Message &#x60;\&quot;OD\&quot;&#x60; | Outbound Direct Message &#x60;\&quot;ID\&quot;&#x60; | Inbound Direct Message 
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    GP("GP"),
    
    GC("GC"),
    
    GT("GT"),
    
    GZ("GZ"),
    
    IF("IF"),
    
    OF("OF"),
    
    IL("IL"),
    
    IR("IR"),
    
    OR("OR"),
    
    IE("IE"),
    
    OA("OA"),
    
    PO("PO"),
    
    PI("PI"),
    
    PM("PM"),
    
    OO("OO"),
    
    OD("OD"),
    
    ID("ID"),
    
    DL("DL"),
    
    CN("CN");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updated_at";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private String updatedAt;

  public static final String SERIALIZED_NAME_WORKFLOW_STEP = "workflow_step";
  @SerializedName(SERIALIZED_NAME_WORKFLOW_STEP)
  private String workflowStep;

  public DoctorMessage() {
  }

  public DoctorMessage(
     Boolean archived, 
     Integer id, 
     Boolean read, 
     String receivedAt, 
     Boolean starred, 
     String updatedAt, 
     String workflowStep
  ) {
    this();
    this.archived = archived;
    this.id = id;
    this.read = read;
    this.receivedAt = receivedAt;
    this.starred = starred;
    this.updatedAt = updatedAt;
    this.workflowStep = workflowStep;
  }

  /**
   * If true, indicates that the message has been soft-deleted
   * @return archived
   */
  @javax.annotation.Nullable
  public Boolean getArchived() {
    return archived;
  }



  public DoctorMessage attachment(String attachment) {
    this.attachment = attachment;
    return this;
  }

  /**
   * Files are passed using &#x60;multipart/form-data&#x60; encoding, but returned as URLs.
   * @return attachment
   */
  @javax.annotation.Nullable
  public String getAttachment() {
    return attachment;
  }

  public void setAttachment(String attachment) {
    this.attachment = attachment;
  }


  public DoctorMessage doctor(Integer doctor) {
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


  /**
   * 
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }



  public DoctorMessage messageNotes(List<MessageNote> messageNotes) {
    this.messageNotes = messageNotes;
    return this;
  }

  public DoctorMessage addMessageNotesItem(MessageNote messageNotesItem) {
    if (this.messageNotes == null) {
      this.messageNotes = new ArrayList<>();
    }
    this.messageNotes.add(messageNotesItem);
    return this;
  }

  /**
   * Array of notes attached to the message
   * @return messageNotes
   */
  @javax.annotation.Nullable
  public List<MessageNote> getMessageNotes() {
    return messageNotes;
  }

  public void setMessageNotes(List<MessageNote> messageNotes) {
    this.messageNotes = messageNotes;
  }


  public DoctorMessage owner(String owner) {
    this.owner = owner;
    return this;
  }

  /**
   * ID of &#x60;/api/users&#x60; who owns the message, who may be the doctor themselves or one of their staff members
   * @return owner
   */
  @javax.annotation.Nullable
  public String getOwner() {
    return owner;
  }

  public void setOwner(String owner) {
    this.owner = owner;
  }


  public DoctorMessage patient(Integer patient) {
    this.patient = patient;
    return this;
  }

  /**
   * ID of patient that the message concerns, if applicable
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
   * 
   * @return read
   */
  @javax.annotation.Nullable
  public Boolean getRead() {
    return read;
  }



  /**
   * 
   * @return receivedAt
   */
  @javax.annotation.Nullable
  public String getReceivedAt() {
    return receivedAt;
  }



  public DoctorMessage responsibleUser(String responsibleUser) {
    this.responsibleUser = responsibleUser;
    return this;
  }

  /**
   * ID of &#x60;/api/users&#x60; who has been assigned to process the message, who may be the doctor themselves or one of their staff members
   * @return responsibleUser
   */
  @javax.annotation.Nullable
  public String getResponsibleUser() {
    return responsibleUser;
  }

  public void setResponsibleUser(String responsibleUser) {
    this.responsibleUser = responsibleUser;
  }


  /**
   * 
   * @return starred
   */
  @javax.annotation.Nullable
  public Boolean getStarred() {
    return starred;
  }



  public DoctorMessage title(String title) {
    this.title = title;
    return this;
  }

  /**
   * 
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public DoctorMessage type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   *  Value | Description ----- | ----------- &#x60;\&quot;GP\&quot;&#x60; | Generated PDF &#x60;\&quot;GC\&quot;&#x60; | Generated CSV &#x60;\&quot;GZ\&quot;&#x60; | Generated ZIP &#x60;\&quot;IF\&quot;&#x60; | Incoming Fax &#x60;\&quot;OF\&quot;&#x60; | Outgoing Fax &#x60;\&quot;IL\&quot;&#x60; | Incoming Labs &#x60;\&quot;IR\&quot;&#x60; | Inbound Referrals &#x60;\&quot;OR\&quot;&#x60; | Outbound Referrals &#x60;\&quot;IE\&quot;&#x60; | Incoming eRx &#x60;\&quot;OA\&quot;&#x60; | Online Appointments &#x60;\&quot;PO\&quot;&#x60; | Patient Onboarding &#x60;\&quot;PI\&quot;&#x60; | Patient Incoming Message &#x60;\&quot;PM\&quot;&#x60; | Patient Outgoing Message &#x60;\&quot;OO\&quot;&#x60; | Demo Meeting Message &#x60;\&quot;OD\&quot;&#x60; | Outbound Direct Message &#x60;\&quot;ID\&quot;&#x60; | Inbound Direct Message 
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }


  /**
   * 
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public String getUpdatedAt() {
    return updatedAt;
  }



  /**
   * Used by doctors and their staff to keep track of what step of processing the message is in
   * @return workflowStep
   */
  @javax.annotation.Nullable
  public String getWorkflowStep() {
    return workflowStep;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DoctorMessage doctorMessage = (DoctorMessage) o;
    return Objects.equals(this.archived, doctorMessage.archived) &&
        Objects.equals(this.attachment, doctorMessage.attachment) &&
        Objects.equals(this.doctor, doctorMessage.doctor) &&
        Objects.equals(this.id, doctorMessage.id) &&
        Objects.equals(this.messageNotes, doctorMessage.messageNotes) &&
        Objects.equals(this.owner, doctorMessage.owner) &&
        Objects.equals(this.patient, doctorMessage.patient) &&
        Objects.equals(this.read, doctorMessage.read) &&
        Objects.equals(this.receivedAt, doctorMessage.receivedAt) &&
        Objects.equals(this.responsibleUser, doctorMessage.responsibleUser) &&
        Objects.equals(this.starred, doctorMessage.starred) &&
        Objects.equals(this.title, doctorMessage.title) &&
        Objects.equals(this.type, doctorMessage.type) &&
        Objects.equals(this.updatedAt, doctorMessage.updatedAt) &&
        Objects.equals(this.workflowStep, doctorMessage.workflowStep);
  }

  @Override
  public int hashCode() {
    return Objects.hash(archived, attachment, doctor, id, messageNotes, owner, patient, read, receivedAt, responsibleUser, starred, title, type, updatedAt, workflowStep);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DoctorMessage {\n");
    sb.append("    archived: ").append(toIndentedString(archived)).append("\n");
    sb.append("    attachment: ").append(toIndentedString(attachment)).append("\n");
    sb.append("    doctor: ").append(toIndentedString(doctor)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    messageNotes: ").append(toIndentedString(messageNotes)).append("\n");
    sb.append("    owner: ").append(toIndentedString(owner)).append("\n");
    sb.append("    patient: ").append(toIndentedString(patient)).append("\n");
    sb.append("    read: ").append(toIndentedString(read)).append("\n");
    sb.append("    receivedAt: ").append(toIndentedString(receivedAt)).append("\n");
    sb.append("    responsibleUser: ").append(toIndentedString(responsibleUser)).append("\n");
    sb.append("    starred: ").append(toIndentedString(starred)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    workflowStep: ").append(toIndentedString(workflowStep)).append("\n");
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
    openapiFields.add("archived");
    openapiFields.add("attachment");
    openapiFields.add("doctor");
    openapiFields.add("id");
    openapiFields.add("message_notes");
    openapiFields.add("owner");
    openapiFields.add("patient");
    openapiFields.add("read");
    openapiFields.add("received_at");
    openapiFields.add("responsible_user");
    openapiFields.add("starred");
    openapiFields.add("title");
    openapiFields.add("type");
    openapiFields.add("updated_at");
    openapiFields.add("workflow_step");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("doctor");
    openapiRequiredFields.add("title");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DoctorMessage
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DoctorMessage.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DoctorMessage is not found in the empty JSON string", DoctorMessage.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DoctorMessage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DoctorMessage` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : DoctorMessage.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("attachment") != null && !jsonObj.get("attachment").isJsonNull()) && !jsonObj.get("attachment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `attachment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("attachment").toString()));
      }
      if (jsonObj.get("message_notes") != null && !jsonObj.get("message_notes").isJsonNull()) {
        JsonArray jsonArraymessageNotes = jsonObj.getAsJsonArray("message_notes");
        if (jsonArraymessageNotes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("message_notes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `message_notes` to be an array in the JSON string but got `%s`", jsonObj.get("message_notes").toString()));
          }

          // validate the optional field `message_notes` (array)
          for (int i = 0; i < jsonArraymessageNotes.size(); i++) {
            MessageNote.validateJsonElement(jsonArraymessageNotes.get(i));
          };
        }
      }
      if ((jsonObj.get("owner") != null && !jsonObj.get("owner").isJsonNull()) && !jsonObj.get("owner").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `owner` to be a primitive type in the JSON string but got `%s`", jsonObj.get("owner").toString()));
      }
      if ((jsonObj.get("received_at") != null && !jsonObj.get("received_at").isJsonNull()) && !jsonObj.get("received_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `received_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("received_at").toString()));
      }
      if ((jsonObj.get("responsible_user") != null && !jsonObj.get("responsible_user").isJsonNull()) && !jsonObj.get("responsible_user").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `responsible_user` to be a primitive type in the JSON string but got `%s`", jsonObj.get("responsible_user").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
      if ((jsonObj.get("updated_at") != null && !jsonObj.get("updated_at").isJsonNull()) && !jsonObj.get("updated_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `updated_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("updated_at").toString()));
      }
      if ((jsonObj.get("workflow_step") != null && !jsonObj.get("workflow_step").isJsonNull()) && !jsonObj.get("workflow_step").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workflow_step` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workflow_step").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DoctorMessage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DoctorMessage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DoctorMessage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DoctorMessage.class));

       return (TypeAdapter<T>) new TypeAdapter<DoctorMessage>() {
           @Override
           public void write(JsonWriter out, DoctorMessage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DoctorMessage read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DoctorMessage given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DoctorMessage
   * @throws IOException if the JSON string is invalid with respect to DoctorMessage
   */
  public static DoctorMessage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DoctorMessage.class);
  }

  /**
   * Convert an instance of DoctorMessage to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

