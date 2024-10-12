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
import java.time.OffsetDateTime;
import java.util.Arrays;

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
 * InventoryItem
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class InventoryItem {
  public static final String SERIALIZED_NAME_COST_PRICE = "CostPrice";
  @SerializedName(SERIALIZED_NAME_COST_PRICE)
  private Double costPrice;

  public static final String SERIALIZED_NAME_DATE_CREATED = "DateCreated";
  @SerializedName(SERIALIZED_NAME_DATE_CREATED)
  private OffsetDateTime dateCreated;

  public static final String SERIALIZED_NAME_DATE_UPDATED = "DateUpdated";
  @SerializedName(SERIALIZED_NAME_DATE_UPDATED)
  private OffsetDateTime dateUpdated;

  public static final String SERIALIZED_NAME_DESCRIPTION = "Description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_INVENTORY_ITEM_I_D = "InventoryItemID";
  @SerializedName(SERIALIZED_NAME_INVENTORY_ITEM_I_D)
  private Long inventoryItemID;

  public static final String SERIALIZED_NAME_NAME = "Name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_S_K_U = "SKU";
  @SerializedName(SERIALIZED_NAME_S_K_U)
  private String SKU;

  public static final String SERIALIZED_NAME_SALE_PRICE = "SalePrice";
  @SerializedName(SERIALIZED_NAME_SALE_PRICE)
  private Double salePrice;

  public static final String SERIALIZED_NAME_SALE_TAX_I_D_F_K = "SaleTaxIDFK";
  @SerializedName(SERIALIZED_NAME_SALE_TAX_I_D_F_K)
  private Integer saleTaxIDFK;

  public static final String SERIALIZED_NAME_IS_HIDDEN = "isHidden";
  @SerializedName(SERIALIZED_NAME_IS_HIDDEN)
  private Boolean isHidden;

  public InventoryItem() {
  }

  public InventoryItem costPrice(Double costPrice) {
    this.costPrice = costPrice;
    return this;
  }

  /**
   * Get costPrice
   * @return costPrice
   */
  @javax.annotation.Nullable
  public Double getCostPrice() {
    return costPrice;
  }

  public void setCostPrice(Double costPrice) {
    this.costPrice = costPrice;
  }


  public InventoryItem dateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
    return this;
  }

  /**
   * Get dateCreated
   * @return dateCreated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateCreated() {
    return dateCreated;
  }

  public void setDateCreated(OffsetDateTime dateCreated) {
    this.dateCreated = dateCreated;
  }


  public InventoryItem dateUpdated(OffsetDateTime dateUpdated) {
    this.dateUpdated = dateUpdated;
    return this;
  }

  /**
   * Get dateUpdated
   * @return dateUpdated
   */
  @javax.annotation.Nullable
  public OffsetDateTime getDateUpdated() {
    return dateUpdated;
  }

  public void setDateUpdated(OffsetDateTime dateUpdated) {
    this.dateUpdated = dateUpdated;
  }


  public InventoryItem description(String description) {
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


  public InventoryItem inventoryItemID(Long inventoryItemID) {
    this.inventoryItemID = inventoryItemID;
    return this;
  }

  /**
   * Get inventoryItemID
   * @return inventoryItemID
   */
  @javax.annotation.Nullable
  public Long getInventoryItemID() {
    return inventoryItemID;
  }

  public void setInventoryItemID(Long inventoryItemID) {
    this.inventoryItemID = inventoryItemID;
  }


  public InventoryItem name(String name) {
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


  public InventoryItem SKU(String SKU) {
    this.SKU = SKU;
    return this;
  }

  /**
   * Get SKU
   * @return SKU
   */
  @javax.annotation.Nullable
  public String getSKU() {
    return SKU;
  }

  public void setSKU(String SKU) {
    this.SKU = SKU;
  }


  public InventoryItem salePrice(Double salePrice) {
    this.salePrice = salePrice;
    return this;
  }

  /**
   * Get salePrice
   * @return salePrice
   */
  @javax.annotation.Nullable
  public Double getSalePrice() {
    return salePrice;
  }

  public void setSalePrice(Double salePrice) {
    this.salePrice = salePrice;
  }


  public InventoryItem saleTaxIDFK(Integer saleTaxIDFK) {
    this.saleTaxIDFK = saleTaxIDFK;
    return this;
  }

  /**
   * Get saleTaxIDFK
   * @return saleTaxIDFK
   */
  @javax.annotation.Nullable
  public Integer getSaleTaxIDFK() {
    return saleTaxIDFK;
  }

  public void setSaleTaxIDFK(Integer saleTaxIDFK) {
    this.saleTaxIDFK = saleTaxIDFK;
  }


  public InventoryItem isHidden(Boolean isHidden) {
    this.isHidden = isHidden;
    return this;
  }

  /**
   * Get isHidden
   * @return isHidden
   */
  @javax.annotation.Nullable
  public Boolean getIsHidden() {
    return isHidden;
  }

  public void setIsHidden(Boolean isHidden) {
    this.isHidden = isHidden;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InventoryItem inventoryItem = (InventoryItem) o;
    return Objects.equals(this.costPrice, inventoryItem.costPrice) &&
        Objects.equals(this.dateCreated, inventoryItem.dateCreated) &&
        Objects.equals(this.dateUpdated, inventoryItem.dateUpdated) &&
        Objects.equals(this.description, inventoryItem.description) &&
        Objects.equals(this.inventoryItemID, inventoryItem.inventoryItemID) &&
        Objects.equals(this.name, inventoryItem.name) &&
        Objects.equals(this.SKU, inventoryItem.SKU) &&
        Objects.equals(this.salePrice, inventoryItem.salePrice) &&
        Objects.equals(this.saleTaxIDFK, inventoryItem.saleTaxIDFK) &&
        Objects.equals(this.isHidden, inventoryItem.isHidden);
  }

  @Override
  public int hashCode() {
    return Objects.hash(costPrice, dateCreated, dateUpdated, description, inventoryItemID, name, SKU, salePrice, saleTaxIDFK, isHidden);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InventoryItem {\n");
    sb.append("    costPrice: ").append(toIndentedString(costPrice)).append("\n");
    sb.append("    dateCreated: ").append(toIndentedString(dateCreated)).append("\n");
    sb.append("    dateUpdated: ").append(toIndentedString(dateUpdated)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    inventoryItemID: ").append(toIndentedString(inventoryItemID)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    SKU: ").append(toIndentedString(SKU)).append("\n");
    sb.append("    salePrice: ").append(toIndentedString(salePrice)).append("\n");
    sb.append("    saleTaxIDFK: ").append(toIndentedString(saleTaxIDFK)).append("\n");
    sb.append("    isHidden: ").append(toIndentedString(isHidden)).append("\n");
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
    openapiFields.add("CostPrice");
    openapiFields.add("DateCreated");
    openapiFields.add("DateUpdated");
    openapiFields.add("Description");
    openapiFields.add("InventoryItemID");
    openapiFields.add("Name");
    openapiFields.add("SKU");
    openapiFields.add("SalePrice");
    openapiFields.add("SaleTaxIDFK");
    openapiFields.add("isHidden");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to InventoryItem
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!InventoryItem.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in InventoryItem is not found in the empty JSON string", InventoryItem.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!InventoryItem.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `InventoryItem` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("Description") != null && !jsonObj.get("Description").isJsonNull()) && !jsonObj.get("Description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Description").toString()));
      }
      if ((jsonObj.get("Name") != null && !jsonObj.get("Name").isJsonNull()) && !jsonObj.get("Name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Name").toString()));
      }
      if ((jsonObj.get("SKU") != null && !jsonObj.get("SKU").isJsonNull()) && !jsonObj.get("SKU").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `SKU` to be a primitive type in the JSON string but got `%s`", jsonObj.get("SKU").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!InventoryItem.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'InventoryItem' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<InventoryItem> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(InventoryItem.class));

       return (TypeAdapter<T>) new TypeAdapter<InventoryItem>() {
           @Override
           public void write(JsonWriter out, InventoryItem value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public InventoryItem read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of InventoryItem given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of InventoryItem
   * @throws IOException if the JSON string is invalid with respect to InventoryItem
   */
  public static InventoryItem fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, InventoryItem.class);
  }

  /**
   * Convert an instance of InventoryItem to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

