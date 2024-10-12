/*
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
import org.openapitools.client.model.AlternateImagesMixin;
import org.openapitools.client.model.AncestorTitles;
import org.openapitools.client.model.AncestorsTitles;
import org.openapitools.client.model.AvailabilityMixin;
import org.openapitools.client.model.ContributionsMixin;
import org.openapitools.client.model.Embargoed;
import org.openapitools.client.model.GenreGroupingsType;
import org.openapitools.client.model.Identifiers;
import org.openapitools.client.model.ImageLink;
import org.openapitools.client.model.ImagesMixin;
import org.openapitools.client.model.MasterBrandLink;
import org.openapitools.client.model.PidReference;
import org.openapitools.client.model.PreviousNextMixin;
import org.openapitools.client.model.ProgrammeFormats;
import org.openapitools.client.model.ProgrammeType;
import org.openapitools.client.model.Reference;
import org.openapitools.client.model.RelatedLinks;
import org.openapitools.client.model.ReleaseDateGroup;
import org.openapitools.client.model.Synopses;

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
 * Series
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:25.242429-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Series {
  public static final String SERIALIZED_NAME_ALTERNATE_IMAGES_MIXIN = "alternate_images_mixin";
  @SerializedName(SERIALIZED_NAME_ALTERNATE_IMAGES_MIXIN)
  private AlternateImagesMixin alternateImagesMixin;

  public static final String SERIALIZED_NAME_ANCESTOR_TITLES = "ancestor_titles";
  @SerializedName(SERIALIZED_NAME_ANCESTOR_TITLES)
  private AncestorTitles ancestorTitles;

  public static final String SERIALIZED_NAME_ANCESTORS = "ancestors";
  @SerializedName(SERIALIZED_NAME_ANCESTORS)
  private Reference ancestors;

  public static final String SERIALIZED_NAME_ANCESTORS_TITLES = "ancestors_titles";
  @SerializedName(SERIALIZED_NAME_ANCESTORS_TITLES)
  private AncestorsTitles ancestorsTitles;

  public static final String SERIALIZED_NAME_AVAILABILITY_MIXIN = "availability_mixin";
  @SerializedName(SERIALIZED_NAME_AVAILABILITY_MIXIN)
  private AvailabilityMixin availabilityMixin;

  public static final String SERIALIZED_NAME_CONTRIBUTIONS_MIXIN = "contributions_mixin";
  @SerializedName(SERIALIZED_NAME_CONTRIBUTIONS_MIXIN)
  private ContributionsMixin contributionsMixin;

  public static final String SERIALIZED_NAME_EMBARGOED = "embargoed";
  @SerializedName(SERIALIZED_NAME_EMBARGOED)
  private Embargoed embargoed;

  public static final String SERIALIZED_NAME_EXPECTED_CHILD_COUNT = "expected_child_count";
  @SerializedName(SERIALIZED_NAME_EXPECTED_CHILD_COUNT)
  private Integer expectedChildCount;

  public static final String SERIALIZED_NAME_GENRE_GROUPINGS = "genre_groupings";
  @SerializedName(SERIALIZED_NAME_GENRE_GROUPINGS)
  private GenreGroupingsType genreGroupings;

  public static final String SERIALIZED_NAME_IDENTIFIERS = "identifiers";
  @SerializedName(SERIALIZED_NAME_IDENTIFIERS)
  private Identifiers identifiers;

  public static final String SERIALIZED_NAME_IMAGE_LINK = "image_link";
  @SerializedName(SERIALIZED_NAME_IMAGE_LINK)
  private ImageLink imageLink;

  public static final String SERIALIZED_NAME_IMAGES_MIXIN = "images_mixin";
  @SerializedName(SERIALIZED_NAME_IMAGES_MIXIN)
  private ImagesMixin imagesMixin;

  public static final String SERIALIZED_NAME_IS_EMBEDDABLE = "is_embeddable";
  @SerializedName(SERIALIZED_NAME_IS_EMBEDDABLE)
  private Boolean isEmbeddable;

  public static final String SERIALIZED_NAME_ITEMS_FOR = "items_for";
  @SerializedName(SERIALIZED_NAME_ITEMS_FOR)
  private Reference itemsFor;

  public static final String SERIALIZED_NAME_MASTER_BRAND_LINK = "master_brand_link";
  @SerializedName(SERIALIZED_NAME_MASTER_BRAND_LINK)
  private MasterBrandLink masterBrandLink;

  public static final String SERIALIZED_NAME_PARTNER = "partner";
  @SerializedName(SERIALIZED_NAME_PARTNER)
  private String partner;

  public static final String SERIALIZED_NAME_PID = "pid";
  @SerializedName(SERIALIZED_NAME_PID)
  private String pid;

  public static final String SERIALIZED_NAME_PREVIOUS_NEXT_MIXIN = "previous_next_mixin";
  @SerializedName(SERIALIZED_NAME_PREVIOUS_NEXT_MIXIN)
  private PreviousNextMixin previousNextMixin;

  public static final String SERIALIZED_NAME_PROGRAMME_FORMATS = "programme_formats";
  @SerializedName(SERIALIZED_NAME_PROGRAMME_FORMATS)
  private ProgrammeFormats programmeFormats;

  public static final String SERIALIZED_NAME_PROGRAMME_TYPE = "programme_type";
  @SerializedName(SERIALIZED_NAME_PROGRAMME_TYPE)
  private ProgrammeType programmeType;

  public static final String SERIALIZED_NAME_RELATED_LINKS = "related_links";
  @SerializedName(SERIALIZED_NAME_RELATED_LINKS)
  private RelatedLinks relatedLinks;

  public static final String SERIALIZED_NAME_RELEASE_DATE_GROUP = "release_date_group";
  @SerializedName(SERIALIZED_NAME_RELEASE_DATE_GROUP)
  private ReleaseDateGroup releaseDateGroup;

  public static final String SERIALIZED_NAME_SERIES_OF = "series_of";
  @SerializedName(SERIALIZED_NAME_SERIES_OF)
  private PidReference seriesOf;

  public static final String SERIALIZED_NAME_SYNOPSES = "synopses";
  @SerializedName(SERIALIZED_NAME_SYNOPSES)
  private Synopses synopses;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updated_time";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_URI = "uri";
  @SerializedName(SERIALIZED_NAME_URI)
  private String uri;

  public Series() {
  }

  public Series alternateImagesMixin(AlternateImagesMixin alternateImagesMixin) {
    this.alternateImagesMixin = alternateImagesMixin;
    return this;
  }

  /**
   * Get alternateImagesMixin
   * @return alternateImagesMixin
   */
  @javax.annotation.Nullable
  public AlternateImagesMixin getAlternateImagesMixin() {
    return alternateImagesMixin;
  }

  public void setAlternateImagesMixin(AlternateImagesMixin alternateImagesMixin) {
    this.alternateImagesMixin = alternateImagesMixin;
  }


  public Series ancestorTitles(AncestorTitles ancestorTitles) {
    this.ancestorTitles = ancestorTitles;
    return this;
  }

  /**
   * Get ancestorTitles
   * @return ancestorTitles
   */
  @javax.annotation.Nullable
  public AncestorTitles getAncestorTitles() {
    return ancestorTitles;
  }

  public void setAncestorTitles(AncestorTitles ancestorTitles) {
    this.ancestorTitles = ancestorTitles;
  }


  public Series ancestors(Reference ancestors) {
    this.ancestors = ancestors;
    return this;
  }

  /**
   * Get ancestors
   * @return ancestors
   */
  @javax.annotation.Nullable
  public Reference getAncestors() {
    return ancestors;
  }

  public void setAncestors(Reference ancestors) {
    this.ancestors = ancestors;
  }


  public Series ancestorsTitles(AncestorsTitles ancestorsTitles) {
    this.ancestorsTitles = ancestorsTitles;
    return this;
  }

  /**
   * Get ancestorsTitles
   * @return ancestorsTitles
   */
  @javax.annotation.Nullable
  public AncestorsTitles getAncestorsTitles() {
    return ancestorsTitles;
  }

  public void setAncestorsTitles(AncestorsTitles ancestorsTitles) {
    this.ancestorsTitles = ancestorsTitles;
  }


  public Series availabilityMixin(AvailabilityMixin availabilityMixin) {
    this.availabilityMixin = availabilityMixin;
    return this;
  }

  /**
   * Get availabilityMixin
   * @return availabilityMixin
   */
  @javax.annotation.Nullable
  public AvailabilityMixin getAvailabilityMixin() {
    return availabilityMixin;
  }

  public void setAvailabilityMixin(AvailabilityMixin availabilityMixin) {
    this.availabilityMixin = availabilityMixin;
  }


  public Series contributionsMixin(ContributionsMixin contributionsMixin) {
    this.contributionsMixin = contributionsMixin;
    return this;
  }

  /**
   * Get contributionsMixin
   * @return contributionsMixin
   */
  @javax.annotation.Nullable
  public ContributionsMixin getContributionsMixin() {
    return contributionsMixin;
  }

  public void setContributionsMixin(ContributionsMixin contributionsMixin) {
    this.contributionsMixin = contributionsMixin;
  }


  public Series embargoed(Embargoed embargoed) {
    this.embargoed = embargoed;
    return this;
  }

  /**
   * Get embargoed
   * @return embargoed
   */
  @javax.annotation.Nonnull
  public Embargoed getEmbargoed() {
    return embargoed;
  }

  public void setEmbargoed(Embargoed embargoed) {
    this.embargoed = embargoed;
  }


  public Series expectedChildCount(Integer expectedChildCount) {
    this.expectedChildCount = expectedChildCount;
    return this;
  }

  /**
   * Get expectedChildCount
   * @return expectedChildCount
   */
  @javax.annotation.Nullable
  public Integer getExpectedChildCount() {
    return expectedChildCount;
  }

  public void setExpectedChildCount(Integer expectedChildCount) {
    this.expectedChildCount = expectedChildCount;
  }


  public Series genreGroupings(GenreGroupingsType genreGroupings) {
    this.genreGroupings = genreGroupings;
    return this;
  }

  /**
   * Get genreGroupings
   * @return genreGroupings
   */
  @javax.annotation.Nullable
  public GenreGroupingsType getGenreGroupings() {
    return genreGroupings;
  }

  public void setGenreGroupings(GenreGroupingsType genreGroupings) {
    this.genreGroupings = genreGroupings;
  }


  public Series identifiers(Identifiers identifiers) {
    this.identifiers = identifiers;
    return this;
  }

  /**
   * Get identifiers
   * @return identifiers
   */
  @javax.annotation.Nullable
  public Identifiers getIdentifiers() {
    return identifiers;
  }

  public void setIdentifiers(Identifiers identifiers) {
    this.identifiers = identifiers;
  }


  public Series imageLink(ImageLink imageLink) {
    this.imageLink = imageLink;
    return this;
  }

  /**
   * Get imageLink
   * @return imageLink
   */
  @javax.annotation.Nullable
  public ImageLink getImageLink() {
    return imageLink;
  }

  public void setImageLink(ImageLink imageLink) {
    this.imageLink = imageLink;
  }


  public Series imagesMixin(ImagesMixin imagesMixin) {
    this.imagesMixin = imagesMixin;
    return this;
  }

  /**
   * Get imagesMixin
   * @return imagesMixin
   */
  @javax.annotation.Nullable
  public ImagesMixin getImagesMixin() {
    return imagesMixin;
  }

  public void setImagesMixin(ImagesMixin imagesMixin) {
    this.imagesMixin = imagesMixin;
  }


  public Series isEmbeddable(Boolean isEmbeddable) {
    this.isEmbeddable = isEmbeddable;
    return this;
  }

  /**
   * Get isEmbeddable
   * @return isEmbeddable
   */
  @javax.annotation.Nullable
  public Boolean getIsEmbeddable() {
    return isEmbeddable;
  }

  public void setIsEmbeddable(Boolean isEmbeddable) {
    this.isEmbeddable = isEmbeddable;
  }


  public Series itemsFor(Reference itemsFor) {
    this.itemsFor = itemsFor;
    return this;
  }

  /**
   * Get itemsFor
   * @return itemsFor
   */
  @javax.annotation.Nullable
  public Reference getItemsFor() {
    return itemsFor;
  }

  public void setItemsFor(Reference itemsFor) {
    this.itemsFor = itemsFor;
  }


  public Series masterBrandLink(MasterBrandLink masterBrandLink) {
    this.masterBrandLink = masterBrandLink;
    return this;
  }

  /**
   * Get masterBrandLink
   * @return masterBrandLink
   */
  @javax.annotation.Nullable
  public MasterBrandLink getMasterBrandLink() {
    return masterBrandLink;
  }

  public void setMasterBrandLink(MasterBrandLink masterBrandLink) {
    this.masterBrandLink = masterBrandLink;
  }


  public Series partner(String partner) {
    this.partner = partner;
    return this;
  }

  /**
   * Get partner
   * @return partner
   */
  @javax.annotation.Nonnull
  public String getPartner() {
    return partner;
  }

  public void setPartner(String partner) {
    this.partner = partner;
  }


  public Series pid(String pid) {
    this.pid = pid;
    return this;
  }

  /**
   * Get pid
   * @return pid
   */
  @javax.annotation.Nonnull
  public String getPid() {
    return pid;
  }

  public void setPid(String pid) {
    this.pid = pid;
  }


  public Series previousNextMixin(PreviousNextMixin previousNextMixin) {
    this.previousNextMixin = previousNextMixin;
    return this;
  }

  /**
   * Get previousNextMixin
   * @return previousNextMixin
   */
  @javax.annotation.Nullable
  public PreviousNextMixin getPreviousNextMixin() {
    return previousNextMixin;
  }

  public void setPreviousNextMixin(PreviousNextMixin previousNextMixin) {
    this.previousNextMixin = previousNextMixin;
  }


  public Series programmeFormats(ProgrammeFormats programmeFormats) {
    this.programmeFormats = programmeFormats;
    return this;
  }

  /**
   * Get programmeFormats
   * @return programmeFormats
   */
  @javax.annotation.Nullable
  public ProgrammeFormats getProgrammeFormats() {
    return programmeFormats;
  }

  public void setProgrammeFormats(ProgrammeFormats programmeFormats) {
    this.programmeFormats = programmeFormats;
  }


  public Series programmeType(ProgrammeType programmeType) {
    this.programmeType = programmeType;
    return this;
  }

  /**
   * Get programmeType
   * @return programmeType
   */
  @javax.annotation.Nullable
  public ProgrammeType getProgrammeType() {
    return programmeType;
  }

  public void setProgrammeType(ProgrammeType programmeType) {
    this.programmeType = programmeType;
  }


  public Series relatedLinks(RelatedLinks relatedLinks) {
    this.relatedLinks = relatedLinks;
    return this;
  }

  /**
   * Get relatedLinks
   * @return relatedLinks
   */
  @javax.annotation.Nullable
  public RelatedLinks getRelatedLinks() {
    return relatedLinks;
  }

  public void setRelatedLinks(RelatedLinks relatedLinks) {
    this.relatedLinks = relatedLinks;
  }


  public Series releaseDateGroup(ReleaseDateGroup releaseDateGroup) {
    this.releaseDateGroup = releaseDateGroup;
    return this;
  }

  /**
   * Get releaseDateGroup
   * @return releaseDateGroup
   */
  @javax.annotation.Nullable
  public ReleaseDateGroup getReleaseDateGroup() {
    return releaseDateGroup;
  }

  public void setReleaseDateGroup(ReleaseDateGroup releaseDateGroup) {
    this.releaseDateGroup = releaseDateGroup;
  }


  public Series seriesOf(PidReference seriesOf) {
    this.seriesOf = seriesOf;
    return this;
  }

  /**
   * Get seriesOf
   * @return seriesOf
   */
  @javax.annotation.Nullable
  public PidReference getSeriesOf() {
    return seriesOf;
  }

  public void setSeriesOf(PidReference seriesOf) {
    this.seriesOf = seriesOf;
  }


  public Series synopses(Synopses synopses) {
    this.synopses = synopses;
    return this;
  }

  /**
   * Get synopses
   * @return synopses
   */
  @javax.annotation.Nullable
  public Synopses getSynopses() {
    return synopses;
  }

  public void setSynopses(Synopses synopses) {
    this.synopses = synopses;
  }


  public Series title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Series updatedTime(OffsetDateTime updatedTime) {
    this.updatedTime = updatedTime;
    return this;
  }

  /**
   * Get updatedTime
   * @return updatedTime
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }

  public void setUpdatedTime(OffsetDateTime updatedTime) {
    this.updatedTime = updatedTime;
  }


  public Series uri(String uri) {
    this.uri = uri;
    return this;
  }

  /**
   * Get uri
   * @return uri
   */
  @javax.annotation.Nullable
  public String getUri() {
    return uri;
  }

  public void setUri(String uri) {
    this.uri = uri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Series series = (Series) o;
    return Objects.equals(this.alternateImagesMixin, series.alternateImagesMixin) &&
        Objects.equals(this.ancestorTitles, series.ancestorTitles) &&
        Objects.equals(this.ancestors, series.ancestors) &&
        Objects.equals(this.ancestorsTitles, series.ancestorsTitles) &&
        Objects.equals(this.availabilityMixin, series.availabilityMixin) &&
        Objects.equals(this.contributionsMixin, series.contributionsMixin) &&
        Objects.equals(this.embargoed, series.embargoed) &&
        Objects.equals(this.expectedChildCount, series.expectedChildCount) &&
        Objects.equals(this.genreGroupings, series.genreGroupings) &&
        Objects.equals(this.identifiers, series.identifiers) &&
        Objects.equals(this.imageLink, series.imageLink) &&
        Objects.equals(this.imagesMixin, series.imagesMixin) &&
        Objects.equals(this.isEmbeddable, series.isEmbeddable) &&
        Objects.equals(this.itemsFor, series.itemsFor) &&
        Objects.equals(this.masterBrandLink, series.masterBrandLink) &&
        Objects.equals(this.partner, series.partner) &&
        Objects.equals(this.pid, series.pid) &&
        Objects.equals(this.previousNextMixin, series.previousNextMixin) &&
        Objects.equals(this.programmeFormats, series.programmeFormats) &&
        Objects.equals(this.programmeType, series.programmeType) &&
        Objects.equals(this.relatedLinks, series.relatedLinks) &&
        Objects.equals(this.releaseDateGroup, series.releaseDateGroup) &&
        Objects.equals(this.seriesOf, series.seriesOf) &&
        Objects.equals(this.synopses, series.synopses) &&
        Objects.equals(this.title, series.title) &&
        Objects.equals(this.updatedTime, series.updatedTime) &&
        Objects.equals(this.uri, series.uri);
  }

  @Override
  public int hashCode() {
    return Objects.hash(alternateImagesMixin, ancestorTitles, ancestors, ancestorsTitles, availabilityMixin, contributionsMixin, embargoed, expectedChildCount, genreGroupings, identifiers, imageLink, imagesMixin, isEmbeddable, itemsFor, masterBrandLink, partner, pid, previousNextMixin, programmeFormats, programmeType, relatedLinks, releaseDateGroup, seriesOf, synopses, title, updatedTime, uri);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Series {\n");
    sb.append("    alternateImagesMixin: ").append(toIndentedString(alternateImagesMixin)).append("\n");
    sb.append("    ancestorTitles: ").append(toIndentedString(ancestorTitles)).append("\n");
    sb.append("    ancestors: ").append(toIndentedString(ancestors)).append("\n");
    sb.append("    ancestorsTitles: ").append(toIndentedString(ancestorsTitles)).append("\n");
    sb.append("    availabilityMixin: ").append(toIndentedString(availabilityMixin)).append("\n");
    sb.append("    contributionsMixin: ").append(toIndentedString(contributionsMixin)).append("\n");
    sb.append("    embargoed: ").append(toIndentedString(embargoed)).append("\n");
    sb.append("    expectedChildCount: ").append(toIndentedString(expectedChildCount)).append("\n");
    sb.append("    genreGroupings: ").append(toIndentedString(genreGroupings)).append("\n");
    sb.append("    identifiers: ").append(toIndentedString(identifiers)).append("\n");
    sb.append("    imageLink: ").append(toIndentedString(imageLink)).append("\n");
    sb.append("    imagesMixin: ").append(toIndentedString(imagesMixin)).append("\n");
    sb.append("    isEmbeddable: ").append(toIndentedString(isEmbeddable)).append("\n");
    sb.append("    itemsFor: ").append(toIndentedString(itemsFor)).append("\n");
    sb.append("    masterBrandLink: ").append(toIndentedString(masterBrandLink)).append("\n");
    sb.append("    partner: ").append(toIndentedString(partner)).append("\n");
    sb.append("    pid: ").append(toIndentedString(pid)).append("\n");
    sb.append("    previousNextMixin: ").append(toIndentedString(previousNextMixin)).append("\n");
    sb.append("    programmeFormats: ").append(toIndentedString(programmeFormats)).append("\n");
    sb.append("    programmeType: ").append(toIndentedString(programmeType)).append("\n");
    sb.append("    relatedLinks: ").append(toIndentedString(relatedLinks)).append("\n");
    sb.append("    releaseDateGroup: ").append(toIndentedString(releaseDateGroup)).append("\n");
    sb.append("    seriesOf: ").append(toIndentedString(seriesOf)).append("\n");
    sb.append("    synopses: ").append(toIndentedString(synopses)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    uri: ").append(toIndentedString(uri)).append("\n");
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
    openapiFields.add("alternate_images_mixin");
    openapiFields.add("ancestor_titles");
    openapiFields.add("ancestors");
    openapiFields.add("ancestors_titles");
    openapiFields.add("availability_mixin");
    openapiFields.add("contributions_mixin");
    openapiFields.add("embargoed");
    openapiFields.add("expected_child_count");
    openapiFields.add("genre_groupings");
    openapiFields.add("identifiers");
    openapiFields.add("image_link");
    openapiFields.add("images_mixin");
    openapiFields.add("is_embeddable");
    openapiFields.add("items_for");
    openapiFields.add("master_brand_link");
    openapiFields.add("partner");
    openapiFields.add("pid");
    openapiFields.add("previous_next_mixin");
    openapiFields.add("programme_formats");
    openapiFields.add("programme_type");
    openapiFields.add("related_links");
    openapiFields.add("release_date_group");
    openapiFields.add("series_of");
    openapiFields.add("synopses");
    openapiFields.add("title");
    openapiFields.add("updated_time");
    openapiFields.add("uri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("embargoed");
    openapiRequiredFields.add("partner");
    openapiRequiredFields.add("pid");
    openapiRequiredFields.add("updated_time");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Series
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Series.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Series is not found in the empty JSON string", Series.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Series.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Series` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Series.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `alternate_images_mixin`
      if (jsonObj.get("alternate_images_mixin") != null && !jsonObj.get("alternate_images_mixin").isJsonNull()) {
        AlternateImagesMixin.validateJsonElement(jsonObj.get("alternate_images_mixin"));
      }
      // validate the optional field `ancestor_titles`
      if (jsonObj.get("ancestor_titles") != null && !jsonObj.get("ancestor_titles").isJsonNull()) {
        AncestorTitles.validateJsonElement(jsonObj.get("ancestor_titles"));
      }
      // validate the optional field `ancestors`
      if (jsonObj.get("ancestors") != null && !jsonObj.get("ancestors").isJsonNull()) {
        Reference.validateJsonElement(jsonObj.get("ancestors"));
      }
      // validate the optional field `ancestors_titles`
      if (jsonObj.get("ancestors_titles") != null && !jsonObj.get("ancestors_titles").isJsonNull()) {
        AncestorsTitles.validateJsonElement(jsonObj.get("ancestors_titles"));
      }
      // validate the optional field `availability_mixin`
      if (jsonObj.get("availability_mixin") != null && !jsonObj.get("availability_mixin").isJsonNull()) {
        AvailabilityMixin.validateJsonElement(jsonObj.get("availability_mixin"));
      }
      // validate the optional field `contributions_mixin`
      if (jsonObj.get("contributions_mixin") != null && !jsonObj.get("contributions_mixin").isJsonNull()) {
        ContributionsMixin.validateJsonElement(jsonObj.get("contributions_mixin"));
      }
      // validate the required field `embargoed`
      Embargoed.validateJsonElement(jsonObj.get("embargoed"));
      // validate the optional field `genre_groupings`
      if (jsonObj.get("genre_groupings") != null && !jsonObj.get("genre_groupings").isJsonNull()) {
        GenreGroupingsType.validateJsonElement(jsonObj.get("genre_groupings"));
      }
      // validate the optional field `identifiers`
      if (jsonObj.get("identifiers") != null && !jsonObj.get("identifiers").isJsonNull()) {
        Identifiers.validateJsonElement(jsonObj.get("identifiers"));
      }
      // validate the optional field `image_link`
      if (jsonObj.get("image_link") != null && !jsonObj.get("image_link").isJsonNull()) {
        ImageLink.validateJsonElement(jsonObj.get("image_link"));
      }
      // validate the optional field `images_mixin`
      if (jsonObj.get("images_mixin") != null && !jsonObj.get("images_mixin").isJsonNull()) {
        ImagesMixin.validateJsonElement(jsonObj.get("images_mixin"));
      }
      // validate the optional field `items_for`
      if (jsonObj.get("items_for") != null && !jsonObj.get("items_for").isJsonNull()) {
        Reference.validateJsonElement(jsonObj.get("items_for"));
      }
      // validate the optional field `master_brand_link`
      if (jsonObj.get("master_brand_link") != null && !jsonObj.get("master_brand_link").isJsonNull()) {
        MasterBrandLink.validateJsonElement(jsonObj.get("master_brand_link"));
      }
      if (!jsonObj.get("partner").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `partner` to be a primitive type in the JSON string but got `%s`", jsonObj.get("partner").toString()));
      }
      if (!jsonObj.get("pid").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pid` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pid").toString()));
      }
      // validate the optional field `previous_next_mixin`
      if (jsonObj.get("previous_next_mixin") != null && !jsonObj.get("previous_next_mixin").isJsonNull()) {
        PreviousNextMixin.validateJsonElement(jsonObj.get("previous_next_mixin"));
      }
      // validate the optional field `programme_formats`
      if (jsonObj.get("programme_formats") != null && !jsonObj.get("programme_formats").isJsonNull()) {
        ProgrammeFormats.validateJsonElement(jsonObj.get("programme_formats"));
      }
      // validate the optional field `programme_type`
      if (jsonObj.get("programme_type") != null && !jsonObj.get("programme_type").isJsonNull()) {
        ProgrammeType.validateJsonElement(jsonObj.get("programme_type"));
      }
      // validate the optional field `related_links`
      if (jsonObj.get("related_links") != null && !jsonObj.get("related_links").isJsonNull()) {
        RelatedLinks.validateJsonElement(jsonObj.get("related_links"));
      }
      // validate the optional field `release_date_group`
      if (jsonObj.get("release_date_group") != null && !jsonObj.get("release_date_group").isJsonNull()) {
        ReleaseDateGroup.validateJsonElement(jsonObj.get("release_date_group"));
      }
      // validate the optional field `series_of`
      if (jsonObj.get("series_of") != null && !jsonObj.get("series_of").isJsonNull()) {
        PidReference.validateJsonElement(jsonObj.get("series_of"));
      }
      // validate the optional field `synopses`
      if (jsonObj.get("synopses") != null && !jsonObj.get("synopses").isJsonNull()) {
        Synopses.validateJsonElement(jsonObj.get("synopses"));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      if ((jsonObj.get("uri") != null && !jsonObj.get("uri").isJsonNull()) && !jsonObj.get("uri").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `uri` to be a primitive type in the JSON string but got `%s`", jsonObj.get("uri").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Series.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Series' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Series> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Series.class));

       return (TypeAdapter<T>) new TypeAdapter<Series>() {
           @Override
           public void write(JsonWriter out, Series value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Series read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Series given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Series
   * @throws IOException if the JSON string is invalid with respect to Series
   */
  public static Series fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Series.class);
  }

  /**
   * Convert an instance of Series to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

