/*
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
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
 * HidBenefitDelinkRequestPayload
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:34.465238-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class HidBenefitDelinkRequestPayload {
  public static final String SERIALIZED_NAME_BENEFIT_NAME = "benefitName";
  @SerializedName(SERIALIZED_NAME_BENEFIT_NAME)
  private String benefitName;

  public static final String SERIALIZED_NAME_UID_TOKEN = "uidToken";
  @SerializedName(SERIALIZED_NAME_UID_TOKEN)
  private String uidToken;

  public HidBenefitDelinkRequestPayload() {
  }

  public HidBenefitDelinkRequestPayload benefitName(String benefitName) {
    this.benefitName = benefitName;
    return this;
  }

  /**
   * Get benefitName
   * @return benefitName
   */
  @javax.annotation.Nullable
  public String getBenefitName() {
    return benefitName;
  }

  public void setBenefitName(String benefitName) {
    this.benefitName = benefitName;
  }


  public HidBenefitDelinkRequestPayload uidToken(String uidToken) {
    this.uidToken = uidToken;
    return this;
  }

  /**
   * Get uidToken
   * @return uidToken
   */
  @javax.annotation.Nullable
  public String getUidToken() {
    return uidToken;
  }

  public void setUidToken(String uidToken) {
    this.uidToken = uidToken;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    HidBenefitDelinkRequestPayload hidBenefitDelinkRequestPayload = (HidBenefitDelinkRequestPayload) o;
    return Objects.equals(this.benefitName, hidBenefitDelinkRequestPayload.benefitName) &&
        Objects.equals(this.uidToken, hidBenefitDelinkRequestPayload.uidToken);
  }

  @Override
  public int hashCode() {
    return Objects.hash(benefitName, uidToken);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class HidBenefitDelinkRequestPayload {\n");
    sb.append("    benefitName: ").append(toIndentedString(benefitName)).append("\n");
    sb.append("    uidToken: ").append(toIndentedString(uidToken)).append("\n");
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
    openapiFields.add("benefitName");
    openapiFields.add("uidToken");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to HidBenefitDelinkRequestPayload
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!HidBenefitDelinkRequestPayload.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in HidBenefitDelinkRequestPayload is not found in the empty JSON string", HidBenefitDelinkRequestPayload.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!HidBenefitDelinkRequestPayload.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `HidBenefitDelinkRequestPayload` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("benefitName") != null && !jsonObj.get("benefitName").isJsonNull()) && !jsonObj.get("benefitName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `benefitName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("benefitName").toString()));
      }
      if ((jsonObj.get("uidToken") != null && !jsonObj.get("uidToken").isJsonNull()) && !jsonObj.get("uidToken").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uidToken` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uidToken").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!HidBenefitDelinkRequestPayload.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'HidBenefitDelinkRequestPayload' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<HidBenefitDelinkRequestPayload> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(HidBenefitDelinkRequestPayload.class));

       return (TypeAdapter<T>) new TypeAdapter<HidBenefitDelinkRequestPayload>() {
           @Override
           public void write(JsonWriter out, HidBenefitDelinkRequestPayload value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public HidBenefitDelinkRequestPayload read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of HidBenefitDelinkRequestPayload given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of HidBenefitDelinkRequestPayload
   * @throws IOException if the JSON string is invalid with respect to HidBenefitDelinkRequestPayload
   */
  public static HidBenefitDelinkRequestPayload fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, HidBenefitDelinkRequestPayload.class);
  }

  /**
   * Convert an instance of HidBenefitDelinkRequestPayload to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

