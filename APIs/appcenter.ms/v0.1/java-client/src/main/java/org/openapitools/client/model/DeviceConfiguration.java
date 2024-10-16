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
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.UUID;
import org.openapitools.client.model.TestGetDeviceConfigurations200ResponseInnerImage;
import org.openapitools.client.model.TestGetDeviceConfigurations200ResponseInnerModel;

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
 * DeviceConfiguration
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:40.008147-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeviceConfiguration {
  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private TestGetDeviceConfigurations200ResponseInnerImage image;

  public static final String SERIALIZED_NAME_MARKET_SHARE = "marketShare";
  @SerializedName(SERIALIZED_NAME_MARKET_SHARE)
  private BigDecimal marketShare;

  public static final String SERIALIZED_NAME_MODEL = "model";
  @SerializedName(SERIALIZED_NAME_MODEL)
  private TestGetDeviceConfigurations200ResponseInnerModel model;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_OS = "os";
  @SerializedName(SERIALIZED_NAME_OS)
  private String os;

  public static final String SERIALIZED_NAME_OS_NAME = "osName";
  @SerializedName(SERIALIZED_NAME_OS_NAME)
  private String osName;

  public static final String SERIALIZED_NAME_TIER = "tier";
  @SerializedName(SERIALIZED_NAME_TIER)
  private BigDecimal tier;

  public DeviceConfiguration() {
  }

  public DeviceConfiguration id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * The unique id of the device configuration
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public DeviceConfiguration image(TestGetDeviceConfigurations200ResponseInnerImage image) {
    this.image = image;
    return this;
  }

  /**
   * Get image
   * @return image
   */
  @javax.annotation.Nullable
  public TestGetDeviceConfigurations200ResponseInnerImage getImage() {
    return image;
  }

  public void setImage(TestGetDeviceConfigurations200ResponseInnerImage image) {
    this.image = image;
  }


  public DeviceConfiguration marketShare(BigDecimal marketShare) {
    this.marketShare = marketShare;
    return this;
  }

  /**
   * Get marketShare
   * @return marketShare
   */
  @javax.annotation.Nullable
  public BigDecimal getMarketShare() {
    return marketShare;
  }

  public void setMarketShare(BigDecimal marketShare) {
    this.marketShare = marketShare;
  }


  public DeviceConfiguration model(TestGetDeviceConfigurations200ResponseInnerModel model) {
    this.model = model;
    return this;
  }

  /**
   * Get model
   * @return model
   */
  @javax.annotation.Nullable
  public TestGetDeviceConfigurations200ResponseInnerModel getModel() {
    return model;
  }

  public void setModel(TestGetDeviceConfigurations200ResponseInnerModel model) {
    this.model = model;
  }


  public DeviceConfiguration name(String name) {
    this.name = name;
    return this;
  }

  /**
   * The name of the device model and OS version
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public DeviceConfiguration os(String os) {
    this.os = os;
    return this;
  }

  /**
   * Get os
   * @return os
   */
  @javax.annotation.Nullable
  public String getOs() {
    return os;
  }

  public void setOs(String os) {
    this.os = os;
  }


  public DeviceConfiguration osName(String osName) {
    this.osName = osName;
    return this;
  }

  /**
   * Get osName
   * @return osName
   */
  @javax.annotation.Nullable
  public String getOsName() {
    return osName;
  }

  public void setOsName(String osName) {
    this.osName = osName;
  }


  public DeviceConfiguration tier(BigDecimal tier) {
    this.tier = tier;
    return this;
  }

  /**
   * The tier
   * @return tier
   */
  @javax.annotation.Nullable
  public BigDecimal getTier() {
    return tier;
  }

  public void setTier(BigDecimal tier) {
    this.tier = tier;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeviceConfiguration deviceConfiguration = (DeviceConfiguration) o;
    return Objects.equals(this.id, deviceConfiguration.id) &&
        Objects.equals(this.image, deviceConfiguration.image) &&
        Objects.equals(this.marketShare, deviceConfiguration.marketShare) &&
        Objects.equals(this.model, deviceConfiguration.model) &&
        Objects.equals(this.name, deviceConfiguration.name) &&
        Objects.equals(this.os, deviceConfiguration.os) &&
        Objects.equals(this.osName, deviceConfiguration.osName) &&
        Objects.equals(this.tier, deviceConfiguration.tier);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, image, marketShare, model, name, os, osName, tier);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeviceConfiguration {\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    marketShare: ").append(toIndentedString(marketShare)).append("\n");
    sb.append("    model: ").append(toIndentedString(model)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    osName: ").append(toIndentedString(osName)).append("\n");
    sb.append("    tier: ").append(toIndentedString(tier)).append("\n");
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
    openapiFields.add("id");
    openapiFields.add("image");
    openapiFields.add("marketShare");
    openapiFields.add("model");
    openapiFields.add("name");
    openapiFields.add("os");
    openapiFields.add("osName");
    openapiFields.add("tier");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeviceConfiguration
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeviceConfiguration.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeviceConfiguration is not found in the empty JSON string", DeviceConfiguration.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeviceConfiguration.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeviceConfiguration` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      // validate the optional field `image`
      if (jsonObj.get("image") != null && !jsonObj.get("image").isJsonNull()) {
        TestGetDeviceConfigurations200ResponseInnerImage.validateJsonElement(jsonObj.get("image"));
      }
      // validate the optional field `model`
      if (jsonObj.get("model") != null && !jsonObj.get("model").isJsonNull()) {
        TestGetDeviceConfigurations200ResponseInnerModel.validateJsonElement(jsonObj.get("model"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("os") != null && !jsonObj.get("os").isJsonNull()) && !jsonObj.get("os").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `os` to be a primitive type in the JSON string but got `%s`", jsonObj.get("os").toString()));
      }
      if ((jsonObj.get("osName") != null && !jsonObj.get("osName").isJsonNull()) && !jsonObj.get("osName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `osName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("osName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeviceConfiguration.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeviceConfiguration' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeviceConfiguration> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeviceConfiguration.class));

       return (TypeAdapter<T>) new TypeAdapter<DeviceConfiguration>() {
           @Override
           public void write(JsonWriter out, DeviceConfiguration value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeviceConfiguration read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeviceConfiguration given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeviceConfiguration
   * @throws IOException if the JSON string is invalid with respect to DeviceConfiguration
   */
  public static DeviceConfiguration fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeviceConfiguration.class);
  }

  /**
   * Convert an instance of DeviceConfiguration to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

