/*
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
 * A request containing information for creating a Auto Provisioning Config.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AutoProvisioningConfigRequest {
  public static final String SERIALIZED_NAME_ALLOW_AUTO_PROVISIONING = "allow_auto_provisioning";
  @SerializedName(SERIALIZED_NAME_ALLOW_AUTO_PROVISIONING)
  private Boolean allowAutoProvisioning;

  public static final String SERIALIZED_NAME_APPLE_DEVELOPER_ACCOUNT_KEY = "apple_developer_account_key";
  @SerializedName(SERIALIZED_NAME_APPLE_DEVELOPER_ACCOUNT_KEY)
  private String appleDeveloperAccountKey;

  public static final String SERIALIZED_NAME_APPLE_DISTRIBUTION_CERTIFICATE_KEY = "apple_distribution_certificate_key";
  @SerializedName(SERIALIZED_NAME_APPLE_DISTRIBUTION_CERTIFICATE_KEY)
  private String appleDistributionCertificateKey;

  public AutoProvisioningConfigRequest() {
  }

  public AutoProvisioningConfigRequest allowAutoProvisioning(Boolean allowAutoProvisioning) {
    this.allowAutoProvisioning = allowAutoProvisioning;
    return this;
  }

  /**
   * When *true* enables auto provisioning
   * @return allowAutoProvisioning
   */
  @javax.annotation.Nullable
  public Boolean getAllowAutoProvisioning() {
    return allowAutoProvisioning;
  }

  public void setAllowAutoProvisioning(Boolean allowAutoProvisioning) {
    this.allowAutoProvisioning = allowAutoProvisioning;
  }


  public AutoProvisioningConfigRequest appleDeveloperAccountKey(String appleDeveloperAccountKey) {
    this.appleDeveloperAccountKey = appleDeveloperAccountKey;
    return this;
  }

  /**
   * A key to a secret in customer-credential-store. apple_developer_account refers to the user&#39;s developer account that is used to log into https://developer.apple.com. Normally the user&#39;s email.
   * @return appleDeveloperAccountKey
   */
  @javax.annotation.Nullable
  public String getAppleDeveloperAccountKey() {
    return appleDeveloperAccountKey;
  }

  public void setAppleDeveloperAccountKey(String appleDeveloperAccountKey) {
    this.appleDeveloperAccountKey = appleDeveloperAccountKey;
  }


  public AutoProvisioningConfigRequest appleDistributionCertificateKey(String appleDistributionCertificateKey) {
    this.appleDistributionCertificateKey = appleDistributionCertificateKey;
    return this;
  }

  /**
   * A key to a secret in customer-credential-store. distribution_certificate refers to the customer&#39;s certificate (that holds the private key) that will be used to sign the app.
   * @return appleDistributionCertificateKey
   */
  @javax.annotation.Nullable
  public String getAppleDistributionCertificateKey() {
    return appleDistributionCertificateKey;
  }

  public void setAppleDistributionCertificateKey(String appleDistributionCertificateKey) {
    this.appleDistributionCertificateKey = appleDistributionCertificateKey;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AutoProvisioningConfigRequest autoProvisioningConfigRequest = (AutoProvisioningConfigRequest) o;
    return Objects.equals(this.allowAutoProvisioning, autoProvisioningConfigRequest.allowAutoProvisioning) &&
        Objects.equals(this.appleDeveloperAccountKey, autoProvisioningConfigRequest.appleDeveloperAccountKey) &&
        Objects.equals(this.appleDistributionCertificateKey, autoProvisioningConfigRequest.appleDistributionCertificateKey);
  }

  @Override
  public int hashCode() {
    return Objects.hash(allowAutoProvisioning, appleDeveloperAccountKey, appleDistributionCertificateKey);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AutoProvisioningConfigRequest {\n");
    sb.append("    allowAutoProvisioning: ").append(toIndentedString(allowAutoProvisioning)).append("\n");
    sb.append("    appleDeveloperAccountKey: ").append(toIndentedString(appleDeveloperAccountKey)).append("\n");
    sb.append("    appleDistributionCertificateKey: ").append(toIndentedString(appleDistributionCertificateKey)).append("\n");
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
    openapiFields.add("allow_auto_provisioning");
    openapiFields.add("apple_developer_account_key");
    openapiFields.add("apple_distribution_certificate_key");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AutoProvisioningConfigRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AutoProvisioningConfigRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AutoProvisioningConfigRequest is not found in the empty JSON string", AutoProvisioningConfigRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AutoProvisioningConfigRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AutoProvisioningConfigRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("apple_developer_account_key") != null && !jsonObj.get("apple_developer_account_key").isJsonNull()) && !jsonObj.get("apple_developer_account_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `apple_developer_account_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("apple_developer_account_key").toString()));
      }
      if ((jsonObj.get("apple_distribution_certificate_key") != null && !jsonObj.get("apple_distribution_certificate_key").isJsonNull()) && !jsonObj.get("apple_distribution_certificate_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `apple_distribution_certificate_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("apple_distribution_certificate_key").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AutoProvisioningConfigRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AutoProvisioningConfigRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AutoProvisioningConfigRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AutoProvisioningConfigRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<AutoProvisioningConfigRequest>() {
           @Override
           public void write(JsonWriter out, AutoProvisioningConfigRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AutoProvisioningConfigRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AutoProvisioningConfigRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AutoProvisioningConfigRequest
   * @throws IOException if the JSON string is invalid with respect to AutoProvisioningConfigRequest
   */
  public static AutoProvisioningConfigRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AutoProvisioningConfigRequest.class);
  }

  /**
   * Convert an instance of AutoProvisioningConfigRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

