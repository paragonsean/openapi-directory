/**
 * Hubhopper Partner Integration API(s) - Production
 * This is an interactive document explaining the API(s) that could be used to fetch data from [Hubhopper](https://hubhopper.com). Use the api key provided to authorize `x-api-key` and test the API(s). The output data models are also available for reference.
 *
 * The version of the OpenAPI document: v5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISinglePodcast.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISinglePodcast::OAISinglePodcast(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISinglePodcast::OAISinglePodcast() {
    this->initializeModel();
}

OAISinglePodcast::~OAISinglePodcast() {}

void OAISinglePodcast::initializeModel() {

    m_podcast_isSet = false;
    m_podcast_isValid = false;
}

void OAISinglePodcast::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISinglePodcast::fromJsonObject(QJsonObject json) {

    m_podcast_isValid = ::OpenAPI::fromJsonValue(m_podcast, json[QString("podcast")]);
    m_podcast_isSet = !json[QString("podcast")].isNull() && m_podcast_isValid;
}

QString OAISinglePodcast::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISinglePodcast::asJsonObject() const {
    QJsonObject obj;
    if (m_podcast.isSet()) {
        obj.insert(QString("podcast"), ::OpenAPI::toJsonValue(m_podcast));
    }
    return obj;
}

OAISinglePodcastPodcast OAISinglePodcast::getPodcast() const {
    return m_podcast;
}
void OAISinglePodcast::setPodcast(const OAISinglePodcastPodcast &podcast) {
    m_podcast = podcast;
    m_podcast_isSet = true;
}

bool OAISinglePodcast::is_podcast_Set() const{
    return m_podcast_isSet;
}

bool OAISinglePodcast::is_podcast_Valid() const{
    return m_podcast_isValid;
}

bool OAISinglePodcast::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_podcast.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISinglePodcast::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
