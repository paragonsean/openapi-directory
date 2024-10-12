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
import org.openapitools.client.model.AlternateImagesMixin;
import org.openapitools.client.model.Embargoed;
import org.openapitools.client.model.ForProgrammes;
import org.openapitools.client.model.Identifiers;
import org.openapitools.client.model.Ids;
import org.openapitools.client.model.ImagesMixin;
import org.openapitools.client.model.MasterBrandLink;
import org.openapitools.client.model.RelatedLinks;
import org.openapitools.client.model.Scheduled;
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
 * GroupBody
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GroupBody {
  public static final String SERIALIZED_NAME_ALTERNATE_IMAGES_MIXIN = "alternate_images_mixin";
  @SerializedName(SERIALIZED_NAME_ALTERNATE_IMAGES_MIXIN)
  private AlternateImagesMixin alternateImagesMixin;

  public static final String SERIALIZED_NAME_EMBARGOED = "embargoed";
  @SerializedName(SERIALIZED_NAME_EMBARGOED)
  private Embargoed embargoed;

  public static final String SERIALIZED_NAME_FOR_PROGRAMMES = "for_programmes";
  @SerializedName(SERIALIZED_NAME_FOR_PROGRAMMES)
  private ForProgrammes forProgrammes;

  public static final String SERIALIZED_NAME_IDENTIFIERS = "identifiers";
  @SerializedName(SERIALIZED_NAME_IDENTIFIERS)
  private Identifiers identifiers;

  public static final String SERIALIZED_NAME_IDS = "ids";
  @SerializedName(SERIALIZED_NAME_IDS)
  private Ids ids;

  public static final String SERIALIZED_NAME_IMAGES_MIXIN = "images_mixin";
  @SerializedName(SERIALIZED_NAME_IMAGES_MIXIN)
  private ImagesMixin imagesMixin;

  public static final String SERIALIZED_NAME_MASTER_BRAND_LINK = "master_brand_link";
  @SerializedName(SERIALIZED_NAME_MASTER_BRAND_LINK)
  private MasterBrandLink masterBrandLink;

  public static final String SERIALIZED_NAME_PARTNER = "partner";
  @SerializedName(SERIALIZED_NAME_PARTNER)
  private String partner;

  public static final String SERIALIZED_NAME_PID = "pid";
  @SerializedName(SERIALIZED_NAME_PID)
  private String pid;

  public static final String SERIALIZED_NAME_RELATED_LINKS = "related_links";
  @SerializedName(SERIALIZED_NAME_RELATED_LINKS)
  private RelatedLinks relatedLinks;

  public static final String SERIALIZED_NAME_SCHEDULED = "scheduled";
  @SerializedName(SERIALIZED_NAME_SCHEDULED)
  private Scheduled scheduled;

  public static final String SERIALIZED_NAME_SYNOPSES = "synopses";
  @SerializedName(SERIALIZED_NAME_SYNOPSES)
  private Synopses synopses;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updated_time";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_URL_KEY = "url_key";
  @SerializedName(SERIALIZED_NAME_URL_KEY)
  private String urlKey;

  public GroupBody() {
  }

  public GroupBody alternateImagesMixin(AlternateImagesMixin alternateImagesMixin) {
    this.alternateImagesMixin = alternateImagesMixin;
    return this;
  }

  /**
   * Get alternateImagesMixin
   * @return alternateImagesMixin
   */
  @javax.annotation.Nullable
  public AlternateImagesMixin getAlternateImagesMixin() {
    return alternateImagesMixin;
  }

  public void setAlternateImagesMixin(AlternateImagesMixin alternateImagesMixin) {
    this.alternateImagesMixin = alternateImagesMixin;
  }


  public GroupBody embargoed(Embargoed embargoed) {
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


  public GroupBody forProgrammes(ForProgrammes forProgrammes) {
    this.forProgrammes = forProgrammes;
    return this;
  }

  /**
   * Get forProgrammes
   * @return forProgrammes
   */
  @javax.annotation.Nullable
  public ForProgrammes getForProgrammes() {
    return forProgrammes;
  }

  public void setForProgrammes(ForProgrammes forProgrammes) {
    this.forProgrammes = forProgrammes;
  }


  public GroupBody identifiers(Identifiers identifiers) {
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


  public GroupBody ids(Ids ids) {
    this.ids = ids;
    return this;
  }

  /**
   * Get ids
   * @return ids
   */
  @javax.annotation.Nullable
  public Ids getIds() {
    return ids;
  }

  public void setIds(Ids ids) {
    this.ids = ids;
  }


  public GroupBody imagesMixin(ImagesMixin imagesMixin) {
    this.imagesMixin = imagesMixin;
    return this;
  }

  /**
   * Get imagesMixin
   * @return imagesMixin
   */
  @javax.annotation.Nullable
  public ImagesMixin getImagesMixin() {
    return imagesMixin;
  }

  public void setImagesMixin(ImagesMixin imagesMixin) {
    this.imagesMixin = imagesMixin;
  }


  public GroupBody masterBrandLink(MasterBrandLink masterBrandLink) {
    this.masterBrandLink = masterBrandLink;
    return this;
  }

  /**
   * Get masterBrandLink
   * @return masterBrandLink
   */
  @javax.annotation.Nullable
  public MasterBrandLink getMasterBrandLink() {
    return masterBrandLink;
  }

  public void setMasterBrandLink(MasterBrandLink masterBrandLink) {
    this.masterBrandLink = masterBrandLink;
  }


  public GroupBody partner(String partner) {
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


  public GroupBody pid(String pid) {
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


  public GroupBody relatedLinks(RelatedLinks relatedLinks) {
    this.relatedLinks = relatedLinks;
    return this;
  }

  /**
   * Get relatedLinks
   * @return relatedLinks
   */
  @javax.annotation.Nullable
  public RelatedLinks getRelatedLinks() {
    return relatedLinks;
  }

  public void setRelatedLinks(RelatedLinks relatedLinks) {
    this.relatedLinks = relatedLinks;
  }


  public GroupBody scheduled(Scheduled scheduled) {
    this.scheduled = scheduled;
    return this;
  }

  /**
   * Get scheduled
   * @return scheduled
   */
  @javax.annotation.Nullable
  public Scheduled getScheduled() {
    return scheduled;
  }

  public void setScheduled(Scheduled scheduled) {
    this.scheduled = scheduled;
  }


  public GroupBody synopses(Synopses synopses) {
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


  public GroupBody title(String title) {
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


  public GroupBody updatedTime(OffsetDateTime updatedTime) {
    this.updatedTime = updatedTime;
    return this;
  }

  /**
   * Get updatedTime
   * @return updatedTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }

  public void setUpdatedTime(OffsetDateTime updatedTime) {
    this.updatedTime = updatedTime;
  }


  public GroupBody urlKey(String urlKey) {
    this.urlKey = urlKey;
    return this;
  }

  /**
   * Get urlKey
   * @return urlKey
   */
  @javax.annotation.Nullable
  public String getUrlKey() {
    return urlKey;
  }

  public void setUrlKey(String urlKey) {
    this.urlKey = urlKey;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GroupBody groupBody = (GroupBody) o;
    return Objects.equals(this.alternateImagesMixin, groupBody.alternateImagesMixin) &&
        Objects.equals(this.embargoed, groupBody.embargoed) &&
        Objects.equals(this.forProgrammes, groupBody.forProgrammes) &&
        Objects.equals(this.identifiers, groupBody.identifiers) &&
        Objects.equals(this.ids, groupBody.ids) &&
        Objects.equals(this.imagesMixin, groupBody.imagesMixin) &&
        Objects.equals(this.masterBrandLink, groupBody.masterBrandLink) &&
        Objects.equals(this.partner, groupBody.partner) &&
        Objects.equals(this.pid, groupBody.pid) &&
        Objects.equals(this.relatedLinks, groupBody.relatedLinks) &&
        Objects.equals(this.scheduled, groupBody.scheduled) &&
        Objects.equals(this.synopses, groupBody.synopses) &&
        Objects.equals(this.title, groupBody.title) &&
        Objects.equals(this.updatedTime, groupBody.updatedTime) &&
        Objects.equals(this.urlKey, groupBody.urlKey);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alternateImagesMixin, embargoed, forProgrammes, identifiers, ids, imagesMixin, masterBrandLink, partner, pid, relatedLinks, scheduled, synopses, title, updatedTime, urlKey);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GroupBody {\n");
    sb.append("    alternateImagesMixin: ").append(toIndentedString(alternateImagesMixin)).append("\n");
    sb.append("    embargoed: ").append(toIndentedString(embargoed)).append("\n");
    sb.append("    forProgrammes: ").append(toIndentedString(forProgrammes)).append("\n");
    sb.append("    identifiers: ").append(toIndentedString(identifiers)).append("\n");
    sb.append("    ids: ").append(toIndentedString(ids)).append("\n");
    sb.append("    imagesMixin: ").append(toIndentedString(imagesMixin)).append("\n");
    sb.append("    masterBrandLink: ").append(toIndentedString(masterBrandLink)).append("\n");
    sb.append("    partner: ").append(toIndentedString(partner)).append("\n");
    sb.append("    pid: ").append(toIndentedString(pid)).append("\n");
    sb.append("    relatedLinks: ").append(toIndentedString(relatedLinks)).append("\n");
    sb.append("    scheduled: ").append(toIndentedString(scheduled)).append("\n");
    sb.append("    synopses: ").append(toIndentedString(synopses)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    urlKey: ").append(toIndentedString(urlKey)).append("\n");
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
    openapiFields.add("alternate_images_mixin");
    openapiFields.add("embargoed");
    openapiFields.add("for_programmes");
    openapiFields.add("identifiers");
    openapiFields.add("ids");
    openapiFields.add("images_mixin");
    openapiFields.add("master_brand_link");
    openapiFields.add("partner");
    openapiFields.add("pid");
    openapiFields.add("related_links");
    openapiFields.add("scheduled");
    openapiFields.add("synopses");
    openapiFields.add("title");
    openapiFields.add("updated_time");
    openapiFields.add("url_key");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("embargoed");
    openapiRequiredFields.add("partner");
    openapiRequiredFields.add("pid");
    openapiRequiredFields.add("updated_time");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GroupBody
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GroupBody.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GroupBody is not found in the empty JSON string", GroupBody.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GroupBody.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GroupBody` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : GroupBody.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `alternate_images_mixin`
      if (jsonObj.get("alternate_images_mixin") != null && !jsonObj.get("alternate_images_mixin").isJsonNull()) {
        AlternateImagesMixin.validateJsonElement(jsonObj.get("alternate_images_mixin"));
      }
      // validate the required field `embargoed`
      Embargoed.validateJsonElement(jsonObj.get("embargoed"));
      // validate the optional field `for_programmes`
      if (jsonObj.get("for_programmes") != null && !jsonObj.get("for_programmes").isJsonNull()) {
        ForProgrammes.validateJsonElement(jsonObj.get("for_programmes"));
      }
      // validate the optional field `identifiers`
      if (jsonObj.get("identifiers") != null && !jsonObj.get("identifiers").isJsonNull()) {
        Identifiers.validateJsonElement(jsonObj.get("identifiers"));
      }
      // validate the optional field `ids`
      if (jsonObj.get("ids") != null && !jsonObj.get("ids").isJsonNull()) {
        Ids.validateJsonElement(jsonObj.get("ids"));
      }
      // validate the optional field `images_mixin`
      if (jsonObj.get("images_mixin") != null && !jsonObj.get("images_mixin").isJsonNull()) {
        ImagesMixin.validateJsonElement(jsonObj.get("images_mixin"));
      }
      // validate the optional field `master_brand_link`
      if (jsonObj.get("master_brand_link") != null && !jsonObj.get("master_brand_link").isJsonNull()) {
        MasterBrandLink.validateJsonElement(jsonObj.get("master_brand_link"));
      }
      if (!jsonObj.get("partner").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `partner` to be a primitive type in the JSON string but got `%s`", jsonObj.get("partner").toString()));
      }
      if (!jsonObj.get("pid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pid").toString()));
      }
      // validate the optional field `related_links`
      if (jsonObj.get("related_links") != null && !jsonObj.get("related_links").isJsonNull()) {
        RelatedLinks.validateJsonElement(jsonObj.get("related_links"));
      }
      // validate the optional field `scheduled`
      if (jsonObj.get("scheduled") != null && !jsonObj.get("scheduled").isJsonNull()) {
        Scheduled.validateJsonElement(jsonObj.get("scheduled"));
      }
      // validate the optional field `synopses`
      if (jsonObj.get("synopses") != null && !jsonObj.get("synopses").isJsonNull()) {
        Synopses.validateJsonElement(jsonObj.get("synopses"));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("url_key") != null && !jsonObj.get("url_key").isJsonNull()) && !jsonObj.get("url_key").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `url_key` to be a primitive type in the JSON string but got `%s`", jsonObj.get("url_key").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GroupBody.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GroupBody' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GroupBody> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GroupBody.class));

       return (TypeAdapter<T>) new TypeAdapter<GroupBody>() {
           @Override
           public void write(JsonWriter out, GroupBody value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GroupBody read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GroupBody given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GroupBody
   * @throws IOException if the JSON string is invalid with respect to GroupBody
   */
  public static GroupBody fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GroupBody.class);
  }

  /**
   * Convert an instance of GroupBody to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

