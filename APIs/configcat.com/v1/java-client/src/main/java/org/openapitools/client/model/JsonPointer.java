/*
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
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
import org.openapitools.client.model.JsonPointerKind;
import org.openapitools.client.model.PointerSegment;
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
 * JsonPointer
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:46.616681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class JsonPointer {
  public static final String SERIALIZED_NAME_IS_URI_ENCODED = "isUriEncoded";
  @SerializedName(SERIALIZED_NAME_IS_URI_ENCODED)
  private Boolean isUriEncoded;

  public static final String SERIALIZED_NAME_KIND = "kind";
  @SerializedName(SERIALIZED_NAME_KIND)
  private JsonPointerKind kind;

  public static final String SERIALIZED_NAME_SEGMENTS = "segments";
  @SerializedName(SERIALIZED_NAME_SEGMENTS)
  private List<PointerSegment> segments;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public JsonPointer() {
  }

  public JsonPointer(
     Boolean isUriEncoded, 
     List<PointerSegment> segments, 
     String source
  ) {
    this();
    this.isUriEncoded = isUriEncoded;
    this.segments = segments;
    this.source = source;
  }

  /**
   * Get isUriEncoded
   * @return isUriEncoded
   */
  @javax.annotation.Nullable
  public Boolean getIsUriEncoded() {
    return isUriEncoded;
  }



  public JsonPointer kind(JsonPointerKind kind) {
    this.kind = kind;
    return this;
  }

  /**
   * Get kind
   * @return kind
   */
  @javax.annotation.Nullable
  public JsonPointerKind getKind() {
    return kind;
  }

  public void setKind(JsonPointerKind kind) {
    this.kind = kind;
  }


  /**
   * Get segments
   * @return segments
   */
  @javax.annotation.Nullable
  public List<PointerSegment> getSegments() {
    return segments;
  }



  /**
   * Get source
   * @return source
   */
  @javax.annotation.Nullable
  public String getSource() {
    return source;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    JsonPointer jsonPointer = (JsonPointer) o;
    return Objects.equals(this.isUriEncoded, jsonPointer.isUriEncoded) &&
        Objects.equals(this.kind, jsonPointer.kind) &&
        Objects.equals(this.segments, jsonPointer.segments) &&
        Objects.equals(this.source, jsonPointer.source);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(isUriEncoded, kind, segments, source);
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
    sb.append("class JsonPointer {\n");
    sb.append("    isUriEncoded: ").append(toIndentedString(isUriEncoded)).append("\n");
    sb.append("    kind: ").append(toIndentedString(kind)).append("\n");
    sb.append("    segments: ").append(toIndentedString(segments)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
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
    openapiFields.add("isUriEncoded");
    openapiFields.add("kind");
    openapiFields.add("segments");
    openapiFields.add("source");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to JsonPointer
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!JsonPointer.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in JsonPointer is not found in the empty JSON string", JsonPointer.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!JsonPointer.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `JsonPointer` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `kind`
      if (jsonObj.get("kind") != null && !jsonObj.get("kind").isJsonNull()) {
        JsonPointerKind.validateJsonElement(jsonObj.get("kind"));
      }
      if (jsonObj.get("segments") != null && !jsonObj.get("segments").isJsonNull()) {
        JsonArray jsonArraysegments = jsonObj.getAsJsonArray("segments");
        if (jsonArraysegments != null) {
          // ensure the json data is an array
          if (!jsonObj.get("segments").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `segments` to be an array in the JSON string but got `%s`", jsonObj.get("segments").toString()));
          }

          // validate the optional field `segments` (array)
          for (int i = 0; i < jsonArraysegments.size(); i++) {
            PointerSegment.validateJsonElement(jsonArraysegments.get(i));
          };
        }
      }
      if ((jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) && !jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!JsonPointer.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'JsonPointer' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<JsonPointer> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(JsonPointer.class));

       return (TypeAdapter<T>) new TypeAdapter<JsonPointer>() {
           @Override
           public void write(JsonWriter out, JsonPointer value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public JsonPointer read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of JsonPointer given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of JsonPointer
   * @throws IOException if the JSON string is invalid with respect to JsonPointer
   */
  public static JsonPointer fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, JsonPointer.class);
  }

  /**
   * Convert an instance of JsonPointer to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

