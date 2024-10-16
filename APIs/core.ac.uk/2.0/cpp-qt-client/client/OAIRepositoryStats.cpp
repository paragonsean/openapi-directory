/**
 * CORE API v2
 * <p style=\"text-align: justify;\">You can use the CORE API to access the      resources harvested and enriched by CORE. If you encounter any problems with the API, please <a href=\"/contact\">report them to us</a>.</p>  <h2>Overview</h2> <p style=\"text-align: justify;\">The API is organised by resource type. The resources are <b>articles</b>,      <b>journals</b> and <b>repositories</b> and are represented using JSON data format. Furthermore,      each resource has a list of methods. The API also provides two global methods for accessing all resources at once.</p>  <h2>Response format</h2> <p style=\"text-align: justify;\">Response for each query contains two fields: <b>status</b> and <b>data</b>.     In case of an error status, the data field is empty. The data field contains a single object     in case the request is for a specific identifier (e.g. CORE ID, CORE repository ID, etc.), or       contains a list of objects, for example for search queries. In case of batch requests, the response     is an array of objects, each of which contains its own <b>status</b> and <b>data</b> fields.     For search queries the response contains an additional field <b>totalHits</b>, which is the      total number of items which match the search criteria.</p>  <h2>Search query syntax</h2>  <p style=\"text-align: justify\">Complex search queries can be used in all of the API search methods.     The query can be a simple string or it can be built using terms and operators described in Elasticsearch     <a href=\"http://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-query-string-query.html#query-string-syntax\">documentation</a>.     The usable field names are <strong>title</strong>, <strong>description</strong>, <strong>fullText</strong>,      <strong>authors</strong>, <strong>publisher</strong>, <strong>repositories.id</strong>, <strong>repositories.name</strong>,      <strong>doi</strong>, <strong>oai</strong>, <strong>identifiers</strong> (which is a list of article identifiers including OAI, URL, etc.), <strong>language.name</strong>      and <strong>year</strong>. Some example queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>title:psychology and language.name:English</p></li>     <li><p>repositories.id:86 AND year:2014</p></li>     <li><p>identifiers:\"oai:aura.abdn.ac.uk:2164/3837\" OR identifiers:\"oai:aura.abdn.ac.uk:2164/3843\"</p></li>     <li><p>doi:\"10.1186/1471-2458-6-309\"</p></li> </ul>  <h3>Retrieving the latest Articles</h3> <p style=\"text-align: justify\">     You can retrieve the harvested items since specific dates using the following queries: </p>  <ul style=\"margin-left: 30px;\">     <li><p>repositoryDocument.metadataUpdated:>2017-02-10</p></li>     <li><p>repositoryDocument.metadataUpdated:>2017-03-01 AND repositoryDocument.metadataUpdated:<2017-03-31</p></li>     </ul>  <h2>Sort order</h2>  <p style=\"text-align: justify;\">For search queries, the results are ordered by relevance score. For batch      requests, the results are retrieved in the order of the requests.</p>  <h2>Parameters</h2> <p style=\"text-align: justify;\">The API methods allow different parameters to be passed. Additionally, there is an API key parameter which is common to all API methods. For all API methods      the API key can be provided either as a query parameter or in the request header. If the API key      is not provided, the API will return HTTP 401 error. You can register for an API key <a href=\"/services#api\">here</a>.</p>  <h2>API methods</h2>
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRepositoryStats.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRepositoryStats::OAIRepositoryStats(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRepositoryStats::OAIRepositoryStats() {
    this->initializeModel();
}

OAIRepositoryStats::~OAIRepositoryStats() {}

void OAIRepositoryStats::initializeModel() {

    m_count_fulltext_isSet = false;
    m_count_fulltext_isValid = false;

    m_count_metadata_isSet = false;
    m_count_metadata_isValid = false;

    m_date_last_processed_isSet = false;
    m_date_last_processed_isValid = false;
}

void OAIRepositoryStats::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRepositoryStats::fromJsonObject(QJsonObject json) {

    m_count_fulltext_isValid = ::OpenAPI::fromJsonValue(m_count_fulltext, json[QString("countFulltext")]);
    m_count_fulltext_isSet = !json[QString("countFulltext")].isNull() && m_count_fulltext_isValid;

    m_count_metadata_isValid = ::OpenAPI::fromJsonValue(m_count_metadata, json[QString("countMetadata")]);
    m_count_metadata_isSet = !json[QString("countMetadata")].isNull() && m_count_metadata_isValid;

    m_date_last_processed_isValid = ::OpenAPI::fromJsonValue(m_date_last_processed, json[QString("dateLastProcessed")]);
    m_date_last_processed_isSet = !json[QString("dateLastProcessed")].isNull() && m_date_last_processed_isValid;
}

QString OAIRepositoryStats::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRepositoryStats::asJsonObject() const {
    QJsonObject obj;
    if (m_count_fulltext_isSet) {
        obj.insert(QString("countFulltext"), ::OpenAPI::toJsonValue(m_count_fulltext));
    }
    if (m_count_metadata_isSet) {
        obj.insert(QString("countMetadata"), ::OpenAPI::toJsonValue(m_count_metadata));
    }
    if (m_date_last_processed_isSet) {
        obj.insert(QString("dateLastProcessed"), ::OpenAPI::toJsonValue(m_date_last_processed));
    }
    return obj;
}

qint32 OAIRepositoryStats::getCountFulltext() const {
    return m_count_fulltext;
}
void OAIRepositoryStats::setCountFulltext(const qint32 &count_fulltext) {
    m_count_fulltext = count_fulltext;
    m_count_fulltext_isSet = true;
}

bool OAIRepositoryStats::is_count_fulltext_Set() const{
    return m_count_fulltext_isSet;
}

bool OAIRepositoryStats::is_count_fulltext_Valid() const{
    return m_count_fulltext_isValid;
}

qint32 OAIRepositoryStats::getCountMetadata() const {
    return m_count_metadata;
}
void OAIRepositoryStats::setCountMetadata(const qint32 &count_metadata) {
    m_count_metadata = count_metadata;
    m_count_metadata_isSet = true;
}

bool OAIRepositoryStats::is_count_metadata_Set() const{
    return m_count_metadata_isSet;
}

bool OAIRepositoryStats::is_count_metadata_Valid() const{
    return m_count_metadata_isValid;
}

QString OAIRepositoryStats::getDateLastProcessed() const {
    return m_date_last_processed;
}
void OAIRepositoryStats::setDateLastProcessed(const QString &date_last_processed) {
    m_date_last_processed = date_last_processed;
    m_date_last_processed_isSet = true;
}

bool OAIRepositoryStats::is_date_last_processed_Set() const{
    return m_date_last_processed_isSet;
}

bool OAIRepositoryStats::is_date_last_processed_Valid() const{
    return m_date_last_processed_isValid;
}

bool OAIRepositoryStats::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_fulltext_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_count_metadata_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_last_processed_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRepositoryStats::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
