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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.Embargoed;
import org.openapitools.client.model.Identifiers;
import org.openapitools.client.model.SourceAsset;
import org.openapitools.client.model.Synopses;

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
 * Image
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Image {
  public static final String SERIALIZED_NAME_AUTHOR = "author";
  @SerializedName(SERIALIZED_NAME_AUTHOR)
  private String author;

  public static final String SERIALIZED_NAME_EMBARGOED = "embargoed";
  @SerializedName(SERIALIZED_NAME_EMBARGOED)
  private Embargoed embargoed;

  public static final String SERIALIZED_NAME_IDENTIFIERS = "identifiers";
  @SerializedName(SERIALIZED_NAME_IDENTIFIERS)
  private Identifiers identifiers;

  public static final String SERIALIZED_NAME_PARTNER = "partner";
  @SerializedName(SERIALIZED_NAME_PARTNER)
  private String partner;

  public static final String SERIALIZED_NAME_PID = "pid";
  @SerializedName(SERIALIZED_NAME_PID)
  private String pid;

  public static final String SERIALIZED_NAME_SHOOT_DATE = "shoot_date";
  @SerializedName(SERIALIZED_NAME_SHOOT_DATE)
  private OffsetDateTime shootDate;

  public static final String SERIALIZED_NAME_SOURCE_ASSET = "source_asset";
  @SerializedName(SERIALIZED_NAME_SOURCE_ASSET)
  private SourceAsset sourceAsset;

  public static final String SERIALIZED_NAME_SYNOPSES = "synopses";
  @SerializedName(SERIALIZED_NAME_SYNOPSES)
  private Synopses synopses;

  public static final String SERIALIZED_NAME_TEMPLATE_URL = "template_url";
  @SerializedName(SERIALIZED_NAME_TEMPLATE_URL)
  private String templateUrl;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Image() {
  }

  public Image author(String author) {
    this.author = author;
    return this;
  }

  /**
   * Get author
   * @return author
   */
  @javax.annotation.Nullable
  public String getAuthor() {
    return author;
  }

  public void setAuthor(String author) {
    this.author = author;
  }


  public Image embargoed(Embargoed embargoed) {
    this.embargoed = embargoed;
    return this;
  }

  /**
   * Get embargoed
   * @return embargoed
   */
  @javax.annotation.Nonnull
  public Embargoed getEmbargoed() {
    return embargoed;
  }

  public void setEmbargoed(Embargoed embargoed) {
    this.embargoed = embargoed;
  }


  public Image identifiers(Identifiers identifiers) {
    this.identifiers = identifiers;
    return this;
  }

  /**
   * Get identifiers
   * @return identifiers
   */
  @javax.annotation.Nullable
  public Identifiers getIdentifiers() {
    return identifiers;
  }

  public void setIdentifiers(Identifiers identifiers) {
    this.identifiers = identifiers;
  }


  public Image partner(String partner) {
    this.partner = partner;
    return this;
  }

  /**
   * Get partner
   * @return partner
   */
  @javax.annotation.Nonnull
  public String getPartner() {
    return partner;
  }

  public void setPartner(String partner) {
    this.partner = partner;
  }


  public Image pid(String pid) {
    this.pid = pid;
    return this;
  }

  /**
   * Get pid
   * @return pid
   */
  @javax.annotation.Nonnull
  public String getPid() {
    return pid;
  }

  public void setPid(String pid) {
    this.pid = pid;
  }


  public Image shootDate(OffsetDateTime shootDate) {
    this.shootDate = shootDate;
    return this;
  }

  /**
   * Get shootDate
   * @return shootDate
   */
  @javax.annotation.Nullable
  public OffsetDateTime getShootDate() {
    return shootDate;
  }

  public void setShootDate(OffsetDateTime shootDate) {
    this.shootDate = shootDate;
  }


  public Image sourceAsset(SourceAsset sourceAsset) {
    this.sourceAsset = sourceAsset;
    return this;
  }

  /**
   * Get sourceAsset
   * @return sourceAsset
   */
  @javax.annotation.Nullable
  public SourceAsset getSourceAsset() {
    return sourceAsset;
  }

  public void setSourceAsset(SourceAsset sourceAsset) {
    this.sourceAsset = sourceAsset;
  }


  public Image synopses(Synopses synopses) {
    this.synopses = synopses;
    return this;
  }

  /**
   * Get synopses
   * @return synopses
   */
  @javax.annotation.Nullable
  public Synopses getSynopses() {
    return synopses;
  }

  public void setSynopses(Synopses synopses) {
    this.synopses = synopses;
  }


  public Image templateUrl(String templateUrl) {
    this.templateUrl = templateUrl;
    return this;
  }

  /**
   * Get templateUrl
   * @return templateUrl
   */
  @javax.annotation.Nullable
  public String getTemplateUrl() {
    return templateUrl;
  }

  public void setTemplateUrl(String templateUrl) {
    this.templateUrl = templateUrl;
  }


  public Image title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Image type(String type) {
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
    Image image = (Image) o;
    return Objects.equals(this.author, image.author) &&
        Objects.equals(this.embargoed, image.embargoed) &&
        Objects.equals(this.identifiers, image.identifiers) &&
        Objects.equals(this.partner, image.partner) &&
        Objects.equals(this.pid, image.pid) &&
        Objects.equals(this.shootDate, image.shootDate) &&
        Objects.equals(this.sourceAsset, image.sourceAsset) &&
        Objects.equals(this.synopses, image.synopses) &&
        Objects.equals(this.templateUrl, image.templateUrl) &&
        Objects.equals(this.title, image.title) &&
        Objects.equals(this.type, image.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(author, embargoed, identifiers, partner, pid, shootDate, sourceAsset, synopses, templateUrl, title, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Image {\n");
    sb.append("    author: ").append(toIndentedString(author)).append("\n");
    sb.append("    embargoed: ").append(toIndentedString(embargoed)).append("\n");
    sb.append("    identifiers: ").append(toIndentedString(identifiers)).append("\n");
    sb.append("    partner: ").append(toIndentedString(partner)).append("\n");
    sb.append("    pid: ").append(toIndentedString(pid)).append("\n");
    sb.append("    shootDate: ").append(toIndentedString(shootDate)).append("\n");
    sb.append("    sourceAsset: ").append(toIndentedString(sourceAsset)).append("\n");
    sb.append("    synopses: ").append(toIndentedString(synopses)).append("\n");
    sb.append("    templateUrl: ").append(toIndentedString(templateUrl)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("author");
    openapiFields.add("embargoed");
    openapiFields.add("identifiers");
    openapiFields.add("partner");
    openapiFields.add("pid");
    openapiFields.add("shoot_date");
    openapiFields.add("source_asset");
    openapiFields.add("synopses");
    openapiFields.add("template_url");
    openapiFields.add("title");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("embargoed");
    openapiRequiredFields.add("partner");
    openapiRequiredFields.add("pid");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Image
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Image.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Image is not found in the empty JSON string", Image.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Image.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Image` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Image.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("author") != null && !jsonObj.get("author").isJsonNull()) && !jsonObj.get("author").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `author` to be a primitive type in the JSON string but got `%s`", jsonObj.get("author").toString()));
      }
      // validate the required field `embargoed`
      Embargoed.validateJsonElement(jsonObj.get("embargoed"));
      // validate the optional field `identifiers`
      if (jsonObj.get("identifiers") != null && !jsonObj.get("identifiers").isJsonNull()) {
        Identifiers.validateJsonElement(jsonObj.get("identifiers"));
      }
      if (!jsonObj.get("partner").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `partner` to be a primitive type in the JSON string but got `%s`", jsonObj.get("partner").toString()));
      }
      if (!jsonObj.get("pid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pid").toString()));
      }
      // validate the optional field `source_asset`
      if (jsonObj.get("source_asset") != null && !jsonObj.get("source_asset").isJsonNull()) {
        SourceAsset.validateJsonElement(jsonObj.get("source_asset"));
      }
      // validate the optional field `synopses`
      if (jsonObj.get("synopses") != null && !jsonObj.get("synopses").isJsonNull()) {
        Synopses.validateJsonElement(jsonObj.get("synopses"));
      }
      if ((jsonObj.get("template_url") != null && !jsonObj.get("template_url").isJsonNull()) && !jsonObj.get("template_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `template_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("template_url").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Image.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Image' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Image> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Image.class));

       return (TypeAdapter<T>) new TypeAdapter<Image>() {
           @Override
           public void write(JsonWriter out, Image value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Image read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Image given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Image
   * @throws IOException if the JSON string is invalid with respect to Image
   */
  public static Image fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Image.class);
  }

  /**
   * Convert an instance of Image to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

