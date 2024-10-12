/**
 * Facial Recognition Reverse Image Face Search API
 * Let your users search the Internet by face! Integrate FaceCheck facial search seamlessly with your app, website or software platform.   FaceCheck's REST API is hassle-free and easy to use. For code examples visit <a href='https://facecheck.id/Face-Search/API'>https://facecheck.id/Face-Search/API</a>
 *
 * The version of the OpenAPI document: v1.02
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIInfoResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInfoResponse::OAIInfoResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInfoResponse::OAIInfoResponse() {
    this->initializeModel();
}

OAIInfoResponse::~OAIInfoResponse() {}

void OAIInfoResponse::initializeModel() {

    m_faces_isSet = false;
    m_faces_isValid = false;

    m_has_credits_to_search_isSet = false;
    m_has_credits_to_search_isValid = false;

    m_is_online_isSet = false;
    m_is_online_isValid = false;

    m_remaining_credits_isSet = false;
    m_remaining_credits_isValid = false;
}

void OAIInfoResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInfoResponse::fromJsonObject(QJsonObject json) {

    m_faces_isValid = ::OpenAPI::fromJsonValue(m_faces, json[QString("faces")]);
    m_faces_isSet = !json[QString("faces")].isNull() && m_faces_isValid;

    m_has_credits_to_search_isValid = ::OpenAPI::fromJsonValue(m_has_credits_to_search, json[QString("has_credits_to_search")]);
    m_has_credits_to_search_isSet = !json[QString("has_credits_to_search")].isNull() && m_has_credits_to_search_isValid;

    m_is_online_isValid = ::OpenAPI::fromJsonValue(m_is_online, json[QString("is_online")]);
    m_is_online_isSet = !json[QString("is_online")].isNull() && m_is_online_isValid;

    m_remaining_credits_isValid = ::OpenAPI::fromJsonValue(m_remaining_credits, json[QString("remaining_credits")]);
    m_remaining_credits_isSet = !json[QString("remaining_credits")].isNull() && m_remaining_credits_isValid;
}

QString OAIInfoResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInfoResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_faces_isSet) {
        obj.insert(QString("faces"), ::OpenAPI::toJsonValue(m_faces));
    }
    if (m_has_credits_to_search_isSet) {
        obj.insert(QString("has_credits_to_search"), ::OpenAPI::toJsonValue(m_has_credits_to_search));
    }
    if (m_is_online_isSet) {
        obj.insert(QString("is_online"), ::OpenAPI::toJsonValue(m_is_online));
    }
    if (m_remaining_credits_isSet) {
        obj.insert(QString("remaining_credits"), ::OpenAPI::toJsonValue(m_remaining_credits));
    }
    return obj;
}

qint32 OAIInfoResponse::getFaces() const {
    return m_faces;
}
void OAIInfoResponse::setFaces(const qint32 &faces) {
    m_faces = faces;
    m_faces_isSet = true;
}

bool OAIInfoResponse::is_faces_Set() const{
    return m_faces_isSet;
}

bool OAIInfoResponse::is_faces_Valid() const{
    return m_faces_isValid;
}

bool OAIInfoResponse::isHasCreditsToSearch() const {
    return m_has_credits_to_search;
}
void OAIInfoResponse::setHasCreditsToSearch(const bool &has_credits_to_search) {
    m_has_credits_to_search = has_credits_to_search;
    m_has_credits_to_search_isSet = true;
}

bool OAIInfoResponse::is_has_credits_to_search_Set() const{
    return m_has_credits_to_search_isSet;
}

bool OAIInfoResponse::is_has_credits_to_search_Valid() const{
    return m_has_credits_to_search_isValid;
}

bool OAIInfoResponse::isIsOnline() const {
    return m_is_online;
}
void OAIInfoResponse::setIsOnline(const bool &is_online) {
    m_is_online = is_online;
    m_is_online_isSet = true;
}

bool OAIInfoResponse::is_is_online_Set() const{
    return m_is_online_isSet;
}

bool OAIInfoResponse::is_is_online_Valid() const{
    return m_is_online_isValid;
}

qint32 OAIInfoResponse::getRemainingCredits() const {
    return m_remaining_credits;
}
void OAIInfoResponse::setRemainingCredits(const qint32 &remaining_credits) {
    m_remaining_credits = remaining_credits;
    m_remaining_credits_isSet = true;
}

bool OAIInfoResponse::is_remaining_credits_Set() const{
    return m_remaining_credits_isSet;
}

bool OAIInfoResponse::is_remaining_credits_Valid() const{
    return m_remaining_credits_isValid;
}

bool OAIInfoResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_faces_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_credits_to_search_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_online_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remaining_credits_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInfoResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
