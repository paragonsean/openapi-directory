/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
import org.openapitools.client.model.UpdateEncryptionPasswordPolicies;
import org.openapitools.client.model.UpdateLoginPasswordPolicies;
import org.openapitools.client.model.UpdateSharesPasswordPolicies;

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
 * Request model for updating a set of password policies
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:04:27.439567-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdatePasswordPoliciesConfig {
  public static final String SERIALIZED_NAME_ENCRYPTION_PASSWORD_POLICIES = "encryptionPasswordPolicies";
  @SerializedName(SERIALIZED_NAME_ENCRYPTION_PASSWORD_POLICIES)
  private UpdateEncryptionPasswordPolicies encryptionPasswordPolicies;

  public static final String SERIALIZED_NAME_LOGIN_PASSWORD_POLICIES = "loginPasswordPolicies";
  @SerializedName(SERIALIZED_NAME_LOGIN_PASSWORD_POLICIES)
  private UpdateLoginPasswordPolicies loginPasswordPolicies;

  public static final String SERIALIZED_NAME_SHARES_PASSWORD_POLICIES = "sharesPasswordPolicies";
  @SerializedName(SERIALIZED_NAME_SHARES_PASSWORD_POLICIES)
  private UpdateSharesPasswordPolicies sharesPasswordPolicies;

  public UpdatePasswordPoliciesConfig() {
  }

  public UpdatePasswordPoliciesConfig encryptionPasswordPolicies(UpdateEncryptionPasswordPolicies encryptionPasswordPolicies) {
    this.encryptionPasswordPolicies = encryptionPasswordPolicies;
    return this;
  }

  /**
   * Get encryptionPasswordPolicies
   * @return encryptionPasswordPolicies
   */
  @javax.annotation.Nullable
  public UpdateEncryptionPasswordPolicies getEncryptionPasswordPolicies() {
    return encryptionPasswordPolicies;
  }

  public void setEncryptionPasswordPolicies(UpdateEncryptionPasswordPolicies encryptionPasswordPolicies) {
    this.encryptionPasswordPolicies = encryptionPasswordPolicies;
  }


  public UpdatePasswordPoliciesConfig loginPasswordPolicies(UpdateLoginPasswordPolicies loginPasswordPolicies) {
    this.loginPasswordPolicies = loginPasswordPolicies;
    return this;
  }

  /**
   * Get loginPasswordPolicies
   * @return loginPasswordPolicies
   */
  @javax.annotation.Nullable
  public UpdateLoginPasswordPolicies getLoginPasswordPolicies() {
    return loginPasswordPolicies;
  }

  public void setLoginPasswordPolicies(UpdateLoginPasswordPolicies loginPasswordPolicies) {
    this.loginPasswordPolicies = loginPasswordPolicies;
  }


  public UpdatePasswordPoliciesConfig sharesPasswordPolicies(UpdateSharesPasswordPolicies sharesPasswordPolicies) {
    this.sharesPasswordPolicies = sharesPasswordPolicies;
    return this;
  }

  /**
   * Get sharesPasswordPolicies
   * @return sharesPasswordPolicies
   */
  @javax.annotation.Nullable
  public UpdateSharesPasswordPolicies getSharesPasswordPolicies() {
    return sharesPasswordPolicies;
  }

  public void setSharesPasswordPolicies(UpdateSharesPasswordPolicies sharesPasswordPolicies) {
    this.sharesPasswordPolicies = sharesPasswordPolicies;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdatePasswordPoliciesConfig updatePasswordPoliciesConfig = (UpdatePasswordPoliciesConfig) o;
    return Objects.equals(this.encryptionPasswordPolicies, updatePasswordPoliciesConfig.encryptionPasswordPolicies) &&
        Objects.equals(this.loginPasswordPolicies, updatePasswordPoliciesConfig.loginPasswordPolicies) &&
        Objects.equals(this.sharesPasswordPolicies, updatePasswordPoliciesConfig.sharesPasswordPolicies);
  }

  @Override
  public int hashCode() {
    return Objects.hash(encryptionPasswordPolicies, loginPasswordPolicies, sharesPasswordPolicies);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdatePasswordPoliciesConfig {\n");
    sb.append("    encryptionPasswordPolicies: ").append(toIndentedString(encryptionPasswordPolicies)).append("\n");
    sb.append("    loginPasswordPolicies: ").append(toIndentedString(loginPasswordPolicies)).append("\n");
    sb.append("    sharesPasswordPolicies: ").append(toIndentedString(sharesPasswordPolicies)).append("\n");
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
    openapiFields.add("encryptionPasswordPolicies");
    openapiFields.add("loginPasswordPolicies");
    openapiFields.add("sharesPasswordPolicies");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdatePasswordPoliciesConfig
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdatePasswordPoliciesConfig.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdatePasswordPoliciesConfig is not found in the empty JSON string", UpdatePasswordPoliciesConfig.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdatePasswordPoliciesConfig.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdatePasswordPoliciesConfig` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `encryptionPasswordPolicies`
      if (jsonObj.get("encryptionPasswordPolicies") != null && !jsonObj.get("encryptionPasswordPolicies").isJsonNull()) {
        UpdateEncryptionPasswordPolicies.validateJsonElement(jsonObj.get("encryptionPasswordPolicies"));
      }
      // validate the optional field `loginPasswordPolicies`
      if (jsonObj.get("loginPasswordPolicies") != null && !jsonObj.get("loginPasswordPolicies").isJsonNull()) {
        UpdateLoginPasswordPolicies.validateJsonElement(jsonObj.get("loginPasswordPolicies"));
      }
      // validate the optional field `sharesPasswordPolicies`
      if (jsonObj.get("sharesPasswordPolicies") != null && !jsonObj.get("sharesPasswordPolicies").isJsonNull()) {
        UpdateSharesPasswordPolicies.validateJsonElement(jsonObj.get("sharesPasswordPolicies"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdatePasswordPoliciesConfig.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdatePasswordPoliciesConfig' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdatePasswordPoliciesConfig> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdatePasswordPoliciesConfig.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdatePasswordPoliciesConfig>() {
           @Override
           public void write(JsonWriter out, UpdatePasswordPoliciesConfig value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdatePasswordPoliciesConfig read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdatePasswordPoliciesConfig given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdatePasswordPoliciesConfig
   * @throws IOException if the JSON string is invalid with respect to UpdatePasswordPoliciesConfig
   */
  public static UpdatePasswordPoliciesConfig fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdatePasswordPoliciesConfig.class);
  }

  /**
   * Convert an instance of UpdatePasswordPoliciesConfig to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

