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

#include "OAI_improve_post_400_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_improve_post_400_response::OAI_improve_post_400_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_improve_post_400_response::OAI_improve_post_400_response() {
    this->initializeModel();
}

OAI_improve_post_400_response::~OAI_improve_post_400_response() {}

void OAI_improve_post_400_response::initializeModel() {

    m_errors_isSet = false;
    m_errors_isValid = false;
}

void OAI_improve_post_400_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_improve_post_400_response::fromJsonObject(QJsonObject json) {

    m_errors_isValid = ::OpenAPI::fromJsonValue(m_errors, json[QString("errors")]);
    m_errors_isSet = !json[QString("errors")].isNull() && m_errors_isValid;
}

QString OAI_improve_post_400_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_improve_post_400_response::asJsonObject() const {
    QJsonObject obj;
    if (m_errors.size() > 0) {
        obj.insert(QString("errors"), ::OpenAPI::toJsonValue(m_errors));
    }
    return obj;
}

QList<OAI_improve_post_400_response_errors_inner> OAI_improve_post_400_response::getErrors() const {
    return m_errors;
}
void OAI_improve_post_400_response::setErrors(const QList<OAI_improve_post_400_response_errors_inner> &errors) {
    m_errors = errors;
    m_errors_isSet = true;
}

bool OAI_improve_post_400_response::is_errors_Set() const{
    return m_errors_isSet;
}

bool OAI_improve_post_400_response::is_errors_Valid() const{
    return m_errors_isValid;
}

bool OAI_improve_post_400_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_improve_post_400_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
