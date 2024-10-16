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
 * org settings response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrgComplianceSettingsResponse {
  public static final String SERIALIZED_NAME_CERTIFICATE_CONNECTION_ID = "certificate_connection_id";
  @SerializedName(SERIALIZED_NAME_CERTIFICATE_CONNECTION_ID)
  private String certificateConnectionId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_MAM_ENABLED = "is_mam_enabled";
  @SerializedName(SERIALIZED_NAME_IS_MAM_ENABLED)
  private Boolean isMamEnabled;

  public static final String SERIALIZED_NAME_ORG_ID = "org_id";
  @SerializedName(SERIALIZED_NAME_ORG_ID)
  private String orgId;

  public OrgComplianceSettingsResponse() {
  }

  public OrgComplianceSettingsResponse certificateConnectionId(String certificateConnectionId) {
    this.certificateConnectionId = certificateConnectionId;
    return this;
  }

  /**
   * certificate connection id to wrap and resign the app after wrapping
   * @return certificateConnectionId
   */
  @javax.annotation.Nonnull
  public String getCertificateConnectionId() {
    return certificateConnectionId;
  }

  public void setCertificateConnectionId(String certificateConnectionId) {
    this.certificateConnectionId = certificateConnectionId;
  }


  public OrgComplianceSettingsResponse id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The internal unique id (UUID) of the organization compliance setting
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public OrgComplianceSettingsResponse isMamEnabled(Boolean isMamEnabled) {
    this.isMamEnabled = isMamEnabled;
    return this;
  }

  /**
   * flag to tell if mam warpping is enabled on the Org
   * @return isMamEnabled
   */
  @javax.annotation.Nullable
  public Boolean getIsMamEnabled() {
    return isMamEnabled;
  }

  public void setIsMamEnabled(Boolean isMamEnabled) {
    this.isMamEnabled = isMamEnabled;
  }


  public OrgComplianceSettingsResponse orgId(String orgId) {
    this.orgId = orgId;
    return this;
  }

  /**
   * The internal unique id (UUID) of the organization.
   * @return orgId
   */
  @javax.annotation.Nonnull
  public String getOrgId() {
    return orgId;
  }

  public void setOrgId(String orgId) {
    this.orgId = orgId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrgComplianceSettingsResponse orgComplianceSettingsResponse = (OrgComplianceSettingsResponse) o;
    return Objects.equals(this.certificateConnectionId, orgComplianceSettingsResponse.certificateConnectionId) &&
        Objects.equals(this.id, orgComplianceSettingsResponse.id) &&
        Objects.equals(this.isMamEnabled, orgComplianceSettingsResponse.isMamEnabled) &&
        Objects.equals(this.orgId, orgComplianceSettingsResponse.orgId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(certificateConnectionId, id, isMamEnabled, orgId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrgComplianceSettingsResponse {\n");
    sb.append("    certificateConnectionId: ").append(toIndentedString(certificateConnectionId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isMamEnabled: ").append(toIndentedString(isMamEnabled)).append("\n");
    sb.append("    orgId: ").append(toIndentedString(orgId)).append("\n");
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
    openapiFields.add("certificate_connection_id");
    openapiFields.add("id");
    openapiFields.add("is_mam_enabled");
    openapiFields.add("org_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("certificate_connection_id");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("org_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrgComplianceSettingsResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrgComplianceSettingsResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrgComplianceSettingsResponse is not found in the empty JSON string", OrgComplianceSettingsResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrgComplianceSettingsResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrgComplianceSettingsResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : OrgComplianceSettingsResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("certificate_connection_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `certificate_connection_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("certificate_connection_id").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if (!jsonObj.get("org_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `org_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("org_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrgComplianceSettingsResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrgComplianceSettingsResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrgComplianceSettingsResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrgComplianceSettingsResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<OrgComplianceSettingsResponse>() {
           @Override
           public void write(JsonWriter out, OrgComplianceSettingsResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrgComplianceSettingsResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrgComplianceSettingsResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrgComplianceSettingsResponse
   * @throws IOException if the JSON string is invalid with respect to OrgComplianceSettingsResponse
   */
  public static OrgComplianceSettingsResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrgComplianceSettingsResponse.class);
  }

  /**
   * Convert an instance of OrgComplianceSettingsResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

