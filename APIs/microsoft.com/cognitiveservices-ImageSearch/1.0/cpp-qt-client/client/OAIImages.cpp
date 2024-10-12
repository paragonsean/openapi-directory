/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImages.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImages::OAIImages(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImages::OAIImages() {
    this->initializeModel();
}

OAIImages::~OAIImages() {}

void OAIImages::initializeModel() {

    m_next_offset_isSet = false;
    m_next_offset_isValid = false;

    m_pivot_suggestions_isSet = false;
    m_pivot_suggestions_isValid = false;

    m_query_expansions_isSet = false;
    m_query_expansions_isValid = false;

    m_similar_terms_isSet = false;
    m_similar_terms_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;

    m_total_estimated_matches_isSet = false;
    m_total_estimated_matches_isValid = false;

    m_read_link_isSet = false;
    m_read_link_isValid = false;

    m_web_search_url_isSet = false;
    m_web_search_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m__type_isSet = false;
    m__type_isValid = false;
}

void OAIImages::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImages::fromJsonObject(QJsonObject json) {

    m_next_offset_isValid = ::OpenAPI::fromJsonValue(m_next_offset, json[QString("nextOffset")]);
    m_next_offset_isSet = !json[QString("nextOffset")].isNull() && m_next_offset_isValid;

    m_pivot_suggestions_isValid = ::OpenAPI::fromJsonValue(m_pivot_suggestions, json[QString("pivotSuggestions")]);
    m_pivot_suggestions_isSet = !json[QString("pivotSuggestions")].isNull() && m_pivot_suggestions_isValid;

    m_query_expansions_isValid = ::OpenAPI::fromJsonValue(m_query_expansions, json[QString("queryExpansions")]);
    m_query_expansions_isSet = !json[QString("queryExpansions")].isNull() && m_query_expansions_isValid;

    m_similar_terms_isValid = ::OpenAPI::fromJsonValue(m_similar_terms, json[QString("similarTerms")]);
    m_similar_terms_isSet = !json[QString("similarTerms")].isNull() && m_similar_terms_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_total_estimated_matches_isValid = ::OpenAPI::fromJsonValue(m_total_estimated_matches, json[QString("totalEstimatedMatches")]);
    m_total_estimated_matches_isSet = !json[QString("totalEstimatedMatches")].isNull() && m_total_estimated_matches_isValid;

    m_read_link_isValid = ::OpenAPI::fromJsonValue(m_read_link, json[QString("readLink")]);
    m_read_link_isSet = !json[QString("readLink")].isNull() && m_read_link_isValid;

    m_web_search_url_isValid = ::OpenAPI::fromJsonValue(m_web_search_url, json[QString("webSearchUrl")]);
    m_web_search_url_isSet = !json[QString("webSearchUrl")].isNull() && m_web_search_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m__type_isValid = ::OpenAPI::fromJsonValue(m__type, json[QString("_type")]);
    m__type_isSet = !json[QString("_type")].isNull() && m__type_isValid;
}

QString OAIImages::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImages::asJsonObject() const {
    QJsonObject obj;
    if (m_next_offset_isSet) {
        obj.insert(QString("nextOffset"), ::OpenAPI::toJsonValue(m_next_offset));
    }
    if (m_pivot_suggestions.size() > 0) {
        obj.insert(QString("pivotSuggestions"), ::OpenAPI::toJsonValue(m_pivot_suggestions));
    }
    if (m_query_expansions.size() > 0) {
        obj.insert(QString("queryExpansions"), ::OpenAPI::toJsonValue(m_query_expansions));
    }
    if (m_similar_terms.size() > 0) {
        obj.insert(QString("similarTerms"), ::OpenAPI::toJsonValue(m_similar_terms));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_total_estimated_matches_isSet) {
        obj.insert(QString("totalEstimatedMatches"), ::OpenAPI::toJsonValue(m_total_estimated_matches));
    }
    if (m_read_link_isSet) {
        obj.insert(QString("readLink"), ::OpenAPI::toJsonValue(m_read_link));
    }
    if (m_web_search_url_isSet) {
        obj.insert(QString("webSearchUrl"), ::OpenAPI::toJsonValue(m_web_search_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m__type_isSet) {
        obj.insert(QString("_type"), ::OpenAPI::toJsonValue(m__type));
    }
    return obj;
}

qint32 OAIImages::getNextOffset() const {
    return m_next_offset;
}
void OAIImages::setNextOffset(const qint32 &next_offset) {
    m_next_offset = next_offset;
    m_next_offset_isSet = true;
}

bool OAIImages::is_next_offset_Set() const{
    return m_next_offset_isSet;
}

bool OAIImages::is_next_offset_Valid() const{
    return m_next_offset_isValid;
}

QList<OAIPivotSuggestions> OAIImages::getPivotSuggestions() const {
    return m_pivot_suggestions;
}
void OAIImages::setPivotSuggestions(const QList<OAIPivotSuggestions> &pivot_suggestions) {
    m_pivot_suggestions = pivot_suggestions;
    m_pivot_suggestions_isSet = true;
}

bool OAIImages::is_pivot_suggestions_Set() const{
    return m_pivot_suggestions_isSet;
}

bool OAIImages::is_pivot_suggestions_Valid() const{
    return m_pivot_suggestions_isValid;
}

QList<OAIQuery> OAIImages::getQueryExpansions() const {
    return m_query_expansions;
}
void OAIImages::setQueryExpansions(const QList<OAIQuery> &query_expansions) {
    m_query_expansions = query_expansions;
    m_query_expansions_isSet = true;
}

bool OAIImages::is_query_expansions_Set() const{
    return m_query_expansions_isSet;
}

bool OAIImages::is_query_expansions_Valid() const{
    return m_query_expansions_isValid;
}

QList<OAIQuery> OAIImages::getSimilarTerms() const {
    return m_similar_terms;
}
void OAIImages::setSimilarTerms(const QList<OAIQuery> &similar_terms) {
    m_similar_terms = similar_terms;
    m_similar_terms_isSet = true;
}

bool OAIImages::is_similar_terms_Set() const{
    return m_similar_terms_isSet;
}

bool OAIImages::is_similar_terms_Valid() const{
    return m_similar_terms_isValid;
}

QList<OAIImageObject> OAIImages::getValue() const {
    return m_value;
}
void OAIImages::setValue(const QList<OAIImageObject> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIImages::is_value_Set() const{
    return m_value_isSet;
}

bool OAIImages::is_value_Valid() const{
    return m_value_isValid;
}

qint64 OAIImages::getTotalEstimatedMatches() const {
    return m_total_estimated_matches;
}
void OAIImages::setTotalEstimatedMatches(const qint64 &total_estimated_matches) {
    m_total_estimated_matches = total_estimated_matches;
    m_total_estimated_matches_isSet = true;
}

bool OAIImages::is_total_estimated_matches_Set() const{
    return m_total_estimated_matches_isSet;
}

bool OAIImages::is_total_estimated_matches_Valid() const{
    return m_total_estimated_matches_isValid;
}

QString OAIImages::getReadLink() const {
    return m_read_link;
}
void OAIImages::setReadLink(const QString &read_link) {
    m_read_link = read_link;
    m_read_link_isSet = true;
}

bool OAIImages::is_read_link_Set() const{
    return m_read_link_isSet;
}

bool OAIImages::is_read_link_Valid() const{
    return m_read_link_isValid;
}

QString OAIImages::getWebSearchUrl() const {
    return m_web_search_url;
}
void OAIImages::setWebSearchUrl(const QString &web_search_url) {
    m_web_search_url = web_search_url;
    m_web_search_url_isSet = true;
}

bool OAIImages::is_web_search_url_Set() const{
    return m_web_search_url_isSet;
}

bool OAIImages::is_web_search_url_Valid() const{
    return m_web_search_url_isValid;
}

QString OAIImages::getId() const {
    return m_id;
}
void OAIImages::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIImages::is_id_Set() const{
    return m_id_isSet;
}

bool OAIImages::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIImages::getType() const {
    return m__type;
}
void OAIImages::setType(const QString &_type) {
    m__type = _type;
    m__type_isSet = true;
}

bool OAIImages::is__type_Set() const{
    return m__type_isSet;
}

bool OAIImages::is__type_Valid() const{
    return m__type_isValid;
}

bool OAIImages::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_offset_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pivot_suggestions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_query_expansions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_similar_terms.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_estimated_matches_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_read_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_web_search_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImages::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && m__type_isValid && true;
}

} // namespace OpenAPI
