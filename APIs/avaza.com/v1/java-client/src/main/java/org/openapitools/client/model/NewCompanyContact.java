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
 * NewCompanyContact
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:56.431364-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NewCompanyContact {
  public static final String SERIALIZED_NAME_COMPANY_BILLING_ADDRESS = "CompanyBillingAddress";
  @SerializedName(SERIALIZED_NAME_COMPANY_BILLING_ADDRESS)
  private String companyBillingAddress;

  public static final String SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_CITY = "CompanyBillingAddressCity";
  @SerializedName(SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_CITY)
  private String companyBillingAddressCity;

  public static final String SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_COUNTRY_CODE = "CompanyBillingAddressCountryCode";
  @SerializedName(SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_COUNTRY_CODE)
  private String companyBillingAddressCountryCode;

  public static final String SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_LINE = "CompanyBillingAddressLine";
  @SerializedName(SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_LINE)
  private String companyBillingAddressLine;

  public static final String SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_POST_CODE = "CompanyBillingAddressPostCode";
  @SerializedName(SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_POST_CODE)
  private String companyBillingAddressPostCode;

  public static final String SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_STATE = "CompanyBillingAddressState";
  @SerializedName(SERIALIZED_NAME_COMPANY_BILLING_ADDRESS_STATE)
  private String companyBillingAddressState;

  public static final String SERIALIZED_NAME_COMPANY_I_D_F_K = "CompanyIDFK";
  @SerializedName(SERIALIZED_NAME_COMPANY_I_D_F_K)
  private Integer companyIDFK;

  public static final String SERIALIZED_NAME_COMPANY_NAME = "CompanyName";
  @SerializedName(SERIALIZED_NAME_COMPANY_NAME)
  private String companyName;

  public static final String SERIALIZED_NAME_CONTACT_EMAIL = "ContactEmail";
  @SerializedName(SERIALIZED_NAME_CONTACT_EMAIL)
  private String contactEmail;

  public static final String SERIALIZED_NAME_CURRENCY_CODE = "CurrencyCode";
  @SerializedName(SERIALIZED_NAME_CURRENCY_CODE)
  private String currencyCode;

  public static final String SERIALIZED_NAME_FIRSTNAME = "Firstname";
  @SerializedName(SERIALIZED_NAME_FIRSTNAME)
  private String firstname;

  public static final String SERIALIZED_NAME_LASTNAME = "Lastname";
  @SerializedName(SERIALIZED_NAME_LASTNAME)
  private String lastname;

  public static final String SERIALIZED_NAME_MOBILE = "Mobile";
  @SerializedName(SERIALIZED_NAME_MOBILE)
  private String mobile;

  public static final String SERIALIZED_NAME_PHONE = "Phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_POSITION_TITLE = "PositionTitle";
  @SerializedName(SERIALIZED_NAME_POSITION_TITLE)
  private String positionTitle;

  public static final String SERIALIZED_NAME_UPDATE_EXISTING = "UpdateExisting";
  @SerializedName(SERIALIZED_NAME_UPDATE_EXISTING)
  private Boolean updateExisting;

  public NewCompanyContact() {
  }

  public NewCompanyContact companyBillingAddress(String companyBillingAddress) {
    this.companyBillingAddress = companyBillingAddress;
    return this;
  }

  /**
   * Get companyBillingAddress
   * @return companyBillingAddress
   */
  @javax.annotation.Nullable
  public String getCompanyBillingAddress() {
    return companyBillingAddress;
  }

  public void setCompanyBillingAddress(String companyBillingAddress) {
    this.companyBillingAddress = companyBillingAddress;
  }


  public NewCompanyContact companyBillingAddressCity(String companyBillingAddressCity) {
    this.companyBillingAddressCity = companyBillingAddressCity;
    return this;
  }

  /**
   * Get companyBillingAddressCity
   * @return companyBillingAddressCity
   */
  @javax.annotation.Nullable
  public String getCompanyBillingAddressCity() {
    return companyBillingAddressCity;
  }

  public void setCompanyBillingAddressCity(String companyBillingAddressCity) {
    this.companyBillingAddressCity = companyBillingAddressCity;
  }


  public NewCompanyContact companyBillingAddressCountryCode(String companyBillingAddressCountryCode) {
    this.companyBillingAddressCountryCode = companyBillingAddressCountryCode;
    return this;
  }

  /**
   * Get companyBillingAddressCountryCode
   * @return companyBillingAddressCountryCode
   */
  @javax.annotation.Nullable
  public String getCompanyBillingAddressCountryCode() {
    return companyBillingAddressCountryCode;
  }

  public void setCompanyBillingAddressCountryCode(String companyBillingAddressCountryCode) {
    this.companyBillingAddressCountryCode = companyBillingAddressCountryCode;
  }


  public NewCompanyContact companyBillingAddressLine(String companyBillingAddressLine) {
    this.companyBillingAddressLine = companyBillingAddressLine;
    return this;
  }

  /**
   * Get companyBillingAddressLine
   * @return companyBillingAddressLine
   */
  @javax.annotation.Nullable
  public String getCompanyBillingAddressLine() {
    return companyBillingAddressLine;
  }

  public void setCompanyBillingAddressLine(String companyBillingAddressLine) {
    this.companyBillingAddressLine = companyBillingAddressLine;
  }


  public NewCompanyContact companyBillingAddressPostCode(String companyBillingAddressPostCode) {
    this.companyBillingAddressPostCode = companyBillingAddressPostCode;
    return this;
  }

  /**
   * Get companyBillingAddressPostCode
   * @return companyBillingAddressPostCode
   */
  @javax.annotation.Nullable
  public String getCompanyBillingAddressPostCode() {
    return companyBillingAddressPostCode;
  }

  public void setCompanyBillingAddressPostCode(String companyBillingAddressPostCode) {
    this.companyBillingAddressPostCode = companyBillingAddressPostCode;
  }


  public NewCompanyContact companyBillingAddressState(String companyBillingAddressState) {
    this.companyBillingAddressState = companyBillingAddressState;
    return this;
  }

  /**
   * Get companyBillingAddressState
   * @return companyBillingAddressState
   */
  @javax.annotation.Nullable
  public String getCompanyBillingAddressState() {
    return companyBillingAddressState;
  }

  public void setCompanyBillingAddressState(String companyBillingAddressState) {
    this.companyBillingAddressState = companyBillingAddressState;
  }


  public NewCompanyContact companyIDFK(Integer companyIDFK) {
    this.companyIDFK = companyIDFK;
    return this;
  }

  /**
   * Get companyIDFK
   * @return companyIDFK
   */
  @javax.annotation.Nullable
  public Integer getCompanyIDFK() {
    return companyIDFK;
  }

  public void setCompanyIDFK(Integer companyIDFK) {
    this.companyIDFK = companyIDFK;
  }


  public NewCompanyContact companyName(String companyName) {
    this.companyName = companyName;
    return this;
  }

  /**
   * Get companyName
   * @return companyName
   */
  @javax.annotation.Nullable
  public String getCompanyName() {
    return companyName;
  }

  public void setCompanyName(String companyName) {
    this.companyName = companyName;
  }


  public NewCompanyContact contactEmail(String contactEmail) {
    this.contactEmail = contactEmail;
    return this;
  }

  /**
   * Get contactEmail
   * @return contactEmail
   */
  @javax.annotation.Nonnull
  public String getContactEmail() {
    return contactEmail;
  }

  public void setContactEmail(String contactEmail) {
    this.contactEmail = contactEmail;
  }


  public NewCompanyContact currencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
    return this;
  }

  /**
   * Get currencyCode
   * @return currencyCode
   */
  @javax.annotation.Nullable
  public String getCurrencyCode() {
    return currencyCode;
  }

  public void setCurrencyCode(String currencyCode) {
    this.currencyCode = currencyCode;
  }


  public NewCompanyContact firstname(String firstname) {
    this.firstname = firstname;
    return this;
  }

  /**
   * Get firstname
   * @return firstname
   */
  @javax.annotation.Nonnull
  public String getFirstname() {
    return firstname;
  }

  public void setFirstname(String firstname) {
    this.firstname = firstname;
  }


  public NewCompanyContact lastname(String lastname) {
    this.lastname = lastname;
    return this;
  }

  /**
   * Get lastname
   * @return lastname
   */
  @javax.annotation.Nonnull
  public String getLastname() {
    return lastname;
  }

  public void setLastname(String lastname) {
    this.lastname = lastname;
  }


  public NewCompanyContact mobile(String mobile) {
    this.mobile = mobile;
    return this;
  }

  /**
   * Get mobile
   * @return mobile
   */
  @javax.annotation.Nullable
  public String getMobile() {
    return mobile;
  }

  public void setMobile(String mobile) {
    this.mobile = mobile;
  }


  public NewCompanyContact phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Get phone
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public NewCompanyContact positionTitle(String positionTitle) {
    this.positionTitle = positionTitle;
    return this;
  }

  /**
   * Get positionTitle
   * @return positionTitle
   */
  @javax.annotation.Nullable
  public String getPositionTitle() {
    return positionTitle;
  }

  public void setPositionTitle(String positionTitle) {
    this.positionTitle = positionTitle;
  }


  public NewCompanyContact updateExisting(Boolean updateExisting) {
    this.updateExisting = updateExisting;
    return this;
  }

  /**
   * Get updateExisting
   * @return updateExisting
   */
  @javax.annotation.Nullable
  public Boolean getUpdateExisting() {
    return updateExisting;
  }

  public void setUpdateExisting(Boolean updateExisting) {
    this.updateExisting = updateExisting;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NewCompanyContact newCompanyContact = (NewCompanyContact) o;
    return Objects.equals(this.companyBillingAddress, newCompanyContact.companyBillingAddress) &&
        Objects.equals(this.companyBillingAddressCity, newCompanyContact.companyBillingAddressCity) &&
        Objects.equals(this.companyBillingAddressCountryCode, newCompanyContact.companyBillingAddressCountryCode) &&
        Objects.equals(this.companyBillingAddressLine, newCompanyContact.companyBillingAddressLine) &&
        Objects.equals(this.companyBillingAddressPostCode, newCompanyContact.companyBillingAddressPostCode) &&
        Objects.equals(this.companyBillingAddressState, newCompanyContact.companyBillingAddressState) &&
        Objects.equals(this.companyIDFK, newCompanyContact.companyIDFK) &&
        Objects.equals(this.companyName, newCompanyContact.companyName) &&
        Objects.equals(this.contactEmail, newCompanyContact.contactEmail) &&
        Objects.equals(this.currencyCode, newCompanyContact.currencyCode) &&
        Objects.equals(this.firstname, newCompanyContact.firstname) &&
        Objects.equals(this.lastname, newCompanyContact.lastname) &&
        Objects.equals(this.mobile, newCompanyContact.mobile) &&
        Objects.equals(this.phone, newCompanyContact.phone) &&
        Objects.equals(this.positionTitle, newCompanyContact.positionTitle) &&
        Objects.equals(this.updateExisting, newCompanyContact.updateExisting);
  }

  @Override
  public int hashCode() {
    return Objects.hash(companyBillingAddress, companyBillingAddressCity, companyBillingAddressCountryCode, companyBillingAddressLine, companyBillingAddressPostCode, companyBillingAddressState, companyIDFK, companyName, contactEmail, currencyCode, firstname, lastname, mobile, phone, positionTitle, updateExisting);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NewCompanyContact {\n");
    sb.append("    companyBillingAddress: ").append(toIndentedString(companyBillingAddress)).append("\n");
    sb.append("    companyBillingAddressCity: ").append(toIndentedString(companyBillingAddressCity)).append("\n");
    sb.append("    companyBillingAddressCountryCode: ").append(toIndentedString(companyBillingAddressCountryCode)).append("\n");
    sb.append("    companyBillingAddressLine: ").append(toIndentedString(companyBillingAddressLine)).append("\n");
    sb.append("    companyBillingAddressPostCode: ").append(toIndentedString(companyBillingAddressPostCode)).append("\n");
    sb.append("    companyBillingAddressState: ").append(toIndentedString(companyBillingAddressState)).append("\n");
    sb.append("    companyIDFK: ").append(toIndentedString(companyIDFK)).append("\n");
    sb.append("    companyName: ").append(toIndentedString(companyName)).append("\n");
    sb.append("    contactEmail: ").append(toIndentedString(contactEmail)).append("\n");
    sb.append("    currencyCode: ").append(toIndentedString(currencyCode)).append("\n");
    sb.append("    firstname: ").append(toIndentedString(firstname)).append("\n");
    sb.append("    lastname: ").append(toIndentedString(lastname)).append("\n");
    sb.append("    mobile: ").append(toIndentedString(mobile)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    positionTitle: ").append(toIndentedString(positionTitle)).append("\n");
    sb.append("    updateExisting: ").append(toIndentedString(updateExisting)).append("\n");
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
    openapiFields.add("CompanyBillingAddress");
    openapiFields.add("CompanyBillingAddressCity");
    openapiFields.add("CompanyBillingAddressCountryCode");
    openapiFields.add("CompanyBillingAddressLine");
    openapiFields.add("CompanyBillingAddressPostCode");
    openapiFields.add("CompanyBillingAddressState");
    openapiFields.add("CompanyIDFK");
    openapiFields.add("CompanyName");
    openapiFields.add("ContactEmail");
    openapiFields.add("CurrencyCode");
    openapiFields.add("Firstname");
    openapiFields.add("Lastname");
    openapiFields.add("Mobile");
    openapiFields.add("Phone");
    openapiFields.add("PositionTitle");
    openapiFields.add("UpdateExisting");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("ContactEmail");
    openapiRequiredFields.add("Firstname");
    openapiRequiredFields.add("Lastname");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NewCompanyContact
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NewCompanyContact.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NewCompanyContact is not found in the empty JSON string", NewCompanyContact.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NewCompanyContact.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NewCompanyContact` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : NewCompanyContact.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("CompanyBillingAddress") != null && !jsonObj.get("CompanyBillingAddress").isJsonNull()) && !jsonObj.get("CompanyBillingAddress").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyBillingAddress` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyBillingAddress").toString()));
      }
      if ((jsonObj.get("CompanyBillingAddressCity") != null && !jsonObj.get("CompanyBillingAddressCity").isJsonNull()) && !jsonObj.get("CompanyBillingAddressCity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyBillingAddressCity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyBillingAddressCity").toString()));
      }
      if ((jsonObj.get("CompanyBillingAddressCountryCode") != null && !jsonObj.get("CompanyBillingAddressCountryCode").isJsonNull()) && !jsonObj.get("CompanyBillingAddressCountryCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyBillingAddressCountryCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyBillingAddressCountryCode").toString()));
      }
      if ((jsonObj.get("CompanyBillingAddressLine") != null && !jsonObj.get("CompanyBillingAddressLine").isJsonNull()) && !jsonObj.get("CompanyBillingAddressLine").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyBillingAddressLine` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyBillingAddressLine").toString()));
      }
      if ((jsonObj.get("CompanyBillingAddressPostCode") != null && !jsonObj.get("CompanyBillingAddressPostCode").isJsonNull()) && !jsonObj.get("CompanyBillingAddressPostCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyBillingAddressPostCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyBillingAddressPostCode").toString()));
      }
      if ((jsonObj.get("CompanyBillingAddressState") != null && !jsonObj.get("CompanyBillingAddressState").isJsonNull()) && !jsonObj.get("CompanyBillingAddressState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyBillingAddressState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyBillingAddressState").toString()));
      }
      if ((jsonObj.get("CompanyName") != null && !jsonObj.get("CompanyName").isJsonNull()) && !jsonObj.get("CompanyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CompanyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CompanyName").toString()));
      }
      if (!jsonObj.get("ContactEmail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ContactEmail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ContactEmail").toString()));
      }
      if ((jsonObj.get("CurrencyCode") != null && !jsonObj.get("CurrencyCode").isJsonNull()) && !jsonObj.get("CurrencyCode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `CurrencyCode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("CurrencyCode").toString()));
      }
      if (!jsonObj.get("Firstname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Firstname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Firstname").toString()));
      }
      if (!jsonObj.get("Lastname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Lastname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Lastname").toString()));
      }
      if ((jsonObj.get("Mobile") != null && !jsonObj.get("Mobile").isJsonNull()) && !jsonObj.get("Mobile").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Mobile` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Mobile").toString()));
      }
      if ((jsonObj.get("Phone") != null && !jsonObj.get("Phone").isJsonNull()) && !jsonObj.get("Phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Phone").toString()));
      }
      if ((jsonObj.get("PositionTitle") != null && !jsonObj.get("PositionTitle").isJsonNull()) && !jsonObj.get("PositionTitle").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `PositionTitle` to be a primitive type in the JSON string but got `%s`", jsonObj.get("PositionTitle").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NewCompanyContact.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NewCompanyContact' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NewCompanyContact> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NewCompanyContact.class));

       return (TypeAdapter<T>) new TypeAdapter<NewCompanyContact>() {
           @Override
           public void write(JsonWriter out, NewCompanyContact value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NewCompanyContact read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NewCompanyContact given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NewCompanyContact
   * @throws IOException if the JSON string is invalid with respect to NewCompanyContact
   */
  public static NewCompanyContact fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NewCompanyContact.class);
  }

  /**
   * Convert an instance of NewCompanyContact to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

