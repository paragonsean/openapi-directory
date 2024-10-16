/*
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AdvicentNaviPlanRestApiGoalsModelsGoalFundingAccount;

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
 * AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem {
  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FUNDING_ACCOUNTS = "fundingAccounts";
  @SerializedName(SERIALIZED_NAME_FUNDING_ACCOUNTS)
  private List<AdvicentNaviPlanRestApiGoalsModelsGoalFundingAccount> fundingAccounts = new ArrayList<>();

  public static final String SERIALIZED_NAME_GOAL_ID = "goalId";
  @SerializedName(SERIALIZED_NAME_GOAL_ID)
  private Integer goalId;

  public AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem() {
  }

  public AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem fundingAccounts(List<AdvicentNaviPlanRestApiGoalsModelsGoalFundingAccount> fundingAccounts) {
    this.fundingAccounts = fundingAccounts;
    return this;
  }

  public AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem addFundingAccountsItem(AdvicentNaviPlanRestApiGoalsModelsGoalFundingAccount fundingAccountsItem) {
    if (this.fundingAccounts == null) {
      this.fundingAccounts = new ArrayList<>();
    }
    this.fundingAccounts.add(fundingAccountsItem);
    return this;
  }

  /**
   * Get fundingAccounts
   * @return fundingAccounts
   */
  @javax.annotation.Nullable
  public List<AdvicentNaviPlanRestApiGoalsModelsGoalFundingAccount> getFundingAccounts() {
    return fundingAccounts;
  }

  public void setFundingAccounts(List<AdvicentNaviPlanRestApiGoalsModelsGoalFundingAccount> fundingAccounts) {
    this.fundingAccounts = fundingAccounts;
  }


  public AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem goalId(Integer goalId) {
    this.goalId = goalId;
    return this;
  }

  /**
   * Get goalId
   * @return goalId
   */
  @javax.annotation.Nullable
  public Integer getGoalId() {
    return goalId;
  }

  public void setGoalId(Integer goalId) {
    this.goalId = goalId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem advicentNaviPlanRestApiGoalsModelsGoalFundingListItem = (AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem) o;
    return Objects.equals(this.description, advicentNaviPlanRestApiGoalsModelsGoalFundingListItem.description) &&
        Objects.equals(this.fundingAccounts, advicentNaviPlanRestApiGoalsModelsGoalFundingListItem.fundingAccounts) &&
        Objects.equals(this.goalId, advicentNaviPlanRestApiGoalsModelsGoalFundingListItem.goalId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(description, fundingAccounts, goalId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem {\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    fundingAccounts: ").append(toIndentedString(fundingAccounts)).append("\n");
    sb.append("    goalId: ").append(toIndentedString(goalId)).append("\n");
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
    openapiFields.add("description");
    openapiFields.add("fundingAccounts");
    openapiFields.add("goalId");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem is not found in the empty JSON string", AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (jsonObj.get("fundingAccounts") != null && !jsonObj.get("fundingAccounts").isJsonNull()) {
        JsonArray jsonArrayfundingAccounts = jsonObj.getAsJsonArray("fundingAccounts");
        if (jsonArrayfundingAccounts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("fundingAccounts").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `fundingAccounts` to be an array in the JSON string but got `%s`", jsonObj.get("fundingAccounts").toString()));
          }

          // validate the optional field `fundingAccounts` (array)
          for (int i = 0; i < jsonArrayfundingAccounts.size(); i++) {
            AdvicentNaviPlanRestApiGoalsModelsGoalFundingAccount.validateJsonElement(jsonArrayfundingAccounts.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem.class));

       return (TypeAdapter<T>) new TypeAdapter<AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem>() {
           @Override
           public void write(JsonWriter out, AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem
   * @throws IOException if the JSON string is invalid with respect to AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem
   */
  public static AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem.class);
  }

  /**
   * Convert an instance of AdvicentNaviPlanRestApiGoalsModelsGoalFundingListItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

