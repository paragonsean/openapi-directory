/*
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
import org.openapitools.client.model.EndpointPostAudiencesIDMembershipsDataAudience;
import org.openapitools.client.model.User;

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
 * EndpointPostAudiencesIDMembershipsData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:21.899808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EndpointPostAudiencesIDMembershipsData {
  public static final String SERIALIZED_NAME_AUDIENCE = "audience";
  @SerializedName(SERIALIZED_NAME_AUDIENCE)
  private EndpointPostAudiencesIDMembershipsDataAudience audience;

  public static final String SERIALIZED_NAME_MEMBER = "member";
  @SerializedName(SERIALIZED_NAME_MEMBER)
  private User member;

  public EndpointPostAudiencesIDMembershipsData() {
  }

  public EndpointPostAudiencesIDMembershipsData audience(EndpointPostAudiencesIDMembershipsDataAudience audience) {
    this.audience = audience;
    return this;
  }

  /**
   * Get audience
   * @return audience
   */
  @javax.annotation.Nullable
  public EndpointPostAudiencesIDMembershipsDataAudience getAudience() {
    return audience;
  }

  public void setAudience(EndpointPostAudiencesIDMembershipsDataAudience audience) {
    this.audience = audience;
  }


  public EndpointPostAudiencesIDMembershipsData member(User member) {
    this.member = member;
    return this;
  }

  /**
   * Get member
   * @return member
   */
  @javax.annotation.Nullable
  public User getMember() {
    return member;
  }

  public void setMember(User member) {
    this.member = member;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EndpointPostAudiencesIDMembershipsData endpointPostAudiencesIDMembershipsData = (EndpointPostAudiencesIDMembershipsData) o;
    return Objects.equals(this.audience, endpointPostAudiencesIDMembershipsData.audience) &&
        Objects.equals(this.member, endpointPostAudiencesIDMembershipsData.member);
  }

  @Override
  public int hashCode() {
    return Objects.hash(audience, member);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EndpointPostAudiencesIDMembershipsData {\n");
    sb.append("    audience: ").append(toIndentedString(audience)).append("\n");
    sb.append("    member: ").append(toIndentedString(member)).append("\n");
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
    openapiFields.add("audience");
    openapiFields.add("member");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EndpointPostAudiencesIDMembershipsData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EndpointPostAudiencesIDMembershipsData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EndpointPostAudiencesIDMembershipsData is not found in the empty JSON string", EndpointPostAudiencesIDMembershipsData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EndpointPostAudiencesIDMembershipsData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EndpointPostAudiencesIDMembershipsData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `audience`
      if (jsonObj.get("audience") != null && !jsonObj.get("audience").isJsonNull()) {
        EndpointPostAudiencesIDMembershipsDataAudience.validateJsonElement(jsonObj.get("audience"));
      }
      // validate the optional field `member`
      if (jsonObj.get("member") != null && !jsonObj.get("member").isJsonNull()) {
        User.validateJsonElement(jsonObj.get("member"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EndpointPostAudiencesIDMembershipsData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EndpointPostAudiencesIDMembershipsData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EndpointPostAudiencesIDMembershipsData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EndpointPostAudiencesIDMembershipsData.class));

       return (TypeAdapter<T>) new TypeAdapter<EndpointPostAudiencesIDMembershipsData>() {
           @Override
           public void write(JsonWriter out, EndpointPostAudiencesIDMembershipsData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EndpointPostAudiencesIDMembershipsData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EndpointPostAudiencesIDMembershipsData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EndpointPostAudiencesIDMembershipsData
   * @throws IOException if the JSON string is invalid with respect to EndpointPostAudiencesIDMembershipsData
   */
  public static EndpointPostAudiencesIDMembershipsData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EndpointPostAudiencesIDMembershipsData.class);
  }

  /**
   * Convert an instance of EndpointPostAudiencesIDMembershipsData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

