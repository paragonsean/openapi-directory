/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetPodcastsInBatchResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetPodcastsInBatchResponse::OAIGetPodcastsInBatchResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetPodcastsInBatchResponse::OAIGetPodcastsInBatchResponse() {
    this->initializeModel();
}

OAIGetPodcastsInBatchResponse::~OAIGetPodcastsInBatchResponse() {}

void OAIGetPodcastsInBatchResponse::initializeModel() {

    m_latest_episodes_isSet = false;
    m_latest_episodes_isValid = false;

    m_podcasts_isSet = false;
    m_podcasts_isValid = false;
}

void OAIGetPodcastsInBatchResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetPodcastsInBatchResponse::fromJsonObject(QJsonObject json) {

    m_latest_episodes_isValid = ::OpenAPI::fromJsonValue(m_latest_episodes, json[QString("latest_episodes")]);
    m_latest_episodes_isSet = !json[QString("latest_episodes")].isNull() && m_latest_episodes_isValid;

    m_podcasts_isValid = ::OpenAPI::fromJsonValue(m_podcasts, json[QString("podcasts")]);
    m_podcasts_isSet = !json[QString("podcasts")].isNull() && m_podcasts_isValid;
}

QString OAIGetPodcastsInBatchResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetPodcastsInBatchResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_latest_episodes.size() > 0) {
        obj.insert(QString("latest_episodes"), ::OpenAPI::toJsonValue(m_latest_episodes));
    }
    if (m_podcasts.size() > 0) {
        obj.insert(QString("podcasts"), ::OpenAPI::toJsonValue(m_podcasts));
    }
    return obj;
}

QList<OAIEpisodeSimple> OAIGetPodcastsInBatchResponse::getLatestEpisodes() const {
    return m_latest_episodes;
}
void OAIGetPodcastsInBatchResponse::setLatestEpisodes(const QList<OAIEpisodeSimple> &latest_episodes) {
    m_latest_episodes = latest_episodes;
    m_latest_episodes_isSet = true;
}

bool OAIGetPodcastsInBatchResponse::is_latest_episodes_Set() const{
    return m_latest_episodes_isSet;
}

bool OAIGetPodcastsInBatchResponse::is_latest_episodes_Valid() const{
    return m_latest_episodes_isValid;
}

QList<OAIPodcastSimple> OAIGetPodcastsInBatchResponse::getPodcasts() const {
    return m_podcasts;
}
void OAIGetPodcastsInBatchResponse::setPodcasts(const QList<OAIPodcastSimple> &podcasts) {
    m_podcasts = podcasts;
    m_podcasts_isSet = true;
}

bool OAIGetPodcastsInBatchResponse::is_podcasts_Set() const{
    return m_podcasts_isSet;
}

bool OAIGetPodcastsInBatchResponse::is_podcasts_Valid() const{
    return m_podcasts_isValid;
}

bool OAIGetPodcastsInBatchResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_latest_episodes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_podcasts.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetPodcastsInBatchResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_podcasts_isValid && true;
}

} // namespace OpenAPI
