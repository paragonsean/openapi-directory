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
 * This contains all routing specific configurations.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Routing {
  public static final String SERIALIZED_NAME_CALC_POINTS = "calc_points";
  @SerializedName(SERIALIZED_NAME_CALC_POINTS)
  private Boolean calcPoints = false;

  public static final String SERIALIZED_NAME_CONSIDER_TRAFFIC = "consider_traffic";
  @SerializedName(SERIALIZED_NAME_CONSIDER_TRAFFIC)
  private Boolean considerTraffic = false;

  /**
   * In some cases curbside constraints cannot be fulfilled. For example in one-way streets you cannot arrive at a building that is on the left side of the street such that the building is to the right of you (unless you drove the one-way street the wrong/illegal way). You can set the &#x60;curbside_strictness&#x60; to &#x60;soft&#x60; to ignore the curbside constraint in such cases or set it to &#x60;strict&#x60; to get an error response instead. You can also set it to &#x60;ignore&#x60; to ignore all curbside constraints (this is useful to compare the results with and without constraints without modifying every single address).
   */
  @JsonAdapter(CurbsideStrictnessEnum.Adapter.class)
  public enum CurbsideStrictnessEnum {
    IGNORE("ignore"),
    
    SOFT("soft"),
    
    STRICT("strict");

    private String value;

    CurbsideStrictnessEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CurbsideStrictnessEnum fromValue(String value) {
      for (CurbsideStrictnessEnum b : CurbsideStrictnessEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CurbsideStrictnessEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CurbsideStrictnessEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CurbsideStrictnessEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CurbsideStrictnessEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CurbsideStrictnessEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CURBSIDE_STRICTNESS = "curbside_strictness";
  @SerializedName(SERIALIZED_NAME_CURBSIDE_STRICTNESS)
  private CurbsideStrictnessEnum curbsideStrictness = CurbsideStrictnessEnum.SOFT;

  public static final String SERIALIZED_NAME_FAIL_FAST = "fail_fast";
  @SerializedName(SERIALIZED_NAME_FAIL_FAST)
  private Boolean failFast = true;

  /**
   * specifies the data provider, read more about it [here](#section/Map-Data-and-Routing-Profiles).
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

  public static final String SERIALIZED_NAME_RETURN_SNAPPED_WAYPOINTS = "return_snapped_waypoints";
  @SerializedName(SERIALIZED_NAME_RETURN_SNAPPED_WAYPOINTS)
  private Boolean returnSnappedWaypoints = false;

  /**
   * Gets or Sets snapPreventions
   */
  @JsonAdapter(SnapPreventionsEnum.Adapter.class)
  public enum SnapPreventionsEnum {
    MOTORWAY("motorway"),
    
    TRUNK("trunk"),
    
    BRIDGE("bridge"),
    
    FORD("ford"),
    
    TUNNEL("tunnel"),
    
    FERRY("ferry");

    private String value;

    SnapPreventionsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static SnapPreventionsEnum fromValue(String value) {
      for (SnapPreventionsEnum b : SnapPreventionsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<SnapPreventionsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final SnapPreventionsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public SnapPreventionsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return SnapPreventionsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      SnapPreventionsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SNAP_PREVENTIONS = "snap_preventions";
  @SerializedName(SERIALIZED_NAME_SNAP_PREVENTIONS)
  private List<SnapPreventionsEnum> snapPreventions = new ArrayList<>();

  public Routing() {
  }

  public Routing calcPoints(Boolean calcPoints) {
    this.calcPoints = calcPoints;
    return this;
  }

  /**
   * It lets you specify whether the API should provide you with route geometries for vehicle routes or not. Thus, you do not need to do extra routing to get the polyline for each route.
   * @return calcPoints
   */
  @javax.annotation.Nullable
  public Boolean getCalcPoints() {
    return calcPoints;
  }

  public void setCalcPoints(Boolean calcPoints) {
    this.calcPoints = calcPoints;
  }


  public Routing considerTraffic(Boolean considerTraffic) {
    this.considerTraffic = considerTraffic;
    return this;
  }

  /**
   * indicates whether historical traffic information should be considered
   * @return considerTraffic
   */
  @javax.annotation.Nullable
  public Boolean getConsiderTraffic() {
    return considerTraffic;
  }

  public void setConsiderTraffic(Boolean considerTraffic) {
    this.considerTraffic = considerTraffic;
  }


  public Routing curbsideStrictness(CurbsideStrictnessEnum curbsideStrictness) {
    this.curbsideStrictness = curbsideStrictness;
    return this;
  }

  /**
   * In some cases curbside constraints cannot be fulfilled. For example in one-way streets you cannot arrive at a building that is on the left side of the street such that the building is to the right of you (unless you drove the one-way street the wrong/illegal way). You can set the &#x60;curbside_strictness&#x60; to &#x60;soft&#x60; to ignore the curbside constraint in such cases or set it to &#x60;strict&#x60; to get an error response instead. You can also set it to &#x60;ignore&#x60; to ignore all curbside constraints (this is useful to compare the results with and without constraints without modifying every single address).
   * @return curbsideStrictness
   */
  @javax.annotation.Nullable
  public CurbsideStrictnessEnum getCurbsideStrictness() {
    return curbsideStrictness;
  }

  public void setCurbsideStrictness(CurbsideStrictnessEnum curbsideStrictness) {
    this.curbsideStrictness = curbsideStrictness;
  }


  public Routing failFast(Boolean failFast) {
    this.failFast = failFast;
    return this;
  }

  /**
   * indicates whether matrix calculation should fail fast when points cannot be connected
   * @return failFast
   */
  @javax.annotation.Nullable
  public Boolean getFailFast() {
    return failFast;
  }

  public void setFailFast(Boolean failFast) {
    this.failFast = failFast;
  }


  public Routing networkDataProvider(NetworkDataProviderEnum networkDataProvider) {
    this.networkDataProvider = networkDataProvider;
    return this;
  }

  /**
   * specifies the data provider, read more about it [here](#section/Map-Data-and-Routing-Profiles).
   * @return networkDataProvider
   */
  @javax.annotation.Nullable
  public NetworkDataProviderEnum getNetworkDataProvider() {
    return networkDataProvider;
  }

  public void setNetworkDataProvider(NetworkDataProviderEnum networkDataProvider) {
    this.networkDataProvider = networkDataProvider;
  }


  public Routing returnSnappedWaypoints(Boolean returnSnappedWaypoints) {
    this.returnSnappedWaypoints = returnSnappedWaypoints;
    return this;
  }

  /**
   * Indicates whether a solution includes snapped waypoints. In contrary to the address coordinate a snapped waypoint is the access point to the (road) network.
   * @return returnSnappedWaypoints
   */
  @javax.annotation.Nullable
  public Boolean getReturnSnappedWaypoints() {
    return returnSnappedWaypoints;
  }

  public void setReturnSnappedWaypoints(Boolean returnSnappedWaypoints) {
    this.returnSnappedWaypoints = returnSnappedWaypoints;
  }


  public Routing snapPreventions(List<SnapPreventionsEnum> snapPreventions) {
    this.snapPreventions = snapPreventions;
    return this;
  }

  public Routing addSnapPreventionsItem(SnapPreventionsEnum snapPreventionsItem) {
    if (this.snapPreventions == null) {
      this.snapPreventions = new ArrayList<>();
    }
    this.snapPreventions.add(snapPreventionsItem);
    return this;
  }

  /**
   * Prevents snapping locations to road links of specified road types, e.g. to motorway.
   * @return snapPreventions
   */
  @javax.annotation.Nullable
  public List<SnapPreventionsEnum> getSnapPreventions() {
    return snapPreventions;
  }

  public void setSnapPreventions(List<SnapPreventionsEnum> snapPreventions) {
    this.snapPreventions = snapPreventions;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Routing routing = (Routing) o;
    return Objects.equals(this.calcPoints, routing.calcPoints) &&
        Objects.equals(this.considerTraffic, routing.considerTraffic) &&
        Objects.equals(this.curbsideStrictness, routing.curbsideStrictness) &&
        Objects.equals(this.failFast, routing.failFast) &&
        Objects.equals(this.networkDataProvider, routing.networkDataProvider) &&
        Objects.equals(this.returnSnappedWaypoints, routing.returnSnappedWaypoints) &&
        Objects.equals(this.snapPreventions, routing.snapPreventions);
  }

  @Override
  public int hashCode() {
    return Objects.hash(calcPoints, considerTraffic, curbsideStrictness, failFast, networkDataProvider, returnSnappedWaypoints, snapPreventions);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Routing {\n");
    sb.append("    calcPoints: ").append(toIndentedString(calcPoints)).append("\n");
    sb.append("    considerTraffic: ").append(toIndentedString(considerTraffic)).append("\n");
    sb.append("    curbsideStrictness: ").append(toIndentedString(curbsideStrictness)).append("\n");
    sb.append("    failFast: ").append(toIndentedString(failFast)).append("\n");
    sb.append("    networkDataProvider: ").append(toIndentedString(networkDataProvider)).append("\n");
    sb.append("    returnSnappedWaypoints: ").append(toIndentedString(returnSnappedWaypoints)).append("\n");
    sb.append("    snapPreventions: ").append(toIndentedString(snapPreventions)).append("\n");
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
    openapiFields.add("calc_points");
    openapiFields.add("consider_traffic");
    openapiFields.add("curbside_strictness");
    openapiFields.add("fail_fast");
    openapiFields.add("network_data_provider");
    openapiFields.add("return_snapped_waypoints");
    openapiFields.add("snap_preventions");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Routing
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Routing.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Routing is not found in the empty JSON string", Routing.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Routing.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Routing` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("curbside_strictness") != null && !jsonObj.get("curbside_strictness").isJsonNull()) && !jsonObj.get("curbside_strictness").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `curbside_strictness` to be a primitive type in the JSON string but got `%s`", jsonObj.get("curbside_strictness").toString()));
      }
      // validate the optional field `curbside_strictness`
      if (jsonObj.get("curbside_strictness") != null && !jsonObj.get("curbside_strictness").isJsonNull()) {
        CurbsideStrictnessEnum.validateJsonElement(jsonObj.get("curbside_strictness"));
      }
      if ((jsonObj.get("network_data_provider") != null && !jsonObj.get("network_data_provider").isJsonNull()) && !jsonObj.get("network_data_provider").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `network_data_provider` to be a primitive type in the JSON string but got `%s`", jsonObj.get("network_data_provider").toString()));
      }
      // validate the optional field `network_data_provider`
      if (jsonObj.get("network_data_provider") != null && !jsonObj.get("network_data_provider").isJsonNull()) {
        NetworkDataProviderEnum.validateJsonElement(jsonObj.get("network_data_provider"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("snap_preventions") != null && !jsonObj.get("snap_preventions").isJsonNull() && !jsonObj.get("snap_preventions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `snap_preventions` to be an array in the JSON string but got `%s`", jsonObj.get("snap_preventions").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Routing.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Routing' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Routing> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Routing.class));

       return (TypeAdapter<T>) new TypeAdapter<Routing>() {
           @Override
           public void write(JsonWriter out, Routing value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Routing read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Routing given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Routing
   * @throws IOException if the JSON string is invalid with respect to Routing
   */
  public static Routing fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Routing.class);
  }

  /**
   * Convert an instance of Routing to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

