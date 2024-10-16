/*
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
import org.openapitools.client.model.AvailableVersions;
import org.openapitools.client.model.EpisodeSummary;
import org.openapitools.client.model.Image;
import org.openapitools.client.model.NetworkSummary;
import org.openapitools.client.model.ProgrammeTitles;

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
 * BrandSummary
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:46.845451-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BrandSummary {
  public static final String SERIALIZED_NAME_AVAILABLE_VERSIONS = "available_versions";
  @SerializedName(SERIALIZED_NAME_AVAILABLE_VERSIONS)
  private List<AvailableVersions> availableVersions = new ArrayList<>();

  public static final String SERIALIZED_NAME_IMAGES = "images";
  @SerializedName(SERIALIZED_NAME_IMAGES)
  private List<Image> images = new ArrayList<>();

  public static final String SERIALIZED_NAME_LATEST_AVAILABLE_EPISODES = "latest_available_episodes";
  @SerializedName(SERIALIZED_NAME_LATEST_AVAILABLE_EPISODES)
  private List<EpisodeSummary> latestAvailableEpisodes = new ArrayList<>();

  public static final String SERIALIZED_NAME_NETWORK_SUMMARY = "network_summary";
  @SerializedName(SERIALIZED_NAME_NETWORK_SUMMARY)
  private NetworkSummary networkSummary;

  public static final String SERIALIZED_NAME_PID = "pid";
  @SerializedName(SERIALIZED_NAME_PID)
  private String pid;

  public static final String SERIALIZED_NAME_SHORT_SYNOPSIS = "short_synopsis";
  @SerializedName(SERIALIZED_NAME_SHORT_SYNOPSIS)
  private String shortSynopsis;

  public static final String SERIALIZED_NAME_TITLES = "titles";
  @SerializedName(SERIALIZED_NAME_TITLES)
  private ProgrammeTitles titles;

  public static final String SERIALIZED_NAME_TOTAL_AVAILABLE_EPISODES = "total_available_episodes";
  @SerializedName(SERIALIZED_NAME_TOTAL_AVAILABLE_EPISODES)
  private Integer totalAvailableEpisodes;

  /**
   * Gets or Sets type
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    BRAND_SUMMARY("brand_summary");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public BrandSummary() {
  }

  public BrandSummary availableVersions(List<AvailableVersions> availableVersions) {
    this.availableVersions = availableVersions;
    return this;
  }

  public BrandSummary addAvailableVersionsItem(AvailableVersions availableVersionsItem) {
    if (this.availableVersions == null) {
      this.availableVersions = new ArrayList<>();
    }
    this.availableVersions.add(availableVersionsItem);
    return this;
  }

  /**
   * Get availableVersions
   * @return availableVersions
   */
  @javax.annotation.Nullable
  public List<AvailableVersions> getAvailableVersions() {
    return availableVersions;
  }

  public void setAvailableVersions(List<AvailableVersions> availableVersions) {
    this.availableVersions = availableVersions;
  }


  public BrandSummary images(List<Image> images) {
    this.images = images;
    return this;
  }

  public BrandSummary addImagesItem(Image imagesItem) {
    if (this.images == null) {
      this.images = new ArrayList<>();
    }
    this.images.add(imagesItem);
    return this;
  }

  /**
   * Get images
   * @return images
   */
  @javax.annotation.Nonnull
  public List<Image> getImages() {
    return images;
  }

  public void setImages(List<Image> images) {
    this.images = images;
  }


  public BrandSummary latestAvailableEpisodes(List<EpisodeSummary> latestAvailableEpisodes) {
    this.latestAvailableEpisodes = latestAvailableEpisodes;
    return this;
  }

  public BrandSummary addLatestAvailableEpisodesItem(EpisodeSummary latestAvailableEpisodesItem) {
    if (this.latestAvailableEpisodes == null) {
      this.latestAvailableEpisodes = new ArrayList<>();
    }
    this.latestAvailableEpisodes.add(latestAvailableEpisodesItem);
    return this;
  }

  /**
   * Get latestAvailableEpisodes
   * @return latestAvailableEpisodes
   */
  @javax.annotation.Nonnull
  public List<EpisodeSummary> getLatestAvailableEpisodes() {
    return latestAvailableEpisodes;
  }

  public void setLatestAvailableEpisodes(List<EpisodeSummary> latestAvailableEpisodes) {
    this.latestAvailableEpisodes = latestAvailableEpisodes;
  }


  public BrandSummary networkSummary(NetworkSummary networkSummary) {
    this.networkSummary = networkSummary;
    return this;
  }

  /**
   * Get networkSummary
   * @return networkSummary
   */
  @javax.annotation.Nonnull
  public NetworkSummary getNetworkSummary() {
    return networkSummary;
  }

  public void setNetworkSummary(NetworkSummary networkSummary) {
    this.networkSummary = networkSummary;
  }


  public BrandSummary pid(String pid) {
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


  public BrandSummary shortSynopsis(String shortSynopsis) {
    this.shortSynopsis = shortSynopsis;
    return this;
  }

  /**
   * Get shortSynopsis
   * @return shortSynopsis
   */
  @javax.annotation.Nonnull
  public String getShortSynopsis() {
    return shortSynopsis;
  }

  public void setShortSynopsis(String shortSynopsis) {
    this.shortSynopsis = shortSynopsis;
  }


  public BrandSummary titles(ProgrammeTitles titles) {
    this.titles = titles;
    return this;
  }

  /**
   * Get titles
   * @return titles
   */
  @javax.annotation.Nonnull
  public ProgrammeTitles getTitles() {
    return titles;
  }

  public void setTitles(ProgrammeTitles titles) {
    this.titles = titles;
  }


  public BrandSummary totalAvailableEpisodes(Integer totalAvailableEpisodes) {
    this.totalAvailableEpisodes = totalAvailableEpisodes;
    return this;
  }

  /**
   * Get totalAvailableEpisodes
   * @return totalAvailableEpisodes
   */
  @javax.annotation.Nonnull
  public Integer getTotalAvailableEpisodes() {
    return totalAvailableEpisodes;
  }

  public void setTotalAvailableEpisodes(Integer totalAvailableEpisodes) {
    this.totalAvailableEpisodes = totalAvailableEpisodes;
  }


  public BrandSummary type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nonnull
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
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
    BrandSummary brandSummary = (BrandSummary) o;
    return Objects.equals(this.availableVersions, brandSummary.availableVersions) &&
        Objects.equals(this.images, brandSummary.images) &&
        Objects.equals(this.latestAvailableEpisodes, brandSummary.latestAvailableEpisodes) &&
        Objects.equals(this.networkSummary, brandSummary.networkSummary) &&
        Objects.equals(this.pid, brandSummary.pid) &&
        Objects.equals(this.shortSynopsis, brandSummary.shortSynopsis) &&
        Objects.equals(this.titles, brandSummary.titles) &&
        Objects.equals(this.totalAvailableEpisodes, brandSummary.totalAvailableEpisodes) &&
        Objects.equals(this.type, brandSummary.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(availableVersions, images, latestAvailableEpisodes, networkSummary, pid, shortSynopsis, titles, totalAvailableEpisodes, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BrandSummary {\n");
    sb.append("    availableVersions: ").append(toIndentedString(availableVersions)).append("\n");
    sb.append("    images: ").append(toIndentedString(images)).append("\n");
    sb.append("    latestAvailableEpisodes: ").append(toIndentedString(latestAvailableEpisodes)).append("\n");
    sb.append("    networkSummary: ").append(toIndentedString(networkSummary)).append("\n");
    sb.append("    pid: ").append(toIndentedString(pid)).append("\n");
    sb.append("    shortSynopsis: ").append(toIndentedString(shortSynopsis)).append("\n");
    sb.append("    titles: ").append(toIndentedString(titles)).append("\n");
    sb.append("    totalAvailableEpisodes: ").append(toIndentedString(totalAvailableEpisodes)).append("\n");
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
    openapiFields.add("available_versions");
    openapiFields.add("images");
    openapiFields.add("latest_available_episodes");
    openapiFields.add("network_summary");
    openapiFields.add("pid");
    openapiFields.add("short_synopsis");
    openapiFields.add("titles");
    openapiFields.add("total_available_episodes");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("images");
    openapiRequiredFields.add("latest_available_episodes");
    openapiRequiredFields.add("network_summary");
    openapiRequiredFields.add("pid");
    openapiRequiredFields.add("short_synopsis");
    openapiRequiredFields.add("titles");
    openapiRequiredFields.add("total_available_episodes");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BrandSummary
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BrandSummary.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BrandSummary is not found in the empty JSON string", BrandSummary.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BrandSummary.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BrandSummary` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BrandSummary.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("available_versions") != null && !jsonObj.get("available_versions").isJsonNull()) {
        JsonArray jsonArrayavailableVersions = jsonObj.getAsJsonArray("available_versions");
        if (jsonArrayavailableVersions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("available_versions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `available_versions` to be an array in the JSON string but got `%s`", jsonObj.get("available_versions").toString()));
          }

          // validate the optional field `available_versions` (array)
          for (int i = 0; i < jsonArrayavailableVersions.size(); i++) {
            AvailableVersions.validateJsonElement(jsonArrayavailableVersions.get(i));
          };
        }
      }
      // ensure the json data is an array
      if (!jsonObj.get("images").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `images` to be an array in the JSON string but got `%s`", jsonObj.get("images").toString()));
      }

      JsonArray jsonArrayimages = jsonObj.getAsJsonArray("images");
      // validate the required field `images` (array)
      for (int i = 0; i < jsonArrayimages.size(); i++) {
        Image.validateJsonElement(jsonArrayimages.get(i));
      };
      // ensure the json data is an array
      if (!jsonObj.get("latest_available_episodes").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `latest_available_episodes` to be an array in the JSON string but got `%s`", jsonObj.get("latest_available_episodes").toString()));
      }

      JsonArray jsonArraylatestAvailableEpisodes = jsonObj.getAsJsonArray("latest_available_episodes");
      // validate the required field `latest_available_episodes` (array)
      for (int i = 0; i < jsonArraylatestAvailableEpisodes.size(); i++) {
        EpisodeSummary.validateJsonElement(jsonArraylatestAvailableEpisodes.get(i));
      };
      // validate the required field `network_summary`
      NetworkSummary.validateJsonElement(jsonObj.get("network_summary"));
      if (!jsonObj.get("pid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pid").toString()));
      }
      if (!jsonObj.get("short_synopsis").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `short_synopsis` to be a primitive type in the JSON string but got `%s`", jsonObj.get("short_synopsis").toString()));
      }
      // validate the required field `titles`
      ProgrammeTitles.validateJsonElement(jsonObj.get("titles"));
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the required field `type`
      TypeEnum.validateJsonElement(jsonObj.get("type"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BrandSummary.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BrandSummary' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BrandSummary> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BrandSummary.class));

       return (TypeAdapter<T>) new TypeAdapter<BrandSummary>() {
           @Override
           public void write(JsonWriter out, BrandSummary value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BrandSummary read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BrandSummary given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BrandSummary
   * @throws IOException if the JSON string is invalid with respect to BrandSummary
   */
  public static BrandSummary fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BrandSummary.class);
  }

  /**
   * Convert an instance of BrandSummary to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

