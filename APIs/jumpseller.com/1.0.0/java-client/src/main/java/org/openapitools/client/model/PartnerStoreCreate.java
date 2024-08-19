/*
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
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
 * PartnerStoreCreate
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PartnerStoreCreate {
  public static final String SERIALIZED_NAME_AFF = "aff";
  @SerializedName(SERIALIZED_NAME_AFF)
  private String aff;

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_LOCALE = "locale";
  @SerializedName(SERIALIZED_NAME_LOCALE)
  private String locale = "en";

  public static final String SERIALIZED_NAME_PASSWORD = "password";
  @SerializedName(SERIALIZED_NAME_PASSWORD)
  private String password;

  /**
   * New Store plan name.
   */
  @JsonAdapter(PlanNameEnum.Adapter.class)
  public enum PlanNameEnum {
    PRO("pro"),
    
    PLUS("plus"),
    
    PREMIUM("premium");

    private String value;

    PlanNameEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PlanNameEnum fromValue(String value) {
      for (PlanNameEnum b : PlanNameEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PlanNameEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PlanNameEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PlanNameEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PlanNameEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PlanNameEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PLAN_NAME = "plan_name";
  @SerializedName(SERIALIZED_NAME_PLAN_NAME)
  private PlanNameEnum planName = PlanNameEnum.PRO;

  public static final String SERIALIZED_NAME_REJECT_DUPLICATES = "reject_duplicates";
  @SerializedName(SERIALIZED_NAME_REJECT_DUPLICATES)
  private Boolean rejectDuplicates = false;

  public static final String SERIALIZED_NAME_STORE_NAME = "store_name";
  @SerializedName(SERIALIZED_NAME_STORE_NAME)
  private String storeName;

  public PartnerStoreCreate() {
  }

  public PartnerStoreCreate aff(String aff) {
    this.aff = aff;
    return this;
  }

  /**
   * Partner code.
   * @return aff
   */
  @javax.annotation.Nullable
  public String getAff() {
    return aff;
  }

  public void setAff(String aff) {
    this.aff = aff;
  }


  public PartnerStoreCreate email(String email) {
    this.email = email;
    return this;
  }

  /**
   * New Store administrator email.
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public PartnerStoreCreate locale(String locale) {
    this.locale = locale;
    return this;
  }

  /**
   * ISO3166-2 code for the store langauge.
   * @return locale
   */
  @javax.annotation.Nullable
  public String getLocale() {
    return locale;
  }

  public void setLocale(String locale) {
    this.locale = locale;
  }


  public PartnerStoreCreate password(String password) {
    this.password = password;
    return this;
  }

  /**
   * New Store administrator password.
   * @return password
   */
  @javax.annotation.Nullable
  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }


  public PartnerStoreCreate planName(PlanNameEnum planName) {
    this.planName = planName;
    return this;
  }

  /**
   * New Store plan name.
   * @return planName
   */
  @javax.annotation.Nullable
  public PlanNameEnum getPlanName() {
    return planName;
  }

  public void setPlanName(PlanNameEnum planName) {
    this.planName = planName;
  }


  public PartnerStoreCreate rejectDuplicates(Boolean rejectDuplicates) {
    this.rejectDuplicates = rejectDuplicates;
    return this;
  }

  /**
   * Indicates whether the request should fail if the Store name provided is already in use.
   * @return rejectDuplicates
   */
  @javax.annotation.Nullable
  public Boolean getRejectDuplicates() {
    return rejectDuplicates;
  }

  public void setRejectDuplicates(Boolean rejectDuplicates) {
    this.rejectDuplicates = rejectDuplicates;
  }


  public PartnerStoreCreate storeName(String storeName) {
    this.storeName = storeName;
    return this;
  }

  /**
   * New Store name.
   * @return storeName
   */
  @javax.annotation.Nullable
  public String getStoreName() {
    return storeName;
  }

  public void setStoreName(String storeName) {
    this.storeName = storeName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PartnerStoreCreate partnerStoreCreate = (PartnerStoreCreate) o;
    return Objects.equals(this.aff, partnerStoreCreate.aff) &&
        Objects.equals(this.email, partnerStoreCreate.email) &&
        Objects.equals(this.locale, partnerStoreCreate.locale) &&
        Objects.equals(this.password, partnerStoreCreate.password) &&
        Objects.equals(this.planName, partnerStoreCreate.planName) &&
        Objects.equals(this.rejectDuplicates, partnerStoreCreate.rejectDuplicates) &&
        Objects.equals(this.storeName, partnerStoreCreate.storeName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aff, email, locale, password, planName, rejectDuplicates, storeName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PartnerStoreCreate {\n");
    sb.append("    aff: ").append(toIndentedString(aff)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    locale: ").append(toIndentedString(locale)).append("\n");
    sb.append("    password: ").append(toIndentedString(password)).append("\n");
    sb.append("    planName: ").append(toIndentedString(planName)).append("\n");
    sb.append("    rejectDuplicates: ").append(toIndentedString(rejectDuplicates)).append("\n");
    sb.append("    storeName: ").append(toIndentedString(storeName)).append("\n");
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
    openapiFields.add("aff");
    openapiFields.add("email");
    openapiFields.add("locale");
    openapiFields.add("password");
    openapiFields.add("plan_name");
    openapiFields.add("reject_duplicates");
    openapiFields.add("store_name");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PartnerStoreCreate
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PartnerStoreCreate.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PartnerStoreCreate is not found in the empty JSON string", PartnerStoreCreate.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PartnerStoreCreate.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PartnerStoreCreate` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("aff") != null && !jsonObj.get("aff").isJsonNull()) && !jsonObj.get("aff").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `aff` to be a primitive type in the JSON string but got `%s`", jsonObj.get("aff").toString()));
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("locale") != null && !jsonObj.get("locale").isJsonNull()) && !jsonObj.get("locale").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `locale` to be a primitive type in the JSON string but got `%s`", jsonObj.get("locale").toString()));
      }
      if ((jsonObj.get("password") != null && !jsonObj.get("password").isJsonNull()) && !jsonObj.get("password").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `password` to be a primitive type in the JSON string but got `%s`", jsonObj.get("password").toString()));
      }
      if ((jsonObj.get("plan_name") != null && !jsonObj.get("plan_name").isJsonNull()) && !jsonObj.get("plan_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `plan_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("plan_name").toString()));
      }
      // validate the optional field `plan_name`
      if (jsonObj.get("plan_name") != null && !jsonObj.get("plan_name").isJsonNull()) {
        PlanNameEnum.validateJsonElement(jsonObj.get("plan_name"));
      }
      if ((jsonObj.get("store_name") != null && !jsonObj.get("store_name").isJsonNull()) && !jsonObj.get("store_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `store_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("store_name").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PartnerStoreCreate.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PartnerStoreCreate' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PartnerStoreCreate> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PartnerStoreCreate.class));

       return (TypeAdapter<T>) new TypeAdapter<PartnerStoreCreate>() {
           @Override
           public void write(JsonWriter out, PartnerStoreCreate value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PartnerStoreCreate read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PartnerStoreCreate given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PartnerStoreCreate
   * @throws IOException if the JSON string is invalid with respect to PartnerStoreCreate
   */
  public static PartnerStoreCreate fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PartnerStoreCreate.class);
  }

  /**
   * Convert an instance of PartnerStoreCreate to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

