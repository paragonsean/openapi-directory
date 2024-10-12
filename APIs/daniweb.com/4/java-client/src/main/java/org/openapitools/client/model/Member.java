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
import java.math.BigDecimal;
import java.util.Arrays;
import org.openapitools.client.model.EndpointPostMarkdownData;
import org.openapitools.client.model.MemberIdentity;
import org.openapitools.client.model.MemberLocation;
import org.openapitools.client.model.MemberPersonal;
import org.openapitools.client.model.MemberStats;

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
 * Member
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:21.899808-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Member {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private BigDecimal id;

  public static final String SERIALIZED_NAME_IDENTITY = "identity";
  @SerializedName(SERIALIZED_NAME_IDENTITY)
  private MemberIdentity identity;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private MemberLocation location;

  public static final String SERIALIZED_NAME_PERSONAL = "personal";
  @SerializedName(SERIALIZED_NAME_PERSONAL)
  private MemberPersonal personal;

  public static final String SERIALIZED_NAME_SIGNATURE = "signature";
  @SerializedName(SERIALIZED_NAME_SIGNATURE)
  private EndpointPostMarkdownData signature;

  public static final String SERIALIZED_NAME_STATS = "stats";
  @SerializedName(SERIALIZED_NAME_STATS)
  private MemberStats stats;

  public Member() {
  }

  public Member id(BigDecimal id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public BigDecimal getId() {
    return id;
  }

  public void setId(BigDecimal id) {
    this.id = id;
  }


  public Member identity(MemberIdentity identity) {
    this.identity = identity;
    return this;
  }

  /**
   * Get identity
   * @return identity
   */
  @javax.annotation.Nullable
  public MemberIdentity getIdentity() {
    return identity;
  }

  public void setIdentity(MemberIdentity identity) {
    this.identity = identity;
  }


  public Member location(MemberLocation location) {
    this.location = location;
    return this;
  }

  /**
   * Get location
   * @return location
   */
  @javax.annotation.Nullable
  public MemberLocation getLocation() {
    return location;
  }

  public void setLocation(MemberLocation location) {
    this.location = location;
  }


  public Member personal(MemberPersonal personal) {
    this.personal = personal;
    return this;
  }

  /**
   * Get personal
   * @return personal
   */
  @javax.annotation.Nullable
  public MemberPersonal getPersonal() {
    return personal;
  }

  public void setPersonal(MemberPersonal personal) {
    this.personal = personal;
  }


  public Member signature(EndpointPostMarkdownData signature) {
    this.signature = signature;
    return this;
  }

  /**
   * Get signature
   * @return signature
   */
  @javax.annotation.Nullable
  public EndpointPostMarkdownData getSignature() {
    return signature;
  }

  public void setSignature(EndpointPostMarkdownData signature) {
    this.signature = signature;
  }


  public Member stats(MemberStats stats) {
    this.stats = stats;
    return this;
  }

  /**
   * Get stats
   * @return stats
   */
  @javax.annotation.Nullable
  public MemberStats getStats() {
    return stats;
  }

  public void setStats(MemberStats stats) {
    this.stats = stats;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Member member = (Member) o;
    return Objects.equals(this.id, member.id) &&
        Objects.equals(this.identity, member.identity) &&
        Objects.equals(this.location, member.location) &&
        Objects.equals(this.personal, member.personal) &&
        Objects.equals(this.signature, member.signature) &&
        Objects.equals(this.stats, member.stats);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, identity, location, personal, signature, stats);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Member {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    identity: ").append(toIndentedString(identity)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    personal: ").append(toIndentedString(personal)).append("\n");
    sb.append("    signature: ").append(toIndentedString(signature)).append("\n");
    sb.append("    stats: ").append(toIndentedString(stats)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("identity");
    openapiFields.add("location");
    openapiFields.add("personal");
    openapiFields.add("signature");
    openapiFields.add("stats");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Member
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Member.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Member is not found in the empty JSON string", Member.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Member.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Member` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Member.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `identity`
      if (jsonObj.get("identity") != null && !jsonObj.get("identity").isJsonNull()) {
        MemberIdentity.validateJsonElement(jsonObj.get("identity"));
      }
      // validate the optional field `location`
      if (jsonObj.get("location") != null && !jsonObj.get("location").isJsonNull()) {
        MemberLocation.validateJsonElement(jsonObj.get("location"));
      }
      // validate the optional field `personal`
      if (jsonObj.get("personal") != null && !jsonObj.get("personal").isJsonNull()) {
        MemberPersonal.validateJsonElement(jsonObj.get("personal"));
      }
      // validate the optional field `signature`
      if (jsonObj.get("signature") != null && !jsonObj.get("signature").isJsonNull()) {
        EndpointPostMarkdownData.validateJsonElement(jsonObj.get("signature"));
      }
      // validate the optional field `stats`
      if (jsonObj.get("stats") != null && !jsonObj.get("stats").isJsonNull()) {
        MemberStats.validateJsonElement(jsonObj.get("stats"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Member.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Member' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Member> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Member.class));

       return (TypeAdapter<T>) new TypeAdapter<Member>() {
           @Override
           public void write(JsonWriter out, Member value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Member read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Member given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Member
   * @throws IOException if the JSON string is invalid with respect to Member
   */
  public static Member fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Member.class);
  }

  /**
   * Convert an instance of Member to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

