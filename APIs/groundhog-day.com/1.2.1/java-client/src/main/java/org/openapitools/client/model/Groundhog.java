/*
 * Groundhog Day API
 * This API returns all of North America’s prognosticating animals and their yearly weather predictions.
 *
 * The version of the OpenAPI document: 1.2.1
 * Contact: hello@groundhog-day.com
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
import org.openapitools.client.model.Prediction;

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
 * An animal that makes an annual prediction on Groundhog Day.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:36.948560-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Groundhog {
  /**
   * Gets or Sets active
   */
  @JsonAdapter(ActiveEnum.Adapter.class)
  public enum ActiveEnum {
    NUMBER_0(0),
    
    NUMBER_1(1);

    private Integer value;

    ActiveEnum(Integer value) {
      this.value = value;
    }

    public Integer getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ActiveEnum fromValue(Integer value) {
      for (ActiveEnum b : ActiveEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ActiveEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ActiveEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ActiveEnum read(final JsonReader jsonReader) throws IOException {
        Integer value =  jsonReader.nextInt();
        return ActiveEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      Integer value = jsonElement.getAsInt();
      ActiveEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACTIVE = "active";
  @SerializedName(SERIALIZED_NAME_ACTIVE)
  private ActiveEnum active;

  public static final String SERIALIZED_NAME_CITY = "city";
  @SerializedName(SERIALIZED_NAME_CITY)
  private String city;

  public static final String SERIALIZED_NAME_CONTACT = "contact";
  @SerializedName(SERIALIZED_NAME_CONTACT)
  private String contact;

  public static final String SERIALIZED_NAME_COORDINATES = "coordinates";
  @SerializedName(SERIALIZED_NAME_COORDINATES)
  private String coordinates;

  public static final String SERIALIZED_NAME_COUNTRY = "country";
  @SerializedName(SERIALIZED_NAME_COUNTRY)
  private String country;

  public static final String SERIALIZED_NAME_CURRENT_PREDICTION = "currentPrediction";
  @SerializedName(SERIALIZED_NAME_CURRENT_PREDICTION)
  private String currentPrediction;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IMAGE = "image";
  @SerializedName(SERIALIZED_NAME_IMAGE)
  private String image;

  public static final String SERIALIZED_NAME_IS_GROUNDHOG = "isGroundhog";
  @SerializedName(SERIALIZED_NAME_IS_GROUNDHOG)
  private Integer isGroundhog;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PREDICTIONS = "predictions";
  @SerializedName(SERIALIZED_NAME_PREDICTIONS)
  private List<Prediction> predictions = new ArrayList<>();

  public static final String SERIALIZED_NAME_PREDICTIONS_COUNT = "predictionsCount";
  @SerializedName(SERIALIZED_NAME_PREDICTIONS_COUNT)
  private Integer predictionsCount;

  public static final String SERIALIZED_NAME_REGION = "region";
  @SerializedName(SERIALIZED_NAME_REGION)
  private String region;

  public static final String SERIALIZED_NAME_SHORTNAME = "shortname";
  @SerializedName(SERIALIZED_NAME_SHORTNAME)
  private String shortname;

  public static final String SERIALIZED_NAME_SLUG = "slug";
  @SerializedName(SERIALIZED_NAME_SLUG)
  private String slug;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public Groundhog() {
  }

  public Groundhog active(ActiveEnum active) {
    this.active = active;
    return this;
  }

  /**
   * Get active
   * minimum: 0
   * maximum: 1
   * @return active
   */
  @javax.annotation.Nonnull
  public ActiveEnum getActive() {
    return active;
  }

  public void setActive(ActiveEnum active) {
    this.active = active;
  }


  public Groundhog city(String city) {
    this.city = city;
    return this;
  }

  /**
   * Get city
   * @return city
   */
  @javax.annotation.Nonnull
  public String getCity() {
    return city;
  }

  public void setCity(String city) {
    this.city = city;
  }


  public Groundhog contact(String contact) {
    this.contact = contact;
    return this;
  }

  /**
   * Get contact
   * @return contact
   */
  @javax.annotation.Nonnull
  public String getContact() {
    return contact;
  }

  public void setContact(String contact) {
    this.contact = contact;
  }


  public Groundhog coordinates(String coordinates) {
    this.coordinates = coordinates;
    return this;
  }

  /**
   * Get coordinates
   * @return coordinates
   */
  @javax.annotation.Nonnull
  public String getCoordinates() {
    return coordinates;
  }

  public void setCoordinates(String coordinates) {
    this.coordinates = coordinates;
  }


  public Groundhog country(String country) {
    this.country = country;
    return this;
  }

  /**
   * Get country
   * @return country
   */
  @javax.annotation.Nonnull
  public String getCountry() {
    return country;
  }

  public void setCountry(String country) {
    this.country = country;
  }


  public Groundhog currentPrediction(String currentPrediction) {
    this.currentPrediction = currentPrediction;
    return this;
  }

  /**
   * Get currentPrediction
   * @return currentPrediction
   */
  @javax.annotation.Nonnull
  public String getCurrentPrediction() {
    return currentPrediction;
  }

  public void setCurrentPrediction(String currentPrediction) {
    this.currentPrediction = currentPrediction;
  }


  public Groundhog description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nonnull
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Groundhog id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * minimum: 1
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public Groundhog image(String image) {
    this.image = image;
    return this;
  }

  /**
   * Get image
   * @return image
   */
  @javax.annotation.Nonnull
  public String getImage() {
    return image;
  }

  public void setImage(String image) {
    this.image = image;
  }


  public Groundhog isGroundhog(Integer isGroundhog) {
    this.isGroundhog = isGroundhog;
    return this;
  }

  /**
   * Get isGroundhog
   * minimum: 0
   * maximum: 1
   * @return isGroundhog
   */
  @javax.annotation.Nonnull
  public Integer getIsGroundhog() {
    return isGroundhog;
  }

  public void setIsGroundhog(Integer isGroundhog) {
    this.isGroundhog = isGroundhog;
  }


  public Groundhog name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Groundhog predictions(List<Prediction> predictions) {
    this.predictions = predictions;
    return this;
  }

  public Groundhog addPredictionsItem(Prediction predictionsItem) {
    if (this.predictions == null) {
      this.predictions = new ArrayList<>();
    }
    this.predictions.add(predictionsItem);
    return this;
  }

  /**
   * Get predictions
   * @return predictions
   */
  @javax.annotation.Nullable
  public List<Prediction> getPredictions() {
    return predictions;
  }

  public void setPredictions(List<Prediction> predictions) {
    this.predictions = predictions;
  }


  public Groundhog predictionsCount(Integer predictionsCount) {
    this.predictionsCount = predictionsCount;
    return this;
  }

  /**
   * All predictions, excluding nulls.
   * minimum: 1
   * @return predictionsCount
   */
  @javax.annotation.Nullable
  public Integer getPredictionsCount() {
    return predictionsCount;
  }

  public void setPredictionsCount(Integer predictionsCount) {
    this.predictionsCount = predictionsCount;
  }


  public Groundhog region(String region) {
    this.region = region;
    return this;
  }

  /**
   * Get region
   * @return region
   */
  @javax.annotation.Nonnull
  public String getRegion() {
    return region;
  }

  public void setRegion(String region) {
    this.region = region;
  }


  public Groundhog shortname(String shortname) {
    this.shortname = shortname;
    return this;
  }

  /**
   * Get shortname
   * @return shortname
   */
  @javax.annotation.Nonnull
  public String getShortname() {
    return shortname;
  }

  public void setShortname(String shortname) {
    this.shortname = shortname;
  }


  public Groundhog slug(String slug) {
    this.slug = slug;
    return this;
  }

  /**
   * Get slug
   * @return slug
   */
  @javax.annotation.Nonnull
  public String getSlug() {
    return slug;
  }

  public void setSlug(String slug) {
    this.slug = slug;
  }


  public Groundhog source(String source) {
    this.source = source;
    return this;
  }

  /**
   * Get source
   * @return source
   */
  @javax.annotation.Nonnull
  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }


  public Groundhog type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Get type
   * @return type
   */
  @javax.annotation.Nonnull
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
    Groundhog groundhog = (Groundhog) o;
    return Objects.equals(this.active, groundhog.active) &&
        Objects.equals(this.city, groundhog.city) &&
        Objects.equals(this.contact, groundhog.contact) &&
        Objects.equals(this.coordinates, groundhog.coordinates) &&
        Objects.equals(this.country, groundhog.country) &&
        Objects.equals(this.currentPrediction, groundhog.currentPrediction) &&
        Objects.equals(this.description, groundhog.description) &&
        Objects.equals(this.id, groundhog.id) &&
        Objects.equals(this.image, groundhog.image) &&
        Objects.equals(this.isGroundhog, groundhog.isGroundhog) &&
        Objects.equals(this.name, groundhog.name) &&
        Objects.equals(this.predictions, groundhog.predictions) &&
        Objects.equals(this.predictionsCount, groundhog.predictionsCount) &&
        Objects.equals(this.region, groundhog.region) &&
        Objects.equals(this.shortname, groundhog.shortname) &&
        Objects.equals(this.slug, groundhog.slug) &&
        Objects.equals(this.source, groundhog.source) &&
        Objects.equals(this.type, groundhog.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(active, city, contact, coordinates, country, currentPrediction, description, id, image, isGroundhog, name, predictions, predictionsCount, region, shortname, slug, source, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Groundhog {\n");
    sb.append("    active: ").append(toIndentedString(active)).append("\n");
    sb.append("    city: ").append(toIndentedString(city)).append("\n");
    sb.append("    contact: ").append(toIndentedString(contact)).append("\n");
    sb.append("    coordinates: ").append(toIndentedString(coordinates)).append("\n");
    sb.append("    country: ").append(toIndentedString(country)).append("\n");
    sb.append("    currentPrediction: ").append(toIndentedString(currentPrediction)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    image: ").append(toIndentedString(image)).append("\n");
    sb.append("    isGroundhog: ").append(toIndentedString(isGroundhog)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    predictions: ").append(toIndentedString(predictions)).append("\n");
    sb.append("    predictionsCount: ").append(toIndentedString(predictionsCount)).append("\n");
    sb.append("    region: ").append(toIndentedString(region)).append("\n");
    sb.append("    shortname: ").append(toIndentedString(shortname)).append("\n");
    sb.append("    slug: ").append(toIndentedString(slug)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
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
    openapiFields.add("active");
    openapiFields.add("city");
    openapiFields.add("contact");
    openapiFields.add("coordinates");
    openapiFields.add("country");
    openapiFields.add("currentPrediction");
    openapiFields.add("description");
    openapiFields.add("id");
    openapiFields.add("image");
    openapiFields.add("isGroundhog");
    openapiFields.add("name");
    openapiFields.add("predictions");
    openapiFields.add("predictionsCount");
    openapiFields.add("region");
    openapiFields.add("shortname");
    openapiFields.add("slug");
    openapiFields.add("source");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("active");
    openapiRequiredFields.add("city");
    openapiRequiredFields.add("contact");
    openapiRequiredFields.add("coordinates");
    openapiRequiredFields.add("country");
    openapiRequiredFields.add("currentPrediction");
    openapiRequiredFields.add("description");
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("image");
    openapiRequiredFields.add("isGroundhog");
    openapiRequiredFields.add("name");
    openapiRequiredFields.add("region");
    openapiRequiredFields.add("shortname");
    openapiRequiredFields.add("slug");
    openapiRequiredFields.add("source");
    openapiRequiredFields.add("type");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Groundhog
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Groundhog.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Groundhog is not found in the empty JSON string", Groundhog.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Groundhog.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Groundhog` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Groundhog.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `active`
      ActiveEnum.validateJsonElement(jsonObj.get("active"));
      if (!jsonObj.get("city").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city").toString()));
      }
      if (!jsonObj.get("contact").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact").toString()));
      }
      if (!jsonObj.get("coordinates").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `coordinates` to be a primitive type in the JSON string but got `%s`", jsonObj.get("coordinates").toString()));
      }
      if (!jsonObj.get("country").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `country` to be a primitive type in the JSON string but got `%s`", jsonObj.get("country").toString()));
      }
      if (!jsonObj.get("currentPrediction").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currentPrediction` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currentPrediction").toString()));
      }
      if (!jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if (!jsonObj.get("image").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `image` to be a primitive type in the JSON string but got `%s`", jsonObj.get("image").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if (jsonObj.get("predictions") != null && !jsonObj.get("predictions").isJsonNull()) {
        JsonArray jsonArraypredictions = jsonObj.getAsJsonArray("predictions");
        if (jsonArraypredictions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("predictions").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `predictions` to be an array in the JSON string but got `%s`", jsonObj.get("predictions").toString()));
          }

          // validate the optional field `predictions` (array)
          for (int i = 0; i < jsonArraypredictions.size(); i++) {
            Prediction.validateJsonElement(jsonArraypredictions.get(i));
          };
        }
      }
      if (!jsonObj.get("region").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `region` to be a primitive type in the JSON string but got `%s`", jsonObj.get("region").toString()));
      }
      if (!jsonObj.get("shortname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shortname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shortname").toString()));
      }
      if (!jsonObj.get("slug").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `slug` to be a primitive type in the JSON string but got `%s`", jsonObj.get("slug").toString()));
      }
      if (!jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      if (!jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Groundhog.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Groundhog' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Groundhog> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Groundhog.class));

       return (TypeAdapter<T>) new TypeAdapter<Groundhog>() {
           @Override
           public void write(JsonWriter out, Groundhog value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Groundhog read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Groundhog given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Groundhog
   * @throws IOException if the JSON string is invalid with respect to Groundhog
   */
  public static Groundhog fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Groundhog.class);
  }

  /**
   * Convert an instance of Groundhog to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

