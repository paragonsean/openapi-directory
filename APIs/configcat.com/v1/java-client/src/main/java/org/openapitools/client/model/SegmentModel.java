/*
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
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
import java.util.UUID;
import org.openapitools.client.model.ProductModel;
import org.openapitools.client.model.RolloutRuleComparator;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * SegmentModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:03:46.616681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SegmentModel {
  public static final String SERIALIZED_NAME_COMPARATOR = "comparator";
  @SerializedName(SERIALIZED_NAME_COMPARATOR)
  private RolloutRuleComparator comparator;

  public static final String SERIALIZED_NAME_COMPARISON_ATTRIBUTE = "comparisonAttribute";
  @SerializedName(SERIALIZED_NAME_COMPARISON_ATTRIBUTE)
  private String comparisonAttribute;

  public static final String SERIALIZED_NAME_COMPARISON_VALUE = "comparisonValue";
  @SerializedName(SERIALIZED_NAME_COMPARISON_VALUE)
  private String comparisonValue;

  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_CREATOR_EMAIL = "creatorEmail";
  @SerializedName(SERIALIZED_NAME_CREATOR_EMAIL)
  private String creatorEmail;

  public static final String SERIALIZED_NAME_CREATOR_FULL_NAME = "creatorFullName";
  @SerializedName(SERIALIZED_NAME_CREATOR_FULL_NAME)
  private String creatorFullName;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_LAST_UPDATER_EMAIL = "lastUpdaterEmail";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATER_EMAIL)
  private String lastUpdaterEmail;

  public static final String SERIALIZED_NAME_LAST_UPDATER_FULL_NAME = "lastUpdaterFullName";
  @SerializedName(SERIALIZED_NAME_LAST_UPDATER_FULL_NAME)
  private String lastUpdaterFullName;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PRODUCT = "product";
  @SerializedName(SERIALIZED_NAME_PRODUCT)
  private ProductModel product;

  public static final String SERIALIZED_NAME_SEGMENT_ID = "segmentId";
  @SerializedName(SERIALIZED_NAME_SEGMENT_ID)
  private UUID segmentId;

  public static final String SERIALIZED_NAME_UPDATED_AT = "updatedAt";
  @SerializedName(SERIALIZED_NAME_UPDATED_AT)
  private OffsetDateTime updatedAt;

  public SegmentModel() {
  }

  public SegmentModel comparator(RolloutRuleComparator comparator) {
    this.comparator = comparator;
    return this;
  }

  /**
   * Get comparator
   * @return comparator
   */
  @javax.annotation.Nullable
  public RolloutRuleComparator getComparator() {
    return comparator;
  }

  public void setComparator(RolloutRuleComparator comparator) {
    this.comparator = comparator;
  }


  public SegmentModel comparisonAttribute(String comparisonAttribute) {
    this.comparisonAttribute = comparisonAttribute;
    return this;
  }

  /**
   * Get comparisonAttribute
   * @return comparisonAttribute
   */
  @javax.annotation.Nullable
  public String getComparisonAttribute() {
    return comparisonAttribute;
  }

  public void setComparisonAttribute(String comparisonAttribute) {
    this.comparisonAttribute = comparisonAttribute;
  }


  public SegmentModel comparisonValue(String comparisonValue) {
    this.comparisonValue = comparisonValue;
    return this;
  }

  /**
   * Get comparisonValue
   * @return comparisonValue
   */
  @javax.annotation.Nullable
  public String getComparisonValue() {
    return comparisonValue;
  }

  public void setComparisonValue(String comparisonValue) {
    this.comparisonValue = comparisonValue;
  }


  public SegmentModel createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public SegmentModel creatorEmail(String creatorEmail) {
    this.creatorEmail = creatorEmail;
    return this;
  }

  /**
   * Get creatorEmail
   * @return creatorEmail
   */
  @javax.annotation.Nullable
  public String getCreatorEmail() {
    return creatorEmail;
  }

  public void setCreatorEmail(String creatorEmail) {
    this.creatorEmail = creatorEmail;
  }


  public SegmentModel creatorFullName(String creatorFullName) {
    this.creatorFullName = creatorFullName;
    return this;
  }

  /**
   * Get creatorFullName
   * @return creatorFullName
   */
  @javax.annotation.Nullable
  public String getCreatorFullName() {
    return creatorFullName;
  }

  public void setCreatorFullName(String creatorFullName) {
    this.creatorFullName = creatorFullName;
  }


  public SegmentModel description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public SegmentModel lastUpdaterEmail(String lastUpdaterEmail) {
    this.lastUpdaterEmail = lastUpdaterEmail;
    return this;
  }

  /**
   * Get lastUpdaterEmail
   * @return lastUpdaterEmail
   */
  @javax.annotation.Nullable
  public String getLastUpdaterEmail() {
    return lastUpdaterEmail;
  }

  public void setLastUpdaterEmail(String lastUpdaterEmail) {
    this.lastUpdaterEmail = lastUpdaterEmail;
  }


  public SegmentModel lastUpdaterFullName(String lastUpdaterFullName) {
    this.lastUpdaterFullName = lastUpdaterFullName;
    return this;
  }

  /**
   * Get lastUpdaterFullName
   * @return lastUpdaterFullName
   */
  @javax.annotation.Nullable
  public String getLastUpdaterFullName() {
    return lastUpdaterFullName;
  }

  public void setLastUpdaterFullName(String lastUpdaterFullName) {
    this.lastUpdaterFullName = lastUpdaterFullName;
  }


  public SegmentModel name(String name) {
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


  public SegmentModel product(ProductModel product) {
    this.product = product;
    return this;
  }

  /**
   * Get product
   * @return product
   */
  @javax.annotation.Nullable
  public ProductModel getProduct() {
    return product;
  }

  public void setProduct(ProductModel product) {
    this.product = product;
  }


  public SegmentModel segmentId(UUID segmentId) {
    this.segmentId = segmentId;
    return this;
  }

  /**
   * Get segmentId
   * @return segmentId
   */
  @javax.annotation.Nullable
  public UUID getSegmentId() {
    return segmentId;
  }

  public void setSegmentId(UUID segmentId) {
    this.segmentId = segmentId;
  }


  public SegmentModel updatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
    return this;
  }

  /**
   * Get updatedAt
   * @return updatedAt
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedAt() {
    return updatedAt;
  }

  public void setUpdatedAt(OffsetDateTime updatedAt) {
    this.updatedAt = updatedAt;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SegmentModel segmentModel = (SegmentModel) o;
    return Objects.equals(this.comparator, segmentModel.comparator) &&
        Objects.equals(this.comparisonAttribute, segmentModel.comparisonAttribute) &&
        Objects.equals(this.comparisonValue, segmentModel.comparisonValue) &&
        Objects.equals(this.createdAt, segmentModel.createdAt) &&
        Objects.equals(this.creatorEmail, segmentModel.creatorEmail) &&
        Objects.equals(this.creatorFullName, segmentModel.creatorFullName) &&
        Objects.equals(this.description, segmentModel.description) &&
        Objects.equals(this.lastUpdaterEmail, segmentModel.lastUpdaterEmail) &&
        Objects.equals(this.lastUpdaterFullName, segmentModel.lastUpdaterFullName) &&
        Objects.equals(this.name, segmentModel.name) &&
        Objects.equals(this.product, segmentModel.product) &&
        Objects.equals(this.segmentId, segmentModel.segmentId) &&
        Objects.equals(this.updatedAt, segmentModel.updatedAt);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(comparator, comparisonAttribute, comparisonValue, createdAt, creatorEmail, creatorFullName, description, lastUpdaterEmail, lastUpdaterFullName, name, product, segmentId, updatedAt);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SegmentModel {\n");
    sb.append("    comparator: ").append(toIndentedString(comparator)).append("\n");
    sb.append("    comparisonAttribute: ").append(toIndentedString(comparisonAttribute)).append("\n");
    sb.append("    comparisonValue: ").append(toIndentedString(comparisonValue)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    creatorEmail: ").append(toIndentedString(creatorEmail)).append("\n");
    sb.append("    creatorFullName: ").append(toIndentedString(creatorFullName)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    lastUpdaterEmail: ").append(toIndentedString(lastUpdaterEmail)).append("\n");
    sb.append("    lastUpdaterFullName: ").append(toIndentedString(lastUpdaterFullName)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    product: ").append(toIndentedString(product)).append("\n");
    sb.append("    segmentId: ").append(toIndentedString(segmentId)).append("\n");
    sb.append("    updatedAt: ").append(toIndentedString(updatedAt)).append("\n");
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
    openapiFields.add("comparator");
    openapiFields.add("comparisonAttribute");
    openapiFields.add("comparisonValue");
    openapiFields.add("createdAt");
    openapiFields.add("creatorEmail");
    openapiFields.add("creatorFullName");
    openapiFields.add("description");
    openapiFields.add("lastUpdaterEmail");
    openapiFields.add("lastUpdaterFullName");
    openapiFields.add("name");
    openapiFields.add("product");
    openapiFields.add("segmentId");
    openapiFields.add("updatedAt");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SegmentModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SegmentModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SegmentModel is not found in the empty JSON string", SegmentModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SegmentModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SegmentModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `comparator`
      if (jsonObj.get("comparator") != null && !jsonObj.get("comparator").isJsonNull()) {
        RolloutRuleComparator.validateJsonElement(jsonObj.get("comparator"));
      }
      if ((jsonObj.get("comparisonAttribute") != null && !jsonObj.get("comparisonAttribute").isJsonNull()) && !jsonObj.get("comparisonAttribute").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comparisonAttribute` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comparisonAttribute").toString()));
      }
      if ((jsonObj.get("comparisonValue") != null && !jsonObj.get("comparisonValue").isJsonNull()) && !jsonObj.get("comparisonValue").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `comparisonValue` to be a primitive type in the JSON string but got `%s`", jsonObj.get("comparisonValue").toString()));
      }
      if ((jsonObj.get("creatorEmail") != null && !jsonObj.get("creatorEmail").isJsonNull()) && !jsonObj.get("creatorEmail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creatorEmail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creatorEmail").toString()));
      }
      if ((jsonObj.get("creatorFullName") != null && !jsonObj.get("creatorFullName").isJsonNull()) && !jsonObj.get("creatorFullName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `creatorFullName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("creatorFullName").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("lastUpdaterEmail") != null && !jsonObj.get("lastUpdaterEmail").isJsonNull()) && !jsonObj.get("lastUpdaterEmail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastUpdaterEmail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastUpdaterEmail").toString()));
      }
      if ((jsonObj.get("lastUpdaterFullName") != null && !jsonObj.get("lastUpdaterFullName").isJsonNull()) && !jsonObj.get("lastUpdaterFullName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastUpdaterFullName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastUpdaterFullName").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // validate the optional field `product`
      if (jsonObj.get("product") != null && !jsonObj.get("product").isJsonNull()) {
        ProductModel.validateJsonElement(jsonObj.get("product"));
      }
      if ((jsonObj.get("segmentId") != null && !jsonObj.get("segmentId").isJsonNull()) && !jsonObj.get("segmentId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `segmentId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("segmentId").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SegmentModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SegmentModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SegmentModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SegmentModel.class));

       return (TypeAdapter<T>) new TypeAdapter<SegmentModel>() {
           @Override
           public void write(JsonWriter out, SegmentModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SegmentModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SegmentModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SegmentModel
   * @throws IOException if the JSON string is invalid with respect to SegmentModel
   */
  public static SegmentModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SegmentModel.class);
  }

  /**
   * Convert an instance of SegmentModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

