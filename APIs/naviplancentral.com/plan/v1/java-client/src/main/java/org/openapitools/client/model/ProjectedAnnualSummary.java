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
import java.util.Arrays;
import org.openapitools.client.model.CashFlowSummary;
import org.openapitools.client.model.NetWorthSummary;

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
 * ProjectedAnnualSummary
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectedAnnualSummary {
  public static final String SERIALIZED_NAME_CASH_FLOW = "cashFlow";
  @SerializedName(SERIALIZED_NAME_CASH_FLOW)
  private CashFlowSummary cashFlow;

  public static final String SERIALIZED_NAME_CLIENT_AGE = "clientAge";
  @SerializedName(SERIALIZED_NAME_CLIENT_AGE)
  private Integer clientAge;

  public static final String SERIALIZED_NAME_CO_CLIENT_AGE = "coClientAge";
  @SerializedName(SERIALIZED_NAME_CO_CLIENT_AGE)
  private Integer coClientAge;

  public static final String SERIALIZED_NAME_NET_WORTH = "netWorth";
  @SerializedName(SERIALIZED_NAME_NET_WORTH)
  private NetWorthSummary netWorth;

  public static final String SERIALIZED_NAME_YEAR = "year";
  @SerializedName(SERIALIZED_NAME_YEAR)
  private Integer year;

  public ProjectedAnnualSummary() {
  }

  public ProjectedAnnualSummary cashFlow(CashFlowSummary cashFlow) {
    this.cashFlow = cashFlow;
    return this;
  }

  /**
   * Get cashFlow
   * @return cashFlow
   */
  @javax.annotation.Nullable
  public CashFlowSummary getCashFlow() {
    return cashFlow;
  }

  public void setCashFlow(CashFlowSummary cashFlow) {
    this.cashFlow = cashFlow;
  }


  public ProjectedAnnualSummary clientAge(Integer clientAge) {
    this.clientAge = clientAge;
    return this;
  }

  /**
   * Get clientAge
   * @return clientAge
   */
  @javax.annotation.Nullable
  public Integer getClientAge() {
    return clientAge;
  }

  public void setClientAge(Integer clientAge) {
    this.clientAge = clientAge;
  }


  public ProjectedAnnualSummary coClientAge(Integer coClientAge) {
    this.coClientAge = coClientAge;
    return this;
  }

  /**
   * Get coClientAge
   * @return coClientAge
   */
  @javax.annotation.Nullable
  public Integer getCoClientAge() {
    return coClientAge;
  }

  public void setCoClientAge(Integer coClientAge) {
    this.coClientAge = coClientAge;
  }


  public ProjectedAnnualSummary netWorth(NetWorthSummary netWorth) {
    this.netWorth = netWorth;
    return this;
  }

  /**
   * Get netWorth
   * @return netWorth
   */
  @javax.annotation.Nullable
  public NetWorthSummary getNetWorth() {
    return netWorth;
  }

  public void setNetWorth(NetWorthSummary netWorth) {
    this.netWorth = netWorth;
  }


  public ProjectedAnnualSummary year(Integer year) {
    this.year = year;
    return this;
  }

  /**
   * Get year
   * @return year
   */
  @javax.annotation.Nullable
  public Integer getYear() {
    return year;
  }

  public void setYear(Integer year) {
    this.year = year;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectedAnnualSummary projectedAnnualSummary = (ProjectedAnnualSummary) o;
    return Objects.equals(this.cashFlow, projectedAnnualSummary.cashFlow) &&
        Objects.equals(this.clientAge, projectedAnnualSummary.clientAge) &&
        Objects.equals(this.coClientAge, projectedAnnualSummary.coClientAge) &&
        Objects.equals(this.netWorth, projectedAnnualSummary.netWorth) &&
        Objects.equals(this.year, projectedAnnualSummary.year);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cashFlow, clientAge, coClientAge, netWorth, year);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectedAnnualSummary {\n");
    sb.append("    cashFlow: ").append(toIndentedString(cashFlow)).append("\n");
    sb.append("    clientAge: ").append(toIndentedString(clientAge)).append("\n");
    sb.append("    coClientAge: ").append(toIndentedString(coClientAge)).append("\n");
    sb.append("    netWorth: ").append(toIndentedString(netWorth)).append("\n");
    sb.append("    year: ").append(toIndentedString(year)).append("\n");
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
    openapiFields.add("cashFlow");
    openapiFields.add("clientAge");
    openapiFields.add("coClientAge");
    openapiFields.add("netWorth");
    openapiFields.add("year");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectedAnnualSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectedAnnualSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectedAnnualSummary is not found in the empty JSON string", ProjectedAnnualSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectedAnnualSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectedAnnualSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `cashFlow`
      if (jsonObj.get("cashFlow") != null && !jsonObj.get("cashFlow").isJsonNull()) {
        CashFlowSummary.validateJsonElement(jsonObj.get("cashFlow"));
      }
      // validate the optional field `netWorth`
      if (jsonObj.get("netWorth") != null && !jsonObj.get("netWorth").isJsonNull()) {
        NetWorthSummary.validateJsonElement(jsonObj.get("netWorth"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectedAnnualSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectedAnnualSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectedAnnualSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectedAnnualSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectedAnnualSummary>() {
           @Override
           public void write(JsonWriter out, ProjectedAnnualSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectedAnnualSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectedAnnualSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectedAnnualSummary
   * @throws IOException if the JSON string is invalid with respect to ProjectedAnnualSummary
   */
  public static ProjectedAnnualSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectedAnnualSummary.class);
  }

  /**
   * Convert an instance of ProjectedAnnualSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

