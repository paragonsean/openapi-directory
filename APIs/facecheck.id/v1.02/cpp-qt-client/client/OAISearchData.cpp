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

#include "OAISearchData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISearchData::OAISearchData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISearchData::OAISearchData() {
    this->initializeModel();
}

OAISearchData::~OAISearchData() {}

void OAISearchData::initializeModel() {

    m_demo_isSet = false;
    m_demo_isValid = false;

    m_id_captcha_isSet = false;
    m_id_captcha_isValid = false;

    m_id_search_isSet = false;
    m_id_search_isValid = false;

    m_status_only_isSet = false;
    m_status_only_isValid = false;

    m_with_progress_isSet = false;
    m_with_progress_isValid = false;
}

void OAISearchData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISearchData::fromJsonObject(QJsonObject json) {

    m_demo_isValid = ::OpenAPI::fromJsonValue(m_demo, json[QString("demo")]);
    m_demo_isSet = !json[QString("demo")].isNull() && m_demo_isValid;

    m_id_captcha_isValid = ::OpenAPI::fromJsonValue(m_id_captcha, json[QString("id_captcha")]);
    m_id_captcha_isSet = !json[QString("id_captcha")].isNull() && m_id_captcha_isValid;

    m_id_search_isValid = ::OpenAPI::fromJsonValue(m_id_search, json[QString("id_search")]);
    m_id_search_isSet = !json[QString("id_search")].isNull() && m_id_search_isValid;

    m_status_only_isValid = ::OpenAPI::fromJsonValue(m_status_only, json[QString("status_only")]);
    m_status_only_isSet = !json[QString("status_only")].isNull() && m_status_only_isValid;

    m_with_progress_isValid = ::OpenAPI::fromJsonValue(m_with_progress, json[QString("with_progress")]);
    m_with_progress_isSet = !json[QString("with_progress")].isNull() && m_with_progress_isValid;
}

QString OAISearchData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISearchData::asJsonObject() const {
    QJsonObject obj;
    if (m_demo_isSet) {
        obj.insert(QString("demo"), ::OpenAPI::toJsonValue(m_demo));
    }
    if (m_id_captcha_isSet) {
        obj.insert(QString("id_captcha"), ::OpenAPI::toJsonValue(m_id_captcha));
    }
    if (m_id_search_isSet) {
        obj.insert(QString("id_search"), ::OpenAPI::toJsonValue(m_id_search));
    }
    if (m_status_only_isSet) {
        obj.insert(QString("status_only"), ::OpenAPI::toJsonValue(m_status_only));
    }
    if (m_with_progress_isSet) {
        obj.insert(QString("with_progress"), ::OpenAPI::toJsonValue(m_with_progress));
    }
    return obj;
}

bool OAISearchData::isDemo() const {
    return m_demo;
}
void OAISearchData::setDemo(const bool &demo) {
    m_demo = demo;
    m_demo_isSet = true;
}

bool OAISearchData::is_demo_Set() const{
    return m_demo_isSet;
}

bool OAISearchData::is_demo_Valid() const{
    return m_demo_isValid;
}

QString OAISearchData::getIdCaptcha() const {
    return m_id_captcha;
}
void OAISearchData::setIdCaptcha(const QString &id_captcha) {
    m_id_captcha = id_captcha;
    m_id_captcha_isSet = true;
}

bool OAISearchData::is_id_captcha_Set() const{
    return m_id_captcha_isSet;
}

bool OAISearchData::is_id_captcha_Valid() const{
    return m_id_captcha_isValid;
}

QString OAISearchData::getIdSearch() const {
    return m_id_search;
}
void OAISearchData::setIdSearch(const QString &id_search) {
    m_id_search = id_search;
    m_id_search_isSet = true;
}

bool OAISearchData::is_id_search_Set() const{
    return m_id_search_isSet;
}

bool OAISearchData::is_id_search_Valid() const{
    return m_id_search_isValid;
}

bool OAISearchData::isStatusOnly() const {
    return m_status_only;
}
void OAISearchData::setStatusOnly(const bool &status_only) {
    m_status_only = status_only;
    m_status_only_isSet = true;
}

bool OAISearchData::is_status_only_Set() const{
    return m_status_only_isSet;
}

bool OAISearchData::is_status_only_Valid() const{
    return m_status_only_isValid;
}

bool OAISearchData::isWithProgress() const {
    return m_with_progress;
}
void OAISearchData::setWithProgress(const bool &with_progress) {
    m_with_progress = with_progress;
    m_with_progress_isSet = true;
}

bool OAISearchData::is_with_progress_Set() const{
    return m_with_progress_isSet;
}

bool OAISearchData::is_with_progress_Valid() const{
    return m_with_progress_isValid;
}

bool OAISearchData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_demo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_captcha_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_search_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_with_progress_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISearchData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
