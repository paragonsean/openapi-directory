/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BankAccountAllOfLinks;
import org.openapitools.client.model.LeadSourceData;

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
 * LeadSource
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LeadSource {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<BankAccountAllOfLinks> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_AFFILIATE = "affiliate";
  @SerializedName(SERIALIZED_NAME_AFFILIATE)
  private String affiliate;

  public static final String SERIALIZED_NAME_CAMPAIGN = "campaign";
  @SerializedName(SERIALIZED_NAME_CAMPAIGN)
  private String campaign;

  public static final String SERIALIZED_NAME_CLICK_ID = "clickId";
  @SerializedName(SERIALIZED_NAME_CLICK_ID)
  private String clickId;

  public static final String SERIALIZED_NAME_CONTENT = "content";
  @SerializedName(SERIALIZED_NAME_CONTENT)
  private String content;

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_MEDIUM = "medium";
  @SerializedName(SERIALIZED_NAME_MEDIUM)
  private String medium;

  public static final String SERIALIZED_NAME_PATH = "path";
  @SerializedName(SERIALIZED_NAME_PATH)
  private String path;

  public static final String SERIALIZED_NAME_REFERRER = "referrer";
  @SerializedName(SERIALIZED_NAME_REFERRER)
  private String referrer;

  public static final String SERIALIZED_NAME_SALES_AGENT = "salesAgent";
  @SerializedName(SERIALIZED_NAME_SALES_AGENT)
  private String salesAgent;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public static final String SERIALIZED_NAME_SUB_AFFILIATE = "subAffiliate";
  @SerializedName(SERIALIZED_NAME_SUB_AFFILIATE)
  private String subAffiliate;

  public static final String SERIALIZED_NAME_TERM = "term";
  @SerializedName(SERIALIZED_NAME_TERM)
  private String term;

  public static final String SERIALIZED_NAME_ORIGINAL = "original";
  @SerializedName(SERIALIZED_NAME_ORIGINAL)
  private LeadSourceData original;

  public LeadSource() {
  }

  public LeadSource(
     List<BankAccountAllOfLinks> links, 
     OffsetDateTime createdTime, 
     LeadSourceData original
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.original = original;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<BankAccountAllOfLinks> getLinks() {
    return links;
  }



  public LeadSource affiliate(String affiliate) {
    this.affiliate = affiliate;
    return this;
  }

  /**
   * Lead source affiliate (eg 123, Bob Smith).
   * @return affiliate
   */
  @javax.annotation.Nullable
  public String getAffiliate() {
    return affiliate;
  }

  public void setAffiliate(String affiliate) {
    this.affiliate = affiliate;
  }


  public LeadSource campaign(String campaign) {
    this.campaign = campaign;
    return this;
  }

  /**
   * Lead source campaign (eg go-big-123).
   * @return campaign
   */
  @javax.annotation.Nullable
  public String getCampaign() {
    return campaign;
  }

  public void setCampaign(String campaign) {
    this.campaign = campaign;
  }


  public LeadSource clickId(String clickId) {
    this.clickId = clickId;
    return this;
  }

  /**
   * Lead source click id (may come from an ad server).
   * @return clickId
   */
  @javax.annotation.Nullable
  public String getClickId() {
    return clickId;
  }

  public void setClickId(String clickId) {
    this.clickId = clickId;
  }


  public LeadSource content(String content) {
    this.content = content;
    return this;
  }

  /**
   * Lead source content (eg smiley faces).
   * @return content
   */
  @javax.annotation.Nullable
  public String getContent() {
    return content;
  }

  public void setContent(String content) {
    this.content = content;
  }


  /**
   * Lead source created time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public LeadSource medium(String medium) {
    this.medium = medium;
    return this;
  }

  /**
   * Lead source medium (eg search, display).
   * @return medium
   */
  @javax.annotation.Nullable
  public String getMedium() {
    return medium;
  }

  public void setMedium(String medium) {
    this.medium = medium;
  }


  public LeadSource path(String path) {
    this.path = path;
    return this;
  }

  /**
   * Lead source path url (eg www.example.com/some/landing/path).
   * @return path
   */
  @javax.annotation.Nullable
  public String getPath() {
    return path;
  }

  public void setPath(String path) {
    this.path = path;
  }


  public LeadSource referrer(String referrer) {
    this.referrer = referrer;
    return this;
  }

  /**
   * Lead source [&#x60;referer&#x60; url](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer) as determined (eg www.example.com/some/landing/path).
   * @return referrer
   */
  @javax.annotation.Nullable
  public String getReferrer() {
    return referrer;
  }

  public void setReferrer(String referrer) {
    this.referrer = referrer;
  }


  public LeadSource salesAgent(String salesAgent) {
    this.salesAgent = salesAgent;
    return this;
  }

  /**
   * Lead source sales agent (eg James Bond).
   * @return salesAgent
   */
  @javax.annotation.Nullable
  public String getSalesAgent() {
    return salesAgent;
  }

  public void setSalesAgent(String salesAgent) {
    this.salesAgent = salesAgent;
  }


  public LeadSource source(String source) {
    this.source = source;
    return this;
  }

  /**
   * Lead source origin (eg google, yahoo).
   * @return source
   */
  @javax.annotation.Nullable
  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }


  public LeadSource subAffiliate(String subAffiliate) {
    this.subAffiliate = subAffiliate;
    return this;
  }

  /**
   * Lead source sub-affiliate also called a sub-id or click id in some circles (eg 123456).
   * @return subAffiliate
   */
  @javax.annotation.Nullable
  public String getSubAffiliate() {
    return subAffiliate;
  }

  public void setSubAffiliate(String subAffiliate) {
    this.subAffiliate = subAffiliate;
  }


  public LeadSource term(String term) {
    this.term = term;
    return this;
  }

  /**
   * Lead source term (eg salt shakers).
   * @return term
   */
  @javax.annotation.Nullable
  public String getTerm() {
    return term;
  }

  public void setTerm(String term) {
    this.term = term;
  }


  /**
   * Get original
   * @return original
   */
  @javax.annotation.Nullable
  public LeadSourceData getOriginal() {
    return original;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LeadSource leadSource = (LeadSource) o;
    return Objects.equals(this.links, leadSource.links) &&
        Objects.equals(this.affiliate, leadSource.affiliate) &&
        Objects.equals(this.campaign, leadSource.campaign) &&
        Objects.equals(this.clickId, leadSource.clickId) &&
        Objects.equals(this.content, leadSource.content) &&
        Objects.equals(this.createdTime, leadSource.createdTime) &&
        Objects.equals(this.medium, leadSource.medium) &&
        Objects.equals(this.path, leadSource.path) &&
        Objects.equals(this.referrer, leadSource.referrer) &&
        Objects.equals(this.salesAgent, leadSource.salesAgent) &&
        Objects.equals(this.source, leadSource.source) &&
        Objects.equals(this.subAffiliate, leadSource.subAffiliate) &&
        Objects.equals(this.term, leadSource.term) &&
        Objects.equals(this.original, leadSource.original);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, affiliate, campaign, clickId, content, createdTime, medium, path, referrer, salesAgent, source, subAffiliate, term, original);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LeadSource {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    affiliate: ").append(toIndentedString(affiliate)).append("\n");
    sb.append("    campaign: ").append(toIndentedString(campaign)).append("\n");
    sb.append("    clickId: ").append(toIndentedString(clickId)).append("\n");
    sb.append("    content: ").append(toIndentedString(content)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    medium: ").append(toIndentedString(medium)).append("\n");
    sb.append("    path: ").append(toIndentedString(path)).append("\n");
    sb.append("    referrer: ").append(toIndentedString(referrer)).append("\n");
    sb.append("    salesAgent: ").append(toIndentedString(salesAgent)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    subAffiliate: ").append(toIndentedString(subAffiliate)).append("\n");
    sb.append("    term: ").append(toIndentedString(term)).append("\n");
    sb.append("    original: ").append(toIndentedString(original)).append("\n");
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
    openapiFields.add("_links");
    openapiFields.add("affiliate");
    openapiFields.add("campaign");
    openapiFields.add("clickId");
    openapiFields.add("content");
    openapiFields.add("createdTime");
    openapiFields.add("medium");
    openapiFields.add("path");
    openapiFields.add("referrer");
    openapiFields.add("salesAgent");
    openapiFields.add("source");
    openapiFields.add("subAffiliate");
    openapiFields.add("term");
    openapiFields.add("original");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LeadSource
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LeadSource.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LeadSource is not found in the empty JSON string", LeadSource.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!LeadSource.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `LeadSource` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("_links") != null && !jsonObj.get("_links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("_links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_links` to be an array in the JSON string but got `%s`", jsonObj.get("_links").toString()));
          }

          // validate the optional field `_links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            BankAccountAllOfLinks.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if ((jsonObj.get("affiliate") != null && !jsonObj.get("affiliate").isJsonNull()) && !jsonObj.get("affiliate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `affiliate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("affiliate").toString()));
      }
      if ((jsonObj.get("campaign") != null && !jsonObj.get("campaign").isJsonNull()) && !jsonObj.get("campaign").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `campaign` to be a primitive type in the JSON string but got `%s`", jsonObj.get("campaign").toString()));
      }
      if ((jsonObj.get("clickId") != null && !jsonObj.get("clickId").isJsonNull()) && !jsonObj.get("clickId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `clickId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("clickId").toString()));
      }
      if ((jsonObj.get("content") != null && !jsonObj.get("content").isJsonNull()) && !jsonObj.get("content").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `content` to be a primitive type in the JSON string but got `%s`", jsonObj.get("content").toString()));
      }
      if ((jsonObj.get("medium") != null && !jsonObj.get("medium").isJsonNull()) && !jsonObj.get("medium").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `medium` to be a primitive type in the JSON string but got `%s`", jsonObj.get("medium").toString()));
      }
      if ((jsonObj.get("path") != null && !jsonObj.get("path").isJsonNull()) && !jsonObj.get("path").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `path` to be a primitive type in the JSON string but got `%s`", jsonObj.get("path").toString()));
      }
      if ((jsonObj.get("referrer") != null && !jsonObj.get("referrer").isJsonNull()) && !jsonObj.get("referrer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `referrer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("referrer").toString()));
      }
      if ((jsonObj.get("salesAgent") != null && !jsonObj.get("salesAgent").isJsonNull()) && !jsonObj.get("salesAgent").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `salesAgent` to be a primitive type in the JSON string but got `%s`", jsonObj.get("salesAgent").toString()));
      }
      if ((jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) && !jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
      if ((jsonObj.get("subAffiliate") != null && !jsonObj.get("subAffiliate").isJsonNull()) && !jsonObj.get("subAffiliate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subAffiliate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subAffiliate").toString()));
      }
      if ((jsonObj.get("term") != null && !jsonObj.get("term").isJsonNull()) && !jsonObj.get("term").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `term` to be a primitive type in the JSON string but got `%s`", jsonObj.get("term").toString()));
      }
      // validate the optional field `original`
      if (jsonObj.get("original") != null && !jsonObj.get("original").isJsonNull()) {
        LeadSourceData.validateJsonElement(jsonObj.get("original"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LeadSource.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LeadSource' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LeadSource> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LeadSource.class));

       return (TypeAdapter<T>) new TypeAdapter<LeadSource>() {
           @Override
           public void write(JsonWriter out, LeadSource value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public LeadSource read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LeadSource given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LeadSource
   * @throws IOException if the JSON string is invalid with respect to LeadSource
   */
  public static LeadSource fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LeadSource.class);
  }

  /**
   * Convert an instance of LeadSource to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

