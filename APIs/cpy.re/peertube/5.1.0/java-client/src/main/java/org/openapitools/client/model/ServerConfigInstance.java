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
import java.util.Arrays;
import org.openapitools.client.model.ServerConfigInstanceCustomizations;

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
 * ServerConfigInstance
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:13.152727-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerConfigInstance {
  public static final String SERIALIZED_NAME_CUSTOMIZATIONS = "customizations";
  @SerializedName(SERIALIZED_NAME_CUSTOMIZATIONS)
  private ServerConfigInstanceCustomizations customizations;

  public static final String SERIALIZED_NAME_DEFAULT_CLIENT_ROUTE = "defaultClientRoute";
  @SerializedName(SERIALIZED_NAME_DEFAULT_CLIENT_ROUTE)
  private String defaultClientRoute;

  public static final String SERIALIZED_NAME_DEFAULT_N_S_F_W_POLICY = "defaultNSFWPolicy";
  @SerializedName(SERIALIZED_NAME_DEFAULT_N_S_F_W_POLICY)
  private String defaultNSFWPolicy;

  public static final String SERIALIZED_NAME_IS_N_S_F_W = "isNSFW";
  @SerializedName(SERIALIZED_NAME_IS_N_S_F_W)
  private Boolean isNSFW;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SHORT_DESCRIPTION = "shortDescription";
  @SerializedName(SERIALIZED_NAME_SHORT_DESCRIPTION)
  private String shortDescription;

  public ServerConfigInstance() {
  }

  public ServerConfigInstance customizations(ServerConfigInstanceCustomizations customizations) {
    this.customizations = customizations;
    return this;
  }

  /**
   * Get customizations
   * @return customizations
   */
  @javax.annotation.Nullable
  public ServerConfigInstanceCustomizations getCustomizations() {
    return customizations;
  }

  public void setCustomizations(ServerConfigInstanceCustomizations customizations) {
    this.customizations = customizations;
  }


  public ServerConfigInstance defaultClientRoute(String defaultClientRoute) {
    this.defaultClientRoute = defaultClientRoute;
    return this;
  }

  /**
   * Get defaultClientRoute
   * @return defaultClientRoute
   */
  @javax.annotation.Nullable
  public String getDefaultClientRoute() {
    return defaultClientRoute;
  }

  public void setDefaultClientRoute(String defaultClientRoute) {
    this.defaultClientRoute = defaultClientRoute;
  }


  public ServerConfigInstance defaultNSFWPolicy(String defaultNSFWPolicy) {
    this.defaultNSFWPolicy = defaultNSFWPolicy;
    return this;
  }

  /**
   * Get defaultNSFWPolicy
   * @return defaultNSFWPolicy
   */
  @javax.annotation.Nullable
  public String getDefaultNSFWPolicy() {
    return defaultNSFWPolicy;
  }

  public void setDefaultNSFWPolicy(String defaultNSFWPolicy) {
    this.defaultNSFWPolicy = defaultNSFWPolicy;
  }


  public ServerConfigInstance isNSFW(Boolean isNSFW) {
    this.isNSFW = isNSFW;
    return this;
  }

  /**
   * Get isNSFW
   * @return isNSFW
   */
  @javax.annotation.Nullable
  public Boolean getIsNSFW() {
    return isNSFW;
  }

  public void setIsNSFW(Boolean isNSFW) {
    this.isNSFW = isNSFW;
  }


  public ServerConfigInstance name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public ServerConfigInstance shortDescription(String shortDescription) {
    this.shortDescription = shortDescription;
    return this;
  }

  /**
   * Get shortDescription
   * @return shortDescription
   */
  @javax.annotation.Nullable
  public String getShortDescription() {
    return shortDescription;
  }

  public void setShortDescription(String shortDescription) {
    this.shortDescription = shortDescription;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ServerConfigInstance serverConfigInstance = (ServerConfigInstance) o;
    return Objects.equals(this.customizations, serverConfigInstance.customizations) &&
        Objects.equals(this.defaultClientRoute, serverConfigInstance.defaultClientRoute) &&
        Objects.equals(this.defaultNSFWPolicy, serverConfigInstance.defaultNSFWPolicy) &&
        Objects.equals(this.isNSFW, serverConfigInstance.isNSFW) &&
        Objects.equals(this.name, serverConfigInstance.name) &&
        Objects.equals(this.shortDescription, serverConfigInstance.shortDescription);
  }

  @Override
  public int hashCode() {
    return Objects.hash(customizations, defaultClientRoute, defaultNSFWPolicy, isNSFW, name, shortDescription);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ServerConfigInstance {\n");
    sb.append("    customizations: ").append(toIndentedString(customizations)).append("\n");
    sb.append("    defaultClientRoute: ").append(toIndentedString(defaultClientRoute)).append("\n");
    sb.append("    defaultNSFWPolicy: ").append(toIndentedString(defaultNSFWPolicy)).append("\n");
    sb.append("    isNSFW: ").append(toIndentedString(isNSFW)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    shortDescription: ").append(toIndentedString(shortDescription)).append("\n");
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
    openapiFields.add("customizations");
    openapiFields.add("defaultClientRoute");
    openapiFields.add("defaultNSFWPolicy");
    openapiFields.add("isNSFW");
    openapiFields.add("name");
    openapiFields.add("shortDescription");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ServerConfigInstance
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ServerConfigInstance.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ServerConfigInstance is not found in the empty JSON string", ServerConfigInstance.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ServerConfigInstance.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ServerConfigInstance` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `customizations`
      if (jsonObj.get("customizations") != null && !jsonObj.get("customizations").isJsonNull()) {
        ServerConfigInstanceCustomizations.validateJsonElement(jsonObj.get("customizations"));
      }
      if ((jsonObj.get("defaultClientRoute") != null && !jsonObj.get("defaultClientRoute").isJsonNull()) && !jsonObj.get("defaultClientRoute").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `defaultClientRoute` to be a primitive type in the JSON string but got `%s`", jsonObj.get("defaultClientRoute").toString()));
      }
      if ((jsonObj.get("defaultNSFWPolicy") != null && !jsonObj.get("defaultNSFWPolicy").isJsonNull()) && !jsonObj.get("defaultNSFWPolicy").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `defaultNSFWPolicy` to be a primitive type in the JSON string but got `%s`", jsonObj.get("defaultNSFWPolicy").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("shortDescription") != null && !jsonObj.get("shortDescription").isJsonNull()) && !jsonObj.get("shortDescription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shortDescription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shortDescription").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ServerConfigInstance.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ServerConfigInstance' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ServerConfigInstance> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ServerConfigInstance.class));

       return (TypeAdapter<T>) new TypeAdapter<ServerConfigInstance>() {
           @Override
           public void write(JsonWriter out, ServerConfigInstance value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ServerConfigInstance read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ServerConfigInstance given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ServerConfigInstance
   * @throws IOException if the JSON string is invalid with respect to ServerConfigInstance
   */
  public static ServerConfigInstance fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ServerConfigInstance.class);
  }

  /**
   * Convert an instance of ServerConfigInstance to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

