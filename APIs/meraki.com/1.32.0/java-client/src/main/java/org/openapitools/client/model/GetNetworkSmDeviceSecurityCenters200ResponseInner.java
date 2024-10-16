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
 * GetNetworkSmDeviceSecurityCenters200ResponseInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetNetworkSmDeviceSecurityCenters200ResponseInner {
  public static final String SERIALIZED_NAME_ANTI_VIRUS_NAME = "antiVirusName";
  @SerializedName(SERIALIZED_NAME_ANTI_VIRUS_NAME)
  private String antiVirusName;

  public static final String SERIALIZED_NAME_FIRE_WALL_NAME = "fireWallName";
  @SerializedName(SERIALIZED_NAME_FIRE_WALL_NAME)
  private String fireWallName;

  public static final String SERIALIZED_NAME_HAS_ANTI_VIRUS = "hasAntiVirus";
  @SerializedName(SERIALIZED_NAME_HAS_ANTI_VIRUS)
  private Boolean hasAntiVirus;

  public static final String SERIALIZED_NAME_HAS_FIRE_WALL_INSTALLED = "hasFireWallInstalled";
  @SerializedName(SERIALIZED_NAME_HAS_FIRE_WALL_INSTALLED)
  private Boolean hasFireWallInstalled;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_AUTO_LOGIN_DISABLED = "isAutoLoginDisabled";
  @SerializedName(SERIALIZED_NAME_IS_AUTO_LOGIN_DISABLED)
  private Boolean isAutoLoginDisabled;

  public static final String SERIALIZED_NAME_IS_DISK_ENCRYPTED = "isDiskEncrypted";
  @SerializedName(SERIALIZED_NAME_IS_DISK_ENCRYPTED)
  private Boolean isDiskEncrypted;

  public static final String SERIALIZED_NAME_IS_FIRE_WALL_ENABLED = "isFireWallEnabled";
  @SerializedName(SERIALIZED_NAME_IS_FIRE_WALL_ENABLED)
  private Boolean isFireWallEnabled;

  public static final String SERIALIZED_NAME_IS_ROOTED = "isRooted";
  @SerializedName(SERIALIZED_NAME_IS_ROOTED)
  private Boolean isRooted;

  public static final String SERIALIZED_NAME_RUNNING_PROCS = "runningProcs";
  @SerializedName(SERIALIZED_NAME_RUNNING_PROCS)
  private String runningProcs;

  public GetNetworkSmDeviceSecurityCenters200ResponseInner() {
  }

  public GetNetworkSmDeviceSecurityCenters200ResponseInner antiVirusName(String antiVirusName) {
    this.antiVirusName = antiVirusName;
    return this;
  }

  /**
   * The name of the Antivirus.
   * @return antiVirusName
   */
  @javax.annotation.Nullable
  public String getAntiVirusName() {
    return antiVirusName;
  }

  public void setAntiVirusName(String antiVirusName) {
    this.antiVirusName = antiVirusName;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner fireWallName(String fireWallName) {
    this.fireWallName = fireWallName;
    return this;
  }

  /**
   * The name of the Firewall.
   * @return fireWallName
   */
  @javax.annotation.Nullable
  public String getFireWallName() {
    return fireWallName;
  }

  public void setFireWallName(String fireWallName) {
    this.fireWallName = fireWallName;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner hasAntiVirus(Boolean hasAntiVirus) {
    this.hasAntiVirus = hasAntiVirus;
    return this;
  }

  /**
   * Boolean indicating if the device has Antivirus.
   * @return hasAntiVirus
   */
  @javax.annotation.Nullable
  public Boolean getHasAntiVirus() {
    return hasAntiVirus;
  }

  public void setHasAntiVirus(Boolean hasAntiVirus) {
    this.hasAntiVirus = hasAntiVirus;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner hasFireWallInstalled(Boolean hasFireWallInstalled) {
    this.hasFireWallInstalled = hasFireWallInstalled;
    return this;
  }

  /**
   * Boolean indicating if the device has a Firewall installed.
   * @return hasFireWallInstalled
   */
  @javax.annotation.Nullable
  public Boolean getHasFireWallInstalled() {
    return hasFireWallInstalled;
  }

  public void setHasFireWallInstalled(Boolean hasFireWallInstalled) {
    this.hasFireWallInstalled = hasFireWallInstalled;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner id(String id) {
    this.id = id;
    return this;
  }

  /**
   * The Meraki identifier for the security center record.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner isAutoLoginDisabled(Boolean isAutoLoginDisabled) {
    this.isAutoLoginDisabled = isAutoLoginDisabled;
    return this;
  }

  /**
   * Boolean indicating if the device has auto login disabled.
   * @return isAutoLoginDisabled
   */
  @javax.annotation.Nullable
  public Boolean getIsAutoLoginDisabled() {
    return isAutoLoginDisabled;
  }

  public void setIsAutoLoginDisabled(Boolean isAutoLoginDisabled) {
    this.isAutoLoginDisabled = isAutoLoginDisabled;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner isDiskEncrypted(Boolean isDiskEncrypted) {
    this.isDiskEncrypted = isDiskEncrypted;
    return this;
  }

  /**
   * Boolean indicating if the device has disk encryption.
   * @return isDiskEncrypted
   */
  @javax.annotation.Nullable
  public Boolean getIsDiskEncrypted() {
    return isDiskEncrypted;
  }

  public void setIsDiskEncrypted(Boolean isDiskEncrypted) {
    this.isDiskEncrypted = isDiskEncrypted;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner isFireWallEnabled(Boolean isFireWallEnabled) {
    this.isFireWallEnabled = isFireWallEnabled;
    return this;
  }

  /**
   * Boolean indicating if the device has a Firewall enabled.
   * @return isFireWallEnabled
   */
  @javax.annotation.Nullable
  public Boolean getIsFireWallEnabled() {
    return isFireWallEnabled;
  }

  public void setIsFireWallEnabled(Boolean isFireWallEnabled) {
    this.isFireWallEnabled = isFireWallEnabled;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner isRooted(Boolean isRooted) {
    this.isRooted = isRooted;
    return this;
  }

  /**
   * Boolean indicating if the device is rooted.
   * @return isRooted
   */
  @javax.annotation.Nullable
  public Boolean getIsRooted() {
    return isRooted;
  }

  public void setIsRooted(Boolean isRooted) {
    this.isRooted = isRooted;
  }


  public GetNetworkSmDeviceSecurityCenters200ResponseInner runningProcs(String runningProcs) {
    this.runningProcs = runningProcs;
    return this;
  }

  /**
   * A comma seperated list of procs running on the device.
   * @return runningProcs
   */
  @javax.annotation.Nullable
  public String getRunningProcs() {
    return runningProcs;
  }

  public void setRunningProcs(String runningProcs) {
    this.runningProcs = runningProcs;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetNetworkSmDeviceSecurityCenters200ResponseInner getNetworkSmDeviceSecurityCenters200ResponseInner = (GetNetworkSmDeviceSecurityCenters200ResponseInner) o;
    return Objects.equals(this.antiVirusName, getNetworkSmDeviceSecurityCenters200ResponseInner.antiVirusName) &&
        Objects.equals(this.fireWallName, getNetworkSmDeviceSecurityCenters200ResponseInner.fireWallName) &&
        Objects.equals(this.hasAntiVirus, getNetworkSmDeviceSecurityCenters200ResponseInner.hasAntiVirus) &&
        Objects.equals(this.hasFireWallInstalled, getNetworkSmDeviceSecurityCenters200ResponseInner.hasFireWallInstalled) &&
        Objects.equals(this.id, getNetworkSmDeviceSecurityCenters200ResponseInner.id) &&
        Objects.equals(this.isAutoLoginDisabled, getNetworkSmDeviceSecurityCenters200ResponseInner.isAutoLoginDisabled) &&
        Objects.equals(this.isDiskEncrypted, getNetworkSmDeviceSecurityCenters200ResponseInner.isDiskEncrypted) &&
        Objects.equals(this.isFireWallEnabled, getNetworkSmDeviceSecurityCenters200ResponseInner.isFireWallEnabled) &&
        Objects.equals(this.isRooted, getNetworkSmDeviceSecurityCenters200ResponseInner.isRooted) &&
        Objects.equals(this.runningProcs, getNetworkSmDeviceSecurityCenters200ResponseInner.runningProcs);
  }

  @Override
  public int hashCode() {
    return Objects.hash(antiVirusName, fireWallName, hasAntiVirus, hasFireWallInstalled, id, isAutoLoginDisabled, isDiskEncrypted, isFireWallEnabled, isRooted, runningProcs);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetNetworkSmDeviceSecurityCenters200ResponseInner {\n");
    sb.append("    antiVirusName: ").append(toIndentedString(antiVirusName)).append("\n");
    sb.append("    fireWallName: ").append(toIndentedString(fireWallName)).append("\n");
    sb.append("    hasAntiVirus: ").append(toIndentedString(hasAntiVirus)).append("\n");
    sb.append("    hasFireWallInstalled: ").append(toIndentedString(hasFireWallInstalled)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isAutoLoginDisabled: ").append(toIndentedString(isAutoLoginDisabled)).append("\n");
    sb.append("    isDiskEncrypted: ").append(toIndentedString(isDiskEncrypted)).append("\n");
    sb.append("    isFireWallEnabled: ").append(toIndentedString(isFireWallEnabled)).append("\n");
    sb.append("    isRooted: ").append(toIndentedString(isRooted)).append("\n");
    sb.append("    runningProcs: ").append(toIndentedString(runningProcs)).append("\n");
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
    openapiFields.add("antiVirusName");
    openapiFields.add("fireWallName");
    openapiFields.add("hasAntiVirus");
    openapiFields.add("hasFireWallInstalled");
    openapiFields.add("id");
    openapiFields.add("isAutoLoginDisabled");
    openapiFields.add("isDiskEncrypted");
    openapiFields.add("isFireWallEnabled");
    openapiFields.add("isRooted");
    openapiFields.add("runningProcs");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetNetworkSmDeviceSecurityCenters200ResponseInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetNetworkSmDeviceSecurityCenters200ResponseInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetNetworkSmDeviceSecurityCenters200ResponseInner is not found in the empty JSON string", GetNetworkSmDeviceSecurityCenters200ResponseInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetNetworkSmDeviceSecurityCenters200ResponseInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetNetworkSmDeviceSecurityCenters200ResponseInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("antiVirusName") != null && !jsonObj.get("antiVirusName").isJsonNull()) && !jsonObj.get("antiVirusName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `antiVirusName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("antiVirusName").toString()));
      }
      if ((jsonObj.get("fireWallName") != null && !jsonObj.get("fireWallName").isJsonNull()) && !jsonObj.get("fireWallName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fireWallName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fireWallName").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("runningProcs") != null && !jsonObj.get("runningProcs").isJsonNull()) && !jsonObj.get("runningProcs").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `runningProcs` to be a primitive type in the JSON string but got `%s`", jsonObj.get("runningProcs").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetNetworkSmDeviceSecurityCenters200ResponseInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetNetworkSmDeviceSecurityCenters200ResponseInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetNetworkSmDeviceSecurityCenters200ResponseInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetNetworkSmDeviceSecurityCenters200ResponseInner.class));

       return (TypeAdapter<T>) new TypeAdapter<GetNetworkSmDeviceSecurityCenters200ResponseInner>() {
           @Override
           public void write(JsonWriter out, GetNetworkSmDeviceSecurityCenters200ResponseInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetNetworkSmDeviceSecurityCenters200ResponseInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetNetworkSmDeviceSecurityCenters200ResponseInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetNetworkSmDeviceSecurityCenters200ResponseInner
   * @throws IOException if the JSON string is invalid with respect to GetNetworkSmDeviceSecurityCenters200ResponseInner
   */
  public static GetNetworkSmDeviceSecurityCenters200ResponseInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetNetworkSmDeviceSecurityCenters200ResponseInner.class);
  }

  /**
   * Convert an instance of GetNetworkSmDeviceSecurityCenters200ResponseInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

