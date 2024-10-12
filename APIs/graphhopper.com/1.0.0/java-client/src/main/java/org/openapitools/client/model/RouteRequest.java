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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.VehicleProfileId;

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
 * RouteRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class RouteRequest {
  /**
   * Rather than looking for the shortest or fastest path, this lets you solve two different problems related to routing: With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. This requires &#x60;ch.disable&#x3D;true&#x60;. With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other. You can control both of these features with additional parameters, see below. 
   */
  @JsonAdapter(AlgorithmEnum.Adapter.class)
  public enum AlgorithmEnum {
    ROUND_TRIP("round_trip"),
    
    ALTERNATIVE_ROUTE("alternative_route");

    private String value;

    AlgorithmEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AlgorithmEnum fromValue(String value) {
      for (AlgorithmEnum b : AlgorithmEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AlgorithmEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AlgorithmEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AlgorithmEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AlgorithmEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AlgorithmEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ALGORITHM = "algorithm";
  @SerializedName(SERIALIZED_NAME_ALGORITHM)
  private AlgorithmEnum algorithm;

  public static final String SERIALIZED_NAME_ALTERNATIVE_ROUTE_MAX_PATHS = "alternative_route.max_paths";
  @SerializedName(SERIALIZED_NAME_ALTERNATIVE_ROUTE_MAX_PATHS)
  private Integer alternativeRouteMaxPaths = 2;

  public static final String SERIALIZED_NAME_ALTERNATIVE_ROUTE_MAX_SHARE_FACTOR = "alternative_route.max_share_factor";
  @SerializedName(SERIALIZED_NAME_ALTERNATIVE_ROUTE_MAX_SHARE_FACTOR)
  private BigDecimal alternativeRouteMaxShareFactor = new BigDecimal("0.6");

  public static final String SERIALIZED_NAME_ALTERNATIVE_ROUTE_MAX_WEIGHT_FACTOR = "alternative_route.max_weight_factor";
  @SerializedName(SERIALIZED_NAME_ALTERNATIVE_ROUTE_MAX_WEIGHT_FACTOR)
  private BigDecimal alternativeRouteMaxWeightFactor = new BigDecimal("1.4");

  public static final String SERIALIZED_NAME_AVOID = "avoid";
  @SerializedName(SERIALIZED_NAME_AVOID)
  private String avoid;

  public static final String SERIALIZED_NAME_BLOCK_AREA = "block_area";
  @SerializedName(SERIALIZED_NAME_BLOCK_AREA)
  private String blockArea;

  public static final String SERIALIZED_NAME_CALC_POINTS = "calc_points";
  @SerializedName(SERIALIZED_NAME_CALC_POINTS)
  private Boolean calcPoints = true;

  public static final String SERIALIZED_NAME_CH_DISABLE = "ch.disable";
  @SerializedName(SERIALIZED_NAME_CH_DISABLE)
  private Boolean chDisable = false;

  /**
   * Gets or Sets curbsides
   */
  @JsonAdapter(CurbsidesEnum.Adapter.class)
  public enum CurbsidesEnum {
    ANY("any"),
    
    RIGHT("right"),
    
    LEFT("left");

    private String value;

    CurbsidesEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static CurbsidesEnum fromValue(String value) {
      for (CurbsidesEnum b : CurbsidesEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<CurbsidesEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final CurbsidesEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public CurbsidesEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return CurbsidesEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      CurbsidesEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_CURBSIDES = "curbsides";
  @SerializedName(SERIALIZED_NAME_CURBSIDES)
  private List<CurbsidesEnum> curbsides = new ArrayList<>();

  public static final String SERIALIZED_NAME_DEBUG = "debug";
  @SerializedName(SERIALIZED_NAME_DEBUG)
  private Boolean debug = false;

  public static final String SERIALIZED_NAME_DETAILS = "details";
  @SerializedName(SERIALIZED_NAME_DETAILS)
  private List<String> details = new ArrayList<>();

  public static final String SERIALIZED_NAME_ELEVATION = "elevation";
  @SerializedName(SERIALIZED_NAME_ELEVATION)
  private Boolean elevation = false;

  public static final String SERIALIZED_NAME_HEADING_PENALTY = "heading_penalty";
  @SerializedName(SERIALIZED_NAME_HEADING_PENALTY)
  private Integer headingPenalty = 120;

  public static final String SERIALIZED_NAME_HEADINGS = "headings";
  @SerializedName(SERIALIZED_NAME_HEADINGS)
  private List<Integer> headings = new ArrayList<>();

  public static final String SERIALIZED_NAME_INSTRUCTIONS = "instructions";
  @SerializedName(SERIALIZED_NAME_INSTRUCTIONS)
  private Boolean instructions = true;

  public static final String SERIALIZED_NAME_LOCALE = "locale";
  @SerializedName(SERIALIZED_NAME_LOCALE)
  private String locale = "en";

  public static final String SERIALIZED_NAME_OPTIMIZE = "optimize";
  @SerializedName(SERIALIZED_NAME_OPTIMIZE)
  private String optimize = "false";

  public static final String SERIALIZED_NAME_PASS_THROUGH = "pass_through";
  @SerializedName(SERIALIZED_NAME_PASS_THROUGH)
  private Boolean passThrough = false;

  public static final String SERIALIZED_NAME_POINT_HINTS = "point_hints";
  @SerializedName(SERIALIZED_NAME_POINT_HINTS)
  private List<String> pointHints = new ArrayList<>();

  public static final String SERIALIZED_NAME_POINTS = "points";
  @SerializedName(SERIALIZED_NAME_POINTS)
  private List<List<Double>> points = new ArrayList<>();

  public static final String SERIALIZED_NAME_POINTS_ENCODED = "points_encoded";
  @SerializedName(SERIALIZED_NAME_POINTS_ENCODED)
  private Boolean pointsEncoded = true;

  public static final String SERIALIZED_NAME_ROUND_TRIP_DISTANCE = "round_trip.distance";
  @SerializedName(SERIALIZED_NAME_ROUND_TRIP_DISTANCE)
  private Integer roundTripDistance = 10000;

  public static final String SERIALIZED_NAME_ROUND_TRIP_SEED = "round_trip.seed";
  @SerializedName(SERIALIZED_NAME_ROUND_TRIP_SEED)
  private Long roundTripSeed;

  public static final String SERIALIZED_NAME_SNAP_PREVENTIONS = "snap_preventions";
  @SerializedName(SERIALIZED_NAME_SNAP_PREVENTIONS)
  private List<String> snapPreventions = new ArrayList<>();

  public static final String SERIALIZED_NAME_VEHICLE = "vehicle";
  @SerializedName(SERIALIZED_NAME_VEHICLE)
  private VehicleProfileId vehicle;

  public static final String SERIALIZED_NAME_WEIGHTING = "weighting";
  @SerializedName(SERIALIZED_NAME_WEIGHTING)
  private String weighting = "fastest";

  public RouteRequest() {
  }

  public RouteRequest algorithm(AlgorithmEnum algorithm) {
    this.algorithm = algorithm;
    return this;
  }

  /**
   * Rather than looking for the shortest or fastest path, this lets you solve two different problems related to routing: With &#x60;round_trip&#x60;, the route will get you back to where you started. This is meant for fun (think of a bike trip), so we will add some randomness. This requires &#x60;ch.disable&#x3D;true&#x60;. With &#x60;alternative_route&#x60;, we give you not one but several routes that are close to optimal, but not too similar to each other. You can control both of these features with additional parameters, see below. 
   * @return algorithm
   */
  @javax.annotation.Nullable
  public AlgorithmEnum getAlgorithm() {
    return algorithm;
  }

  public void setAlgorithm(AlgorithmEnum algorithm) {
    this.algorithm = algorithm;
  }


  public RouteRequest alternativeRouteMaxPaths(Integer alternativeRouteMaxPaths) {
    this.alternativeRouteMaxPaths = alternativeRouteMaxPaths;
    return this;
  }

  /**
   * If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the number of maximum paths which should be calculated. Increasing can lead to worse alternatives. 
   * @return alternativeRouteMaxPaths
   */
  @javax.annotation.Nullable
  public Integer getAlternativeRouteMaxPaths() {
    return alternativeRouteMaxPaths;
  }

  public void setAlternativeRouteMaxPaths(Integer alternativeRouteMaxPaths) {
    this.alternativeRouteMaxPaths = alternativeRouteMaxPaths;
  }


  public RouteRequest alternativeRouteMaxShareFactor(BigDecimal alternativeRouteMaxShareFactor) {
    this.alternativeRouteMaxShareFactor = alternativeRouteMaxShareFactor;
    return this;
  }

  /**
   * If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter specifies how similar an alternative route can be to the optimal route. Increasing can lead to worse alternatives. 
   * @return alternativeRouteMaxShareFactor
   */
  @javax.annotation.Nullable
  public BigDecimal getAlternativeRouteMaxShareFactor() {
    return alternativeRouteMaxShareFactor;
  }

  public void setAlternativeRouteMaxShareFactor(BigDecimal alternativeRouteMaxShareFactor) {
    this.alternativeRouteMaxShareFactor = alternativeRouteMaxShareFactor;
  }


  public RouteRequest alternativeRouteMaxWeightFactor(BigDecimal alternativeRouteMaxWeightFactor) {
    this.alternativeRouteMaxWeightFactor = alternativeRouteMaxWeightFactor;
    return this;
  }

  /**
   * If &#x60;algorithm&#x3D;alternative_route&#x60;, this parameter sets the factor by which the alternatives routes can be longer than the optimal route. Increasing can lead to worse alternatives. 
   * @return alternativeRouteMaxWeightFactor
   */
  @javax.annotation.Nullable
  public BigDecimal getAlternativeRouteMaxWeightFactor() {
    return alternativeRouteMaxWeightFactor;
  }

  public void setAlternativeRouteMaxWeightFactor(BigDecimal alternativeRouteMaxWeightFactor) {
    this.alternativeRouteMaxWeightFactor = alternativeRouteMaxWeightFactor;
  }


  public RouteRequest avoid(String avoid) {
    this.avoid = avoid;
    return this;
  }

  /**
   * Specify which road classes and environments you would like to avoid. Possible values are &#x60;motorway&#x60;, &#x60;steps&#x60;, &#x60;track&#x60;, &#x60;toll&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60; and &#x60;bridge&#x60;. Separate several values with &#x60;;&#x60;. Obviously not all the values make sense for all vehicle profiles e.g. &#x60;bike&#x60; is already forbidden on a &#x60;motorway&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;. 
   * @return avoid
   */
  @javax.annotation.Nullable
  public String getAvoid() {
    return avoid;
  }

  public void setAvoid(String avoid) {
    this.avoid = avoid;
  }


  public RouteRequest blockArea(String blockArea) {
    this.blockArea = blockArea;
    return this;
  }

  /**
   * Block road access via a point with the format &#x60;latitude,longitude&#x60; or an area defined by a circle &#x60;lat,lon,radius&#x60; or a rectangle &#x60;lat1,lon1,lat2,lon2&#x60;. Separate several values with &#x60;;&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;. 
   * @return blockArea
   */
  @javax.annotation.Nullable
  public String getBlockArea() {
    return blockArea;
  }

  public void setBlockArea(String blockArea) {
    this.blockArea = blockArea;
  }


  public RouteRequest calcPoints(Boolean calcPoints) {
    this.calcPoints = calcPoints;
    return this;
  }

  /**
   * If the points for the route should be calculated at all. 
   * @return calcPoints
   */
  @javax.annotation.Nullable
  public Boolean getCalcPoints() {
    return calcPoints;
  }

  public void setCalcPoints(Boolean calcPoints) {
    this.calcPoints = calcPoints;
  }


  public RouteRequest chDisable(Boolean chDisable) {
    this.chDisable = chDisable;
    return this;
  }

  /**
   * Use this parameter in combination with one or more parameters from below. 
   * @return chDisable
   */
  @javax.annotation.Nullable
  public Boolean getChDisable() {
    return chDisable;
  }

  public void setChDisable(Boolean chDisable) {
    this.chDisable = chDisable;
  }


  public RouteRequest curbsides(List<CurbsidesEnum> curbsides) {
    this.curbsides = curbsides;
    return this;
  }

  public RouteRequest addCurbsidesItem(CurbsidesEnum curbsidesItem) {
    if (this.curbsides == null) {
      this.curbsides = new ArrayList<>();
    }
    this.curbsides.add(curbsidesItem);
    return this;
  }

  /**
   * Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.
   * @return curbsides
   */
  @javax.annotation.Nullable
  public List<CurbsidesEnum> getCurbsides() {
    return curbsides;
  }

  public void setCurbsides(List<CurbsidesEnum> curbsides) {
    this.curbsides = curbsides;
  }


  public RouteRequest debug(Boolean debug) {
    this.debug = debug;
    return this;
  }

  /**
   * If &#x60;true&#x60;, the output will be formatted. 
   * @return debug
   */
  @javax.annotation.Nullable
  public Boolean getDebug() {
    return debug;
  }

  public void setDebug(Boolean debug) {
    this.debug = debug;
  }


  public RouteRequest details(List<String> details) {
    this.details = details;
    return this;
  }

  public RouteRequest addDetailsItem(String detailsItem) {
    if (this.details == null) {
      this.details = new ArrayList<>();
    }
    this.details.add(detailsItem);
    return this;
  }

  /**
   * Optional parameter to retrieve path details. You can request additional details for the route: &#x60;street_name&#x60;, &#x60;time&#x60;, &#x60;distance&#x60;, &#x60;max_speed&#x60;, &#x60;toll&#x60;, &#x60;road_class&#x60;, &#x60;road_class_link&#x60;, &#x60;road_access&#x60;, &#x60;road_environment&#x60;, &#x60;lanes&#x60;, and &#x60;surface&#x60;. Read more about the usage of path details [here](https://discuss.graphhopper.com/t/2539). 
   * @return details
   */
  @javax.annotation.Nullable
  public List<String> getDetails() {
    return details;
  }

  public void setDetails(List<String> details) {
    this.details = details;
  }


  public RouteRequest elevation(Boolean elevation) {
    this.elevation = elevation;
    return this;
  }

  /**
   * If &#x60;true&#x60;, a third coordinate, the altitude, is included with all positions in the response. This changes the format of the &#x60;points&#x60; and &#x60;snapped_waypoints&#x60; fields of the response, in both their encodings. Unless you switch off the &#x60;points_encoded&#x60; parameter, you need special code on the client side that can handle three-dimensional coordinates. A request can fail if the vehicle profile does not support elevation. See the features object for every vehicle profile. 
   * @return elevation
   */
  @javax.annotation.Nullable
  public Boolean getElevation() {
    return elevation;
  }

  public void setElevation(Boolean elevation) {
    this.elevation = elevation;
  }


  public RouteRequest headingPenalty(Integer headingPenalty) {
    this.headingPenalty = headingPenalty;
    return this;
  }

  /**
   * Time penalty in seconds for not obeying a specified heading. Requires &#x60;ch.disable&#x3D;true&#x60;. 
   * @return headingPenalty
   */
  @javax.annotation.Nullable
  public Integer getHeadingPenalty() {
    return headingPenalty;
  }

  public void setHeadingPenalty(Integer headingPenalty) {
    this.headingPenalty = headingPenalty;
  }


  public RouteRequest headings(List<Integer> headings) {
    this.headings = headings;
    return this;
  }

  public RouteRequest addHeadingsItem(Integer headingsItem) {
    if (this.headings == null) {
      this.headings = new ArrayList<>();
    }
    this.headings.add(headingsItem);
    return this;
  }

  /**
   * Favour a heading direction for a certain point. Specify either one heading for the start point or as many as there are points. In this case headings are associated by their order to the specific points. Headings are given as north based clockwise angle between 0 and 360 degree. This parameter also influences the tour generated with &#x60;algorithm&#x3D;round_trip&#x60; and forces the initial direction.  Requires &#x60;ch.disable&#x3D;true&#x60;. 
   * @return headings
   */
  @javax.annotation.Nullable
  public List<Integer> getHeadings() {
    return headings;
  }

  public void setHeadings(List<Integer> headings) {
    this.headings = headings;
  }


  public RouteRequest instructions(Boolean instructions) {
    this.instructions = instructions;
    return this;
  }

  /**
   * If instructions should be calculated and returned 
   * @return instructions
   */
  @javax.annotation.Nullable
  public Boolean getInstructions() {
    return instructions;
  }

  public void setInstructions(Boolean instructions) {
    this.instructions = instructions;
  }


  public RouteRequest locale(String locale) {
    this.locale = locale;
    return this;
  }

  /**
   * The locale of the resulting turn instructions. E.g. &#x60;pt_PT&#x60; for Portuguese or &#x60;de&#x60; for German. 
   * @return locale
   */
  @javax.annotation.Nullable
  public String getLocale() {
    return locale;
  }

  public void setLocale(String locale) {
    this.locale = locale;
  }


  public RouteRequest optimize(String optimize) {
    this.optimize = optimize;
    return this;
  }

  /**
   * Normally, the calculated route will visit the points in the order you specified them. If you have more than two points, you can set this parameter to &#x60;\&quot;true\&quot;&#x60; and the points may be re-ordered to minimize the total travel time. Keep in mind that the limits on the number of locations of the Route Optimization API applies, and the request costs more credits. 
   * @return optimize
   */
  @javax.annotation.Nullable
  public String getOptimize() {
    return optimize;
  }

  public void setOptimize(String optimize) {
    this.optimize = optimize;
  }


  public RouteRequest passThrough(Boolean passThrough) {
    this.passThrough = passThrough;
    return this;
  }

  /**
   * If &#x60;true&#x60;, u-turns are avoided at via-points with regard to the &#x60;heading_penalty&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;. 
   * @return passThrough
   */
  @javax.annotation.Nullable
  public Boolean getPassThrough() {
    return passThrough;
  }

  public void setPassThrough(Boolean passThrough) {
    this.passThrough = passThrough;
  }


  public RouteRequest pointHints(List<String> pointHints) {
    this.pointHints = pointHints;
    return this;
  }

  public RouteRequest addPointHintsItem(String pointHintsItem) {
    if (this.pointHints == null) {
      this.pointHints = new ArrayList<>();
    }
    this.pointHints.add(pointHintsItem);
    return this;
  }

  /**
   * Optional parameter. Specifies a hint for each point in the &#x60;points&#x60; array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.
   * @return pointHints
   */
  @javax.annotation.Nullable
  public List<String> getPointHints() {
    return pointHints;
  }

  public void setPointHints(List<String> pointHints) {
    this.pointHints = pointHints;
  }


  public RouteRequest points(List<List<Double>> points) {
    this.points = points;
    return this;
  }

  public RouteRequest addPointsItem(List<Double> pointsItem) {
    if (this.points == null) {
      this.points = new ArrayList<>();
    }
    this.points.add(pointsItem);
    return this;
  }

  /**
   * The points for the route in an array of &#x60;[longitude,latitude]&#x60;. For instance, if you want to calculate a route from point A to B to C then you specify &#x60;points: [ [A_longitude, A_latitude], [B_longitude, B_latitude], [C_longitude, C_latitude]] 
   * @return points
   */
  @javax.annotation.Nullable
  public List<List<Double>> getPoints() {
    return points;
  }

  public void setPoints(List<List<Double>> points) {
    this.points = points;
  }


  public RouteRequest pointsEncoded(Boolean pointsEncoded) {
    this.pointsEncoded = pointsEncoded;
    return this;
  }

  /**
   * Allows changing the encoding of location data in the response. The default is polyline encoding, which is compact but requires special client code to unpack. (We provide it in our JavaScript client library!) Set this parameter to &#x60;false&#x60; to switch the encoding to simple coordinate pairs like &#x60;[lon,lat]&#x60;, or &#x60;[lon,lat,elevation]&#x60;. See the description of the response format for more information. 
   * @return pointsEncoded
   */
  @javax.annotation.Nullable
  public Boolean getPointsEncoded() {
    return pointsEncoded;
  }

  public void setPointsEncoded(Boolean pointsEncoded) {
    this.pointsEncoded = pointsEncoded;
  }


  public RouteRequest roundTripDistance(Integer roundTripDistance) {
    this.roundTripDistance = roundTripDistance;
    return this;
  }

  /**
   * If &#x60;algorithm&#x3D;round_trip&#x60;, this parameter configures approximative length of the resulting round trip. Requires &#x60;ch.disable&#x3D;true&#x60;. 
   * @return roundTripDistance
   */
  @javax.annotation.Nullable
  public Integer getRoundTripDistance() {
    return roundTripDistance;
  }

  public void setRoundTripDistance(Integer roundTripDistance) {
    this.roundTripDistance = roundTripDistance;
  }


  public RouteRequest roundTripSeed(Long roundTripSeed) {
    this.roundTripSeed = roundTripSeed;
    return this;
  }

  /**
   * If &#x60;algorithm&#x3D;round_trip&#x60;, this sets the random seed. Change this to get a different tour for each value. 
   * @return roundTripSeed
   */
  @javax.annotation.Nullable
  public Long getRoundTripSeed() {
    return roundTripSeed;
  }

  public void setRoundTripSeed(Long roundTripSeed) {
    this.roundTripSeed = roundTripSeed;
  }


  public RouteRequest snapPreventions(List<String> snapPreventions) {
    this.snapPreventions = snapPreventions;
    return this;
  }

  public RouteRequest addSnapPreventionsItem(String snapPreventionsItem) {
    if (this.snapPreventions == null) {
      this.snapPreventions = new ArrayList<>();
    }
    this.snapPreventions.add(snapPreventionsItem);
    return this;
  }

  /**
   * Optional parameter to avoid snapping to a certain road class or road environment. Current supported values &#x60;motorway&#x60;, &#x60;trunk&#x60;, &#x60;ferry&#x60;, &#x60;tunnel&#x60;, &#x60;bridge&#x60; and &#x60;ford&#x60;
   * @return snapPreventions
   */
  @javax.annotation.Nullable
  public List<String> getSnapPreventions() {
    return snapPreventions;
  }

  public void setSnapPreventions(List<String> snapPreventions) {
    this.snapPreventions = snapPreventions;
  }


  public RouteRequest vehicle(VehicleProfileId vehicle) {
    this.vehicle = vehicle;
    return this;
  }

  /**
   * Get vehicle
   * @return vehicle
   */
  @javax.annotation.Nullable
  public VehicleProfileId getVehicle() {
    return vehicle;
  }

  public void setVehicle(VehicleProfileId vehicle) {
    this.vehicle = vehicle;
  }


  public RouteRequest weighting(String weighting) {
    this.weighting = weighting;
    return this;
  }

  /**
   * Determines the way the &#39;&#39;best&#39;&#39; route is calculated. Default is &#x60;fastest&#x60;. Other options are &#x60;shortest&#x60; (e.g. for &#x60;vehicle&#x3D;foot&#x60; or &#x60;bike&#x60;) and &#x60;short_fastest&#x60; which finds a reasonable balance between &#x60;shortest&#x60; and &#x60;fastest&#x60;. Requires &#x60;ch.disable&#x3D;true&#x60;. 
   * @return weighting
   */
  @javax.annotation.Nullable
  public String getWeighting() {
    return weighting;
  }

  public void setWeighting(String weighting) {
    this.weighting = weighting;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RouteRequest routeRequest = (RouteRequest) o;
    return Objects.equals(this.algorithm, routeRequest.algorithm) &&
        Objects.equals(this.alternativeRouteMaxPaths, routeRequest.alternativeRouteMaxPaths) &&
        Objects.equals(this.alternativeRouteMaxShareFactor, routeRequest.alternativeRouteMaxShareFactor) &&
        Objects.equals(this.alternativeRouteMaxWeightFactor, routeRequest.alternativeRouteMaxWeightFactor) &&
        Objects.equals(this.avoid, routeRequest.avoid) &&
        Objects.equals(this.blockArea, routeRequest.blockArea) &&
        Objects.equals(this.calcPoints, routeRequest.calcPoints) &&
        Objects.equals(this.chDisable, routeRequest.chDisable) &&
        Objects.equals(this.curbsides, routeRequest.curbsides) &&
        Objects.equals(this.debug, routeRequest.debug) &&
        Objects.equals(this.details, routeRequest.details) &&
        Objects.equals(this.elevation, routeRequest.elevation) &&
        Objects.equals(this.headingPenalty, routeRequest.headingPenalty) &&
        Objects.equals(this.headings, routeRequest.headings) &&
        Objects.equals(this.instructions, routeRequest.instructions) &&
        Objects.equals(this.locale, routeRequest.locale) &&
        Objects.equals(this.optimize, routeRequest.optimize) &&
        Objects.equals(this.passThrough, routeRequest.passThrough) &&
        Objects.equals(this.pointHints, routeRequest.pointHints) &&
        Objects.equals(this.points, routeRequest.points) &&
        Objects.equals(this.pointsEncoded, routeRequest.pointsEncoded) &&
        Objects.equals(this.roundTripDistance, routeRequest.roundTripDistance) &&
        Objects.equals(this.roundTripSeed, routeRequest.roundTripSeed) &&
        Objects.equals(this.snapPreventions, routeRequest.snapPreventions) &&
        Objects.equals(this.vehicle, routeRequest.vehicle) &&
        Objects.equals(this.weighting, routeRequest.weighting);
  }

  @Override
  public int hashCode() {
    return Objects.hash(algorithm, alternativeRouteMaxPaths, alternativeRouteMaxShareFactor, alternativeRouteMaxWeightFactor, avoid, blockArea, calcPoints, chDisable, curbsides, debug, details, elevation, headingPenalty, headings, instructions, locale, optimize, passThrough, pointHints, points, pointsEncoded, roundTripDistance, roundTripSeed, snapPreventions, vehicle, weighting);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RouteRequest {\n");
    sb.append("    algorithm: ").append(toIndentedString(algorithm)).append("\n");
    sb.append("    alternativeRouteMaxPaths: ").append(toIndentedString(alternativeRouteMaxPaths)).append("\n");
    sb.append("    alternativeRouteMaxShareFactor: ").append(toIndentedString(alternativeRouteMaxShareFactor)).append("\n");
    sb.append("    alternativeRouteMaxWeightFactor: ").append(toIndentedString(alternativeRouteMaxWeightFactor)).append("\n");
    sb.append("    avoid: ").append(toIndentedString(avoid)).append("\n");
    sb.append("    blockArea: ").append(toIndentedString(blockArea)).append("\n");
    sb.append("    calcPoints: ").append(toIndentedString(calcPoints)).append("\n");
    sb.append("    chDisable: ").append(toIndentedString(chDisable)).append("\n");
    sb.append("    curbsides: ").append(toIndentedString(curbsides)).append("\n");
    sb.append("    debug: ").append(toIndentedString(debug)).append("\n");
    sb.append("    details: ").append(toIndentedString(details)).append("\n");
    sb.append("    elevation: ").append(toIndentedString(elevation)).append("\n");
    sb.append("    headingPenalty: ").append(toIndentedString(headingPenalty)).append("\n");
    sb.append("    headings: ").append(toIndentedString(headings)).append("\n");
    sb.append("    instructions: ").append(toIndentedString(instructions)).append("\n");
    sb.append("    locale: ").append(toIndentedString(locale)).append("\n");
    sb.append("    optimize: ").append(toIndentedString(optimize)).append("\n");
    sb.append("    passThrough: ").append(toIndentedString(passThrough)).append("\n");
    sb.append("    pointHints: ").append(toIndentedString(pointHints)).append("\n");
    sb.append("    points: ").append(toIndentedString(points)).append("\n");
    sb.append("    pointsEncoded: ").append(toIndentedString(pointsEncoded)).append("\n");
    sb.append("    roundTripDistance: ").append(toIndentedString(roundTripDistance)).append("\n");
    sb.append("    roundTripSeed: ").append(toIndentedString(roundTripSeed)).append("\n");
    sb.append("    snapPreventions: ").append(toIndentedString(snapPreventions)).append("\n");
    sb.append("    vehicle: ").append(toIndentedString(vehicle)).append("\n");
    sb.append("    weighting: ").append(toIndentedString(weighting)).append("\n");
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
    openapiFields.add("algorithm");
    openapiFields.add("alternative_route.max_paths");
    openapiFields.add("alternative_route.max_share_factor");
    openapiFields.add("alternative_route.max_weight_factor");
    openapiFields.add("avoid");
    openapiFields.add("block_area");
    openapiFields.add("calc_points");
    openapiFields.add("ch.disable");
    openapiFields.add("curbsides");
    openapiFields.add("debug");
    openapiFields.add("details");
    openapiFields.add("elevation");
    openapiFields.add("heading_penalty");
    openapiFields.add("headings");
    openapiFields.add("instructions");
    openapiFields.add("locale");
    openapiFields.add("optimize");
    openapiFields.add("pass_through");
    openapiFields.add("point_hints");
    openapiFields.add("points");
    openapiFields.add("points_encoded");
    openapiFields.add("round_trip.distance");
    openapiFields.add("round_trip.seed");
    openapiFields.add("snap_preventions");
    openapiFields.add("vehicle");
    openapiFields.add("weighting");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to RouteRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!RouteRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in RouteRequest is not found in the empty JSON string", RouteRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!RouteRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `RouteRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("algorithm") != null && !jsonObj.get("algorithm").isJsonNull()) && !jsonObj.get("algorithm").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `algorithm` to be a primitive type in the JSON string but got `%s`", jsonObj.get("algorithm").toString()));
      }
      // validate the optional field `algorithm`
      if (jsonObj.get("algorithm") != null && !jsonObj.get("algorithm").isJsonNull()) {
        AlgorithmEnum.validateJsonElement(jsonObj.get("algorithm"));
      }
      if ((jsonObj.get("avoid") != null && !jsonObj.get("avoid").isJsonNull()) && !jsonObj.get("avoid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `avoid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("avoid").toString()));
      }
      if ((jsonObj.get("block_area") != null && !jsonObj.get("block_area").isJsonNull()) && !jsonObj.get("block_area").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `block_area` to be a primitive type in the JSON string but got `%s`", jsonObj.get("block_area").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("curbsides") != null && !jsonObj.get("curbsides").isJsonNull() && !jsonObj.get("curbsides").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `curbsides` to be an array in the JSON string but got `%s`", jsonObj.get("curbsides").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("details") != null && !jsonObj.get("details").isJsonNull() && !jsonObj.get("details").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `details` to be an array in the JSON string but got `%s`", jsonObj.get("details").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("headings") != null && !jsonObj.get("headings").isJsonNull() && !jsonObj.get("headings").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `headings` to be an array in the JSON string but got `%s`", jsonObj.get("headings").toString()));
      }
      if ((jsonObj.get("locale") != null && !jsonObj.get("locale").isJsonNull()) && !jsonObj.get("locale").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `locale` to be a primitive type in the JSON string but got `%s`", jsonObj.get("locale").toString()));
      }
      if ((jsonObj.get("optimize") != null && !jsonObj.get("optimize").isJsonNull()) && !jsonObj.get("optimize").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `optimize` to be a primitive type in the JSON string but got `%s`", jsonObj.get("optimize").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("point_hints") != null && !jsonObj.get("point_hints").isJsonNull() && !jsonObj.get("point_hints").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `point_hints` to be an array in the JSON string but got `%s`", jsonObj.get("point_hints").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("points") != null && !jsonObj.get("points").isJsonNull() && !jsonObj.get("points").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `points` to be an array in the JSON string but got `%s`", jsonObj.get("points").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("snap_preventions") != null && !jsonObj.get("snap_preventions").isJsonNull() && !jsonObj.get("snap_preventions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `snap_preventions` to be an array in the JSON string but got `%s`", jsonObj.get("snap_preventions").toString()));
      }
      // validate the optional field `vehicle`
      if (jsonObj.get("vehicle") != null && !jsonObj.get("vehicle").isJsonNull()) {
        VehicleProfileId.validateJsonElement(jsonObj.get("vehicle"));
      }
      if ((jsonObj.get("weighting") != null && !jsonObj.get("weighting").isJsonNull()) && !jsonObj.get("weighting").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `weighting` to be a primitive type in the JSON string but got `%s`", jsonObj.get("weighting").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!RouteRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'RouteRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<RouteRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(RouteRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<RouteRequest>() {
           @Override
           public void write(JsonWriter out, RouteRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public RouteRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of RouteRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of RouteRequest
   * @throws IOException if the JSON string is invalid with respect to RouteRequest
   */
  public static RouteRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, RouteRequest.class);
  }

  /**
   * Convert an instance of RouteRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

