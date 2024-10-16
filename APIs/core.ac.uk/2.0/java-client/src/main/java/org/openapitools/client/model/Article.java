/*
 * CORE API v2
 * <p style=\"text-align: justify;\">You can use the CORE API to access the      resources harvested and enriched by CORE. If you encounter any problems with the API, please <a href=\"/contact\">report them to us</a>.</p>  <h2>Overview</h2> <p style=\"text-align: justify;\">The API is organised by resource type. The resources are <b>articles</b>,      <b>journals</b> and <b>repositories</b> and are represented using JSON data format. Furthermore,      each resource has a list of methods. The API also provides two global methods for accessing all resources at once.</p>  <h2>Response format</h2> <p style=\"text-align: justify;\">Response for each query contains two fields: <b>status</b> and <b>data</b>.     In case of an error status, the data field is empty. The data field contains a single object     in case the request is for a specific identifier (e.g. CORE ID, CORE repository ID, etc.), or       contains a list of objects, for example for search queries. In case of batch requests, the response     is an array of objects, each of which contains its own <b>status</b> and <b>data</b> fields.     For search queries the response contains an additional field <b>totalHits</b>, which is the      total number of items which match the search criteria.</p>  <h2>Search query syntax</h2>  <p style=\"text-align: justify\">Complex search queries can be used in all of the API search methods.     The query can be a simple string or it can be built using terms and operators described in Elasticsearch     <a href=\"http://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-query-string-query.html#query-string-syntax\">documentation</a>.     The usable field names are <strong>title</strong>, <strong>description</strong>, <strong>fullText</strong>,      <strong>authors</strong>, <strong>publisher</strong>, <strong>repositories.id</strong>, <strong>repositories.name</strong>,      <strong>doi</strong>, <strong>oai</strong>, <strong>identifiers</strong> (which is a list of article identifiers including OAI, URL, etc.), <strong>language.name</strong>      and <strong>year</strong>. Some example queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>title:psychology and language.name:English</p></li>     <li><p>repositories.id:86 AND year:2014</p></li>     <li><p>identifiers:\"oai:aura.abdn.ac.uk:2164/3837\" OR identifiers:\"oai:aura.abdn.ac.uk:2164/3843\"</p></li>     <li><p>doi:\"10.1186/1471-2458-6-309\"</p></li> </ul>  <h3>Retrieving the latest Articles</h3> <p style=\"text-align: justify\">     You can retrieve the harvested items since specific dates using the following queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>repositoryDocument.metadataUpdated:>2017-02-10</p></li>     <li><p>repositoryDocument.metadataUpdated:>2017-03-01 AND repositoryDocument.metadataUpdated:<2017-03-31</p></li>     </ul>  <h2>Sort order</h2>  <p style=\"text-align: justify;\">For search queries, the results are ordered by relevance score. For batch      requests, the results are retrieved in the order of the requests.</p>  <h2>Parameters</h2> <p style=\"text-align: justify;\">The API methods allow different parameters to be passed. Additionally, there is an API key parameter which is common to all API methods. For all API methods      the API key can be provided either as a query parameter or in the request header. If the API key      is not provided, the API will return HTTP 401 error. You can register for an API key <a href=\"/services#api\">here</a>.</p>  <h2>API methods</h2>
 *
 * The version of the OpenAPI document: 2.0
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
import org.openapitools.client.model.ArticleJournal;
import org.openapitools.client.model.Citation;
import org.openapitools.client.model.Language;
import org.openapitools.client.model.RawRecordXml;
import org.openapitools.client.model.Repository;
import org.openapitools.client.model.Similar;

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
 * Article
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:44.717365-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Article {
  public static final String SERIALIZED_NAME_AUTHORS = "authors";
  @SerializedName(SERIALIZED_NAME_AUTHORS)
  private List<String> authors = new ArrayList<>();

  public static final String SERIALIZED_NAME_CITATIONS = "citations";
  @SerializedName(SERIALIZED_NAME_CITATIONS)
  private List<Citation> citations = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONTRIBUTORS = "contributors";
  @SerializedName(SERIALIZED_NAME_CONTRIBUTORS)
  private List<String> contributors = new ArrayList<>();

  public static final String SERIALIZED_NAME_DATE_PUBLISHED = "datePublished";
  @SerializedName(SERIALIZED_NAME_DATE_PUBLISHED)
  private String datePublished;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DOI = "doi";
  @SerializedName(SERIALIZED_NAME_DOI)
  private String doi;

  public static final String SERIALIZED_NAME_DOWNLOAD_URL = "downloadUrl";
  @SerializedName(SERIALIZED_NAME_DOWNLOAD_URL)
  private String downloadUrl;

  public static final String SERIALIZED_NAME_FULLTEXT = "fulltext";
  @SerializedName(SERIALIZED_NAME_FULLTEXT)
  private String fulltext;

  public static final String SERIALIZED_NAME_FULLTEXT_IDENTIFIER = "fulltextIdentifier";
  @SerializedName(SERIALIZED_NAME_FULLTEXT_IDENTIFIER)
  private String fulltextIdentifier;

  public static final String SERIALIZED_NAME_FULLTEXT_URLS = "fulltextUrls";
  @SerializedName(SERIALIZED_NAME_FULLTEXT_URLS)
  private List<String> fulltextUrls = new ArrayList<>();

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IDENTIFIERS = "identifiers";
  @SerializedName(SERIALIZED_NAME_IDENTIFIERS)
  private List<String> identifiers = new ArrayList<>();

  public static final String SERIALIZED_NAME_JOURNALS = "journals";
  @SerializedName(SERIALIZED_NAME_JOURNALS)
  private List<ArticleJournal> journals = new ArrayList<>();

  public static final String SERIALIZED_NAME_LANGUAGE = "language";
  @SerializedName(SERIALIZED_NAME_LANGUAGE)
  private Language language;

  public static final String SERIALIZED_NAME_OAI = "oai";
  @SerializedName(SERIALIZED_NAME_OAI)
  private String oai;

  public static final String SERIALIZED_NAME_PUBLISHER = "publisher";
  @SerializedName(SERIALIZED_NAME_PUBLISHER)
  private String publisher;

  public static final String SERIALIZED_NAME_RAW_RECORD_XML = "rawRecordXml";
  @SerializedName(SERIALIZED_NAME_RAW_RECORD_XML)
  private RawRecordXml rawRecordXml;

  public static final String SERIALIZED_NAME_RELATIONS = "relations";
  @SerializedName(SERIALIZED_NAME_RELATIONS)
  private List<String> relations = new ArrayList<>();

  public static final String SERIALIZED_NAME_REPOSITORIES = "repositories";
  @SerializedName(SERIALIZED_NAME_REPOSITORIES)
  private List<Repository> repositories = new ArrayList<>();

  public static final String SERIALIZED_NAME_REPOSITORY_DOCUMENT = "repositoryDocument";
  @SerializedName(SERIALIZED_NAME_REPOSITORY_DOCUMENT)
  private Object repositoryDocument;

  public static final String SERIALIZED_NAME_SIMILARITIES = "similarities";
  @SerializedName(SERIALIZED_NAME_SIMILARITIES)
  private List<Similar> similarities = new ArrayList<>();

  public static final String SERIALIZED_NAME_SUBJECTS = "subjects";
  @SerializedName(SERIALIZED_NAME_SUBJECTS)
  private List<String> subjects = new ArrayList<>();

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public static final String SERIALIZED_NAME_TOPICS = "topics";
  @SerializedName(SERIALIZED_NAME_TOPICS)
  private List<String> topics = new ArrayList<>();

  public static final String SERIALIZED_NAME_TYPES = "types";
  @SerializedName(SERIALIZED_NAME_TYPES)
  private List<String> types = new ArrayList<>();

  public static final String SERIALIZED_NAME_YEAR = "year";
  @SerializedName(SERIALIZED_NAME_YEAR)
  private Integer year;

  public Article() {
  }

  public Article authors(List<String> authors) {
    this.authors = authors;
    return this;
  }

  public Article addAuthorsItem(String authorsItem) {
    if (this.authors == null) {
      this.authors = new ArrayList<>();
    }
    this.authors.add(authorsItem);
    return this;
  }

  /**
   * List of article authors
   * @return authors
   */
  @javax.annotation.Nullable
  public List<String> getAuthors() {
    return authors;
  }

  public void setAuthors(List<String> authors) {
    this.authors = authors;
  }


  public Article citations(List<Citation> citations) {
    this.citations = citations;
    return this;
  }

  public Article addCitationsItem(Citation citationsItem) {
    if (this.citations == null) {
      this.citations = new ArrayList<>();
    }
    this.citations.add(citationsItem);
    return this;
  }

  /**
   * Citations found in the article
   * @return citations
   */
  @javax.annotation.Nullable
  public List<Citation> getCitations() {
    return citations;
  }

  public void setCitations(List<Citation> citations) {
    this.citations = citations;
  }


  public Article contributors(List<String> contributors) {
    this.contributors = contributors;
    return this;
  }

  public Article addContributorsItem(String contributorsItem) {
    if (this.contributors == null) {
      this.contributors = new ArrayList<>();
    }
    this.contributors.add(contributorsItem);
    return this;
  }

  /**
   * List of article contributors
   * @return contributors
   */
  @javax.annotation.Nullable
  public List<String> getContributors() {
    return contributors;
  }

  public void setContributors(List<String> contributors) {
    this.contributors = contributors;
  }


  public Article datePublished(String datePublished) {
    this.datePublished = datePublished;
    return this;
  }

  /**
   * Date article published
   * @return datePublished
   */
  @javax.annotation.Nullable
  public String getDatePublished() {
    return datePublished;
  }

  public void setDatePublished(String datePublished) {
    this.datePublished = datePublished;
  }


  public Article description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The abstract
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Article doi(String doi) {
    this.doi = doi;
    return this;
  }

  /**
   * The DOI of the article
   * @return doi
   */
  @javax.annotation.Nullable
  public String getDoi() {
    return doi;
  }

  public void setDoi(String doi) {
    this.doi = doi;
  }


  public Article downloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
    return this;
  }

  /**
   * The download PDF URL which is displayed on our /display/[ArticleID] page
   * @return downloadUrl
   */
  @javax.annotation.Nullable
  public String getDownloadUrl() {
    return downloadUrl;
  }

  public void setDownloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
  }


  public Article fulltext(String fulltext) {
    this.fulltext = fulltext;
    return this;
  }

  /**
   * Article full text
   * @return fulltext
   */
  @javax.annotation.Nullable
  public String getFulltext() {
    return fulltext;
  }

  public void setFulltext(String fulltext) {
    this.fulltext = fulltext;
  }


  public Article fulltextIdentifier(String fulltextIdentifier) {
    this.fulltextIdentifier = fulltextIdentifier;
    return this;
  }

  /**
   * The URL to the fulltext
   * @return fulltextIdentifier
   */
  @javax.annotation.Nullable
  public String getFulltextIdentifier() {
    return fulltextIdentifier;
  }

  public void setFulltextIdentifier(String fulltextIdentifier) {
    this.fulltextIdentifier = fulltextIdentifier;
  }


  public Article fulltextUrls(List<String> fulltextUrls) {
    this.fulltextUrls = fulltextUrls;
    return this;
  }

  public Article addFulltextUrlsItem(String fulltextUrlsItem) {
    if (this.fulltextUrls == null) {
      this.fulltextUrls = new ArrayList<>();
    }
    this.fulltextUrls.add(fulltextUrlsItem);
    return this;
  }

  /**
   * URLs of the fulltext version of this article
   * @return fulltextUrls
   */
  @javax.annotation.Nullable
  public List<String> getFulltextUrls() {
    return fulltextUrls;
  }

  public void setFulltextUrls(List<String> fulltextUrls) {
    this.fulltextUrls = fulltextUrls;
  }


  public Article id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Article ID
   * @return id
   */
  @javax.annotation.Nonnull
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public Article identifiers(List<String> identifiers) {
    this.identifiers = identifiers;
    return this;
  }

  public Article addIdentifiersItem(String identifiersItem) {
    if (this.identifiers == null) {
      this.identifiers = new ArrayList<>();
    }
    this.identifiers.add(identifiersItem);
    return this;
  }

  /**
   * List of document identifiers
   * @return identifiers
   */
  @javax.annotation.Nullable
  public List<String> getIdentifiers() {
    return identifiers;
  }

  public void setIdentifiers(List<String> identifiers) {
    this.identifiers = identifiers;
  }


  public Article journals(List<ArticleJournal> journals) {
    this.journals = journals;
    return this;
  }

  public Article addJournalsItem(ArticleJournal journalsItem) {
    if (this.journals == null) {
      this.journals = new ArrayList<>();
    }
    this.journals.add(journalsItem);
    return this;
  }

  /**
   * List of journals this article belongs to
   * @return journals
   */
  @javax.annotation.Nullable
  public List<ArticleJournal> getJournals() {
    return journals;
  }

  public void setJournals(List<ArticleJournal> journals) {
    this.journals = journals;
  }


  public Article language(Language language) {
    this.language = language;
    return this;
  }

  /**
   * Get language
   * @return language
   */
  @javax.annotation.Nullable
  public Language getLanguage() {
    return language;
  }

  public void setLanguage(Language language) {
    this.language = language;
  }


  public Article oai(String oai) {
    this.oai = oai;
    return this;
  }

  /**
   * The OAI of the article
   * @return oai
   */
  @javax.annotation.Nullable
  public String getOai() {
    return oai;
  }

  public void setOai(String oai) {
    this.oai = oai;
  }


  public Article publisher(String publisher) {
    this.publisher = publisher;
    return this;
  }

  /**
   * Publisher of the article
   * @return publisher
   */
  @javax.annotation.Nullable
  public String getPublisher() {
    return publisher;
  }

  public void setPublisher(String publisher) {
    this.publisher = publisher;
  }


  public Article rawRecordXml(RawRecordXml rawRecordXml) {
    this.rawRecordXml = rawRecordXml;
    return this;
  }

  /**
   * Get rawRecordXml
   * @return rawRecordXml
   */
  @javax.annotation.Nullable
  public RawRecordXml getRawRecordXml() {
    return rawRecordXml;
  }

  public void setRawRecordXml(RawRecordXml rawRecordXml) {
    this.rawRecordXml = rawRecordXml;
  }


  public Article relations(List<String> relations) {
    this.relations = relations;
    return this;
  }

  public Article addRelationsItem(String relationsItem) {
    if (this.relations == null) {
      this.relations = new ArrayList<>();
    }
    this.relations.add(relationsItem);
    return this;
  }

  /**
   * URLs of relating articles, etc.
   * @return relations
   */
  @javax.annotation.Nullable
  public List<String> getRelations() {
    return relations;
  }

  public void setRelations(List<String> relations) {
    this.relations = relations;
  }


  public Article repositories(List<Repository> repositories) {
    this.repositories = repositories;
    return this;
  }

  public Article addRepositoriesItem(Repository repositoriesItem) {
    if (this.repositories == null) {
      this.repositories = new ArrayList<>();
    }
    this.repositories.add(repositoriesItem);
    return this;
  }

  /**
   * List of repositories this article belongs to
   * @return repositories
   */
  @javax.annotation.Nullable
  public List<Repository> getRepositories() {
    return repositories;
  }

  public void setRepositories(List<Repository> repositories) {
    this.repositories = repositories;
  }


  public Article repositoryDocument(Object repositoryDocument) {
    this.repositoryDocument = repositoryDocument;
    return this;
  }

  /**
   * Get repositoryDocument
   * @return repositoryDocument
   */
  @javax.annotation.Nullable
  public Object getRepositoryDocument() {
    return repositoryDocument;
  }

  public void setRepositoryDocument(Object repositoryDocument) {
    this.repositoryDocument = repositoryDocument;
  }


  public Article similarities(List<Similar> similarities) {
    this.similarities = similarities;
    return this;
  }

  public Article addSimilaritiesItem(Similar similaritiesItem) {
    if (this.similarities == null) {
      this.similarities = new ArrayList<>();
    }
    this.similarities.add(similaritiesItem);
    return this;
  }

  /**
   * Similar articles
   * @return similarities
   */
  @javax.annotation.Nullable
  public List<Similar> getSimilarities() {
    return similarities;
  }

  public void setSimilarities(List<Similar> similarities) {
    this.similarities = similarities;
  }


  public Article subjects(List<String> subjects) {
    this.subjects = subjects;
    return this;
  }

  public Article addSubjectsItem(String subjectsItem) {
    if (this.subjects == null) {
      this.subjects = new ArrayList<>();
    }
    this.subjects.add(subjectsItem);
    return this;
  }

  /**
   * Article subjects
   * @return subjects
   */
  @javax.annotation.Nullable
  public List<String> getSubjects() {
    return subjects;
  }

  public void setSubjects(List<String> subjects) {
    this.subjects = subjects;
  }


  public Article title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Article title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }


  public Article topics(List<String> topics) {
    this.topics = topics;
    return this;
  }

  public Article addTopicsItem(String topicsItem) {
    if (this.topics == null) {
      this.topics = new ArrayList<>();
    }
    this.topics.add(topicsItem);
    return this;
  }

  /**
   * Article topics
   * @return topics
   */
  @javax.annotation.Nullable
  public List<String> getTopics() {
    return topics;
  }

  public void setTopics(List<String> topics) {
    this.topics = topics;
  }


  public Article types(List<String> types) {
    this.types = types;
    return this;
  }

  public Article addTypesItem(String typesItem) {
    if (this.types == null) {
      this.types = new ArrayList<>();
    }
    this.types.add(typesItem);
    return this;
  }

  /**
   * Types, e.g. conference paper, journal paper, etc.
   * @return types
   */
  @javax.annotation.Nullable
  public List<String> getTypes() {
    return types;
  }

  public void setTypes(List<String> types) {
    this.types = types;
  }


  public Article year(Integer year) {
    this.year = year;
    return this;
  }

  /**
   * Year the article was published
   * @return year
   */
  @javax.annotation.Nullable
  public Integer getYear() {
    return year;
  }

  public void setYear(Integer year) {
    this.year = year;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Article article = (Article) o;
    return Objects.equals(this.authors, article.authors) &&
        Objects.equals(this.citations, article.citations) &&
        Objects.equals(this.contributors, article.contributors) &&
        Objects.equals(this.datePublished, article.datePublished) &&
        Objects.equals(this.description, article.description) &&
        Objects.equals(this.doi, article.doi) &&
        Objects.equals(this.downloadUrl, article.downloadUrl) &&
        Objects.equals(this.fulltext, article.fulltext) &&
        Objects.equals(this.fulltextIdentifier, article.fulltextIdentifier) &&
        Objects.equals(this.fulltextUrls, article.fulltextUrls) &&
        Objects.equals(this.id, article.id) &&
        Objects.equals(this.identifiers, article.identifiers) &&
        Objects.equals(this.journals, article.journals) &&
        Objects.equals(this.language, article.language) &&
        Objects.equals(this.oai, article.oai) &&
        Objects.equals(this.publisher, article.publisher) &&
        Objects.equals(this.rawRecordXml, article.rawRecordXml) &&
        Objects.equals(this.relations, article.relations) &&
        Objects.equals(this.repositories, article.repositories) &&
        Objects.equals(this.repositoryDocument, article.repositoryDocument) &&
        Objects.equals(this.similarities, article.similarities) &&
        Objects.equals(this.subjects, article.subjects) &&
        Objects.equals(this.title, article.title) &&
        Objects.equals(this.topics, article.topics) &&
        Objects.equals(this.types, article.types) &&
        Objects.equals(this.year, article.year);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authors, citations, contributors, datePublished, description, doi, downloadUrl, fulltext, fulltextIdentifier, fulltextUrls, id, identifiers, journals, language, oai, publisher, rawRecordXml, relations, repositories, repositoryDocument, similarities, subjects, title, topics, types, year);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Article {\n");
    sb.append("    authors: ").append(toIndentedString(authors)).append("\n");
    sb.append("    citations: ").append(toIndentedString(citations)).append("\n");
    sb.append("    contributors: ").append(toIndentedString(contributors)).append("\n");
    sb.append("    datePublished: ").append(toIndentedString(datePublished)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    doi: ").append(toIndentedString(doi)).append("\n");
    sb.append("    downloadUrl: ").append(toIndentedString(downloadUrl)).append("\n");
    sb.append("    fulltext: ").append(toIndentedString(fulltext)).append("\n");
    sb.append("    fulltextIdentifier: ").append(toIndentedString(fulltextIdentifier)).append("\n");
    sb.append("    fulltextUrls: ").append(toIndentedString(fulltextUrls)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    identifiers: ").append(toIndentedString(identifiers)).append("\n");
    sb.append("    journals: ").append(toIndentedString(journals)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    oai: ").append(toIndentedString(oai)).append("\n");
    sb.append("    publisher: ").append(toIndentedString(publisher)).append("\n");
    sb.append("    rawRecordXml: ").append(toIndentedString(rawRecordXml)).append("\n");
    sb.append("    relations: ").append(toIndentedString(relations)).append("\n");
    sb.append("    repositories: ").append(toIndentedString(repositories)).append("\n");
    sb.append("    repositoryDocument: ").append(toIndentedString(repositoryDocument)).append("\n");
    sb.append("    similarities: ").append(toIndentedString(similarities)).append("\n");
    sb.append("    subjects: ").append(toIndentedString(subjects)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
    sb.append("    topics: ").append(toIndentedString(topics)).append("\n");
    sb.append("    types: ").append(toIndentedString(types)).append("\n");
    sb.append("    year: ").append(toIndentedString(year)).append("\n");
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
    openapiFields.add("authors");
    openapiFields.add("citations");
    openapiFields.add("contributors");
    openapiFields.add("datePublished");
    openapiFields.add("description");
    openapiFields.add("doi");
    openapiFields.add("downloadUrl");
    openapiFields.add("fulltext");
    openapiFields.add("fulltextIdentifier");
    openapiFields.add("fulltextUrls");
    openapiFields.add("id");
    openapiFields.add("identifiers");
    openapiFields.add("journals");
    openapiFields.add("language");
    openapiFields.add("oai");
    openapiFields.add("publisher");
    openapiFields.add("rawRecordXml");
    openapiFields.add("relations");
    openapiFields.add("repositories");
    openapiFields.add("repositoryDocument");
    openapiFields.add("similarities");
    openapiFields.add("subjects");
    openapiFields.add("title");
    openapiFields.add("topics");
    openapiFields.add("types");
    openapiFields.add("year");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Article
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Article.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Article is not found in the empty JSON string", Article.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Article.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Article` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Article.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("authors") != null && !jsonObj.get("authors").isJsonNull() && !jsonObj.get("authors").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `authors` to be an array in the JSON string but got `%s`", jsonObj.get("authors").toString()));
      }
      if (jsonObj.get("citations") != null && !jsonObj.get("citations").isJsonNull()) {
        JsonArray jsonArraycitations = jsonObj.getAsJsonArray("citations");
        if (jsonArraycitations != null) {
          // ensure the json data is an array
          if (!jsonObj.get("citations").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `citations` to be an array in the JSON string but got `%s`", jsonObj.get("citations").toString()));
          }

          // validate the optional field `citations` (array)
          for (int i = 0; i < jsonArraycitations.size(); i++) {
            Citation.validateJsonElement(jsonArraycitations.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("contributors") != null && !jsonObj.get("contributors").isJsonNull() && !jsonObj.get("contributors").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `contributors` to be an array in the JSON string but got `%s`", jsonObj.get("contributors").toString()));
      }
      if ((jsonObj.get("datePublished") != null && !jsonObj.get("datePublished").isJsonNull()) && !jsonObj.get("datePublished").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `datePublished` to be a primitive type in the JSON string but got `%s`", jsonObj.get("datePublished").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("doi") != null && !jsonObj.get("doi").isJsonNull()) && !jsonObj.get("doi").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `doi` to be a primitive type in the JSON string but got `%s`", jsonObj.get("doi").toString()));
      }
      if ((jsonObj.get("downloadUrl") != null && !jsonObj.get("downloadUrl").isJsonNull()) && !jsonObj.get("downloadUrl").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `downloadUrl` to be a primitive type in the JSON string but got `%s`", jsonObj.get("downloadUrl").toString()));
      }
      if ((jsonObj.get("fulltext") != null && !jsonObj.get("fulltext").isJsonNull()) && !jsonObj.get("fulltext").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fulltext` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fulltext").toString()));
      }
      if ((jsonObj.get("fulltextIdentifier") != null && !jsonObj.get("fulltextIdentifier").isJsonNull()) && !jsonObj.get("fulltextIdentifier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `fulltextIdentifier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("fulltextIdentifier").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("fulltextUrls") != null && !jsonObj.get("fulltextUrls").isJsonNull() && !jsonObj.get("fulltextUrls").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `fulltextUrls` to be an array in the JSON string but got `%s`", jsonObj.get("fulltextUrls").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("identifiers") != null && !jsonObj.get("identifiers").isJsonNull() && !jsonObj.get("identifiers").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `identifiers` to be an array in the JSON string but got `%s`", jsonObj.get("identifiers").toString()));
      }
      if (jsonObj.get("journals") != null && !jsonObj.get("journals").isJsonNull()) {
        JsonArray jsonArrayjournals = jsonObj.getAsJsonArray("journals");
        if (jsonArrayjournals != null) {
          // ensure the json data is an array
          if (!jsonObj.get("journals").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `journals` to be an array in the JSON string but got `%s`", jsonObj.get("journals").toString()));
          }

          // validate the optional field `journals` (array)
          for (int i = 0; i < jsonArrayjournals.size(); i++) {
            ArticleJournal.validateJsonElement(jsonArrayjournals.get(i));
          };
        }
      }
      // validate the optional field `language`
      if (jsonObj.get("language") != null && !jsonObj.get("language").isJsonNull()) {
        Language.validateJsonElement(jsonObj.get("language"));
      }
      if ((jsonObj.get("oai") != null && !jsonObj.get("oai").isJsonNull()) && !jsonObj.get("oai").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `oai` to be a primitive type in the JSON string but got `%s`", jsonObj.get("oai").toString()));
      }
      if ((jsonObj.get("publisher") != null && !jsonObj.get("publisher").isJsonNull()) && !jsonObj.get("publisher").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `publisher` to be a primitive type in the JSON string but got `%s`", jsonObj.get("publisher").toString()));
      }
      // validate the optional field `rawRecordXml`
      if (jsonObj.get("rawRecordXml") != null && !jsonObj.get("rawRecordXml").isJsonNull()) {
        RawRecordXml.validateJsonElement(jsonObj.get("rawRecordXml"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("relations") != null && !jsonObj.get("relations").isJsonNull() && !jsonObj.get("relations").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `relations` to be an array in the JSON string but got `%s`", jsonObj.get("relations").toString()));
      }
      if (jsonObj.get("repositories") != null && !jsonObj.get("repositories").isJsonNull()) {
        JsonArray jsonArrayrepositories = jsonObj.getAsJsonArray("repositories");
        if (jsonArrayrepositories != null) {
          // ensure the json data is an array
          if (!jsonObj.get("repositories").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `repositories` to be an array in the JSON string but got `%s`", jsonObj.get("repositories").toString()));
          }

          // validate the optional field `repositories` (array)
          for (int i = 0; i < jsonArrayrepositories.size(); i++) {
            Repository.validateJsonElement(jsonArrayrepositories.get(i));
          };
        }
      }
      if (jsonObj.get("similarities") != null && !jsonObj.get("similarities").isJsonNull()) {
        JsonArray jsonArraysimilarities = jsonObj.getAsJsonArray("similarities");
        if (jsonArraysimilarities != null) {
          // ensure the json data is an array
          if (!jsonObj.get("similarities").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `similarities` to be an array in the JSON string but got `%s`", jsonObj.get("similarities").toString()));
          }

          // validate the optional field `similarities` (array)
          for (int i = 0; i < jsonArraysimilarities.size(); i++) {
            Similar.validateJsonElement(jsonArraysimilarities.get(i));
          };
        }
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("subjects") != null && !jsonObj.get("subjects").isJsonNull() && !jsonObj.get("subjects").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `subjects` to be an array in the JSON string but got `%s`", jsonObj.get("subjects").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("topics") != null && !jsonObj.get("topics").isJsonNull() && !jsonObj.get("topics").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `topics` to be an array in the JSON string but got `%s`", jsonObj.get("topics").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("types") != null && !jsonObj.get("types").isJsonNull() && !jsonObj.get("types").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `types` to be an array in the JSON string but got `%s`", jsonObj.get("types").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Article.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Article' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Article> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Article.class));

       return (TypeAdapter<T>) new TypeAdapter<Article>() {
           @Override
           public void write(JsonWriter out, Article value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Article read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Article given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Article
   * @throws IOException if the JSON string is invalid with respect to Article
   */
  public static Article fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Article.class);
  }

  /**
   * Convert an instance of Article to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

