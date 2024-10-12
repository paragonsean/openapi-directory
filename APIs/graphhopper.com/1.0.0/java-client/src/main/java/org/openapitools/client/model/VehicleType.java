/*
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
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
 * VehicleType
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VehicleType {
  public static final String SERIALIZED_NAME_CAPACITY = "capacity";
  @SerializedName(SERIALIZED_NAME_CAPACITY)
  private List<Integer> capacity = new ArrayList<>(Arrays.asList(0));

  public static final String SERIALIZED_NAME_CONSIDER_TRAFFIC = "consider_traffic";
  @SerializedName(SERIALIZED_NAME_CONSIDER_TRAFFIC)
  private Boolean considerTraffic = false;

  public static final String SERIALIZED_NAME_COST_PER_ACTIVATION = "cost_per_activation";
  @SerializedName(SERIALIZED_NAME_COST_PER_ACTIVATION)
  private Double costPerActivation;

  public static final String SERIALIZED_NAME_COST_PER_METER = "cost_per_meter";
  @SerializedName(SERIALIZED_NAME_COST_PER_METER)
  private Double costPerMeter;

  public static final String SERIALIZED_NAME_COST_PER_SECOND = "cost_per_second";
  @SerializedName(SERIALIZED_NAME_COST_PER_SECOND)
  private Double costPerSecond;

  /**
   * Specifies the network data provider. Either use [&#x60;openstreetmap&#x60;](#section/Map-Data-and-Routing-Profiles/OpenStreetMap) (default) or [&#x60;tomtom&#x60;](#section/Map-Data-and-Routing-Profiles/TomTom) (add-on required).
   */
  @JsonAdapter(NetworkDataProviderEnum.Adapter.class)
  public enum NetworkDataProviderEnum {
    OPENSTREETMAP("openstreetmap"),
    
    TOMTOM("tomtom");

    private String value;

    NetworkDataProviderEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static NetworkDataProviderEnum fromValue(String value) {
      for (NetworkDataProviderEnum b : NetworkDataProviderEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<NetworkDataProviderEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final NetworkDataProviderEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public NetworkDataProviderEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return NetworkDataProviderEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      NetworkDataProviderEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_NETWORK_DATA_PROVIDER = "network_data_provider";
  @SerializedName(SERIALIZED_NAME_NETWORK_DATA_PROVIDER)
  private NetworkDataProviderEnum networkDataProvider = NetworkDataProviderEnum.OPENSTREETMAP;

  public static final String SERIALIZED_NAME_PROFILE = "profile";
  @SerializedName(SERIALIZED_NAME_PROFILE)
  private Object profile;

  public static final String SERIALIZED_NAME_SERVICE_TIME_FACTOR = "service_time_factor";
  @SerializedName(SERIALIZED_NAME_SERVICE_TIME_FACTOR)
  private Double serviceTimeFactor = 1d;

  public static final String SERIALIZED_NAME_SPEED_FACTOR = "speed_factor";
  @SerializedName(SERIALIZED_NAME_SPEED_FACTOR)
  private Double speedFactor = 1d;

  public static final String SERIALIZED_NAME_TYPE_ID = "type_id";
  @SerializedName(SERIALIZED_NAME_TYPE_ID)
  private String typeId;

  public VehicleType() {
  }

  public VehicleType capacity(List<Integer> capacity) {
    this.capacity = capacity;
    return this;
  }

  public VehicleType addCapacityItem(Integer capacityItem) {
    if (this.capacity == null) {
      this.capacity = new ArrayList<>(Arrays.asList(0));
    }
    this.capacity.add(capacityItem);
    return this;
  }

  /**
   * Specifies an array of capacity dimension values which need to be int values. For example, if there are two dimensions such as volume and weight then it needs to be defined as [ 1000, 300 ] assuming a maximum volume of 1000 and a maximum weight of 300.
   * @return capacity
   */
  @javax.annotation.Nullable
  public List<Integer> getCapacity() {
    return capacity;
  }

  public void setCapacity(List<Integer> capacity) {
    this.capacity = capacity;
  }


  public VehicleType considerTraffic(Boolean considerTraffic) {
    this.considerTraffic = considerTraffic;
    return this;
  }

  /**
   * Specifies whether traffic should be considered. if \&quot;tomtom\&quot; is used and this is false, free flow travel times from \&quot;tomtom\&quot; are calculated. If this is true, historical traffic info are used. We do not yet have traffic data for \&quot;openstreetmap\&quot;, thus, setting this true has no effect at all.
   * @return considerTraffic
   */
  @javax.annotation.Nullable
  public Boolean getConsiderTraffic() {
    return considerTraffic;
  }

  public void setConsiderTraffic(Boolean considerTraffic) {
    this.considerTraffic = considerTraffic;
  }


  public VehicleType costPerActivation(Double costPerActivation) {
    this.costPerActivation = costPerActivation;
    return this;
  }

  /**
   * **_BETA feature_**! Cost parameter vehicle activation, i.e. fixed costs per vehicle
   * @return costPerActivation
   */
  @javax.annotation.Nullable
  public Double getCostPerActivation() {
    return costPerActivation;
  }

  public void setCostPerActivation(Double costPerActivation) {
    this.costPerActivation = costPerActivation;
  }


  public VehicleType costPerMeter(Double costPerMeter) {
    this.costPerMeter = costPerMeter;
    return this;
  }

  /**
   * **_BETA feature_**! Cost parameter per distance unit, here meter is used
   * @return costPerMeter
   */
  @javax.annotation.Nullable
  public Double getCostPerMeter() {
    return costPerMeter;
  }

  public void setCostPerMeter(Double costPerMeter) {
    this.costPerMeter = costPerMeter;
  }


  public VehicleType costPerSecond(Double costPerSecond) {
    this.costPerSecond = costPerSecond;
    return this;
  }

  /**
   * **_BETA feature_**! Cost parameter per time unit, here second is used
   * @return costPerSecond
   */
  @javax.annotation.Nullable
  public Double getCostPerSecond() {
    return costPerSecond;
  }

  public void setCostPerSecond(Double costPerSecond) {
    this.costPerSecond = costPerSecond;
  }


  public VehicleType networkDataProvider(NetworkDataProviderEnum networkDataProvider) {
    this.networkDataProvider = networkDataProvider;
    return this;
  }

  /**
   * Specifies the network data provider. Either use [&#x60;openstreetmap&#x60;](#section/Map-Data-and-Routing-Profiles/OpenStreetMap) (default) or [&#x60;tomtom&#x60;](#section/Map-Data-and-Routing-Profiles/TomTom) (add-on required).
   * @return networkDataProvider
   */
  @javax.annotation.Nullable
  public NetworkDataProviderEnum getNetworkDataProvider() {
    return networkDataProvider;
  }

  public void setNetworkDataProvider(NetworkDataProviderEnum networkDataProvider) {
    this.networkDataProvider = networkDataProvider;
  }


  public VehicleType profile(Object profile) {
    this.profile = profile;
    return this;
  }

  /**
   * Get profile
   * @return profile
   */
  @javax.annotation.Nullable
  public Object getProfile() {
    return profile;
  }

  public void setProfile(Object profile) {
    this.profile = profile;
  }


  public VehicleType serviceTimeFactor(Double serviceTimeFactor) {
    this.serviceTimeFactor = serviceTimeFactor;
    return this;
  }

  /**
   * Specifies a service time factor for this vehicle type. If the vehicle/driver that uses this type is able to conduct the service as double as fast as it is determined in the corresponding service or shipment then set it to 0.5.
   * @return serviceTimeFactor
   */
  @javax.annotation.Nullable
  public Double getServiceTimeFactor() {
    return serviceTimeFactor;
  }

  public void setServiceTimeFactor(Double serviceTimeFactor) {
    this.serviceTimeFactor = serviceTimeFactor;
  }


  public VehicleType speedFactor(Double speedFactor) {
    this.speedFactor = speedFactor;
    return this;
  }

  /**
   * Specifies a speed factor for this vehicle type. If the vehicle that uses this type needs to be only half as fast as what is actually calculated with our routing engine then set the speed factor to 0.5.
   * @return speedFactor
   */
  @javax.annotation.Nullable
  public Double getSpeedFactor() {
    return speedFactor;
  }

  public void setSpeedFactor(Double speedFactor) {
    this.speedFactor = speedFactor;
  }


  public VehicleType typeId(String typeId) {
    this.typeId = typeId;
    return this;
  }

  /**
   * Specifies the id of the vehicle type. If a vehicle needs to be of this type, it should refer to this with its type_id attribute.
   * @return typeId
   */
  @javax.annotation.Nonnull
  public String getTypeId() {
    return typeId;
  }

  public void setTypeId(String typeId) {
    this.typeId = typeId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleType vehicleType = (VehicleType) o;
    return Objects.equals(this.capacity, vehicleType.capacity) &&
        Objects.equals(this.considerTraffic, vehicleType.considerTraffic) &&
        Objects.equals(this.costPerActivation, vehicleType.costPerActivation) &&
        Objects.equals(this.costPerMeter, vehicleType.costPerMeter) &&
        Objects.equals(this.costPerSecond, vehicleType.costPerSecond) &&
        Objects.equals(this.networkDataProvider, vehicleType.networkDataProvider) &&
        Objects.equals(this.profile, vehicleType.profile) &&
        Objects.equals(this.serviceTimeFactor, vehicleType.serviceTimeFactor) &&
        Objects.equals(this.speedFactor, vehicleType.speedFactor) &&
        Objects.equals(this.typeId, vehicleType.typeId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(capacity, considerTraffic, costPerActivation, costPerMeter, costPerSecond, networkDataProvider, profile, serviceTimeFactor, speedFactor, typeId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleType {\n");
    sb.append("    capacity: ").append(toIndentedString(capacity)).append("\n");
    sb.append("    considerTraffic: ").append(toIndentedString(considerTraffic)).append("\n");
    sb.append("    costPerActivation: ").append(toIndentedString(costPerActivation)).append("\n");
    sb.append("    costPerMeter: ").append(toIndentedString(costPerMeter)).append("\n");
    sb.append("    costPerSecond: ").append(toIndentedString(costPerSecond)).append("\n");
    sb.append("    networkDataProvider: ").append(toIndentedString(networkDataProvider)).append("\n");
    sb.append("    profile: ").append(toIndentedString(profile)).append("\n");
    sb.append("    serviceTimeFactor: ").append(toIndentedString(serviceTimeFactor)).append("\n");
    sb.append("    speedFactor: ").append(toIndentedString(speedFactor)).append("\n");
    sb.append("    typeId: ").append(toIndentedString(typeId)).append("\n");
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
    openapiFields.add("capacity");
    openapiFields.add("consider_traffic");
    openapiFields.add("cost_per_activation");
    openapiFields.add("cost_per_meter");
    openapiFields.add("cost_per_second");
    openapiFields.add("network_data_provider");
    openapiFields.add("profile");
    openapiFields.add("service_time_factor");
    openapiFields.add("speed_factor");
    openapiFields.add("type_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("type_id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VehicleType
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VehicleType.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VehicleType is not found in the empty JSON string", VehicleType.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VehicleType.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VehicleType` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : VehicleType.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("capacity") != null && !jsonObj.get("capacity").isJsonNull() && !jsonObj.get("capacity").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `capacity` to be an array in the JSON string but got `%s`", jsonObj.get("capacity").toString()));
      }
      if ((jsonObj.get("network_data_provider") != null && !jsonObj.get("network_data_provider").isJsonNull()) && !jsonObj.get("network_data_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `network_data_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("network_data_provider").toString()));
      }
      // validate the optional field `network_data_provider`
      if (jsonObj.get("network_data_provider") != null && !jsonObj.get("network_data_provider").isJsonNull()) {
        NetworkDataProviderEnum.validateJsonElement(jsonObj.get("network_data_provider"));
      }
      // validate the optional field `profile`
      if (jsonObj.get("profile") != null && !jsonObj.get("profile").isJsonNull()) {
        Object.validateJsonElement(jsonObj.get("profile"));
      }
      if (!jsonObj.get("type_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VehicleType.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VehicleType' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VehicleType> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VehicleType.class));

       return (TypeAdapter<T>) new TypeAdapter<VehicleType>() {
           @Override
           public void write(JsonWriter out, VehicleType value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VehicleType read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VehicleType given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VehicleType
   * @throws IOException if the JSON string is invalid with respect to VehicleType
   */
  public static VehicleType fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VehicleType.class);
  }

  /**
   * Convert an instance of VehicleType to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

