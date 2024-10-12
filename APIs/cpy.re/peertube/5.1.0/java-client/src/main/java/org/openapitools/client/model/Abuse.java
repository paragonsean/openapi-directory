/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AbuseStateConstant;
import org.openapitools.client.model.Account;
import org.openapitools.client.model.VideoInfo;

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
 * Abuse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Abuse {
  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_MODERATION_COMMENT = "moderationComment";
  @SerializedName(SERIALIZED_NAME_MODERATION_COMMENT)
  private String moderationComment;

  /**
   * Gets or Sets predefinedReasons
   */
  @JsonAdapter(PredefinedReasonsEnum.Adapter.class)
  public enum PredefinedReasonsEnum {
    VIOLENT_OR_ABUSIVE("violentOrAbusive"),
    
    HATEFUL_OR_ABUSIVE("hatefulOrAbusive"),
    
    SPAM_OR_MISLEADING("spamOrMisleading"),
    
    PRIVACY("privacy"),
    
    RIGHTS("rights"),
    
    SERVER_RULES("serverRules"),
    
    THUMBNAILS("thumbnails"),
    
    CAPTIONS("captions");

    private String value;

    PredefinedReasonsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PredefinedReasonsEnum fromValue(String value) {
      for (PredefinedReasonsEnum b : PredefinedReasonsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PredefinedReasonsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PredefinedReasonsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PredefinedReasonsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PredefinedReasonsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PredefinedReasonsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PREDEFINED_REASONS = "predefinedReasons";
  @SerializedName(SERIALIZED_NAME_PREDEFINED_REASONS)
  private List<PredefinedReasonsEnum> predefinedReasons = new ArrayList<>();

  public static final String SERIALIZED_NAME_REASON = "reason";
  @SerializedName(SERIALIZED_NAME_REASON)
  private String reason;

  public static final String SERIALIZED_NAME_REPORTER_ACCOUNT = "reporterAccount";
  @SerializedName(SERIALIZED_NAME_REPORTER_ACCOUNT)
  private Account reporterAccount;

  public static final String SERIALIZED_NAME_STATE = "state";
  @SerializedName(SERIALIZED_NAME_STATE)
  private AbuseStateConstant state;

  public static final String SERIALIZED_NAME_VIDEO = "video";
  @SerializedName(SERIALIZED_NAME_VIDEO)
  private VideoInfo video;

  public Abuse() {
  }

  public Abuse createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public Abuse id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * minimum: 1
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public Abuse moderationComment(String moderationComment) {
    this.moderationComment = moderationComment;
    return this;
  }

  /**
   * Get moderationComment
   * @return moderationComment
   */
  @javax.annotation.Nullable
  public String getModerationComment() {
    return moderationComment;
  }

  public void setModerationComment(String moderationComment) {
    this.moderationComment = moderationComment;
  }


  public Abuse predefinedReasons(List<PredefinedReasonsEnum> predefinedReasons) {
    this.predefinedReasons = predefinedReasons;
    return this;
  }

  public Abuse addPredefinedReasonsItem(PredefinedReasonsEnum predefinedReasonsItem) {
    if (this.predefinedReasons == null) {
      this.predefinedReasons = new ArrayList<>();
    }
    this.predefinedReasons.add(predefinedReasonsItem);
    return this;
  }

  /**
   * Get predefinedReasons
   * @return predefinedReasons
   */
  @javax.annotation.Nullable
  public List<PredefinedReasonsEnum> getPredefinedReasons() {
    return predefinedReasons;
  }

  public void setPredefinedReasons(List<PredefinedReasonsEnum> predefinedReasons) {
    this.predefinedReasons = predefinedReasons;
  }


  public Abuse reason(String reason) {
    this.reason = reason;
    return this;
  }

  /**
   * Get reason
   * @return reason
   */
  @javax.annotation.Nullable
  public String getReason() {
    return reason;
  }

  public void setReason(String reason) {
    this.reason = reason;
  }


  public Abuse reporterAccount(Account reporterAccount) {
    this.reporterAccount = reporterAccount;
    return this;
  }

  /**
   * Get reporterAccount
   * @return reporterAccount
   */
  @javax.annotation.Nullable
  public Account getReporterAccount() {
    return reporterAccount;
  }

  public void setReporterAccount(Account reporterAccount) {
    this.reporterAccount = reporterAccount;
  }


  public Abuse state(AbuseStateConstant state) {
    this.state = state;
    return this;
  }

  /**
   * Get state
   * @return state
   */
  @javax.annotation.Nullable
  public AbuseStateConstant getState() {
    return state;
  }

  public void setState(AbuseStateConstant state) {
    this.state = state;
  }


  public Abuse video(VideoInfo video) {
    this.video = video;
    return this;
  }

  /**
   * Get video
   * @return video
   */
  @javax.annotation.Nullable
  public VideoInfo getVideo() {
    return video;
  }

  public void setVideo(VideoInfo video) {
    this.video = video;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Abuse abuse = (Abuse) o;
    return Objects.equals(this.createdAt, abuse.createdAt) &&
        Objects.equals(this.id, abuse.id) &&
        Objects.equals(this.moderationComment, abuse.moderationComment) &&
        Objects.equals(this.predefinedReasons, abuse.predefinedReasons) &&
        Objects.equals(this.reason, abuse.reason) &&
        Objects.equals(this.reporterAccount, abuse.reporterAccount) &&
        Objects.equals(this.state, abuse.state) &&
        Objects.equals(this.video, abuse.video);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, id, moderationComment, predefinedReasons, reason, reporterAccount, state, video);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Abuse {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    moderationComment: ").append(toIndentedString(moderationComment)).append("\n");
    sb.append("    predefinedReasons: ").append(toIndentedString(predefinedReasons)).append("\n");
    sb.append("    reason: ").append(toIndentedString(reason)).append("\n");
    sb.append("    reporterAccount: ").append(toIndentedString(reporterAccount)).append("\n");
    sb.append("    state: ").append(toIndentedString(state)).append("\n");
    sb.append("    video: ").append(toIndentedString(video)).append("\n");
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
    openapiFields.add("createdAt");
    openapiFields.add("id");
    openapiFields.add("moderationComment");
    openapiFields.add("predefinedReasons");
    openapiFields.add("reason");
    openapiFields.add("reporterAccount");
    openapiFields.add("state");
    openapiFields.add("video");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Abuse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Abuse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Abuse is not found in the empty JSON string", Abuse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Abuse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Abuse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("moderationComment") != null && !jsonObj.get("moderationComment").isJsonNull()) && !jsonObj.get("moderationComment").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `moderationComment` to be a primitive type in the JSON string but got `%s`", jsonObj.get("moderationComment").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("predefinedReasons") != null && !jsonObj.get("predefinedReasons").isJsonNull() && !jsonObj.get("predefinedReasons").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `predefinedReasons` to be an array in the JSON string but got `%s`", jsonObj.get("predefinedReasons").toString()));
      }
      if ((jsonObj.get("reason") != null && !jsonObj.get("reason").isJsonNull()) && !jsonObj.get("reason").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `reason` to be a primitive type in the JSON string but got `%s`", jsonObj.get("reason").toString()));
      }
      // validate the optional field `reporterAccount`
      if (jsonObj.get("reporterAccount") != null && !jsonObj.get("reporterAccount").isJsonNull()) {
        Account.validateJsonElement(jsonObj.get("reporterAccount"));
      }
      // validate the optional field `state`
      if (jsonObj.get("state") != null && !jsonObj.get("state").isJsonNull()) {
        AbuseStateConstant.validateJsonElement(jsonObj.get("state"));
      }
      // validate the optional field `video`
      if (jsonObj.get("video") != null && !jsonObj.get("video").isJsonNull()) {
        VideoInfo.validateJsonElement(jsonObj.get("video"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Abuse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Abuse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Abuse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Abuse.class));

       return (TypeAdapter<T>) new TypeAdapter<Abuse>() {
           @Override
           public void write(JsonWriter out, Abuse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Abuse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Abuse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Abuse
   * @throws IOException if the JSON string is invalid with respect to Abuse
   */
  public static Abuse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Abuse.class);
  }

  /**
   * Convert an instance of Abuse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

