/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageCreateSummary.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageCreateSummary::OAIImageCreateSummary(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageCreateSummary::OAIImageCreateSummary() {
    this->initializeModel();
}

OAIImageCreateSummary::~OAIImageCreateSummary() {}

void OAIImageCreateSummary::initializeModel() {

    m_images_isSet = false;
    m_images_isValid = false;

    m_is_batch_successful_isSet = false;
    m_is_batch_successful_isValid = false;
}

void OAIImageCreateSummary::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageCreateSummary::fromJsonObject(QJsonObject json) {

    m_images_isValid = ::OpenAPI::fromJsonValue(m_images, json[QString("images")]);
    m_images_isSet = !json[QString("images")].isNull() && m_images_isValid;

    m_is_batch_successful_isValid = ::OpenAPI::fromJsonValue(m_is_batch_successful, json[QString("isBatchSuccessful")]);
    m_is_batch_successful_isSet = !json[QString("isBatchSuccessful")].isNull() && m_is_batch_successful_isValid;
}

QString OAIImageCreateSummary::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageCreateSummary::asJsonObject() const {
    QJsonObject obj;
    if (m_images.size() > 0) {
        obj.insert(QString("images"), ::OpenAPI::toJsonValue(m_images));
    }
    if (m_is_batch_successful_isSet) {
        obj.insert(QString("isBatchSuccessful"), ::OpenAPI::toJsonValue(m_is_batch_successful));
    }
    return obj;
}

QList<OAIImageCreateResult> OAIImageCreateSummary::getImages() const {
    return m_images;
}
void OAIImageCreateSummary::setImages(const QList<OAIImageCreateResult> &images) {
    m_images = images;
    m_images_isSet = true;
}

bool OAIImageCreateSummary::is_images_Set() const{
    return m_images_isSet;
}

bool OAIImageCreateSummary::is_images_Valid() const{
    return m_images_isValid;
}

bool OAIImageCreateSummary::isIsBatchSuccessful() const {
    return m_is_batch_successful;
}
void OAIImageCreateSummary::setIsBatchSuccessful(const bool &is_batch_successful) {
    m_is_batch_successful = is_batch_successful;
    m_is_batch_successful_isSet = true;
}

bool OAIImageCreateSummary::is_is_batch_successful_Set() const{
    return m_is_batch_successful_isSet;
}

bool OAIImageCreateSummary::is_is_batch_successful_Valid() const{
    return m_is_batch_successful_isValid;
}

bool OAIImageCreateSummary::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_images.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_batch_successful_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageCreateSummary::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
