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
 * Shipment Track Creation interface.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SalesDataShipmentTrackCreationInterface {
  public static final String SERIALIZED_NAME_CARRIER_CODE = "carrier_code";
  @SerializedName(SERIALIZED_NAME_CARRIER_CODE)
  private String carrierCode;

  public static final String SERIALIZED_NAME_EXTENSION_ATTRIBUTES = "extension_attributes";
  @SerializedName(SERIALIZED_NAME_EXTENSION_ATTRIBUTES)
  private Object extensionAttributes;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TRACK_NUMBER = "track_number";
  @SerializedName(SERIALIZED_NAME_TRACK_NUMBER)
  private String trackNumber;

  public SalesDataShipmentTrackCreationInterface() {
  }

  public SalesDataShipmentTrackCreationInterface carrierCode(String carrierCode) {
    this.carrierCode = carrierCode;
    return this;
  }

  /**
   * Carrier code.
   * @return carrierCode
   */
  @javax.annotation.Nonnull
  public String getCarrierCode() {
    return carrierCode;
  }

  public void setCarrierCode(String carrierCode) {
    this.carrierCode = carrierCode;
  }


  public SalesDataShipmentTrackCreationInterface extensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
    return this;
  }

  /**
   * ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\ShipmentTrackCreationInterface
   * @return extensionAttributes
   */
  @javax.annotation.Nullable
  public Object getExtensionAttributes() {
    return extensionAttributes;
  }

  public void setExtensionAttributes(Object extensionAttributes) {
    this.extensionAttributes = extensionAttributes;
  }


  public SalesDataShipmentTrackCreationInterface title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Title.
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public SalesDataShipmentTrackCreationInterface trackNumber(String trackNumber) {
    this.trackNumber = trackNumber;
    return this;
  }

  /**
   * Track number.
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
    SalesDataShipmentTrackCreationInterface salesDataShipmentTrackCreationInterface = (SalesDataShipmentTrackCreationInterface) o;
    return Objects.equals(this.carrierCode, salesDataShipmentTrackCreationInterface.carrierCode) &&
        Objects.equals(this.extensionAttributes, salesDataShipmentTrackCreationInterface.extensionAttributes) &&
        Objects.equals(this.title, salesDataShipmentTrackCreationInterface.title) &&
        Objects.equals(this.trackNumber, salesDataShipmentTrackCreationInterface.trackNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(carrierCode, extensionAttributes, title, trackNumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SalesDataShipmentTrackCreationInterface {\n");
    sb.append("    carrierCode: ").append(toIndentedString(carrierCode)).append("\n");
    sb.append("    extensionAttributes: ").append(toIndentedString(extensionAttributes)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("extension_attributes");
    openapiFields.add("title");
    openapiFields.add("track_number");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("carrier_code");
    openapiRequiredFields.add("title");
    openapiRequiredFields.add("track_number");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SalesDataShipmentTrackCreationInterface
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SalesDataShipmentTrackCreationInterface.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SalesDataShipmentTrackCreationInterface is not found in the empty JSON string", SalesDataShipmentTrackCreationInterface.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SalesDataShipmentTrackCreationInterface.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SalesDataShipmentTrackCreationInterface` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SalesDataShipmentTrackCreationInterface.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("carrier_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `carrier_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("carrier_code").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if (!jsonObj.get("track_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `track_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("track_number").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SalesDataShipmentTrackCreationInterface.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SalesDataShipmentTrackCreationInterface' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SalesDataShipmentTrackCreationInterface> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SalesDataShipmentTrackCreationInterface.class));

       return (TypeAdapter<T>) new TypeAdapter<SalesDataShipmentTrackCreationInterface>() {
           @Override
           public void write(JsonWriter out, SalesDataShipmentTrackCreationInterface value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SalesDataShipmentTrackCreationInterface read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SalesDataShipmentTrackCreationInterface given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SalesDataShipmentTrackCreationInterface
   * @throws IOException if the JSON string is invalid with respect to SalesDataShipmentTrackCreationInterface
   */
  public static SalesDataShipmentTrackCreationInterface fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SalesDataShipmentTrackCreationInterface.class);
  }

  /**
   * Convert an instance of SalesDataShipmentTrackCreationInterface to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

