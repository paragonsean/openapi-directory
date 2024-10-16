/**
 * Background Removal API
 * Remove the background of any image
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthFailed_errors_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthFailed_errors_inner::OAIAuthFailed_errors_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthFailed_errors_inner::OAIAuthFailed_errors_inner() {
    this->initializeModel();
}

OAIAuthFailed_errors_inner::~OAIAuthFailed_errors_inner() {}

void OAIAuthFailed_errors_inner::initializeModel() {

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIAuthFailed_errors_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthFailed_errors_inner::fromJsonObject(QJsonObject json) {

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIAuthFailed_errors_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthFailed_errors_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAIAuthFailed_errors_inner::getTitle() const {
    return m_title;
}
void OAIAuthFailed_errors_inner::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIAuthFailed_errors_inner::is_title_Set() const{
    return m_title_isSet;
}

bool OAIAuthFailed_errors_inner::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIAuthFailed_errors_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthFailed_errors_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
