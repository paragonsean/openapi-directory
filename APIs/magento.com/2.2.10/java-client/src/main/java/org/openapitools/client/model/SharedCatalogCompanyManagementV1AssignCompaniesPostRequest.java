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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CompanyDataCompanyInterface;

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
 * SharedCatalogCompanyManagementV1AssignCompaniesPostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SharedCatalogCompanyManagementV1AssignCompaniesPostRequest {
  public static final String SERIALIZED_NAME_COMPANIES = "companies";
  @SerializedName(SERIALIZED_NAME_COMPANIES)
  private List<CompanyDataCompanyInterface> companies = new ArrayList<>();

  public SharedCatalogCompanyManagementV1AssignCompaniesPostRequest() {
  }

  public SharedCatalogCompanyManagementV1AssignCompaniesPostRequest companies(List<CompanyDataCompanyInterface> companies) {
    this.companies = companies;
    return this;
  }

  public SharedCatalogCompanyManagementV1AssignCompaniesPostRequest addCompaniesItem(CompanyDataCompanyInterface companiesItem) {
    if (this.companies == null) {
      this.companies = new ArrayList<>();
    }
    this.companies.add(companiesItem);
    return this;
  }

  /**
   * Get companies
   * @return companies
   */
  @javax.annotation.Nonnull
  public List<CompanyDataCompanyInterface> getCompanies() {
    return companies;
  }

  public void setCompanies(List<CompanyDataCompanyInterface> companies) {
    this.companies = companies;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SharedCatalogCompanyManagementV1AssignCompaniesPostRequest sharedCatalogCompanyManagementV1AssignCompaniesPostRequest = (SharedCatalogCompanyManagementV1AssignCompaniesPostRequest) o;
    return Objects.equals(this.companies, sharedCatalogCompanyManagementV1AssignCompaniesPostRequest.companies);
  }

  @Override
  public int hashCode() {
    return Objects.hash(companies);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SharedCatalogCompanyManagementV1AssignCompaniesPostRequest {\n");
    sb.append("    companies: ").append(toIndentedString(companies)).append("\n");
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
    openapiFields.add("companies");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("companies");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SharedCatalogCompanyManagementV1AssignCompaniesPostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SharedCatalogCompanyManagementV1AssignCompaniesPostRequest is not found in the empty JSON string", SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SharedCatalogCompanyManagementV1AssignCompaniesPostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("companies").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `companies` to be an array in the JSON string but got `%s`", jsonObj.get("companies").toString()));
      }

      JsonArray jsonArraycompanies = jsonObj.getAsJsonArray("companies");
      // validate the required field `companies` (array)
      for (int i = 0; i < jsonArraycompanies.size(); i++) {
        CompanyDataCompanyInterface.validateJsonElement(jsonArraycompanies.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SharedCatalogCompanyManagementV1AssignCompaniesPostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SharedCatalogCompanyManagementV1AssignCompaniesPostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<SharedCatalogCompanyManagementV1AssignCompaniesPostRequest>() {
           @Override
           public void write(JsonWriter out, SharedCatalogCompanyManagementV1AssignCompaniesPostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SharedCatalogCompanyManagementV1AssignCompaniesPostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SharedCatalogCompanyManagementV1AssignCompaniesPostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SharedCatalogCompanyManagementV1AssignCompaniesPostRequest
   * @throws IOException if the JSON string is invalid with respect to SharedCatalogCompanyManagementV1AssignCompaniesPostRequest
   */
  public static SharedCatalogCompanyManagementV1AssignCompaniesPostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SharedCatalogCompanyManagementV1AssignCompaniesPostRequest.class);
  }

  /**
   * Convert an instance of SharedCatalogCompanyManagementV1AssignCompaniesPostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

