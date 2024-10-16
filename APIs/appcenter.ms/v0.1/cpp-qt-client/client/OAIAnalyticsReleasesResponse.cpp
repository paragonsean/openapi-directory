/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAnalyticsReleasesResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAnalyticsReleasesResponse::OAIAnalyticsReleasesResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAnalyticsReleasesResponse::OAIAnalyticsReleasesResponse() {
    this->initializeModel();
}

OAIAnalyticsReleasesResponse::~OAIAnalyticsReleasesResponse() {}

void OAIAnalyticsReleasesResponse::initializeModel() {

    m_releases_isSet = false;
    m_releases_isValid = false;
}

void OAIAnalyticsReleasesResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAnalyticsReleasesResponse::fromJsonObject(QJsonObject json) {

    m_releases_isValid = ::OpenAPI::fromJsonValue(m_releases, json[QString("releases")]);
    m_releases_isSet = !json[QString("releases")].isNull() && m_releases_isValid;
}

QString OAIAnalyticsReleasesResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAnalyticsReleasesResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_releases.size() > 0) {
        obj.insert(QString("releases"), ::OpenAPI::toJsonValue(m_releases));
    }
    return obj;
}

QList<OAIDistibutionReleases_installAnalytics_request_releases_inner> OAIAnalyticsReleasesResponse::getReleases() const {
    return m_releases;
}
void OAIAnalyticsReleasesResponse::setReleases(const QList<OAIDistibutionReleases_installAnalytics_request_releases_inner> &releases) {
    m_releases = releases;
    m_releases_isSet = true;
}

bool OAIAnalyticsReleasesResponse::is_releases_Set() const{
    return m_releases_isSet;
}

bool OAIAnalyticsReleasesResponse::is_releases_Valid() const{
    return m_releases_isValid;
}

bool OAIAnalyticsReleasesResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_releases.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAnalyticsReleasesResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
