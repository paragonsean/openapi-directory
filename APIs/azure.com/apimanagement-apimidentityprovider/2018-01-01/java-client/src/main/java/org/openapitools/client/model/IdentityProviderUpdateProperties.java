/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2018-01-01
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
 * Parameters supplied to the Update Identity Provider operation.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:41:14.009991-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class IdentityProviderUpdateProperties {
  public static final String SERIALIZED_NAME_CLIENT_ID = "clientId";
  @SerializedName(SERIALIZED_NAME_CLIENT_ID)
  private String clientId;

  public static final String SERIALIZED_NAME_CLIENT_SECRET = "clientSecret";
  @SerializedName(SERIALIZED_NAME_CLIENT_SECRET)
  private String clientSecret;

  public static final String SERIALIZED_NAME_ALLOWED_TENANTS = "allowedTenants";
  @SerializedName(SERIALIZED_NAME_ALLOWED_TENANTS)
  private List<String> allowedTenants = new ArrayList<>();

  public static final String SERIALIZED_NAME_PASSWORD_RESET_POLICY_NAME = "passwordResetPolicyName";
  @SerializedName(SERIALIZED_NAME_PASSWORD_RESET_POLICY_NAME)
  private String passwordResetPolicyName;

  public static final String SERIALIZED_NAME_PROFILE_EDITING_POLICY_NAME = "profileEditingPolicyName";
  @SerializedName(SERIALIZED_NAME_PROFILE_EDITING_POLICY_NAME)
  private String profileEditingPolicyName;

  public static final String SERIALIZED_NAME_SIGNIN_POLICY_NAME = "signinPolicyName";
  @SerializedName(SERIALIZED_NAME_SIGNIN_POLICY_NAME)
  private String signinPolicyName;

  public static final String SERIALIZED_NAME_SIGNUP_POLICY_NAME = "signupPolicyName";
  @SerializedName(SERIALIZED_NAME_SIGNUP_POLICY_NAME)
  private String signupPolicyName;

  /**
   * Identity Provider Type identifier.
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    FACEBOOK("facebook"),
    
    GOOGLE("google"),
    
    MICROSOFT("microsoft"),
    
    TWITTER("twitter"),
    
    AAD("aad"),
    
    AAD_B2_C("aadB2C");

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

  public IdentityProviderUpdateProperties() {
  }

  public IdentityProviderUpdateProperties clientId(String clientId) {
    this.clientId = clientId;
    return this;
  }

  /**
   * Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.
   * @return clientId
   */
  @javax.annotation.Nullable
  public String getClientId() {
    return clientId;
  }

  public void setClientId(String clientId) {
    this.clientId = clientId;
  }


  public IdentityProviderUpdateProperties clientSecret(String clientSecret) {
    this.clientSecret = clientSecret;
    return this;
  }

  /**
   * Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.
   * @return clientSecret
   */
  @javax.annotation.Nullable
  public String getClientSecret() {
    return clientSecret;
  }

  public void setClientSecret(String clientSecret) {
    this.clientSecret = clientSecret;
  }


  public IdentityProviderUpdateProperties allowedTenants(List<String> allowedTenants) {
    this.allowedTenants = allowedTenants;
    return this;
  }

  public IdentityProviderUpdateProperties addAllowedTenantsItem(String allowedTenantsItem) {
    if (this.allowedTenants == null) {
      this.allowedTenants = new ArrayList<>();
    }
    this.allowedTenants.add(allowedTenantsItem);
    return this;
  }

  /**
   * List of Allowed Tenants when configuring Azure Active Directory login.
   * @return allowedTenants
   */
  @javax.annotation.Nullable
  public List<String> getAllowedTenants() {
    return allowedTenants;
  }

  public void setAllowedTenants(List<String> allowedTenants) {
    this.allowedTenants = allowedTenants;
  }


  public IdentityProviderUpdateProperties passwordResetPolicyName(String passwordResetPolicyName) {
    this.passwordResetPolicyName = passwordResetPolicyName;
    return this;
  }

  /**
   * Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
   * @return passwordResetPolicyName
   */
  @javax.annotation.Nullable
  public String getPasswordResetPolicyName() {
    return passwordResetPolicyName;
  }

  public void setPasswordResetPolicyName(String passwordResetPolicyName) {
    this.passwordResetPolicyName = passwordResetPolicyName;
  }


  public IdentityProviderUpdateProperties profileEditingPolicyName(String profileEditingPolicyName) {
    this.profileEditingPolicyName = profileEditingPolicyName;
    return this;
  }

  /**
   * Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
   * @return profileEditingPolicyName
   */
  @javax.annotation.Nullable
  public String getProfileEditingPolicyName() {
    return profileEditingPolicyName;
  }

  public void setProfileEditingPolicyName(String profileEditingPolicyName) {
    this.profileEditingPolicyName = profileEditingPolicyName;
  }


  public IdentityProviderUpdateProperties signinPolicyName(String signinPolicyName) {
    this.signinPolicyName = signinPolicyName;
    return this;
  }

  /**
   * Signin Policy Name. Only applies to AAD B2C Identity Provider.
   * @return signinPolicyName
   */
  @javax.annotation.Nullable
  public String getSigninPolicyName() {
    return signinPolicyName;
  }

  public void setSigninPolicyName(String signinPolicyName) {
    this.signinPolicyName = signinPolicyName;
  }


  public IdentityProviderUpdateProperties signupPolicyName(String signupPolicyName) {
    this.signupPolicyName = signupPolicyName;
    return this;
  }

  /**
   * Signup Policy Name. Only applies to AAD B2C Identity Provider.
   * @return signupPolicyName
   */
  @javax.annotation.Nullable
  public String getSignupPolicyName() {
    return signupPolicyName;
  }

  public void setSignupPolicyName(String signupPolicyName) {
    this.signupPolicyName = signupPolicyName;
  }


  public IdentityProviderUpdateProperties type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Identity Provider Type identifier.
   * @return type
   */
  @javax.annotation.Nullable
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
    IdentityProviderUpdateProperties identityProviderUpdateProperties = (IdentityProviderUpdateProperties) o;
    return Objects.equals(this.clientId, identityProviderUpdateProperties.clientId) &&
        Objects.equals(this.clientSecret, identityProviderUpdateProperties.clientSecret) &&
        Objects.equals(this.allowedTenants, identityProviderUpdateProperties.allowedTenants) &&
        Objects.equals(this.passwordResetPolicyName, identityProviderUpdateProperties.passwordResetPolicyName) &&
        Objects.equals(this.profileEditingPolicyName, identityProviderUpdateProperties.profileEditingPolicyName) &&
        Objects.equals(this.signinPolicyName, identityProviderUpdateProperties.signinPolicyName) &&
        Objects.equals(this.signupPolicyName, identityProviderUpdateProperties.signupPolicyName) &&
        Objects.equals(this.type, identityProviderUpdateProperties.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(clientId, clientSecret, allowedTenants, passwordResetPolicyName, profileEditingPolicyName, signinPolicyName, signupPolicyName, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class IdentityProviderUpdateProperties {\n");
    sb.append("    clientId: ").append(toIndentedString(clientId)).append("\n");
    sb.append("    clientSecret: ").append(toIndentedString(clientSecret)).append("\n");
    sb.append("    allowedTenants: ").append(toIndentedString(allowedTenants)).append("\n");
    sb.append("    passwordResetPolicyName: ").append(toIndentedString(passwordResetPolicyName)).append("\n");
    sb.append("    profileEditingPolicyName: ").append(toIndentedString(profileEditingPolicyName)).append("\n");
    sb.append("    signinPolicyName: ").append(toIndentedString(signinPolicyName)).append("\n");
    sb.append("    signupPolicyName: ").append(toIndentedString(signupPolicyName)).append("\n");
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
    openapiFields.add("allowedTenants");
    openapiFields.add("passwordResetPolicyName");
    openapiFields.add("profileEditingPolicyName");
    openapiFields.add("signinPolicyName");
    openapiFields.add("signupPolicyName");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to IdentityProviderUpdateProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!IdentityProviderUpdateProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in IdentityProviderUpdateProperties is not found in the empty JSON string", IdentityProviderUpdateProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!IdentityProviderUpdateProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `IdentityProviderUpdateProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("clientId") != null && !jsonObj.get("clientId").isJsonNull()) && !jsonObj.get("clientId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clientId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clientId").toString()));
      }
      if ((jsonObj.get("clientSecret") != null && !jsonObj.get("clientSecret").isJsonNull()) && !jsonObj.get("clientSecret").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clientSecret` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clientSecret").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("allowedTenants") != null && !jsonObj.get("allowedTenants").isJsonNull() && !jsonObj.get("allowedTenants").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `allowedTenants` to be an array in the JSON string but got `%s`", jsonObj.get("allowedTenants").toString()));
      }
      if ((jsonObj.get("passwordResetPolicyName") != null && !jsonObj.get("passwordResetPolicyName").isJsonNull()) && !jsonObj.get("passwordResetPolicyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `passwordResetPolicyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("passwordResetPolicyName").toString()));
      }
      if ((jsonObj.get("profileEditingPolicyName") != null && !jsonObj.get("profileEditingPolicyName").isJsonNull()) && !jsonObj.get("profileEditingPolicyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `profileEditingPolicyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("profileEditingPolicyName").toString()));
      }
      if ((jsonObj.get("signinPolicyName") != null && !jsonObj.get("signinPolicyName").isJsonNull()) && !jsonObj.get("signinPolicyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `signinPolicyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("signinPolicyName").toString()));
      }
      if ((jsonObj.get("signupPolicyName") != null && !jsonObj.get("signupPolicyName").isJsonNull()) && !jsonObj.get("signupPolicyName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `signupPolicyName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("signupPolicyName").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!IdentityProviderUpdateProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'IdentityProviderUpdateProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<IdentityProviderUpdateProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(IdentityProviderUpdateProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<IdentityProviderUpdateProperties>() {
           @Override
           public void write(JsonWriter out, IdentityProviderUpdateProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public IdentityProviderUpdateProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of IdentityProviderUpdateProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of IdentityProviderUpdateProperties
   * @throws IOException if the JSON string is invalid with respect to IdentityProviderUpdateProperties
   */
  public static IdentityProviderUpdateProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, IdentityProviderUpdateProperties.class);
  }

  /**
   * Convert an instance of IdentityProviderUpdateProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

