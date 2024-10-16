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

#include "OAIInputImage.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInputImage::OAIInputImage(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInputImage::OAIInputImage() {
    this->initializeModel();
}

OAIInputImage::~OAIInputImage() {}

void OAIInputImage::initializeModel() {

    m_base64_isSet = false;
    m_base64_isValid = false;

    m_id_pic_isSet = false;
    m_id_pic_isValid = false;

    m_svg_anim_isSet = false;
    m_svg_anim_isValid = false;

    m_url_source_isSet = false;
    m_url_source_isValid = false;
}

void OAIInputImage::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInputImage::fromJsonObject(QJsonObject json) {

    m_base64_isValid = ::OpenAPI::fromJsonValue(m_base64, json[QString("base64")]);
    m_base64_isSet = !json[QString("base64")].isNull() && m_base64_isValid;

    m_id_pic_isValid = ::OpenAPI::fromJsonValue(m_id_pic, json[QString("id_pic")]);
    m_id_pic_isSet = !json[QString("id_pic")].isNull() && m_id_pic_isValid;

    m_svg_anim_isValid = ::OpenAPI::fromJsonValue(m_svg_anim, json[QString("svg_anim")]);
    m_svg_anim_isSet = !json[QString("svg_anim")].isNull() && m_svg_anim_isValid;

    m_url_source_isValid = ::OpenAPI::fromJsonValue(m_url_source, json[QString("url_source")]);
    m_url_source_isSet = !json[QString("url_source")].isNull() && m_url_source_isValid;
}

QString OAIInputImage::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInputImage::asJsonObject() const {
    QJsonObject obj;
    if (m_base64_isSet) {
        obj.insert(QString("base64"), ::OpenAPI::toJsonValue(m_base64));
    }
    if (m_id_pic_isSet) {
        obj.insert(QString("id_pic"), ::OpenAPI::toJsonValue(m_id_pic));
    }
    if (m_svg_anim_isSet) {
        obj.insert(QString("svg_anim"), ::OpenAPI::toJsonValue(m_svg_anim));
    }
    if (m_url_source_isSet) {
        obj.insert(QString("url_source"), ::OpenAPI::toJsonValue(m_url_source));
    }
    return obj;
}

QString OAIInputImage::getBase64() const {
    return m_base64;
}
void OAIInputImage::setBase64(const QString &base64) {
    m_base64 = base64;
    m_base64_isSet = true;
}

bool OAIInputImage::is_base64_Set() const{
    return m_base64_isSet;
}

bool OAIInputImage::is_base64_Valid() const{
    return m_base64_isValid;
}

QString OAIInputImage::getIdPic() const {
    return m_id_pic;
}
void OAIInputImage::setIdPic(const QString &id_pic) {
    m_id_pic = id_pic;
    m_id_pic_isSet = true;
}

bool OAIInputImage::is_id_pic_Set() const{
    return m_id_pic_isSet;
}

bool OAIInputImage::is_id_pic_Valid() const{
    return m_id_pic_isValid;
}

QString OAIInputImage::getSvgAnim() const {
    return m_svg_anim;
}
void OAIInputImage::setSvgAnim(const QString &svg_anim) {
    m_svg_anim = svg_anim;
    m_svg_anim_isSet = true;
}

bool OAIInputImage::is_svg_anim_Set() const{
    return m_svg_anim_isSet;
}

bool OAIInputImage::is_svg_anim_Valid() const{
    return m_svg_anim_isValid;
}

QString OAIInputImage::getUrlSource() const {
    return m_url_source;
}
void OAIInputImage::setUrlSource(const QString &url_source) {
    m_url_source = url_source;
    m_url_source_isSet = true;
}

bool OAIInputImage::is_url_source_Set() const{
    return m_url_source_isSet;
}

bool OAIInputImage::is_url_source_Valid() const{
    return m_url_source_isValid;
}

bool OAIInputImage::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base64_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_pic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_svg_anim_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_source_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIInputImage::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
