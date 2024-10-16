/*
 * IdealSpot GeoData
 * Hyperlocal Demographics, Vehicle Traffic, Economic, Market Signals, and More. Use this API to request IdealSpot hyperlocal geospatial market insight and geometry data.   ## Detailed Description  Use this API as your **local economy microscope** by querying [IdealSpot](https://www.idealspot.com) hyperlocal market insight and geometry data. We offer the most precise, extensive, and frequently-updated local market data in the US. Our data is available across the entire US and can be queried at geographic scales ranging from the micro (Census block) through the macro (nation).  Better data and analysis leads to a better understanding of local market opportunities and risks. Integrate with your commercial real estate and marketing applications, machine learning workflows, and other investment analytics.  Our goal is to offer the most complete snapshot of the geographically distributed consumer and retail economy. We start with the fundamentals of consumers and business establishments. To connect retailers with consumers, we provide mobility data like vehicle traffic and mobile device data. To describe consumer intent, we provide geolocated digital marketing data.   We believe that accurate capital allocation through reliable local market data is foundational to creating robust, healthy, and livable communities for all. We hope you and your clients find tremendous value in this service.  ## Features  Query data and GeoJSON geometries at these scales for any US latitude and longitude:  * Rings (0.5 km+) * Drive time (1-60 minutes) * Bike time (3-60 minutes) * Walk time (5-60 minutes) * Public transit time (5-60 minutes) * Administrative region (US, states, core-based statistical areas, counties, Census-designated places, Census tracts, zipcodes, Census block groups, opportunity zones)  | Data Feature | Description | | ------- | ------------------------------| | Demographics, Housing, Spending | *Updated Quarterly*.  Current and historical market data including population, spending, and housing. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Labor, Business Establishments, Economic Conditions | *Updated Quarterly*.  Traditional market data including workforce, business establishment counts, and economic conditions like local GDP, unemployment rates. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Consumer segmentation | *Updated Annually*. Demographics grouped into narrative-oriented segments. | | Vehicle Traffic | *Updated semi-annually*. Gold standard in vehicle traffic data from INRIX. Counts by day of week, time of day and side of street. | | Rings and Travel time polygons | *Estimate in Real-time*. Rings alongside drive time, walk time, bike time, and public transit time polygons. Request as GeoJSON geometries for mapping or use with data queries | | Administrative region polygons | *Updated Annually*. GeoJSON administrative regions from US Census Bureau: block groups, tracts, counties, CBSAs, states, opportunity zones, USPS zipcodes | | Internet Search Volumes | 30 day rolling averages for geolocated advertising potential across 450 business categories from major search engines | | Social Media Interest | 30 day rolling average for geolocated advertising potential across 450 business categories from major social networks |  ### Coming Soon!  This API powers our local market research platform at [IdealSpot.com](https://www.idealspot.com). The functionality exposed so far is only a portion of our current capabilities. We will be exposing additional API features in time so watch this space!  | Data Feature | Description | | ------- | ------------------------------| Mobile device visit counts, points of interest, brands | Fresh point of interest data across 3000+ brands, millions of POI, and historical foot traffic counts using mobile data for those points of interest Origin/destination trips from mobile devices | Map origins and destinations of devices visiting an arbitrary catchment area Competition search | Search all major point-of-interest aggregators in one query Environment/climate | Expected weather patterns like temperature and precipitation Filter search API | Query data for all counties in state, all tracts in MSA, etc Road segment tiles | Plot road segments on maps in interactive applications  ## Developer Website  For more detail see https://developer.idealspot.com/
 *
 * The version of the OpenAPI document: 1.0
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
 * Units
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:58.672234-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Units {
  public static final String SERIALIZED_NAME_$100K125K = "$100k-125k";
  @SerializedName(SERIALIZED_NAME_$100K125K)
  private String $100k125k;

  public static final String SERIALIZED_NAME_$10K15K = "$10k-15k";
  @SerializedName(SERIALIZED_NAME_$10K15K)
  private String $10k15k;

  public static final String SERIALIZED_NAME_$125K150K = "$125k-150k";
  @SerializedName(SERIALIZED_NAME_$125K150K)
  private String $125k150k;

  public static final String SERIALIZED_NAME_$150K175K = "$150k-175k";
  @SerializedName(SERIALIZED_NAME_$150K175K)
  private String $150k175k;

  public static final String SERIALIZED_NAME_$15K20K = "$15k-20k";
  @SerializedName(SERIALIZED_NAME_$15K20K)
  private String $15k20k;

  public static final String SERIALIZED_NAME_$175K200K = "$175k-200k";
  @SerializedName(SERIALIZED_NAME_$175K200K)
  private String $175k200k;

  public static final String SERIALIZED_NAME_$200K250K = "$200k-250k";
  @SerializedName(SERIALIZED_NAME_$200K250K)
  private String $200k250k;

  public static final String SERIALIZED_NAME_$20K25K = "$20k-25k";
  @SerializedName(SERIALIZED_NAME_$20K25K)
  private String $20k25k;

  public static final String SERIALIZED_NAME_$250K300K = "$250k-300k";
  @SerializedName(SERIALIZED_NAME_$250K300K)
  private String $250k300k;

  public static final String SERIALIZED_NAME_$25K30K = "$25k-30k";
  @SerializedName(SERIALIZED_NAME_$25K30K)
  private String $25k30k;

  public static final String SERIALIZED_NAME_$300K400K = "$300k-400k";
  @SerializedName(SERIALIZED_NAME_$300K400K)
  private String $300k400k;

  public static final String SERIALIZED_NAME_$30K35K = "$30k-35k";
  @SerializedName(SERIALIZED_NAME_$30K35K)
  private String $30k35k;

  public static final String SERIALIZED_NAME_$35K40K = "$35k-40k";
  @SerializedName(SERIALIZED_NAME_$35K40K)
  private String $35k40k;

  public static final String SERIALIZED_NAME_$400K500K = "$400k-500k";
  @SerializedName(SERIALIZED_NAME_$400K500K)
  private String $400k500k;

  public static final String SERIALIZED_NAME_$40K50K = "$40k-50k";
  @SerializedName(SERIALIZED_NAME_$40K50K)
  private String $40k50k;

  public static final String SERIALIZED_NAME_$500K750K = "$500k-750k";
  @SerializedName(SERIALIZED_NAME_$500K750K)
  private String $500k750k;

  public static final String SERIALIZED_NAME_$50K60K = "$50k-60k";
  @SerializedName(SERIALIZED_NAME_$50K60K)
  private String $50k60k;

  public static final String SERIALIZED_NAME_$60K70K = "$60k-70k";
  @SerializedName(SERIALIZED_NAME_$60K70K)
  private String $60k70k;

  public static final String SERIALIZED_NAME_$70K80K = "$70k-80k";
  @SerializedName(SERIALIZED_NAME_$70K80K)
  private String $70k80k;

  public static final String SERIALIZED_NAME_$750K1_M = "$750k-1M";
  @SerializedName(SERIALIZED_NAME_$750K1_M)
  private String $750k1M;

  public static final String SERIALIZED_NAME_$80K90K = "$80k-90k";
  @SerializedName(SERIALIZED_NAME_$80K90K)
  private String $80k90k;

  public static final String SERIALIZED_NAME_$90K100K = "$90k-100k";
  @SerializedName(SERIALIZED_NAME_$90K100K)
  private String $90k100k;

  public static final String SERIALIZED_NAME_MEDIAN_HOME_VALUE = "Median Home Value";
  @SerializedName(SERIALIZED_NAME_MEDIAN_HOME_VALUE)
  private String medianHomeValue;

  public static final String SERIALIZED_NAME_OVER$1_M = "Over $1M";
  @SerializedName(SERIALIZED_NAME_OVER$1_M)
  private String over$1M;

  public static final String SERIALIZED_NAME_OWNER_OCCUPIED_HOUSEHOLDS = "Owner Occupied Households";
  @SerializedName(SERIALIZED_NAME_OWNER_OCCUPIED_HOUSEHOLDS)
  private String ownerOccupiedHouseholds;

  public static final String SERIALIZED_NAME_UNDER$10K = "Under $10k";
  @SerializedName(SERIALIZED_NAME_UNDER$10K)
  private String under$10k;

  public static final String SERIALIZED_NAME_CONTEXT_HOUSEHOLDS = "context.households";
  @SerializedName(SERIALIZED_NAME_CONTEXT_HOUSEHOLDS)
  private String contextHouseholds;

  public static final String SERIALIZED_NAME_CONTEXT_LANDAREA = "context.landarea";
  @SerializedName(SERIALIZED_NAME_CONTEXT_LANDAREA)
  private String contextLandarea;

  public Units() {
  }

  public Units $100k125k(String $100k125k) {
    this.$100k125k = $100k125k;
    return this;
  }

  /**
   * Get $100k125k
   * @return $100k125k
   */
  @javax.annotation.Nonnull
  public String get$100k125k() {
    return $100k125k;
  }

  public void set$100k125k(String $100k125k) {
    this.$100k125k = $100k125k;
  }


  public Units $10k15k(String $10k15k) {
    this.$10k15k = $10k15k;
    return this;
  }

  /**
   * Get $10k15k
   * @return $10k15k
   */
  @javax.annotation.Nonnull
  public String get$10k15k() {
    return $10k15k;
  }

  public void set$10k15k(String $10k15k) {
    this.$10k15k = $10k15k;
  }


  public Units $125k150k(String $125k150k) {
    this.$125k150k = $125k150k;
    return this;
  }

  /**
   * Get $125k150k
   * @return $125k150k
   */
  @javax.annotation.Nonnull
  public String get$125k150k() {
    return $125k150k;
  }

  public void set$125k150k(String $125k150k) {
    this.$125k150k = $125k150k;
  }


  public Units $150k175k(String $150k175k) {
    this.$150k175k = $150k175k;
    return this;
  }

  /**
   * Get $150k175k
   * @return $150k175k
   */
  @javax.annotation.Nonnull
  public String get$150k175k() {
    return $150k175k;
  }

  public void set$150k175k(String $150k175k) {
    this.$150k175k = $150k175k;
  }


  public Units $15k20k(String $15k20k) {
    this.$15k20k = $15k20k;
    return this;
  }

  /**
   * Get $15k20k
   * @return $15k20k
   */
  @javax.annotation.Nonnull
  public String get$15k20k() {
    return $15k20k;
  }

  public void set$15k20k(String $15k20k) {
    this.$15k20k = $15k20k;
  }


  public Units $175k200k(String $175k200k) {
    this.$175k200k = $175k200k;
    return this;
  }

  /**
   * Get $175k200k
   * @return $175k200k
   */
  @javax.annotation.Nonnull
  public String get$175k200k() {
    return $175k200k;
  }

  public void set$175k200k(String $175k200k) {
    this.$175k200k = $175k200k;
  }


  public Units $200k250k(String $200k250k) {
    this.$200k250k = $200k250k;
    return this;
  }

  /**
   * Get $200k250k
   * @return $200k250k
   */
  @javax.annotation.Nonnull
  public String get$200k250k() {
    return $200k250k;
  }

  public void set$200k250k(String $200k250k) {
    this.$200k250k = $200k250k;
  }


  public Units $20k25k(String $20k25k) {
    this.$20k25k = $20k25k;
    return this;
  }

  /**
   * Get $20k25k
   * @return $20k25k
   */
  @javax.annotation.Nonnull
  public String get$20k25k() {
    return $20k25k;
  }

  public void set$20k25k(String $20k25k) {
    this.$20k25k = $20k25k;
  }


  public Units $250k300k(String $250k300k) {
    this.$250k300k = $250k300k;
    return this;
  }

  /**
   * Get $250k300k
   * @return $250k300k
   */
  @javax.annotation.Nonnull
  public String get$250k300k() {
    return $250k300k;
  }

  public void set$250k300k(String $250k300k) {
    this.$250k300k = $250k300k;
  }


  public Units $25k30k(String $25k30k) {
    this.$25k30k = $25k30k;
    return this;
  }

  /**
   * Get $25k30k
   * @return $25k30k
   */
  @javax.annotation.Nonnull
  public String get$25k30k() {
    return $25k30k;
  }

  public void set$25k30k(String $25k30k) {
    this.$25k30k = $25k30k;
  }


  public Units $300k400k(String $300k400k) {
    this.$300k400k = $300k400k;
    return this;
  }

  /**
   * Get $300k400k
   * @return $300k400k
   */
  @javax.annotation.Nonnull
  public String get$300k400k() {
    return $300k400k;
  }

  public void set$300k400k(String $300k400k) {
    this.$300k400k = $300k400k;
  }


  public Units $30k35k(String $30k35k) {
    this.$30k35k = $30k35k;
    return this;
  }

  /**
   * Get $30k35k
   * @return $30k35k
   */
  @javax.annotation.Nonnull
  public String get$30k35k() {
    return $30k35k;
  }

  public void set$30k35k(String $30k35k) {
    this.$30k35k = $30k35k;
  }


  public Units $35k40k(String $35k40k) {
    this.$35k40k = $35k40k;
    return this;
  }

  /**
   * Get $35k40k
   * @return $35k40k
   */
  @javax.annotation.Nonnull
  public String get$35k40k() {
    return $35k40k;
  }

  public void set$35k40k(String $35k40k) {
    this.$35k40k = $35k40k;
  }


  public Units $400k500k(String $400k500k) {
    this.$400k500k = $400k500k;
    return this;
  }

  /**
   * Get $400k500k
   * @return $400k500k
   */
  @javax.annotation.Nonnull
  public String get$400k500k() {
    return $400k500k;
  }

  public void set$400k500k(String $400k500k) {
    this.$400k500k = $400k500k;
  }


  public Units $40k50k(String $40k50k) {
    this.$40k50k = $40k50k;
    return this;
  }

  /**
   * Get $40k50k
   * @return $40k50k
   */
  @javax.annotation.Nonnull
  public String get$40k50k() {
    return $40k50k;
  }

  public void set$40k50k(String $40k50k) {
    this.$40k50k = $40k50k;
  }


  public Units $500k750k(String $500k750k) {
    this.$500k750k = $500k750k;
    return this;
  }

  /**
   * Get $500k750k
   * @return $500k750k
   */
  @javax.annotation.Nonnull
  public String get$500k750k() {
    return $500k750k;
  }

  public void set$500k750k(String $500k750k) {
    this.$500k750k = $500k750k;
  }


  public Units $50k60k(String $50k60k) {
    this.$50k60k = $50k60k;
    return this;
  }

  /**
   * Get $50k60k
   * @return $50k60k
   */
  @javax.annotation.Nonnull
  public String get$50k60k() {
    return $50k60k;
  }

  public void set$50k60k(String $50k60k) {
    this.$50k60k = $50k60k;
  }


  public Units $60k70k(String $60k70k) {
    this.$60k70k = $60k70k;
    return this;
  }

  /**
   * Get $60k70k
   * @return $60k70k
   */
  @javax.annotation.Nonnull
  public String get$60k70k() {
    return $60k70k;
  }

  public void set$60k70k(String $60k70k) {
    this.$60k70k = $60k70k;
  }


  public Units $70k80k(String $70k80k) {
    this.$70k80k = $70k80k;
    return this;
  }

  /**
   * Get $70k80k
   * @return $70k80k
   */
  @javax.annotation.Nonnull
  public String get$70k80k() {
    return $70k80k;
  }

  public void set$70k80k(String $70k80k) {
    this.$70k80k = $70k80k;
  }


  public Units $750k1M(String $750k1M) {
    this.$750k1M = $750k1M;
    return this;
  }

  /**
   * Get $750k1M
   * @return $750k1M
   */
  @javax.annotation.Nonnull
  public String get$750k1M() {
    return $750k1M;
  }

  public void set$750k1M(String $750k1M) {
    this.$750k1M = $750k1M;
  }


  public Units $80k90k(String $80k90k) {
    this.$80k90k = $80k90k;
    return this;
  }

  /**
   * Get $80k90k
   * @return $80k90k
   */
  @javax.annotation.Nonnull
  public String get$80k90k() {
    return $80k90k;
  }

  public void set$80k90k(String $80k90k) {
    this.$80k90k = $80k90k;
  }


  public Units $90k100k(String $90k100k) {
    this.$90k100k = $90k100k;
    return this;
  }

  /**
   * Get $90k100k
   * @return $90k100k
   */
  @javax.annotation.Nonnull
  public String get$90k100k() {
    return $90k100k;
  }

  public void set$90k100k(String $90k100k) {
    this.$90k100k = $90k100k;
  }


  public Units medianHomeValue(String medianHomeValue) {
    this.medianHomeValue = medianHomeValue;
    return this;
  }

  /**
   * Get medianHomeValue
   * @return medianHomeValue
   */
  @javax.annotation.Nonnull
  public String getMedianHomeValue() {
    return medianHomeValue;
  }

  public void setMedianHomeValue(String medianHomeValue) {
    this.medianHomeValue = medianHomeValue;
  }


  public Units over$1M(String over$1M) {
    this.over$1M = over$1M;
    return this;
  }

  /**
   * Get over$1M
   * @return over$1M
   */
  @javax.annotation.Nonnull
  public String getOver$1M() {
    return over$1M;
  }

  public void setOver$1M(String over$1M) {
    this.over$1M = over$1M;
  }


  public Units ownerOccupiedHouseholds(String ownerOccupiedHouseholds) {
    this.ownerOccupiedHouseholds = ownerOccupiedHouseholds;
    return this;
  }

  /**
   * Get ownerOccupiedHouseholds
   * @return ownerOccupiedHouseholds
   */
  @javax.annotation.Nonnull
  public String getOwnerOccupiedHouseholds() {
    return ownerOccupiedHouseholds;
  }

  public void setOwnerOccupiedHouseholds(String ownerOccupiedHouseholds) {
    this.ownerOccupiedHouseholds = ownerOccupiedHouseholds;
  }


  public Units under$10k(String under$10k) {
    this.under$10k = under$10k;
    return this;
  }

  /**
   * Get under$10k
   * @return under$10k
   */
  @javax.annotation.Nonnull
  public String getUnder$10k() {
    return under$10k;
  }

  public void setUnder$10k(String under$10k) {
    this.under$10k = under$10k;
  }


  public Units contextHouseholds(String contextHouseholds) {
    this.contextHouseholds = contextHouseholds;
    return this;
  }

  /**
   * Get contextHouseholds
   * @return contextHouseholds
   */
  @javax.annotation.Nonnull
  public String getContextHouseholds() {
    return contextHouseholds;
  }

  public void setContextHouseholds(String contextHouseholds) {
    this.contextHouseholds = contextHouseholds;
  }


  public Units contextLandarea(String contextLandarea) {
    this.contextLandarea = contextLandarea;
    return this;
  }

  /**
   * Get contextLandarea
   * @return contextLandarea
   */
  @javax.annotation.Nonnull
  public String getContextLandarea() {
    return contextLandarea;
  }

  public void setContextLandarea(String contextLandarea) {
    this.contextLandarea = contextLandarea;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Units units = (Units) o;
    return Objects.equals(this.$100k125k, units.$100k125k) &&
        Objects.equals(this.$10k15k, units.$10k15k) &&
        Objects.equals(this.$125k150k, units.$125k150k) &&
        Objects.equals(this.$150k175k, units.$150k175k) &&
        Objects.equals(this.$15k20k, units.$15k20k) &&
        Objects.equals(this.$175k200k, units.$175k200k) &&
        Objects.equals(this.$200k250k, units.$200k250k) &&
        Objects.equals(this.$20k25k, units.$20k25k) &&
        Objects.equals(this.$250k300k, units.$250k300k) &&
        Objects.equals(this.$25k30k, units.$25k30k) &&
        Objects.equals(this.$300k400k, units.$300k400k) &&
        Objects.equals(this.$30k35k, units.$30k35k) &&
        Objects.equals(this.$35k40k, units.$35k40k) &&
        Objects.equals(this.$400k500k, units.$400k500k) &&
        Objects.equals(this.$40k50k, units.$40k50k) &&
        Objects.equals(this.$500k750k, units.$500k750k) &&
        Objects.equals(this.$50k60k, units.$50k60k) &&
        Objects.equals(this.$60k70k, units.$60k70k) &&
        Objects.equals(this.$70k80k, units.$70k80k) &&
        Objects.equals(this.$750k1M, units.$750k1M) &&
        Objects.equals(this.$80k90k, units.$80k90k) &&
        Objects.equals(this.$90k100k, units.$90k100k) &&
        Objects.equals(this.medianHomeValue, units.medianHomeValue) &&
        Objects.equals(this.over$1M, units.over$1M) &&
        Objects.equals(this.ownerOccupiedHouseholds, units.ownerOccupiedHouseholds) &&
        Objects.equals(this.under$10k, units.under$10k) &&
        Objects.equals(this.contextHouseholds, units.contextHouseholds) &&
        Objects.equals(this.contextLandarea, units.contextLandarea);
  }

  @Override
  public int hashCode() {
    return Objects.hash($100k125k, $10k15k, $125k150k, $150k175k, $15k20k, $175k200k, $200k250k, $20k25k, $250k300k, $25k30k, $300k400k, $30k35k, $35k40k, $400k500k, $40k50k, $500k750k, $50k60k, $60k70k, $70k80k, $750k1M, $80k90k, $90k100k, medianHomeValue, over$1M, ownerOccupiedHouseholds, under$10k, contextHouseholds, contextLandarea);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Units {\n");
    sb.append("    $100k125k: ").append(toIndentedString($100k125k)).append("\n");
    sb.append("    $10k15k: ").append(toIndentedString($10k15k)).append("\n");
    sb.append("    $125k150k: ").append(toIndentedString($125k150k)).append("\n");
    sb.append("    $150k175k: ").append(toIndentedString($150k175k)).append("\n");
    sb.append("    $15k20k: ").append(toIndentedString($15k20k)).append("\n");
    sb.append("    $175k200k: ").append(toIndentedString($175k200k)).append("\n");
    sb.append("    $200k250k: ").append(toIndentedString($200k250k)).append("\n");
    sb.append("    $20k25k: ").append(toIndentedString($20k25k)).append("\n");
    sb.append("    $250k300k: ").append(toIndentedString($250k300k)).append("\n");
    sb.append("    $25k30k: ").append(toIndentedString($25k30k)).append("\n");
    sb.append("    $300k400k: ").append(toIndentedString($300k400k)).append("\n");
    sb.append("    $30k35k: ").append(toIndentedString($30k35k)).append("\n");
    sb.append("    $35k40k: ").append(toIndentedString($35k40k)).append("\n");
    sb.append("    $400k500k: ").append(toIndentedString($400k500k)).append("\n");
    sb.append("    $40k50k: ").append(toIndentedString($40k50k)).append("\n");
    sb.append("    $500k750k: ").append(toIndentedString($500k750k)).append("\n");
    sb.append("    $50k60k: ").append(toIndentedString($50k60k)).append("\n");
    sb.append("    $60k70k: ").append(toIndentedString($60k70k)).append("\n");
    sb.append("    $70k80k: ").append(toIndentedString($70k80k)).append("\n");
    sb.append("    $750k1M: ").append(toIndentedString($750k1M)).append("\n");
    sb.append("    $80k90k: ").append(toIndentedString($80k90k)).append("\n");
    sb.append("    $90k100k: ").append(toIndentedString($90k100k)).append("\n");
    sb.append("    medianHomeValue: ").append(toIndentedString(medianHomeValue)).append("\n");
    sb.append("    over$1M: ").append(toIndentedString(over$1M)).append("\n");
    sb.append("    ownerOccupiedHouseholds: ").append(toIndentedString(ownerOccupiedHouseholds)).append("\n");
    sb.append("    under$10k: ").append(toIndentedString(under$10k)).append("\n");
    sb.append("    contextHouseholds: ").append(toIndentedString(contextHouseholds)).append("\n");
    sb.append("    contextLandarea: ").append(toIndentedString(contextLandarea)).append("\n");
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
    openapiFields.add("$100k-125k");
    openapiFields.add("$10k-15k");
    openapiFields.add("$125k-150k");
    openapiFields.add("$150k-175k");
    openapiFields.add("$15k-20k");
    openapiFields.add("$175k-200k");
    openapiFields.add("$200k-250k");
    openapiFields.add("$20k-25k");
    openapiFields.add("$250k-300k");
    openapiFields.add("$25k-30k");
    openapiFields.add("$300k-400k");
    openapiFields.add("$30k-35k");
    openapiFields.add("$35k-40k");
    openapiFields.add("$400k-500k");
    openapiFields.add("$40k-50k");
    openapiFields.add("$500k-750k");
    openapiFields.add("$50k-60k");
    openapiFields.add("$60k-70k");
    openapiFields.add("$70k-80k");
    openapiFields.add("$750k-1M");
    openapiFields.add("$80k-90k");
    openapiFields.add("$90k-100k");
    openapiFields.add("Median Home Value");
    openapiFields.add("Over $1M");
    openapiFields.add("Owner Occupied Households");
    openapiFields.add("Under $10k");
    openapiFields.add("context.households");
    openapiFields.add("context.landarea");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("$100k-125k");
    openapiRequiredFields.add("$10k-15k");
    openapiRequiredFields.add("$125k-150k");
    openapiRequiredFields.add("$150k-175k");
    openapiRequiredFields.add("$15k-20k");
    openapiRequiredFields.add("$175k-200k");
    openapiRequiredFields.add("$200k-250k");
    openapiRequiredFields.add("$20k-25k");
    openapiRequiredFields.add("$250k-300k");
    openapiRequiredFields.add("$25k-30k");
    openapiRequiredFields.add("$300k-400k");
    openapiRequiredFields.add("$30k-35k");
    openapiRequiredFields.add("$35k-40k");
    openapiRequiredFields.add("$400k-500k");
    openapiRequiredFields.add("$40k-50k");
    openapiRequiredFields.add("$500k-750k");
    openapiRequiredFields.add("$50k-60k");
    openapiRequiredFields.add("$60k-70k");
    openapiRequiredFields.add("$70k-80k");
    openapiRequiredFields.add("$750k-1M");
    openapiRequiredFields.add("$80k-90k");
    openapiRequiredFields.add("$90k-100k");
    openapiRequiredFields.add("Median Home Value");
    openapiRequiredFields.add("Over $1M");
    openapiRequiredFields.add("Owner Occupied Households");
    openapiRequiredFields.add("Under $10k");
    openapiRequiredFields.add("context.households");
    openapiRequiredFields.add("context.landarea");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Units
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Units.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Units is not found in the empty JSON string", Units.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Units.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Units` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Units.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("$100k-125k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$100k-125k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$100k-125k").toString()));
      }
      if (!jsonObj.get("$10k-15k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$10k-15k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$10k-15k").toString()));
      }
      if (!jsonObj.get("$125k-150k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$125k-150k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$125k-150k").toString()));
      }
      if (!jsonObj.get("$150k-175k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$150k-175k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$150k-175k").toString()));
      }
      if (!jsonObj.get("$15k-20k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$15k-20k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$15k-20k").toString()));
      }
      if (!jsonObj.get("$175k-200k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$175k-200k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$175k-200k").toString()));
      }
      if (!jsonObj.get("$200k-250k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$200k-250k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$200k-250k").toString()));
      }
      if (!jsonObj.get("$20k-25k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$20k-25k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$20k-25k").toString()));
      }
      if (!jsonObj.get("$250k-300k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$250k-300k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$250k-300k").toString()));
      }
      if (!jsonObj.get("$25k-30k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$25k-30k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$25k-30k").toString()));
      }
      if (!jsonObj.get("$300k-400k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$300k-400k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$300k-400k").toString()));
      }
      if (!jsonObj.get("$30k-35k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$30k-35k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$30k-35k").toString()));
      }
      if (!jsonObj.get("$35k-40k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$35k-40k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$35k-40k").toString()));
      }
      if (!jsonObj.get("$400k-500k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$400k-500k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$400k-500k").toString()));
      }
      if (!jsonObj.get("$40k-50k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$40k-50k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$40k-50k").toString()));
      }
      if (!jsonObj.get("$500k-750k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$500k-750k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$500k-750k").toString()));
      }
      if (!jsonObj.get("$50k-60k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$50k-60k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$50k-60k").toString()));
      }
      if (!jsonObj.get("$60k-70k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$60k-70k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$60k-70k").toString()));
      }
      if (!jsonObj.get("$70k-80k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$70k-80k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$70k-80k").toString()));
      }
      if (!jsonObj.get("$750k-1M").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$750k-1M` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$750k-1M").toString()));
      }
      if (!jsonObj.get("$80k-90k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$80k-90k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$80k-90k").toString()));
      }
      if (!jsonObj.get("$90k-100k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `$90k-100k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("$90k-100k").toString()));
      }
      if (!jsonObj.get("Median Home Value").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Median Home Value` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Median Home Value").toString()));
      }
      if (!jsonObj.get("Over $1M").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Over $1M` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Over $1M").toString()));
      }
      if (!jsonObj.get("Owner Occupied Households").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Owner Occupied Households` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Owner Occupied Households").toString()));
      }
      if (!jsonObj.get("Under $10k").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `Under $10k` to be a primitive type in the JSON string but got `%s`", jsonObj.get("Under $10k").toString()));
      }
      if (!jsonObj.get("context.households").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `context.households` to be a primitive type in the JSON string but got `%s`", jsonObj.get("context.households").toString()));
      }
      if (!jsonObj.get("context.landarea").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `context.landarea` to be a primitive type in the JSON string but got `%s`", jsonObj.get("context.landarea").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Units.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Units' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Units> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Units.class));

       return (TypeAdapter<T>) new TypeAdapter<Units>() {
           @Override
           public void write(JsonWriter out, Units value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Units read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Units given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Units
   * @throws IOException if the JSON string is invalid with respect to Units
   */
  public static Units fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Units.class);
  }

  /**
   * Convert an instance of Units to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

