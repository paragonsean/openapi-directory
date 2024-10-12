/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICryptoPaymentQRCode.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICryptoPaymentQRCode::OAICryptoPaymentQRCode(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICryptoPaymentQRCode::OAICryptoPaymentQRCode() {
    this->initializeModel();
}

OAICryptoPaymentQRCode::~OAICryptoPaymentQRCode() {}

void OAICryptoPaymentQRCode::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_output_isSet = false;
    m_output_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_style_isSet = false;
    m_style_isValid = false;
}

void OAICryptoPaymentQRCode::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICryptoPaymentQRCode::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_output_isValid = ::OpenAPI::fromJsonValue(m_output, json[QString("output")]);
    m_output_isSet = !json[QString("output")].isNull() && m_output_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_style_isValid = ::OpenAPI::fromJsonValue(m_style, json[QString("style")]);
    m_style_isSet = !json[QString("style")].isNull() && m_style_isValid;
}

QString OAICryptoPaymentQRCode::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICryptoPaymentQRCode::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_image.isSet()) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_output.isSet()) {
        obj.insert(QString("output"), ::OpenAPI::toJsonValue(m_output));
    }
    if (m_size.isSet()) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_style.isSet()) {
        obj.insert(QString("style"), ::OpenAPI::toJsonValue(m_style));
    }
    return obj;
}

OAICryptoPaymentData OAICryptoPaymentQRCode::getData() const {
    return m_data;
}
void OAICryptoPaymentQRCode::setData(const OAICryptoPaymentData &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAICryptoPaymentQRCode::is_data_Set() const{
    return m_data_isSet;
}

bool OAICryptoPaymentQRCode::is_data_Valid() const{
    return m_data_isValid;
}

OAIEmbeddedImage OAICryptoPaymentQRCode::getImage() const {
    return m_image;
}
void OAICryptoPaymentQRCode::setImage(const OAIEmbeddedImage &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAICryptoPaymentQRCode::is_image_Set() const{
    return m_image_isSet;
}

bool OAICryptoPaymentQRCode::is_image_Valid() const{
    return m_image_isValid;
}

OAIOutputFile OAICryptoPaymentQRCode::getOutput() const {
    return m_output;
}
void OAICryptoPaymentQRCode::setOutput(const OAIOutputFile &output) {
    m_output = output;
    m_output_isSet = true;
}

bool OAICryptoPaymentQRCode::is_output_Set() const{
    return m_output_isSet;
}

bool OAICryptoPaymentQRCode::is_output_Valid() const{
    return m_output_isValid;
}

OAISize OAICryptoPaymentQRCode::getSize() const {
    return m_size;
}
void OAICryptoPaymentQRCode::setSize(const OAISize &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAICryptoPaymentQRCode::is_size_Set() const{
    return m_size_isSet;
}

bool OAICryptoPaymentQRCode::is_size_Valid() const{
    return m_size_isValid;
}

OAIStyle OAICryptoPaymentQRCode::getStyle() const {
    return m_style;
}
void OAICryptoPaymentQRCode::setStyle(const OAIStyle &style) {
    m_style = style;
    m_style_isSet = true;
}

bool OAICryptoPaymentQRCode::is_style_Set() const{
    return m_style_isSet;
}

bool OAICryptoPaymentQRCode::is_style_Valid() const{
    return m_style_isValid;
}

bool OAICryptoPaymentQRCode::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_image.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_output.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_size.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_style.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICryptoPaymentQRCode::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_isValid && true;
}

} // namespace OpenAPI
