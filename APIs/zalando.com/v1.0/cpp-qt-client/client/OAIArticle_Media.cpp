/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArticle_Media.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArticle_Media::OAIArticle_Media(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArticle_Media::OAIArticle_Media() {
    this->initializeModel();
}

OAIArticle_Media::~OAIArticle_Media() {}

void OAIArticle_Media::initializeModel() {

    m_images_isSet = false;
    m_images_isValid = false;
}

void OAIArticle_Media::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArticle_Media::fromJsonObject(QJsonObject json) {

    m_images_isValid = ::OpenAPI::fromJsonValue(m_images, json[QString("images")]);
    m_images_isSet = !json[QString("images")].isNull() && m_images_isValid;
}

QString OAIArticle_Media::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArticle_Media::asJsonObject() const {
    QJsonObject obj;
    if (m_images.size() > 0) {
        obj.insert(QString("images"), ::OpenAPI::toJsonValue(m_images));
    }
    return obj;
}

QList<OAIArticle_Image> OAIArticle_Media::getImages() const {
    return m_images;
}
void OAIArticle_Media::setImages(const QList<OAIArticle_Image> &images) {
    m_images = images;
    m_images_isSet = true;
}

bool OAIArticle_Media::is_images_Set() const{
    return m_images_isSet;
}

bool OAIArticle_Media::is_images_Valid() const{
    return m_images_isValid;
}

bool OAIArticle_Media::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_images.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArticle_Media::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_images_isValid && true;
}

} // namespace OpenAPI
