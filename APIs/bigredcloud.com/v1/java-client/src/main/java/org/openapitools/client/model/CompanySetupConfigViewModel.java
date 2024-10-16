/*
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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
import org.openapitools.client.model.CompanyFinancialYearViewModel;
import org.openapitools.client.model.CompanyGeneralDetaisViewModel;
import org.openapitools.client.model.CompanyOptionViewModel;
import org.openapitools.client.model.CompanyReferenceSettingViewModel;

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
 * CompanySetupConfigViewModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:05.666566-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompanySetupConfigViewModel {
  public static final String SERIALIZED_NAME_FINANCIAL_YEAR = "financialYear";
  @SerializedName(SERIALIZED_NAME_FINANCIAL_YEAR)
  private CompanyFinancialYearViewModel financialYear;

  public static final String SERIALIZED_NAME_GENERAL_DETAILS = "generalDetails";
  @SerializedName(SERIALIZED_NAME_GENERAL_DETAILS)
  private CompanyGeneralDetaisViewModel generalDetails;

  public static final String SERIALIZED_NAME_OPTIONS = "options";
  @SerializedName(SERIALIZED_NAME_OPTIONS)
  private CompanyOptionViewModel options;

  public static final String SERIALIZED_NAME_REFERENCE_SETTINGS = "referenceSettings";
  @SerializedName(SERIALIZED_NAME_REFERENCE_SETTINGS)
  private CompanyReferenceSettingViewModel referenceSettings;

  public CompanySetupConfigViewModel() {
  }

  public CompanySetupConfigViewModel financialYear(CompanyFinancialYearViewModel financialYear) {
    this.financialYear = financialYear;
    return this;
  }

  /**
   * Get financialYear
   * @return financialYear
   */
  @javax.annotation.Nullable
  public CompanyFinancialYearViewModel getFinancialYear() {
    return financialYear;
  }

  public void setFinancialYear(CompanyFinancialYearViewModel financialYear) {
    this.financialYear = financialYear;
  }


  public CompanySetupConfigViewModel generalDetails(CompanyGeneralDetaisViewModel generalDetails) {
    this.generalDetails = generalDetails;
    return this;
  }

  /**
   * Get generalDetails
   * @return generalDetails
   */
  @javax.annotation.Nullable
  public CompanyGeneralDetaisViewModel getGeneralDetails() {
    return generalDetails;
  }

  public void setGeneralDetails(CompanyGeneralDetaisViewModel generalDetails) {
    this.generalDetails = generalDetails;
  }


  public CompanySetupConfigViewModel options(CompanyOptionViewModel options) {
    this.options = options;
    return this;
  }

  /**
   * Get options
   * @return options
   */
  @javax.annotation.Nullable
  public CompanyOptionViewModel getOptions() {
    return options;
  }

  public void setOptions(CompanyOptionViewModel options) {
    this.options = options;
  }


  public CompanySetupConfigViewModel referenceSettings(CompanyReferenceSettingViewModel referenceSettings) {
    this.referenceSettings = referenceSettings;
    return this;
  }

  /**
   * Get referenceSettings
   * @return referenceSettings
   */
  @javax.annotation.Nullable
  public CompanyReferenceSettingViewModel getReferenceSettings() {
    return referenceSettings;
  }

  public void setReferenceSettings(CompanyReferenceSettingViewModel referenceSettings) {
    this.referenceSettings = referenceSettings;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompanySetupConfigViewModel companySetupConfigViewModel = (CompanySetupConfigViewModel) o;
    return Objects.equals(this.financialYear, companySetupConfigViewModel.financialYear) &&
        Objects.equals(this.generalDetails, companySetupConfigViewModel.generalDetails) &&
        Objects.equals(this.options, companySetupConfigViewModel.options) &&
        Objects.equals(this.referenceSettings, companySetupConfigViewModel.referenceSettings);
  }

  @Override
  public int hashCode() {
    return Objects.hash(financialYear, generalDetails, options, referenceSettings);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompanySetupConfigViewModel {\n");
    sb.append("    financialYear: ").append(toIndentedString(financialYear)).append("\n");
    sb.append("    generalDetails: ").append(toIndentedString(generalDetails)).append("\n");
    sb.append("    options: ").append(toIndentedString(options)).append("\n");
    sb.append("    referenceSettings: ").append(toIndentedString(referenceSettings)).append("\n");
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
    openapiFields.add("financialYear");
    openapiFields.add("generalDetails");
    openapiFields.add("options");
    openapiFields.add("referenceSettings");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompanySetupConfigViewModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompanySetupConfigViewModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompanySetupConfigViewModel is not found in the empty JSON string", CompanySetupConfigViewModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompanySetupConfigViewModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompanySetupConfigViewModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `financialYear`
      if (jsonObj.get("financialYear") != null && !jsonObj.get("financialYear").isJsonNull()) {
        CompanyFinancialYearViewModel.validateJsonElement(jsonObj.get("financialYear"));
      }
      // validate the optional field `generalDetails`
      if (jsonObj.get("generalDetails") != null && !jsonObj.get("generalDetails").isJsonNull()) {
        CompanyGeneralDetaisViewModel.validateJsonElement(jsonObj.get("generalDetails"));
      }
      // validate the optional field `options`
      if (jsonObj.get("options") != null && !jsonObj.get("options").isJsonNull()) {
        CompanyOptionViewModel.validateJsonElement(jsonObj.get("options"));
      }
      // validate the optional field `referenceSettings`
      if (jsonObj.get("referenceSettings") != null && !jsonObj.get("referenceSettings").isJsonNull()) {
        CompanyReferenceSettingViewModel.validateJsonElement(jsonObj.get("referenceSettings"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompanySetupConfigViewModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompanySetupConfigViewModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompanySetupConfigViewModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompanySetupConfigViewModel.class));

       return (TypeAdapter<T>) new TypeAdapter<CompanySetupConfigViewModel>() {
           @Override
           public void write(JsonWriter out, CompanySetupConfigViewModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompanySetupConfigViewModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompanySetupConfigViewModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompanySetupConfigViewModel
   * @throws IOException if the JSON string is invalid with respect to CompanySetupConfigViewModel
   */
  public static CompanySetupConfigViewModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompanySetupConfigViewModel.class);
  }

  /**
   * Convert an instance of CompanySetupConfigViewModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

