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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner;
import org.openapitools.client.model.UpdateNetworkFirmwareUpgradesStagedEventsRequestStagesInner;

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
 * RollbacksNetworkFirmwareUpgradesStagedEventsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RollbacksNetworkFirmwareUpgradesStagedEventsRequest {
  public static final String SERIALIZED_NAME_REASONS = "reasons";
  @SerializedName(SERIALIZED_NAME_REASONS)
  private List<CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner> reasons = new ArrayList<>();

  public static final String SERIALIZED_NAME_STAGES = "stages";
  @SerializedName(SERIALIZED_NAME_STAGES)
  private List<UpdateNetworkFirmwareUpgradesStagedEventsRequestStagesInner> stages = new ArrayList<>();

  public RollbacksNetworkFirmwareUpgradesStagedEventsRequest() {
  }

  public RollbacksNetworkFirmwareUpgradesStagedEventsRequest reasons(List<CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner> reasons) {
    this.reasons = reasons;
    return this;
  }

  public RollbacksNetworkFirmwareUpgradesStagedEventsRequest addReasonsItem(CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner reasonsItem) {
    if (this.reasons == null) {
      this.reasons = new ArrayList<>();
    }
    this.reasons.add(reasonsItem);
    return this;
  }

  /**
   * The reason for rolling back the staged upgrade
   * @return reasons
   */
  @javax.annotation.Nullable
  public List<CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner> getReasons() {
    return reasons;
  }

  public void setReasons(List<CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner> reasons) {
    this.reasons = reasons;
  }


  public RollbacksNetworkFirmwareUpgradesStagedEventsRequest stages(List<UpdateNetworkFirmwareUpgradesStagedEventsRequestStagesInner> stages) {
    this.stages = stages;
    return this;
  }

  public RollbacksNetworkFirmwareUpgradesStagedEventsRequest addStagesItem(UpdateNetworkFirmwareUpgradesStagedEventsRequestStagesInner stagesItem) {
    if (this.stages == null) {
      this.stages = new ArrayList<>();
    }
    this.stages.add(stagesItem);
    return this;
  }

  /**
   * All completed or in-progress stages in the network with their new start times. All pending stages will be canceled
   * @return stages
   */
  @javax.annotation.Nonnull
  public List<UpdateNetworkFirmwareUpgradesStagedEventsRequestStagesInner> getStages() {
    return stages;
  }

  public void setStages(List<UpdateNetworkFirmwareUpgradesStagedEventsRequestStagesInner> stages) {
    this.stages = stages;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RollbacksNetworkFirmwareUpgradesStagedEventsRequest rollbacksNetworkFirmwareUpgradesStagedEventsRequest = (RollbacksNetworkFirmwareUpgradesStagedEventsRequest) o;
    return Objects.equals(this.reasons, rollbacksNetworkFirmwareUpgradesStagedEventsRequest.reasons) &&
        Objects.equals(this.stages, rollbacksNetworkFirmwareUpgradesStagedEventsRequest.stages);
  }

  @Override
  public int hashCode() {
    return Objects.hash(reasons, stages);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RollbacksNetworkFirmwareUpgradesStagedEventsRequest {\n");
    sb.append("    reasons: ").append(toIndentedString(reasons)).append("\n");
    sb.append("    stages: ").append(toIndentedString(stages)).append("\n");
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
    openapiFields.add("reasons");
    openapiFields.add("stages");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("stages");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RollbacksNetworkFirmwareUpgradesStagedEventsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RollbacksNetworkFirmwareUpgradesStagedEventsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RollbacksNetworkFirmwareUpgradesStagedEventsRequest is not found in the empty JSON string", RollbacksNetworkFirmwareUpgradesStagedEventsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RollbacksNetworkFirmwareUpgradesStagedEventsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RollbacksNetworkFirmwareUpgradesStagedEventsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : RollbacksNetworkFirmwareUpgradesStagedEventsRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("reasons") != null && !jsonObj.get("reasons").isJsonNull()) {
        JsonArray jsonArrayreasons = jsonObj.getAsJsonArray("reasons");
        if (jsonArrayreasons != null) {
          // ensure the json data is an array
          if (!jsonObj.get("reasons").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `reasons` to be an array in the JSON string but got `%s`", jsonObj.get("reasons").toString()));
          }

          // validate the optional field `reasons` (array)
          for (int i = 0; i < jsonArrayreasons.size(); i++) {
            CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner.validateJsonElement(jsonArrayreasons.get(i));
          };
        }
      }
      // ensure the json data is an array
      if (!jsonObj.get("stages").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `stages` to be an array in the JSON string but got `%s`", jsonObj.get("stages").toString()));
      }

      JsonArray jsonArraystages = jsonObj.getAsJsonArray("stages");
      // validate the required field `stages` (array)
      for (int i = 0; i < jsonArraystages.size(); i++) {
        UpdateNetworkFirmwareUpgradesStagedEventsRequestStagesInner.validateJsonElement(jsonArraystages.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RollbacksNetworkFirmwareUpgradesStagedEventsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RollbacksNetworkFirmwareUpgradesStagedEventsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RollbacksNetworkFirmwareUpgradesStagedEventsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RollbacksNetworkFirmwareUpgradesStagedEventsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<RollbacksNetworkFirmwareUpgradesStagedEventsRequest>() {
           @Override
           public void write(JsonWriter out, RollbacksNetworkFirmwareUpgradesStagedEventsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RollbacksNetworkFirmwareUpgradesStagedEventsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RollbacksNetworkFirmwareUpgradesStagedEventsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RollbacksNetworkFirmwareUpgradesStagedEventsRequest
   * @throws IOException if the JSON string is invalid with respect to RollbacksNetworkFirmwareUpgradesStagedEventsRequest
   */
  public static RollbacksNetworkFirmwareUpgradesStagedEventsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RollbacksNetworkFirmwareUpgradesStagedEventsRequest.class);
  }

  /**
   * Convert an instance of RollbacksNetworkFirmwareUpgradesStagedEventsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

