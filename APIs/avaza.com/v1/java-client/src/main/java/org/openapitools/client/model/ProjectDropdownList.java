/*
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
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
import org.openapitools.client.model.ProjectCompanyGroup;

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
 * ProjectDropdownList
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectDropdownList {
  public static final String SERIALIZED_NAME_PAGE_SIZE = "PageSize";
  @SerializedName(SERIALIZED_NAME_PAGE_SIZE)
  private Integer pageSize;

  public static final String SERIALIZED_NAME_COMPANIES = "companies";
  @SerializedName(SERIALIZED_NAME_COMPANIES)
  private List<ProjectCompanyGroup> companies = new ArrayList<>();

  public static final String SERIALIZED_NAME_HAS_MORE = "hasMore";
  @SerializedName(SERIALIZED_NAME_HAS_MORE)
  private Boolean hasMore;

  public static final String SERIALIZED_NAME_PAGE_NUMBER = "pageNumber";
  @SerializedName(SERIALIZED_NAME_PAGE_NUMBER)
  private Integer pageNumber;

  public ProjectDropdownList() {
  }

  public ProjectDropdownList pageSize(Integer pageSize) {
    this.pageSize = pageSize;
    return this;
  }

  /**
   * Current page size
   * @return pageSize
   */
  @javax.annotation.Nullable
  public Integer getPageSize() {
    return pageSize;
  }

  public void setPageSize(Integer pageSize) {
    this.pageSize = pageSize;
  }


  public ProjectDropdownList companies(List<ProjectCompanyGroup> companies) {
    this.companies = companies;
    return this;
  }

  public ProjectDropdownList addCompaniesItem(ProjectCompanyGroup companiesItem) {
    if (this.companies == null) {
      this.companies = new ArrayList<>();
    }
    this.companies.add(companiesItem);
    return this;
  }

  /**
   * List of Projects grouped by Customer Name
   * @return companies
   */
  @javax.annotation.Nullable
  public List<ProjectCompanyGroup> getCompanies() {
    return companies;
  }

  public void setCompanies(List<ProjectCompanyGroup> companies) {
    this.companies = companies;
  }


  public ProjectDropdownList hasMore(Boolean hasMore) {
    this.hasMore = hasMore;
    return this;
  }

  /**
   * More records probably exist
   * @return hasMore
   */
  @javax.annotation.Nullable
  public Boolean getHasMore() {
    return hasMore;
  }

  public void setHasMore(Boolean hasMore) {
    this.hasMore = hasMore;
  }


  public ProjectDropdownList pageNumber(Integer pageNumber) {
    this.pageNumber = pageNumber;
    return this;
  }

  /**
   * Current page number (1 based)
   * @return pageNumber
   */
  @javax.annotation.Nullable
  public Integer getPageNumber() {
    return pageNumber;
  }

  public void setPageNumber(Integer pageNumber) {
    this.pageNumber = pageNumber;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectDropdownList projectDropdownList = (ProjectDropdownList) o;
    return Objects.equals(this.pageSize, projectDropdownList.pageSize) &&
        Objects.equals(this.companies, projectDropdownList.companies) &&
        Objects.equals(this.hasMore, projectDropdownList.hasMore) &&
        Objects.equals(this.pageNumber, projectDropdownList.pageNumber);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pageSize, companies, hasMore, pageNumber);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectDropdownList {\n");
    sb.append("    pageSize: ").append(toIndentedString(pageSize)).append("\n");
    sb.append("    companies: ").append(toIndentedString(companies)).append("\n");
    sb.append("    hasMore: ").append(toIndentedString(hasMore)).append("\n");
    sb.append("    pageNumber: ").append(toIndentedString(pageNumber)).append("\n");
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
    openapiFields.add("PageSize");
    openapiFields.add("companies");
    openapiFields.add("hasMore");
    openapiFields.add("pageNumber");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectDropdownList
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectDropdownList.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectDropdownList is not found in the empty JSON string", ProjectDropdownList.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectDropdownList.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectDropdownList` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("companies") != null && !jsonObj.get("companies").isJsonNull()) {
        JsonArray jsonArraycompanies = jsonObj.getAsJsonArray("companies");
        if (jsonArraycompanies != null) {
          // ensure the json data is an array
          if (!jsonObj.get("companies").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `companies` to be an array in the JSON string but got `%s`", jsonObj.get("companies").toString()));
          }

          // validate the optional field `companies` (array)
          for (int i = 0; i < jsonArraycompanies.size(); i++) {
            ProjectCompanyGroup.validateJsonElement(jsonArraycompanies.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectDropdownList.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectDropdownList' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectDropdownList> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectDropdownList.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectDropdownList>() {
           @Override
           public void write(JsonWriter out, ProjectDropdownList value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectDropdownList read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectDropdownList given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectDropdownList
   * @throws IOException if the JSON string is invalid with respect to ProjectDropdownList
   */
  public static ProjectDropdownList fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectDropdownList.class);
  }

  /**
   * Convert an instance of ProjectDropdownList to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

