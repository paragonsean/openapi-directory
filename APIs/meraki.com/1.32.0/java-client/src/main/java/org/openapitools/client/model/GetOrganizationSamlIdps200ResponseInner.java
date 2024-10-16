/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
 * GetOrganizationSamlIdps200ResponseInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetOrganizationSamlIdps200ResponseInner {
  public static final String SERIALIZED_NAME_CONSUMER_URL = "consumerUrl";
  @SerializedName(SERIALIZED_NAME_CONSUMER_URL)
  private String consumerUrl;

  public static final String SERIALIZED_NAME_IDP_ID = "idpId";
  @SerializedName(SERIALIZED_NAME_IDP_ID)
  private String idpId;

  public static final String SERIALIZED_NAME_SLO_LOGOUT_URL = "sloLogoutUrl";
  @SerializedName(SERIALIZED_NAME_SLO_LOGOUT_URL)
  private String sloLogoutUrl;

  public static final String SERIALIZED_NAME_X509CERT_SHA1_FINGERPRINT = "x509certSha1Fingerprint";
  @SerializedName(SERIALIZED_NAME_X509CERT_SHA1_FINGERPRINT)
  private String x509certSha1Fingerprint;

  public GetOrganizationSamlIdps200ResponseInner() {
  }

  public GetOrganizationSamlIdps200ResponseInner consumerUrl(String consumerUrl) {
    this.consumerUrl = consumerUrl;
    return this;
  }

  /**
   * URL that is consuming SAML Identity Provider (IdP)
   * @return consumerUrl
   */
  @javax.annotation.Nullable
  public String getConsumerUrl() {
    return consumerUrl;
  }

  public void setConsumerUrl(String consumerUrl) {
    this.consumerUrl = consumerUrl;
  }


  public GetOrganizationSamlIdps200ResponseInner idpId(String idpId) {
    this.idpId = idpId;
    return this;
  }

  /**
   * ID associated with the SAML Identity Provider (IdP)
   * @return idpId
   */
  @javax.annotation.Nullable
  public String getIdpId() {
    return idpId;
  }

  public void setIdpId(String idpId) {
    this.idpId = idpId;
  }


  public GetOrganizationSamlIdps200ResponseInner sloLogoutUrl(String sloLogoutUrl) {
    this.sloLogoutUrl = sloLogoutUrl;
    return this;
  }

  /**
   * Dashboard will redirect users to this URL when they sign out.
   * @return sloLogoutUrl
   */
  @javax.annotation.Nullable
  public String getSloLogoutUrl() {
    return sloLogoutUrl;
  }

  public void setSloLogoutUrl(String sloLogoutUrl) {
    this.sloLogoutUrl = sloLogoutUrl;
  }


  public GetOrganizationSamlIdps200ResponseInner x509certSha1Fingerprint(String x509certSha1Fingerprint) {
    this.x509certSha1Fingerprint = x509certSha1Fingerprint;
    return this;
  }

  /**
   * Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
   * @return x509certSha1Fingerprint
   */
  @javax.annotation.Nullable
  public String getX509certSha1Fingerprint() {
    return x509certSha1Fingerprint;
  }

  public void setX509certSha1Fingerprint(String x509certSha1Fingerprint) {
    this.x509certSha1Fingerprint = x509certSha1Fingerprint;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetOrganizationSamlIdps200ResponseInner getOrganizationSamlIdps200ResponseInner = (GetOrganizationSamlIdps200ResponseInner) o;
    return Objects.equals(this.consumerUrl, getOrganizationSamlIdps200ResponseInner.consumerUrl) &&
        Objects.equals(this.idpId, getOrganizationSamlIdps200ResponseInner.idpId) &&
        Objects.equals(this.sloLogoutUrl, getOrganizationSamlIdps200ResponseInner.sloLogoutUrl) &&
        Objects.equals(this.x509certSha1Fingerprint, getOrganizationSamlIdps200ResponseInner.x509certSha1Fingerprint);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consumerUrl, idpId, sloLogoutUrl, x509certSha1Fingerprint);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetOrganizationSamlIdps200ResponseInner {\n");
    sb.append("    consumerUrl: ").append(toIndentedString(consumerUrl)).append("\n");
    sb.append("    idpId: ").append(toIndentedString(idpId)).append("\n");
    sb.append("    sloLogoutUrl: ").append(toIndentedString(sloLogoutUrl)).append("\n");
    sb.append("    x509certSha1Fingerprint: ").append(toIndentedString(x509certSha1Fingerprint)).append("\n");
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
    openapiFields.add("consumerUrl");
    openapiFields.add("idpId");
    openapiFields.add("sloLogoutUrl");
    openapiFields.add("x509certSha1Fingerprint");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetOrganizationSamlIdps200ResponseInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetOrganizationSamlIdps200ResponseInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetOrganizationSamlIdps200ResponseInner is not found in the empty JSON string", GetOrganizationSamlIdps200ResponseInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetOrganizationSamlIdps200ResponseInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetOrganizationSamlIdps200ResponseInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("consumerUrl") != null && !jsonObj.get("consumerUrl").isJsonNull()) && !jsonObj.get("consumerUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consumerUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consumerUrl").toString()));
      }
      if ((jsonObj.get("idpId") != null && !jsonObj.get("idpId").isJsonNull()) && !jsonObj.get("idpId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `idpId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("idpId").toString()));
      }
      if ((jsonObj.get("sloLogoutUrl") != null && !jsonObj.get("sloLogoutUrl").isJsonNull()) && !jsonObj.get("sloLogoutUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sloLogoutUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sloLogoutUrl").toString()));
      }
      if ((jsonObj.get("x509certSha1Fingerprint") != null && !jsonObj.get("x509certSha1Fingerprint").isJsonNull()) && !jsonObj.get("x509certSha1Fingerprint").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `x509certSha1Fingerprint` to be a primitive type in the JSON string but got `%s`", jsonObj.get("x509certSha1Fingerprint").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetOrganizationSamlIdps200ResponseInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetOrganizationSamlIdps200ResponseInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetOrganizationSamlIdps200ResponseInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetOrganizationSamlIdps200ResponseInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetOrganizationSamlIdps200ResponseInner>() {
           @Override
           public void write(JsonWriter out, GetOrganizationSamlIdps200ResponseInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetOrganizationSamlIdps200ResponseInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetOrganizationSamlIdps200ResponseInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetOrganizationSamlIdps200ResponseInner
   * @throws IOException if the JSON string is invalid with respect to GetOrganizationSamlIdps200ResponseInner
   */
  public static GetOrganizationSamlIdps200ResponseInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetOrganizationSamlIdps200ResponseInner.class);
  }

  /**
   * Convert an instance of GetOrganizationSamlIdps200ResponseInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

