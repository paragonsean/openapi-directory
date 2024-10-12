/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
import java.util.Arrays;
import org.openapitools.client.model.CompanyDataCompanyInterface;

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
 * CompanyCompanyRepositoryV1SavePostRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:51.810681-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CompanyCompanyRepositoryV1SavePostRequest {
  public static final String SERIALIZED_NAME_COMPANY = "company";
  @SerializedName(SERIALIZED_NAME_COMPANY)
  private CompanyDataCompanyInterface company;

  public CompanyCompanyRepositoryV1SavePostRequest() {
  }

  public CompanyCompanyRepositoryV1SavePostRequest company(CompanyDataCompanyInterface company) {
    this.company = company;
    return this;
  }

  /**
   * Get company
   * @return company
   */
  @javax.annotation.Nonnull
  public CompanyDataCompanyInterface getCompany() {
    return company;
  }

  public void setCompany(CompanyDataCompanyInterface company) {
    this.company = company;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CompanyCompanyRepositoryV1SavePostRequest companyCompanyRepositoryV1SavePostRequest = (CompanyCompanyRepositoryV1SavePostRequest) o;
    return Objects.equals(this.company, companyCompanyRepositoryV1SavePostRequest.company);
  }

  @Override
  public int hashCode() {
    return Objects.hash(company);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CompanyCompanyRepositoryV1SavePostRequest {\n");
    sb.append("    company: ").append(toIndentedString(company)).append("\n");
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
    openapiFields.add("company");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("company");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CompanyCompanyRepositoryV1SavePostRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CompanyCompanyRepositoryV1SavePostRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CompanyCompanyRepositoryV1SavePostRequest is not found in the empty JSON string", CompanyCompanyRepositoryV1SavePostRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CompanyCompanyRepositoryV1SavePostRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CompanyCompanyRepositoryV1SavePostRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CompanyCompanyRepositoryV1SavePostRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `company`
      CompanyDataCompanyInterface.validateJsonElement(jsonObj.get("company"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CompanyCompanyRepositoryV1SavePostRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CompanyCompanyRepositoryV1SavePostRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CompanyCompanyRepositoryV1SavePostRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CompanyCompanyRepositoryV1SavePostRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CompanyCompanyRepositoryV1SavePostRequest>() {
           @Override
           public void write(JsonWriter out, CompanyCompanyRepositoryV1SavePostRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CompanyCompanyRepositoryV1SavePostRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CompanyCompanyRepositoryV1SavePostRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CompanyCompanyRepositoryV1SavePostRequest
   * @throws IOException if the JSON string is invalid with respect to CompanyCompanyRepositoryV1SavePostRequest
   */
  public static CompanyCompanyRepositoryV1SavePostRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CompanyCompanyRepositoryV1SavePostRequest.class);
  }

  /**
   * Convert an instance of CompanyCompanyRepositoryV1SavePostRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

