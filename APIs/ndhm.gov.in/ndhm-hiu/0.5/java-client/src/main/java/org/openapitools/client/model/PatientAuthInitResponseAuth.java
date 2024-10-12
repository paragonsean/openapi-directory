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
import org.openapitools.client.model.AuthMeta;
import org.openapitools.client.model.AuthenticationMode;

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
 * PatientAuthInitResponseAuth
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:36.866529-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PatientAuthInitResponseAuth {
  public static final String SERIALIZED_NAME_META = "meta";
  @SerializedName(SERIALIZED_NAME_META)
  private AuthMeta meta;

  public static final String SERIALIZED_NAME_MODE = "mode";
  @SerializedName(SERIALIZED_NAME_MODE)
  private AuthenticationMode mode;

  public static final String SERIALIZED_NAME_TRANSACTION_ID = "transactionId";
  @SerializedName(SERIALIZED_NAME_TRANSACTION_ID)
  private String transactionId;

  public PatientAuthInitResponseAuth() {
  }

  public PatientAuthInitResponseAuth meta(AuthMeta meta) {
    this.meta = meta;
    return this;
  }

  /**
   * Get meta
   * @return meta
   */
  @javax.annotation.Nullable
  public AuthMeta getMeta() {
    return meta;
  }

  public void setMeta(AuthMeta meta) {
    this.meta = meta;
  }


  public PatientAuthInitResponseAuth mode(AuthenticationMode mode) {
    this.mode = mode;
    return this;
  }

  /**
   * Get mode
   * @return mode
   */
  @javax.annotation.Nonnull
  public AuthenticationMode getMode() {
    return mode;
  }

  public void setMode(AuthenticationMode mode) {
    this.mode = mode;
  }


  public PatientAuthInitResponseAuth transactionId(String transactionId) {
    this.transactionId = transactionId;
    return this;
  }

  /**
   * Get transactionId
   * @return transactionId
   */
  @javax.annotation.Nonnull
  public String getTransactionId() {
    return transactionId;
  }

  public void setTransactionId(String transactionId) {
    this.transactionId = transactionId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PatientAuthInitResponseAuth patientAuthInitResponseAuth = (PatientAuthInitResponseAuth) o;
    return Objects.equals(this.meta, patientAuthInitResponseAuth.meta) &&
        Objects.equals(this.mode, patientAuthInitResponseAuth.mode) &&
        Objects.equals(this.transactionId, patientAuthInitResponseAuth.transactionId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(meta, mode, transactionId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PatientAuthInitResponseAuth {\n");
    sb.append("    meta: ").append(toIndentedString(meta)).append("\n");
    sb.append("    mode: ").append(toIndentedString(mode)).append("\n");
    sb.append("    transactionId: ").append(toIndentedString(transactionId)).append("\n");
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
    openapiFields.add("meta");
    openapiFields.add("mode");
    openapiFields.add("transactionId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("mode");
    openapiRequiredFields.add("transactionId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PatientAuthInitResponseAuth
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PatientAuthInitResponseAuth.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PatientAuthInitResponseAuth is not found in the empty JSON string", PatientAuthInitResponseAuth.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PatientAuthInitResponseAuth.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PatientAuthInitResponseAuth` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PatientAuthInitResponseAuth.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `meta`
      if (jsonObj.get("meta") != null && !jsonObj.get("meta").isJsonNull()) {
        AuthMeta.validateJsonElement(jsonObj.get("meta"));
      }
      // validate the required field `mode`
      AuthenticationMode.validateJsonElement(jsonObj.get("mode"));
      if (!jsonObj.get("transactionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `transactionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("transactionId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PatientAuthInitResponseAuth.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PatientAuthInitResponseAuth' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PatientAuthInitResponseAuth> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PatientAuthInitResponseAuth.class));

       return (TypeAdapter<T>) new TypeAdapter<PatientAuthInitResponseAuth>() {
           @Override
           public void write(JsonWriter out, PatientAuthInitResponseAuth value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PatientAuthInitResponseAuth read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PatientAuthInitResponseAuth given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PatientAuthInitResponseAuth
   * @throws IOException if the JSON string is invalid with respect to PatientAuthInitResponseAuth
   */
  public static PatientAuthInitResponseAuth fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PatientAuthInitResponseAuth.class);
  }

  /**
   * Convert an instance of PatientAuthInitResponseAuth to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

