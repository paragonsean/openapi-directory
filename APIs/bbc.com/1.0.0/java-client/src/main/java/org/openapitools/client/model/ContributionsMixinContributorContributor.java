/*
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
import org.openapitools.client.model.ContributionsMixinContributorContributorContributor;
import org.openapitools.client.model.ContributionsMixinContributorName;

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
 * ContributionsMixinContributorContributor
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ContributionsMixinContributorContributor {
  public static final String SERIALIZED_NAME_CONTRIBUTIONS_MIXIN_CONTRIBUTOR_NAME = "contributions_mixin_contributor_name";
  @SerializedName(SERIALIZED_NAME_CONTRIBUTIONS_MIXIN_CONTRIBUTOR_NAME)
  private ContributionsMixinContributorName contributionsMixinContributorName;

  public static final String SERIALIZED_NAME_CONTRIBUTOR = "contributor";
  @SerializedName(SERIALIZED_NAME_CONTRIBUTOR)
  private ContributionsMixinContributorContributorContributor contributor;

  public static final String SERIALIZED_NAME_HREF = "href";
  @SerializedName(SERIALIZED_NAME_HREF)
  private String href;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public ContributionsMixinContributorContributor() {
  }

  public ContributionsMixinContributorContributor contributionsMixinContributorName(ContributionsMixinContributorName contributionsMixinContributorName) {
    this.contributionsMixinContributorName = contributionsMixinContributorName;
    return this;
  }

  /**
   * Get contributionsMixinContributorName
   * @return contributionsMixinContributorName
   */
  @javax.annotation.Nullable
  public ContributionsMixinContributorName getContributionsMixinContributorName() {
    return contributionsMixinContributorName;
  }

  public void setContributionsMixinContributorName(ContributionsMixinContributorName contributionsMixinContributorName) {
    this.contributionsMixinContributorName = contributionsMixinContributorName;
  }


  public ContributionsMixinContributorContributor contributor(ContributionsMixinContributorContributorContributor contributor) {
    this.contributor = contributor;
    return this;
  }

  /**
   * Get contributor
   * @return contributor
   */
  @javax.annotation.Nonnull
  public ContributionsMixinContributorContributorContributor getContributor() {
    return contributor;
  }

  public void setContributor(ContributionsMixinContributorContributorContributor contributor) {
    this.contributor = contributor;
  }


  public ContributionsMixinContributorContributor href(String href) {
    this.href = href;
    return this;
  }

  /**
   * Get href
   * @return href
   */
  @javax.annotation.Nullable
  public String getHref() {
    return href;
  }

  public void setHref(String href) {
    this.href = href;
  }


  public ContributionsMixinContributorContributor type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ContributionsMixinContributorContributor contributionsMixinContributorContributor = (ContributionsMixinContributorContributor) o;
    return Objects.equals(this.contributionsMixinContributorName, contributionsMixinContributorContributor.contributionsMixinContributorName) &&
        Objects.equals(this.contributor, contributionsMixinContributorContributor.contributor) &&
        Objects.equals(this.href, contributionsMixinContributorContributor.href) &&
        Objects.equals(this.type, contributionsMixinContributorContributor.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(contributionsMixinContributorName, contributor, href, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ContributionsMixinContributorContributor {\n");
    sb.append("    contributionsMixinContributorName: ").append(toIndentedString(contributionsMixinContributorName)).append("\n");
    sb.append("    contributor: ").append(toIndentedString(contributor)).append("\n");
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("contributions_mixin_contributor_name");
    openapiFields.add("contributor");
    openapiFields.add("href");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("contributor");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ContributionsMixinContributorContributor
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ContributionsMixinContributorContributor.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ContributionsMixinContributorContributor is not found in the empty JSON string", ContributionsMixinContributorContributor.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ContributionsMixinContributorContributor.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ContributionsMixinContributorContributor` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ContributionsMixinContributorContributor.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `contributions_mixin_contributor_name`
      if (jsonObj.get("contributions_mixin_contributor_name") != null && !jsonObj.get("contributions_mixin_contributor_name").isJsonNull()) {
        ContributionsMixinContributorName.validateJsonElement(jsonObj.get("contributions_mixin_contributor_name"));
      }
      // validate the required field `contributor`
      ContributionsMixinContributorContributorContributor.validateJsonElement(jsonObj.get("contributor"));
      if ((jsonObj.get("href") != null && !jsonObj.get("href").isJsonNull()) && !jsonObj.get("href").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `href` to be a primitive type in the JSON string but got `%s`", jsonObj.get("href").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ContributionsMixinContributorContributor.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ContributionsMixinContributorContributor' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ContributionsMixinContributorContributor> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ContributionsMixinContributorContributor.class));

       return (TypeAdapter<T>) new TypeAdapter<ContributionsMixinContributorContributor>() {
           @Override
           public void write(JsonWriter out, ContributionsMixinContributorContributor value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ContributionsMixinContributorContributor read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ContributionsMixinContributorContributor given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ContributionsMixinContributorContributor
   * @throws IOException if the JSON string is invalid with respect to ContributionsMixinContributorContributor
   */
  public static ContributionsMixinContributorContributor fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ContributionsMixinContributorContributor.class);
  }

  /**
   * Convert an instance of ContributionsMixinContributorContributor to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

