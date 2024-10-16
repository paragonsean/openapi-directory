/*
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.FormField;
import org.openapitools.client.model.Tag;

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
 * FormSubmission
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:26.140477-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class FormSubmission {
  public static final String SERIALIZED_NAME_CALL_TO_ACTION = "callToAction";
  @SerializedName(SERIALIZED_NAME_CALL_TO_ACTION)
  private String callToAction;

  public static final String SERIALIZED_NAME_CSS_URL = "cssUrl";
  @SerializedName(SERIALIZED_NAME_CSS_URL)
  private String cssUrl;

  public static final String SERIALIZED_NAME_FIELDS = "fields";
  @SerializedName(SERIALIZED_NAME_FIELDS)
  private List<FormField> fields = new ArrayList<>();

  public static final String SERIALIZED_NAME_HEADING = "heading";
  @SerializedName(SERIALIZED_NAME_HEADING)
  private String heading;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NO_CSS = "noCss";
  @SerializedName(SERIALIZED_NAME_NO_CSS)
  private Boolean noCss;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<Tag> tags = new ArrayList<>();

  public FormSubmission() {
  }

  public FormSubmission callToAction(String callToAction) {
    this.callToAction = callToAction;
    return this;
  }

  /**
   * Get callToAction
   * @return callToAction
   */
  @javax.annotation.Nullable
  public String getCallToAction() {
    return callToAction;
  }

  public void setCallToAction(String callToAction) {
    this.callToAction = callToAction;
  }


  public FormSubmission cssUrl(String cssUrl) {
    this.cssUrl = cssUrl;
    return this;
  }

  /**
   * Get cssUrl
   * @return cssUrl
   */
  @javax.annotation.Nullable
  public String getCssUrl() {
    return cssUrl;
  }

  public void setCssUrl(String cssUrl) {
    this.cssUrl = cssUrl;
  }


  public FormSubmission fields(List<FormField> fields) {
    this.fields = fields;
    return this;
  }

  public FormSubmission addFieldsItem(FormField fieldsItem) {
    if (this.fields == null) {
      this.fields = new ArrayList<>();
    }
    this.fields.add(fieldsItem);
    return this;
  }

  /**
   * Get fields
   * @return fields
   */
  @javax.annotation.Nullable
  public List<FormField> getFields() {
    return fields;
  }

  public void setFields(List<FormField> fields) {
    this.fields = fields;
  }


  public FormSubmission heading(String heading) {
    this.heading = heading;
    return this;
  }

  /**
   * Get heading
   * @return heading
   */
  @javax.annotation.Nullable
  public String getHeading() {
    return heading;
  }

  public void setHeading(String heading) {
    this.heading = heading;
  }


  public FormSubmission name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public FormSubmission noCss(Boolean noCss) {
    this.noCss = noCss;
    return this;
  }

  /**
   * Get noCss
   * @return noCss
   */
  @javax.annotation.Nullable
  public Boolean getNoCss() {
    return noCss;
  }

  public void setNoCss(Boolean noCss) {
    this.noCss = noCss;
  }


  public FormSubmission tags(List<Tag> tags) {
    this.tags = tags;
    return this;
  }

  public FormSubmission addTagsItem(Tag tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * Get tags
   * @return tags
   */
  @javax.annotation.Nullable
  public List<Tag> getTags() {
    return tags;
  }

  public void setTags(List<Tag> tags) {
    this.tags = tags;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FormSubmission formSubmission = (FormSubmission) o;
    return Objects.equals(this.callToAction, formSubmission.callToAction) &&
        Objects.equals(this.cssUrl, formSubmission.cssUrl) &&
        Objects.equals(this.fields, formSubmission.fields) &&
        Objects.equals(this.heading, formSubmission.heading) &&
        Objects.equals(this.name, formSubmission.name) &&
        Objects.equals(this.noCss, formSubmission.noCss) &&
        Objects.equals(this.tags, formSubmission.tags);
  }

  @Override
  public int hashCode() {
    return Objects.hash(callToAction, cssUrl, fields, heading, name, noCss, tags);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FormSubmission {\n");
    sb.append("    callToAction: ").append(toIndentedString(callToAction)).append("\n");
    sb.append("    cssUrl: ").append(toIndentedString(cssUrl)).append("\n");
    sb.append("    fields: ").append(toIndentedString(fields)).append("\n");
    sb.append("    heading: ").append(toIndentedString(heading)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    noCss: ").append(toIndentedString(noCss)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
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
    openapiFields.add("callToAction");
    openapiFields.add("cssUrl");
    openapiFields.add("fields");
    openapiFields.add("heading");
    openapiFields.add("name");
    openapiFields.add("noCss");
    openapiFields.add("tags");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to FormSubmission
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!FormSubmission.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in FormSubmission is not found in the empty JSON string", FormSubmission.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!FormSubmission.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `FormSubmission` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("callToAction") != null && !jsonObj.get("callToAction").isJsonNull()) && !jsonObj.get("callToAction").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `callToAction` to be a primitive type in the JSON string but got `%s`", jsonObj.get("callToAction").toString()));
      }
      if ((jsonObj.get("cssUrl") != null && !jsonObj.get("cssUrl").isJsonNull()) && !jsonObj.get("cssUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `cssUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("cssUrl").toString()));
      }
      if (jsonObj.get("fields") != null && !jsonObj.get("fields").isJsonNull()) {
        JsonArray jsonArrayfields = jsonObj.getAsJsonArray("fields");
        if (jsonArrayfields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `fields` to be an array in the JSON string but got `%s`", jsonObj.get("fields").toString()));
          }

          // validate the optional field `fields` (array)
          for (int i = 0; i < jsonArrayfields.size(); i++) {
            FormField.validateJsonElement(jsonArrayfields.get(i));
          };
        }
      }
      if ((jsonObj.get("heading") != null && !jsonObj.get("heading").isJsonNull()) && !jsonObj.get("heading").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `heading` to be a primitive type in the JSON string but got `%s`", jsonObj.get("heading").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull()) {
        JsonArray jsonArraytags = jsonObj.getAsJsonArray("tags");
        if (jsonArraytags != null) {
          // ensure the json data is an array
          if (!jsonObj.get("tags").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
          }

          // validate the optional field `tags` (array)
          for (int i = 0; i < jsonArraytags.size(); i++) {
            Tag.validateJsonElement(jsonArraytags.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!FormSubmission.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'FormSubmission' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<FormSubmission> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(FormSubmission.class));

       return (TypeAdapter<T>) new TypeAdapter<FormSubmission>() {
           @Override
           public void write(JsonWriter out, FormSubmission value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public FormSubmission read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of FormSubmission given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of FormSubmission
   * @throws IOException if the JSON string is invalid with respect to FormSubmission
   */
  public static FormSubmission fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, FormSubmission.class);
  }

  /**
   * Convert an instance of FormSubmission to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

