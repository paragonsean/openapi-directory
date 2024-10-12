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

/*
 * OAIContactQRCodeMetadata.h
 *
 * 
 */

#ifndef OAIContactQRCodeMetadata_H
#define OAIContactQRCodeMetadata_H

#include <QJsonObject>

#include "OAIContactData.h"
#include "OAIEmbeddedImageMultipart.h"
#include "OAIOutputFile.h"
#include "OAISizeMultipart.h"
#include "OAIStyle.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContactData;
class OAIEmbeddedImageMultipart;
class OAIOutputFile;
class OAISizeMultipart;
class OAIStyle;

class OAIContactQRCodeMetadata : public OAIObject {
public:
    OAIContactQRCodeMetadata();
    OAIContactQRCodeMetadata(QString json);
    ~OAIContactQRCodeMetadata() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIContactData getData() const;
    void setData(const OAIContactData &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    OAIEmbeddedImageMultipart getImage() const;
    void setImage(const OAIEmbeddedImageMultipart &image);
    bool is_image_Set() const;
    bool is_image_Valid() const;

    OAIOutputFile getOutput() const;
    void setOutput(const OAIOutputFile &output);
    bool is_output_Set() const;
    bool is_output_Valid() const;

    OAISizeMultipart getSize() const;
    void setSize(const OAISizeMultipart &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    OAIStyle getStyle() const;
    void setStyle(const OAIStyle &style);
    bool is_style_Set() const;
    bool is_style_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIContactData m_data;
    bool m_data_isSet;
    bool m_data_isValid;

    OAIEmbeddedImageMultipart m_image;
    bool m_image_isSet;
    bool m_image_isValid;

    OAIOutputFile m_output;
    bool m_output_isSet;
    bool m_output_isValid;

    OAISizeMultipart m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    OAIStyle m_style;
    bool m_style_isSet;
    bool m_style_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContactQRCodeMetadata)

#endif // OAIContactQRCodeMetadata_H
