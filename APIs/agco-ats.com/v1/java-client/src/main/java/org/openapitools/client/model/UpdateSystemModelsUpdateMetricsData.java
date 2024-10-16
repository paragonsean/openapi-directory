/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord;
import org.openapitools.client.model.UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord;
import org.openapitools.client.model.UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord;

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
 * Model that retrieves the data for UpdateMetrics
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:35.511967-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class UpdateSystemModelsUpdateMetricsData {
  public static final String SERIALIZED_NAME_ACTIVE_VERSION = "ActiveVersion";
  @SerializedName(SERIALIZED_NAME_ACTIVE_VERSION)
  private String activeVersion;

  public static final String SERIALIZED_NAME_ACTIVE_VERSION_BY_CLIENT = "ActiveVersionByClient";
  @SerializedName(SERIALIZED_NAME_ACTIVE_VERSION_BY_CLIENT)
  private List<UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord> activeVersionByClient = new ArrayList<>();

  public static final String SERIALIZED_NAME_CURRENT_STATE_BY_CLIENT = "CurrentStateByClient";
  @SerializedName(SERIALIZED_NAME_CURRENT_STATE_BY_CLIENT)
  private List<UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord> currentStateByClient = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUT_OFF_DATE = "CutOffDate";
  @SerializedName(SERIALIZED_NAME_CUT_OFF_DATE)
  private OffsetDateTime cutOffDate;

  public static final String SERIALIZED_NAME_DATA_REFRESHED = "DataRefreshed";
  @SerializedName(SERIALIZED_NAME_DATA_REFRESHED)
  private OffsetDateTime dataRefreshed;

  public static final String SERIALIZED_NAME_FILTERED_CLIENT_COUNT = "FilteredClientCount";
  @SerializedName(SERIALIZED_NAME_FILTERED_CLIENT_COUNT)
  private Integer filteredClientCount;

  public static final String SERIALIZED_NAME_PACKAGE_ERRORS = "PackageErrors";
  @SerializedName(SERIALIZED_NAME_PACKAGE_ERRORS)
  private List<UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord> packageErrors = new ArrayList<>();

  public static final String SERIALIZED_NAME_TOTAL_CLIENT_COUNT = "TotalClientCount";
  @SerializedName(SERIALIZED_NAME_TOTAL_CLIENT_COUNT)
  private Integer totalClientCount;

  public UpdateSystemModelsUpdateMetricsData() {
  }

  public UpdateSystemModelsUpdateMetricsData activeVersion(String activeVersion) {
    this.activeVersion = activeVersion;
    return this;
  }

  /**
   * Active version (bundle number) of update type.
   * @return activeVersion
   */
  @javax.annotation.Nullable
  public String getActiveVersion() {
    return activeVersion;
  }

  public void setActiveVersion(String activeVersion) {
    this.activeVersion = activeVersion;
  }


  public UpdateSystemModelsUpdateMetricsData activeVersionByClient(List<UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord> activeVersionByClient) {
    this.activeVersionByClient = activeVersionByClient;
    return this;
  }

  public UpdateSystemModelsUpdateMetricsData addActiveVersionByClientItem(UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord activeVersionByClientItem) {
    if (this.activeVersionByClient == null) {
      this.activeVersionByClient = new ArrayList<>();
    }
    this.activeVersionByClient.add(activeVersionByClientItem);
    return this;
  }

  /**
   * Generic collection that is of type ActiveVersionByClientRecord
   * @return activeVersionByClient
   */
  @javax.annotation.Nullable
  public List<UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord> getActiveVersionByClient() {
    return activeVersionByClient;
  }

  public void setActiveVersionByClient(List<UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord> activeVersionByClient) {
    this.activeVersionByClient = activeVersionByClient;
  }


  public UpdateSystemModelsUpdateMetricsData currentStateByClient(List<UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord> currentStateByClient) {
    this.currentStateByClient = currentStateByClient;
    return this;
  }

  public UpdateSystemModelsUpdateMetricsData addCurrentStateByClientItem(UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord currentStateByClientItem) {
    if (this.currentStateByClient == null) {
      this.currentStateByClient = new ArrayList<>();
    }
    this.currentStateByClient.add(currentStateByClientItem);
    return this;
  }

  /**
   * Generic collection that is of type CurrentStateByClientRecord
   * @return currentStateByClient
   */
  @javax.annotation.Nullable
  public List<UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord> getCurrentStateByClient() {
    return currentStateByClient;
  }

  public void setCurrentStateByClient(List<UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord> currentStateByClient) {
    this.currentStateByClient = currentStateByClient;
  }


  public UpdateSystemModelsUpdateMetricsData cutOffDate(OffsetDateTime cutOffDate) {
    this.cutOffDate = cutOffDate;
    return this;
  }

  /**
   * Date that has been configured to only show the most recent clients with a cut off date. (Ex. year from current date)
   * @return cutOffDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCutOffDate() {
    return cutOffDate;
  }

  public void setCutOffDate(OffsetDateTime cutOffDate) {
    this.cutOffDate = cutOffDate;
  }


  public UpdateSystemModelsUpdateMetricsData dataRefreshed(OffsetDateTime dataRefreshed) {
    this.dataRefreshed = dataRefreshed;
    return this;
  }

  /**
   * Data was refreshed at this time.
   * @return dataRefreshed
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDataRefreshed() {
    return dataRefreshed;
  }

  public void setDataRefreshed(OffsetDateTime dataRefreshed) {
    this.dataRefreshed = dataRefreshed;
  }


  public UpdateSystemModelsUpdateMetricsData filteredClientCount(Integer filteredClientCount) {
    this.filteredClientCount = filteredClientCount;
    return this;
  }

  /**
   * Sum of clients represented              Filtered by updateType and lastCheckedInDate
   * @return filteredClientCount
   */
  @javax.annotation.Nullable
  public Integer getFilteredClientCount() {
    return filteredClientCount;
  }

  public void setFilteredClientCount(Integer filteredClientCount) {
    this.filteredClientCount = filteredClientCount;
  }


  public UpdateSystemModelsUpdateMetricsData packageErrors(List<UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord> packageErrors) {
    this.packageErrors = packageErrors;
    return this;
  }

  public UpdateSystemModelsUpdateMetricsData addPackageErrorsItem(UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord packageErrorsItem) {
    if (this.packageErrors == null) {
      this.packageErrors = new ArrayList<>();
    }
    this.packageErrors.add(packageErrorsItem);
    return this;
  }

  /**
   * Generic collection that is of type PackageErrorsRecord
   * @return packageErrors
   */
  @javax.annotation.Nullable
  public List<UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord> getPackageErrors() {
    return packageErrors;
  }

  public void setPackageErrors(List<UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord> packageErrors) {
    this.packageErrors = packageErrors;
  }


  public UpdateSystemModelsUpdateMetricsData totalClientCount(Integer totalClientCount) {
    this.totalClientCount = totalClientCount;
    return this;
  }

  /**
   * Total clients we have ever serviced
   * @return totalClientCount
   */
  @javax.annotation.Nullable
  public Integer getTotalClientCount() {
    return totalClientCount;
  }

  public void setTotalClientCount(Integer totalClientCount) {
    this.totalClientCount = totalClientCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UpdateSystemModelsUpdateMetricsData updateSystemModelsUpdateMetricsData = (UpdateSystemModelsUpdateMetricsData) o;
    return Objects.equals(this.activeVersion, updateSystemModelsUpdateMetricsData.activeVersion) &&
        Objects.equals(this.activeVersionByClient, updateSystemModelsUpdateMetricsData.activeVersionByClient) &&
        Objects.equals(this.currentStateByClient, updateSystemModelsUpdateMetricsData.currentStateByClient) &&
        Objects.equals(this.cutOffDate, updateSystemModelsUpdateMetricsData.cutOffDate) &&
        Objects.equals(this.dataRefreshed, updateSystemModelsUpdateMetricsData.dataRefreshed) &&
        Objects.equals(this.filteredClientCount, updateSystemModelsUpdateMetricsData.filteredClientCount) &&
        Objects.equals(this.packageErrors, updateSystemModelsUpdateMetricsData.packageErrors) &&
        Objects.equals(this.totalClientCount, updateSystemModelsUpdateMetricsData.totalClientCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(activeVersion, activeVersionByClient, currentStateByClient, cutOffDate, dataRefreshed, filteredClientCount, packageErrors, totalClientCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UpdateSystemModelsUpdateMetricsData {\n");
    sb.append("    activeVersion: ").append(toIndentedString(activeVersion)).append("\n");
    sb.append("    activeVersionByClient: ").append(toIndentedString(activeVersionByClient)).append("\n");
    sb.append("    currentStateByClient: ").append(toIndentedString(currentStateByClient)).append("\n");
    sb.append("    cutOffDate: ").append(toIndentedString(cutOffDate)).append("\n");
    sb.append("    dataRefreshed: ").append(toIndentedString(dataRefreshed)).append("\n");
    sb.append("    filteredClientCount: ").append(toIndentedString(filteredClientCount)).append("\n");
    sb.append("    packageErrors: ").append(toIndentedString(packageErrors)).append("\n");
    sb.append("    totalClientCount: ").append(toIndentedString(totalClientCount)).append("\n");
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
    openapiFields.add("ActiveVersion");
    openapiFields.add("ActiveVersionByClient");
    openapiFields.add("CurrentStateByClient");
    openapiFields.add("CutOffDate");
    openapiFields.add("DataRefreshed");
    openapiFields.add("FilteredClientCount");
    openapiFields.add("PackageErrors");
    openapiFields.add("TotalClientCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to UpdateSystemModelsUpdateMetricsData
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!UpdateSystemModelsUpdateMetricsData.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in UpdateSystemModelsUpdateMetricsData is not found in the empty JSON string", UpdateSystemModelsUpdateMetricsData.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!UpdateSystemModelsUpdateMetricsData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `UpdateSystemModelsUpdateMetricsData` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("ActiveVersion") != null && !jsonObj.get("ActiveVersion").isJsonNull()) && !jsonObj.get("ActiveVersion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ActiveVersion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ActiveVersion").toString()));
      }
      if (jsonObj.get("ActiveVersionByClient") != null && !jsonObj.get("ActiveVersionByClient").isJsonNull()) {
        JsonArray jsonArrayactiveVersionByClient = jsonObj.getAsJsonArray("ActiveVersionByClient");
        if (jsonArrayactiveVersionByClient != null) {
          // ensure the json data is an array
          if (!jsonObj.get("ActiveVersionByClient").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `ActiveVersionByClient` to be an array in the JSON string but got `%s`", jsonObj.get("ActiveVersionByClient").toString()));
          }

          // validate the optional field `ActiveVersionByClient` (array)
          for (int i = 0; i < jsonArrayactiveVersionByClient.size(); i++) {
            UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.validateJsonElement(jsonArrayactiveVersionByClient.get(i));
          };
        }
      }
      if (jsonObj.get("CurrentStateByClient") != null && !jsonObj.get("CurrentStateByClient").isJsonNull()) {
        JsonArray jsonArraycurrentStateByClient = jsonObj.getAsJsonArray("CurrentStateByClient");
        if (jsonArraycurrentStateByClient != null) {
          // ensure the json data is an array
          if (!jsonObj.get("CurrentStateByClient").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `CurrentStateByClient` to be an array in the JSON string but got `%s`", jsonObj.get("CurrentStateByClient").toString()));
          }

          // validate the optional field `CurrentStateByClient` (array)
          for (int i = 0; i < jsonArraycurrentStateByClient.size(); i++) {
            UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord.validateJsonElement(jsonArraycurrentStateByClient.get(i));
          };
        }
      }
      if (jsonObj.get("PackageErrors") != null && !jsonObj.get("PackageErrors").isJsonNull()) {
        JsonArray jsonArraypackageErrors = jsonObj.getAsJsonArray("PackageErrors");
        if (jsonArraypackageErrors != null) {
          // ensure the json data is an array
          if (!jsonObj.get("PackageErrors").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `PackageErrors` to be an array in the JSON string but got `%s`", jsonObj.get("PackageErrors").toString()));
          }

          // validate the optional field `PackageErrors` (array)
          for (int i = 0; i < jsonArraypackageErrors.size(); i++) {
            UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.validateJsonElement(jsonArraypackageErrors.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!UpdateSystemModelsUpdateMetricsData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'UpdateSystemModelsUpdateMetricsData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<UpdateSystemModelsUpdateMetricsData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(UpdateSystemModelsUpdateMetricsData.class));

       return (TypeAdapter<T>) new TypeAdapter<UpdateSystemModelsUpdateMetricsData>() {
           @Override
           public void write(JsonWriter out, UpdateSystemModelsUpdateMetricsData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public UpdateSystemModelsUpdateMetricsData read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of UpdateSystemModelsUpdateMetricsData given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of UpdateSystemModelsUpdateMetricsData
   * @throws IOException if the JSON string is invalid with respect to UpdateSystemModelsUpdateMetricsData
   */
  public static UpdateSystemModelsUpdateMetricsData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, UpdateSystemModelsUpdateMetricsData.class);
  }

  /**
   * Convert an instance of UpdateSystemModelsUpdateMetricsData to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

