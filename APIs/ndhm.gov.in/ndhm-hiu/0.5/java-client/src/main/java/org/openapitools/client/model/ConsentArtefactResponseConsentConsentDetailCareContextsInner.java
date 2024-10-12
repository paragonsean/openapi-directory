/*
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
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
 * ConsentArtefactResponseConsentConsentDetailCareContextsInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:36.866529-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ConsentArtefactResponseConsentConsentDetailCareContextsInner {
  public static final String SERIALIZED_NAME_CARE_CONTEXT_REFERENCE = "careContextReference";
  @SerializedName(SERIALIZED_NAME_CARE_CONTEXT_REFERENCE)
  private String careContextReference;

  public static final String SERIALIZED_NAME_PATIENT_REFERENCE = "patientReference";
  @SerializedName(SERIALIZED_NAME_PATIENT_REFERENCE)
  private String patientReference;

  public ConsentArtefactResponseConsentConsentDetailCareContextsInner() {
  }

  public ConsentArtefactResponseConsentConsentDetailCareContextsInner careContextReference(String careContextReference) {
    this.careContextReference = careContextReference;
    return this;
  }

  /**
   * Get careContextReference
   * @return careContextReference
   */
  @javax.annotation.Nonnull
  public String getCareContextReference() {
    return careContextReference;
  }

  public void setCareContextReference(String careContextReference) {
    this.careContextReference = careContextReference;
  }


  public ConsentArtefactResponseConsentConsentDetailCareContextsInner patientReference(String patientReference) {
    this.patientReference = patientReference;
    return this;
  }

  /**
   * Get patientReference
   * @return patientReference
   */
  @javax.annotation.Nonnull
  public String getPatientReference() {
    return patientReference;
  }

  public void setPatientReference(String patientReference) {
    this.patientReference = patientReference;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ConsentArtefactResponseConsentConsentDetailCareContextsInner consentArtefactResponseConsentConsentDetailCareContextsInner = (ConsentArtefactResponseConsentConsentDetailCareContextsInner) o;
    return Objects.equals(this.careContextReference, consentArtefactResponseConsentConsentDetailCareContextsInner.careContextReference) &&
        Objects.equals(this.patientReference, consentArtefactResponseConsentConsentDetailCareContextsInner.patientReference);
  }

  @Override
  public int hashCode() {
    return Objects.hash(careContextReference, patientReference);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ConsentArtefactResponseConsentConsentDetailCareContextsInner {\n");
    sb.append("    careContextReference: ").append(toIndentedString(careContextReference)).append("\n");
    sb.append("    patientReference: ").append(toIndentedString(patientReference)).append("\n");
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
    openapiFields.add("careContextReference");
    openapiFields.add("patientReference");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("careContextReference");
    openapiRequiredFields.add("patientReference");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ConsentArtefactResponseConsentConsentDetailCareContextsInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ConsentArtefactResponseConsentConsentDetailCareContextsInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ConsentArtefactResponseConsentConsentDetailCareContextsInner is not found in the empty JSON string", ConsentArtefactResponseConsentConsentDetailCareContextsInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ConsentArtefactResponseConsentConsentDetailCareContextsInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ConsentArtefactResponseConsentConsentDetailCareContextsInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ConsentArtefactResponseConsentConsentDetailCareContextsInner.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("careContextReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `careContextReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("careContextReference").toString()));
      }
      if (!jsonObj.get("patientReference").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `patientReference` to be a primitive type in the JSON string but got `%s`", jsonObj.get("patientReference").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ConsentArtefactResponseConsentConsentDetailCareContextsInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ConsentArtefactResponseConsentConsentDetailCareContextsInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ConsentArtefactResponseConsentConsentDetailCareContextsInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ConsentArtefactResponseConsentConsentDetailCareContextsInner.class));

       return (TypeAdapter<T>) new TypeAdapter<ConsentArtefactResponseConsentConsentDetailCareContextsInner>() {
           @Override
           public void write(JsonWriter out, ConsentArtefactResponseConsentConsentDetailCareContextsInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ConsentArtefactResponseConsentConsentDetailCareContextsInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ConsentArtefactResponseConsentConsentDetailCareContextsInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ConsentArtefactResponseConsentConsentDetailCareContextsInner
   * @throws IOException if the JSON string is invalid with respect to ConsentArtefactResponseConsentConsentDetailCareContextsInner
   */
  public static ConsentArtefactResponseConsentConsentDetailCareContextsInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ConsentArtefactResponseConsentConsentDetailCareContextsInner.class);
  }

  /**
   * Convert an instance of ConsentArtefactResponseConsentConsentDetailCareContextsInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

