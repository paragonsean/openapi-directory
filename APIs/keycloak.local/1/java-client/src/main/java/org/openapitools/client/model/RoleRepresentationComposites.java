/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
 * RoleRepresentationComposites
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.227825-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RoleRepresentationComposites {
  public static final String SERIALIZED_NAME_CLIENT = "client";
  @SerializedName(SERIALIZED_NAME_CLIENT)
  private Map<String, Object> client = new HashMap<>();

  public static final String SERIALIZED_NAME_REALM = "realm";
  @SerializedName(SERIALIZED_NAME_REALM)
  private List<String> realm = new ArrayList<>();

  public RoleRepresentationComposites() {
  }

  public RoleRepresentationComposites client(Map<String, Object> client) {
    this.client = client;
    return this;
  }

  public RoleRepresentationComposites putClientItem(String key, Object clientItem) {
    if (this.client == null) {
      this.client = new HashMap<>();
    }
    this.client.put(key, clientItem);
    return this;
  }

  /**
   * Get client
   * @return client
   */
  @javax.annotation.Nullable
  public Map<String, Object> getClient() {
    return client;
  }

  public void setClient(Map<String, Object> client) {
    this.client = client;
  }


  public RoleRepresentationComposites realm(List<String> realm) {
    this.realm = realm;
    return this;
  }

  public RoleRepresentationComposites addRealmItem(String realmItem) {
    if (this.realm == null) {
      this.realm = new ArrayList<>();
    }
    this.realm.add(realmItem);
    return this;
  }

  /**
   * Get realm
   * @return realm
   */
  @javax.annotation.Nullable
  public List<String> getRealm() {
    return realm;
  }

  public void setRealm(List<String> realm) {
    this.realm = realm;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RoleRepresentationComposites roleRepresentationComposites = (RoleRepresentationComposites) o;
    return Objects.equals(this.client, roleRepresentationComposites.client) &&
        Objects.equals(this.realm, roleRepresentationComposites.realm);
  }

  @Override
  public int hashCode() {
    return Objects.hash(client, realm);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RoleRepresentationComposites {\n");
    sb.append("    client: ").append(toIndentedString(client)).append("\n");
    sb.append("    realm: ").append(toIndentedString(realm)).append("\n");
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
    openapiFields.add("client");
    openapiFields.add("realm");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RoleRepresentationComposites
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RoleRepresentationComposites.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RoleRepresentationComposites is not found in the empty JSON string", RoleRepresentationComposites.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RoleRepresentationComposites.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RoleRepresentationComposites` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("realm") != null && !jsonObj.get("realm").isJsonNull() && !jsonObj.get("realm").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `realm` to be an array in the JSON string but got `%s`", jsonObj.get("realm").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RoleRepresentationComposites.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RoleRepresentationComposites' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RoleRepresentationComposites> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RoleRepresentationComposites.class));

       return (TypeAdapter<T>) new TypeAdapter<RoleRepresentationComposites>() {
           @Override
           public void write(JsonWriter out, RoleRepresentationComposites value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RoleRepresentationComposites read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RoleRepresentationComposites given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RoleRepresentationComposites
   * @throws IOException if the JSON string is invalid with respect to RoleRepresentationComposites
   */
  public static RoleRepresentationComposites fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RoleRepresentationComposites.class);
  }

  /**
   * Convert an instance of RoleRepresentationComposites to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

