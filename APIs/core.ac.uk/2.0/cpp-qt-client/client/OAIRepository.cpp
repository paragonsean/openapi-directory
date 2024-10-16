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

#include "OAIRepository.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRepository::OAIRepository(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRepository::OAIRepository() {
    this->initializeModel();
}

OAIRepository::~OAIRepository() {}

void OAIRepository::initializeModel() {

    m_data_provider_source_stats_isSet = false;
    m_data_provider_source_stats_isValid = false;

    m_history_isSet = false;
    m_history_isValid = false;

    m_history_cumulative_isSet = false;
    m_history_cumulative_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_seen_isSet = false;
    m_last_seen_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_open_doar_id_isSet = false;
    m_open_doar_id_isValid = false;

    m_repository_location_isSet = false;
    m_repository_location_isValid = false;

    m_repository_stats_isSet = false;
    m_repository_stats_isValid = false;

    m_uri_isSet = false;
    m_uri_isValid = false;

    m_url_homepage_isSet = false;
    m_url_homepage_isValid = false;

    m_url_oaipmh_isSet = false;
    m_url_oaipmh_isValid = false;
}

void OAIRepository::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRepository::fromJsonObject(QJsonObject json) {

    m_data_provider_source_stats_isValid = ::OpenAPI::fromJsonValue(m_data_provider_source_stats, json[QString("dataProviderSourceStats")]);
    m_data_provider_source_stats_isSet = !json[QString("dataProviderSourceStats")].isNull() && m_data_provider_source_stats_isValid;

    m_history_isValid = ::OpenAPI::fromJsonValue(m_history, json[QString("history")]);
    m_history_isSet = !json[QString("history")].isNull() && m_history_isValid;

    m_history_cumulative_isValid = ::OpenAPI::fromJsonValue(m_history_cumulative, json[QString("historyCumulative")]);
    m_history_cumulative_isSet = !json[QString("historyCumulative")].isNull() && m_history_cumulative_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_seen_isValid = ::OpenAPI::fromJsonValue(m_last_seen, json[QString("lastSeen")]);
    m_last_seen_isSet = !json[QString("lastSeen")].isNull() && m_last_seen_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_open_doar_id_isValid = ::OpenAPI::fromJsonValue(m_open_doar_id, json[QString("openDoarId")]);
    m_open_doar_id_isSet = !json[QString("openDoarId")].isNull() && m_open_doar_id_isValid;

    m_repository_location_isValid = ::OpenAPI::fromJsonValue(m_repository_location, json[QString("repositoryLocation")]);
    m_repository_location_isSet = !json[QString("repositoryLocation")].isNull() && m_repository_location_isValid;

    m_repository_stats_isValid = ::OpenAPI::fromJsonValue(m_repository_stats, json[QString("repositoryStats")]);
    m_repository_stats_isSet = !json[QString("repositoryStats")].isNull() && m_repository_stats_isValid;

    m_uri_isValid = ::OpenAPI::fromJsonValue(m_uri, json[QString("uri")]);
    m_uri_isSet = !json[QString("uri")].isNull() && m_uri_isValid;

    m_url_homepage_isValid = ::OpenAPI::fromJsonValue(m_url_homepage, json[QString("urlHomepage")]);
    m_url_homepage_isSet = !json[QString("urlHomepage")].isNull() && m_url_homepage_isValid;

    m_url_oaipmh_isValid = ::OpenAPI::fromJsonValue(m_url_oaipmh, json[QString("urlOaipmh")]);
    m_url_oaipmh_isSet = !json[QString("urlOaipmh")].isNull() && m_url_oaipmh_isValid;
}

QString OAIRepository::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRepository::asJsonObject() const {
    QJsonObject obj;
    if (m_data_provider_source_stats.size() > 0) {
        obj.insert(QString("dataProviderSourceStats"), ::OpenAPI::toJsonValue(m_data_provider_source_stats));
    }
    if (m_history.size() > 0) {
        obj.insert(QString("history"), ::OpenAPI::toJsonValue(m_history));
    }
    if (m_history_cumulative.size() > 0) {
        obj.insert(QString("historyCumulative"), ::OpenAPI::toJsonValue(m_history_cumulative));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_seen_isSet) {
        obj.insert(QString("lastSeen"), ::OpenAPI::toJsonValue(m_last_seen));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_open_doar_id_isSet) {
        obj.insert(QString("openDoarId"), ::OpenAPI::toJsonValue(m_open_doar_id));
    }
    if (m_repository_location.isSet()) {
        obj.insert(QString("repositoryLocation"), ::OpenAPI::toJsonValue(m_repository_location));
    }
    if (m_repository_stats.isSet()) {
        obj.insert(QString("repositoryStats"), ::OpenAPI::toJsonValue(m_repository_stats));
    }
    if (m_uri_isSet) {
        obj.insert(QString("uri"), ::OpenAPI::toJsonValue(m_uri));
    }
    if (m_url_homepage_isSet) {
        obj.insert(QString("urlHomepage"), ::OpenAPI::toJsonValue(m_url_homepage));
    }
    if (m_url_oaipmh_isSet) {
        obj.insert(QString("urlOaipmh"), ::OpenAPI::toJsonValue(m_url_oaipmh));
    }
    return obj;
}

QList<OAIObject> OAIRepository::getDataProviderSourceStats() const {
    return m_data_provider_source_stats;
}
void OAIRepository::setDataProviderSourceStats(const QList<OAIObject> &data_provider_source_stats) {
    m_data_provider_source_stats = data_provider_source_stats;
    m_data_provider_source_stats_isSet = true;
}

bool OAIRepository::is_data_provider_source_stats_Set() const{
    return m_data_provider_source_stats_isSet;
}

bool OAIRepository::is_data_provider_source_stats_Valid() const{
    return m_data_provider_source_stats_isValid;
}

QList<OAIObject> OAIRepository::getHistory() const {
    return m_history;
}
void OAIRepository::setHistory(const QList<OAIObject> &history) {
    m_history = history;
    m_history_isSet = true;
}

bool OAIRepository::is_history_Set() const{
    return m_history_isSet;
}

bool OAIRepository::is_history_Valid() const{
    return m_history_isValid;
}

QList<OAIObject> OAIRepository::getHistoryCumulative() const {
    return m_history_cumulative;
}
void OAIRepository::setHistoryCumulative(const QList<OAIObject> &history_cumulative) {
    m_history_cumulative = history_cumulative;
    m_history_cumulative_isSet = true;
}

bool OAIRepository::is_history_cumulative_Set() const{
    return m_history_cumulative_isSet;
}

bool OAIRepository::is_history_cumulative_Valid() const{
    return m_history_cumulative_isValid;
}

qint32 OAIRepository::getId() const {
    return m_id;
}
void OAIRepository::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRepository::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRepository::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIRepository::getLastSeen() const {
    return m_last_seen;
}
void OAIRepository::setLastSeen(const QDateTime &last_seen) {
    m_last_seen = last_seen;
    m_last_seen_isSet = true;
}

bool OAIRepository::is_last_seen_Set() const{
    return m_last_seen_isSet;
}

bool OAIRepository::is_last_seen_Valid() const{
    return m_last_seen_isValid;
}

QString OAIRepository::getName() const {
    return m_name;
}
void OAIRepository::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIRepository::is_name_Set() const{
    return m_name_isSet;
}

bool OAIRepository::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIRepository::getOpenDoarId() const {
    return m_open_doar_id;
}
void OAIRepository::setOpenDoarId(const qint32 &open_doar_id) {
    m_open_doar_id = open_doar_id;
    m_open_doar_id_isSet = true;
}

bool OAIRepository::is_open_doar_id_Set() const{
    return m_open_doar_id_isSet;
}

bool OAIRepository::is_open_doar_id_Valid() const{
    return m_open_doar_id_isValid;
}

OAIRepositoryLocation OAIRepository::getRepositoryLocation() const {
    return m_repository_location;
}
void OAIRepository::setRepositoryLocation(const OAIRepositoryLocation &repository_location) {
    m_repository_location = repository_location;
    m_repository_location_isSet = true;
}

bool OAIRepository::is_repository_location_Set() const{
    return m_repository_location_isSet;
}

bool OAIRepository::is_repository_location_Valid() const{
    return m_repository_location_isValid;
}

OAIRepositoryStats OAIRepository::getRepositoryStats() const {
    return m_repository_stats;
}
void OAIRepository::setRepositoryStats(const OAIRepositoryStats &repository_stats) {
    m_repository_stats = repository_stats;
    m_repository_stats_isSet = true;
}

bool OAIRepository::is_repository_stats_Set() const{
    return m_repository_stats_isSet;
}

bool OAIRepository::is_repository_stats_Valid() const{
    return m_repository_stats_isValid;
}

QString OAIRepository::getUri() const {
    return m_uri;
}
void OAIRepository::setUri(const QString &uri) {
    m_uri = uri;
    m_uri_isSet = true;
}

bool OAIRepository::is_uri_Set() const{
    return m_uri_isSet;
}

bool OAIRepository::is_uri_Valid() const{
    return m_uri_isValid;
}

QString OAIRepository::getUrlHomepage() const {
    return m_url_homepage;
}
void OAIRepository::setUrlHomepage(const QString &url_homepage) {
    m_url_homepage = url_homepage;
    m_url_homepage_isSet = true;
}

bool OAIRepository::is_url_homepage_Set() const{
    return m_url_homepage_isSet;
}

bool OAIRepository::is_url_homepage_Valid() const{
    return m_url_homepage_isValid;
}

QString OAIRepository::getUrlOaipmh() const {
    return m_url_oaipmh;
}
void OAIRepository::setUrlOaipmh(const QString &url_oaipmh) {
    m_url_oaipmh = url_oaipmh;
    m_url_oaipmh_isSet = true;
}

bool OAIRepository::is_url_oaipmh_Set() const{
    return m_url_oaipmh_isSet;
}

bool OAIRepository::is_url_oaipmh_Valid() const{
    return m_url_oaipmh_isValid;
}

bool OAIRepository::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_provider_source_stats.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_history.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_history_cumulative.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_seen_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_open_doar_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_repository_location.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_repository_stats.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_homepage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_oaipmh_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRepository::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
