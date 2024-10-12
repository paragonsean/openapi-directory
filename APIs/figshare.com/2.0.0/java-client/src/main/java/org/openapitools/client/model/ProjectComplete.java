/*
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
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
import org.openapitools.client.model.Collaborator;
import org.openapitools.client.model.FundingInformation;

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
 * ProjectComplete
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:45.951625-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProjectComplete {
  public static final String SERIALIZED_NAME_COLLABORATORS = "collaborators";
  @SerializedName(SERIALIZED_NAME_COLLABORATORS)
  private List<Collaborator> collaborators = new ArrayList<>();

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_FIGSHARE_URL = "figshare_url";
  @SerializedName(SERIALIZED_NAME_FIGSHARE_URL)
  private String figshareUrl;

  public static final String SERIALIZED_NAME_FUNDING = "funding";
  @SerializedName(SERIALIZED_NAME_FUNDING)
  private String funding;

  public static final String SERIALIZED_NAME_FUNDING_LIST = "funding_list";
  @SerializedName(SERIALIZED_NAME_FUNDING_LIST)
  private List<FundingInformation> fundingList = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Long id;

  public static final String SERIALIZED_NAME_PUBLISHED_DATE = "published_date";
  @SerializedName(SERIALIZED_NAME_PUBLISHED_DATE)
  private String publishedDate;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_URL = "url";
  @SerializedName(SERIALIZED_NAME_URL)
  private String url;

  public ProjectComplete() {
  }

  public ProjectComplete collaborators(List<Collaborator> collaborators) {
    this.collaborators = collaborators;
    return this;
  }

  public ProjectComplete addCollaboratorsItem(Collaborator collaboratorsItem) {
    if (this.collaborators == null) {
      this.collaborators = new ArrayList<>();
    }
    this.collaborators.add(collaboratorsItem);
    return this;
  }

  /**
   * List of project collaborators
   * @return collaborators
   */
  @javax.annotation.Nonnull
  public List<Collaborator> getCollaborators() {
    return collaborators;
  }

  public void setCollaborators(List<Collaborator> collaborators) {
    this.collaborators = collaborators;
  }


  public ProjectComplete description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Project description
   * @return description
   */
  @javax.annotation.Nonnull
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ProjectComplete figshareUrl(String figshareUrl) {
    this.figshareUrl = figshareUrl;
    return this;
  }

  /**
   * Project public url
   * @return figshareUrl
   */
  @javax.annotation.Nullable
  public String getFigshareUrl() {
    return figshareUrl;
  }

  public void setFigshareUrl(String figshareUrl) {
    this.figshareUrl = figshareUrl;
  }


  public ProjectComplete funding(String funding) {
    this.funding = funding;
    return this;
  }

  /**
   * Project funding
   * @return funding
   */
  @javax.annotation.Nonnull
  public String getFunding() {
    return funding;
  }

  public void setFunding(String funding) {
    this.funding = funding;
  }


  public ProjectComplete fundingList(List<FundingInformation> fundingList) {
    this.fundingList = fundingList;
    return this;
  }

  public ProjectComplete addFundingListItem(FundingInformation fundingListItem) {
    if (this.fundingList == null) {
      this.fundingList = new ArrayList<>();
    }
    this.fundingList.add(fundingListItem);
    return this;
  }

  /**
   * Full Project funding information
   * @return fundingList
   */
  @javax.annotation.Nonnull
  public List<FundingInformation> getFundingList() {
    return fundingList;
  }

  public void setFundingList(List<FundingInformation> fundingList) {
    this.fundingList = fundingList;
  }


  public ProjectComplete id(Long id) {
    this.id = id;
    return this;
  }

  /**
   * Project id
   * @return id
   */
  @javax.annotation.Nonnull
  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }


  public ProjectComplete publishedDate(String publishedDate) {
    this.publishedDate = publishedDate;
    return this;
  }

  /**
   * Date when project was published
   * @return publishedDate
   */
  @javax.annotation.Nullable
  public String getPublishedDate() {
    return publishedDate;
  }

  public void setPublishedDate(String publishedDate) {
    this.publishedDate = publishedDate;
  }


  public ProjectComplete title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Project title
   * @return title
   */
  @javax.annotation.Nonnull
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public ProjectComplete url(String url) {
    this.url = url;
    return this;
  }

  /**
   * Api endpoint
   * @return url
   */
  @javax.annotation.Nonnull
  public String getUrl() {
    return url;
  }

  public void setUrl(String url) {
    this.url = url;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProjectComplete projectComplete = (ProjectComplete) o;
    return Objects.equals(this.collaborators, projectComplete.collaborators) &&
        Objects.equals(this.description, projectComplete.description) &&
        Objects.equals(this.figshareUrl, projectComplete.figshareUrl) &&
        Objects.equals(this.funding, projectComplete.funding) &&
        Objects.equals(this.fundingList, projectComplete.fundingList) &&
        Objects.equals(this.id, projectComplete.id) &&
        Objects.equals(this.publishedDate, projectComplete.publishedDate) &&
        Objects.equals(this.title, projectComplete.title) &&
        Objects.equals(this.url, projectComplete.url);
  }

  @Override
  public int hashCode() {
    return Objects.hash(collaborators, description, figshareUrl, funding, fundingList, id, publishedDate, title, url);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProjectComplete {\n");
    sb.append("    collaborators: ").append(toIndentedString(collaborators)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    figshareUrl: ").append(toIndentedString(figshareUrl)).append("\n");
    sb.append("    funding: ").append(toIndentedString(funding)).append("\n");
    sb.append("    fundingList: ").append(toIndentedString(fundingList)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    publishedDate: ").append(toIndentedString(publishedDate)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    url: ").append(toIndentedString(url)).append("\n");
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
    openapiFields.add("published_date");
    openapiFields.add("title");
    openapiFields.add("url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("collaborators");
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("figshare_url");
    openapiRequiredFields.add("funding");
    openapiRequiredFields.add("funding_list");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("published_date");
    openapiRequiredFields.add("title");
    openapiRequiredFields.add("url");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProjectComplete
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProjectComplete.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProjectComplete is not found in the empty JSON string", ProjectComplete.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProjectComplete.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProjectComplete` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ProjectComplete.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("collaborators").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `collaborators` to be an array in the JSON string but got `%s`", jsonObj.get("collaborators").toString()));
      }

      JsonArray jsonArraycollaborators = jsonObj.getAsJsonArray("collaborators");
      // validate the required field `collaborators` (array)
      for (int i = 0; i < jsonArraycollaborators.size(); i++) {
        Collaborator.validateJsonElement(jsonArraycollaborators.get(i));
      };
      if (!jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("figshare_url") != null && !jsonObj.get("figshare_url").isJsonNull()) && !jsonObj.get("figshare_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `figshare_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("figshare_url").toString()));
      }
      if (!jsonObj.get("funding").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `funding` to be a primitive type in the JSON string but got `%s`", jsonObj.get("funding").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("funding_list").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `funding_list` to be an array in the JSON string but got `%s`", jsonObj.get("funding_list").toString()));
      }

      JsonArray jsonArrayfundingList = jsonObj.getAsJsonArray("funding_list");
      // validate the required field `funding_list` (array)
      for (int i = 0; i < jsonArrayfundingList.size(); i++) {
        FundingInformation.validateJsonElement(jsonArrayfundingList.get(i));
      };
      if ((jsonObj.get("published_date") != null && !jsonObj.get("published_date").isJsonNull()) && !jsonObj.get("published_date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `published_date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("published_date").toString()));
      }
      if (!jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if (!jsonObj.get("url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProjectComplete.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProjectComplete' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProjectComplete> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProjectComplete.class));

       return (TypeAdapter<T>) new TypeAdapter<ProjectComplete>() {
           @Override
           public void write(JsonWriter out, ProjectComplete value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProjectComplete read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProjectComplete given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProjectComplete
   * @throws IOException if the JSON string is invalid with respect to ProjectComplete
   */
  public static ProjectComplete fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProjectComplete.class);
  }

  /**
   * Convert an instance of ProjectComplete to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

