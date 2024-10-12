/*
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
import org.openapitools.client.model.AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile;

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
 * AppServicePlan resource specific properties
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:52:50.309367-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AppServicePlansList200ResponseValueInnerProperties {
  public static final String SERIALIZED_NAME_FREE_OFFER_EXPIRATION_TIME = "freeOfferExpirationTime";
  @SerializedName(SERIALIZED_NAME_FREE_OFFER_EXPIRATION_TIME)
  private OffsetDateTime freeOfferExpirationTime;

  public static final String SERIALIZED_NAME_GEO_REGION = "geoRegion";
  @SerializedName(SERIALIZED_NAME_GEO_REGION)
  private String geoRegion;

  public static final String SERIALIZED_NAME_HOSTING_ENVIRONMENT_PROFILE = "hostingEnvironmentProfile";
  @SerializedName(SERIALIZED_NAME_HOSTING_ENVIRONMENT_PROFILE)
  private AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile hostingEnvironmentProfile;

  public static final String SERIALIZED_NAME_HYPER_V = "hyperV";
  @SerializedName(SERIALIZED_NAME_HYPER_V)
  private Boolean hyperV = false;

  public static final String SERIALIZED_NAME_IS_SPOT = "isSpot";
  @SerializedName(SERIALIZED_NAME_IS_SPOT)
  private Boolean isSpot;

  public static final String SERIALIZED_NAME_IS_XENON = "isXenon";
  @SerializedName(SERIALIZED_NAME_IS_XENON)
  private Boolean isXenon = false;

  public static final String SERIALIZED_NAME_MAXIMUM_ELASTIC_WORKER_COUNT = "maximumElasticWorkerCount";
  @SerializedName(SERIALIZED_NAME_MAXIMUM_ELASTIC_WORKER_COUNT)
  private Integer maximumElasticWorkerCount;

  public static final String SERIALIZED_NAME_MAXIMUM_NUMBER_OF_WORKERS = "maximumNumberOfWorkers";
  @SerializedName(SERIALIZED_NAME_MAXIMUM_NUMBER_OF_WORKERS)
  private Integer maximumNumberOfWorkers;

  public static final String SERIALIZED_NAME_NUMBER_OF_SITES = "numberOfSites";
  @SerializedName(SERIALIZED_NAME_NUMBER_OF_SITES)
  private Integer numberOfSites;

  public static final String SERIALIZED_NAME_PER_SITE_SCALING = "perSiteScaling";
  @SerializedName(SERIALIZED_NAME_PER_SITE_SCALING)
  private Boolean perSiteScaling = false;

  /**
   * Provisioning state of the App Service Environment.
   */
  @JsonAdapter(ProvisioningStateEnum.Adapter.class)
  public enum ProvisioningStateEnum {
    SUCCEEDED("Succeeded"),
    
    FAILED("Failed"),
    
    CANCELED("Canceled"),
    
    IN_PROGRESS("InProgress"),
    
    DELETING("Deleting");

    private String value;

    ProvisioningStateEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ProvisioningStateEnum fromValue(String value) {
      for (ProvisioningStateEnum b : ProvisioningStateEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ProvisioningStateEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ProvisioningStateEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ProvisioningStateEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ProvisioningStateEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ProvisioningStateEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PROVISIONING_STATE = "provisioningState";
  @SerializedName(SERIALIZED_NAME_PROVISIONING_STATE)
  private ProvisioningStateEnum provisioningState;

  public static final String SERIALIZED_NAME_RESERVED = "reserved";
  @SerializedName(SERIALIZED_NAME_RESERVED)
  private Boolean reserved = false;

  public static final String SERIALIZED_NAME_RESOURCE_GROUP = "resourceGroup";
  @SerializedName(SERIALIZED_NAME_RESOURCE_GROUP)
  private String resourceGroup;

  public static final String SERIALIZED_NAME_SPOT_EXPIRATION_TIME = "spotExpirationTime";
  @SerializedName(SERIALIZED_NAME_SPOT_EXPIRATION_TIME)
  private OffsetDateTime spotExpirationTime;

  /**
   * App Service plan status.
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    READY("Ready"),
    
    PENDING("Pending"),
    
    CREATING("Creating");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_SUBSCRIPTION = "subscription";
  @SerializedName(SERIALIZED_NAME_SUBSCRIPTION)
  private String subscription;

  public static final String SERIALIZED_NAME_TARGET_WORKER_COUNT = "targetWorkerCount";
  @SerializedName(SERIALIZED_NAME_TARGET_WORKER_COUNT)
  private Integer targetWorkerCount;

  public static final String SERIALIZED_NAME_TARGET_WORKER_SIZE_ID = "targetWorkerSizeId";
  @SerializedName(SERIALIZED_NAME_TARGET_WORKER_SIZE_ID)
  private Integer targetWorkerSizeId;

  public static final String SERIALIZED_NAME_WORKER_TIER_NAME = "workerTierName";
  @SerializedName(SERIALIZED_NAME_WORKER_TIER_NAME)
  private String workerTierName;

  public AppServicePlansList200ResponseValueInnerProperties() {
  }

  public AppServicePlansList200ResponseValueInnerProperties(
     String geoRegion, 
     Integer maximumNumberOfWorkers, 
     Integer numberOfSites, 
     ProvisioningStateEnum provisioningState, 
     String resourceGroup, 
     StatusEnum status, 
     String subscription
  ) {
    this();
    this.geoRegion = geoRegion;
    this.maximumNumberOfWorkers = maximumNumberOfWorkers;
    this.numberOfSites = numberOfSites;
    this.provisioningState = provisioningState;
    this.resourceGroup = resourceGroup;
    this.status = status;
    this.subscription = subscription;
  }

  public AppServicePlansList200ResponseValueInnerProperties freeOfferExpirationTime(OffsetDateTime freeOfferExpirationTime) {
    this.freeOfferExpirationTime = freeOfferExpirationTime;
    return this;
  }

  /**
   * The time when the server farm free offer expires.
   * @return freeOfferExpirationTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getFreeOfferExpirationTime() {
    return freeOfferExpirationTime;
  }

  public void setFreeOfferExpirationTime(OffsetDateTime freeOfferExpirationTime) {
    this.freeOfferExpirationTime = freeOfferExpirationTime;
  }


  /**
   * Geographical location for the App Service plan.
   * @return geoRegion
   */
  @javax.annotation.Nullable
  public String getGeoRegion() {
    return geoRegion;
  }



  public AppServicePlansList200ResponseValueInnerProperties hostingEnvironmentProfile(AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile hostingEnvironmentProfile) {
    this.hostingEnvironmentProfile = hostingEnvironmentProfile;
    return this;
  }

  /**
   * Get hostingEnvironmentProfile
   * @return hostingEnvironmentProfile
   */
  @javax.annotation.Nullable
  public AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile getHostingEnvironmentProfile() {
    return hostingEnvironmentProfile;
  }

  public void setHostingEnvironmentProfile(AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile hostingEnvironmentProfile) {
    this.hostingEnvironmentProfile = hostingEnvironmentProfile;
  }


  public AppServicePlansList200ResponseValueInnerProperties hyperV(Boolean hyperV) {
    this.hyperV = hyperV;
    return this;
  }

  /**
   * If Hyper-V container app service plan &lt;code&gt;true&lt;/code&gt;, &lt;code&gt;false&lt;/code&gt; otherwise.
   * @return hyperV
   */
  @javax.annotation.Nullable
  public Boolean getHyperV() {
    return hyperV;
  }

  public void setHyperV(Boolean hyperV) {
    this.hyperV = hyperV;
  }


  public AppServicePlansList200ResponseValueInnerProperties isSpot(Boolean isSpot) {
    this.isSpot = isSpot;
    return this;
  }

  /**
   * If &lt;code&gt;true&lt;/code&gt;, this App Service Plan owns spot instances.
   * @return isSpot
   */
  @javax.annotation.Nullable
  public Boolean getIsSpot() {
    return isSpot;
  }

  public void setIsSpot(Boolean isSpot) {
    this.isSpot = isSpot;
  }


  public AppServicePlansList200ResponseValueInnerProperties isXenon(Boolean isXenon) {
    this.isXenon = isXenon;
    return this;
  }

  /**
   * Obsolete: If Hyper-V container app service plan &lt;code&gt;true&lt;/code&gt;, &lt;code&gt;false&lt;/code&gt; otherwise.
   * @return isXenon
   */
  @javax.annotation.Nullable
  public Boolean getIsXenon() {
    return isXenon;
  }

  public void setIsXenon(Boolean isXenon) {
    this.isXenon = isXenon;
  }


  public AppServicePlansList200ResponseValueInnerProperties maximumElasticWorkerCount(Integer maximumElasticWorkerCount) {
    this.maximumElasticWorkerCount = maximumElasticWorkerCount;
    return this;
  }

  /**
   * Maximum number of total workers allowed for this ElasticScaleEnabled App Service Plan
   * @return maximumElasticWorkerCount
   */
  @javax.annotation.Nullable
  public Integer getMaximumElasticWorkerCount() {
    return maximumElasticWorkerCount;
  }

  public void setMaximumElasticWorkerCount(Integer maximumElasticWorkerCount) {
    this.maximumElasticWorkerCount = maximumElasticWorkerCount;
  }


  /**
   * Maximum number of instances that can be assigned to this App Service plan.
   * @return maximumNumberOfWorkers
   */
  @javax.annotation.Nullable
  public Integer getMaximumNumberOfWorkers() {
    return maximumNumberOfWorkers;
  }



  /**
   * Number of apps assigned to this App Service plan.
   * @return numberOfSites
   */
  @javax.annotation.Nullable
  public Integer getNumberOfSites() {
    return numberOfSites;
  }



  public AppServicePlansList200ResponseValueInnerProperties perSiteScaling(Boolean perSiteScaling) {
    this.perSiteScaling = perSiteScaling;
    return this;
  }

  /**
   * If &lt;code&gt;true&lt;/code&gt;, apps assigned to this App Service plan can be scaled independently. If &lt;code&gt;false&lt;/code&gt;, apps assigned to this App Service plan will scale to all instances of the plan.
   * @return perSiteScaling
   */
  @javax.annotation.Nullable
  public Boolean getPerSiteScaling() {
    return perSiteScaling;
  }

  public void setPerSiteScaling(Boolean perSiteScaling) {
    this.perSiteScaling = perSiteScaling;
  }


  /**
   * Provisioning state of the App Service Environment.
   * @return provisioningState
   */
  @javax.annotation.Nullable
  public ProvisioningStateEnum getProvisioningState() {
    return provisioningState;
  }



  public AppServicePlansList200ResponseValueInnerProperties reserved(Boolean reserved) {
    this.reserved = reserved;
    return this;
  }

  /**
   * If Linux app service plan &lt;code&gt;true&lt;/code&gt;, &lt;code&gt;false&lt;/code&gt; otherwise.
   * @return reserved
   */
  @javax.annotation.Nullable
  public Boolean getReserved() {
    return reserved;
  }

  public void setReserved(Boolean reserved) {
    this.reserved = reserved;
  }


  /**
   * Resource group of the App Service plan.
   * @return resourceGroup
   */
  @javax.annotation.Nullable
  public String getResourceGroup() {
    return resourceGroup;
  }



  public AppServicePlansList200ResponseValueInnerProperties spotExpirationTime(OffsetDateTime spotExpirationTime) {
    this.spotExpirationTime = spotExpirationTime;
    return this;
  }

  /**
   * The time when the server farm expires. Valid only if it is a spot server farm.
   * @return spotExpirationTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getSpotExpirationTime() {
    return spotExpirationTime;
  }

  public void setSpotExpirationTime(OffsetDateTime spotExpirationTime) {
    this.spotExpirationTime = spotExpirationTime;
  }


  /**
   * App Service plan status.
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }



  /**
   * App Service plan subscription.
   * @return subscription
   */
  @javax.annotation.Nullable
  public String getSubscription() {
    return subscription;
  }



  public AppServicePlansList200ResponseValueInnerProperties targetWorkerCount(Integer targetWorkerCount) {
    this.targetWorkerCount = targetWorkerCount;
    return this;
  }

  /**
   * Scaling worker count.
   * @return targetWorkerCount
   */
  @javax.annotation.Nullable
  public Integer getTargetWorkerCount() {
    return targetWorkerCount;
  }

  public void setTargetWorkerCount(Integer targetWorkerCount) {
    this.targetWorkerCount = targetWorkerCount;
  }


  public AppServicePlansList200ResponseValueInnerProperties targetWorkerSizeId(Integer targetWorkerSizeId) {
    this.targetWorkerSizeId = targetWorkerSizeId;
    return this;
  }

  /**
   * Scaling worker size ID.
   * @return targetWorkerSizeId
   */
  @javax.annotation.Nullable
  public Integer getTargetWorkerSizeId() {
    return targetWorkerSizeId;
  }

  public void setTargetWorkerSizeId(Integer targetWorkerSizeId) {
    this.targetWorkerSizeId = targetWorkerSizeId;
  }


  public AppServicePlansList200ResponseValueInnerProperties workerTierName(String workerTierName) {
    this.workerTierName = workerTierName;
    return this;
  }

  /**
   * Target worker tier assigned to the App Service plan.
   * @return workerTierName
   */
  @javax.annotation.Nullable
  public String getWorkerTierName() {
    return workerTierName;
  }

  public void setWorkerTierName(String workerTierName) {
    this.workerTierName = workerTierName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AppServicePlansList200ResponseValueInnerProperties appServicePlansList200ResponseValueInnerProperties = (AppServicePlansList200ResponseValueInnerProperties) o;
    return Objects.equals(this.freeOfferExpirationTime, appServicePlansList200ResponseValueInnerProperties.freeOfferExpirationTime) &&
        Objects.equals(this.geoRegion, appServicePlansList200ResponseValueInnerProperties.geoRegion) &&
        Objects.equals(this.hostingEnvironmentProfile, appServicePlansList200ResponseValueInnerProperties.hostingEnvironmentProfile) &&
        Objects.equals(this.hyperV, appServicePlansList200ResponseValueInnerProperties.hyperV) &&
        Objects.equals(this.isSpot, appServicePlansList200ResponseValueInnerProperties.isSpot) &&
        Objects.equals(this.isXenon, appServicePlansList200ResponseValueInnerProperties.isXenon) &&
        Objects.equals(this.maximumElasticWorkerCount, appServicePlansList200ResponseValueInnerProperties.maximumElasticWorkerCount) &&
        Objects.equals(this.maximumNumberOfWorkers, appServicePlansList200ResponseValueInnerProperties.maximumNumberOfWorkers) &&
        Objects.equals(this.numberOfSites, appServicePlansList200ResponseValueInnerProperties.numberOfSites) &&
        Objects.equals(this.perSiteScaling, appServicePlansList200ResponseValueInnerProperties.perSiteScaling) &&
        Objects.equals(this.provisioningState, appServicePlansList200ResponseValueInnerProperties.provisioningState) &&
        Objects.equals(this.reserved, appServicePlansList200ResponseValueInnerProperties.reserved) &&
        Objects.equals(this.resourceGroup, appServicePlansList200ResponseValueInnerProperties.resourceGroup) &&
        Objects.equals(this.spotExpirationTime, appServicePlansList200ResponseValueInnerProperties.spotExpirationTime) &&
        Objects.equals(this.status, appServicePlansList200ResponseValueInnerProperties.status) &&
        Objects.equals(this.subscription, appServicePlansList200ResponseValueInnerProperties.subscription) &&
        Objects.equals(this.targetWorkerCount, appServicePlansList200ResponseValueInnerProperties.targetWorkerCount) &&
        Objects.equals(this.targetWorkerSizeId, appServicePlansList200ResponseValueInnerProperties.targetWorkerSizeId) &&
        Objects.equals(this.workerTierName, appServicePlansList200ResponseValueInnerProperties.workerTierName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(freeOfferExpirationTime, geoRegion, hostingEnvironmentProfile, hyperV, isSpot, isXenon, maximumElasticWorkerCount, maximumNumberOfWorkers, numberOfSites, perSiteScaling, provisioningState, reserved, resourceGroup, spotExpirationTime, status, subscription, targetWorkerCount, targetWorkerSizeId, workerTierName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AppServicePlansList200ResponseValueInnerProperties {\n");
    sb.append("    freeOfferExpirationTime: ").append(toIndentedString(freeOfferExpirationTime)).append("\n");
    sb.append("    geoRegion: ").append(toIndentedString(geoRegion)).append("\n");
    sb.append("    hostingEnvironmentProfile: ").append(toIndentedString(hostingEnvironmentProfile)).append("\n");
    sb.append("    hyperV: ").append(toIndentedString(hyperV)).append("\n");
    sb.append("    isSpot: ").append(toIndentedString(isSpot)).append("\n");
    sb.append("    isXenon: ").append(toIndentedString(isXenon)).append("\n");
    sb.append("    maximumElasticWorkerCount: ").append(toIndentedString(maximumElasticWorkerCount)).append("\n");
    sb.append("    maximumNumberOfWorkers: ").append(toIndentedString(maximumNumberOfWorkers)).append("\n");
    sb.append("    numberOfSites: ").append(toIndentedString(numberOfSites)).append("\n");
    sb.append("    perSiteScaling: ").append(toIndentedString(perSiteScaling)).append("\n");
    sb.append("    provisioningState: ").append(toIndentedString(provisioningState)).append("\n");
    sb.append("    reserved: ").append(toIndentedString(reserved)).append("\n");
    sb.append("    resourceGroup: ").append(toIndentedString(resourceGroup)).append("\n");
    sb.append("    spotExpirationTime: ").append(toIndentedString(spotExpirationTime)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subscription: ").append(toIndentedString(subscription)).append("\n");
    sb.append("    targetWorkerCount: ").append(toIndentedString(targetWorkerCount)).append("\n");
    sb.append("    targetWorkerSizeId: ").append(toIndentedString(targetWorkerSizeId)).append("\n");
    sb.append("    workerTierName: ").append(toIndentedString(workerTierName)).append("\n");
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
    openapiFields.add("freeOfferExpirationTime");
    openapiFields.add("geoRegion");
    openapiFields.add("hostingEnvironmentProfile");
    openapiFields.add("hyperV");
    openapiFields.add("isSpot");
    openapiFields.add("isXenon");
    openapiFields.add("maximumElasticWorkerCount");
    openapiFields.add("maximumNumberOfWorkers");
    openapiFields.add("numberOfSites");
    openapiFields.add("perSiteScaling");
    openapiFields.add("provisioningState");
    openapiFields.add("reserved");
    openapiFields.add("resourceGroup");
    openapiFields.add("spotExpirationTime");
    openapiFields.add("status");
    openapiFields.add("subscription");
    openapiFields.add("targetWorkerCount");
    openapiFields.add("targetWorkerSizeId");
    openapiFields.add("workerTierName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AppServicePlansList200ResponseValueInnerProperties
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AppServicePlansList200ResponseValueInnerProperties.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AppServicePlansList200ResponseValueInnerProperties is not found in the empty JSON string", AppServicePlansList200ResponseValueInnerProperties.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AppServicePlansList200ResponseValueInnerProperties.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AppServicePlansList200ResponseValueInnerProperties` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("geoRegion") != null && !jsonObj.get("geoRegion").isJsonNull()) && !jsonObj.get("geoRegion").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `geoRegion` to be a primitive type in the JSON string but got `%s`", jsonObj.get("geoRegion").toString()));
      }
      // validate the optional field `hostingEnvironmentProfile`
      if (jsonObj.get("hostingEnvironmentProfile") != null && !jsonObj.get("hostingEnvironmentProfile").isJsonNull()) {
        AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile.validateJsonElement(jsonObj.get("hostingEnvironmentProfile"));
      }
      if ((jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) && !jsonObj.get("provisioningState").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `provisioningState` to be a primitive type in the JSON string but got `%s`", jsonObj.get("provisioningState").toString()));
      }
      // validate the optional field `provisioningState`
      if (jsonObj.get("provisioningState") != null && !jsonObj.get("provisioningState").isJsonNull()) {
        ProvisioningStateEnum.validateJsonElement(jsonObj.get("provisioningState"));
      }
      if ((jsonObj.get("resourceGroup") != null && !jsonObj.get("resourceGroup").isJsonNull()) && !jsonObj.get("resourceGroup").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `resourceGroup` to be a primitive type in the JSON string but got `%s`", jsonObj.get("resourceGroup").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("subscription") != null && !jsonObj.get("subscription").isJsonNull()) && !jsonObj.get("subscription").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subscription` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subscription").toString()));
      }
      if ((jsonObj.get("workerTierName") != null && !jsonObj.get("workerTierName").isJsonNull()) && !jsonObj.get("workerTierName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `workerTierName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("workerTierName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AppServicePlansList200ResponseValueInnerProperties.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AppServicePlansList200ResponseValueInnerProperties' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AppServicePlansList200ResponseValueInnerProperties> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AppServicePlansList200ResponseValueInnerProperties.class));

       return (TypeAdapter<T>) new TypeAdapter<AppServicePlansList200ResponseValueInnerProperties>() {
           @Override
           public void write(JsonWriter out, AppServicePlansList200ResponseValueInnerProperties value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AppServicePlansList200ResponseValueInnerProperties read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AppServicePlansList200ResponseValueInnerProperties given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AppServicePlansList200ResponseValueInnerProperties
   * @throws IOException if the JSON string is invalid with respect to AppServicePlansList200ResponseValueInnerProperties
   */
  public static AppServicePlansList200ResponseValueInnerProperties fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AppServicePlansList200ResponseValueInnerProperties.class);
  }

  /**
   * Convert an instance of AppServicePlansList200ResponseValueInnerProperties to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

