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
import org.openapitools.client.model.ActorImage;
import org.openapitools.client.model.VideoChannelAllOfOwnerAccount;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * VideoChannelListDataInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VideoChannelListDataInner {
  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_FOLLOWERS_COUNT = "followersCount";
  @SerializedName(SERIALIZED_NAME_FOLLOWERS_COUNT)
  private Integer followersCount;

  public static final String SERIALIZED_NAME_FOLLOWING_COUNT = "followingCount";
  @SerializedName(SERIALIZED_NAME_FOLLOWING_COUNT)
  private Integer followingCount;

  public static final String SERIALIZED_NAME_HOST = "host";
  @SerializedName(SERIALIZED_NAME_HOST)
  private String host;

  public static final String SERIALIZED_NAME_HOST_REDUNDANCY_ALLOWED = "hostRedundancyAllowed";
  @SerializedName(SERIALIZED_NAME_HOST_REDUNDANCY_ALLOWED)
  private Boolean hostRedundancyAllowed;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public static final String SERIALIZED_NAME_BANNERS = "banners";
  @SerializedName(SERIALIZED_NAME_BANNERS)
  private List<ActorImage> banners = new ArrayList<>();

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DISPLAY_NAME = "displayName";
  @SerializedName(SERIALIZED_NAME_DISPLAY_NAME)
  private String displayName;

  public static final String SERIALIZED_NAME_IS_LOCAL = "isLocal";
  @SerializedName(SERIALIZED_NAME_IS_LOCAL)
  private Boolean isLocal;

  public static final String SERIALIZED_NAME_OWNER_ACCOUNT = "ownerAccount";
  @SerializedName(SERIALIZED_NAME_OWNER_ACCOUNT)
  private VideoChannelAllOfOwnerAccount ownerAccount;

  public static final String SERIALIZED_NAME_SUPPORT = "support";
  @SerializedName(SERIALIZED_NAME_SUPPORT)
  private String support;

  public VideoChannelListDataInner() {
  }

  public VideoChannelListDataInner(
     Boolean isLocal
  ) {
    this();
    this.isLocal = isLocal;
  }

  public VideoChannelListDataInner createdAt(OffsetDateTime createdAt) {
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


  public VideoChannelListDataInner followersCount(Integer followersCount) {
    this.followersCount = followersCount;
    return this;
  }

  /**
   * number of followers of this actor, as seen by this instance
   * minimum: 0
   * @return followersCount
   */
  @javax.annotation.Nullable
  public Integer getFollowersCount() {
    return followersCount;
  }

  public void setFollowersCount(Integer followersCount) {
    this.followersCount = followersCount;
  }


  public VideoChannelListDataInner followingCount(Integer followingCount) {
    this.followingCount = followingCount;
    return this;
  }

  /**
   * number of actors subscribed to by this actor, as seen by this instance
   * minimum: 0
   * @return followingCount
   */
  @javax.annotation.Nullable
  public Integer getFollowingCount() {
    return followingCount;
  }

  public void setFollowingCount(Integer followingCount) {
    this.followingCount = followingCount;
  }


  public VideoChannelListDataInner host(String host) {
    this.host = host;
    return this;
  }

  /**
   * server on which the actor is resident
   * @return host
   */
  @javax.annotation.Nullable
  public String getHost() {
    return host;
  }

  public void setHost(String host) {
    this.host = host;
  }


  public VideoChannelListDataInner hostRedundancyAllowed(Boolean hostRedundancyAllowed) {
    this.hostRedundancyAllowed = hostRedundancyAllowed;
    return this;
  }

  /**
   * whether this actor&#39;s host allows redundancy of its videos
   * @return hostRedundancyAllowed
   */
  @javax.annotation.Nullable
  public Boolean getHostRedundancyAllowed() {
    return hostRedundancyAllowed;
  }

  public void setHostRedundancyAllowed(Boolean hostRedundancyAllowed) {
    this.hostRedundancyAllowed = hostRedundancyAllowed;
  }


  public VideoChannelListDataInner id(Integer id) {
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


  public VideoChannelListDataInner name(String name) {
    this.name = name;
    return this;
  }

  /**
   * immutable name of the actor, used to find or mention it
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public VideoChannelListDataInner updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }


  public VideoChannelListDataInner url(String url) {
    this.url = url;
    return this;
  }

  /**
   * Get url
   * @return url
   */
  @javax.annotation.Nullable
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }


  public VideoChannelListDataInner banners(List<ActorImage> banners) {
    this.banners = banners;
    return this;
  }

  public VideoChannelListDataInner addBannersItem(ActorImage bannersItem) {
    if (this.banners == null) {
      this.banners = new ArrayList<>();
    }
    this.banners.add(bannersItem);
    return this;
  }

  /**
   * Get banners
   * @return banners
   */
  @javax.annotation.Nullable
  public List<ActorImage> getBanners() {
    return banners;
  }

  public void setBanners(List<ActorImage> banners) {
    this.banners = banners;
  }


  public VideoChannelListDataInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public VideoChannelListDataInner displayName(String displayName) {
    this.displayName = displayName;
    return this;
  }

  /**
   * editable name of the channel, displayed in its representations
   * @return displayName
   */
  @javax.annotation.Nullable
  public String getDisplayName() {
    return displayName;
  }

  public void setDisplayName(String displayName) {
    this.displayName = displayName;
  }


  /**
   * Get isLocal
   * @return isLocal
   */
  @javax.annotation.Nullable
  public Boolean getIsLocal() {
    return isLocal;
  }



  public VideoChannelListDataInner ownerAccount(VideoChannelAllOfOwnerAccount ownerAccount) {
    this.ownerAccount = ownerAccount;
    return this;
  }

  /**
   * Get ownerAccount
   * @return ownerAccount
   */
  @javax.annotation.Nullable
  public VideoChannelAllOfOwnerAccount getOwnerAccount() {
    return ownerAccount;
  }

  public void setOwnerAccount(VideoChannelAllOfOwnerAccount ownerAccount) {
    this.ownerAccount = ownerAccount;
  }


  public VideoChannelListDataInner support(String support) {
    this.support = support;
    return this;
  }

  /**
   * text shown by default on all videos of this channel, to tell the audience how to support it
   * @return support
   */
  @javax.annotation.Nullable
  public String getSupport() {
    return support;
  }

  public void setSupport(String support) {
    this.support = support;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VideoChannelListDataInner videoChannelListDataInner = (VideoChannelListDataInner) o;
    return Objects.equals(this.createdAt, videoChannelListDataInner.createdAt) &&
        Objects.equals(this.followersCount, videoChannelListDataInner.followersCount) &&
        Objects.equals(this.followingCount, videoChannelListDataInner.followingCount) &&
        Objects.equals(this.host, videoChannelListDataInner.host) &&
        Objects.equals(this.hostRedundancyAllowed, videoChannelListDataInner.hostRedundancyAllowed) &&
        Objects.equals(this.id, videoChannelListDataInner.id) &&
        Objects.equals(this.name, videoChannelListDataInner.name) &&
        Objects.equals(this.updatedAt, videoChannelListDataInner.updatedAt) &&
        Objects.equals(this.url, videoChannelListDataInner.url) &&
        Objects.equals(this.banners, videoChannelListDataInner.banners) &&
        Objects.equals(this.description, videoChannelListDataInner.description) &&
        Objects.equals(this.displayName, videoChannelListDataInner.displayName) &&
        Objects.equals(this.isLocal, videoChannelListDataInner.isLocal) &&
        Objects.equals(this.ownerAccount, videoChannelListDataInner.ownerAccount) &&
        Objects.equals(this.support, videoChannelListDataInner.support);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, followersCount, followingCount, host, hostRedundancyAllowed, id, name, updatedAt, url, banners, description, displayName, isLocal, ownerAccount, support);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VideoChannelListDataInner {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    followersCount: ").append(toIndentedString(followersCount)).append("\n");
    sb.append("    followingCount: ").append(toIndentedString(followingCount)).append("\n");
    sb.append("    host: ").append(toIndentedString(host)).append("\n");
    sb.append("    hostRedundancyAllowed: ").append(toIndentedString(hostRedundancyAllowed)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
    sb.append("    banners: ").append(toIndentedString(banners)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    displayName: ").append(toIndentedString(displayName)).append("\n");
    sb.append("    isLocal: ").append(toIndentedString(isLocal)).append("\n");
    sb.append("    ownerAccount: ").append(toIndentedString(ownerAccount)).append("\n");
    sb.append("    support: ").append(toIndentedString(support)).append("\n");
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
    openapiFields.add("followersCount");
    openapiFields.add("followingCount");
    openapiFields.add("host");
    openapiFields.add("hostRedundancyAllowed");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("updatedAt");
    openapiFields.add("url");
    openapiFields.add("banners");
    openapiFields.add("description");
    openapiFields.add("displayName");
    openapiFields.add("isLocal");
    openapiFields.add("ownerAccount");
    openapiFields.add("support");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VideoChannelListDataInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VideoChannelListDataInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VideoChannelListDataInner is not found in the empty JSON string", VideoChannelListDataInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VideoChannelListDataInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VideoChannelListDataInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("host") != null && !jsonObj.get("host").isJsonNull()) && !jsonObj.get("host").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `host` to be a primitive type in the JSON string but got `%s`", jsonObj.get("host").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("url") != null && !jsonObj.get("url").isJsonNull()) && !jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
      if (jsonObj.get("banners") != null && !jsonObj.get("banners").isJsonNull()) {
        JsonArray jsonArraybanners = jsonObj.getAsJsonArray("banners");
        if (jsonArraybanners != null) {
          // ensure the json data is an array
          if (!jsonObj.get("banners").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `banners` to be an array in the JSON string but got `%s`", jsonObj.get("banners").toString()));
          }

          // validate the optional field `banners` (array)
          for (int i = 0; i < jsonArraybanners.size(); i++) {
            ActorImage.validateJsonElement(jsonArraybanners.get(i));
          };
        }
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("displayName") != null && !jsonObj.get("displayName").isJsonNull()) && !jsonObj.get("displayName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `displayName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("displayName").toString()));
      }
      // validate the optional field `ownerAccount`
      if (jsonObj.get("ownerAccount") != null && !jsonObj.get("ownerAccount").isJsonNull()) {
        VideoChannelAllOfOwnerAccount.validateJsonElement(jsonObj.get("ownerAccount"));
      }
      if ((jsonObj.get("support") != null && !jsonObj.get("support").isJsonNull()) && !jsonObj.get("support").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `support` to be a primitive type in the JSON string but got `%s`", jsonObj.get("support").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VideoChannelListDataInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VideoChannelListDataInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VideoChannelListDataInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VideoChannelListDataInner.class));

       return (TypeAdapter<T>) new TypeAdapter<VideoChannelListDataInner>() {
           @Override
           public void write(JsonWriter out, VideoChannelListDataInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VideoChannelListDataInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VideoChannelListDataInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VideoChannelListDataInner
   * @throws IOException if the JSON string is invalid with respect to VideoChannelListDataInner
   */
  public static VideoChannelListDataInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VideoChannelListDataInner.class);
  }

  /**
   * Convert an instance of VideoChannelListDataInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

