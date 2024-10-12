/*
 * Open States API v3
 *  * [More documentation](https://docs.openstates.org/en/latest/api/v3/index.html) * [Register for an account](https://openstates.org/accounts/signup/)   **We are currently working to restore experimental support for committees & events.**  During this period please note that data is not yet available for all states and the exact format of the new endpoints may change slightly depending on user feedback.  If you have any issues or questions use our [GitHub Issues](https://github.com/openstates/issues/issues) to give feedback. 
 *
 * The version of the OpenAPI document: 2021.11.12
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
import org.openapitools.client.model.Link;

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
 * EventDocument
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:35.610624-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class EventDocument {
  public static final String SERIALIZED_NAME_CLASSIFICATION = "classification";
  @SerializedName(SERIALIZED_NAME_CLASSIFICATION)
  private String classification;

  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<Link> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_NOTE = "note";
  @SerializedName(SERIALIZED_NAME_NOTE)
  private String note;

  public EventDocument() {
  }

  public EventDocument classification(String classification) {
    this.classification = classification;
    return this;
  }

  /**
   * Get classification
   * @return classification
   */
  @javax.annotation.Nonnull
  public String getClassification() {
    return classification;
  }

  public void setClassification(String classification) {
    this.classification = classification;
  }


  public EventDocument date(String date) {
    this.date = date;
    return this;
  }

  /**
   * Get date
   * @return date
   */
  @javax.annotation.Nonnull
  public String getDate() {
    return date;
  }

  public void setDate(String date) {
    this.date = date;
  }


  public EventDocument links(List<Link> links) {
    this.links = links;
    return this;
  }

  public EventDocument addLinksItem(Link linksItem) {
    if (this.links == null) {
      this.links = new ArrayList<>();
    }
    this.links.add(linksItem);
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nonnull
  public List<Link> getLinks() {
    return links;
  }

  public void setLinks(List<Link> links) {
    this.links = links;
  }


  public EventDocument note(String note) {
    this.note = note;
    return this;
  }

  /**
   * Get note
   * @return note
   */
  @javax.annotation.Nonnull
  public String getNote() {
    return note;
  }

  public void setNote(String note) {
    this.note = note;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EventDocument eventDocument = (EventDocument) o;
    return Objects.equals(this.classification, eventDocument.classification) &&
        Objects.equals(this.date, eventDocument.date) &&
        Objects.equals(this.links, eventDocument.links) &&
        Objects.equals(this.note, eventDocument.note);
  }

  @Override
  public int hashCode() {
    return Objects.hash(classification, date, links, note);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EventDocument {\n");
    sb.append("    classification: ").append(toIndentedString(classification)).append("\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    note: ").append(toIndentedString(note)).append("\n");
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
    openapiFields.add("classification");
    openapiFields.add("date");
    openapiFields.add("links");
    openapiFields.add("note");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("classification");
    openapiRequiredFields.add("date");
    openapiRequiredFields.add("links");
    openapiRequiredFields.add("note");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to EventDocument
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!EventDocument.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in EventDocument is not found in the empty JSON string", EventDocument.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!EventDocument.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `EventDocument` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : EventDocument.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("classification").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `classification` to be a primitive type in the JSON string but got `%s`", jsonObj.get("classification").toString()));
      }
      if (!jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
      // ensure the json data is an array
      if (!jsonObj.get("links").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `links` to be an array in the JSON string but got `%s`", jsonObj.get("links").toString()));
      }

      JsonArray jsonArraylinks = jsonObj.getAsJsonArray("links");
      // validate the required field `links` (array)
      for (int i = 0; i < jsonArraylinks.size(); i++) {
        Link.validateJsonElement(jsonArraylinks.get(i));
      };
      if (!jsonObj.get("note").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `note` to be a primitive type in the JSON string but got `%s`", jsonObj.get("note").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!EventDocument.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'EventDocument' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<EventDocument> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(EventDocument.class));

       return (TypeAdapter<T>) new TypeAdapter<EventDocument>() {
           @Override
           public void write(JsonWriter out, EventDocument value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public EventDocument read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of EventDocument given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of EventDocument
   * @throws IOException if the JSON string is invalid with respect to EventDocument
   */
  public static EventDocument fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, EventDocument.class);
  }

  /**
   * Convert an instance of EventDocument to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

