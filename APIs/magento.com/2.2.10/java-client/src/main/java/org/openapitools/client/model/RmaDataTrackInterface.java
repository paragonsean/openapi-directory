/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
 * Interface TrackInterface
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RmaDataTrackInterface {
  public static final String SERIALIZED_NAME_CARRIER_CODE = "carrier_code";
  @SerializedName(SERIALIZED_NAME_CARRIER_CODE)
  private String carrierCode;

  public static final String SERIALIZED_NAME_CARRIER_TITLE = "carrier_title";
  @SerializedName(SERIALIZED_NAME_CARRIER_TITLE)
  private String carrierTitle;

  public static final String SERIALIZED_NAME_ENTITY_ID = "entity_id";
  @SerializedName(SERIALIZED_NAME_ENTITY_ID)
  private Integer entityId;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private Object extensionAttributes;

  public static final String SERIALIZED_NAME_RMA_ENTITY_ID = "rma_entity_id";
  @SerializedName(SERIALIZED_NAME_RMA_ENTITY_ID)
  private Integer rmaEntityId;

  public static final String SERIALIZED_NAME_TRACK_NUMBER = "track_number";
  @SerializedName(SERIALIZED_NAME_TRACK_NUMBER)
  private String trackNumber;

  public RmaDataTrackInterface() {
  }

  public RmaDataTrackInterface carrierCode(String carrierCode) {
    this.carrierCode = carrierCode;
    return this;
  }

  /**
   * Carrier code
   * @return carrierCode
   */
  @javax.annotation.Nonnull
  public String getCarrierCode() {
    return carrierCode;
  }

  public void setCarrierCode(String carrierCode) {
    this.carrierCode = carrierCode;
  }


  public RmaDataTrackInterface carrierTitle(String carrierTitle) {
    this.carrierTitle = carrierTitle;
    return this;
  }

  /**
   * Carrier title
   * @return carrierTitle
   */
  @javax.annotation.Nonnull
  public String getCarrierTitle() {
    return carrierTitle;
  }

  public void setCarrierTitle(String carrierTitle) {
    this.carrierTitle = carrierTitle;
  }


  public RmaDataTrackInterface entityId(Integer entityId) {
    this.entityId = entityId;
    return this;
  }

  /**
   * Entity id
   * @return entityId
   */
  @javax.annotation.Nonnull
  public Integer getEntityId() {
    return entityId;
  }

  public void setEntityId(Integer entityId) {
    this.entityId = entityId;
  }


  public RmaDataTrackInterface extensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * ExtensionInterface class for @see \\Magento\\Rma\\Api\\Data\\TrackInterface
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public Object getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public RmaDataTrackInterface rmaEntityId(Integer rmaEntityId) {
    this.rmaEntityId = rmaEntityId;
    return this;
  }

  /**
   * Rma entity id
   * @return rmaEntityId
   */
  @javax.annotation.Nonnull
  public Integer getRmaEntityId() {
    return rmaEntityId;
  }

  public void setRmaEntityId(Integer rmaEntityId) {
    this.rmaEntityId = rmaEntityId;
  }


  public RmaDataTrackInterface trackNumber(String trackNumber) {
    this.trackNumber = trackNumber;
    return this;
  }

  /**
   * Track number
   * @return trackNumber
   */
  @javax.annotation.Nonnull
  public String getTrackNumber() {
    return trackNumber;
  }

  public void setTrackNumber(String trackNumber) {
    this.trackNumber = trackNumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RmaDataTrackInterface rmaDataTrackInterface = (RmaDataTrackInterface) o;
    return Objects.equals(this.carrierCode, rmaDataTrackInterface.carrierCode) &&
        Objects.equals(this.carrierTitle, rmaDataTrackInterface.carrierTitle) &&
        Objects.equals(this.entityId, rmaDataTrackInterface.entityId) &&
        Objects.equals(this.extensionAttributes, rmaDataTrackInterface.extensionAttributes) &&
        Objects.equals(this.rmaEntityId, rmaDataTrackInterface.rmaEntityId) &&
        Objects.equals(this.trackNumber, rmaDataTrackInterface.trackNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(carrierCode, carrierTitle, entityId, extensionAttributes, rmaEntityId, trackNumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RmaDataTrackInterface {\n");
    sb.append("    carrierCode: ").append(toIndentedString(carrierCode)).append("\n");
    sb.append("    carrierTitle: ").append(toIndentedString(carrierTitle)).append("\n");
    sb.append("    entityId: ").append(toIndentedString(entityId)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    rmaEntityId: ").append(toIndentedString(rmaEntityId)).append("\n");
    sb.append("    trackNumber: ").append(toIndentedString(trackNumber)).append("\n");
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
    openapiFields.add("carrier_code");
    openapiFields.add("carrier_title");
    openapiFields.add("entity_id");
    openapiFields.add("extension_attributes");
    openapiFields.add("rma_entity_id");
    openapiFields.add("track_number");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("carrier_code");
    openapiRequiredFields.add("carrier_title");
    openapiRequiredFields.add("entity_id");
    openapiRequiredFields.add("rma_entity_id");
    openapiRequiredFields.add("track_number");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RmaDataTrackInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RmaDataTrackInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RmaDataTrackInterface is not found in the empty JSON string", RmaDataTrackInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RmaDataTrackInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RmaDataTrackInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : RmaDataTrackInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("carrier_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrier_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrier_code").toString()));
      }
      if (!jsonObj.get("carrier_title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrier_title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrier_title").toString()));
      }
      if (!jsonObj.get("track_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_number").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RmaDataTrackInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RmaDataTrackInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RmaDataTrackInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RmaDataTrackInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<RmaDataTrackInterface>() {
           @Override
           public void write(JsonWriter out, RmaDataTrackInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RmaDataTrackInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RmaDataTrackInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RmaDataTrackInterface
   * @throws IOException if the JSON string is invalid with respect to RmaDataTrackInterface
   */
  public static RmaDataTrackInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RmaDataTrackInterface.class);
  }

  /**
   * Convert an instance of RmaDataTrackInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

