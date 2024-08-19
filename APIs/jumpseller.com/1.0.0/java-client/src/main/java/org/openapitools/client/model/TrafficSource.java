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
 * TrafficSource
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class TrafficSource {
  public static final String SERIALIZED_NAME_CAMPAIGN = "campaign";
  @SerializedName(SERIALIZED_NAME_CAMPAIGN)
  private String campaign;

  public static final String SERIALIZED_NAME_FIRST_PAGE_VISITED = "first_page_visited";
  @SerializedName(SERIALIZED_NAME_FIRST_PAGE_VISITED)
  private String firstPageVisited;

  public static final String SERIALIZED_NAME_FIRST_PAGE_VISITED_AT = "first_page_visited_at";
  @SerializedName(SERIALIZED_NAME_FIRST_PAGE_VISITED_AT)
  private String firstPageVisitedAt;

  public static final String SERIALIZED_NAME_MEDIUM = "medium";
  @SerializedName(SERIALIZED_NAME_MEDIUM)
  private String medium;

  public static final String SERIALIZED_NAME_REFERRAL_CODE = "referral_code";
  @SerializedName(SERIALIZED_NAME_REFERRAL_CODE)
  private String referralCode;

  public static final String SERIALIZED_NAME_REFERRAL_SOURCE = "referral_source";
  @SerializedName(SERIALIZED_NAME_REFERRAL_SOURCE)
  private String referralSource;

  public static final String SERIALIZED_NAME_REFERRAL_URL = "referral_url";
  @SerializedName(SERIALIZED_NAME_REFERRAL_URL)
  private String referralUrl;

  public static final String SERIALIZED_NAME_SOURCE_NAME = "source_name";
  @SerializedName(SERIALIZED_NAME_SOURCE_NAME)
  private String sourceName;

  public static final String SERIALIZED_NAME_USER_AGENT = "user_agent";
  @SerializedName(SERIALIZED_NAME_USER_AGENT)
  private String userAgent;

  public TrafficSource() {
  }

  public TrafficSource campaign(String campaign) {
    this.campaign = campaign;
    return this;
  }

  /**
   * The campaign that referred the customer to the checkout
   * @return campaign
   */
  @javax.annotation.Nullable
  public String getCampaign() {
    return campaign;
  }

  public void setCampaign(String campaign) {
    this.campaign = campaign;
  }


  public TrafficSource firstPageVisited(String firstPageVisited) {
    this.firstPageVisited = firstPageVisited;
    return this;
  }

  /**
   * The first url visited by the customer
   * @return firstPageVisited
   */
  @javax.annotation.Nullable
  public String getFirstPageVisited() {
    return firstPageVisited;
  }

  public void setFirstPageVisited(String firstPageVisited) {
    this.firstPageVisited = firstPageVisited;
  }


  public TrafficSource firstPageVisitedAt(String firstPageVisitedAt) {
    this.firstPageVisitedAt = firstPageVisitedAt;
    return this;
  }

  /**
   * The date when the customer visited the first page
   * @return firstPageVisitedAt
   */
  @javax.annotation.Nullable
  public String getFirstPageVisitedAt() {
    return firstPageVisitedAt;
  }

  public void setFirstPageVisitedAt(String firstPageVisitedAt) {
    this.firstPageVisitedAt = firstPageVisitedAt;
  }


  public TrafficSource medium(String medium) {
    this.medium = medium;
    return this;
  }

  /**
   * The medium that referred the customer to the checkout
   * @return medium
   */
  @javax.annotation.Nullable
  public String getMedium() {
    return medium;
  }

  public void setMedium(String medium) {
    this.medium = medium;
  }


  public TrafficSource referralCode(String referralCode) {
    this.referralCode = referralCode;
    return this;
  }

  /**
   * The code that referred the customer to the checkout
   * @return referralCode
   */
  @javax.annotation.Nullable
  public String getReferralCode() {
    return referralCode;
  }

  public void setReferralCode(String referralCode) {
    this.referralCode = referralCode;
  }


  public TrafficSource referralSource(String referralSource) {
    this.referralSource = referralSource;
    return this;
  }

  /**
   * The source that referred the customer to the website
   * @return referralSource
   */
  @javax.annotation.Nullable
  public String getReferralSource() {
    return referralSource;
  }

  public void setReferralSource(String referralSource) {
    this.referralSource = referralSource;
  }


  public TrafficSource referralUrl(String referralUrl) {
    this.referralUrl = referralUrl;
    return this;
  }

  /**
   * The website that referred the customer to the checkout
   * @return referralUrl
   */
  @javax.annotation.Nullable
  public String getReferralUrl() {
    return referralUrl;
  }

  public void setReferralUrl(String referralUrl) {
    this.referralUrl = referralUrl;
  }


  public TrafficSource sourceName(String sourceName) {
    this.sourceName = sourceName;
    return this;
  }

  /**
   * Where the checkout originated
   * @return sourceName
   */
  @javax.annotation.Nullable
  public String getSourceName() {
    return sourceName;
  }

  public void setSourceName(String sourceName) {
    this.sourceName = sourceName;
  }


  public TrafficSource userAgent(String userAgent) {
    this.userAgent = userAgent;
    return this;
  }

  /**
   * User agent of the referred request to checkout
   * @return userAgent
   */
  @javax.annotation.Nullable
  public String getUserAgent() {
    return userAgent;
  }

  public void setUserAgent(String userAgent) {
    this.userAgent = userAgent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TrafficSource trafficSource = (TrafficSource) o;
    return Objects.equals(this.campaign, trafficSource.campaign) &&
        Objects.equals(this.firstPageVisited, trafficSource.firstPageVisited) &&
        Objects.equals(this.firstPageVisitedAt, trafficSource.firstPageVisitedAt) &&
        Objects.equals(this.medium, trafficSource.medium) &&
        Objects.equals(this.referralCode, trafficSource.referralCode) &&
        Objects.equals(this.referralSource, trafficSource.referralSource) &&
        Objects.equals(this.referralUrl, trafficSource.referralUrl) &&
        Objects.equals(this.sourceName, trafficSource.sourceName) &&
        Objects.equals(this.userAgent, trafficSource.userAgent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(campaign, firstPageVisited, firstPageVisitedAt, medium, referralCode, referralSource, referralUrl, sourceName, userAgent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TrafficSource {\n");
    sb.append("    campaign: ").append(toIndentedString(campaign)).append("\n");
    sb.append("    firstPageVisited: ").append(toIndentedString(firstPageVisited)).append("\n");
    sb.append("    firstPageVisitedAt: ").append(toIndentedString(firstPageVisitedAt)).append("\n");
    sb.append("    medium: ").append(toIndentedString(medium)).append("\n");
    sb.append("    referralCode: ").append(toIndentedString(referralCode)).append("\n");
    sb.append("    referralSource: ").append(toIndentedString(referralSource)).append("\n");
    sb.append("    referralUrl: ").append(toIndentedString(referralUrl)).append("\n");
    sb.append("    sourceName: ").append(toIndentedString(sourceName)).append("\n");
    sb.append("    userAgent: ").append(toIndentedString(userAgent)).append("\n");
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
    openapiFields.add("campaign");
    openapiFields.add("first_page_visited");
    openapiFields.add("first_page_visited_at");
    openapiFields.add("medium");
    openapiFields.add("referral_code");
    openapiFields.add("referral_source");
    openapiFields.add("referral_url");
    openapiFields.add("source_name");
    openapiFields.add("user_agent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to TrafficSource
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!TrafficSource.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in TrafficSource is not found in the empty JSON string", TrafficSource.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!TrafficSource.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TrafficSource` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("campaign") != null && !jsonObj.get("campaign").isJsonNull()) && !jsonObj.get("campaign").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `campaign` to be a primitive type in the JSON string but got `%s`", jsonObj.get("campaign").toString()));
      }
      if ((jsonObj.get("first_page_visited") != null && !jsonObj.get("first_page_visited").isJsonNull()) && !jsonObj.get("first_page_visited").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_page_visited` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_page_visited").toString()));
      }
      if ((jsonObj.get("first_page_visited_at") != null && !jsonObj.get("first_page_visited_at").isJsonNull()) && !jsonObj.get("first_page_visited_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `first_page_visited_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("first_page_visited_at").toString()));
      }
      if ((jsonObj.get("medium") != null && !jsonObj.get("medium").isJsonNull()) && !jsonObj.get("medium").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `medium` to be a primitive type in the JSON string but got `%s`", jsonObj.get("medium").toString()));
      }
      if ((jsonObj.get("referral_code") != null && !jsonObj.get("referral_code").isJsonNull()) && !jsonObj.get("referral_code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referral_code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referral_code").toString()));
      }
      if ((jsonObj.get("referral_source") != null && !jsonObj.get("referral_source").isJsonNull()) && !jsonObj.get("referral_source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referral_source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referral_source").toString()));
      }
      if ((jsonObj.get("referral_url") != null && !jsonObj.get("referral_url").isJsonNull()) && !jsonObj.get("referral_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referral_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referral_url").toString()));
      }
      if ((jsonObj.get("source_name") != null && !jsonObj.get("source_name").isJsonNull()) && !jsonObj.get("source_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source_name").toString()));
      }
      if ((jsonObj.get("user_agent") != null && !jsonObj.get("user_agent").isJsonNull()) && !jsonObj.get("user_agent").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `user_agent` to be a primitive type in the JSON string but got `%s`", jsonObj.get("user_agent").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TrafficSource.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TrafficSource' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TrafficSource> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TrafficSource.class));

       return (TypeAdapter<T>) new TypeAdapter<TrafficSource>() {
           @Override
           public void write(JsonWriter out, TrafficSource value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TrafficSource read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of TrafficSource given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of TrafficSource
   * @throws IOException if the JSON string is invalid with respect to TrafficSource
   */
  public static TrafficSource fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TrafficSource.class);
  }

  /**
   * Convert an instance of TrafficSource to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

